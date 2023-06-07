import requests
from urllib.parse import urlparse
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
from plyer import notification
from setup import selected_option

method = selected_option

input_file = "methods/" + method + ".txt"
hits_file = "hits.txt"

def process_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme == '':
        url = 'https://www.tiktok.com/@' + url

    try:
        response = requests.get(url)

        if response.status_code == 404:
            with open(hits_file, 'a') as hits:
                hits.write(url + '\n')
            print(Fore.GREEN + url)
            show_notification("Neuer Treffer", url)
        else:
            print(Fore.RED + url)

    except requests.exceptions.RequestException:
        print("Fehler bei der Anfrage:", url)

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )

def main():
    method = selected_option

    with open(input_file, 'r') as file:
        urls = [line.strip() for line in file]

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(process_url, url) for url in urls]

        for future in futures:
            future.result()

if __name__ == '__main__':
    main()
