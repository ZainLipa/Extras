def generate_permutations(elements):
    if len(elements) == 1:
        return [elements]

    permutations = []
    for i in range(len(elements)):
        remaining_elements = elements[:i] + elements[i+1:]
        for permutation in generate_permutations(remaining_elements):
            permutations.append([elements[i]] + permutation)

    return permutations

# Example usage
input_list = [1, 2, 3]

permutations = generate_permutations(input_list)
for permutation in permutations:
    print(permutation)
