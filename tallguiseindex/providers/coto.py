import requests
from lxml import etree


from . import Provider

class Coto(Provider):
    URLS = [
        'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-alimentos-frescos-frutas-y-verduras-hortalizas-pesadas/_/N-g7vcbk?Ntt=1004&Ntk=product.sDisp_091',
        'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-alimentos-frescos-frutas-y-verduras-hortalizas-pesadas/_/N-g7vcbk?Nf=product.startDate%7CLTEQ+1.4796864E12%7C%7Cproduct.endDate%7CGTEQ+1.4796864E12&No=12&Nr=AND%28product.language%3Aespa%C3%B1ol%2COR%28product.siteId%3ACotoDigital%29%29&Nrpp=12&Ntk=product.sDisp_091&Ntt=1004'
    ]

    def __init__(self):
        self.products = {}

        for url in Coto.URLS:
            self.scrape_url(url)

    def scrape_url(self, url):
        r = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8743.83.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.93 Safari/537.36'
        })
        tree = etree.HTML(r.text)
        for product in tree.iterfind('.//li'):
            description = product.find('.//div[@class="descrip_full"]')
            if description is None:
                continue
            name = description.text
            price = float(product.find('.//span[@class="atg_store_newPrice"]').text.strip().strip('$'))
            self.products[name] = price

    def price_for_item(self, item):
        loweritem = item.lower()
        for (k, v) in self.products.iteritems():
            if loweritem in k.lower():
                return v

        return None
