
import streamlit as st
from model.pipeline import load_model, predict, NotFittedModel

st.set_page_config(page_title='Release Season Recommender', page_icon='🎵', layout='centered')
st.title('🎵 Release Season Recommender')
st.caption('Move the sliders, then click Recommend.')

# Sliders for numeric features
tempo = st.slider('Tempo (BPM)', 60, 200, 120, 1)
duration_ms = st.slider('Duration (ms)', 60_000, 300_000, 180_000, 1000)
danceability = st.slider('Danceability', 0.0, 1.0, 0.50, 0.01)
energy = st.slider('Energy', 0.0, 1.0, 0.50, 0.01)
valence = st.slider('Valence', 0.0, 1.0, 0.50, 0.01)
acousticness = st.slider('Acousticness', 0.0, 1.0, 0.50, 0.01)
instrumentalness = st.slider('Instrumentalness', 0.0, 1.0, 0.00, 0.01)

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
    st.info('No trained model found yet. Place the public datasets in the repo root and run `python model/train.py` to create `model/artifacts.pkl`. Then re-run the app.')
