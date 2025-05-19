import requests
import json

class SentraAPI:
    def __init__(self):
        """
        Initialize the SentraAPI client with the base URL of the API.
        
        :param base_url: The base URL of the Sentra API (e.g., "https://api.sentra.wannacryptic.com ").
        """
        self.base_url = "http://localhost:8100"

    def scan_file(self, file_path):
        """
        Scan an uploaded file.

        :param file_path: Path to the file to be scanned.
        :return: Response from the API (JSON object).
        """
        url = f"{self.base_url}/scan/"
        files = {'file': open(file_path, 'rb')}
        try:
            response = requests.post(url, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during file scan: {e}")
            return None
        finally:
            files['file'].close()

    def scan_url(self, url_to_scan):
        """
        Scan a URL.

        :param url_to_scan: The URL to be scanned.
        :return: Response from the API (JSON object).
        """
        url = f"{self.base_url}/scan/url/"
        data = {"url": url_to_scan}
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during URL scan: {e}")
            return None