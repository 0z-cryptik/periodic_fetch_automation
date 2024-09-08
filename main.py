import requests
import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path="/Users/user/code2/periodic_fetch_automation/.env"
)

def send_request_to_url(url: str) -> int | None:
    try:
        response = requests.get(url, timeout=120)
        return response.status_code
    except requests.ConnectionError:
        print("connection error")
        return
    except requests.RequestException as e:
        print(f"error: {e}")
        return

def main() -> None:
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

