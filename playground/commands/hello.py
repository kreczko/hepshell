import click


@click.command()
@click.pass_context
def hello(ctx):
    click.echo('>>>>>>> Hello World')
