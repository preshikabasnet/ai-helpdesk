from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import joblib
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db = SQLAlchemy(app)

# Load AI model
model = joblib.load("ticket_classifier.pkl")

# Technician map
tech_map = {
    "Network": "Alice",
    "Hardware": "Bob",
    "Software": "Charlie",
    "Login Issues": "David",
    "General": "Support Team"
}

# DB Model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    assigned_to = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "category": self.category,
            "assigned_to": self.assigned_to
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    data = request.form
    description = data['description']
    predicted_category = model.predict([description])[0]
    technician = tech_map.get(predicted_category, tech_map['General'])

    new_ticket = Ticket(description=description, category=predicted_category, assigned_to=technician)
    db.session.add(new_ticket)
    db.session.commit()

    return render_template("index.html", success=True, ticket=new_ticket)

@app.route('/tickets')
def list_tickets():
    tickets = Ticket.query.all()
    return jsonify([ticket.to_dict() for ticket in tickets])

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('tickets.db'):
            db.create_all()
    app.run(debug=True)
