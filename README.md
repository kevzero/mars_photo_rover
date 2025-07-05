# Mars Rover Photo Downloader

This Python program allows you to download real images taken by NASA’s Mars rovers (Curiosity, Opportunity, and Perseverance) for a specific Earth date. It uses the official NASA Mars Rover Photos API and stores the images locally in organized folders.

## Features

- Choose the Mars rover (`curiosity`, `opportunity`, or `perseverance`)
- Enter a specific Earth date (in format `YYYY-MM-DD`)
- Downloads all available photos for that date
- Saves the images in a local folder named `mars_photos/ROVER_DATE`
- Displays the download progress in the terminal

## How to Use

1. Make sure Python 3 is installed on your system.
2. Install the `requests` library if it's not already installed:
   `pip install requests`
3. Run the script:
   `python mars_rover_downloader.py`
4. When prompted:
   - Enter the rover name (e.g. `curiosity`)
   - Enter the Earth date (e.g. `2025-07-05`)
5. The program will download all the available images for that date into a folder.

## Output Example

If photos are found:
📷 Found 15 photos. Downloading...
✅ Saved: mars_photos/curiosity_2025-07-05/Curiosity_2025-07-05_Front_Hazcam_0.jpg

If no photos are found:
📭 No photos found for perseverance on 2025-07-01.

## Folder Structure

    curiosity_2025-07-05/

      • curiosity_2025-07-05_Front_Hazard_Avoidance_Camera_0.jpg
      • curiosity_2025-07-05_Front_Hazard_Avoidance_Camera_1.jpg
      • curiosity_2025-07-05_Navigation_Camera_2.jpg
      • curiosity_2025-07-05_Mast_Camera_3.jpg
      • ...

## API Key

By default, the script uses NASA’s public `DEMO_KEY`, which is rate-limited. To avoid issues, register for a free API key at https://api.nasa.gov and replace the value of `API_KEY` in the script.

## License

This script is free for educational and personal use. Created to explore space data using Python and promote scientific curiosity.
