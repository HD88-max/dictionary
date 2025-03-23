dictionary =  {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
k = 2
result = 0
for key in dictionary:
    if dictionary[key]==k:
        result=result+1
print(result,"times it is repeating")