import sys
import requests
from lxml import html


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        root = html.fromstring(response.content)
        hrefs = [href for href in root.xpath('//a/@href') if href.startswith('http')]
        return hrefs

    except Exception:
        return []


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        for url in all_hrefs:
            hrefs = download_url_and_get_all_hrefs(url)
            print(hrefs)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
