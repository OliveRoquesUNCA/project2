import click
from giphy_api import GiphyAPI
import os

API_KEY=os.environ["GIPHY_API_KEY"]

# TODO:
# Error handling
# Implement GiphyCLI class

@click.group()
def gif():
    pass

@gif.command()
@click.option('--count', type=int, default=5, show_default=True, help = "define number of results")
@click.option('--markdown', is_flag=True, default=False, help = "output in markdown formatting")
def trending(count, markdown):
    i = 1
    trends = GiphyAPI('trending', limit=str(count))
    results = trends.query(markdown)
    if(not markdown):
        for name, result in results.items():
            click.echo(str(i) + ") " + name + " (" + result + ")")
            i += 1
    else:
        for name, result in results.items():
            click.echo(str(i) + ") ![" + name + "](" + result + ")")
            i += 1

@gif.command()
@click.option('--count', type=int, default=5, show_default=True, help = "define number of results")
@click.option('--markdown', is_flag=True, default=False, help = "output in markdown formatting")
@click.argument('query', type=str)
def search(count, markdown, query):
    i = 1
    searches = GiphyAPI('search', limit=str(count), q=query)
    results = searches.query(markdown)
    if(not markdown):
        for name, result in results.items():
            click.echo(str(i) + ") " + name + " (" + result + ")")
            i += 1
    else:
        for name, result in results.items():
            click.echo(str(i) + ") ![" + name + "](" + result + ")")
            i += 1


if __name__ == "__main__":
    gif()