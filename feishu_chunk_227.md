#### 2. 行列式的性质

n阶行列式

<equation>\begin{array}{l} D _ {n} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| \\ = \sum_ {\left(j _ {1} j _ {2} \dots j _ {n}\right)} (- 1) ^ {r \left(j _ {1} j _ {2} \dots j _ {n}\right)} a _ {1 j _ {1}} a _ {2 j _ {2}} \dots a _ {m _ {j}}, \\ \end{array}</equation>

式中<equation>\sum_{(j_1,j_2,\dots j_n)}</equation>表示对所有<equation>n</equation>级排列<equation>(j_{1}j_{2}\dots j_{n})</equation>求和.


<equation>\textcircled{1}</equation>行列互换，行列式的值不变，也即<equation>D = D^{\mathrm{T}}</equation>

<equation>\textcircled{2}</equation>任意两行(列)互换位置后，行列式改变符号.

推论1 如果行列式中有两行（列）的对应元素相同，则行列式的值为0.

<equation>\textcircled{3}</equation>将行列式的某一行(列)乘以一个常数<equation>k</equation>后，行列式的值变为原来的<equation>k</equation>倍.

---

推论2 如果行列式的某一行（列）全为0，则行列式的值等于0.

推论3 行列式的某两行（列）元素对应成比例，则行列式的值等于0.

<equation>\textcircled{4}</equation>如果行列式某一行（列）的所有元素都可以写成两个元素的和，则该行列式可以写成两个行列式的和，这两个行列式的这一行（列）分别为对应两个加数，其余行（列）与原行列式相等，即

<equation>\begin{array}{l} \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {i 1} + b _ {i 1} & a _ {i 2} + b _ {i 2} & \dots & a _ {i n} + b _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {i 1} & a _ {i 2} & \dots & a _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| + \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ b _ {i 1} & b _ {i 2} & \dots & b _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right|. \\ \end{array}</equation>

<equation>\textcircled{5}</equation>将行列式的某行（列）的 k倍加到另一行（列）上，行列式的值不变.

---


