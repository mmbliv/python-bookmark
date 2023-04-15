from peewee import *
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('option')
args=parser.parse_args()
# print(args)

db=PostgresqlDatabase(
    'bookmark',
    user='minhe',
    password='',
    host='localhost',
    port=5432
)

db.connect()

class BaseModel(Model):
    class Meta:
        database=db

class Bookmark(BaseModel):
    title=CharField()
    link=CharField()

# db.drop_tables([Bookmark])
db.create_tables([Bookmark])

if args.option=='add':
    print('Enter the tilte of the bookmark')
    title=input('title: ')
    print('Enter the link of the bookmark')
    link=input('link: ')
    new_bookmark=Bookmark(title=title,link=link)
    new_bookmark.save()


if args.option=='find_all':
    data=Bookmark.select()
    print([f'{d.title}: {d.link}' for d in data])

if args.option=='find':
    print('Enter the bookmark title that you want to look for')
    title=input('title: ')
    bookmark=Bookmark.select().where(Bookmark.title==title)
    print([f'{d.title}: {d.link}' for d in bookmark])