def generate_cypher_primitives():
    """
    Generates a list of cypher primitives, which are uppercase letters from A to Z.
    Returns:
        list: The list of cypher primitives.
    """
    primitives = []

    # Iterate through the ASCII values of uppercase letters A to Z
    # and append each letter to the list of primitives.
    for letter in range(ord('A'), ord('Z') + 1):
        primitives.append(chr(letter))

    return primitives

def generate_cypher_matrix(cypher_primitives):
    """
    Generates a matrix of cypher primitives by rotating the list of uppercase letters.
    Each row in the matrix is a rotated version of the previous row.
    Returns:
        list: The cypher matrix.
    """

    matrix = []
    for i in range(len(cypher_primitives)):
        
        left_part = []
        right_part = []

        for j in range(0, i):
            left_part.append(cypher_primitives[j])

        for k in range(i, len(cypher_primitives)):
            right_part.append(cypher_primitives[k])
        
        matrix.append(right_part + left_part)

    for row in matrix:
        print(' '.join(row))

    return matrix

def main():
    """
    Main function to execute the generate_cypher_primitives function.
    """
    cypher_primitives = generate_cypher_primitives()
    cypher_matrix = generate_cypher_matrix(cypher_primitives)

if __name__ == "__main__":
    main()