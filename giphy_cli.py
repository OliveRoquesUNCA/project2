import click
from giphy_api import GiphyAPI

@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
def trending():
    print("trending subcommand called!")


@gif.command()
def search():
    print("search subcommand called!")


if __name__ == "__main__":
    gif()