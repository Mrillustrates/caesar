import webapp2

rot_form = """
<html>
<head>
<title> Hello </title>
</head>
<body>
<form action="/" method = "post">
<label>Rotations
 	<input type = "number" name = "rotate_num">
 	</label>
    <br>
 <textarea rows="4" cols="50" name="comment">
 </textarea>
 <input type="submit" value = "Rotate text"/>
 </form>
 </body>
 </html>
 """


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(rot_form)

    def rotate_character(self,text, rot):
        small_alpha = "abcdefghijklmnopqrstuvwxyz"  # reference var for small abcs
        big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # reference variable for BIG ABCS
        new_pos = 0                                 # for new position after rotation
        new_alpha = ""                             #container variable
        punctuation =".?:,/;'{=}[]\|!`~@#$%^&*()_+*-<>"
        numbers ="0123456789"

        for c in text:
            if c in big_alpha:
                new_pos = (big_alpha.index(c) + rot) % 26    #implement previous function to return alpha position + rot % letters in alpha
                new_alpha = new_alpha + big_alpha[new_pos]
            if c in small_alpha:
                new_pos = (small_alpha.index(c) + rot) % 26
                new_alpha = new_alpha + small_alpha[new_pos]
            if c in punctuation:
                new_alpha = new_alpha + c
            if c in numbers:
                new_alpha = new_alpha + c
            if c == ' ':
                new_alpha = new_alpha + c
        return new_alpha

    def post(self):
        new_text = self.request.get('comment')
        new_rotate = self.request.get('rotate_num')
        true_text = self.rotate_character(new_text, int(new_rotate))


        self.response.write(true_text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
