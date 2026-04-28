#### 2. 周期为 21 的傅里叶级数

<equation>\textcircled{1}</equation>只有有限个第一类间断点；

<equation>\textcircled{2}</equation>只有有限个极值点.

则<equation>f ( x )</equation>的以<equation>2 \pi</equation>为周期的傅里叶级数<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} \left(a_{n}\cos nx+b_{n}\sin nx\right)</equation>，其收敛域为<equation>(-\infty , +\infty)</equation>，和函数<equation>S ( x )</equation>是以<equation>2 \pi</equation>为周期的周期函数，且在其一个周期上的表达式为

<equation>S (x) = \left\{ \begin{array}{l l} \frac {f (x - 0) + f (x + 0)}{2}, & x \in (- \pi , \pi), \\ \frac {f (- \pi + 0) + f (\pi - 0)}{2}, & x = \pm \pi . \end{array} \right.</equation>


设函数<equation>f(x)</equation>是周期为<equation>2l</equation>的周期函数，且在区间<equation>[-l, l]</equation>上可积，则称

<equation>a _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots)</equation>

为<equation>f(x)</equation>的傅里叶系数，称三角级数

<equation>\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{l} + b _ {n} \sin \frac {n \pi x}{l}\right)</equation>

为<equation>f(x)</equation>以2l为周期的傅里叶级数.

---

3. 只在<equation>[0, l]</equation>上有定义的函数的傅里叶级数展开

(1) 对称区间上奇、偶函数的傅里叶级数

<equation>\textcircled{1}</equation>若<equation>f(x)</equation>是以<equation>2l</equation>为周期的可积偶函数，则其以<equation>2l</equation>为周期的傅里叶级数为

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l},</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots).</equation>

<equation>\textcircled{2}</equation>若<equation>f(x)</equation>为以<equation>2l</equation>为周期的可积奇函数，则其以<equation>2l</equation>为周期的傅里叶级数为

<equation>f (x) \sim \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l},</equation>

其中

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {1} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

(2) 在<equation>[0, l]</equation>上有定义的函数的傅里叶级数展开

定义在[0，l]上的函数可以有多种方式展开成三角级数，但常用的方式只有三种，即周期奇延拓、周期偶延拓、周期延拓，三种延拓得到的三角级数展开式分别为：

<equation>\textcircled{1}</equation>正弦级数展开：

<equation>f (x) \sim \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l},</equation>

---

其中

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

<equation>\textcircled{2}</equation>余弦级数展开：

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l},</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots).</equation>

<equation>\textcircled{3}</equation>三角级数展开：

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {2 n \pi x}{l} + b _ {n} \sin \frac {2 n \pi x}{l}\right),</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {2 n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {2 n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

---


### 第八章 常微分方程及差分方程


