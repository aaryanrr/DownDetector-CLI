import webbrowser
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

import src.Errors as Errors


# Class for thw URL Instance
class URLInstance(object):

    url = "https://downdetector.com/status/"

    def __init__(self, service_name):
        self.url = f"{self.url}" + service_name
        # Create a session for better connection handling and bot protection bypass
        self.session = requests.Session()

    # Scrape the Status of the Service from the Page
    def get_status(self):
        # Updated headers to mimic a real browser more closely
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Cache-Control": "max-age=0",
            "Referer": "https://www.google.com/"
        }
        
        try:
            # Use session for better connection handling
            response = self.session.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html5lib')
            
            # Try multiple selectors to find the status message (more robust approach)
            status_text = None
            
            # Strategy 1: Try original selector for backward compatibility
            company_div = soup.find('div', attrs={'id': 'company'})
            if company_div:
                text_elem = company_div.find('div', attrs={'class': 'h2 entry-title'})
                if text_elem:
                    status_text = text_elem.text.strip()
            
            # Strategy 2: Try to find entry-title class directly (more common in modern design)
            if not status_text:
                entry_title = soup.find(['h1', 'h2', 'h3', 'div'], class_='entry-title')
                if entry_title:
                    status_text = entry_title.text.strip()
            
            # Strategy 3: Try to find status-related elements with common class patterns
            if not status_text:
                # Look for elements with "status" in class name
                for elem in soup.find_all(['div', 'span', 'h1', 'h2', 'h3']):
                    class_names = elem.get('class', [])
                    if any('status' in str(c).lower() or 'entry-title' in str(c).lower() for c in class_names):
                        text = elem.text.strip()
                        # Filter out very short text or common non-status text
                        if text and len(text) > 5 and not text.lower() in ['status', 'info', 'information']:
                            status_text = text
                            break
            
            # Strategy 4: Look for the page title as fallback
            if not status_text:
                page_title = soup.find('h1')
                if page_title:
                    text = page_title.text.strip()
                    # Only use if it looks like a status message (contains certain keywords)
                    if any(keyword in text.lower() for keyword in ['problem', 'issue', 'outage', 'down', 'working', 'reports', 'no problems']):
                        status_text = text
            
            if status_text:
                print(status_text)
            else:
                raise Errors.InvalidServiceName(
                    "Could not find status information. The service name may be invalid or the page structure has changed."
                )

        except AttributeError:
            # Expecting AttributeError if the Name given is Invalid
            # A NoneType object won't have the attribute .text as used above
            raise Errors.InvalidServiceName("Name of the Service is Invalid!")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            raise Errors.InvalidServiceName("Could not fetch the page. Please check your internet connection and try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get("https://downdetector.com", headers=headers, timeout=10)
        response.raise_for_status()
        print("All Good 👍")
    except ConnectionError:
        print("This program requires an active Internet Connection!")
        quit()
    except requests.exceptions.Timeout:
        print("Connection timeout. Please check your internet connection!")
        quit()
    except Exception as e:
        print(f"Connection check failed: {e}")
        print("Proceeding anyway...")


# Function for the Menu
def menu():
    print("1. Check Status")
    print("2. Open in Browser")
    print("3. Get URL")
    print("4. Get Base URL")
    print("5. Search for Another Service")
    print("6. Exit")
