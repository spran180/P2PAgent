import requests
import os

ETHERCALC_URL = os.getenv("ETHERCALC_URL", "http://localhost:8000")
SHEET_NAME = os.getenv("SHEET_NAME")

def create_table():
    try:
        csv_data = """Peer,Message,Status
            peer1,Hello World,Active
            peer2,Connected,Active
        """
        response = requests.put(
            f"{ETHERCALC_URL}/_/{SHEET_NAME}",
            data=csv_data,
            headers={
                "Content-Type": "text/csv"
            }
        )
        response.raise_for_status()
        print(f"Table '{SHEET_NAME}' created successfully.")  
    except requests.RequestException as e:
        print(f"Error creating table '{SHEET_NAME}': {e}")

def get_table_data():
    try:
        response = requests.get(f"{ETHERCALC_URL}/_/{SHEET_NAME}")
        response.raise_for_status()
        print(f"Table '{SHEET_NAME}' data retrieved successfully.")
        print(response.text)
    except requests.RequestException as e:
        print(f"Error retrieving table '{SHEET_NAME}' data: {e}")

