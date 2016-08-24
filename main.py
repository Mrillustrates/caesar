from helpers import alphabet_position, rotate_character
import webapp2

from sys import argv, exit

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Rotating Characters</title>
</head>
<body>
    <h1>Rotator Application</h1>
"""

page_footer = """
</body>
</html>
"""


#def user_input_is_valid(cl_args):

 #  if len(cl_args) == 2:
#        if cl_args[1].isdigit():
#            return True
#        else:
#            return False
 #  else:
#        return False


rot_form = """

<form action="/" method = "post" id="usrform">
<label id = "rotate"> Number of Rotations
        <input type = "text" value = "0" form = "usrform">
        </label>
        <br>
    <textarea rows="4" cols="50" name="comment" form="usrform">
        </textarea>
        <input type="submit" value = "Rotate it"/>
</form>
"""
query = page_header + rot_form + page_footer
self.response.write(query)

def alphabet_position(letter):
    small_alpha = "abcdefghijklmnopqrstuvwxyz"
    big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"+


    for char in letter:
        if char in small_alpha:
            position = small_alpha.index(char)
        if char in big_alpha:
            position = big_alpha.index(char)
    return position

def rotate_character(char, rot):
    small_alpha = "abcdefghijklmnopqrstuvwxyz"  # reference var for small abcs
    big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # reference variable for BIG ABCS
    new_pos = 0                                 # for new position after rotation
    new_alpha = " "                             #container variable
    punctuation =".?:,/;'{=}[]\|!`~@#$%^&*()_+*-<>"
    numbers ="0123456789"

    if char in big_alpha:
        new_pos = (alphabet_position(char) + rot) % 26    #implement previous function to return alpha position + rot % letters in alpha
        new_alpha = big_alpha[new_pos]
    if char in small_alpha:
        new_pos = (alphabet_position(char) + rot) % 26
        new_alpha = small_alpha[new_pos]
    if char in punctuation:
        new_alpha = char
    if char in numbers:
        new_alpha = char
    return new_alpha



def encrypt(text, rot):
    small_alpha = "abcdefghijklmnopqrstuvwxyz"  # reference var for small abcs
    big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation =".?:,/;'}[{=]\|!`~@#$%^&*()_+*-<>"
    number = "0123456789"
    last_pos = 0
    last_alpha = ""

    for char in text:
        if char in small_alpha:
            last_alpha = last_alpha + rotate_character(char, rot)
        if char in big_alpha:
            lasdt_alpha = last_alpha + rotate_character(char,rot)
        if char == " ":
            last_alpha = last_alpha + char
        if char in punctuation:
            last_alpha = last_alpha + char
        if char in number:
            last_alpha = last_alpha + char
    return last_alpha

class MainPage(webbapp2.RequestHandler):
    """Handles rotation requests """

    def get(self):
        self.request.out.write(rot_form)

    def post(self):
        alpha_pos = alphabet_position(self.request.get('letter'))
        rot_char = rotate_character(self.request.get('char','rot'))
        encryption = encrypt(self.request.get('text','rot'))

        self.response.out.write(last_alpha)

        #cipher_response = page_header + rot_form + page_footer






app = webapp2.WSGIApplication([
    ('/', MainPage),

], debug=True)

#user_input_is_valid(argv)

#if user_input_is_valid(argv) == False:
#    print("usage: python3 caesar.py n")
#    exit()

#message_request = input("Enter a message.")

#rotation_request = int(argv[1])

#print(encrypt(message_request, rotation_request))
