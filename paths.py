from pathlib import Path

#absolute paths
# /usr/local/bin

#relative path
# 

# path = Path('ecommerce')
# print(path.exists()) # returns True

path = Path()
for file in path.glob('*.py'): #gets py files in current directory
    print(file)

