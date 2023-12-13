import os
from encrypt import encrypt_image
from decrypt import decrypt_image

def get_user_choice():
    """
    Displays menu options and gets user choice.

    :return: User's choice (integer).
    """
    print("For image encryption choose 1")
    print("For image decryption choose 2")
    print("To exit choose 3")

    try:
        choice = int(input('Enter your choice: '))
        return choice
    except ValueError:
        print('Error: Please enter a valid integer.')
        return 0

def starter():
    while True:
        choice = get_user_choice()

        if choice == 3:
            break
        elif choice in [1, 2]:
            # Take user input for the image path and key
            image_path = input('Enter the path of the image: ')

            # Check if the provided path is valid
            if not os.path.isfile(image_path):
                print('Error: Invalid file path.')
                continue

            key = int(input('Enter the key: '))

            if choice == 1:
                # Encrypt the image
                encrypt_image(image_path, key)
            elif choice == 2:
                # Decrypt the image
                decrypt_image(image_path, key)
        else:
            print("Invalid choice. Please choose 1 for encryption, 2 for decryption, or 3 to exit.")