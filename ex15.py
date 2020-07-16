from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
fileAgain = input("> ")

txtAgain = open(fileAgain)

print(txtAgain.read())
txtAgain.close()