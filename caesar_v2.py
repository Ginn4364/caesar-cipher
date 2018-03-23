word_e = ""
shift_e = ""
word_d = ""
shift_d = ""

def encrypt(word_e, shift_e):
        word_e = word_e.lower()
        word_list = list(word_e)
        print(word_list)
        encrypt = [int(ord(x)) for x in word_list]
        print(encrypt)
        encrypt = [(x + shift_e) if x != 32 else x for x in encrypt]
        loop_back = [(97 + ((x) - 122) - 1) if x > 122 else x for x in encrypt]
        convert = [chr(x) for x in loop_back]
        result = ''.join(convert)
        print("Your encrypted message is: " + result)

def decrypt(word_d, shift_d):
        word_d = word_d.lower()
        word_list = list(word_d)
        print(word_list)
        decrypt = [int(ord(x)) for x in word_list]
        print(decrypt)
        decrypt = [(x - shift_d) if x != 32 else x for x in decrypt]
        print(decrypt)
        loop_back = [(122 + (x - 96)) if x < 97 else x for x in decrypt]
        print(loop_back)
        ignore_spaces = [(x - 26) if x == 58 else x for x in loop_back]
        print(ignore_spaces)
        convert = [chr(x) for x in ignore_spaces]
        print(convert)
        result = ''.join(convert)
        print("Your decrypted message is: " + result)


option = input("Would you like to encrypt or decrypt? ")
if option == "encrypt":
        word_e = input("Enter the message you would like to encrypt: ")
        shift_e = int(input("Enter the shift you would like your message encrypted by (from 1 to 26): "))
        encrypt(word_e, shift_e)
if option == "decrypt":
        word_d = input("Enter the message you would like to decrypt: ")
        shift_d = int(input("Enter the shift your message was encrypted by: "))

        decrypt(word_d, shift_d)

## Encrypting
##For encrypting the program converts the message to a list. Uses the int() and ord() function to get each characters
##ASCII decimal place (for example, a = 97, z = 122). Then it adds to shift to each of these "decimals" as long as
##the character is not equal to 32, which is the decimal for the whitespace character. Then if the shift makes the
##character go over 122 (which is the end of the lowercase alphabet for ASCII) the loop_back variable will bring the
##character back to the beginning of the lowercase ASCII alphabet. Then the chr() function converts them back to
##letters and then i just .join() and print()

## Decrypting
##Decrypting is more or less the same with a few key differences. The shift is subtracted from the decimal rather than
##added to it. The loop_back looks for numbers that have gone under 97 (which is the end of the ASCII lowercase alphabet)
##as opposed to the encrypting loop_back which looks for numbers that went past z. Since the spaces are under 97 I
##added another variable that simply subracts and negates the effects the loop_back variable had on them. Then it's
##chr() and .join().









