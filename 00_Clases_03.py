class Warehouse:
    purpose = 'Storage'
    __region = 'west'

 


w1 = Warehouse()
w2 = Warehouse()
#w2.purpose = "North"
#print(w1.purpose, w1.region)
#print(w2.purpose, w2.region)
print(w1.__dict__)
print(w2.__dict__)
print(w1.purpose, w1._region)
