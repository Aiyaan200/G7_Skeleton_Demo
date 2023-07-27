from flask import Flask, render_template, request
import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user="root",
    passwd="",
    database ="Demo_Database"
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Web_Page.html')

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO user_info (Name,Email,Password) VALUES(%s,%s,%s)",(name,email,password))
        db.commit()
        return render_template('Web_Page.html')

if __name__ == "__main__":
    app.run(debug=True)

