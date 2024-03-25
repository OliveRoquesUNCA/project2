import click
from giphy_api import GiphyAPI
import os

API_KEY=os.environ["GIPHY_API_KEY"]

# TODO:
# Markdown
# Error handling

@click.group()
def gif():
    pass

@gif.command()
@click.option('--count', type=int, default=5, show_default=True, help = "define number of results")
def trending(count):
    i = 1
    trends = GiphyAPI('trending', limit=str(count))
    results = trends.query()
    for name, result in results.items():
        click.echo(str(i) + ") " + name + " (" + result + ")")
        i += 1

@gif.command()
@click.option('--count', type=int, default=5, show_default=True, help = "define number of results")
@click.argument('query', type=str)
def search(count, query):
    i = 1
    searches = GiphyAPI('search', limit=str(count), q=query)
    results = searches.query()
    for name, result in results.items():
        click.echo(str(i) + ") " + name + " (" + result + ")")
        i += 1

if __name__ == "__main__":
    gif()