# EcoAyur: Herbal Medicine Recommendation System

EcoAyur is a web application built to recommend herbal remedies based on user-input symptoms. The system integrates **web scraping** for gathering herbal data, **machine learning** for predicting herbal remedies, and **data visualization** for presenting crop-related statistics. It also supports multilingual capabilities (English, Hindi, Telugu) and offers an interactive user interface.

## Key Technologies and Libraries

### Frontend:
- **React.js**: Core frontend framework for building user interfaces using functional components and React Hooks (useState).
- **Chart.js & React-chartjs-2**: Used for data visualization with interactive pie charts.
- **CSS**: Custom styling for the user interface.
  - Responsive design utilizing **Flexbox** and **Grid layouts**.
  - Mobile-friendly layout with adaptive styling.
- **React Router**: For navigation between different views in the application.
- **Axios**: For making HTTP requests to the backend API.

### Backend:
- **Flask**: Python web framework for building the backend API.
- **NumPy & Pandas**: Data manipulation and numerical computation libraries.
- **scikit-learn**: Machine learning library for training models.
  - **RandomForestClassifier**: Used for crop prediction and herbal remedy recommendations.
- **Flask-CORS**: Cross-Origin Resource Sharing handling.
- **Joblib**: Used for serializing and saving the trained machine learning models.
  
### Machine Learning:
- **Random Forest**: A machine learning model for multi-label classification.
- **Web Scraping**: Scrapes additional herbal data using **requests** and **BeautifulSoup**.
- **Text Vectorization (TF-IDF)**: For processing and analyzing textual symptom data.

### Features:
- **Multilingual Support**: The app is available in multiple languages—English, Hindi, and Telugu.
- **Form Components**:
  - Dropdown selectors for choosing crops, herbs, etc.
  - Dynamic form handling to display the relevant information.
- **Data Visualization**:
  - Pie charts for displaying crop suitability and herb effectiveness.
  - Interactive tooltips to make charts more informative.
  - Responsive design to ensure charts adapt to various screen sizes.
- **State Management**:
  - Using `useState` for managing form data, language selection, and dynamic UI updates.
  
### Data Structure:
- **Crop Database**:
  - Nested objects for crops categorized by soil type, climate, and water availability.
  - Detailed crop information including suitability ratings, growing tips, benefits, market trends, and current prices.
  
### Project Structure:
```bash
- frontend/                   # React.js frontend
    - public/
    - src/
    - package.json
    - index.html
- backend/                    # Flask backend
    - api/
    - app.py
    - requirements.txt
    - model/
    - static/
    - templates/
