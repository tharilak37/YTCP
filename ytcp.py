import os
import requests
from zipfile import ZipFile

# File paths
image_links_file = "image_links.txt"  #Grab the links, to collect links automatically, use the Chrome extension to copy links to JSON format. and use our JSON to comment link extractor tool and insert the downloaded json file. run it, and you will get the image links text file.
updated_links_file = "updated_image_links.txt"
output_zip = "downloaded_images.zip"  #unizip the generated zip file, you will get all your images on it

def replace_links(input_file, output_file):
    """
    Replaces all occurrences of '/s88' with '/s800' in the given file.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        updated_lines = [line.replace("=s88", "=s800") for line in lines]

        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        print(f"Successfully updated links in '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_images(links_file, zip_name):
    """
    Downloads images from the links in the given file and saves them in a ZIP file.
    """
    with open(links_file, "r", encoding="utf-8") as file:
        links = [line.strip() for line in file.readlines()]

    with ZipFile(zip_name, "w") as zipf:
        for idx, url in enumerate(links, start=1):
            try:
                # Download the image
                response = requests.get(url, stream=True)
                response.raise_for_status()
                img_name = f"image_{idx}.jpg"

                # Save the image temporarily
                with open(img_name, "wb") as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)

                # Add to the ZIP file
                zipf.write(img_name)
                os.remove(img_name)  # Clean up after adding to the ZIP
                print(f"Downloaded and added to ZIP: {img_name}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")

    print(f"All images saved to '{zip_name}'.")

# Replace links
replace_links(image_links_file, updated_links_file)

# Download updated images
if os.path.exists(updated_links_file):
    download_images(updated_links_file, output_zip)
else:
    print(f"Updated links file '{updated_links_file}' not found. Cannot proceed with downloads.")
