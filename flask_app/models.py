from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    # TODO:タイトルのカラムを定義して下さい
    title = db.Column(db.String(100), nullable=False)
    # TODO:詳細のカラムを定義して下さい
    description = db.Column(db.Text, nullable=False)
    # TODO:締切日のカラムを定義して下さい
    deadline_date = db.Column(db.Date, nullable=False)
    # TODO:完了状態を表すカラムを定義して下さい
    completed = db.Column(db.Boolean, default=False)
