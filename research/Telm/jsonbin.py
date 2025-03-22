import os
import sys
import json
import requests
import pkg_resources
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# I am aware that API are insecure to be handled this way ToDO later and TRUSTING YOU!
JSONBIN_API_KEY = '$2a$10$rHjtP6IMGSvO11ZnF4dVtusr7ZbsTiQeF2DPuN0mqrqdBJ06y9U2q'
BIN_ID = '67de341a8561e97a50f09cad'
JSONBIN_URL = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
TELEMETRY_FILE = "research/Telm/telemetry.json"

def get_docoreai_version():
    """Fetches the installed version of DoCoreAI"""
    return pkg_resources.get_distribution("docoreai").version

def is_telemetry_enabled():
    """Check if telemetry is enabled in .env (default: enabled)"""
    return os.getenv("DOCOREAI_TELEMETRY", "True").strip().lower() in ("true", "1", "yes")


def update_jsonbin(notes: str = "Upgrade"):
    try:
        """Updates JSONBin with the new upgrade entry"""
        
        version = get_docoreai_version()  # Fetch installed DoCoreAI version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        timestamp = datetime.utcnow().isoformat() + "Z"

        # Load existing telemetry data or initialize new
        telemetry_data = {"upgrades": []}  # Default structure

        if os.path.exists(TELEMETRY_FILE):
            with open(TELEMETRY_FILE, "r") as f:
                try:
                    telemetry_data = json.load(f)
                    if not isinstance(telemetry_data, dict):
                        telemetry_data = {"upgrades": []}  # Ensure correct structure
                except json.JSONDecodeError:
                    telemetry_data = {"upgrades": []}  # Handle corruption

        # Check last recorded version
        last_version = telemetry_data["upgrades"][-1]["version"] if telemetry_data["upgrades"] else None

        if last_version == version:
            print("🔹 No version change detected. Telemetry update skipped.")
            return  # Exit early

        # Append new version details
        new_entry = {
            "version": version,
            "python_version": python_version,
            "timestamp": timestamp,
            "notes": notes
        }
        telemetry_data["upgrades"].append(new_entry)

        # Save locally
        with open(TELEMETRY_FILE, "w") as f:
            json.dump(telemetry_data, f, indent=4)

        print(f"Version changed to {version}. Updating telemetry...")

        # Update JSONBin
        headers = {"X-Master-Key": JSONBIN_API_KEY, "Content-Type": "application/json"}
        response = requests.get(JSONBIN_URL, headers=headers)

        if response.status_code == 200:
            jsonbin_data = response.json()
            jsonbin_data["record"]["upgrades"].append(new_entry)

            update_response = requests.put(JSONBIN_URL, headers=headers, json=jsonbin_data["record"])
            if update_response.status_code == 200:
                print("JSONBin updated successfully!")
            else:
                print(f"Failed to update JSONBin. HTTP {update_response.status_code}: {update_response.text or 'Unknown error'}")
        else:
            print(f"Failed to fetch existing JSONBin data. HTTP {response.status_code}: {response.text or 'Unknown error'}")
    except Exception as e:
        print(f"Telemetry error occurred: {e}")  # Prints the error message