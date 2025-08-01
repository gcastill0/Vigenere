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

def generate_cypher_key(cypher_key = None):
    """
    Generates a formatted cipher key for use in encryption algorithms.
    If the provided `cypher_key` is empty or None, a default key 
    ('correct horse battery staple') is used. 

    All spaces are removed from the key and the result is converted to uppercase.
    
    Args:
        cypher_key (str): The input cipher key. Can be None or an empty string.
    Returns:
        str: The processed cipher key, with spaces removed and all letters in uppercase.
    """
    if not cypher_key:
        cypher_key = 'correct horse battery staple!'

    # Replace non-alphabetic characters with spaces
    for char in cypher_key:
        if not char.isalpha():
            cypher_key = cypher_key.replace(char, ' ')
    
    # Remove spaces and convert to uppercase
    cypher_key = cypher_key.replace(' ', '').upper()
    
    return cypher_key

def main():
    """
    Main function to execute the print_cypher_matrix function.
    """
    cypher_primitives = generate_cypher_primitives()    
    cypher_matrix = generate_cypher_matrix(cypher_primitives)
    cypher_key = generate_cypher_key()
    print(cypher_key)

if __name__ == "__main__":
    main()