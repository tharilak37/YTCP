import json

# File paths
input_json_file = "input.json"  # Replace with your JSON file name
output_txt_file = "image_links.txt"

def extract_s88_links(json_file, output_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        s88_links = []
        for entry in data:
            link = entry.get("link", "")
            if "s88" in link:
                s88_links.append(link)
      
        with open(output_file, "w", encoding="utf-8") as file:
            for link in s88_links:
                file.write(link + "\n")
        
        print(f"Extracted {len(s88_links)} 's88' links and saved them to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
extract_s88_links(input_json_file, output_txt_file)
