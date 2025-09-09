import requests

# List of important security headers to check for
SECURITY_HEADERS = [
    'Strict-Transport-Security',
    'X-Content-Type-Options',
    'X-XSS-Protection',
    'Content-Security-Policy',
    'X-Frame-Options',
    'Referrer-Policy',
    'Feature-Policy',
    'Permissions-Policy'
]

def check_security_headers(url):
    """
    Function to check for the presence of important security headers in the HTTP response of a website.
    :param url: URL of the website to check.
    :return: None
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        print(f"Checking security headers for {url}...\n")

        # Iterate over each header and check if it's present in the response
        for header in SECURITY_HEADERS:
            if header in response.headers:
                print(f"[+] {header}: {response.headers[header]}")
            else:
                print(f"[-] {header}: Not Found")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    # Take the URL from user input or hardcoded
    url = input("Enter the URL to test (e.g., https://example.com): ")
    
    # Check if the URL is valid
    if url.startswith("http://") or url.startswith("https://"):
        check_security_headers(url)
    else:
        print("Error: Please enter a valid URL starting with http:// or https://")

if __name__ == '__main__':
    main()
