import click


@click.command()
@click.argument('name')
def there(name):
    click.echo('>>>>>>> Hello there, {0}'.format(name))


# def test():
#     click.echo('Hello there')
