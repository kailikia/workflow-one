prods = [['omo','30kshs','300'], ['milk','50kshs','200'],
         ['bread','45kshs','359'], ['coffee','5kshs','79']]
stock = 0
for i in prods:
    stock = stock + int(i[-1])
print(stock)
