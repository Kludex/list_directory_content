#!/usr/bin/env python

import unittest
import os

from option import Option
from ls import ListDirectory
from mock_ls import MockListDirectory as Mock

class TestListDirectory(unittest.TestCase):
    """
    TestCase for ListDirectory.
    """

    def test_default(self):
        """
        Tests default command.

        Files:
            /test/a
            /test/b
        Run:
            ls.py /test/
        Result:
            a
            b
        """
        filenames = ['a', 'b']
        mock = Mock(filenames)

        command = ListDirectory(mock.args())
        result = list(command.files_list())
        expect = mock.result_list()

        self.assertCountEqual(expect, result)

    def test_hidden_files(self):
        """
        Tests with hidden files.

        Files:
            /test/a
            /test/b
            /test/.c
        Run:
            ls.py /test/
        Result:
            a
            b
            .c
        """
        filenames = ['a', 'b', '.c']
        mock = Mock(filenames)

        command = ListDirectory(mock.args())
        result = list(command.files_list())
        expect = mock.result_list()

        self.assertCountEqual(expect, result)

    def test_miss_folder(self):
        """
        Tests with folder name missing.

        Files:
            /test/a
            /test/b
        Run:
            cd /test/
            ls.py
        Result:
            a
            b
        """
        filenames = ['a', 'b']
        mock = Mock(filenames, {'miss_folder'})

        os.chdir(mock.folder)

        command = ListDirectory(mock.args())
        result = list(command.files_list())
        expect = mock.result_list()

        self.assertCountEqual(expect, result)

    def test_wrong_folder(self):
        """
        Tests with wrong folder name.

        Files:
            /test/a
            /test/b
        Run:
            ls.py /test/wrong/
        Result:
            raise Exception
        """
        filenames = ['a', 'b']
        mock = Mock(filenames)

        with self.assertRaises(Exception):
            ListDirectory.folder_from(mock.wrong_folder())

    def test_prefix(self):
        """
        Tests with prefix filename.

        Files:
            /test/aa
            /test/ab
            /test/bb
        Run:
            ls.py /test/a
        Result:
            aa
            ab
        """
        filenames = ['aa', 'ab', 'bb']
        mock = Mock(filenames, {'prefix'})

        command = ListDirectory(mock.args())
        result = list(command.files_list())
        expect = mock.result_list()

        self.assertCountEqual(expect, result)

    def test_wrong_prefix(self):
        """
        Tests with wrong prefix filename.

        Files:
            /test/a
            /test/b
        Run:
            ls.py /test/c
        Result:

        """
        filenames = ['aa', 'ab', 'bb']
        mock = Mock(filenames, {'wrong_prefix'})

        command = ListDirectory(mock.args())
        result = list(command.files_list())
        expect = mock.result_list()

        self.assertCountEqual(expect, result)

    def test_long_list_option(self):
        """
        Tests with long list option.

        Files:
            /test/a
            /test/b
        Run:
            ls.py -l /test/
        Result:
            -rw-rw-r--  2020-02-01 18:47:00 a
            -rwxr-xr-x  2020-02-01 19:18:06 b
        """
        filenames = ['a', 'b']
        mock = Mock(filenames, {'long_list'})

        command = ListDirectory(mock.args())
        result = list(command.files_list())
        expect = mock.result_list()

        self.assertCountEqual(expect, result)

    def test_wrong_option(self):
        """
        Tests with wrong option.

        Files:
            /test/a
            /test/b
        Run:
            ls.py -p /test/
        Result:
            raise Exception
        """
        with self.assertRaises(Exception):
            Option(Mock.wrong_option())

if __name__ == '__main__':
    unittest.main()
