

import pywhatkit as kt

print("Let's Automate Whatsapp!")
p_num = 'the taget phone number goes here!'

#or you can use getpass module to capture cell num
import getpass as gp


'''msg = "scheduled msg,Plz ignore"'''
kt.sendwhatmsg("+91 9971294994", "scheduled msg,Plz ignore", 14,18)