import pandas as pd
from model import build_model
from preprocessing import clean_text
import joblib

df = pd.read_csv('../dataset/data.csv')

df['text'] = df['text'].apply(clean_text)

model = build_model()

model.fit(df['text'], df['rating'])

joblib.dump(model, '../model/model.pkl')