#!/usr/bin/env python

import sys
import os
import stat
from datetime import datetime

from option import Option

class ListDirectory():
    """
    This is a class to list files based on a path.

    Attributes:
        option (Option): format option.
        files (list): information from files.
    """

    def __init__(self, argv: list):
        """
        The constructor for ListDirectory class.

        Parameters:
            argv (list): list of arguments from command line.
        """
        path = ListDirectory.path_in(argv)
        folder = ListDirectory.folder_from(path)
        prefix = ListDirectory.prefix_from(path)
        filenames = ListDirectory.files_from(folder, prefix)
        self.option = ListDirectory.option_in(argv)
        self.files = ListDirectory.info_from(filenames)

    def display_files(self):
        """
        Method that display files.
        """
        for file in self.files_list():
            print(file)

    def files_list(self):
        """
        Create a generator with files information.

        Yields:
            dict: file information.
        """
        for file in self.files:
            yield self.option.format()().format(file)

    @staticmethod
    def option_in(argv: list) -> Option:
        """
        Gets an Option based on the string option found on the argv list.

        Parameters:
            argv (list): list of arguments from command line.

        Returns:
            Option: object that represents the option selected.
        """
        for arg in argv:
            if arg.startswith('-'):
                return Option(arg)
        return Option()

    @staticmethod
    def path_in(argv: list) -> str:
        """
        Gets a path from the argv list.

        Parameters:
            argv (list): list of arguments from command line.

        Raises:
            Exception: if not find the path.

        Returns:
            str: path.
        """
        for arg in argv:
            if arg.startswith('/'):
                return arg
        raise Exception('Path not found.')

    @staticmethod
    def prefix_from(path: str) -> str:
        """
        Gets the filename prefix from a path.

        Parameters:
            path (str): path.

        Returns:
            str: prefix.
        """
        if os.path.exists(path) and os.path.isdir(path):
            return ""
        return path.split('/')[-1]

    @staticmethod
    def folder_from(path: str) -> str:
        """
        Gets the folder name from the path.

        Parameters:
            path (str): path.

        Returns:
            str: folder name.
        """
        if os.path.exists(path) and os.path.isdir(path):
            return path
        return ''.join(path.rpartition('/')[:2])

    @staticmethod
    def files_from(folder: str, prefix: str) -> list:
        """
        Gets filenames list from folder and prefix.

        Parameters:
            folder (str): folder name.
            prefix (str): filename prefix.

        Returns:
            list: list of filenames.
        """
        files = []
        for file in os.listdir(folder):
            if file.startswith(prefix):
                files.append(file)
        return files

    @staticmethod
    def info_from(filenames: list) -> list:
        """
        Gets information from each file.

        Parameters:
            filenames (list): filenames

        Returns:
            list: information from each file.
        """
        files = []
        for filename in filenames:
            file_stat = os.lstat(filename)
            file = {}
            file['filename'] = filename
            file['mode'] = stat.filemode(file_stat.st_mode)
            file['date'] = str(datetime.fromtimestamp(file_stat.st_ctime).replace(microsecond=0))
            files.append(file)
        return files


if __name__ == '__main__':
    command = ListDirectory(sys.argv)
    command.display_files()
