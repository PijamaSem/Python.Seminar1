# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("x","   ","y","   ","z","   ","result")
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if (not (x or y or z)) == ((not x) & (not y) & (not z)):
                result = True
            else:
                result = False
            print (x,y,z,result)