from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# スキーマの定義
class TaskBase(BaseModel):

    # TODO:タイトルは必須項目とし、入力文字数は1〜10文字となるように設定して下さい
    title: str = Field(..., min_length=1, max_length=10)
    # TODO:詳細の入力文字数は最大100文字までとなるように設定して下さい
    description: str = Field(..., max_length=100)
    # TODO:締切日はYYYY-MM-DD形式となるように設定して下さい
    deadline_date: date
    # TODO:完了フラグはデフォルト値がfalseとなるように設定して下さい
    completed: bool = Field(default=False)

class TaskCreate(TaskBase):
    pass
class Task(TaskBase):
    id: int
    class Config:
        from_attributes=True