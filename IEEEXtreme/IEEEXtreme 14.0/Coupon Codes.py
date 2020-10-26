COUPON_LENGTH = 12 # Length without hyphens

def similar(chaine1, chaine2):
    counter = 0

    for i in range(COUPON_LENGTH):
        if chaine1[i] != chaine2[i]:
            counter += 1

        if counter > 1:
            return False

    return True

N = int(input()) # Number of coupon code

coupons = []

for i in range(N):
    coupons.append(input().replace("-", ""))

counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if similar(coupons[i], coupons[j]):
            counter += 1

print(counter)