from functools import wraps
from time import sleep

from modules.blocked_site import BlockedSite


def modifyrecord(fn):
    @wraps(fn)
    def func_wrapper(self, *args, **kwargs):
        result = fn(self, *args, **kwargs)
        self.write()

        return result
    return func_wrapper


class BlockedSites:
    def __init__(self, hosts, filename='sites.dat'):
        self.filename = filename
        self.sites = dict()
        self.hosts = hosts

        # create a file if it doesn't exist
        open(self.filename, 'a').close()

        self.read_block_data()

    def read_block_data(self):
        with open(self.filename) as sites:
            for record in sites:
                site = BlockedSite.from_record(record)
                self.sites[site.short] = site

    def list(self):
        for site in self.sites.values():
            print(site)

    @modifyrecord
    def add(self, record):
        new_site = BlockedSite.from_record(record)

        if new_site.short in self.sites:
            site = self.sites[new_site.short]
            site.max_timeout = new_site.max_timeout
            site.domains = list(set(site.domains + new_site.domains))
        else:
            self.sites[new_site.short] = new_site

        self.hosts.update(self.sites.values())

    @modifyrecord
    def remove(self, names):
        if isinstance(names, str):
            names = [names]

        for name in names:
            if name in self.sites:
                del self.sites[name]

        self.hosts.update(self.sites.values())

    def write(self):
        with open(self.filename, 'w') as file:
            for site in self.sites.values():
                file.write(str(site))
                file.write('\n')

    def unblock(self, short_name, time=None):
        if short_name not in self.sites:
            raise KeyError('site %s is not blocked' % short_name)

        site = self.sites[short_name]
        time = int(time) or site.max_timeout

        if time > site.max_timeout:
            raise ValueError('can\'t unblock %s for more than %d minutes' % (short_name, time))

        if time > 0:
            new_sites = self.sites.copy()
            del new_sites[short_name]

            self.hosts.update(new_sites.values())

            sleep(60*time)
            self.hosts.update(self.sites.values())
