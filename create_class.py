

class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
        """ (Contact, str, str, str) -> NoneType

       Initialize this Contact with first name first_name, last name
       last_name, and email address email_address.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

class fraction(object):
    def __init__(self,numer,denom):
        self.numer=numer
        self.denom=denom
    def __str__(self):
        return str(self.numer)+'/'+str(self.denom)
    def getnumer(self):
        return self.numer
    def convert(self):
        return self.numer/self.denom

class intSet(object):
    def __init__(self):
        self.vals=[]
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
    def member(self,e):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + "not found")
    def __add__(self,other):
        return (self.vals)+(other.vals)
    def __str__(self):
        self.vals.sort()
        result=' '
        for e in self.vals:
            result=result+str(e)+','
        return '('+result[:-1]+')'
    
