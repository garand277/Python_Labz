def sum_nested1(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested1(item)
        else:
            total += item
    return total


def sum_nested2(nums):
    total_sum = 0
    stack = [nums]
    while stack:
        current_list = stack.pop()
        for item in current_list:
            if isinstance(item, list):
                stack.append(item)
            else:
                total_sum += item
    return total_sum

lst = [1, [2, 3, [4, [5]]]]
print(sum_nested1(lst))
print(sum_nested2(lst))


def f_rec(a, k):
    if k == 1:
        return print(1)
    k -= 1
    a = 0.5 * (1**0.5 + 0.5 * a**0.5)
    if k > 1:
        a = f_rec(a, k)
    else: print(a)
   

def f(k):
    i = 1
    a = 1
    while i < k:
        a = 0.5 * (1**0.5 + 0.5 * a**0.5)
        i += 1
    print(a)

f_rec(1, 7)
f(7)
