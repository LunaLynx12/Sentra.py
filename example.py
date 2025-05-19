from lib.sentra_api import SentraAPI
import json

if __name__ == "__main__":
    api = SentraAPI()

    # Example: Scan a file
    print("Scanning file...")
    file_response = api.scan_file("examples/binary.exe")
    if file_response:
        print("File Scan Response:\n", json.dumps(file_response, indent=4))
    else:
        print("File scan failed or returned empty response.")

    # Example: Scan a URL
    print("\nScanning URL...")
    url_response = api.scan_url("https://example.com ")
    if url_response:
        print("URL Scan Response:\n", json.dumps(url_response, indent=4))
    else:
        print("URL scan failed or returned empty response.")