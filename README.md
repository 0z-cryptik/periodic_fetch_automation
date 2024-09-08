# Periodic Fetch Automation Script

This Python script is designed to periodically send requests to a specified URL to keep the server alive. This is especially useful for servers hosted on free platforms that tend to spin down due to inactivity.

## Features
- Sends a periodic GET request to a specified URL.
- Logs the status of the request.
- Handles connection errors gracefully.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.x
- The `requests` library
- `python-dotenv` for loading environment variables from a `.env` file

Install dependencies using:
pip install requests python-dotenv
