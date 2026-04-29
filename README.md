# 🩺 SwasthyaVaani – AI-Driven Multilingual Healthcare Assistant

## 📌 Overview
SwasthyaVaani is an AI-powered healthcare assistant designed to analyze user symptoms from voice or text input and predict possible diseases. The system supports multilingual interaction and aims to improve healthcare accessibility, especially in rural areas.

## 🚀 Features
- Symptom extraction using NLP techniques  
- Disease prediction (~85% accuracy)  
- Multilingual support (English, Hindi, Telugu)  
- Voice and text input processing  
- REST API for real-time inference  
- Structured healthcare data storage  

## 🛠️ Tech Stack
- Python  
- Flask  
- Scikit-learn  
- NLP  
- SQL  
- Tailwind CSS  

## 📂 Project Structure

swasthyavaani/
│── app/
│ ├── main.py
│ ├── models/
│ ├── routes/
│ ├── utils/
│── static/
│── templates/
│── requirements.txt
│── README.md


## ▶️ How to Run
```bash
git clone https://github.com/VarunKumar123456/swasthyavaani
cd swasthyavaani
pip install -r requirements.txt
python app.py

📊 System Workflow
User inputs symptoms (voice/text)
NLP extracts key symptoms
ML model predicts disease
API returns response
Output displayed + optional audio

⚠️ Assumptions
Model trained on limited dataset
Designed for assistance, not medical diagnosis
Single-user interaction system

🚀 Future Improvements
Deep learning models for higher accuracy
Integration with real healthcare datasets
Mobile application support
Doctor consultation integration
👨‍💻 Author

Chitikena Varun Kumar
