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
        matrix.append(cypher_primitives[i:] + cypher_primitives[:i])
    return matrix

def print_cypher_matrix(cypher_matrix):
    """
    This function prints the cypher matrix to the standard output.
    Each row of the matrix is printed on a new line.
    """
    for row in cypher_matrix:
        print(' '.join(row))

def main():
    """
    Main function to execute the print_cypher_matrix function.
    """
    cypher_primitives = generate_cypher_primitives()    
    cypher_matrix = generate_cypher_matrix(cypher_primitives)
    print_cypher_matrix(cypher_matrix)

if __name__ == "__main__":
    main()