import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def classify_post(comment):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
        with open("tfidf.pkl", "rb") as fv:
            vectorizer = pickle.load(fv)
            print(type(vectorizer))
        x = vectorizer.transform([comment])
        value = model.predict(x)[0]
        return value
    
print(classify_post("fuck"))
print(classify_post("hi"))