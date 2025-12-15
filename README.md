## Is there a right time to release a song to make it a Top 10 Hit??🎵🎵🎵

New to Data Science, as a fun project to test my skills, I have used publicly available data to try and see what can be created to allow users to find out which time of the year would be best to release their song.

📄 Project Summary🎵

This project analyses Spotify playlist data and the UK Top 100 songs since 1952.
The revised notebook, 251215 Final_Notebook (1).ipynb, guides users through the following steps:

Imports and merges Spotify and UK Top 100 datasets.

Cleans and standardises the data, including normalising song and artist names.

Combines multiple sheets from the UK Top 100 Excel file into a single dataset.

Merges datasets to identify which Spotify songs appeared in the UK Top 10.

Converts and maps dates to seasons (Winter, Spring, Summer, Autumn).

Performs exploratory analysis such as frequency distributions and summary statistics.

Highlights top artists with the most UK Top 10 hits.

Scales song duration for further analysis.

## Updated Notebook
[View the revised notebook here](notebooks/251215%20Final_Notebook%20(1).ipynb)

This data has then been used to create a fun model below!!

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

















