print("Kaç adet sayının ağırlık merkezini bulmak istersiniz?\n")
number =int(input(" "))
list1 = []
sumx = 0
sumy = 0


print("*********Noktaları arasına virgül koyarak giriniz.*********\n")
for point in range (0,number):
       
    point = input("Noktayı giriniz:  ").split(",")
    x = float(point[0])
    y = float(point[1])
    point = (x,y)
    list1.append(point)
    sumx = sumx + x
    sumy = sumy + y
    
    
centerx = sumx / number
centery = sumy / number
centerofmass = [centerx,centery]

list2 = []
list3 = []
a = 0

for distance in range(0,number):
    
    distance = ((list1[a][0]- centerx)**2 + (list1[a][1] - centery)**2)**0.5
    h = (distance, list1[a])
    list2.append(distance)
    list3.append(h)
    a += 1
    
mindis = min(list2)
maxdis = max(list2)

list3.sort()

print("Ağırlık merkezi",centerofmass, "ve" ,point,"Son nokta arasındaki mesafe:", distance)
print("Ağırlık merkezi: ",centerofmass)
print("Listedeki noktalar:", list1)
print(list2)
print(list3)
print("Ağırlık merkezi ve en YAKIN nokta:", list3[0][1], "arası uzaklık:", list3[0][0])
print("Ağırlık merkezi ve en UZAK nokta:",list3[-1][1], "arası uzaklık:",list3[-1][0]) 
