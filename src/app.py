from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Sample data (you can replace this with your actual dataset)
data = {
    'plant_name': ['Tulsi', 'Ginger', 'Licorice', 'Turmeric', 'Neem'],
    'health_benefits': ['Skin Health, Immunity Booster', 'Digestive Aid, Skin Health', 
                        'Skin Health, Digestive Aid', 'Hair Strengthening, Anti-inflammatory', 
                        'Blood Purifier, Skin Health']
}

df = pd.DataFrame(data)

@app.route('/recommend', methods=['GET'])
def recommend():
    plant = request.args.get('plant')
    # Add logic for plant recommendation
    if plant:
        recommendations = df[df['plant_name'].str.contains(plant, case=False)]
        return jsonify(recommendations.to_dict(orient='records'))
    else:
        return jsonify({'error': 'Plant name is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
