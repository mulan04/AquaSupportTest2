from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postpone_installment', methods=['POST'])
def postpone_installment():
    external_id = request.form['external_id']
    postpone_date = request.form['postpone_date']
    
    # Your API client code here
    # This is where you would integrate the Python code provided earlier
    
    return f"Installment with external ID {external_id} postponed until {postpone_date}."

if __name__ == '__main__':
    app.run(debug=True)
