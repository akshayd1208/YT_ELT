import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():



    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        #print(json.dumps(data, indent=4))

        items = data.get("items")
        if not items:
            raise ValueError(f"No channel found for handle: {CHANNEL_HANDLE}")

        channel_items = items[0]
        channel_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlist_id)

        return channel_playlist_id

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()



     
