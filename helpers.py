
import string
import re

#def valid_username(username):
#    if username.isalpha():
#        nameLength = len(username)
#        if nameLength > 3:
#            return

#def valid_password(psw):
#    for char in psw:
#        if char.isalpha() and char.isdigit():

def valid_verifypsw(psw, vpsw):
    if psw == vpsw:
        return vpsw

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PSW_RE = re.compile(r"^.{3,20}$")
def valid_password(psw):
    return PSW_RE.match(psw)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)
