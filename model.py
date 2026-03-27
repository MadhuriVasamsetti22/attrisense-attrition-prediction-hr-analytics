import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from db import get_connection


def train_model():
    conn = get_connection()
    query = "SELECT age, salary, experience, performance, attrition FROM employees"
    df = pd.read_sql(query, conn)

    if len(df) < 5:
        return "Not enough data"

    X = df[['age', 'salary', 'experience', 'performance']]
    y = df['attrition']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Accuracy
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Save model
    pickle.dump(model, open("attrition_model.pkl", "wb"))

    return f"Model trained successfully. Accuracy: {round(acc*100,2)}%"


def predict_attrition(age, salary, experience, performance):
    model = pickle.load(open("attrition_model.pkl", "rb"))
    prediction = model.predict([[age, salary, experience, performance]])
    return prediction[0]
