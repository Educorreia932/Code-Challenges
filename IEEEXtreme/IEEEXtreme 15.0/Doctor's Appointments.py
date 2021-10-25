cases = int(input())


def min_index(values):
    return min(range(len(values)), key=values.__getitem__)


for case_no in range(cases):
    n_patients = int(input())
    sched = []
    
    for patient in range(n_patients):
        sched.append(tuple([patient] + [int(n) for n in input().split()]))

    sched.sort(key=lambda e: e[1])  # Sort by start
    sched.sort(key=lambda e: e[2])  # Sort by finish

    patient_order = []
    is_possible = True

    for i in range(n_patients):
        cur_day = i + 1

        for j in range(n_patients - i):
            p = sched[j]  # patient
            if cur_day > p[2]:
                is_possible = False
                break
            if cur_day >= p[1]:
                patient_order.append(p[0])
                del sched[j]

                break
        else:
            is_possible = False

        if not is_possible:
            break

    if not is_possible:
        print('impossible')

    else:
        for n in patient_order:
            print(n + 1, end=' ')

        print()
