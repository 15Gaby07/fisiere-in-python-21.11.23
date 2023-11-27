f=open('fisier note_stud')
lst=list(f)
f.close()

for i in range (len(lst)):
    print(i+1,':\t',lst[i])