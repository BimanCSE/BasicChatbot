from typing import TypedDict


class AINewsState(TypedDict):
    frequency: str
    news_data: list
    summary: str
    saved_file_name: str
