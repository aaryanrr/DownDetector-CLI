# Defines the Main Classes

import webbrowser
import requests
from bs4 import BeautifulSoup
from src.Errors import InvalidServiceName
from requests.exceptions import ConnectionError


# Class for thw URL Instance
class URLInstance(object):
    url = "https://downdetector.in/status/"

    def __init__(self, serviceName):
        self.url = f"{self.url}" + serviceName

    # Scrape the Status of the Service from the Page
    def GetStatus(self):
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')

            # Finds the div with h2 entry-title class
            data = soup.find('div', class_="h2 entry-title")
            print(data.text.strip())

        except AttributeError:
            # Expecting AttributeError if the Name given is Invalid
            # A NoneType object won't have the attribute .text as used above
            raise InvalidServiceName("Name of the Service is Invalid!")
        else:
            pass

    # Prints the URL for the Status Page of the Service
    def GetURL(self):
        print(self.url)

    # Opens the URL in the default Web Browser
    def OpenURL(self):
        webbrowser.open(self.url)
        print("The link was opened in the Browser!")

    @classmethod
    def GetBaseURL(cls):
        print(cls.url)


# Function to Check the Internet Connection
def CheckConnection():
    try:
        requests.get("https://downdetector.com")
    except ConnectionError:
        print("This program requires an active Internet Connection!")
    else:
        print("All Good 👍")


# Function for the Menu
def ShowMenu():
    print("1. Check Status")
    print("2. Open in Browser")
    print("3. Get URL")
    print("4. Get Base URL")
    print("5. Search for Another Service")
    print("6. Exit")
