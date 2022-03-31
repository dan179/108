



def younger_person():
    ages = [72,42,50,56,14,78,30,51,89,12,38,67,10]

    solution = ages[0]
    for age in ages:
        if age < solution
            solution = age

    print(solution)



def statistic():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]

    # 1 - how many elements are there in the list ?
    # 2 - what is the sum of all the numbers
    # 3 - Sum the negative numbers
    # 4 - Count how many are over 500
    count = 0 
    total = 0
    negative = 0 
    over_500 = 0

    for num in data:
        count += + 1
        total += num

        if num < 0:
            negative = negative + 1
            # negative += 1

        if(num > 500):
            over_500 += 1 


 
    print(f"1 solution is: {len(data)}")
    print(f"2 solution is: {total}")


def print_some_nums():
    # print the multiples of 10 that exsist between 10 and 100

    for u in range(10):
        print( (y + 1) * 10)
    
    for num in range(1, 11):
        print(num * 10)

    for x in range(10, 110, 10):
        print(x)


print("test test test")
younger_person()
statistics()
def print_some_nums()