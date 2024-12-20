from flask import Flask, render_template, request, session, redirect, url_for
from src.visualization import plot_actual_vs_predicted, plot_residuals
from src.utils import read_csv

# Define file paths
processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_feature_engineered.csv"
predictions_path = "C:/project/Freight_Analysis_Framework-/models/predictions.csv"

# Load data (assuming predictions.csv exists)
predictions = read_csv(predictions_path)

# Extract actual and predicted values
y_test = predictions['Actual']
y_pred = predictions['Predicted']

# Initialize the Flask app
app = Flask(__name__)

# Secret key for session management (replace with a strong random string)
app.config['SECRET_KEY'] = 'your_secret_key'

# Login credentials (replace with actual username and password)
USERS = {'admin': 'password123'}

def login_required(func):
    """Decorator to check if user is logged in"""
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/')
@login_required
def index():
    """Render the main dashboard page"""
    return render_template('index.html', title="Freight Analysis Dashboard",
                            actual_data=y_test.to_json(), predicted_data=y_pred.to_json())

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle login requests"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:  # Check if both username and password are provided
            if username in USERS and USERS[username] == password:
                session['logged_in'] = True
                return redirect(url_for('index'))  # Assuming 'index' is decorated
            else:
                error = 'Invalid username or password'
        else:
            error = 'Please enter both username and password.'
    else:
        error = None
    return render_template('login.html', title='Login', error=error)

@app.route('/logout')
def logout():
    """Log out the user"""
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)