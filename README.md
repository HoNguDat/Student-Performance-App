# student-performance-app-using-machine-learning
🎓 Student Performance Prediction
This project predicts student performance based on various academic, behavioral, and socio-economic factors. It incorporates data analysis, machine learning model development, prediction scripts, retraining functionality, and an optional web interface.

✨ Features
📊 Data Analysis and Visualization

Performed using test.ipynb Jupyter Notebook.

Explores trends and correlations within the StudentPerformanceFactors.csv dataset.

🤖 Machine Learning Model

Pre-trained model stored as student_performance_model.pkl.

Built using sklearn.pipeline.Pipeline, including preprocessing steps:

ColumnTransformer

SimpleImputer

OneHotEncoder

📈 Score Prediction

student_score_predictor.py: Predicts student scores based on user-provided inputs and the trained model.

🔄 Model Retraining

retrain_model.py: Allows retraining the model using updated or additional data.

🌐 Web Interface (Optional)

index.html: A basic front-end interface for predictions (can be extended with Flask/Django for full functionality).

🧰 Technologies Used
Languages: Python

Libraries:

pandas, numpy: Data manipulation and numerical processing

matplotlib, seaborn, plotly: Visualization

scikit-learn: ML pipeline, model training, and evaluation

warnings: Suppressing unwanted warnings

Tools: Jupyter Notebook, Python HTTP server (optional for frontend)

📁 Dataset Overview
Filename: StudentPerformanceFactors.csv
Attributes:

Hours_Studied

Attendance

Parental_Involvement

Access_to_Resources

Extracurricular_Activities

Sleep_Hours

Previous_Scores

Motivation_Level

Internet_Access

Tutoring_Sessions

Family_Income

Teacher_Quality

School_Type

Peer_Influence

Physical_Activity

Learning_Disabilities

Parental_Education_Level

Distance_from_Home

Gender

⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone <repository_url>
cd <repository_name>
2. Install Dependencies
Ensure Python is installed. Then run:

bash
Copy
Edit
pip install pandas numpy matplotlib plotly seaborn scikit-learn
3. Data Setup
Place the dataset StudentPerformanceFactors.csv in the root directory.

4. Run Jupyter Notebook (For Exploration & Development)
bash
Copy
Edit
jupyter notebook
# Open and run test.ipynb
5. Predict Student Scores
bash
Copy
Edit
python student_score_predictor.py
# (Modify the script to handle user input and output as needed.)
6. Retrain the Model
bash
Copy
Edit
python retrain_model.py
# (Ensure new/updated dataset is used inside the script.)
7. Run Web Interface (Optional)
For a static HTML page:

bash
Copy
Edit
python -m http.server 8000
# Open http://localhost:8000/index.html in your browser
📂 Project Structure
bash
Copy
Edit
.
├── StudentPerformanceFactors.csv     # Dataset
├── test.ipynb                        # Jupyter Notebook for analysis
├── student_performance_model.pkl     # Trained ML model
├── student_score_predictor.py        # Script to predict scores
├── retrain_model.py                  # Script to retrain the model
└── index.html                        # (Optional) Web UI
🧠 Potential Improvements
Add form input in the web interface with Flask backend.

Store user predictions in a database.

Introduce model evaluation metrics (R², MAE, RMSE).

Implement real-time feedback visualization.

📬 Contact
For any questions or feedback, feel free to reach out at:
📧 khushbupoul77@gmail.com

