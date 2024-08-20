import requests
import time
import json
from colorama import Fore, Style
from fake_useragent import UserAgent

with open('data.json', 'r') as file:
    data = json.load(file) 
    authorization_data_list = data['authorization_data'] 

headers = {
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"129-83t1ejiXqZksI6D5DMDXM+paHE4"',
    'origin': 'https://tgdapp.duckchain.io',
    'priority': 'u=1, i',
    'referer': 'https://tgdapp.duckchain.io/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

def userinfo(authorization_data):
    api_url = 'https://tgapi.duckchain.io/user/info'
    headers['authorization'] = f'tma {authorization_data}' 

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        data = response.json()

        duck_name = data.get('data', {}).get('duckName')
        if duck_name:
            print(Fore.GREEN + "Duck Name:" + Style.RESET_ALL, duck_name)
        else:
            print(Fore.RED + "Duck name not found in response." + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan saat melakukan permintaan userinfo: {e}" + Style.RESET_ALL)


def quack_execute(authorization_data):
    api_url = 'https://tgapi.duckchain.io/quack/execute'
    headers['authorization'] = f'tma {authorization_data}'

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        data = response.json()

        decibel = data.get('data', {}).get('decibel')
        quack_times = data.get('data', {}).get('quackTimes')

        if decibel and quack_times:
            print(Fore.GREEN + "Balance:" + Style.RESET_ALL, decibel)
            print(Fore.GREEN + "Total Click:" + Style.RESET_ALL, quack_times)
        else:
            print(Fore.RED + "Decibel or Quack Times not found in response." + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan saat melakukan permintaan quack_execute: {e}" + Style.RESET_ALL)

if __name__ == '__main__':
    ua = UserAgent()
    while True:
        for i, authorization_data in enumerate(authorization_data_list):
            headers['user-agent'] = ua.random 
            print(Fore.YELLOW + f"\n=== Akun ke-{i+1} ===" + Style.RESET_ALL) 
            userinfo(authorization_data)
            quack_execute(authorization_data)
            time.sleep(1)