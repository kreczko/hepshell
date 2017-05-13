import logging
import click

logger = logging.getLogger(__name__)


@click.command()
@click.argument('name')
def there(name):
    click.echo('>>>>>>> Hello there, {0}'.format(name))
