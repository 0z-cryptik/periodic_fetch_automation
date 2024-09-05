import requests

def send_request_to_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code, response.json()
    except requests.ConnectionError:
        return None, "No internet connection or URL unreachable."
    except requests.RequestException as e:
        return None, str(e)


def main():
    url = "https://projectplanner-backend.onrender.com/periodicFetch"
    status_code, content = send_request_to_url(url)

    if status_code:
        print(f"Request successful. Status code: {status_code}")
        print("Response content:")
        print(content)
    else:
        print(f"Failed to send request. Error: {content}")


if __name__ == "__main__":
    main()
