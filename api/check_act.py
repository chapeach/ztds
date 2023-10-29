from flask import Blueprint, render_template, redirect, session
import sqlite3

check_act = Blueprint('check_act', __name__)

@check_act.route("/check-act")
def page_check_act():
    if "username" not in session:
        return redirect("/login")
    else:
        app_name = "Check Act"
        con = sqlite3.connect("db/db.db")
        cur = con.cursor()
        sql = 'select site_code, act, team from tb_check_act'
        curs = cur.execute(sql)
        data_list = curs.fetchall()
        return render_template("check_act/check_act.html", app_name = app_name, data_list = data_list)
    
@check_act.route("/check-act/<sitecode>")
def page_check_act_site_code(sitecode):
    return sitecode