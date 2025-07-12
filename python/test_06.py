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

def generate_plain_text(plain_text=None):
    """
    Generates a plain text string for testing purposes.
    Returns:
        str: The plain text string.
    """
    if not plain_text:
        plain_text = "This is a test string for the cypher matrix and key generation."
    
    return plain_text

def prepare_plain_text(plain_text):
    """
    Prepares the plain text by removing non-alphabetic characters and converting it to uppercase.
    Args:
        plain_text (str): The input plain text.
    Returns:
        str: The processed plain text, with non-alphabetic characters removed and converted to uppercase.
    """
    # Replace non-alphabetic characters with spaces
    for char in plain_text:
        if not char.isalpha():
            plain_text = plain_text.replace(char, ' ')
    
    # Remove spaces and convert to uppercase
    plain_text = plain_text.replace(' ', '').upper()
    
    return plain_text

def generate_encryption_key(cypher_key=None, plain_text=None):
    """
    Generates an encryption key for the Vigenère cipher by repeating or truncating the given cypher key to match the length of the prepared plain text.
    Args:
        cypher_key (str, optional): The key used for encryption. If not provided, a new cypher key is generated.
        plain_text (str, optional): The text to be encrypted. If not provided, a new plain text is generated.
    Returns:
        list: A list of characters representing the encryption key, aligned with the length of the prepared plain text.
    Notes:
        - The plain text is preprocessed to remove non-alphabetic characters and convert it to uppercase.
        - The cypher key is repeated as necessary to match the length of the prepared plain text.
    """
    if not cypher_key:
        cypher_key = generate_cypher_key()
    
    if not plain_text:
        plain_text = generate_plain_text()

    # Prepare the plain text by removing non-alphabetic characters and converting to uppercase
    plain_text = prepare_plain_text(plain_text)

    encryption_key = []

    for i in range(len(plain_text)):

        # Calculate the index in the cypher key by using modulo operation
        # This ensures that if the plain text is longer than the cypher key,
        # the key will repeat as necessary.
        ii = i % len(cypher_key)

        encryption_key.append(cypher_key[ii])

    return encryption_key

def main():
    """
    Main function to execute the print_cypher_matrix function.
    """
    cypher_primitives = generate_cypher_primitives()    
    cypher_matrix = generate_cypher_matrix(cypher_primitives)
    cypher_key = generate_cypher_key()
    plain_text = generate_plain_text()
    encryption_key = generate_encryption_key(cypher_key, plain_text)
    print(encryption_key)

if __name__ == "__main__":
    main()