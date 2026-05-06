import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        return response.json()

    def get_all_pages(self, endpoint, params=None):
        if params is None:
            params = {}

        params["per_page"] = 100
        page = 1
        results = []

        while True:
            params["page"] = page
            data = self.get(endpoint, params=params)

            if not data or len(data) == 0:
                break

            results.extend(data)
            page += 1

        return results