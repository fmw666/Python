### list
[Python]()内置的一种数据类型是列表：[list]()。[list]()是一种有序的集合，可以随时添加和删除其中的元素。

比如，列出班里所有同学的名字，就可以用一个[list]()表示：
```python
>>> classmates = ['fmw', 'zhang', 'li']
>>> classmates
['fmw', 'zhang', 'li']
```
变量[classmates]()就是一个[list]()。用[len()]()函数可以获得[list]()元素的个数：
```python
>>> len(classmates)
3
```
用索引来访问list中每一个位置的元素，记得索引下标是从0开始的：
```python
>>> classmates[0]
'fmw'
>>> classmates[1]
'zhang'
>>> classmates[2]
'li'
>>> classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
当索引超出了范围时，[Python]()会报一个[IndexError]()错误，所以，要确保索引不要越界，记得最后一个元素的索引是[len(classmates) - 1]()。

如果要取最后一个元素，除了计算索引位置外，还可以用 [-1]() 做索引，直接获取最后一个元素：
```python
>>>classmates[-1]
'li'
```
以此类推，可以获取倒数第2个、倒数第3个：
```python
>>> classmates[-2]
'Bob'
>>> classmates[-3]
'Michael'
>>> classmates[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
同样注意不要越界！

[list]()是一个可变的有序表，所以，可以往[list]()中追加元素到末尾：
```python
>>> classmates.append('wang')
>>> classmates
['fmw', 'zhang', 'li', 'wang']
```
也可以把元素插入到指定的位置，比如索引号为 [1]() 的位置：
```python
>>> classmates.insert(1, 'song')
>>> classmates
['fmw', 'song', 'zhang', 'li', 'wang']
```
要删除[list]()末尾的元素，用[pop()]()方法：
```python
>>> classmates.pop()
'wang'
>>> classmates
['fmw', 'song', 'zhang', 'li']
```
要删除指定位置的元素，用[pop(i)]()方法，其中 [i]() 是索引位置：
```python
>>> classmates.pop(1)
'song'
>>> classmates
['fmw', 'zhang', 'li']
```
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
```python
>>> classmates[1] = 'chen'
>>> classmates
['fmw', 'chen', 'li']
```
[list]()里面的元素的数据类型也可以不同，比如：
```python
>>> L = ['Apple', 123, True]
```
[list]()元素也可以是另一个[list]()，比如：
```python
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s)
4
```
要注意 [s]() 只有4个元素，其中 [s[2]]() 又是一个[list]()，如果拆开写就更容易理解了：
```python
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
```
要拿到 ['php']() 可以写 [p[1]]() 或者 [s[2][1]]() ，因此 [s]() 可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

如果一个[list]()中一个元素也没有，就是一个空的[list]()，它的长度为0：
```python
>>> L = []
>>> len(L)
0
```
---
### tuple
另一种有序列表叫元组：[tuple]()。[tuple]()和[list]()非常类似，但是[tuple]()一旦初始化就不能修改，比如同样是列出同学的名字：
```python
>>> classmates = ('fmw', 'zhang', 'li')
```
现在，classmates这个[tuple]()不能变了，它也没有[append()]()，[insert()]()这样的方法。其他获取元素的方法和[list]()是一样的，你可以正常地使用[classmates[0]]()，[classmates[-1]]()，但不能赋值成另外的元素。

不可变的[tuple]()有什么意义？因为[tuple]()不可变，所以代码更安全。如果可能，能用[tuple]()代替[list]()就尽量用[tuple]()。

[tuple]()的陷阱：当你定义一个[tuple]()时，在定义的时候，[tuple]()的元素就必须被确定下来，比如：
```python
>>> t = (1, 2)
>>> t
(1, 2)
```
如果要定义一个空的[tuple]()，可以写成 [()]() ：
```python
>>> t = ()
>>> t
()
```
但是，要定义一个只有1个元素的[tuple]()，如果你这么定义：
```python
>>> t = (1)
>>> t
1
```
定义的不是[tuple]()，是1这个数！这是因为括号()既可以表示[tuple]()，又可以表示数学公式中的小括号，这就产生了歧义，因此，[Python]()规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的[tuple]()定义时必须加一个逗号 [,]() ，来消除歧义：
```python
>>> t = (1,)
>>> t
(1,)
```
