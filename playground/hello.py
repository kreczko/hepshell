#from __future__ import print_function
import click



# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet')
@click.group(invoke_without_command=True)
@click.argument('files',nargs=-1, type=click.Path(exists=True))
def hello(files):
    for f in files:
        click.echo(f)

if __name__ == '__main__':
    hello()
