from peewee import *
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('option',help='you can provide option with add, find_all, find, update, or delete')
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

db.create_tables([Bookmark])

if args.option=='add':
    title=input('Enter the tilte of the bookmark: ')
    link=input('Enter the link of the bookmark: ')
    new_bookmark=Bookmark(title=title,link=link)
    new_bookmark.save()
    print(f'{new_bookmark.title}: {new_bookmark.link} added')


if args.option=='find_all':
    data=Bookmark.select()
    print([f'{d.title}: {d.link}' for d in data])

if args.option=='find':
    title=input('Enter the bookmark title that you want to look for: ')
    bookmark=Bookmark.select().where(Bookmark.title==title)
    print([f'{d.title}: {d.link}' for d in bookmark])

if args.option=='update':
   title=input('Enter the title of the boonkmark you want to update: ') 
   bookmark=Bookmark.get(Bookmark.title==title)
   new_title=input('Enter the new title of the boonkmark you want to update: ')
   new_link=input('Enter the new link of the boonkmark you want to update: ')
   bookmark.title=new_title
   bookmark.link=new_link
   bookmark.save()
   print(f'updated to {bookmark.title}: {bookmark.link}')

if args.option=='delete':
    title=input('Enter the title of the boonkmark you want to delete: ')
    bookmark=Bookmark.get(Bookmark.title==title)
    bookmark.delete_instance()
    print(f'{title} deleted')
