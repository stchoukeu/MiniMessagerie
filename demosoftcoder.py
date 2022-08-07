# student management

class Student:
    '''Class student'''
    # Global variable
    university = "UY1-University of Yaounde 1"

    def __init__(self, name, matricule, age = 0) -> None:
        '''Initialise un etudiant'''
        self.name = name
        self.matricule = matricule
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    @classmethod
    def afficherUniversite(cls, other):
        print ('Etudiant', other.name, 'est de universite de', cls.university)



