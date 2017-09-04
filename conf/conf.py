import os
import sys

#print(os.path.join(os.path.abspath(__file__),'a.fdsaf'))
PATH = lambda p:os.path.dirname(os.path.dirname(os.path.join(os.path.abspath(__file__),p)))

x = PATH('a.apk')

print(x)