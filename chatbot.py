import lib
from config import BYE_LIST

x = ""
while x not in BYE_LIST:
    x = input()
    y = lib.response(x)
    print(y)