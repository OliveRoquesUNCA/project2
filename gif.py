import os

import click

from giphy_cli import GiphyCLI

API_KEY = os.environ["GIPHY_API_KEY"]

# TODO:
# Error handling
# Implement GiphyCLI class


@click.group()
def gif():
    pass


@gif.command()
@click.option(
    "--count",
    type=int,
    default=5,
    show_default=True,
    help="define number of results",
)
@click.option(
    "--markdown",
    is_flag=True,
    default=False,
    help="output in markdown formatting",
)
@click.option(
    "--lucky",
    is_flag=True,
    default=False,
    help="returns only first result, overriding count",
)
def trending(count, markdown, lucky):
    cli = GiphyCLI()
    click.echo(cli.trending(count, markdown, lucky))


@gif.command()
@click.option(
    "--count",
    type=int,
    default=5,
    show_default=True,
    help="define number of results",
)
@click.option(
    "--markdown",
    is_flag=True,
    default=False,
    help="output in markdown formatting",
)
@click.option(
    "--lucky",
    is_flag=True,
    default=False,
    help="returns only first result, overriding count",
)
@click.argument("query", type=str)
def search(count, markdown, query, lucky):
    cli = GiphyCLI()
    click.echo(cli.search(query, count, markdown, lucky))


if __name__ == "__main__":
    gif()
