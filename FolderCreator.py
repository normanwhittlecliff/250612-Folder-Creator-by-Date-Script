import os
import shutil

print("Starting script...")

# Path to your camera folder
camera_folder = r"C:\Users\Norman Whittlecliff\Pictures\Phone Storage\camera"

# Create an output folder (you can use the same as camera_folder if you prefer)
output_folder = camera_folder

# Loop through files in the camera folder
for filename in os.listdir(camera_folder):
    filepath = os.path.join(camera_folder, filename)

    # Skip if it's not a file
    if not os.path.isfile(filepath):
        continue

    # Ensure filename has the expected format
    # Example: 20241201_221258.jpg
    if len(filename) >= 15 and (filename[8] == "_" or filename[8] == "-"):
        try:
            year = filename[2:4]   # YY
            month = filename[4:6]  # MM
            day = filename[6:8]    # DD

            # Format the date folder name: YY-MM-DD
            date_folder = f"{year}-{month}-{day}"

            # Create target folder if it doesn't exist
            target_folder = os.path.join(output_folder, date_folder)
            os.makedirs(target_folder, exist_ok=True)

            # Move file
            shutil.move(filepath, os.path.join(target_folder, filename))
            print(f"Moved: {filename} -> {date_folder}")

        except Exception as e:
            print(f"Skipping {filename}: {e}")
    else:
        print(f"Skipping {filename}: invalid format")

input("Press enter to end script...")
