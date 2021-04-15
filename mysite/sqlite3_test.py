import sqlite3
from polls.models import Choice, Question


# conn = sqlite3.connect('db.sqlite3')
# cur = conn.cursor()
# cur.execute("select name from sqlite_master where type='table' order by name")
# print(cur.fetchall())


print(Question.objects.all())