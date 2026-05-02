import joblib

def predict(text):
    model = joblib.load('../model/model.pkl')

    result = model.predict([text])[0]

    return result