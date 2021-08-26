from collections import deque

# a= deque()
# b= deque('abcdef')
# c = deque([1,2,3,4,5])
# print(a,b,c, sep='\n')

b= deque('abcdef', maxlen=3)
c = deque([1,2,3,4,5], maxlen=4)
print(b,c, sep='\n')
