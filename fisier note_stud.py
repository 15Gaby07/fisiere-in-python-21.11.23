f=open('fisier note_stud', 'r')
while True:
    linie=f.readline()
    if len(linie)==0:
        break
    print(linie, end='')
f.close()