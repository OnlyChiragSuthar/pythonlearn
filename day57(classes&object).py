class person:
    name = "harry"
    occupation = "software Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation} and His Salary is {self.networth}")
        # self ka matlab wo object jispe ye method apply ho rhi hai
a = person()
# a.name = "Shubham"
# a.occupation = "accountant"
# a.networth = 100
a.info()
b = person()
b.name = "Chirag"
b.occupation = "Gamer"
b.networth = 10000
# b.info()
# print(a.name,a.occupation,a.networth) 