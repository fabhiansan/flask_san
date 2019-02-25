from os import listdir, getcwd
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import listindir
import ftplib

app = Flask(__name__)

@app.route('/listdir')
def intro():
    y = listdir(getcwd())
    return render_template('listdir.html', **locals())

@app.route("/index")
def index():
    return render_template('index.html')
 
@app.route("/hello/<string:name>/")
def hello(name):
    
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ", "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ", "'To understand recursion you must first understand recursion..' -- Unknown", "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown", "'Mathematics is the key and door to the sciences.' -- Galileo Galilei", "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    
    class xy():
        x = getcwd()
        y = listdir(getcwd())
    return render_template('test.html',**locals())

@app.route('/jstree')
def jstree():
    return render_template('jstree.html')

@app.route('/ftplib', methods=['POST', 'GET'])
def ftplibs():
    if request.method == 'POST':
        resultname = request.form['usernames']
        resultpassword = request.form['passwords']
        
        ftp = ftplib.FTP('192.168.34.10')
        ftp.login(user=resultname, passwd=resultpassword)
        
        files = []
        x = ftp.nlst()
        
        return render_template('ftplib.html', x = x)


if __name__ == "__main__":
    app.run()