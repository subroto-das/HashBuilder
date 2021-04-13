# This is a hacking tool, which can coovert your password/code/plain text to Hash (Encrypted).
# This is created by Subroto Das (Tr0j@n_Pr!nc3)
# Thanks for reading...

import hashlib

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
purple = '\033[95m'
white = '\033[97m'
blue = '\033[94m'
gray = '\033[90m'

#banner of the tool
print(red + bold+"""
================================================================================================================""" + lgreen + bold + """
         _   _              _             ______         _  _      _
        | | | |            | |            | ___ \       (_)| |    | |
        | |_| |  __ _  ___ | |__   ______ | |_/ / _   _  _ | |  __| |  ___  _ __
        |  _  | / _` |/ __|| '_ \ |______|| ___ \| | | || || | / _` | / _ \| '__|
        | | | || (_| |\__ \| | | |        | |_/ /| |_| || || || (_| ||  __/| |
        \_| |_/ \__,_||___/|_| |_|        \____/  \__,_||_||_| \__,_| \___||_|
""" + purple + bold + """
                        - [ B u i l d  Y o u r  O w n  H a s h ] -
""" + yellow + """
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••""" + blue + """
Created by""" + red + bold + """ :""" + cyan + """ [ S u b r o t o   D a s ]""" + blue + """
Code name""" + red + bold + """  :""" + cyan + """ [ Tr0j@n_Pr!nc3 ]""" + yellow + """
---------------------------------------------------------------------------------------------""" + cyan + """
Team name""" + red + bold + """  :""" + blue + """ [ U n d e r w o r l d   H a c k e r s ]""" + cyan + """
We are""" + red + bold + """     :""" + blue + """ [ Tr0j@n_Pr!nc3 | D4rk_W1z@rD | Xyr!5h | bL@nk_c0nS0L3 | BL4ck_5h4d0w ]""" + yellow + """
---------------------------------------------------------------------------------------------""" + blue + """
Version""" + red + bold + """    :""" + cyan + """ [ 1.0.4 (pro) ]""" + blue + """
Date""" + red + bold + """       :""" + cyan + """ [ 16/12/2020 | 4:46 pm ]""" + yellow + """
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••""" + gray + bold+"""
...............................................................................................
""")



hashValue=input(lgreen + bold+""" ┌───────────"""+purple+"""#""" + red + bold + """ root~""" + blue + bold + """Tr0j@n_Pr!nc3 """ + yellow + bold + """ 
 |""" + red + bold + """
 |""" + yellow + bold + """
 |""" + lgreen + bold + """
 └────────────────"""+purple+"""#""" + cyan + """ Enter a string to build Hash: """)
print(yellow + "~~~~~~~~~~~~~~")

hash1=hashlib.md5()
hash1.update(hashValue.encode())
print(yellow + "┌───────────[*] MD5:    " + purple + hash1.hexdigest())


hash2=hashlib.sha1()
hash2.update(hashValue.encode())
print(red + "|" + lgreen + "───────────[*] SHA1:   " + purple + hash2.hexdigest())


hash3=hashlib.sha224()
hash3.update(hashValue.encode())
print(red + "|" + lgreen + "───────────[*] SHA224: " + purple + hash3.hexdigest())


hash4=hashlib.sha256()
hash4.update(hashValue.encode())
print(red + "|" + lgreen + "───────────[*] SHA256: " + purple + hash4.hexdigest())


hash5=hashlib.sha384()
hash5.update(hashValue.encode())
print(red + "|" + lgreen + "───────────[*] SHA384: " + purple + hash5.hexdigest())


hash6=hashlib.sha512()
hash6.update(hashValue.encode())
print(yellow + "└───────────[*] SHA512: " + purple + hash6.hexdigest())

print(yellow+"-----------")
print(white + "[!]" + lgreen + " H a s h   B u i l d e d   S u c c e s s f u l l y .")
print(yellow + "~~~~~~~~~~~~~~")
print(red+"================================================================================================================" + lgreen)
