
#the plan is, to call this function when + operator is seen.
#then, i do like result += number[i], then pop([0]) value, then call next part
#or when looking at expression, it splits the list into subsets, when a
#specific operator is seen

list = [2, 3, 4, 5, 65, 3]
list2 = [ 'allow', 'this', 'atrocity']
def func(*args):
    print(*args)

func(list, list2)