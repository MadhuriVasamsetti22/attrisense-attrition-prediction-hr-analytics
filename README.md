# 🚀 AttriSense – Attrition Prediction & HR Analytics

AttriSense is a full-stack web application designed to help organizations manage employee data and predict employee attrition using Machine Learning. It combines HR analytics with an intuitive dashboard and smart prediction system.

---

## 📌 Overview
AttriSense enables HR teams to:
- Manage employee records efficiently
- Analyze workforce trends
- Predict employee attrition using ML
- Make data-driven HR decisions

---

## ✨ Key Features

### 🔐 Authentication
- Secure Login & Logout system

### 👨‍💼 Employee Management
- Add Employee
- View Employees
- Update Employee Details
- Delete Employee
- Search Employees

### 🤖 Machine Learning
- Train ML model on employee dataset
- Predict whether an employee will leave
- Accuracy-based model evaluation

### 📊 Dashboard & Analytics
- Average Salary by Department
- Attrition Count Visualization
- Real-time chart generation

### 📁 Reports
- Download employee data as CSV file

### 🎨 UI/UX
- Professional responsive design
- Dark / Light mode toggle
- Navigation-based interface (no manual URL typing)

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | HTML, CSS |
| Backend | Python (Flask) |
| Database | SQLite |
| ML Model | Scikit-learn |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Deployment | Render |

---

## 🧠 Machine Learning Details

The model predicts employee attrition based on:
- Age  
- Salary  
- Experience  
- Performance  

Algorithm Used:
- Random Forest Classifier

---

## 📂 Project Structure


AttriSense/
│
├── app.py
├── db.py
├── model.py
├── requirements.txt
├── Procfile
├── employees.db
├── model.pkl
│
├── static/
│ ├── style.css
│ ├── chart1.png
│ └── chart2.png
│
└── templates/
├── login.html
├── index.html
├── add_employee.html
├── employees.html
├── predict.html
├── dashboard.html
└── update_employee.html


---

## ⚙️ Installation (Local Setup)

1. Clone the repository:

git clone https://github.com/yourusername/attrisense-attrition-prediction-hr-analytics.git


2. Navigate to project:

cd attrisense-attrition-prediction-hr-analytics


3. Install dependencies:

pip install -r requirements.txt


4. Run the app:

python app.py


5. Open browser:

http://127.0.0.1:5000


---

## 🌍 Deployment

The application can be deployed using platforms like:
- Render
- Railway

---

## 🎯 Future Enhancements
- Role-based authentication (Admin/User)
- Email notifications for attrition risk
- Advanced ML models
- Cloud database integration
- Interactive dashboards (Plotly)

---

## 📌 Project Highlights
- Full-stack ML application
- Real-time analytics dashboard
- End-to-end deployment ready
- Clean UI with modern features

---

## 👩‍💻 Author
Developed by **[Durga Madhuri Vasamsetti]**

---

## 📄 License
This project is for educational and demonstration purposes.
