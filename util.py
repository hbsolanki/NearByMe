
def checkMobileNumber(number):
    numberch = str(number)
    if len(numberch) == 10 and numberch.isdigit():
        if numberch[0] in ["6", "7", "8", "9"]:
            False
        else:
            return False
    else:
        return False

def checkPassWord(password):
    #len must be 8 one Capital one small One Special

    if (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "!@#$%^&*()_+{}|:\"<>?[];',./" for c in password)
    ):
        return True
    else:
        return False


        



def encodingPassWord(password):
    encoded_password = ""
    for char in password:
        ascii_val = ord(char)
        if char.isdigit():  # If character is a digit
            encoded_password += chr(
                ((ascii_val - 48 + 5) % 10) + 48
            )  # Shift by 5, considering ASCII range for digits
        elif char.isalpha():  # If character is a letter
            if char.islower():
                base = 97
            else:
                base = 65
            encoded_password += chr(
                ((ascii_val - base + 5) % 26) + base
            )  # Shift by 5, considering ASCII range for letters
        else:  # If character is a special character
            encoded_password += chr(
                ((ascii_val - 32 + 5) % 94) + 32
            )  # Shift by 5, considering ASCII range for special characters
    return encoded_password


def checkUserName(username):
    #     # Check if the username length is between 4 and 25 characters
    if not 4 <= len(username) <= 25:
        # Username length should be between 4 and 25 characters
        # return False
        # print("enter min 4 char or max 25 char")
        return False

    # Check if the username starts with a letter
    if not username[0].isalpha():
        # return False  # Username should start with a letter
        # print("starts with only alphabets")
        return False

    # Check if the username contains only alphanumeric characters
    if not username.isalnum():
        # return False  # Username should only contain alphanumeric characters
        # print("must have alpha numeric combination")
        return False

    # return True  # Username satisfies all conditions
    return True


# def checkMobileNumber(number):
#     numberch = str(number)
#     if len(numberch) == 10 and numberch.isdigit():
#         if numberch[0] in ["6", "7", "8", "9"]:
#             print("Valid phone number")
#         else:
#             print("number must starts with 6,7,8,9")
#     else:
#         print("Invalid phone number")


# # number = 9157121505
# # checkMobileNumber(number)


# def checkPassWord(password):
#     if (
#         len(password) >= 8
#         and any(c.isupper() for c in password)
#         and any(c.islower() for c in password)
#         and any(c.isdigit() for c in password)
#         and any(c in "!@#$%^&*()_+{}|:\"<>?[];',./" for c in password)
#     ):
#         print("Password is valid.")
#     else:
#         print("Password is not valid.")


# # checkPassWord("Password!")


# def encodingPassWord(password):
    # encoded_password = ""
    # for char in password:
    #     ascii_val = ord(char)
    #     if char.isdigit():  # If character is a digit
    #         encoded_password += chr(
    #             ((ascii_val - 48 + 5) % 10) + 48
    #         )  # Shift by 5, considering ASCII range for digits
    #     elif char.isalpha():  # If character is a letter
    #         if char.islower():
    #             base = 97
    #         else:
    #             base = 65
    #         encoded_password += chr(
    #             ((ascii_val - base + 5) % 26) + base
    #         )  # Shift by 5, considering ASCII range for letters
    #     else:  # If character is a special character
    #         encoded_password += chr(
    #             ((ascii_val - 32 + 5) % 94) + 32
    #         )  # Shift by 5, considering ASCII range for special characters
    # return encoded_password


# # password = "Password123!"
# # encoded_password = encodingPassWord(password)
# # print("Encoded Password:", encoded_password)


# def checkUserName(username):
#     # Check if the username length is between 4 and 25 characters
#     if not 4 <= len(username) <= 25:
#         # Username length should be between 4 and 25 characters
#         # return False
#         print("enter min 4 char or max 25 char")

#     # Check if the username starts with a letter
#     if not username[0].isalpha():
#         # return False  # Username should start with a letter
#         print("starts with only alphabets")

#     # Check if the username contains only alphanumeric characters
#     if not username.isalnum():
#         # return False  # Username should only contain alphanumeric characters
#         print("must have alpha numeric combination")

#     # return True  # Username satisfies all conditions
#     print("username is valid")


# # username = input("Enter username: ")
# # checkUserName(username)

