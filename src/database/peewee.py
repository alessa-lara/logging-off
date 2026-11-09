from peewee import  DatabaseError, DatabaseProxy, Model, SqliteDatabase, DateTimeField, ForeignKeyField, IntegerField, TextField

DATABASE: DatabaseProxy = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database: DatabaseProxy = DATABASE

class Post(BaseModel):
    date: DateTimeField = DateTimeField(None)
    id: IntegerField = IntegerField(unique = True)
    text: TextField = TextField()

class Tags(BaseModel):
    id: IntegerField = IntegerField(unique = True)
    type: TextField = TextField()

# Posts and tags have a N-N relation
class Post_Tag(BaseModel):
    id: IntegerField = IntegerField(unique = True)
    post: ForeignKeyField = ForeignKeyField(Post)
    tag: ForeignKeyField = ForeignKeyField(Tags)

class Attachments(BaseModel):
    id: IntegerField = IntegerField(unique = True)
    location: TextField = TextField()

# Posts and attachments have a N-N relation
class Post_Attachment(BaseModel):
    id: IntegerField = IntegerField(unique = True)
    post: ForeignKeyField = ForeignKeyField(Post)
    tag: ForeignKeyField = ForeignKeyField(Attachments)

class Sqlite_Database():
    def __init__(self, root: str) -> None:
        DATABASE_LOCATION: str = f"{root}/sqlite.db"
        database: SqliteDatabase = SqliteDatabase(DATABASE_LOCATION)
        DATABASE.initialize( database )

        try:
            database.connect()
        except:
            raise DatabaseError("[ERROR] couldn't connect to database")

        database.create_tables([Post, Tags, Post_Tag, Attachments, Post_Attachment])
