from flask import Flask, render_template, request, redirect

app=Flask(__name__)

todos=[]
  


@app.route("/")
def index():
    return render_template("index.html",todos=todos)

@app.route("/tasker",methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("tasker.html")
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")

