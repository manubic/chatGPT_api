import psycopg2, typer, random
from settings import Settings
from game import Game


settings = Settings()

conn = psycopg2.connect(
            dbname=settings.DBNAME,
            user=settings.DBUSER,
            password=settings.PASSWORD, 
            host=settings.HOST,
            port=settings.PORT,
    )

app = typer.Typer()
def get_rand_story() -> str:
    cursor = conn.cursor()
    cursor.execute("SELECT name, short_story, long_story FROM stories")
    stories = cursor.fetchall()
    return random.choice(stories)

@app.command()
def insert_story() -> None:
    cursor = conn.cursor()
    name = input('Nombre de la historia: ')
    short_story = input('Introduce la historia reducida: ')
    long_story = input('Introduce la historia completa: ')
    cursor.execute("INSERT INTO stories (name, short_story, long_story) VALUES (%s, %s, %s)", (name, short_story, long_story))
    conn.commit()
    cursor.close()
    conn.close()

@app.command()
def play() -> None:
    audio: bool = input('record (YES/NO): ')
    if audio.lower() == 'yes': audio = True
    else: audio = False
    game: Game = Game(settings.CLIENT)
    story: str = get_rand_story()
    print(story)
    game.start(story, audio)
    
if __name__ == "__main__":
    app()