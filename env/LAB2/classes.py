
class User(object):

    def __init__(self, firstname, familyname, email, city, country, gender, password):
        self.firstname = firstname
        self.familyname = familyname
        self.email = email
        self.city = city
        self.country = country
        self.gender = gender
        self.password = password

    def User(self):
        return self

    def __str__(self):
        return self.firstname+" "+self.email
