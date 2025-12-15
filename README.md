
## 📓 View the Analysis Notebook

[Open the full notebook here »](251215_Final_Notebook.ipyn[Open the full notebook here »](251215_Final_Notebook.ipynb)


# 🎵 Release Season Recommender
Predict the best season for a music release based on audio features.

## Try it online
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen)](https://release-season-recommender-exsy9fvlgmr9dymnp5wc4f.streamlit.app)

## 🎵 Audio Features Explained

| Feature          | Range      | Description                                                                 |
|------------------|-----------|-----------------------------------------------------------------------------|
| **Tempo**        | BPM       | Speed of the track in beats per minute.                                    |
| **Duration**     | mm:ss     | Track length (converted from milliseconds).                                |
| **Danceability** | 0.0–1.0   | How suitable the track is for dancing, based on tempo, rhythm stability, beat strength. |
| **Energy**       | 0.0–1.0   | Intensity and activity; high = loud, fast, energetic.                      |
| **Valence**      | 0.0–1.0   | Musical positivity; high = happy/euphoric, low = sad/tense.                |
| **Acousticness** | 0.0–1.0   | Probability the track is acoustic; high = mostly acoustic instruments.     |
| **Instrumentalness** | 0.0–1.0 | Likelihood the track has no vocals; high = instrumental only.             |

> All features except Tempo and Duration are normalised between 0 and 1 by Spotify’s audio analysis API.

## Run locally
```bash
pip install -r requirements.txt
python model/train.py
streamlit run app/app.py




