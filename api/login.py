#from flask import Blueprint
#render_template, redirect
#request, session
#import sqlite3
#import time

#login = Blueprint('login', __name__)

@app.route("/login")
def page_login():
    return "login"

#@login.route("/login")
#def page_login():
#    if "username" not in session:
#        return render_template("/login/login.html")
#    else:
#        return redirect("/")

'''
@login.route("/fn_login", methods=["POST"])
def fn_login():
    try:
        print("*"*50)
        username = request.form["username"]
        password = request.form["password"]
        con = sqlite3.connect("db/db.db")
        cur = con.cursor()
        sql = 'select * from tb_user_login where username = "{}" and password = "{}"'.format(username, password)
        curs = cur.execute(sql)
        data = curs.fetchall()
        if len(data) == 1:
            data = data[0]
            if data[4] == "enable" and len(data) == 5:
                session['username'] = data[1]
                session['password'] = data[2]
                session['access'] = data[3]
                print("time : " + time.ctime())
                print("user : " + username + " login done")
                print("*"*50)
                return redirect("/")
            else:
                return redirect("/login")
        else:
            return redirect("/login")
    except:
        return redirect("/login")

# fn logout
@login.route("/fn_logout")
def fn_logout():
    print("*"*50)
    print("time : " + time.ctime())
    print("user : " + session["username"] + " logout done")
    session.clear()
    print("*"*50)
    return redirect("/login")
'''