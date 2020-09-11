# poetpack_tmpl/console.py

import click
from . import __version__



@click.command()
@click.version_option(version=__version__)





def main():
    """The Poetry template Python project."""
    click.echo("Hello, world from NajlaBH !")


if __name__ == "__main__":
    main()
