from os import listdir, getcwd
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import listindir
import ftplib

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
 
@app.route('/ftplib', methods=['POST', 'GET'])
def ftplibs():
    if request.method == 'POST':
        resultname = request.form['usernames']
        resultpassword = request.form['passwords']
        
        ftp = ftplib.FTP('localhost')
        ftp.login(user=resultname, passwd=resultpassword)
        
        x = ftp.nlst()
        
        return render_template('ftplib.html', x = x)


if __name__ == "__main__":
    app.run()