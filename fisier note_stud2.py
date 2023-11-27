f=open('fisier note_stud', 'r')
lst=list(f)
f.close()

for i, linie in enumerate(lst):
    print(i+1, ':\t',linie, end='')