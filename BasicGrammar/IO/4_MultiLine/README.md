读取和输出多行数据

### 题目描述

前面的题目都是读取和输出一行或者几行数据，现在考虑读取和输出很多行数据。

### 输入描述

输入包含多行，每行为一个整数。

### 输出描述

输出多行，每行为一个读取的整数。

### 测试样例

#### 样例1: 输入-输出

```
1
2
3
```

```
1
2
3
```

### 提示

上一道题中，我们读取了一行没有说明数量的数据，而这一题则是没有说明行数的多行数据。

#### Python3

对于 Python 来说，这次就没有以前那样简单了，你需要判断输入流是否结束：

```python
try:
    while True:
        inp = input()
        print(inp)
except EOFError:
    pass
```

另外需要说明的是，输入流和输出流是两个分开的流。你可以如上面的代码一样，读取数据的同时，即时输出结果，这在很多题目上是有用的。

#### C、C++ 和 Java

之前提到，这些语言将空格、Tab 和回车都视为“空白键”，所以读取的方式和判断结束的方式和上一题是一样的。