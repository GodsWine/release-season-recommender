
# model/train.py
from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Paths
ROOT = Path(__file__).resolve().parents[1]
SPOTIFY_PATH = ROOT / "Spotify.csv"  # your actual file name
ARTIFACT_PATH = Path(__file__).parent / "artifacts.pkl"

# Helper: month → season
def month_to_season(month: int) -> str:
    if month in (12, 1, 2): return "Winter"
    if month in (3, 4, 5): return "Spring"
    if month in (6, 7, 8): return "Summer"
    if month in (9, 10, 11): return "Autumn"
    return "Unknown"

# Load data
print("Loading Spotify data...")
df = pd.read_csv(SPOTIFY_PATH)

# Derive month and season
if "release_date" in df.columns:
    dt = pd.to_datetime(df["release_date"], errors="coerce")
    df["month"] = dt.dt.month
else:
    df["month"] = pd.NA

df["season"] = df["month"].apply(lambda m: month_to_season(int(m)) if pd.notna(m) else "Unknown")

# Features
NUM_FEATURES = ["tempo", "duration_ms", "danceability", "energy", "valence", "acousticness", "instrumentalness"]

# Filter rows
mask = df["season"].ne("Unknown")
X = df.loc[mask, NUM_FEATURES].fillna(0)
y = df.loc[mask, "season"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Pipeline
clf = Pipeline([
    ("scale", StandardScaler()),
    ("lr", LogisticRegression(max_iter=1000, multi_class="auto"))
])

print("Training model...")
clf.fit(X_train, y_train)

# Save artifact
joblib.dump(clf, ARTIFACT_PATH)
print(f"Saved model to {ARTIFACT_PATH}")
print(f"Validation accuracy: {clf.score(X_test, y_test):.3f}")
