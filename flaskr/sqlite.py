import sqlite3
from flask import redirect, render_template, request
from flaskr import app
from flaskr.openai import *


@app.route("/submit", methods=["POST"])
def create_message():
    conn = sqlite3.connect('TestDB.db')
    c = conn.cursor()
    num = get_len()
    c.execute(
        "INSERT INTO Conversation values(?, ?, ?)", (num, request.form.get('text'), request.form.get('name')))
    conn.commit()
    add_AI_response()
    return redirect("/")


@app.route("/get")
def show_data():
    datas = get_data()
    return render_template("index.html", datas=datas)


@app.route("/delete", methods=["POST"])
def delete_data():
    conn = sqlite3.connect('TestDB.db')
    c = conn.cursor()
    c.execute("DELETE FROM Conversation")
    conn.commit()
    return redirect("/")

def get_data():
    conn = sqlite3.connect("TestDB.db")
    c = conn.cursor()
    cur = c.execute("SELECT * FROM Conversation")
    datas = []
    for row in cur:
        datas.append(row)
    cur.close()
    return datas


def get_len():
    conn = sqlite3.connect("TestDB.db")
    c = conn.cursor()
    cur = c.execute("SELECT * FROM Conversation")
    num = 0
    for _ in cur:
        num += 1
    return num


def add_AI_response():
    conn = sqlite3.connect("TestDB.db")
    c = conn.cursor()
    cur = c.execute("SELECT * FROM Conversation")
    conversation_list = []
    for row in cur:
        text = row[1]
        user = row[2]
        conversation = f"{user}: {text}"
        conversation_list.append(conversation)
    param = '\n'.join(conversation_list) + '\nAI:'
    res_message = create_openai_response(param)
    res_message = res_message.replace('\n', '')
    # res_message = "test"
    num = get_len()
    c.execute(
        "INSERT INTO Conversation values(?, ?, ?)", (num, res_message, 'AI'))
    conn.commit()
