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
```

## Backend Functionality:

### Herbal Recommendation System:
- **Scrapes herbal data** from external sources (e.g., NCCIH, BSI, NGDC).
- **Loads and processes data** from CSV files.
- **Uses a Random Forest Classifier** to recommend herbal remedies based on symptoms.

### Recommendation Flow:
1. **Load data, clean and prepare it.**
2. **Train the model** and predict the best herb(s) for given symptoms.
3. **Return herbal recommendations** with preparation instructions and dosage.

### Testing:
- **Machine Learning Model**:
  - Test the model with sample data to ensure its predictions are accurate.
- **Web Scraping**:
  - Verify that the data scraping functionality is properly collecting herbal information.
- **Recommendation System**:
  - Check the robustness of the recommendation system by testing with different symptoms.

# EcoAyur: Herbal Medicine Recommendation System

## Installation and Setup

### Backend Setup (Flask):

1. **Clone the repository**:
   ```bash
   git clone git@github.com:haniyakonain/ecoayur.git
   cd ecoayur/backend
   ```

2. **Create and activate a Python virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**:
   ```bash
   python app.py
   ```

### Frontend Setup (React):

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install the required dependencies**:
   ```bash
   npm install
   ```

3. **Run the frontend in development mode**:
   ```bash
   npm run dev
   ```

### Running the Full Application:
1. Ensure both frontend and backend servers are running.
2. Open a browser and navigate to [http://localhost:3000](http://localhost:3000) for the frontend.

## Project Structure

### Backend Functionality:
- **Herbal Recommendation System**:
  - Scrapes herbal data from external sources (e.g., NCCIH, BSI, NGDC).
  - Loads and processes data from CSV files.
  - Uses a Random Forest Classifier to recommend herbal remedies based on symptoms.

- **Recommendation Flow**:
  - Load data, clean and prepare it.
  - Train the model and predict the best herb(s) for given symptoms.
  - Return herbal recommendations with preparation instructions and dosage.

- **Testing**:
  - **Machine Learning Model**: Test the model with sample data to ensure its predictions are accurate.
  - **Web Scraping**: Verify that the data scraping functionality is properly collecting herbal information.
  - **Recommendation System**: Check the robustness of the recommendation system by testing with different symptoms.

### Frontend Functionality:
- **React.js**:
  - Core frontend framework with functional components.
  - Uses React Hooks (`useState`) for state management.
  - Implements multilingual support for multiple languages (English, Hindi, Telugu).
  - Utilizes Chart.js and React-chartjs-2 for data visualization.

- **Form Components**:
  - Dropdown selectors for symptom input.
  - Dynamic form handling to collect user data.

- **Responsive Design**:
  - Mobile-friendly layout with flexible containers.
  - Adaptive styling using Flexbox and Grid layouts.

## Key Features of the Application

### Herbal Recommendation System:

- **Machine Learning-based Recommendations**: 
  - The system recommends herbal remedies based on symptoms entered by the user. It predicts the most appropriate herbs and provides instructions and recipes.

- **Web Scraping**:
  - The app scrapes herbal data from trusted sources like NCCIH, BSI, and NGDC to enhance the recommendation system.

- **Multilingual Support**:
  - The app supports multiple languages, enabling a wider range of users.

### User Interface:

- **Interactive Forms**:
  - The frontend features dropdown selectors and dynamic form handling for collecting user symptoms.

- **Data Visualization**:
  - Using Chart.js, the app displays various charts such as pie charts, bar graphs, and line graphs for market trends, crop yield, and weather data.

- **Responsive Design**:
  - The UI adapts seamlessly to mobile and desktop views, utilizing Flexbox and Grid layouts for flexible containers and adaptive styling.


