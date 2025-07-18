# AI-Powered Help Desk Ticketing System

This project is a web-based help desk ticketing system that utilizes machine learning to classify support tickets and automatically route them to the appropriate technician. It is designed to streamline IT help desk operations by reducing ticket resolution time and eliminating manual classification.

---

## Version Information

**Version**: 0.1 - Initial Development Phase  
This version focuses on core functionality, and includes:

- Basic machine learning classification (Naive Bayes)
- Technician assignment logic
- A simple HTML-based user interface
- Local storage using SQLite
- Flask-based backend

Future versions will include advanced features such as authentication, ticket history views, urgency levels, UI enhancements, and deployment support.

---

## Project Motivation

This project was created to explore the application of artificial intelligence in IT support systems. As an IT enthusiast, I aimed to solve a real-world challenge: manually triaging and assigning help desk tickets. This system serves as a foundation for building an intelligent, efficient support desk that reduces the time between issue reporting and resolution.

---

## Features

- Submit tickets through a basic web interface
- Automatically classify issue type using a trained machine learning model
- Route the ticket to a technician based on category
- Store submitted tickets in a SQLite database
- Easily extendable for future enhancements

---

## Technology Stack

- **Language**: Python 3.10+
- **Web Framework**: Flask
- **Machine Learning**: scikit-learn (Naive Bayes)
- **Data Handling**: pandas, joblib
- **Database**: SQLite (via SQLAlchemy)
- **Frontend**: HTML5 (Flask templating)

---

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### 1. Clone the Repository

```bash
git clone https://github.com/preshikabasnet/ai-helpdesk.git
cd ai-helpdesk
2. Create and Activate a Virtual Environment (Windows PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
3. Install Required Dependencies
pip install -r requirements.txt
4. Train the AI Model
python train_model.py
This will train a basic Naive Bayes classifier using the sample ticket data and save the model as ticket_classifier.pkl.

5. Run the Application
python app.py

6. Open the Web Application
Open your browser and go to:
http://localhost:5000

Usage
Once the application is running, navigate to the web interface, submit a ticket, and the system will:

Classify the issue (e.g., Network, Software, Hardware)

Automatically assign a technician
Save the ticket to the database

Contributing
This project is open-source and welcomes contributions. To contribute:

Fork the repository
Create a new feature branch
Commit your changes
Submit a pull request
Future contributions may include:
Improved UI/UX
Urgency detection
Ticket history views
User login and authentication
Deployment to cloud platforms
```
## License
This project is licensed under the MIT License. You may use, distribute, or modify this software under the terms of that license.

## Author
Presika Basnet
LinkedIn: https://www.linkedin.com/in/preshika-basnet-497314292/
