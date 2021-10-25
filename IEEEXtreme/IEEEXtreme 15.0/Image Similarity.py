def similitary(image_1, image_2, offset):
    result = 0

    for i in range(len(image_1)):
        for j in range(len(image_1[0])):
            x = j + offset[0]
            y = i + offset[1]

            if (0 <= x < len(image_1[0]) and 0 <= y < len(image_1)
                    and 0 <= j < len(image_2[0]) and 0 <= i < len(image_2)
                    and image_1[y][x] == image_2[i][j] == 1):
                result += 1

    return result


def rotate_anticlockwise(image):
    return list(zip(*image))[::-1]


def rotate_clockwise(image):
    return list(zip(*image[::-1]))


def horizontal_flip(image):
    return list(reversed(image[1:])) + [image[0]]


def vertical_flip(image):
    return horizontal_flip(rotate_clockwise(rotate_clockwise(image)))


def get_neighbors(image, offset):
    x = offset[0]
    y = offset[1]

    directions = (
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0)
    )

    # Translate in any direction
    for direction in directions:
        direction_offset = (offset[0] + direction[0], offset[1] + direction[1])

        yield (image, direction_offset)

    # Rotate anticlockwise
    yield (rotate_anticlockwise(image), offset)

    # Rotate clockwise
    yield (rotate_clockwise(image), offset)

    # Flip horizontally
    yield (horizontal_flip(image), offset)

    # Flip vertically
    yield (vertical_flip(image), offset)


result = 0
states = set()


def bfs(image_1, image_2, offset):
    global result

    state = (tuple(image_1), offset)

    if state in states \
            or offset[0] <= -len(image_1) or offset[0] >= len(image_1) \
            or offset[1] <= -len(image_1[0]) or offset[1] >= len(image_1[0]):
        return

    states.add(state)

    neighbors = get_neighbors(image_1, offset)

    for neighbor in neighbors:
        s = similitary(neighbor[0], image_2, neighbor[1])

        if s > result:
            result = s

        bfs(neighbor[0], image_2, neighbor[1])


def main():
    T = int(input())  # Number of test cases

    for t in range(T):
        images = []
        offset = (0, 0)

        global result
        result = 0

        # Each test case has two images
        for _ in range(2):
            # Numbers of lines and columns
            R = int(input().split()[0])
            image = []

            for i in range(R):
                line = tuple(0 if x == "." else 1 for x in input())
                image.append(line)

            images.append(image)

        bfs(*images, offset)

        print(result)


main()
