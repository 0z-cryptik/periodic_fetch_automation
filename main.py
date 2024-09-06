import requests
import os
from dotenv import load_dotenv

load_dotenv()


def send_request_to_url(url):
    try:
        response = requests.get(url, timeout=120)
        return response.status_code
    except requests.ConnectionError:
        return None, "No internet connection or URL unreachable."
    except requests.RequestException as e:
        return None, str(e)


def main():
    url = os.getenv("URL")

    if not url:
        print("URL is not set in the environment file.")
        return

    status_code = send_request_to_url(url)

    if status_code == 200:
        print(f"Request successful. Status code: {status_code}")
    else:
        print("Error sending request")


if __name__ == "__main__":
    main()
