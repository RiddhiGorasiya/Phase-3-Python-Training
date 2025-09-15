# 1. Input: A list of file download URLs (PDFs, images, etc.)

import threading
import requests
import os

# Function to download a file
def download_file(url, folder="file1"):
    try:
        # Create folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # File name = last part of the URL
        filename = os.path.join(folder, url.split("/")[-1])

        print(f"Downloading: {filename}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error if download fails

        # Save file
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Finished: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# List of URLs to download (make sure they are direct links!)
urls = [
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "https://images.pexels.com/photos/1933239/pexels-photo-1933239.jpeg?cs=srgb/Sample1-jpg-image-500kb.jpg",
    "https://images.pexels.com/photos/1519088/pexels-photo-1519088.jpeg?cs=srgb/Sample2-jpg-image-500kb.jpg" 
]

# Create and start threads
threads = []
for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All downloads completed!")

# **********************************************************

# 2. Use AsyncIO to initiate concurrent download requests

import os
import aiohttp
import asyncio

# Function to download a file asynchronously
async def download_file(session, url, folder="file2"):
    try:
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, url.split("/")[-1])
        print(f"Downloading: {filename}")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/115.0 Safari/537.36"
        }

        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            with open(filename, "wb") as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

        print(f"Finished: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Main function to manage tasks
async def main():
    urls = [
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "https://images.pexels.com/photos/1324803/pexels-photo-1324803.jpeg?_gl=1*1bhqhbc*_ga*OTMxOTg5MTkuMTc1NzkyNjU5NQ..*_ga_8JE65Q40S6*czE3NTc5MjY1OTUkbzEkZzEkdDE3NTc5MjcxNzQkajU3JGwwJGgw.jpg/Sample1-jpg-image-500kb.jpg",
        "https://images.pexels.com/photos/884788/pexels-photo-884788.jpeg?_gl=1*1pdn3y0*_ga*OTMxOTg5MTkuMTc1NzkyNjU5NQ..*_ga_8JE65Q40S6*czE3NTc5MjY1OTUkbzEkZzEkdDE3NTc5MjcyMzkkajU2JGwwJGgw.png/Sample2-png-image-500kb.png"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url) for url in urls]
        await asyncio.gather(*tasks)

# Run the program
if __name__ == "__main__":
    asyncio.run(main())

# **********************************************************

# 3. Use threading to write multiple files to disk simultaneously

import threading
import os

# Function to write data into a file
def write_file(filename, data, folder="file3"):
    try:
        os.makedirs(folder, exist_ok=True)  # Create folder if not exists
        filepath = os.path.join(folder, filename)

        print(f"Writing: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(data)

        print(f"Finished writing: {filepath}")
    except Exception as e:
        print(f"Error writing {filename}: {e}")


def main():
    # Data for multiple files
    files_data = {
        "file1.txt": "Hello, this is content for File 1.",
        "file2.txt": "Python threading is cool!",
        "file3.txt": "Writing multiple files at the same time."
    }

    threads = []
    for filename, data in files_data.items():
        t = threading.Thread(target=write_file, args=(filename, data))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All files written successfully!")


if __name__ == "__main__":
    main()

# **********************************************************

# 4. Implement retry logic with try-except for failed downloads

# **********************************************************

# 5. Use pickle to save download metadata (filename, URL, status, timestamp)