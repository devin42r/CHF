class Student(object):
    '''A student at our school'''

    def __init__(self, name, birth='', address=''):
        self.name = name
        self.birth = birth
        self.address = address

    def get_name(self):
        return self.name


class ISStudent(Student):

    def __init__(self, name, birth='', address='', ctype=''):
        super().__init__(name, birth, address)
        self.ctype = ctype

    def set_computer_type(self, ctype):
        self.ctype = ctype


s1 = Student('Dan Jones', '6/15/91', '2955 West Drive')

# print(s1.name)
s2 = Student('Bertha Jones')
s3 = Student('Julie Jones', address='2955 West Drive')
s1.name = 'asdf'
s2 = ISStudent('Barry')