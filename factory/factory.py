class Shortener(object):
    def __init__(self, shortener):
        self.shortener = shortener

class Bitly(Shortener):
    @classmethod
    def service(cls, service):
        return service == 'bitly'

    def short(self, URL):
        return 'b'

class Clipp(Shortener):
    @classmethod
    def service(cls, service):
        return service == 'clipp'

    def short(self, URL):
        return 'c'

    
def ShortURL(service):
    for cls in Shortener.__subclasses__():
        if cls.service(service):
            return cls(service)
    raise ValueError


clipp = ShortURL('clipp')
print(clipp.short('xx'))

bitly = ShortURL('bitly')
print(bitly.short('xx'))

