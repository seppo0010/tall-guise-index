class Provider(object):
    def price_for_item(self, item):
        raise Exception('Children of provider must implement price_for_item')

from . import coto
