from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):

    # TODO:タイトルの入力欄を定義して下さい
    title = StringField('タイトル', validators=[DataRequired(), Length(min=1, max=10)])
    # TODO:詳細の入力欄を定義して下さい
    description = TextAreaField('詳細', validators=[DataRequired(), Length(max=100)])
    # TODO:締切日の入力欄を定義して下さい
    deadline_date = DateField('締切日', format='%Y-%m-%d', validators=[DataRequired()])
    # TODO:完了状態を表すチェックボックスを定義して下さい
    completed = BooleanField('完了')
    # TODO:送信ボタンを定義して下さい
    submit = SubmitField('タスクを追加')
