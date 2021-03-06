读取和输出一个数组

### 题目描述

在上一题中，我们读取和输出了一行中的几个数据，数量少，单独对每一个数据进行读取和输出是方便的，但是如果数量变多了呢，如果没有说明数量呢？

### 输入描述

> 默认 “数组” 和 “列表” 表示的是一个意思，都是指一组数据。

第一行是一个正整数 N (0 < N < 30)，表示数组的长度

第二行是数组 A，有 N 个浮点数，两两间有一个空格隔开

第三行是数组 B，有 M 个整数，M 未知但小于 30，两两间有一个空格隔开

### 输出描述

输出分为两行。第一行是数组 A，两两间用一个空格隔开，保留两位小数，第二行是数组 B 每一个数乘上2的结果，两两间用一个空格隔开。

### 测试样例

#### 样例1: 输入-输出

```
5
3.605 7.4189 1.5 3.14159 4.0
35 92 51 65 8 42 88
```

```
3.60 7.42 1.50 3.14 4.00
70 184 102 130 16 84 176
```

### 提示

#### Python3

上一题中，我们对每一个数据分别处理，在这道题中显然是不合适的，我们应该考虑批量读取和输出一组数据，所以。。。用循环？不，Python 提供了更方便的方式：`列表生成式` 和 `map()`。

比如可以使用 `列表生成式` 将一组输入转为浮点数列表：

```python
a = [float(i) for i in input().split()]
```

或者使用 `map()` ：

```python
a = map(float, input().split())
```

需要注意的是，在 Python3 中，`map()` 返回的是一个可迭代但不可随机访问的 map 对象，如果想要随机访问，你可以将 map 转为一个列表： `list(map())`。

本题的另一个难点是如何实现输出一行两两用空格隔开的数组。主要有两种方式，一是先将数组格式化为字符串：

```python
print(' '.join(map('{:.2f}'.format, a)))
```

第二种方式是利用 `print()` 本身的特性，它可以接受多个参数，然后两两间用一个空格隔开输出。所以你可以将一个**可迭代对象**使用 `*` 分解为 `print()` 的一个个参数：

```python
print(*map('{:.2f}'.format, a))
```

#### C

读取数组 A，我们只需要根据输入的数组大小 n，循环读取即可：

```c
for (int i = 0; i < n; i++)
    scanf("%lf", &a[i]);
```

输出的时候，我们则需要**考虑到最后一个数据后没有空格，而是换行**：

```c
for (int i = 0; i < n; i++)
    printf("%.2lf%s", a[i], i < n-1 ? " " : "\n");
```

而对于数组 B，因为长度未知，所以我们需要循环读取判断是否到达行尾，输出则一样：

```c++
while(scanf("%d", &b[n]) != EOF)
    ++n;
```

#### C++

A 数组的输入和 C 类似，受限于篇幅，这里就不贴代码了。B 数组的读取方式则和 C 类似：

```c++
while (cin >> b[n])
    ++n;
```

#### Java

Java 有很多读取和输出数组的用法，这里只写 B 数组基本的读取方式：

```java
while (scanner.hasNext())
    b[n++] = scanner.nextInt();
```
