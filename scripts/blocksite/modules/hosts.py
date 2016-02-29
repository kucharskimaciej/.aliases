from shutil import copyfile
from functools import wraps
import os

def backup(fn):
    @wraps(fn)
    def func_wrapper(self, *args, **kwargs):
        self.make_backup()
        return fn(self, *args, **kwargs)
    return func_wrapper

class Hosts:
    def __init__(self,
                 hosts_path='/etc/hosts',
                 backup_file_path='hosts.bkp',
                 blocked_url='127.0.0.1',
                 bare_hosts_path='hosts_bare',
                 script_path='./'):

        self.hosts_path = hosts_path
        self.backup_file_path = backup_file_path
        self.blocked_url = blocked_url
        self.bare_hosts_path = bare_hosts_path
        self.script_path = script_path

        self.tmp_path = '%stmp' % self.script_path

    def make_backup(self, filename=None):
        if filename is None:
            filename = self.backup_file_path

        copyfile(self.hosts_path, filename)

    def restore(self):
        copyfile(self.backup_file_path, self.hosts_path)

    @backup
    def update(self, blocked_sites):
        if os.path.exists(self.tmp_path): os.remove(self.tmp_path)

        copyfile(self.bare_hosts_path, self.tmp_path)

        with open(self.tmp_path, 'a+') as file:
            file.write('\n')
            for site in blocked_sites:
                file.write('# %s \n' % site.short)
                file.write('%s %s\n' % (self.blocked_url, ' '.join(site.domains)))

        copyfile(self.tmp_path, self.hosts_path)
        os.remove(self.tmp_path)