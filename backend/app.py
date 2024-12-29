from flask import Flask, request, jsonify
from ml_model import HerbalRecommendationSystem
from flask_cors import CORS
import os

app = Flask(__name__)

# Dynamic CORS configuration based on environment
FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:5173')
ALLOWED_ORIGINS = [
    FRONTEND_URL,
    'http://localhost:5173',
    'http://localhost:3000',
    'http://localhost:5000'
]

CORS(app, resources={
    r"/*": {
        "origins": [
            "https://*.vercel.app",
            "http://localhost:5173",
            "http://localhost:3000"
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize the herbal recommendation system
herbal_system = HerbalRecommendationSystem()

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/recommend', methods=['POST'])
def get_recommendations():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        symptoms = data.get('symptoms', [])
        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400
        
        # Get recommendations from the ML model
        recommendations = herbal_system.get_recommendations(symptoms)
        
        return jsonify({
            "success": True,
            "recommendations": recommendations
        }), 200
        
    except Exception as e:
        print(f"Error in get_recommendations: {str(e)}")  # Server-side logging
        return jsonify({
            "success": False,
            "error": "Internal server error",
            "message": str(e)
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)