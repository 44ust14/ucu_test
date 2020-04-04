import math
print("Ласкаво Просимо!\nЗа допомогою цієї програми,ви зможете розрахувати взаємне розміщення 2 кіл")
x1=int(input("Введіть x1:\t"))
y1=int(input("Введіть y1:\t"))
r1=int(input("Введіть r1:\t"))
x2=int(input("Введіть x2:\t"))
y2=int(input("Введіть y2:\t"))
r2=int(input("Введіть r2:\t"))


r_sum=(r1 + r2) # сума радіусів
r_div=(r1 - r2) # різниця
center_distance=math.sqrt((x2-x1)**2 + (y2-y1)**2) #відстань між центрами
if x1==x2 and y1==y2 and r1==r2:
    print('Кола збігаються')
elif center_distance ==r_sum:
    print('Кола мають зовнішній дотик')
elif center_distance == r_div:
    print('Кола мають внутрішній дотик')
elif r_div<center_distance<r_sum:
    print('Кола перетинаються,мають дві спільні точки')
else:
    print("Кола не перетинаються")
