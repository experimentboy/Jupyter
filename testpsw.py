# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:01:05 2018

@author: Moi
"""

import requests
import sys

EMAIL = 'manager'
PASSWORD = '1234'

URL = 'https://portal.hackazon.org/challenge/8790d12b0b004695c6be24009ceaa40c/'

def main():
    # Start a session so we can have persistant cookies
    session = requests.session(config={'verbose': sys.stderr})

    # This is the form data that the page sends when logging in
    login_data = {
        'loginemail': EMAIL,
        'loginpswd': PASSWORD,
        'submit': 'login',
    }

    # Authenticate
    r = session.post(URL, data=login_data)

    # Try accessing a page that requires you to be logged in
    r = session.get('https://portal.hackazon.org/challenge/8790d12b0b004695c6be24009ceaa40c/')

if __name__ == '__main__':
    main()


