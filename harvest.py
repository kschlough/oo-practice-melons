############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, name, is_bestseller = None):
        """Initialize a melon."""
        self.reporting_code = code
        self.firstharvet = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.name = name
        self.is_bestseller = is_bestseller

        self.pairings = []
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # print(self.pairings)
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.reporting_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    musk = MelonType('musk','1998','color',True, 'Muskmelon', True)
    musk.add_pairing('mint')
    casaba = MelonType('cas','2003','orange',False,'Casaba')
    casaba.add_pairing('strawberries and mint')

    crenshaw = MelonType('cren', '1996', 'yellow', False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    yellow_watermelon = MelonType('yw', '2013', 'yellow', False, 'Yellow_Watermelon', True)
    yellow_watermelon.add_pairing('ice cream')
    
    all_melon_types = []

    all_melon_types.append(musk) 
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)
    
    print(all_melon_types)
    return all_melon_types
    

def print_pairing_info(melon_types):
    
    """Prints information about each melon type's pairings."""


    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print (f'- {pairing}')
        

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dictionary = {}

    for melon in melon_types:
        melon_dictionary[melon.code] = melon.name

    return melon_dictionary


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, code, shape, color, harvested_from, harvested_by):

        self.code = code
        self.shape = shape
        self.color = color
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        
        self.sellable = []
    
    def is_sellable(self, sellability):
        self.sellable.append(sellability)


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []
    melon_1 = Melon('yw', 8, 7, "Field 2", "Sheila")
    melon_2 = Melon('yw', 3, 4, "Field 2", "Sheila")
    melon_3 = Melon('yw', 9, 8, "Field 3", "Sheila")
    melon_4 = Melon('cas', 10, 6, "Field 35", "Sheila")
    melon_5 = Melon("cren", 8, 9, "Field 35", "Michael")
    melon_6 = Melon('cren',8,2,'Field 35','Michael')
    melon_7 = Melon('cren',2,3,'Field 4','Michael')
    melon_8 = Melon('musk',6,7,'Field 4','Michael')
    melon_9 = Melon('yw',7,10,'Field 3','Sheila')
    
    melon_list.append(melon_1)
    melon_list.append(melon_2)
    melon_list.append(melon_3)
    melon_list.append(melon_4)
    melon_list.append(melon_5)
    melon_list.append(melon_6)
    melon_list.append(melon_7)
    melon_list.append(melon_8)
    melon_list.append(melon_9)
    
 
    return melon_list

def get_sellability_report(melon_list):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melon_list():
        if melon.shape > 5 and (melon.color > 5) and (melon.harvested_from != "Field 3"):
            melon.is_sellable(True)
    
    for melon in melon_list:
        print(f'{melon.code} harvested by {melon.harvested_by} is sellable:' (melon.is_sellable).get())


