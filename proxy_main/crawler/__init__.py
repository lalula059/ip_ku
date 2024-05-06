import pkgutil
from .base import BaseCrawler
import inspect


# load classes subclass of BaseCrawler
# classes = []
# for loader, name, is_pkg in pkgutil.walk_packages(__path__):
#     module = loader.find_module(name).load_module(name)
#     for name, value in inspect.getmembers(module):
#         globals()[name] = value
#         if inspect.isclass(value) and issubclass(value, BaseCrawler) and value is not BaseCrawler \
#                 and not getattr(value, 'ignore', False):
#             classes.append(value)
# __all__ = __ALL__ = classes
print(__path__)
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name)
    print(module)
import pkgutil
import pprint

print('crawler.__path__ before:')
pprint.pprint(__path__)
print()

__path__ = pkgutil.extend_path(__path__, __name__)

print('crawler.__path__ after:')
pprint.pprint(__path__)
print()