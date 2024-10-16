import requests
import os
import time
from farcaster import Warpcast
from dotenv import load_dotenv

load_dotenv()

# Load Farcaster mnemonic securely from environment variables
MNEMONIC = os.getenv("WARPCAST_MNEMONIC")  
# Neynar API endpoint for fetching trending meme casts
FETCH_URL = "https://api.neynar.com/v2/farcaster/feed/trending?limit=3&time_window=24h&channel_id=memes"

# Initialize Warpcast client with mnemonic
client = Warpcast(mnemonic=MNEMONIC)

def fetch_and_process_images():
    """
    Fetch trending meme casts from Neynar API, post a comment on Farcaster, and like the posted comment.
    """
    headers = {
        "accept": "application/json",
        "api_key": "NEYNAR_API_DOCS" ,  # API key
        "User-Agent": "Mozilla/5.0"
    }

    try:
        # Fetch trending meme casts
        response = requests.get(FETCH_URL, headers=headers)
        response.raise_for_status()

        # Parse the response JSON
        casts = response.json().get('casts', [])

        for cast in casts:
            # Post a comment on the cast
            comment_response = client.post_cast(
                text="TRENDING CASTS OF THE DAY @nonlinear.eth", 
                parent={"hash": cast["hash"], "fid": cast["author"]["fid"]}
            )
            print(f"Posted Comment Hash: {comment_response.cast.hash}")

            # Like the posted comment
            like_response = client.like_cast(comment_response.cast.hash)
            if like_response:
                print(f"Liked Comment Hash: {comment_response.cast.hash}")

    except requests.RequestException as e:
        print(f"Error fetching or processing data: {e}")

def main():
    """
    Main function that fetches trending memes every 24 hours.
    """
    while True:
        print("Fetching and processing trending meme casts...")
        fetch_and_process_images()
        print("Waiting for 24 hours before the next fetch...")
        time.sleep(24 * 60 * 60)  # Sleep for 24 hours

if __name__ == "__main__":
    main()
