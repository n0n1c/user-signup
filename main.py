#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import helpers

form="""
<form method='post'>
    <h1>Signup</h1>
    <br>
    <label>
        Username
        <input type="text" name="username" value="%(username)s" required>
    </label>
    <br>
    <label>
        Password
        <input type="password" name="psw" required>
    </label>
    <br>
    <label>
        Verify Password
        <input type="password" name="vpsw" required>
    </label>
    <br>
    <label>
        Email (optional)
        <input type="email" name="email" value="%(email)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <input type='submit'/>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", username="", email=""):
        self.response.out.write(form % {"error": error,
                                        "username": username,
                                        "email": email})

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get("username")
        valid_username = helpers.valid_username(username)
        password = helpers.valid_password(self.request.get("psw"))
        verify_password = helpers.valid_verifypsw(self.request.get("psw"), self.request.get("vpsw"))
        email = self.request.get("email")
        valid_email = helpers.valid_email(email)

        if not (valid_username):
            self.write_form("Please enter valid username", username, email)
        elif not (password):
            self.write_form("Please enter valid password", username, email)
        elif not (verify_password):
            self.write_form("Passwords do not match", username, email)
        else:
            self.response.out.write("Welcome, %s!" %username)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
