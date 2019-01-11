### 循环
[Python]()的循环有两种，一种是 [for...in]() 循环，依次把[list]()或[tuple]()中的每个元素迭代出来，看例子：
```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```
再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
```python
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
```
[Python]()提供一个 [range()]() 函数，可以生成一个整数序列，[range(101)]() 就可以生成0-100的整数序列，计算如下：
```python
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
```
第二种循环是 [while]() 循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用 [while]() 循环实现：
```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```
---
### break
在循环中， [break]() 语句可以提前退出循环。
```pyhon
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```
---
### continue
在循环过程中，也可以通过 [continue]() 语句，跳过当前的这次循环，直接开始下一次循环。
```python
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```

