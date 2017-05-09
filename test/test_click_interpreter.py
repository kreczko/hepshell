import hepshell
from hepshell import interpreterv2
import os
from nose.tools import assert_equal
from click.testing import CliRunner

hepshell.settings.PLUGINS = [os.path.join(
    hepshell.HEP_PATH, 'test', 'commands')]


def test_command_list():
    interpreter = interpreterv2.HEPInterpreter()
    commands = interpreter.list_commands(None)
    assert_equal(sorted(commands), sorted(
        ['hello', 'hello there', 'hello awesome']))

def test_resolve_command():
    interpreter = interpreterv2.HEPInterpreter()
    command = interpreter.resolve_command(None, ['hello'])
    assert_equal(command[0], 'hello')

    command = interpreter.resolve_command(None, ['hello awesome me'])
    assert_equal(command[0], 'hello awesome')


def test_hello():
    runner = CliRunner()
    result = runner.invoke(interpreterv2.run_cli, ['hello'])
    assert_equal(result.exit_code, 0)
    assert_equal(result.output, '>>>>>>> Hello World\n')


def test_hello_awesome():
    runner = CliRunner()
    result = runner.invoke(interpreterv2.run_cli, ['hello awesome'])
    assert_equal(result.exit_code, 0)
    assert_equal(result.output, 'Hello, awesome!\n')

# def test_hello_with_param():
#     runner = CliRunner()
#     result = runner.invoke(interpreterv2.run_cli, ['hello there mee'])
#     assert_equal(result.exit_code, 0)
#     # assert_equal(result.output, '>>>>>>> Hello there, me\n')
