# W A P to calculate total salary of emp based on da =10%, ta =12%, hra =15%
B = int(input('enter salary ='))
da = B * 10/100
ta = B * 12/100
hra = B * 15/100

t_sal = B + da + ta + hra

print('Basic salary=',B)
print('DA =',da)
print('TA =',ta)
print('HRA =',hra)
print('Total salary =',t_sal)