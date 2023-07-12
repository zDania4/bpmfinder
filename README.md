# BPMFinder
A very simple BPM finder written in Python, made because of the lack of a x64 upgrade for *Foobar2000*s *BPM Analyzer* plugin. It was initially written purely for usage on FLACs, but it should work with all filetypes supported by `librosa`.

## Installation
BPMFinder requires `librosa` - to analyse the file - and `pyperclip` - to allow for the output being copied to the clipboard.
You can install it by using: `pip install -r requirements.txt` or `pip install librosa pyperclip`.

## Running
Run the script using `py bpmfinder.py`. The script will ask for the location of the file in question, which you can either paste or type in - do make sure it points **directly** to the FLAC file in question. The BPM will then be rounded to the nearest value and copied to the clipboard.
