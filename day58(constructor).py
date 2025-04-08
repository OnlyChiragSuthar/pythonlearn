class person:
    # name = "harry"
    # occ = "Software Developer"

    def __init__(self,name,occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Divya","HR")
b = person("CHIRAG","MANAGER")
# print(a.name)
# name ="Divya"
# occ = "HR"
a.info()
b.info()