import click
import click_log
import logging
logger = logging.getLogger(__name__)


@click.command()
@click_log.simple_verbosity_option()
@click_log.init(__name__)
@click.argument('name')
def there(name):
    click.echo('>>>>>>> Hello there, {0}'.format(name))
    logger.debug('All is well')


# def test():
#     click.echo('Hello there')
