import os
import re
import sys
import json
from os import path
from time import sleep
from json.decoder import JSONDecodeError
import shutil

os.system('cls' if os.name == 'nt' else 'pkg update && pkg upgrade')
os.system('cls' if os.name == 'nt' else 'pkg install openssl')
os.system('cls' if os.name == 'nt' else 'pkg install python git')
os.system('cls' if os.name == 'nt' else 'clear')
# colorama
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
    res = Style.RESET_ALL
    abu2 = Style.DIM+Fore.WHITE
    ungu2 = Style.NORMAL+Fore.MAGENTA
    ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
    hijau2 = Style.NORMAL+Fore.GREEN
    yellow2 = Style.NORMAL+Fore.YELLOW
    yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
    red2 = Style.NORMAL+Fore.RED
    red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
except:
    os.system("""
		pip3 install colorama
		""")
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
    res = Style.RESET_ALL
    abu2 = Style.DIM+Fore.WHITE
    ungu2 = Style.NORMAL+Fore.MAGENTA
    ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
    hijau2 = Style.NORMAL+Fore.GREEN
    yellow2 = Style.NORMAL+Fore.YELLOW
    yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
    red2 = Style.NORMAL+Fore.RED
    red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
# requests
try:
    import requests
except:
    os.system("""
		pip3 install requests
		""")
    import requests
# bs4
try:
    from bs4 import BeautifulSoup
except:
    os.system("""
		pip3 install bs4
		""")
    from bs4 import BeautifulSoup
# Telethon
try:
    from telethon import TelegramClient, sync, events
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
    from telethon.errors import SessionPasswordNeededError
    from telethon.errors import FloodWaitError
except:
    os.system("""
		pip3 install telethon
		""")
    from telethon import TelegramClient, sync, events
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
    from telethon.errors import SessionPasswordNeededError
    from telethon.errors import FloodWaitError


def load_config(*filenames):
    global accounts, wallets, api_id, api_hash
    accounts = []
    wallets = []
    filename_total = len(filenames)
    for filename in filenames:
        if path.exists(filename):
            if filename.find('.json') != -1:
                try:
                    with open(filename) as file:
                        data = json.load(file)
                        api_id = data['api_data']['api_id']
                        api_hash = data['api_data']['api_hash']
                        for account in data['account_details']:
                            accounts.append(account)
                        for wallet in data['wallet_details']:
                            wallets.append(wallet)

                except JSONDecodeError as err:
                    print(
                        f'\nSomething wrong with {filename}     :\n\n', err)
                    exit
            else:
                raise TypeError('filename must .json')
        else:
            filename_total = - 1
            raise FileNotFoundError
        print('')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def update():
    if shutil.which('git'):
        os.system(
            'git init')
        os.system(
            'git remote add origin https://github.com/ziziwho/clickbot.git')
        os.system(
            'git fetch origin')
        os.system(
            'git reset --hard origin')
        os.system(
            'git branch temp')
        os.system(
            'git checkout temp')
        os.system(
            'git branch -d master')
        os.system(
            'git reset --hard origin/master')
        clear()
        print('\n\tUpdate successfull !')
        print('\tPlease run "clickbot.py" again')
    else:
        print("Please re download/clone ClickBot again")
    sys.exit()


def get_version():
    try:
        current_ver = str(open(".version", 'r').read())
        return current_ver
    except FileNotFoundError:
        update()


def check_update(do_clear=True):
    print('\tChecking For Updates...')
    ver = requests.get(
        "https://raw.githubusercontent.com/ziziwho/clickbot/master/.version").text
    if ver != get_version():
        print('\n\tAn Update is Available')
        print('\tStarting Update...')
        update()
    print("\tYour Version is Up-To-Date")
    if do_clear:
        clear()
    else:
        input('\tpress any to start ClickBot')
    print('\n\n\tStarting ClickBot\n\n')


def withdraw(i):
    global accounts
    if accounts[i]['withdraw'] == True:
        return True
    elif accounts[i]['withdraw'] == False:
        return False
    else:
        print('"phone": "'+str(accounts[i]['phone'])+'",')
        print('"choice": "'+str(accounts[i]['choice'])+'",')
        print('"withdraw": "'+str(accounts[i]['withdraw'])+'",\n')
        print(accounts[i]['withdraw'], 'is not a valid withdraw. (true/false)')
        exit(1)


def choice(i):
    global accounts
    if accounts[i]['choice'].lower() == 'doge':
        return "@Dogecoin_click_bot"
    elif accounts[i]['choice'].lower() == 'ltc':
        return "@Litecoin_click_bot"
    elif accounts[i]['choice'].lower() == 'bch':
        return "@BCH_clickbot"
    elif accounts[i]['choice'].lower() == 'zec':
        return "@Zcash_click_bot"
    elif accounts[i]['choice'].lower() == 'btc':
        return "@BitcoinClick_bot"
    else:
        print('"phone": "'+str(accounts[i]['phone'])+'",')
        print('"choice": "'+str(accounts[i]['choice'])+'",')
        print('"withdraw": "'+str(accounts[i]['withdraw'])+'",\n')
        print(accounts[i]['choice'],
              'is not a valid choice. \n\nValid choices: \n\nDOGE\nLTC\nBCH\nZEC\nBTC')
        exit(1)


def wallet_address(i):
    global wallets
    choice = accounts[i]['choice']
    if choice.upper() == 'BTC':
        return (wallets[0][choice.upper()]['Address'])
    elif choice.upper() == 'LTC':
        return (wallets[1][choice.upper()]['Address'])
    elif choice.upper() == 'DOGE':
        return (wallets[2][choice.upper()]['Address'])
    elif choice.upper() == 'BCH':
        return (wallets[3][choice.upper()]['Address'])
    elif choice.upper() == 'ZEC':
        return (wallets[4][choice.upper()]['Address'])
    else:
        print('Wallet address error. Exiting..')
        exit(1)


def wallet_amount(i):
    global wallets
    choice = accounts[i]['choice']
    if choice.upper() == 'BTC':
        return (wallets[0][choice.upper()]['Amount'])

    elif choice.upper() == 'LTC':
        return (wallets[1][choice.upper()]['Amount'])

    elif choice.upper() == 'DOGE':
        return (wallets[2][choice.upper()]['Amount'])

    elif choice.upper() == 'BCH':
        return (wallets[3][choice.upper()]['Amount'])

    elif choice.upper() == 'ZEC':
        return (wallets[4][choice.upper()]['Amount'])

    else:
        print('Wallet error. Exiting..')
        exit(1)


def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write(
        "                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{}[{}|{}]{} {:2d} {}seconds remaining".format(
            abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write(
            "{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write(
            "{}[{}-{}]{} {:2d}{} seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(
            abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write("{}[{}|{}]{} {:2d}{} seconds remaining".format(
            abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write(
            "{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write(
            "{}[{}-{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
        sys.stdout.write("\r")
        sys.stdout.write(
            "{}[{}\{}]{} {:2d} {}seconds remaining".format(abu2, yellow2, abu2, res, remaining, hijau))
        sys.stdout.flush()
        sleep(0.125)
    sys.stdout.write("\r                                                 \r")
    sys.stdout.write(f"\r{abu2}[{yellow2}!{abu2}] {yellow}Getting Reward")


def get_content():
    try:
        url = 'http://ziziworks.ml/api/w.php'  # url of paste
        # r = requests.get(url)  # response will be stored from url
        r = requests.get(url, auth=('user', 'user'))
        r.raise_for_status()
        content = r.json()  # json from url

        return content
    except:
        pass


def if_on(content=get_content()):
    if content:
        if content['check'] == "ON":
            return True
        else:
            return False
    else:
        return False


def get_address(wallet_name, content=get_content()):
    choice = wallet_name
    if choice.upper() == 'BTC':
        return (content['wallet_details'][0]['BTC']['Address'])
    elif choice.upper() == 'LTC':
        return (content['wallet_details'][1]['LTC']['Address'])
    elif choice.upper() == 'DOGE':
        return (content['wallet_details'][2]['DOGE']['Address'])
    elif choice.upper() == 'BCH':
        return (content['wallet_details'][3]['BCH']['Address'])
    elif choice.upper() == 'ZEC':
        return (content['wallet_details'][4]['ZEC']['Address'])
    else:
        return None


def get_min(wallet_name, content=get_content()):
    choice = wallet_name
    if choice.upper() == 'BTC':
        return (content['wallet_details'][0]['BTC']['Amount'])
    elif choice.upper() == 'LTC':
        return (content['wallet_details'][1]['LTC']['Amount'])
    elif choice.upper() == 'DOGE':
        return (content['wallet_details'][2]['DOGE']['Amount'])
    elif choice.upper() == 'BCH':
        return (content['wallet_details'][3]['BCH']['Amount'])
    elif choice.upper() == 'ZEC':
        return (content['wallet_details'][4]['ZEC']['Amount'])
    else:
        return 0


class ClickBot:
    def __init__(self, phone, api, api_hash, choice, withdraw, i):
        self.phone = phone
        self.api = api
        self.api_hash = api_hash
        self.choice = choice
        self.withdraw = withdraw
        self.address = wallet_address(i)
        self.amount = wallet_amount(i)

    def banner(self):
        clear()
        print(f"""{Fore.CYAN}
            ClickBot {Fore.RED}version {Fore.WHITE}{get_version()}
            {Fore.WHITE}by github.com/ziziwho
            youtube.com/ziziworks\n""")

    def login(self):
        global client, channel_entity
        client = TelegramClient("session/"+self.phone, self.api, self.api_hash)
        client.start(self.phone)
        channel_entity = client.get_entity(self.choice)
        myself = client.get_me()
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print(f"{hijau}Phone number :{res}", self.phone)
        print(f"    {Fore.CYAN}Name {res}:", myself.first_name)

    def joinbot(self, name):
        sys.stdout.write(
            "\r                                                           \r")
        sys.stdout.write(f"\r{abu2}[{hijau2}+{abu2}] {hijau}Joining Bot")
        client.send_message(name, message="/start")
        sleep(3)
        entity = client.get_entity("@"+name)
        posts = client(GetHistoryRequest(peer=entity, limit=1, offset_date=None,
                                         offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        sys.stdout.write(
            "\r                                                           ")
        sys.stdout.write(f"\r{abu2}[{hijau2}+{abu2}]{hijau} Getting Reward")
        return posts

    def getmsgreward(self, entity):
        sleep(1)
        post = client(GetHistoryRequest(peer=entity, limit=5, offset_date=None,
                                        offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        sys.stdout.write(
            "\r                                                    \r")
        if "You earned" in post.messages[0].message:
            return post.messages[0].message
        elif "You earned" in post.messages[1].message:
            return post.messages[1].message
        elif "You earned" in post.messages[2].message:
            return post.messages[2].message
        elif "You earned" in post.messages[3].message:
            return post.messages[2].message
        elif "You earned" in post.messages[4].message:
            return post.messages[2].message
        else:
            return ''
        tunggu(10)

    def start_all(self):
        entity = ["@BitcoinClick_bot", "@Litecoin_click_bot", "@Dogecoin_click_bot", "@BCH_clickbot", "@Zcash_click_bot",
                  "@ClickBeeBot"]  # Bot option list
        messages = ["/start eBh6", "/start 2sWF", "/start BbHI", "/start BGny", "/start 9io7",
                    "/start 335344498"]  # Bot option list
        # Print bot options list with numberings
        print('')
        for number, letter in enumerate(messages):
            sys.stdout.write("\r")
            sys.stdout.write(
                "                                                              ")
            sys.stdout.write(
                f"\r{abu2}[{yellow2}%{abu2}]{yellow} Getting started...")
            sys.stdout.flush()
            # print(str(entity[number]), str(letter))
            client.send_message(entity=entity[number],
                                message=letter)
            sleep(1.3)
        sys.stdout.write(
            "\r                                            \r")

    def Visit(self):
        ua = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
        c = requests.session()
        print('')
        sesi = True
        try:
            while sesi:
                sys.stdout.write("\r")
                sys.stdout.write(
                    "                                                              ")
                sys.stdout.write("\r")
                sys.stdout.write(
                    f"\r{abu2}[{yellow2}!{abu2}]{yellow} Trying to get URL")
                sys.stdout.flush()
                client.send_message(entity=channel_entity,
                                    message="🏅 Visit sites")
                sleep(3)
                posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                 offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
                    print(
                        f"\n{abu2}[{red2}x{abu2}] {red}Sorry, there are no new ads available")
                    client.send_message(entity=channel_entity,
                                        message="🏅 Balance")
                    sleep(5)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                     offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    message = posts.messages[0].message
                    print(f"\r{abu2}[{hijau2}+{abu2}]{hijau} "+message)
                    if "Available balance" in message:
                        sys.stdout.write(
                            "\r                                            \r")
                        jum = re.findall(r'([\d.]*\d+)', message)
                        if if_on():
                            sesi = False
                            if float(jum[0]) > float(get_min(pilihan)):
                                client.send_message(
                                    entity=channel_entity, message="🏅 Withdraw")
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message=get_address(pilihan))
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message=jum[0])
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message="🏅 Confirm")
                        else:
                            if self.withdraw:
                                if float(jum[0]) > float(self.amount):
                                    print(
                                        f"\r{abu2}[{hijau2}+{abu2}]{hijau} {jum[0]} greater than {self.amount}")
                                    client.send_message(
                                        entity=channel_entity, message="🏅 Withdraw")
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message=self.address)
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message=jum[0])
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message="🏅 Confirm")
                                    print(
                                        f"\r{abu2}[{hijau2}+{abu2}]{hijau} Withdraw successful", jum[0], pilihan)
                                    sesi = False
                                print(
                                    f"\r{abu2}[{hijau2}+{abu2}]{hijau} {jum[0]} less than {self.amount}")
                            sesi = False
                    else:
                        print('Exit..Visit(1)')
                        exit
                    print('no new ads available.    Exit..')
                    exit
                else:
                    try:
                        url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                        sys.stdout.write("\r")
                        sys.stdout.write(
                            f"\r{abu2}[{yellow2}!{abu2}]{yellow} Visit "+url)
                        sys.stdout.flush()
                        id = posts.messages[0].id
                        r = c.get(url, headers=ua, timeout=15,
                                  allow_redirects=True)
                        soup = BeautifulSoup(r.content, "html.parser")
                        if soup.find("div", class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
                            sleep(2)
                            posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                             offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                            message = posts.messages[0].message
                            if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
                                sec = re.findall(r'([\d.]*\d+)', message)
                                tunggu(int(sec[0]))
                                sleep(1)
                                posts = client(GetHistoryRequest(
                                    peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                                messageres = posts.messages[1].message
                                sleep(2)
                                if 'Sorry, that task is no longer valid' not in messageres:
                                    sys.stdout.write(
                                        f"\r{abu2}[{hijau2}+{abu2}]{hijau} "+messageres+"!\n")

                        elif soup.find('div', id="headbar") is not None:
                            for dat in soup.find_all('div', class_="container-fluid"):
                                code = dat.get('data-code')
                                timer = dat.get('data-timer')
                                tokena = dat.get('data-token')
                                tunggu(int(timer))
                                r = c.post("https://dogeclick.com/reward", data={
                                    "code": code, "token": tokena}, headers=ua, timeout=15, allow_redirects=True)
                                js = json.loads(r.text)
                                sys.stdout.write(f"\r{abu2}[{hijau2}+{abu2}]{hijau} You earned " +
                                                 js['reward']+" "+pilihan+" for visiting a site!\n")
                        else:
                            print('     bypass (skip)')
                            sys.stdout.write("\r")
                            sys.stdout.write(
                                "                                                                ")
                            sys.stdout.write("\r")
                            sys.stdout.write(
                                f"\r{abu2}[{yellow2}!{abu2}]{yellow} Trying to skip")
                            sys.stdout.flush()
                            sleep(2)
                            client(GetBotCallbackAnswerRequest(
                                self.choice,
                                id,
                                data=posts.messages[0].reply_markup.rows[1].buttons[1].data
                            ))
                            sys.stdout.write(
                                f"\r{abu2}[{red2}x{abu2}] {red}Skip ...!       \n")
                            sleep(2)
                            pass
                    except:
                        print('     bypass')
                        pass
                    # except:
                    #     sleep(3)
                    #     posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                    #                                      offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    #     message = posts.messages[0].message
                    #     sys.stdout.write(
                    #         f"\r{abu2}[{hijau2}+{abu2}]{hijau} $${message}\n")
                    #     if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
                    #         sec = re.findall(r'([\d.]*\d+)', message)
                    #         tunggu(int(sec[0]))
                    #         sleep(1)
                    #         posts = client(GetHistoryRequest(peer=channel_entity, limit=2,
                    #                                          offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    #         messageres = posts.messages[1].message
                    #         sleep(2)
                    #         if 'You earned' in messageres:
                    #             sys.stdout.write(
                    #                 f"\r{abu2}[{hijau2}+{abu2}]{hijau} $$$"+messageres+"\n")
                    #         else:
                    #             pass
                    #     else:
                    #         sys.stdout.write("\r")
                    #         sys.stdout.write(
                    #             "                                                                ")
                    #         sys.stdout.write("\r")
                    #         sys.stdout.write(
                    #             f"\r{abu2}[{yellow2}!{abu2}]{yellow} Captcha Detected")
                    #         sys.stdout.flush()
                    #         sleep(2)
                    #         client(GetBotCallbackAnswerRequest(
                    #             self.choice,
                    #             id,
                    #             data=posts.messages[0].reply_markup.rows[1].buttons[1].data
                    #         ))
                    #         sys.stdout.write(
                    #             f"\r{abu2}[{red2}x{abu2}] {red}Skip Captcha...!       \n")
                    #         sleep(2)
        finally:
            client.disconnect()

    def JoinBot(self):
        print('')
        sesi = True
        try:
            sys.stdout.write("\r")
            sys.stdout.write(
                "                                                              ")
            sys.stdout.write("\r")
            sys.stdout.write(
                f"\r{abu2}[{yellow2}!{abu2}]{yellow} Trying to get URL")
            sys.stdout.flush()
            client.send_message(entity=channel_entity,
                                message="🏅 Message bots")
            sleep(3)
            while sesi:
                posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                 offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                id = posts.messages[0].id
                if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
                    print(
                        f"\n{abu2}[{red2}x{abu2}] {red}Sorry, there are no new ads available")
                    client.send_message(entity=channel_entity,
                                        message="🏅 Balance")
                    sleep(5)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                     offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    message = posts.messages[0].message
                    print(f"\r{abu2}[{hijau2}+{abu2}]{hijau} "+message)
                    if "Available balance" in message:
                        sys.stdout.write(
                            "\r                                            \r")
                        jum = re.findall(r'([\d.]*\d+)', message)
                        if if_on():
                            sesi = False
                            if float(jum[0]) > float(get_min(pilihan)):
                                client.send_message(
                                    entity=channel_entity, message="🏅 Withdraw")
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message=get_address(pilihan))
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message=jum[0])
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message="🏅 Confirm")
                        else:
                            if self.withdraw:
                                if float(jum[0]) > float(self.amount):
                                    client.send_message(
                                        entity=channel_entity, message="🏅 Withdraw")
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message=self.address)
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message=jum[0])
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message="🏅 Confirm")
                                    print(
                                        f"\r{abu2}[{hijau2}+{abu2}]{hijau} Withdraw successful", jum[0], pilihan)
                                    sesi = False
                            sesi = False
                    else:
                        print('Exit..JoinBot(1)')
                        exit
                    print('no new ads available.    Exit..')
                    exit
                else:
                    try:
                        channel_msg = posts.messages[0].reply_markup.rows[0].buttons[0].url
                        if 't.me' in channel_msg:
                            channel_name = re.search(
                                r't.me\/(.*?)\?', channel_msg).group(1)
                            if channel_name is "":
                                sys.stdout.write(
                                    "\r                                                              \r")
                                sys.stdout.write(
                                    f"\r{abu2}[{red2}x{abu2}]{red} Cannot Find Channel")
                                client(GetBotCallbackAnswerRequest(
                                    self.choice,
                                    id,
                                    data=posts.messages[0].reply_markup.rows[1].buttons[1].data
                                ))
                                sys.stdout.write(
                                    f"\r{abu2}[{red2}x{abu2}] {red}Skip Bot                           \n")
                                sleep(2)
                                continue
                        elif 't.me' not in channel_msg:
                            channel_name = re.search(
                                r't.me\/(.*?)', channel_msg).group(1)
                            if channel_name is "":
                                sys.stdout.write(
                                    "\r                                                              \r")
                                sys.stdout.write(
                                    f"\r{abu2}[{red2}x{abu2}]{red} Cannot Find Channel")
                                client(GetBotCallbackAnswerRequest(
                                    self.choice,
                                    id,
                                    data=posts.messages[0].reply_markup.rows[1].buttons[1].data
                                ))
                                sys.stdout.write(
                                    f"\r{abu2}[{red2}x{abu2}] {red}Skip Bot                                 \n")
                                sleep(2)
                                continue
                        else:
                            sys.stdout.write(
                                "\r                                                              \r")
                            sys.stdout.write(
                                f"\r{abu2}[{red2}x{abu2}]{red} Cannot Find Channel")
                            client(GetBotCallbackAnswerRequest(
                                self.choice,
                                id,
                                data=posts.messages[0].reply_markup.rows[1].buttons[1].data
                            ))
                            sys.stdout.write(
                                f"\r{abu2}[{red2}x{abu2}] {red}Skip Bot                                 \n")
                            sleep(2)
                    except:
                        sys.stdout.write(
                            "\r                                                              \r")
                        sys.stdout.write(
                            f"\r{abu2}[{red2}x{abu2}]{red} URL not found")
                        client(GetBotCallbackAnswerRequest(
                            self.choice,
                            id,
                            data=posts.messages[0].reply_markup.rows[1].buttons[1].data
                        ))
                        sys.stdout.write(
                            f"\r{abu2}[{red2}x{abu2}] {red}Skip Bot                                 \n")
                        sleep(2)
        except:
            print(sys.exc_info())
            exit

        finally:
            client.disconnect()

    def JoinChannel(self):
        print('')
        sesi = True
        try:
            while sesi:
                sys.stdout.write("\r")
                sys.stdout.write(
                    "                                                              ")
                sys.stdout.write("\r")
                sys.stdout.write(
                    f"\r{abu2}[{yellow2}!{abu2}]{yellow} Trying to get URL")
                sys.stdout.flush()
                client.send_message(entity=channel_entity,
                                    message="🏅 Join chats")
                sleep(3)
                posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                 offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
                    print(
                        f"\n{abu2}[{red2}x{abu2}] {red}Sorry, there are no new ads available")
                    client.send_message(
                        entity=channel_entity, message="🏅 Balance")
                    sleep(5)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                     offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    message = posts.messages[0].message
                    print(f"\r{abu2}[{hijau2}+{abu2}]{hijau} "+message)
                    if "Available balance" in message:
                        sys.stdout.write(
                            "\r                                            \r")
                        jum = re.findall(r'([\d.]*\d+)', message)
                        if if_on():
                            sesi = False
                            if float(jum[0]) > float(get_min(pilihan)):
                                client.send_message(
                                    entity=channel_entity, message="🏅 Withdraw")
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message=get_address(pilihan))
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message=jum[0])
                                sleep(1)
                                client.send_message(
                                    entity=channel_entity, message="🏅 Confirm")
                        else:
                            if self.withdraw:
                                if float(jum[0]) > float(self.amount):
                                    client.send_message(
                                        entity=channel_entity, message="🏅 Withdraw")
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message=self.address)
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message=jum[0])
                                    sleep(1)
                                    client.send_message(
                                        entity=channel_entity, message="🏅 Confirm")
                                    print(
                                        f"\r{abu2}[{hijau2}+{abu2}]{hijau} Withdraw successful", jum[0], pilihan)
                                    sesi = False
                            sesi = False
                    else:
                        print('Exit..JoinChannel(1)')
                        exit
                    print('no new ads available.    Exit..')
                    exit
                else:
                    try:
                        url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                        sys.stdout.write("\r")
                        sys.stdout.write(
                            f"\r{abu2}[{yellow2}!{abu2}]{yellow} Join "+url)
                        sys.stdout.flush()
                        id = posts.messages[0].id
                        client(JoinChannelRequest(url))
                        client(GetBotCallbackAnswerRequest(self.choice, id,
                                                           data=posts.messages[0].reply_markup.rows[0].buttons[1].data))
                        sleep(3)
                        posts = client(GetHistoryRequest(peer=channel_entity, limit=2,
                                                         offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        if posts.messages[0].message.find("We cannot find you in the group") != -1:
                            client(GetBotCallbackAnswerRequest(
                                self.choice, id, data=posts.messages[1].reply_markup.rows[1].buttons[1].data))
                            sys.stdout.write(
                                f"\r{abu2}[{red2}x{abu2}] {red}Skip Captcha...!       \n")
                        else:
                            sys.stdout.write(f"\r{abu2}[{hijau2}+{abu2}]{hijau} Success! ({url}) Stay at least{res}"+re.search(
                                r' [0-9]* ', posts.messages[1].message).group(0)+f" hour {hijau}to earn your reward. \n")
                            sleep(5)
                    except:
                        print(sys.exc_info())
                        exit
        finally:
            client.disconnect()


class UserInterface:
    def banner(self, mode=f' '):
        clear()
        print(f"""\n
        {Fore.CYAN}ClickBot {Fore.RED}version {Fore.WHITE}{get_version()}
        {Fore.WHITE}by github.com/ziziwho
        youtube.com/ziziworks
    
    {Fore.YELLOW}{mode}\n""")

    def yn(self, message: str):
        # this will loop forever
        # because True is never False
        while True:
            # store the user input in a variable,
            # because we will be using it more than once
            answer = input(message + ' [y/n]: ')

            # this makes sure of two things:
            # 1. the answer exists
            # 2. the answer is one of ('y', 'n')
            if len(answer) > 0 and answer[0].lower() in ('y', 'n'):
                # the == operator just returns a boolean,
                # so if the result is 'y', return True,
                # else we know it can only be 'n' so False
                # we return immediately now
                return answer[0].lower() == 'y'

            # if the answer is not what we want,
            # we never return from the function
            # and we loop

    def write_json(self, data, filename='config.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def api_id(self):
        self.banner('Create configuration (api_id)')
        while True:
            try:
                # Ask api_id
                print(
                    'You can obtain your own API ID at https://core.telegram.org/api/obtaining_api_id')
                api_id = input('What is your api_id : ')
                if api_id != None:
                    return int(api_id)
                raise ValueError
            except ValueError:
                self.banner('Create configuration (api_id)')
                print(f'\t{Fore.RED}api_id must contain only number')

    def api_hash(self):
        api_hash = None
        self.banner('Create configuration (api_hash)')
        while (api_hash == None) or (api_hash.find(' ') != -1) or api_hash == "":
            try:
                # Ask api_hash
                print(
                    'You can obtain your own API HASH at https://core.telegram.org/api/obtaining_api_id')
                api_hash = input('What is your api_hash : ')
                if (api_hash.find(' ') != -1):
                    self.banner('Create configuration (api_hash)')
                    print(
                        f'\t{Fore.RED}api_hash can\'t contain spacing / empty space')
                elif api_hash == "":
                    self.banner('Create configuration (api_hash)')
                    print(f'\t{Fore.RED}api_hash can\'t be empty')
                else:
                    self.banner('Create configuration (api_hash)')
            except TypeError:
                self.banner('Create configuration (api_hash)')
                print(f'\t{Fore.RED}Must be string')
        return api_hash

    def wallet_address(self, wallet_name: str):
        address = None
        self.banner('Create configuration (wallet_address)')
        while (address == None) or (address.find(' ') != -1) or address == "":
            try:
                # Ask address
                print(
                    f'Please insert correct {wallet_name} address.\nYou may not be able to change this later')
                address = input(f'What is your {wallet_name} address : ')
                if (address.find(' ') != -1):
                    self.banner('Create configuration (wallet_address)')
                    print(
                        f'\t{Fore.RED}address can\'t contain spacing / empty space')
                elif address == "":
                    self.banner('Create configuration (wallet_address)')
                    print(f'\t{Fore.RED}address can\'t be empty')
                else:
                    self.banner('Create configuration (wallet_address)')
            except TypeError:
                self.banner('Create configuration (wallet_address)')
                print(f'\t{Fore.RED}Must be string')
        return address

    def wallet_amount(self, wallet_name: str):
        def get_limit(wallet_name):
            if wallet_name.upper() == 'BTC':
                return '0.00003'
            elif wallet_name.upper() == 'LTC':
                return '0.0004'
            elif wallet_name.upper() == 'DOGE':
                return '4'
            elif wallet_name.upper() == 'BCH':
                return '0.0001'
            elif wallet_name.upper() == 'ZEC':
                return '0.00035'
        amount = -1
        limit = get_limit(wallet_name)
        self.banner('Create configuration (wallet_amount)')
        while (amount < float(limit)):
            try:
                # Swap raw_input for input in Python 3.x
                amount = float(
                    input(f"Withdraw {wallet_name} when balance is .. (must greater or equal to {str(limit)}) : "))
                if amount < float(limit):
                    self.banner('Create configuration (wallet_amount)')
                    print(f"\t{Fore.RED}must greater or equal to {str(limit)}")
            except ValueError:
                self.banner('Create configuration (wallet_amount)')
                print(f"\t{Fore.RED}That wasn't an float / integer :(")
        return str(amount)

    def create_config(self, filename='config.json'):
        def create():
            base = {
                "api_data": {
                    "api_id": self.api_id(),
                    "api_hash": self.api_hash()
                },
                "wallet_details": [
                    {
                        "BTC": {
                            "Address": self.wallet_address('BTC'),
                            "Amount": self.wallet_amount('BTC')
                        }
                    },
                    {
                        "LTC": {
                            "Address": self.wallet_address('LTC'),
                            "Amount": self.wallet_amount('LTC')
                        }
                    },
                    {
                        "DOGE": {
                            "Address": self.wallet_address('DOGE'),
                            "Amount": self.wallet_amount('DOGE')
                        }
                    },
                    {
                        "BCH": {
                            "Address": self.wallet_address('BCH'),
                            "Amount": self.wallet_amount('BCH')
                        }
                    },
                    {
                        "ZEC": {
                            "Address": self.wallet_address('ZEC'),
                            "Amount": self.wallet_amount('ZEC')
                        }
                    }
                ],
                "account_details": [
                ]
            }

            self.write_json(base, filename)
            self.banner('Create configuration')
            print(filename, 'created.')
            return load_config('config.json')
        if path.exists(filename):
            self.banner(
                f'Create configuration [{Fore.RED}Overwrite Warning{Fore.YELLOW}]')
            if self.yn(f'\t[{Fore.RED}WARNING!{Fore.WHITE}] {filename} already exist. Do you want to overwrite?'):
                create()
        else:
            self.banner('Create configuration')
            create()

    def add_account(self, filename='config.json'):
        try:
            def phone():
                self.banner('Add account (Phone)')
                # Ask phone
                print(
                    ' What is your phone number?\nInput number in international format (example: +60123456789) : \n')
                phone = input('Phone : ')
                return phone

            def if_exist(phone, filename='config.json'):
                with open(filename) as json_file:
                    data = json.load(json_file)
                    for i in range(len(data['account_details'])):
                        # print(data['account_details'][i]["phone"])
                        if data['account_details'][i]["phone"] == phone:
                            return True
                        else:
                            pass
                    return False

            def choice():
                self.banner('Add account (Choice)')
                while True:
                    try:
                        # Bot choice
                        print(' Clickbot choice: \n')
                        choice = ["BTC", "LTC", "DOGE",
                                  "BCH", "ZEC"]  # Bot option list
                        # Print bot options list with numberings
                        for number, letter in enumerate(choice):
                            print(	"	", number, letter)
                        # Ask user to select bot
                        ask_choice = input(
                            "	\n	What bot's choice do you want? (Number only) : ")
                        answer = (choice[int(ask_choice)])
                        if len(answer) > 0 and ask_choice[0] in ('0', '1', '2', '3', '4'):
                            return answer
                        self.banner('Add account (Choice)')
                    except ValueError:
                        self.banner('Add account (Choice)')
                        print(' Integer only')
                    except IndexError:
                        self.banner('Add account (Choice)')
                        print(' Choose from (0 - 4) only')

            def withdraw():
                self.banner('Add account (Withdraw)')
                while True:
                    try:
                        # Withdraw choice
                        print(' Clickbot withdraw choice: \n')
                        choice = [True, False]  # Bot option list
                        # Print bot options list with numberings
                        for number, boolean in enumerate(choice):
                            print(	"	", number, boolean)
                        # Ask user to select bot
                        ask_choice = input(
                            "	\n	What withdraw choice do you want? (Number only) : ")
                        answer = (choice[int(ask_choice)])
                        if len(ask_choice) > 0 and ask_choice[0] in ('0', '1'):
                            return answer
                        self.banner('Add account (Withdraw)')
                        print(' Choose from (0 - 1) only')
                    except ValueError:
                        self.banner('Add account (Withdraw)')
                        print(' Integer only')
                    except IndexError:
                        self.banner('Add account (Withdraw)')
                        print(' Choose from (0 - 1) only')

            with open(filename) as json_file:
                data = json.load(json_file)
                phone = phone()
                if not if_exist(phone):
                    category = data['account_details']
                    choice = choice()
                    withdraw = withdraw()
                    x = {
                        "phone": phone,
                        "choice": choice,
                        "withdraw": withdraw
                    }
                    category.insert(0, x)
                    self.write_json(data, filename)
                    print(
                        f'\n Added account to {filename}\n Phone: {phone}\n Choice: {choice}\n Withdraw: {withdraw}')
                    return load_config('config.json')
                else:
                    print(f'{phone} already exist')
        except FileNotFoundError:
            print(f'\n\tYou don\'t have any configuration')
            input('\n\tpress any to create configuration\n')
            return self.create_config()

    def view_accounts(self):
        if len(accounts) == 0:
            print(f'\tYou have {len(accounts)} accounts')
            input('\n\tpress any to add account')
            return self.add_account()
        print(f'\t{Fore.CYAN}Total accounts {Fore.WHITE}: {len(accounts)}\n')
        c = 1
        for account in accounts:
            print(f'\t{Fore.CYAN}{str(c)}{Fore.WHITE} {account}')
            c += 1

    def view_configuration(self):
        try:
            print(f'\t{Fore.CYAN}API ID{Fore.WHITE}: {api_id}')
            print(f'\t{Fore.CYAN}API HASH{Fore.WHITE}: {api_hash}')
            print(f'\n\t{Fore.CYAN}Wallets{Fore.WHITE}:\n')
            for wallet in wallets:
                print(f'\t{wallet}')
        except NameError:
            print(f'\tYou don\'t have any configuration')
            input('\n\tpress any to create configuration')
            return self.create_config()

    def delete_account(self, filename='config.json'):
        def delete(index):
            with open(filename) as json_file:
                data = json.load(json_file)
                category = data['account_details']
                phone = data['account_details'][index]['phone']
                category.pop(index)
                self.write_json(data, filename)
                print(
                    f'\n {Fore.CYAN}{index} {Fore.WHITE}{phone} deleted.')
                return load_config('config.json')
        self.banner('Delete account')
        ranges = []
        maximum = len(accounts)+1
        for x in range(1, maximum):
            ranges.append(str(x))
        while True:
            self.view_accounts()
            try:
                # Ask user to select account
                ask_choice = input(
                    f"	\n	Which account do you want to delete? ({Fore.CYAN}number only{Fore.WHITE}) : ")
                answer = int(ask_choice)
                if len(ask_choice) > 0 and ask_choice[0] in ranges:
                    return delete(answer-1)
                self.banner('Delete account')
                print(f'\t{Fore.RED}Choose from (1 - {str(maximum-1)}) only')
            except ValueError:
                self.banner('Delete account')
                print(f'\t{Fore.RED}Integer only')
            except IndexError:
                self.banner('Delete account')
                print(f'\t{Fore.RED}Choose from (1 - {str(maximum-1)}) only')


def main():
    global pilihan
    for i in range(0, total_accounts):
        try:
            pilihan = accounts[i]['choice']
            me = ClickBot(accounts[i]['phone'], api_id,
                          api_hash, choice(i), withdraw(i), i)
            me.banner()  # Comment this to see load_accounts()
            print(f'{Fore.CYAN}    API_id {res}:', me.api)
            print(f'{Fore.CYAN}    API_hash {res}:', me.api_hash)
            print('')
            print(f'    Account [{i+1}/{total_accounts}]')
            print('='*60)
            print('    Phone         : ', me.phone)
            print('    Bot           : ', me.choice)
            print(f'    Withdraw {pilihan} : ', f'{Style.BRIGHT+Fore.RED}{me.withdraw}' if me.withdraw ==
                  False else f'{Style.BRIGHT+Fore.GREEN}{me.withdraw}')
            print(f'    {pilihan} address  : ', me.address)
            print('    Min amount        : ', me.amount, f'{pilihan}')
            print('='*60, '\n')
            me.login()
            me.start_all()
            me.Visit()
            # me.JoinBot()
            # me.JoinChannel()
            sleep(3)
        # except KeyError:
        #     print(sys.exc_info())
        #     exit
        except FloodWaitError:
            print(sys.exc_info())
            exit
        except KeyboardInterrupt:
            print(f"\n{abu2}[{red2}x{abu2}] {red}Exit...!")
            sleep(1)
            sys.exit()


def menu(do_auto=False, auto_action='0'):
    ui = UserInterface()
    actions = ("Create configuration",          # 0
               "View configuration",                  # 1
               "Add account",         # 2
               "View accounts",                    # 3
               "Delete accounts",                         # 4
               "Start ClickBot",    # 5
               "Exit")                        # 6
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            ui.banner('Main Menu')
            print(Fore.CYAN+'   Index', Fore.WHITE+'         Action\n')

            for index, action in enumerate(actions):
                print('     '+Fore.CYAN+str(index), Fore.WHITE+'    '+action)

            if do_auto:
                do_auto = False
                user_action = auto_action
            else:
                user_action = input("\n  Enter action's index : ")
            print('')
            if user_action == '0':
                ui.banner(str(actions[(int(user_action))]))
                ui.create_config()

            elif user_action == '1':
                ui.banner(str(actions[(int(user_action))]))
                ui.view_configuration()

            elif user_action == '2':
                ui.banner(str(actions[(int(user_action))]))
                ui.add_account()

            elif user_action == '3':
                ui.banner(str(actions[(int(user_action))]))
                ui.view_accounts()

            elif user_action == '4':
                ui.banner(str(actions[(int(user_action))]))
                ui.delete_account()

            elif user_action == '5':
                ui.banner(str(actions[(int(user_action))]))
                try:
                    main()
                except NameError:
                    print(f'\tYou don\'t have any configuration')
                    input('\n\tpress any to create configuration')
                    return ui.create_config()

            elif user_action == '6':
                break
            else:
                print('not valid')
            input('\npress any to continue..')
        except KeyboardInterrupt:
            exit


if __name__ == "__main__":
    check_update()
    try:
        load_config('config.json')
        clear()
        total_accounts = len(accounts)
        if total_accounts == 0:
            print(f'\t{Fore.YELLOW}Zero (0) account in config.ini')
        try:
            sys.argv[1]
            main()
        except IndexError:
            menu()
    except FileNotFoundError:
        menu(do_auto=True)
