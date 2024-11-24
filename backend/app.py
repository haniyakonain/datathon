from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import random
from web_scraper import MedicineScraper

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Sample data (replace with your actual data or logic)
plant_data = {
    'plant_name': [
        'Tulsi', 'Ginger', 'Licorice', 'Turmeric', 'Neem', 
        'Brahmi', 'Fenugreek', 'Amla', 'Ashwagandha'
    ],
    'health_benefits': [
        ['Skin Health', 'Immunity Booster'], 
        ['Skin Health', 'Digestive Aid'], 
        ['Skin Health', 'Digestive Aid'], 
        ['Hair Strengthening', 'Anti-inflammatory'], 
        ['Blood Purifier', 'Skin Health'], 
        ['Stress Relief', 'Brain Health'],
        ['Hair Growth', 'Digestive Aid'],
        ['Immunity Booster', 'Blood Purifier'],
        ['Energy Boost', 'Anti-stress']
    ]
}

# Convert to DataFrame
df = pd.DataFrame(plant_data)

# Initialize the MedicineScraper
scraper = MedicineScraper()

# Route for home
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Ayurvedic Remedy API!"})

# Route for getting Ayurvedic plant recommendations based on input symptoms
@app.route('/api/recommendation', methods=['GET'])
def get_recommendation():
    symptoms = request.args.get('symptoms', default="", type=str)
    
    # Example logic: Filter based on symptoms (you can add more complex logic here)
    recommendations = []

    if symptoms:
        for index, row in df.iterrows():
            # Check if any health benefit matches the input symptoms
            if any(symptom.lower() in " ".join(row['health_benefits']).lower() for symptom in symptoms.split(',')):
                recommendations.append({
                    'plant_name': row['plant_name'],
                    'health_benefits': row['health_benefits']
                })
    
    # If no matches, return a random set of plants as recommendations
    if not recommendations:
        recommendations = random.sample(df.to_dict(orient="records"), 3)

    return jsonify({"recommendations": recommendations})

# Route to get detailed information about a specific plant
@app.route('/api/plant/<plant_name>', methods=['GET'])
def get_plant_info(plant_name):
    plant_info = df[df['plant_name'].str.lower() == plant_name.lower()]
    
    if plant_info.empty:
        return jsonify({"error": "Plant not found"}), 404
    
    # Return plant details
    plant_details = plant_info.to_dict(orient='records')[0]
    return jsonify(plant_details)

# Route to scrape products from an e-commerce site based on a search query
@app.route('/api/scrape_products', methods=['GET'])
def scrape_products():
    search_term = request.args.get('search_term', type=str)
    
    if not search_term:
        return jsonify({"error": "Search term is required"}), 400
    
    # Use MedicineScraper to fetch products based on the search term
    products = scraper.scrape_products(search_term)
    
    if not products:
        return jsonify({"error": "No products found"}), 404
    
    return jsonify({"products": products})

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
