def solution(area):
    result = []

    while area > 0:
        biggest_square_area = (int(area ** 0.5)) ** 2
        area -= biggest_square_area

        result.append(biggest_square_area)

    return result
