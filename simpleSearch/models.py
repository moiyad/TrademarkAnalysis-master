from django.db import models


class TrademarkModel(models.Model):
    Vienna_Code = (
        ('category_1', '1-CELESTIAL BODIES, NATURAL PHENOMENA, GEOGRAPHICAL MAPS'),
        ('category_2', '2-Human beings'),
        ('category_3', '3-Animals'),
        ('category_4', '4-SUPERNATURAL, FABULOUS, FANTASTIC OR UNIDENTIFIABLE BEINGS'),
        ('category_5', '5-PLANTS'),
        ('category_6', '6-LANDSCAPES'),
        ('category_7', '7-CONSTRUCTIONS, STRUCTURES FOR ADVERTISEMENTS, GATES OR BARRIERS'),
        ('category_8', '8-FOODSTUFFS'),
        ('category_9', '9-TEXTILES, CLOTHING, SEWING ACCESSORIES, HEADWEAR, FOOTWEAR'),
        ('category_10', '10-TOBACCO, SMOKERS REQUISITES, MATCHES, TRAVEL GOODS, FANS, TOILET ARTICLES'),
        ('category_11', '11-HOUSEHOLD UTENSILS'),
        ('category_12', '12-FURNITURE, SANITARY INSTALLATIONS'),
        ('category_13',
         '13-LIGHTING, WIRELESS VALVES, HEATING, COOKING OR REFRIGERATING EQUIPMENT, WASHING MACHINES, DRYING EQUIPMENT'),
        ('category_14', '14-IRONMONGERY, TOOLS, LADDERS'),
        ('category_15', '15-MACHINERY, MOTORS, ENGINES'),
        ('category_16',
         '16-TELECOMMUNICATIONS, SOUND RECORDING OR REPRODUCTION, COMPUTERS, PHOTOGRAPHY, CINEMATOGRAPHY, OPTICS'),
        ('category_17', '17-HOROLOGICAL INSTRUMENTS, JEWELRY, WEIGHTS AND MEASURES'),
        ('category_18', '18-TRANSPORT, EQUIPMENT FOR ANIMALS'),
        ('category_19', '19-CONTAINERS AND PACKING, REPRESENTATIONS OF MISCELLANEOUS PRODUCTS'),
        ('category_20',
         '20-WRITING, DRAWING OR PAINTING MATERIALS, OFFICE REQUISITES, STATIONERY AND BOOKSELLERS GOODS'),
        ('category_21', '21-GAMES, TOYS, SPORTING ARTICLES, ROUNDABOUTS'),
        ('category_22', '22-MUSICAL INSTRUMENTS AND THEIR ACCESSORIES, MUSIC ACCESSORIES, BELLS, PICTURES, SCULPTURES'),
        ('category_23', '23-ARMS, AMMUNITION, ARMOUR'),
        ('category_24', '24-HERALDRY, COINS, EMBLEMS, SYMBOLS'),
        ('category_25', '25-ORNAMENTAL MOTIFS, SURFACES OR BACKGROUNDS WITH ORNAMENTS'),
        ('category_26', '26-GEOMETRICAL FIGURES AND SOLIDS'),
        ('category_27', '27-FORMS OF WRITING, NUMERALS'),
        ('category_28', '28-INSCRIPTIONS IN VARIOUS CHARACTERS'),
        ('category_29', '29-COLOURS'),
    )
    Name = models.CharField(max_length=150, null=True)
    Product = models.CharField(max_length=150, null=True)
    Vienna_Code = models.CharField(max_length=150, choices=Vienna_Code, default='default')
    Image = models.ImageField(upload_to="./media/", null=True)
    Owner_name = models.CharField(max_length=150, null=True)
    Trademark_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.Name + '-' + self.Product
