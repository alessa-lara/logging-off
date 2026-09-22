class Post():
    date: str
    id: int
    text: str
    tags: list[str]
    attachments: list[str]

    def __init__(self, date: str, id: int, text: str, tags: list[str], attachments: list[str]) -> None:
        self.date = date
        self.id = id
        self.text = text
        self.tags = tags
        self.attachments = attachments
