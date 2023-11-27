with open('fisier note_stud', 'rt') as f:
    linii=f.readlines()

print(linii)
print()
for linie in linii:
    print(linie.rstrip())