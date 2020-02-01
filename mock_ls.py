
import tempfile
import os

class MockListDirectoryContent():

    @property
    def tmp_dir(self):
        return self._tmp_dir

    @property
    def argv(self):
        return self._argv

    def __init__(self, tmp_filenames, opt='', has_folder=True, prefix='', valid_folder=True):
        self._tmp_dir = self.create_folder()
        self._argv = self.create_argv(opt, has_folder, prefix, valid_folder)
        self.create_files(tmp_filenames)
    
    def __del__(self):
        for tmp_filename in os.listdir(self.tmp_dir):
            os.remove(os.path.join(self.tmp_dir, tmp_filename))
        os.rmdir(self.tmp_dir)

    def create_folder(self):
        return tempfile.mkdtemp()

    def create_files(self, tmp_filenames):
        for tmp_filename in tmp_filenames:
            open(os.path.join(self.tmp_dir, tmp_filename), 'a').close()

    def create_argv(self, opt, has_folder, prefix, valid_folder):
        argv = ['ls.py']
        if opt:
            argv.append(opt)
        if has_folder:
            prt = self.tmp_dir if valid_folder else self.tmp_dir[:-2] + '/'
            print("KK" if valid_folder else prt)
            argv.append(prt)
        if prefix:
            argv[-1] = argv[-1] + '/' + prefix
        return argv
