import os

def decrypt_image(path, key):
    # Print the path of the image file and decryption key
    print('Path of the file:', path)
    print('Key for decryption:', key)

    try:
        # Open the file for reading
        with open(path, 'rb') as file:
            # Read the image data
            image = bytearray(file.read())

        # Perform XOR operation on each value of the bytearray
        decrypted_image = bytearray([value ^ key for value in image])

        # Create a new file name for the decrypted image
        directory, filename = os.path.split(path)
        decrypted_filename = 'decrypted_' + filename

        # Write the decrypted data to a new file
        decrypted_path = os.path.join(directory, decrypted_filename)
        with open(decrypted_path, 'wb') as file:
            file.write(decrypted_image)

        print('Decryption completed. Decrypted image saved as:', decrypted_path)

    except IOError:
        print('Error: An error occurred while decrypting the image.')

    except Exception as e:
        print('Error caught:', type(e).__name__)
