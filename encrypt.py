import os

def encrypt_image(path, key):
    # Print the path of the image file and encryption key
    print('Path of the file:', path)
    print('Key for encryption:', key)

    try:
        # Open the file for reading
        with open(path, 'rb') as file:
            # Read the image data
            image = bytearray(file.read())

        # Perform XOR operation on each value of the bytearray
        encrypted_image = bytearray([value ^ key for value in image])

        # Create a new file name for the encrypted image
        directory, filename = os.path.split(path)
        encrypted_filename = 'encrypted_' + filename

        # Write the encrypted data to a new file
        encrypted_path = os.path.join(directory, encrypted_filename)
        with open(encrypted_path, 'wb') as file:
            file.write(encrypted_image)

        print('Encryption completed. Encrypted image saved as:', encrypted_path)
    except IOError:
        print('Error: An error occurred while encrypting the image.')

