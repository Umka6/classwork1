#import module as mod
#import os

#print(mod.plus(2,4))
#print(os.getpid())

import os
from module import min as m, plus as p

print(m(12,2))
print(os.getpid())
try:
    print(plus(3,7))
except NameError:
    print('Такого метода нет')