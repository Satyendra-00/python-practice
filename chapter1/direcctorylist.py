import os
#definingn path of the directory
directory_path = '/Users/satye/OneDrive/Desktop/Python'
#listing the content of the directory
content=os.listdir(directory_path)
#printing the content of the directory
for item in content:
    print(item)