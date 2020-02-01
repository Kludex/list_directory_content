#!/usr/bin/env python

from ls import ListDirectoryContent
from mock_ls import MockListDirectoryContent as Mock

from datetime import datetime
import unittest
import stat
import os

class TestListDirectoryContent(unittest.TestCase):
    WRONG_OPT = '-p'

    def create_result(self, tmp_filenames, mock=None, wrong_opt=False):
        if wrong_opt:
            return ""
        result = ''
        for filename in tmp_filenames:
            if mock:
                file_info = os.lstat(os.path.join(mock.tmp_dir, filename))
                date = str(datetime.fromtimestamp(file_info.st_ctime).replace(microsecond=0))
                mode = stat.filemode(file_info.st_mode)
                result += mode + ' ' + date + ' '
            result += filename + '\n'
        return result

    def test_list_all_files(self):
        tmp_filenames = ['a', 'b']
        mock = Mock(tmp_filenames)
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(),
                                  self.create_result(tmp_filenames))

    def test_list_all_hidden_files(self):
        tmp_filenames = ['a', 'b', '.c']
        mock = Mock(tmp_filenames)
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(), 
                                  self.create_result(tmp_filenames[:-1]))

    def test_without_folder_name(self):
        tmp_filenames = ['a', 'b']
        mock = Mock(tmp_filenames, has_folder=False)

        os.chdir(mock.tmp_dir)
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(), 
                                  self.create_result(tmp_filenames))

    def test_wrong_folder_name(self):
        tmp_filenames = ['a', 'b']
        mock = Mock(tmp_filenames, valid_folder=False)
        
        print(mock.argv)
        ls = ListDirectoryContent(mock.argv)
        ls.display_files()
        self.assertMultiLineEqual(ls.get_displayable_files(),
                                  self.create_result(tmp_filenames))

    @unittest.skip
    def test_more_than_one_folder_name(self):
        pass

    def test_list_prefix(self):
        tmp_filenames = ['aa', 'ab', 'bb']
        mock = Mock(tmp_filenames, prefix='a')

        os.chdir(mock.tmp_dir)
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(), 
                                  self.create_result(tmp_filenames[:-1]))

    def test_list_wrong_prefix(self):
        tmp_filenames = ['aa', 'ab', 'bb']
        mock = Mock(tmp_filenames, prefix='j')

        os.chdir(mock.tmp_dir)
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(), 
                                  self.create_result([]))

    def test_long_list_option(self):
        tmp_filenames = ['a', 'b']
        mock = Mock(tmp_filenames, opt='-l')
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(),
                                  self.create_result(tmp_filenames, mock))

    # maybe change this one
    def test_wrong_options(self):
        tmp_filenames = ['a', 'b']
        mock = Mock(tmp_filenames)
        
        ls = ListDirectoryContent(mock.argv)
        self.assertMultiLineEqual(ls.get_displayable_files(),
                                  self.create_result(tmp_filenames))

if __name__ == '__main__':
    unittest.main()
