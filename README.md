
# Meme Trending Farcaster Bot

This Python script fetches trending meme casts from the Neynar API, posts a comment on each cast, and likes the comment using the Farcaster API.

## Features

- Fetch trending meme casts from Neynar API.
- Post a comment on each trending meme cast.
- Like the posted comment.

## Setup

### Prerequisites

- Python 3.x
- A virtual environment (venv)
- API keys for both Neynar and Farcaster (WARPCAST_MNEMONIC)

### Installation

1. Clone the repository or download the script.
      ```bash
   git clone https://github.com/rahulrock213/Trending_Memes.git && cd Trending_Memes
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up your environment variables:
   - Create a `.env` file in the root of your project.
   - Add your Farcaster mnemonic and Neynar API key:
     ```bash
     WARPCAST_MNEMONIC="your-mnemonic"  #add your wrapcaster mnemonic
     ```

### Usage

1. Run the script:
   ```bash
   python main.py
   ```

#Enjoy :)
