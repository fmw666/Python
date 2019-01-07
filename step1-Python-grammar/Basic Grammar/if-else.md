### 条件判断
用 [if]() 语句来实现条件判断：
```python
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')
```
根据[Python]()的缩进规则，如果 [if]() 语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

也可以给 [if]() 添加一个 [else]() 语句，意思是，如果 [if]() 判断是False，不要执行 [if]() 的内容，去把 [else]() 执行了：
```python
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
```
注意不要少写了冒号 [:]() 。

当然上面的判断是很粗略的，完全可以用[elif]()做更细致的判断：
```python
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```
[if]() 语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的 [elif]() 和 [else]() ，所以下面的程序打印的是teenager：
```python
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```


