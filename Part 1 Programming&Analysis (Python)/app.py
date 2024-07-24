#Import flask, usefull libraries
from flask import Flask, request, jsonify
import pandas as pd

#Load the data 
df = pd.read_csv("clean_dataset.csv")

#Start the app
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the API!"

# Endpoint to get the top N highest-paid employees
@app.route('/top_employees', methods=['GET'])
def get_top_employees():
    try:
        n = int(request.args.get('N', 5))  # Default to top 5 employees if N is not provided
        top_employees = df.nlargest(n, 'Salary').to_dict(orient='records')
        return jsonify(top_employees)
    except Exception as e:
        return jsonify({'error': str(e)})

# Endpoint to get the number of employees in department X
@app.route('/employees_in_department', methods=['GET'])
def get_employees_in_department():
    department = request.args.get('X')
    if department is None:
        return "Please provide a department X."
    count = df[df['Department'] == department].shape[0]
    return jsonify({'department': department, 'employee_count': count})

if __name__ == '__main__':
    app.run(debug=True)


## you can now test your /top_employees and /employees_in_department endpoints using various tools, For example like curl.
# Testing /top_employees Endpoint:
  # To get the top N highest-paid employees, you can make a GET request to the /top_employees endpoint with the optional parameter N.
  # curl "http://127.0.0.1:5000/top_employees?N=3"

# Testing /employees_in_department Endpoint:
  # To get the number of employees in a specific department, you need to provide the X parameter.
  # curl "http://127.0.0.1:5000/employees_in_department?X=Finance"

# You can run these curl commands in your terminal to send HTTP requests to your Flask application and see the responses.
  
#http://127.0.0.1:5000/employees_in_department?X=Finance
#http://127.0.0.1:5000/top_employees?N=3
