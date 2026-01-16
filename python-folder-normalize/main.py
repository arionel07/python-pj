import os

os.chdir('./test')
print(os.listdir())

for folder in os.listdir():
    #parts = folder.split('-')
    #if len(parts) == 3 and (2003 <= int(parts[0]) < 2007 and...):
    year, month, day, = folder.split('-')
    os.rename(folder, day + ':' + month + '--' + year)
        
