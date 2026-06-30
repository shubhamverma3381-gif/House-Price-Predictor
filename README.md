# Bengaluru House Price Predictor 🏠

This is an end-to-end Machine Learning project that predicts house prices in Bengaluru. I have done all the work myself, starting from data cleaning and model training to deploying it as a web application using Flask.

---

## 🚀 Key Features

* *Accurate Prediction:* Predicts property prices instantly based on location, size (BHK), total square feet, and number of bathrooms.
* *Dynamic Dropdown:* The location dropdown on the website automatically loads all valid areas directly from the dataset.
* *Cursor Animation:* Features a smooth snake-like trail animation that follows the mouse cursor to improve the user experience.

---

## 📁 Project Structure

text
├── templates/
│   └── index.html               # Frontend interface (with custom cursor animation)
├── Bengaluru_House_Data.xls     # Raw dataset used for training
├── Cleaned_data.csv             # Cleaned and processed dataset exported from the notebook
├── RidgeModel_Best.pkl          # Final trained machine learning model (Pickle format)
├── PROJECT 2 (House-Price-Predictor).ipynb # Jupyter Notebook containing the ML pipeline
├── main.py                      # Flask backend code connecting the model to the website
└── README.md                    # Project documentation (This file)


---

## 📊 Machine Learning Pipeline & Training Steps

The complete data analysis and model training workflow was performed inside the PROJECT 2 (House-Price-Predictor).ipynb notebook:

### 1. Data Cleaning
* Used pandas and numpy libraries to handle and fill missing (NaN) values.
* Cleaned the size column by standardizing mixed formats (like 4 Bedroom and 2 BHK) into clean numerical values.
* Processed the total_sqft column by converting numerical ranges (like 2100 - 2850) into their average values.
* Saved the final processed data as Cleaned_data.csv.

### 2. Preprocessing & Pipeline Construction
* Split the dataset into training (80%) and testing (20%) sets using train_test_split.
* Handled categorical text features using *OneHotEncoder* to convert locations into numbers.
* Implemented *make_column_transformer* to cleanly manage data encoding and scaling together.
* Structured the workflow using *make_pipeline* to securely bundle the preprocessing steps with the model.

### 3. Model Selection & Evaluation
* Tested and compared three different regression algorithms: *Linear Regression, **Lasso, and **Ridge*.
* Evaluated model accuracy using the *r2_score* metric on the test dataset.
* Selected *Ridge Regression* as the final model because it delivered the most stable and optimal performance.
* Exported the finalized trained pipeline into the RidgeModel_Best.pkl file.

---

## 💻 Web Application & Animation Details

* *Flask Backend:* Developed the backend server using the Flask framework in main.py. This server receives user inputs from the webpage, passes them through the loaded .pkl pipeline, and displays the predicted price.
* *Snake Animation:* Designed a custom snake/trail follower animation using clean JavaScript and CSS inside index.html that dynamically responds to mouse movement.

---

## 🛠️ Tech Stack

* *Frontend:* HTML5, CSS3, JavaScript
* *Backend Framework:* Flask (Python)
* *Data Science & ML:* Pandas, NumPy, Scikit-Learn (OneHotEncoder, make_pipeline, r2_score), Pickle

---

## 🚀 How to Run Locally (Installation)

### 1. Clone the repository
bash
git clone https://github.com
cd House-Price-Predictor


### 2. Install required packages
bash
pip install flask pandas numpy scikit-learn


### 3. Run the application
bash
python main.py


### 4. Open in browser
Navigate to the following local address in your web browser: http://127.0.0

---

🧑‍💻 *Developer:* Shubham Verma ([@shubhamverma3381-gif](https://github.com))
