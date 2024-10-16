import os
import requests

# URL of the aaindex1 file stored in a variable
AAIINDEX1 = 'https://www.genome.jp/ftp/db/community/aaindex/aaindex1'
TARGET = '/mnt/data/aaindex/'

# Specify the local filename to save the file
local_filename = "aaindex1.txt"

def download_file(url, target_dir, local_filename):
    # Ensure the target directory exists, create it if it doesn't
    os.makedirs(target_dir, exist_ok=True)
    
    # Full path to save the file
    file_path = os.path.join(target_dir, local_filename)
    
    # Make the request
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary write mode and write the response content to it
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"File downloaded successfully and saved to '{file_path}'.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

# Call the function to download the file to the target directory
download_file(AAIINDEX1, TARGET, local_filename)
