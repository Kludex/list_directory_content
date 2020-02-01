
import tempfile
import stat
import os
from datetime import datetime

class MockListDirectory():
    """
    Mock class to help on the test development process.
    """

    @property
    def filenames(self):
        """
        Get filenames.
        """
        return self._filenames

    @property
    def folder(self):
        """
        Get folder.
        """
        return self._folder

    @property
    def info(self):
        """
        Get info.
        """
        return self._info

    @staticmethod
    def wrong_option():
        """
        Generates a wrong option command.

        Returns:
            str: wrong option command.
        """
        return '-1'

    def wrong_folder(self):
        """
        Generates a wrong folder path.

        Returns:
            str: wrong folder path.
        """
        return os.path.join(self.folder, 'wrong/')

    def args(self):
        """
        Generates argument list to create a ListDirectory object.

        Returns:
            list: arguments used to create a ListDirectory
        """
        argv = []
        argv.append('ls.py')
        if 'miss_folder' in self.info:
            return argv
        if 'prefix' in self.info:
            argv.append(os.path.join(self.folder, 'a'))
        elif 'wrong_prefix' in self.info:
            argv.append(os.path.join(self.folder, 'c'))
        else:
            if 'long_list' in self.info:
                argv.append('-l')
            argv.append(self.folder)
        return argv

    def result_list(self):
        """
        Generates a list of expected results to use for testing purposes.

        Returns:
            list: expected results.
        """
        results = []
        if 'wrong_prefix' in self.info:
            return results
        for filename in self.filenames:
            file = ""
            if 'long_list' in self.info:
                file_stat = os.lstat(filename)
                file += stat.filemode(file_stat.st_mode) + '  '
                file += str(datetime.fromtimestamp(file_stat.st_ctime).replace(microsecond=0)) + ' '
            file += filename.split('/')[-1]
            if 'prefix' in self.info:
                if file.startswith('a'):
                    results.append(file)
            else:
                results.append(file)
        return results

    def __init__(self, filenames, info=set()):
        """
        The constructor for MockListDirectory class.

        Parameters:
            filenames (list): filenames.
            info (set): describe the type of command. Defaults to set().
        """
        self._folder = tempfile.mkdtemp()
        self._filenames = self.create_files(filenames)
        self._info = info

    def __del__(self):
        """
        The destructor for MockListDirectory class. Deletes all temporary files.
        """
        for filename in self.filenames:
            os.remove(filename)
        os.rmdir(self.folder)

    def create_files(self, filenames):
        """
        Create files based on their filenames.

        Parameters:
            filenames (list): list of filenames.

        Returns:
            list: absolute file path.
        """
        paths = []
        for filename in filenames:
            path = os.path.join(self.folder, filename)
            open(path, 'a').close()
            paths.append(path)
        return paths
