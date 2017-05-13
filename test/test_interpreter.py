import unittest
import os
os.environ['HEP_PROJECT_ROOT'] = ''
os.environ['USE_HEPSHELL_COMMANDS'] = '1'
import hepshell

hepshell.SETTINGS.COMMANDS = [
    'hepshell.commands',
]

from hepshell import interpreter_legacy


class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.cli_input1 = ['help', 'list', 'sample']
        self.args1 = ['list', 'verbose=1', 'sample=TTJet', 'lumi=100.05']
        self.args2 = ['list', '--verbose', '--sample=TTJet', '--lumi=100.05']

    def test_find_command(self):
        from hepshell.commands.help import Command as HC
        command, args = hepshell.interpreter_legacy._find_command_and_args(
            self.cli_input1)
        self.assertIsInstance(command, HC)
        self.assertEqual(args, self.cli_input1[1:])

    def test_parse1(self):
        args, params = hepshell.interpreter_legacy._parse_args(
            self.args1)
        self.assertEqual(len(args), 1)
        self.assertEqual(args[0], 'list')
        self.assertIn('verbose', params)
        self.assertIn('sample', params)
        self.assertIn('lumi', params)
        self.assertEqual(params['verbose'], True)
        self.assertEqual(params['sample'], 'TTJet')
        self.assertAlmostEqual(params['lumi'], 100.05, delta=0.001)

    def test_parse2(self):
        args, params = hepshell.interpreter_legacy._parse_args(
            self.args2)
        self.assertEqual(len(args), 1)
        self.assertEqual(args[0], 'list')
        self.assertIn('verbose', params)
        self.assertIn('sample', params)
        self.assertIn('lumi', params)
        self.assertEqual(params['verbose'], True)
        self.assertEqual(params['sample'], 'TTJet')
        self.assertAlmostEqual(params['lumi'], 100.05, delta=0.001)

if __name__ == '__main__':
    unittest.main()
