from playsound import playsound  # imports method from object package
import click  # imports object that contains methods


@click.command()
@click.option("--song-number", 'song',
              prompt="Number of audio file",
              type=click.IntRange(0, 20, clamp=True),
              help="The number that matches the audio file you want to play")
def playSelectedSound(song):
    """Press a button, hear the beep"""
    while song != 0:
        playsound('assets/wayne.mp3')
        playSelectedSound()
    exit


if __name__ == '__main__':
    playSelectedSound()