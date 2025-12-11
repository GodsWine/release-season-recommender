
# Ensure 'model' package imports work on Streamlit Cloud
import sys, os
from pathlib import Path

# Add the repository root to sys.path so 'model' is importable
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(REPO_ROOT))

from model.pipeline import load_model, predict, NotFittedModel


import streamlit as st
from model.pipeline import load_model, predict, NotFittedModel

st.set_page_config(page_title='Release Season Recommender', page_icon='🎵', layout='centered')
st.title('🎵 Release Season Recommender')
st.caption('Move the sliders, then click Recommend.')

# Convert duration from ms to mm:ss for display
def format_duration(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    return f"{minutes}:{seconds:02d}"

# Sliders with tooltips
tempo = st.slider('Tempo (BPM)', 60, 200, 120, 1, help="Speed of the track in beats per minute.")
duration_ms = st.slider('Duration (ms)', 60_000, 300_000, 180_000, 1000,
                        help="Track length in milliseconds. Example: 180000 ms = 3:00.")
st.caption(f"Selected duration: {format_duration(duration_ms)} (mm:ss)")

danceability = st.slider('Danceability', 0.0, 1.0, 0.50, 0.01,
                          help="Suitability for dancing (0 = least, 1 = most).")
energy = st.slider('Energy', 0.0, 1.0, 0.50, 0.01,
                   help="Intensity and activity (0 = calm, 1 = energetic).")
valence = st.slider('Valence', 0.0, 1.0, 0.50, 0.01,
                    help="Musical positivity (0 = sad/tense, 1 = happy/euphoric).")
acousticness = st.slider('Acousticness', 0.0, 1.0, 0.50, 0.01,
                         help="Probability the track is acoustic (0 = electronic, 1 = acoustic).")
instrumentalness = st.slider('Instrumentalness', 0.0, 1.0, 0.00, 0.01,
                              help="Likelihood the track has no vocals (0 = vocal-heavy, 1 = instrumental).")

features = [tempo, duration_ms, danceability, energy, valence, acousticness, instrumentalness]

try:
    model = load_model()
    if st.button('Recommend season'):
        season, conf = predict(model, features)
        st.success(f'Recommended season: **{season}**')
        if conf is not None:
            st.progress(int(conf * 100))
            st.caption(f'Confidence: {conf:.2f}')
except NotFittedModel:
    st.warning("Model artifact not found. Please train locally or upload artifact for predictions.")




