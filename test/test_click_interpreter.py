import hepshell
from hepshell import interpreterv2
import os
from nose.tools import assert_equal

hepshell.settings.PLUGINS = [os.path.join(hepshell.HEP_PATH, 'test', 'commands')]

def test_command_list():
    interpreter = interpreterv2.HEPInterpreter()
    commands = interpreter.list_commands(None)
    print(commands)
    assert_equal(sorted(commands),sorted(['hello', 'hello there', 'hello awesome']))
