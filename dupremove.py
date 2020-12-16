'''Lakshmi REddy
To remove duplicate elements  in a list.'''
def dupremove():
    L=[]
    x=[]
    
    
    n=int(input("Enter number of elements"))
    print("enter elements")
    for i in range(0,n):
        e=int(input())
        L.append(e)
    for i in L:
        for j in L:
            if i==j and i in L:
                L.remove(i)
                L.remove(L.index(j))
               
    print(L)
        
dupremove()
    
                
