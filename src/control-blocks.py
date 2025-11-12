# flow control stmts 
"""
if - elif - else
for - loop
"""

temp = 35
if temp > 30:
    print("very hot")
elif temp > 25:
    print("reasonable heat")
else:
    print("cool weather")

# [0, 4] inclusive
for i in range(5):
    print(i)

# [1,9]
for i in range(1,10):
    print(i)

#1, 3, 5, 7, 9
for i in range(1,10,2):
    print(i)