def find_requested_recipe(message):
    recipe_counts = {letter: 0 for letter in 'abcdefg'}

    for char in message:
        if char in recipe_counts:
            recipe_counts[char] += 1

    requested_recipe = max(recipe_counts, key=recipe_counts.get)
    return requested_recipe.upper()


n = int(input())

for _ in range(n):
    message = input()
    recipe = find_requested_recipe(message)
    print(recipe)
