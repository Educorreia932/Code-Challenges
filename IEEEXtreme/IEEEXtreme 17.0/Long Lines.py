n, h0, a, c, q = (int(x) for x in input().split())

def calculate_heights(start_height, n):
    heights = [start_height]

    for i in range(1, n):
        height = (a * heights[i - 1] + c) % q
        
        heights.append(height)

    return heights

def noticeable_people(heights):
    total = 0

    for i in range(1, len(heights)):
        total += 1
        highest = heights[i - 1]

        for j in range(i - 2, -1, -1):
            if heights[j] > highest:
                highest = heights[j]

                total += 1
    
    return total

heights = calculate_heights(h0, n)
print(noticeable_people(heights))
