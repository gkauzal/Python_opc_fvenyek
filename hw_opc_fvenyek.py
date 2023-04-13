"1.feladat"

nums = [3, 4, 9, 6, 2]


def arr(nums):
    for x in nums:
        if x % 2 == 0:
            print(f'{x} osztható')
        else:
            print(f'{x} nem osztható')


arr(nums)
"2.feladat"

players = ['Peter', 'Kate', 'John']


def numb_list(list):
    i = 1
    for x in list:
        print(f'{i}. {x}')
        i += 1


numb_list(players)
"3.feladat"

x = ('', 4, True)
arr = []


def get_data_type(x):
    for x in x:
        if type(x) is int:
            arr.append('integer')
        elif type(x) is bool:
            arr.append('boolean')
        elif type(x) is str:
            arr.append('string')
        else:
            arr.append('other type')


get_data_type(x)

print(arr)