import os

path = "."

for root, dir, file in os.walk(path, topdown=True):
    for f in file:
        print(f)


