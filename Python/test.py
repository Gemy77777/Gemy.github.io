import os
folders = input("enter folder(s) name: ").split()
for folder in folders:
    print(f"---- listing files in {folder} directory ----")
    files = os.listdir(folder)
    for file in files:
        print(f"|_{file}")



