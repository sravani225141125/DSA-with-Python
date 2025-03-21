
'''
The code which is given below is the example of 
O(n^2) 
which is also known as loop within a loop
'''
def print_items(n) :
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)
