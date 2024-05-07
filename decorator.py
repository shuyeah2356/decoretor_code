import time

# 计时器装饰器
def test_time(func):
    def wrapper(*args, **kwargs):
        time_1 = time.time()
        result = func(*args, **kwargs)
        time_2 = time.time()
        print(time_2-time_1)
        print(result)

        return result
    return wrapper
    

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True

    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

@ test_time
def prime_nums(num1, num2):
    count= 0
    for i in range(num1, num2):
        if is_prime(i):
            # print(i)
            count+=1
    return count
    

if __name__ == "__main__":
    prime_nums(2, 500)