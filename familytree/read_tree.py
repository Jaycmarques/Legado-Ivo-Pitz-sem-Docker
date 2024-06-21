# Create your models here.
class FamilyMember:
    """
    - This class handles information about family members
    which are essential to build the tree connections.
    - The id field follows the format a.b.c.d(...)
    - The children attribute consists of a list of children
    - Partner corresponds to the current partner of the
    family member in the blood line.
    - The divorcedParent attribute is used to handle situations
    where a member has a child from a previous marriage/relationship,
    so it is associated with the child's name (i.e: John had a son with
    Jessica called Steve, but now John is married to Katherin. So when
    displaying Steve on the tree under John's name we want to display
    "Steve (son of Jessica) rather than simply Steve."
    """

    def __init__(self, id, name: str):
        self.id = id
        self.name = name
        self.children = []
        self.partner = ''
        self.divorcedParent = ''

    def addChild(self, p: 'FamilyMember', divorcedParent: str = ''):
        p.divorcedParent = divorcedParent
        self.children.append(p)

    def addPartner(self, name: str):
        self.partner = name

    def printFamilyMember(self):
        """
        This method simply displays basic info of a family member.
        """
        if self.divorcedParent == '':
            print(f'{self.id:s} -- {self.name:s}')
        else:
            print(f'{self.id:s} -- {self.name:s} (filho(a) de {self.divorcedParent:s})')

    def printTree(self):
        """
        This method is used to print the family tree starting from 
        a specific person, i.e. only a portion of the entire family
        tree is displayed. Note that the function is called recursively.
        """
        self.printFamilyMember()
        if len(self.children) > 0:
            for c in self.children:
                if len(c.children) > 0:
                    c.printTree()
                else:
                    c.printFamilyMember()


def printSomeonesTree(name: str):
    # Search for a person and print their tree
    for p in family:
        if p.name == name:
            p.printTree()
            break


def setDivorcedParent(name: str, parent: str):
    # Set the divorced parent of a family member
    # This can be set in the constructor, but we
    # never know what the future holds
    for p in family:
        if p.name == name:
            p.divorcedParent = parent
            break


def addNewMember(name: str, bloodlineParent: str):
    # we first have to look how many children
    # the blood line parent has to find the new
    # member's id
    for p in family:
        if p.name == bloodlineParent:
            bloodlineParent_id = p.id
            bloodlineParent_nchildren = len(p.children)
            break
    if bloodlineParent_nchildren == 0:
        id = f'{bloodlineParent_id:s}.1'
    else:
        id = f'{bloodlineParent_id:s}.{bloodlineParent_nchildren+1:d}'
    new = FamilyMember(id, name)
    p.addChild(new)


# This is where the data contained in the
# familyData.txt file is read and parsed.
# For now the id, name and partner are extracted.
# The children follow from the numbering (id) convention
family = []
with open('familyData.txt') as file:
    lines = file.readlines()
    i = 0
    for l in lines:
        div = l.split(" - ")
        id = div[0]
        name = div[1].split(",")[0].strip()
        P = FamilyMember(id, name)
        married = l.lower().replace("casada", "casado")
        married = married.replace("-", ",")
        married = married.lower().split("casado com")
        if len(married) > 1:
            married = married[1].split(",")[0]
            P.addPartner(married.title().strip())
        family.append(P)
        i += 1

for i in range(len(family)):
    id = family[i].id
    k = 1
    for j in range(len(family)):
        id_format = f'{id:s}.{k:d}'
        if family[j].id == id_format:
            family[i].addChild(family[j])
            k += 1

# count = 0
# with open('foo.txt') as file:
#     lines = file.readlines()
#     i = 0
#     for l in lines:
#         casado = l.lower().replace("casada", "casado")
#         casado = casado.replace("-", ",")
#         casado = casado.lower().split("casado com")
#         if len(casado) > 1:
#             casado = casado[1].split(",")[0]
#             print(casado.title().strip())
