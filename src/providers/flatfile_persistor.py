"""
    flat file persistor class abstracts the I/O operations to flat file.
"""
from src.providers.persistor_base import Persistor_Base
from src.utility.file_functions import file_exist, write_binary_file, read_binary_file, delete_file

class Flat_File_Persistor(Persistor_Base):
    def __init__(self, config):
        self.config = config
        self.path = '%s/%s' % (config['default']['root_dir'], config['default']['folder_name'])

    def write(self, feature, dumps, **kwargs):
        filename = '%s.dill'%(feature.uid)
        write_binary_file(self.path,filename,dumps)

    def read(self, uid, **kwargs):
        filename = '%s.dill'%(uid)
        if file_exist(self.path, filename):
            content = read_binary_file(self.path, filename)
            return content
        return None

    def delete(self, uid, **kwargs):
        filename = '%s.dill'%(uid)
        if file_exist(self.path, filename):
            delete_file(self.path,filename)