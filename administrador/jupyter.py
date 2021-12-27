def busqueda_binaria(array, valor):
    ary = array
    a = 0
    b = len(array)
 
    while a < b:
        m = (a + b) // 2
 
        if array[m] == valor:
            return m
        elif array[m] < valor:
            a = m + 1
        else:
            b = m
 
    return None
 
x1 = [0,1,2,3,4,5,6,7]
x2 = [1,4,8,12,41]
x3 = [0,1,2,4,8,16,32]