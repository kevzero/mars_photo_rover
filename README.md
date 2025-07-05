Mars Rover Photo Downloader
This Python script allows users to download photos taken by NASA's Mars Rovers (Curiosity, Opportunity, Perseverance) on a specific Earth date. It uses the official NASA Mars Rover Photos API and saves the downloaded images into a local folder named after the rover and date.

Features
Choose which rover to query (Curiosity, Opportunity, Perseverance)

Enter any valid Earth date (format: YYYY-MM-DD)

Downloads all available images taken on that date by the selected rover

Saves images in a structured folder: mars_photos/{rover}_{date}

Prints status messages for each image downloaded or skipped

Requirements
Python 3.x

requests library (install with: pip install requests)

How to Use
Run the script using: python script_name.py

Enter the name of the rover when prompted

Enter the desired Earth date (e.g., 2025-07-01)

The script will connect to NASA's API, download available images, and save them in a local folder.

Example Output
If you select "curiosity" and the date "2025-07-01", the script will download all available images for that rover and date into the folder: mars_photos/curiosity_2025-07-01/

Each file is named using the rover, date, camera name, and index, like: curiosity_2025-07-01_Navigation_Camera_0.jpg

Notes
If no images are found for the given date, the script will notify you.

If there are connection issues or NASA's API is down, an error message will be shown.

The default API key used is "DEMO_KEY", which has rate limits. You can get your own key for free at https://api.nasa.gov

License
This script is provided for educational and demonstration purposes. You are free to use, modify, and distribute it as needed.

Tutto in una sola finestra, come richiesto. Fammi sapere se vuoi anche il file .txt.
