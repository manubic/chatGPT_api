import psycopg2, os, typer, random
from dotenv import load_dotenv
from main import start

load_dotenv()

app = typer.Typer()
def get_rand_story() -> list[list[str]]:
    conn = psycopg2.connect(dbname=os.environ.get('DBNAME'), user=os.environ.get('DBUSER'), password=os.environ.get('PASSWORD'), host=os.environ.get('HOST'), port=os.environ.get('PORT'))
    cursor = conn.cursor()
    cursor.execute("SELECT name, short_story, long_story FROM stories")
    stories = cursor.fetchall()
    return random.choice(stories)

@app.command()
def insert_story() -> None:
    conn = psycopg2.connect(dbname=os.environ.get('DBNAME'), user=os.environ.get('DBUSER'), password=os.environ.get('PASSWORD'), host=os.environ.get('HOST'), port=os.environ.get('PORT'))
    cursor = conn.cursor()
    name = input('Nombre de la historia: ')
    short_story = input('Introduce la historia reducida: ')
    long_story = input('Introduce la historia completa: ')
    cursor.execute("INSERT INTO stories (name, short_story, long_story) VALUES (%s, %s, %s)", (name, short_story, long_story))
    conn.commit()
    cursor.close()
    conn.close()

@app.command()
def play(audio) -> None:
    story = get_rand_story()
    start(story, audio)
    
if __name__ == "__main__":
    app()