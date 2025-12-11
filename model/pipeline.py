
from pathlib import Path
import joblib
import numpy as np

ARTIFACT_PATH = Path(__file__).parent / 'artifacts.pkl'

class NotFittedModel(Exception):
    pass

def load_model():
    if not ARTIFACT_PATH.exists():
        raise NotFittedModel('artifacts.pkl not found. Run model/train.py first.')
    return joblib.load(ARTIFACT_PATH)

# Expect features in this order:
# ['tempo','duration_ms','danceability','energy','valence','acousticness','instrumentalness']
def predict(model, features: list[float]):
    X = np.array([features], dtype=float)  # shape (1, n_features)
    label = model.predict(X)[0]
    conf = None
    if hasattr(model, 'predict_proba'):
        conf = float(max(model.predict_proba(X)[0]))
    return str(label), conf
