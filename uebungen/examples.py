lst = [12, 45, 43, 73, 17, 13, 11]

bit_lst = [1, 1, 1, 1 , 0, 0, 0, 0]

# filter, map, sum
mapped_lst = list(map(lambda v: v ^ 1, bit_lst))
print(mapped_lst)
print(bin(240 ^ 0xff))
print(bin(240 ^ 255))
print(bin(240 ^ 0b11111111))
print(bin(0b11110000 ^ 0xff))
print(bin(0b11110000 ^ 0b11111111))
exit(0)

neue_lst = list(filter(lambda x: x < 20, lst))
print(neue_lst)

def filter_props(x):
    return x < 20

neue_lst = list(filter(lambda x: x < 20, lst))

