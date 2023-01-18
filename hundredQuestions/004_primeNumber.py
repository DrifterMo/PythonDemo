# coding = utf-8
""""
输入开始数字和结束数字，打印区间所有素数
只能被1和自己整除
"""

def primeNumber(start_num, end_num):
    primeNumber_list = []
    for num in range(start_num, end_num, 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primeNumber_list.append(num)
    return primeNumber_list


print(primeNumber(10, 100))


"""
思路：从结果倒退。找出区间内的所有数（print_prime），判断一个数是否是素数（is_prime)

示例代码：

def is_prime(number):
    if number in (1,2):
        return True
    for idx in range(2,number):
        if number % idx ==0:
            return False
    return True

def print_primes(begin, end):
    for number in range(begin, end+1):
        if is_prime(number):
            print(f"{number} is a prime")


begin = 11
end = 25
print_primes(begin, end)


"""

