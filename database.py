import psycopg2, os
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(dbname=os.environ.get('DBNAME'), user=os.environ.get('DBUSER'), password=os.environ.get('PASSWORD'), host=os.environ.get('HOST'), port=os.environ.get('PORT'))
cursor = conn.cursor()

def insert_story(cursor, name, short_story, long_story) -> None:
    cursor.execute("INSERT INTO stories (name, short_story, long_story) VALUES (%s, %s, %s)", (name, short_story, long_story))

insert_story(cursor, 'hola', 'adios', 'jejecrwecrcfwfew')

conn.commit()

cursor.close()
conn.close()

