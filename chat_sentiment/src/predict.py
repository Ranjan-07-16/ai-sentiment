import joblib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "model", "model.pkl")

model = joblib.load(model_path)

def predict(text):

    result = model.predict([text])[0]

    return result