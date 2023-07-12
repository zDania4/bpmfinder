import os
import librosa
import pyperclip

def calculate_bpm(file_path):
    # Load the audio file
    audio, sr = librosa.load(file_path)

    # Calculate the tempo (BPM)
    tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)

    return tempo

# Prompt the user to enter the path to the file
music_file_path = input("Enter the path to the file: ")

# Remove surrounding double quotation marks
music_file_path = music_file_path.strip('"')

# Normalize the file path
music_file_path = os.path.normpath(music_file_path)

# Calculate the BPM
bpm = calculate_bpm(music_file_path)

# Round the BPM to the nearest whole number
rounded_bpm = round(bpm)

# Format and output the BPM values
output = f"\nThe BPM of the file is:\nNon-rounded: {bpm}\nRounded: {rounded_bpm}\n"
print(output)

# Copy the rounded BPM to the clipboard
pyperclip.copy(str(rounded_bpm))
print("Rounded BPM copied to clipboard.")
