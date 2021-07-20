import webbrowser
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

from .Errors import InvalidServiceName


# Class for thw URL Instance
class URLInstance(object):

    url = "https://downdetector.com/status/"

    def __init__(self, service_name):
        self.url = f"{self.url}" + service_name

    # Scrape the Status of the Service from the Page
    def get_status(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/74.0.3729.169 Safari/537.36",
            'referer': 'https://www.google.com/'
        }
        try:
            page = requests.get(self.url, headers=header)
            soup = BeautifulSoup(page.content, 'html5lib')
            status = soup.find('div', attrs={'id': 'company'})
            text = status.find('div', attrs={'class': 'h2 entry-title'})
            print(text.text.strip())

        except AttributeError:
            # Expecting AttributeError if the Name given is Invalid
            # A NoneType object won't have the attribute .text as used above
            raise InvalidServiceName("Name of the Service is Invalid!")
        else:
            pass

    # Prints the URL for the Status Page of the Service
    def get_url(self):
        print(self.url)

    # Opens the URL in the default Web Browser
    def open_url(self):
        webbrowser.open(self.url)
        print("The link was opened in the Browser!")

    @classmethod
    def get_base_url(cls):
        print(cls.url)


# Function to Check the Internet Connection
def check_connection():
    try:
        requests.get("https://downdetector.com")
    except ConnectionError:
        print("This program requires an active Internet Connection!")
    else:
        print("All Good 👍")


# Function for the Menu
def menu():
    print("1. Check Status")
    print("2. Open in Browser")
    print("3. Get URL")
    print("4. Get Base URL")
    print("5. Search for Another Service")
    print("6. Exit")
