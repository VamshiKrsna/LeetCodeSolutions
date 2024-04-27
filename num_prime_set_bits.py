# 762. Prime Number Of Set Bits in Binary Representation
left,right = 6,10
fin = 0
lis = []
for i in range(left,right+1):
    num = bin(i)[2:]
    counter = num.count("1")
    if counter == 1:pass
    lis.append(counter)

print(lis) # Right till here.

# Checking Prime:
def is_prime(n):
    if n < 2:return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for item in lis:
    if is_prime(item):fin += 1

print(fin)