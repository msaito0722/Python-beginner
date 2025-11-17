from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Task
from forms import TaskForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key"

db.init_app(app)

# データベースの初期化
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    # TODO:データベースから全タスクを取得する処理を記述して下さい
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            deadline_date=form.deadline_date.data,
            completed=form.completed.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_task.html", form=form)

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.deadline_date = form.deadline_date.data
        task.completed = form.completed.data
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_task.html", form=form)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)