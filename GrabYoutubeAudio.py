# Arthur Powers
# Started 8/5/2022

# Using Python 3.10.0


################################### IMPORTS #####################################

import os
import sys
import subprocess

# Attempt to import pytube, install if it doesn't exist
try:
    from pytube import YouTube
except ModuleNotFoundError:

    print("Module not found: pytube. Installing pytube")
    subprocess.call([sys.executable, "-m", "pip", "install", "pytube"])
    print("Pytube installation complete. ")

    from pytube import YouTube

##################################### MAIN ######################################

def main():

    file_ext = ["mp4", "mp3"]

    #Grabs a youtube video from given URL
    url = input("Youtube URL: ").strip()
    try:
        video = YouTube(url)
    except :
        print(f"Could not grab video: {url}")
        return
        
    #Prompt user to select audio
    audio = video.streams.get_audio_only()
    print(f"Retrieving {audio.mime_type}: {audio.title}")

    # Set default download path

    download_path = os.path.expanduser(os.sep.join(["~", "Downloads"]))
    
    download_path_exists = os.path.exists(download_path)
    default_download_msg = f" ({download_path}):" if download_path_exists else ":"
    
    # Prompt user to change download path
    user_download_path = input(f'Download path{ default_download_msg } ').strip()

    if user_download_path != "" and not os.path.exists(user_download_path):
        print(f"Could not find location: {user_download_path}")
        return
    
    # Download Youtube audio
    final_download_path = download_path if user_download_path == "" else user_download_path
    audio.download(final_download_path)
    print(f"Saved audio to {final_download_path}")


if __name__ == "__main__":
    main()