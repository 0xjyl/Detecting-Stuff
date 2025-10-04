# sometimes domain-takedowns aren't enough 

import webbrowser
import urllib.parse
import platform
import os

# Function to open a URL in a new tab of the default web browser
def open_url_in_new_tab(url):
    try:
        if platform.system() == 'Darwin':  # macOS
            os.system(f'open -a "Firefox" "{url}"')  # Specify browser if needed
        else:
            webbrowser.open_new_tab(url)
        print(f'Successfully opened browser for URL: {url}')
    except Exception as e:
        print(f'Failed to open browser for URL: {url}, Error: {e}')

# Function to open Google Safe Browsing report page with pre-filled URL
def report_to_google(malicious_url):
    google_base_url = 'https://safebrowsing.google.com/safebrowsing/report_phish/'
    google_params = {'url': malicious_url}
    google_full_url = f'{google_base_url}?{urllib.parse.urlencode(google_params)}'
    open_url_in_new_tab(google_full_url)
    print(f'Opened browser to report URL to Google: {malicious_url}')

# Function to open Microsoft SmartScreen report page with pre-filled URL
def report_to_microsoft(malicious_url):
    microsoft_base_url = 'https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site-guest'
    microsoft_params = {'url': malicious_url}
    microsoft_full_url = f'{microsoft_base_url}?{urllib.parse.urlencode(microsoft_params)}'
    open_url_in_new_tab(microsoft_full_url)
    print(f'Opened browser to report URL to Microsoft: {malicious_url}')

if __name__ == '__main__':
    malicious_url = input('Enter the malicious URL: ')
    report_to_google(malicious_url)
    report_to_microsoft(malicious_url)
