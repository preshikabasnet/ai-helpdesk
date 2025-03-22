import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

print("📥 Step 1: Loading CSV...")
try:
    df = pd.read_csv("data/tickets.csv")
    print("✅ CSV loaded successfully.")
except Exception as e:
    print("❌ Error loading CSV:", e)
    exit()

print("🧠 Step 2: Training model...")
try:
    X = df["description"]
    y = df["category"]
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)
    print("✅ Model trained.")
except Exception as e:
    print("❌ Error during model training:", e)
    exit()

print("💾 Step 3: Saving model...")
try:
    joblib.dump(model, "ticket_classifier.pkl")
    print("✅ Model saved successfully.")
except Exception as e:
    print("❌ Error saving model:", e)
