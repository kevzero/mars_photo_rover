import os
import requests # type: ignore
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, ttk
from datetime import datetime

API_KEY = "DEMO_KEY" # Replace with your actual NASA API key
API_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"

def get_mars_photos(rover, earth_date, save_folder):
    params = {
        "earth_date": earth_date,
        "api_key": API_KEY
    }
    url = API_URL.format(rover=rover.lower())
    response = requests.get(url, params=params)

    if response.status_code != 200:
        messagebox.showerror("Error", f"Failed to fetch data: {response.status_code}")
        return

    data = response.json()
    photos = data.get("photos", [])

    if not photos:
        messagebox.showinfo("No Photos", f"No photos found for {rover} on {earth_date}.")
        return

    folder = os.path.join(save_folder, f"{rover}_{earth_date}")
    os.makedirs(folder, exist_ok=True)

    for idx, photo in enumerate(photos):
        img_url = photo["img_src"]
        camera_name = photo["camera"]["full_name"].replace(" ", "_")
        filename = os.path.join(folder, f"{rover}_{earth_date}_{camera_name}_{idx}.jpg")

        try:
            img_data = requests.get(img_url).content
            with open(filename, 'wb') as f:
                f.write(img_data)
        except Exception as e:
            print(f"Error saving image {img_url}: {e}")

    messagebox.showinfo("Download Complete", f"Downloaded {len(photos)} photos to:\n{folder}")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        save_path_var.set(folder)

def start_download():
    rover = rover_var.get()
    date = date_entry.get()
    folder = save_path_var.get()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
        return

    if not folder:
        messagebox.showerror("Missing Folder", "Please choose a folder to save the images.")
        return

    get_mars_photos(rover, date, folder)

# === Interfaccia grafica ===
root = tk.Tk()
root.title("Mars Rover Photo Downloader")

ttk.Label(root, text="Select Rover:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
rover_var = tk.StringVar(value="curiosity")
ttk.Combobox(root, textvariable=rover_var, values=["curiosity", "opportunity", "perseverance"]).grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Earth Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
date_entry = ttk.Entry(root)
date_entry.insert(0, "2022-07-01")
date_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Save Folder:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
save_path_var = tk.StringVar()
ttk.Entry(root, textvariable=save_path_var, width=30).grid(row=2, column=1, padx=10, pady=5)
ttk.Button(root, text="Browse", command=browse_folder).grid(row=2, column=2, padx=10, pady=5)

ttk.Button(root, text="Download Photos", command=start_download).grid(row=3, column=0, columnspan=3, pady=15)

root.mainloop()
