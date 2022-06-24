# Who is using this script have the 100% of responsabilities and aftermath about their actions.

# (@u@) scripted by Skripto (@YourAnonSkripto) (@u@)

#      " Keyboard is more powerful than a nuke. "


import requests, re, optparse, sys, time, colorama, os
from urllib import parse

class parameters:
    def __init__(self):
        PARSER = optparse.OptionParser()
        PARSER.add_option('-u', metavar='example.ex', dest='URL', help='Enter the URL without the http/s!')
        PARSER.add_option('-s', action='store_true', dest='HTTPSORNOT', help='Enter this option for HTTPS protocol.')
        self.OPTS, ARGS = PARSER.parse_args()

        self.check_parameters()
        COMPLETE_URL = self.PROTOCOL + self.OPTS.URL
        crawler(COMPLETE_URL)

    def check_parameters(self):
        if not self.OPTS.URL:
            print(colorama.Back.RED+'\nPlease type "--help" for more informations. <Specify the protocol "-u"> !'+colorama.Back.RESET+'\n')
            sys.exit()

        if self.OPTS.HTTPSORNOT:
            self.PROTOCOL = 'https://'
        else:
            self.PROTOCOL = 'http://'

class crawler:
    def __init__(self, URL):
        os.system('clear')
        print(
            colorama.Fore.LIGHTBLACK_EX+'''
  _________                       __                
  \_   ___ \____________ __  _  _|  |   ___________ 
  /    \  \/\_  __ \__  \\\ \/ \/ /  | _/ __ \_  __ \ 
  \     \____|  | \// __ \\\     /|  |_\  ___/|  | \/
   \______  /|__|  (____  /\/\_/ |____/\___  >__|   
          \/            \/                 \/       \033[39mSkripto \033[39m(\033[91m@\033[39mu\033[91m@\033[39m)
            '''+colorama.Fore.RESET
        )

        self.URL = URL
        print('\n Target ='+colorama.Fore.CYAN,URL+colorama.Fore.RESET)
        
        try:
            self.RESPONSE = requests.get(URL)
        except:
            os.system('clear')
            print('\nUnable to find "'+colorama.Fore.CYAN+URL+colorama.Fore.RESET+'".\n')
            sys.exit()
        if self.RESPONSE.status_code == 200:
            print(' Check live:'+colorama.Fore.GREEN+' True'+colorama.Fore.RESET)
        else:
            print(' Check live:'+colorama.Fore.RED+' False'+colorama.Fore.RESET+'\n')
            sys.exit()

        time.sleep(1)
        print('\n Loading ...')
        time.sleep(1)

        self.link_extractor()
        print(colorama.Fore.LIGHTYELLOW_EX)
        self.result_printer()
        if len(self.LINKLISTTW) == 0:
            print('\n No links have been found.\n'+colorama.Fore.RESET)
            sys.exit()    

        print(colorama.Fore.RESET)
        self.link_saver()

    def link_extractor(self):
        self.LINKLIST = re.findall('(?:href=")(.*?)"', self.RESPONSE.content.decode())

    def result_printer(self):
        self.LINKLISTTW = []
        for LINK in self.LINKLIST:
            LINK = parse.urljoin(self.URL, LINK)

            if self.URL in LINK:
                print(' ',LINK)
                self.LINKLISTTW.append(LINK)

    def link_saver(self):
        NUM = 1
        try:
            while True:
                
                FILE_NAME = self.URL.split('/')[2]+'-'+str(NUM)+'.txt'
                with open(FILE_NAME,'r') as CHECK_FILE:
                    CHECK_FILE.close()
                NUM += 1
        except:
            with open(self.URL.split('/')[2]+'-'+str(NUM)+'.txt','w') as FILE:
                for LINK in self.LINKLISTTW:
                    FILE.write(LINK+'\n')
                FILE.close()
                
parameters()
