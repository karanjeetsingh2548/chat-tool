from flask import Flask, render_template, request, redirect


app=Flask(__name__)

todos=[]

        
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html",todos=todos)
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")
