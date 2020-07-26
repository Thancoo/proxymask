# Python 对象中常用魔术方法

- `__call__`

对象通过提供 `__call__` 方法可以模拟函数的行为，如果一个对象提供了该方法，就可以像函数一样使用它。

```python
class Test:
    def __init__(self):
        self.a = 1

    def __call__(self, *args, **kwargs):
        res = str()
        for i in args:
            res += str(i)
        return f"the value is {res}"


if __name__ == '__main__':
    t = Test()
    print(t(100, 'string'))k
```
```text
the value is 100string
```

- `__len__`

`len()` 调用后会调用对象的 `__len__` 函数，我们可以为其定制输出。但是该函数要求我们返回的值必须为 int，否则会报错。

```python
class Test:
    def __init__(self):
        self.a = [1, 2, 3, 4, 5]

    def __len__(self):
        print('__len__')
        # TypeError: 'str' object cannot be interpreted as an integer
        # return str(len(self.a) + 100)
        return len(self.a) + 100


if __name__ == '__main__':
    b = Test()
    res = len(b)
    print(res)
```
```text
__len__
105
```




