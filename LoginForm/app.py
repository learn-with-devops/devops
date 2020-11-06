from flask import Flask, escape, request, render_template
import mysql.connector

mydb = mysql.connector.connect(
    host='10.80.1.5',
    user='anand',
    passwd='Anand@839',
    database='gateway'
)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mypass = request.form['pass']
        re_pass = request.form['re_pass']
        data = mydb.cursor()
        data.execute("INSERT INTO gatewaylogin(name, email, pass, re_pass) values(%s, %s, SHA1(%s), SHA1(%s))",(name, email, mypass, re_pass))
        mydb.commit()
        data.close()
        return "Data Inserted Successfully"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')
