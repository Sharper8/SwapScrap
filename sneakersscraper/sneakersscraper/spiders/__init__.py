# import scrapy

# class MonSpider(scrapy.Spider):
#     name = 'mon_spider'
#     start_urls = ['URL_de_la_page']

#     def parse(self, response):
#         noms = response.css('h3.DropCard__CardBrandName-sc-1f2e4y6-5::text').getall()
#         for nom in noms:
#             yield {
#                 'nom': nom,
#             }

import scrapy
import sqlite3

class MonSpider(scrapy.Spider):
    name = 'mon_spider'
    start_urls = ['URL_de_la_page']

    def __init__(self):
        super(MonSpider, self).__init__()
        self.conn = sqlite3.connect('ma_base_de_donnees.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS produits
                         (nom TEXT, model TEXT, lien_image TEXT)''')

    def parse(self, response):
        noms = response.css('h3.DropCard__CardBrandName-sc-1f2e4y6-5::text').getall()
        models = response.css('h4.DropCard__CardModelName-sc-1f2e4y6-4::text').getall()
        liens_images = response.css('img.image::attr(src)').getall()

        for nom, model, lien_image in zip(noms, models, liens_images):
            self.c.execute("INSERT INTO produits (nom, model, lien_image) VALUES (?, ?, ?)", (nom, model, lien_image))
            self.conn.commit()
            yield {
                'nom': nom,
                'model': model,
                'lien_image': lien_image
            }

    def closed(self, reason):
        self.conn.close()
        self.conn = sqlite3.connect('ma_base_de_donnees.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT COUNT(*) FROM produits")
        nombre_lignes = self.c.fetchone()[0]
        print("Nombre de lignes dans la table produits :", nombre_lignes)

