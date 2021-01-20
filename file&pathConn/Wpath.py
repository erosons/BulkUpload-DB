from pathlib import Path

# Ways to access a file path in raw form(r)
path = Path(r"C:\Users\gw\Documents\Python Scripts\tutorial\abc.py")
print(path.name)
print(path.is_file)
print(path.exists)


# Accessing path with Class Path
path1 = Path("tutorial/abc.py")
print(path1.name)
print(path1.is_file)
print(path1.stem)
print(path1.suffix)

# Another way of Accessing path with Class Path
path2 = Path()/"tutorial"/"abc.py"
print(path2.name)
print(path2.is_file)
print(path2.stem)
print(path2.suffix)
print(path2.parent)

# Creating an arbitrary file path
path3 = path2.with_name("file.txt")
print(path3)
print(path3.absolute())  # This file does not exist in the path is
print(path3.home())      # Print the main path.exit
