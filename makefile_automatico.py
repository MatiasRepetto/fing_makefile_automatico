import os

print("Developed by Matias Repetto Zecchi, GitHub: MatiasRepetto\n")

print("Cuantos Modulos tiene ? :")
cantmodulos = int(input())

modd = []

mods = "MODULOS ="

for x in range(0, cantmodulos):
    print("ingrese el nombre del modulo: ")
    modules = str(input())
    modd.append(modules)
    mods = mods + " " + modules

mf = open("Makefile.txt", "w")
mf.write(mods)
mf.close()

with open("Makefile.txt", "a") as mk:
    lines = ["\n", "\nCC = g++", "\nLD = -g -Wall", "\nMC = -c", "\n","\nODIR = obj", "\n",
             "\nOBJ = $(MODULOS:%=$(ODIR)/%.o)", "\n",
             "\nmain: $(OBJ) main.cpp", "\n\t$(CC) $(LD) $(OBJ) main.cpp -o main"]
    mk.writelines(lines)
    mk.close()

for j in range(0, cantmodulos):
    mf = open("Makefile.txt", "a")
    linesj = ["\n", "\nobj/" + modd[j] + ".o: include/" + modd[j] + ".h src/" + modd[j] + ".cpp",
              "\n\t$(CC) $(LD) $(MC) src/" + modd[j] + ".cpp -o obj/" + modd[j] + ".o"]
    mf.writelines(linesj)
    mf.close()

with open("Makefile.txt", "a") as mk:
    linesk = ["\n", "\nclean:", "\n\trm -f $(OBJ) main", "\n", "\nrebuild:", "\n\tmake clean", "\n\tmake"]
    mk.writelines(linesk)
    mk.close()

os.rename("./Makefile.txt", "./Makefile")

