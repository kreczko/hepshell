import os
import logging
import copy

LOG = logging.getLogger(__name__)


class Command(object):
    """Base class for all commands"""
    REQUIRE_GRID_CERT = False
    DEFAULTS = {}

    def __init__(self, path=__file__, doc=__doc__):
        current_path = os.path.split(path)[0]
        parent_folder = current_path.split("/")[-1]
        if parent_folder == 'commands':
            self.__name = 'hep'
        else:
            self.__name = parent_folder
        self.__doc = doc
        self.__text = ''
        self.__variables = copy.deepcopy(self.DEFAULTS)
        self.__args = []
        self.__results = {}

    def __can_run(self):
        return True

    def run(self, args, variables):
        """
            Runs the commands and an exit code (True if everything went OK)
        """
        self.__prepare(args, variables)
        self.__text = "NOT IMPLEMENTED"

        return True

    def help(self):
        """Returns a little help text with the description of the command."""
        if self.__doc:
            return self.__doc
        else:
            return 'Documentation for command "{0}" is missing'.format(self.__name)

    def __parse_arguments(self, args):
        """ This function is command specific """
        self.__args = args

    def get_text(self):
        return self.__text

    def __set_variables(self, variables):
        """
            Overwrites defaults with set variables
        """
        for name, value in variables.items():
            if name in variables:
                self.__variables[name] = value

    def __prepare(self, args, variables):
        self.__set_variables(variables)
        self.__parse_arguments(args)
        if self.REQUIRE_GRID_CERT:
            if not self.__has_valid_proxy():
                self.__create_proxy()

    def results(self):
        return self.__results

    def __create_proxy(self):
        from hepshell.commands.create.grid_proxy import Command as CP
        create_proxy = CP()
        create_proxy.run([], {'vo': 'cms', 'hours': '80'})

    def __has_valid_proxy(self):
        from hepshell.commands.check.grid_proxy import Command as CP
        check_proxy = CP()
        is_valid = check_proxy.run([], {})
        results = check_proxy.results()
        timeleft_in_minutes = results['timeleft_in_minutes']
        # more than 30min time left
        is_valid = is_valid and timeleft_in_minutes > 30
        return is_valid

    def __extract_additional_parameters(self, prefix='', skip=[]):
        """
            Searches through given parameters and extracts unknown (not defined
            in DEFAULTS dictionary) ones. These are then treated as additional
            parameters that can be used for a shell command.

            @param prefix: determines how paremeters are constructed. Usually
                           either empty or '--'
            @param skip: list of parameters to be skipped
        """
        args = []
        for p, value in self.__variables.items():
            if p in self.DEFAULTS or p in skip:
                continue
            args.append('{0}{1}={2}'.format(prefix, p, value))
        return ' '.join(args)
