import click


@click.command()
@click.pass_context
def hello(ctx):
    print(ctx)
    click.echo('>>>>>>> Hello World')
