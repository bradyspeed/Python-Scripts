# User generated GUID module - prompts user input for (1) GUID character length and (2) number of GUIDs generated.

import random
import string

def user_generated_id(length):
    return ''.join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k = length
        )
    )

num_of_char = int(input('Enter number of characters in user ID:'))
num_user_id = int(input('Enter number of user IDs to create: '))
for number in range(num_user_id):
    print(user_generated_id(num_of_char))