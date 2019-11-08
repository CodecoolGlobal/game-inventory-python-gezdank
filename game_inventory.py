
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.

inve = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']



def display_inventory(inventory):
    for i in inventory.items():
        print(i[0]+": "+ str(i[1]))

print(display_inventory(inve))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1

add_to_inventory(inve, dragon_loot)

print(display_inventory(inve))

def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''



def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    
    '''
    '''
    inve = []
    with open(filename, "r") as file:
        inve.append(f.readline())
    '''


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''
    #with open(filename, "w") as f:
