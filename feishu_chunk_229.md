#### 三、几种特殊的行列式

<equation>= \sum_ {i = 1} ^ {n} a _ {i j} A _ {i j} \quad (j = 1, 2, \dots , n) (\mathrm {按 第} j \mathrm {列 展 开}).</equation>

推论：行列式<equation>D</equation>的某一行（列）各元素与另一行（列）对应元素的代数余子式的乘积之和为零，即

<equation>\begin{array}{l} \sum_ {j = 1} ^ {n} a _ {i j} A _ {k j} = a _ {i 1} A _ {k 1} + a _ {i 2} A _ {k 2} + \dots + a _ {i n} A _ {k n} = 0, \quad (i \neq k) \\ \sum_ {j = 1} ^ {n} a _ {i j} A _ {j k} = a _ {1 i} A _ {1 k} + a _ {2 i} A _ {2 k} + \dots + a _ {n i} A _ {n k} = 0. \quad (i \neq k) \\ \end{array}</equation>


1. 上三角形、下三角形、对角形行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c} a _ {1 1} & 0 & \dots & 0 \\ 0 & a _ {2 2} & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & a _ {m} \end{array} \right| = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ 0 & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & a _ {m} \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & 0 & \dots & 0 \\ a _ {2 1} & a _ {2 2} & \dots & 0 \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| \\ = a _ {1 1} a _ {2 2} \dots a _ {m}. \\ \end{array}</equation>

---

2. 次对角线行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c} 0 & \dots & 0 & a _ {1 n} \\ 0 & \dots & a _ {2 (n - 1)} & 0 \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & 0 & 0 \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & \dots & a _ {1 (n - 1)} & a _ {1 n} \\ a _ {2 1} & \dots & a _ {2 (n - 1)} & 0 \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & 0 & 0 \end{array} \right| \\ = \left| \begin{array}{c c c c} 0 & \dots & 0 & a _ {1 n} \\ 0 & \dots & a _ {2 (n - 1)} & a _ {2 n} \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & a _ {n (n - 1)} & a _ {n n} \end{array} \right| \\ = (- 1) ^ {\frac {n (n - 1)}{2}} a _ {1 n} \dots a _ {n 1}. \\ \end{array}</equation>

3. 范德蒙德行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c c} 1 & 1 & 1 & \dots & 1 \\ a _ {1} & a _ {2} & a _ {3} & \dots & a _ {n} \\ a _ {1} ^ {2} & a _ {2} ^ {2} & a _ {3} ^ {2} & \dots & a _ {n} ^ {2} \\ \vdots & \vdots & \vdots & & \vdots \\ a _ {1} ^ {n - 1} & a _ {2} ^ {n - 1} & a _ {3} ^ {n - 1} & \dots & a _ {n} ^ {n - 1} \end{array} \right| \\ = \prod_ {1 \leq i < j \leq n} \left(a _ {j} - a _ {i}\right). \\ \end{array}</equation>

---


