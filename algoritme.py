#mbledhi te gjitha elementet e listes
scores = [68,42,57,78,35,62,50]
shuma = 0
for i in scores:
   shuma= shuma+i
if i==57:
    continue
print(shuma)

shuma2=0

for i in scores:
    if i>35:
        shuma2=shuma2+i

print(shuma2)


