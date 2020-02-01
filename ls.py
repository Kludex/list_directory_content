#!/usr/bin/env python

from ls_options import LsOptions
from datetime import datetime
import sys
import os
import stat

class ListDirectoryContent():
    OPTIONS = {
        '-l': LsOptions.LONG_LISTING,
    }

    def __init__(self, argv):
        self.opts = self.get_command_options(argv)
        self.folder = self.get_folder_name(argv[1:])

    def get_command_options(self, argv):
        opts = []
        for arg in argv:
            if arg in self.OPTIONS.keys():
                opts.append(self.OPTIONS[arg])
        return opts

    def get_folder_name(self, argv):
        for arg in argv:
            if arg not in self.OPTIONS.keys() and not arg.startswith('-'):
                return arg
        return os.getcwd()

    def display_files(self):
        _, folder = self.prefix_folder()
        if not os.path.exists(folder):
            print("ls: cannot access directory")
        else:
            print(self.get_displayable_files(), end='')

    def get_displayable_files(self):
        prefix, folder = self.prefix_folder()
        info = self.options_info(folder)
        display = ''
        for file in os.listdir(folder):
            if not self.has_hidden_attribute(file) and file.startswith(prefix):
                display += ''.join(i + ' ' for i in info[file]) + file + '\n'
        return display

    def has_hidden_attribute(self, file):
        return file.startswith('.')

    def prefix_folder(self):
        if os.path.exists(self.folder):
            return "", self.folder
        split_folder = self.folder.split('/')
        folder = '/'.join(_ for _ in split_folder[:-1]) + '/'
        prefix = split_folder[-1]
        return prefix, folder

    def options_info(self, folder):
        info = dict()
        for file in os.listdir(folder):
            curr_file = os.path.join(folder, file)
            info[file] = []
            for opt in self.opts:
                if opt == LsOptions.LONG_LISTING:
                    info[file].append(self.mode_info(curr_file))
                    info[file].append(self.creation_time(curr_file))
        return info

    def creation_time(self, file):
        file_info = os.lstat(file)
        return str(datetime.fromtimestamp(file_info.st_ctime).replace(microsecond=0))
    
    def mode_info(self, file):
        file_info = os.lstat(file)
        return stat.filemode(file_info.st_mode)

if __name__ == '__main__':
    ls = ListDirectoryContent(sys.argv)
    ls.display_files()
