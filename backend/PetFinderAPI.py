import requests
import os
import time
import json
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.environ.get("PETFINDER_API_KEY")
CLIENT_SECRET = os.environ.get("PETFINDER_API_SECRET")

TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"
API_BASE_URL = "https://api.petfinder.com/v2"

token_info = {
    "access_token": None,
    "expires_at": 0
}

def get_petfinder_token():
    """Requests a new access token from the Petfinder API."""
    global token_info

    if not CLIENT_ID or not CLIENT_SECRET:
         print("Error: Petfinder API Key or Secret Key not found in environment variables.")
         return None

    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    try:
        print("Requesting new Petfinder token...")
        response = requests.post(TOKEN_URL, data=data, timeout=10) # Added timeout
        response.raise_for_status()

        token_data = response.json()
        current_time = time.time()
        # Store token and calculate expiration time (with a 60s buffer)
        token_info["access_token"] = token_data['access_token']
        token_info["expires_at"] = current_time + token_data['expires_in'] - 60
        # print(f"Token expires around: {time.ctime(token_info['expires_at'])}") # Uncomment for debugging
        return token_info["access_token"]

    except requests.exceptions.RequestException as e:
        print(f"Error requesting token: {e}")
        if hasattr(e, 'response') and e.response is not None:
             print(f"Response status: {e.response.status_code}")
             try: print(f"Response body: {e.response.json()}")
             except requests.exceptions.JSONDecodeError: print(f"Response body: {e.response.text}")
        token_info["access_token"] = None
        token_info["expires_at"] = 0
        return None
    except KeyError:
        print("Error: 'access_token' or 'expires_in' not found in the token response.")
        token_info["access_token"] = None
        token_info["expires_at"] = 0
        return None

def get_valid_token():
    """Returns a valid access token, requesting a new one if needed."""
    if token_info["access_token"] and time.time() < token_info["expires_at"]:
        return token_info["access_token"]
    else:
        # print("Token missing or expired.") # Uncomment for debugging
        return get_petfinder_token()

def make_api_call(endpoint, params=None):
    """Makes a GET request to a specified Petfinder API endpoint."""
    access_token = get_valid_token()
    if not access_token:
        print("Cannot make API call: No valid token.")
        return None

    headers = {'Authorization': f'Bearer {access_token}'}
    url = f"{API_BASE_URL}{endpoint}" # Construct full URL

    try:
        # print(f"Calling: {url} with params: {params}") # Uncomment for debugging
        response = requests.get(url, headers=headers, params=params, timeout=15) # Added timeout
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error during API call to {url}: {e}")
        if hasattr(e, 'response') and e.response is not None:
             print(f"Response status: {e.response.status_code}")
             try: print(f"Response body: {e.response.json()}")
             except requests.exceptions.JSONDecodeError: print(f"Response body: {e.response.text}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during API call: {e}")
        return None


'''
# --- Main Execution Example ---
if __name__ == "__main__":
    print("--- Fetching dogs near Milwaukee, WI ---")
    # Remember the current location is Milwaukee, Wisconsin, United States.
    # Current date is Saturday, April 26, 2025.
    search_params = {
        'type': 'dog',
        'location': 'Milwaukee, WI',
        'limit': 5,
        'status': 'adoptable' # Only show adoptable pets
    }
    # Ensure endpoint starts with a slash
    animals_data = make_api_call("/animals", params=search_params)

    if animals_data and animals_data.get("animals"):
        print("\nFound Animals:")
        for i, animal in enumerate(animals_data["animals"]):
            name = animal.get('name', 'N/A')
            breed = animal.get('breeds', {}).get('primary', 'N/A')
            print(f"  {i+1}. {name} ({breed})")
        # print("\nFull response snippet:")
        # print(json.dumps(animals_data['animals'][0], indent=2)) # Print details of the first animal
    elif animals_data:
        print("\nNo animals found matching the criteria.")
    else:
        print("\nFailed to retrieve data from Petfinder API.")
'''