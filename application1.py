from flask import Flask, render_template, request, redirect


app = Flask(__name__)

todo = []

@app.route("/")
def index():
  if request.method == "GET":
    return render_template("add1.html")
  else:
    todo = request.form.get("task")
    todos.append(todo)
    return redirect("/")
