from attr import attrs, attrib

@attrs
class Proxy(object):
    host = attrib(type=str,default='0')
    port = attrib(type=int,default=0)

    def __str__(self):
            """
            to string, for print
            :return:
            """
            return f'{self.host}:{self.port}'
