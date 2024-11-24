import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
import joblib

class RecommendationEngine:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.mlb = MultiLabelBinarizer()
        self.model = RandomForestClassifier()

    def preprocess_data(self):
        # Preprocessing logic
        features = self.mlb.fit_transform(self.data['conditions'])
        labels = self.data['medicine']
        return features, labels

    def train_model(self):
        features, labels = self.preprocess_data()
        self.model.fit(features, labels)
        joblib.dump(self.model, 'recommendation_model.pkl')

    def recommend(self, user_conditions):
        conditions_vector = self.mlb.transform([user_conditions])
        predictions = self.model.predict(conditions_vector)
        return predictions
