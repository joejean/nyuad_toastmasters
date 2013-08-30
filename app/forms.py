from flask.ext.wtf import Form, HiddenField, TextField
from flask.ext.wtf import Required, Length

class SignupForm(Form):
    netID = TextField('netID',validators = [Required("Please enter your netID.")])
    name = TextField('name',validators = [Required("Please enter your name. ")])

class AdminForm(Form):
    netID = TextField('netID',validators = [Required("Please enter your netID.")])
    name = TextField('name',validators = [Required("Please enter your name. ")])
    password = TextField('password',validators = [Required("Please enter your password.")])

    
   
