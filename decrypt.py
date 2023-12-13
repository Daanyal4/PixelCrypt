import os

def decrypt_image(path, key):
    """
    Decrypts an image file using XOR operation with the given key.

    :param path: Path to the encrypted image file.
    :param key: Decryption key (integer).
    """
    # Print the path of the image file and decryption key
    print('Path of the file:', path)
    print('Key for decryption:', key)

    try:
        # Open the file for reading
        with open(path, 'rb') as file:
            # Read the image data
            encrypted_image = bytearray(file.read())

        # Perform XOR operation on each value of the bytearray
        decrypted_image = bytearray([value ^ key for value in encrypted_image])

        # Create a new file name for the decrypted image
        directory, filename = os.path.split(path)
        decrypted_filename = 'decrypted_' + filename

        # Write the decrypted data to a new file
        decrypted_path = os.path.join(directory, decrypted_filename)
        with open(decrypted_path, 'wb') as file:
            file.write(decrypted_image)

        print('Decryption completed. Decrypted image saved as:', decrypted_path)

    except IOError as e:
        print(f'Error: An error occurred while decrypting the image. {e}')

    except Exception as e:
        print(f'Error caught: {type(e).__name__} - {e}')
