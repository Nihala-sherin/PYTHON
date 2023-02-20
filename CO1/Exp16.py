dic = {'Afla':5, 'Thesni':20, 'Fami':17}
l = list(dic.items())
l.sort()
d = dict(l)
print("Ascending is: ", d)
l = list(dic.items())
l.sort(reverse = True)
d = dict(l)
print("Descending is: ", d)
