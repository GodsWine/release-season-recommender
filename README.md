
# 🎵 Release Season Recommender

Pick a **tempo (BPM)** and get a suggested **season** to release your track.

## Quick start
```bash
pip install -r requirements.txt
# Train (once) from public datasets placed in the repo root:
# Spotify.csv and top_100_songs_1952_to_20250809.xlsx
python model/train.py

# Run the app
streamlit run app/app.py
