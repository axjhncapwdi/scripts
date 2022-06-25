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
        self.LINKLIST = []
        self.URL = URL

        os.system('clear')
        print(
            colorama.Fore.LIGHTBLACK_EX+'''
    _________                       __                             
    \_   ___ \____________ __  _  _|  |   ___________       __     
    /    \  \/\_  __ \__  \\\ \/ \/ /  | _/ __ \_  __ \   __|  |___ 
    \     \____|  | \// __ \\\     /|  |_\  ___/|  | \/  /__    __/ 
     \______  /|__|  (____  /\/\_/ |____/\___  >__|        |__|    Pentesting tool
            \/            \/                 \/                    
                '''+colorama.Fore.LIGHTBLACK_EX+'\n\t\t~S'+colorama.Fore.WHITE+'k'+colorama.Fore.LIGHTBLACK_EX+'ripto ('+colorama.Fore.LIGHTRED_EX+'@'+colorama.Fore.LIGHTBLACK_EX+'u'+colorama.Fore.LIGHTRED_EX+'@'+colorama.Fore.LIGHTBLACK_EX+')'+colorama.Fore.RESET)

        try:
            self.RESPONSE = requests.get(URL)
            print('\n Target ='+colorama.Fore.CYAN,URL+colorama.Fore.RESET)
            time.sleep(1)
        except:
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
        print('\n '+colorama.Back.LIGHTCYAN_EX+' '+colorama.Back.RESET+' is for primary links.\n ', end='')
        time.sleep(1)
        print(colorama.Back.LIGHTBLACK_EX+' '+colorama.Back.RESET+' is for secondary links.\n')
        time.sleep(1)
        print(colorama.Fore.WHITE+'\n Website Map:\n')
        self.result_printer(URL)
        if len(self.LINKLIST) == 0:
            print(colorama.Fore.LIGHTBLACK_EX+' No links have been found.\n'+colorama.Fore.RESET)
            sys.exit()
        print()
        self.link_saver()
        sys.exit()

    def link_extractor(self):
        self.HREF_LINKS = re.findall('(?:href=")(.*?)"', self.RESPONSE.content.decode())

    def result_printer(self, URL):
        
        LINK_COLOR = colorama.Fore.LIGHTCYAN_EX
        for LINK in self.HREF_LINKS:
            LINK = parse.urljoin(URL, LINK)

            if '#' in LINK:
                LINK_COLOR = colorama.Fore.LIGHTBLACK_EX

            if URL in LINK and LINK not in self.LINKLIST:
                self.LINKLIST.append(LINK)
                print(LINK_COLOR+' ',LINK+colorama.Fore.RESET)
                LINK_COLOR = colorama.Fore.LIGHTCYAN_EX
                self.result_printer(LINK)
                
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
                for LINK in self.LINKLIST:
                    FILE.write(' '+LINK+'\n')
                FILE.close()

parameters()
