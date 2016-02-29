class BlockedSite:
    def __init__(self, short, domains, max_timeout=5):
        self.short = short
        if domains and len(domains):
            self.domains = domains
        else:
            raise ValueError('must specify at least one domain')

        self.max_timeout = max_timeout

    @staticmethod
    def from_record(record=''):
        if isinstance(record, str):
            _ = record.split(' ')
        else:
            _ = record

        [short, domains, max_timeout] = [_[0], _[1:-1], _[-1]]

        try:
            max_timeout = int(max_timeout)
            return BlockedSite(short, domains, max_timeout)
        except ValueError:
            domains.append(max_timeout)
            return BlockedSite(short, domains)

    def __str__(self):
        return "%s %s %d" % (self.short, ' '.join(self.domains), self.max_timeout)