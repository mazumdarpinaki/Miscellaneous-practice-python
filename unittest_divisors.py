def get_divisors(num,possible_divisors):
    '''(int,list of int) ->list of int
    return a list of values from possible_divisors that are divisors of num.

    >>>get_divisors(8,[1,2,3])
    [1,2]
    >>>get_divisors(4,[-2,0,2])
    [-2,2]
    '''

    divisors=[]
    for item in possible_divisors:
        if item !=0 and num % item==0:
            divisors.append(item)


        return divisors


    if _name_=='_main_':
        import doctest
        doctest.testmod()
