from itertools import combinations

T=[['Bread', 'Butter', 'Jam', 'Milk'],
   ['Bread', 'Butter', 'Milk'],
   ['Bread', 'Juice', 'Curd'],
   ['Bread', 'Milk', 'Juice'],
   ['Butter', 'Juice', 'Milk']]
N=len(T); min_sup=0.6

F={frozenset([i]) for t in T for i in t if sum(1 for x in T if i in x)/N>=min_sup}
allF=F.copy(); k=2
while F:
    C={a|b for a in F for b in F if len(a|b)==k}
    F={c for c in C if sum(1 for t in T if c.issubset(t))/N>=min_sup}
    allF |= F; k+=1

print("Freq:", [set(x) for x in allF])
# Fix: convert tuple to frozenset before subtraction
print("Rules 100% conf:", [(set(frozenset(l)), set(f - frozenset(l))) 
      for f in allF if len(f)>1 for i in range(1,len(f)) for l in combinations(f,i) 
      if sum(1 for t in T if f.issubset(t))==sum(1 for t in T if frozenset(l).issubset(t))])
