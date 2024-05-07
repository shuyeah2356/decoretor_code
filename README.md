# decoretor_code

## 1、装饰器
python装饰器是一个用于拓展原来函数功能的函数。<br>装饰器可增加代码的可读性和复用性<br>装饰器的返回值也是一个函数，在不改变原函数名称的情况下新增函数的功能。<br>
一个函数添加了@符号，该函数就成了被装饰的结果，将原来的函数作为装饰器的参数<br>
装饰器将整个函数作为参数，装饰器在黑匣子内部增加代码<br>
将公有代码写入装饰器，自己的函数在装饰器中作为参数传入的一小部分

例如实现一个功能，打印出[2,10000)之间的所有质数，并打印出运行时间

```python
import time

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


def prime_nums():
    time_1 = time.time()
    for i in range(2, 10000):
        if is_prime(i):
            print(i)
    time_2 = time.time()
    print(time_2-time_1)

if __name__ == "__main__":
    prime_nums()
 
```

定义了两个函数：is_prime打印质数、prime_nums计算时间。
如果一个类中的多个函数都需要打印时间，就需要将每一个函数中都添加
```python
time_1 = time.time()
func()# 函数完成的功能
time_2 = time.time()
print(time_2-time_1)
```

可以使用装饰器实现相同功能，将实现的功能代码写进装饰器中，计算时间的函数来调用装饰器函数。
```python
import time

# 计时器装饰器
def test_time(func):
    def wrapper():
        time_1 = time.time()
        func()
        time_2 = time.time()
        print(time_2-time_1)
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
def prime_nums():
    
    for i in range(2, 10000):
        if is_prime(i):
            print(i)
    

if __name__ == "__main__":
    prime_nums()
```

如果实现原始功能的函数带有返回值，功能变为计算[2,10000）之间质数的个数
```python
import time

# 计时器装饰器
def test_time(func):
    def wrapper():
        time_1 = time.time()
        # 增加装饰器的函数增加了一个返回值
        result = func()
        time_2 = time.time()
        print(time_2-time_1)
        # wrapper函数也添加返回值
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
def prime_nums():
    count= 0
    for i in range(2, 10000):
        if is_prime(i):
            # print(i)
            count+=1☟
    return count
    

if __name__ == "__main__":
    result = prime_nums()
    print(result)
```
如果原始功能函数带有参数，功能变为计算自定义区间之间质数的个数。
```python
import time

# 计时器装饰器
def test_time(func):
    # 原始功能的函数有两个参数，wrapper函数也需要增加两个参数
    def wrapper(*args, **kwargs):
        time_1 = time.time()
        # func也有两个参数
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
```
