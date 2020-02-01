#!/usr/bin/env python

import types

class Option():
    """
    This is a class to manage all the options available.

    Attributes:
        _format (types.FunctionType): function format.
    """

    @staticmethod
    def long_list_format() -> str:
        """
        Gets a format from long list option.

        Returns:
            str: long list format.
        """
        return '{0[mode]}  {0[date]} {0[filename]}'

    @staticmethod
    def default_format() -> str:
        """
        Gets a format from the default option.

        Returns:
            str: default format.
        """
        return '{0[filename]}'

    OPTIONS = {
        '': default_format.__func__,
        '-l': long_list_format.__func__,
    }

    def __init__(self, option: str = ''):
        """
        The constructor for Option class.

        Parameters:
            option (str): selected option. Defaults to empty string.
        """
        self._format = self.format_from(option)

    def format_from(self, option: str) -> types.FunctionType:
        """
        Gets a format function from an option.

        Parameters:
            option (str): option.

        Raises:
            Exception: if option is not implemented.

        Returns:
            types.FunctionType: [description]
        """
        if option in self.OPTIONS:
            return self.OPTIONS[option]
        raise Exception("Option not found.")

    def format(self) -> types.FunctionType:
        """
        Gets the format function.

        Returns:
            types.FunctionType: format function.
        """
        return self._format
