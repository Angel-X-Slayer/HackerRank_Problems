# def count(start=0, step=1):
#     # count(10) --> 10 11 12 13 14 ...
#     # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
#     n = start
#     while :
#         yield n
#         n += step

##****************************************##

my_list=[x for x in range(1,10)]
for i in range(len(my_list)):
    yield my_list*2
print( my_list)