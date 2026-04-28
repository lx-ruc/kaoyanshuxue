#### 向量组的线性相关性

**2024年第16题 | 填空题 | 5分**
16. 设向量<equation>\alpha_{1}=\left( \begin{array}{c} a \\ 1 \\ -1 \\ 1 \end{array} \right),\alpha_{2}=\left( \begin{array}{c} 1 \\ 1 \\ b \\ a \end{array} \right),\alpha_{3}=\left( \begin{array}{c} 1 \\ a \\ -1 \\ 1 \end{array} \right)</equation>若<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，且其中任意两个向量均线性无关，则

ab = ___
**答案: **```latex
-4
```

**解析:**解（法一）由于<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关，故该向量组的秩小于3，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\leqslant 2.</equation>又因为该向量组中任意两个向量均线性无关，所以该向量组的秩不小于2，从而<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})\geqslant 2.</equation>于是，<equation>r(\alpha_{1},\alpha_{2},\alpha_{3})=2.</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得，矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0.于是，<equation>\begin{aligned} \left| \begin{array}{l l l} a & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| \xlongequal {c _ {1} + c _ {2} + c _ {3}} \left| \begin{array}{l l l} a + 2 & 1 & 1 \\ a + 2 & 1 & a \\ a + 2 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 1 & 1 \\ 1 & 1 & a \\ 1 & a & 1  \right| &= (a + 2) \left| \begin{array}{l l l} 1 & 0 & 0 \\ 1 & 0 & a - 1 \\ 1 & a - 1 & 0  \right| \\ &= - (a + 2) (a - 1) ^ {2} = 0. \end{aligned}</equation>由此可得 a=-2或a=1. 但是当 a=1时，<equation>\alpha_{1}=\alpha_{3}</equation>，从而<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.于是，a=-2.

代入<equation>a = -2</equation>，再由矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>的任意一个3阶子式均为0可得<equation>\left| \begin{array}{c c c} 1 & 1 & - 2 \\ - 1 & b & - 1 \\ 1 & - 2 & 1 \end{array} \right| \frac {c _ {2} - c _ {1}}{c _ {3} + 2 c _ {1}} \left| \begin{array}{c c c} 1 & 0 & 0 \\ - 1 & b + 1 & - 3 \\ 1 & - 3 & 3 \end{array} \right| = 3 (b + 1) - 9 = 0.</equation>解得 b=2.

因此，<equation>a=-2,b=2,ab=-4.</equation>（法二）同法一可得<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2.</equation>对矩阵<equation>(\alpha_{1},\alpha_{2},\alpha_{3})</equation>作初等行变换.<equation>\begin{array}{l} \left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) = \left( \begin{array}{c c c} a & 1 & 1 \\ 1 & 1 & a \\ - 1 & b & - 1 \\ 1 & a & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 1 & a & 1 \\ - 1 & b & - 1 \\ a & 1 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 1 - a & 1 - a ^ {2} \end{array} \right) \\ \rightarrow \left( \begin{array}{c c c} 1 & 1 & a \\ 0 & a - 1 & 1 - a \\ 0 & b + 1 & a - 1 \\ 0 & 0 & 2 - a - a ^ {2} \end{array} \right). \\ \end{array}</equation>当<equation>a = -2</equation>或<equation>a = 1</equation>时，<equation>2 - a - a^{2} = -(a + 2)(a - 1) = 0.</equation>当 a =1时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right) \rightarrow \left(\begin{array}{c c c}1&1&1\\0&0&0\\0&b + 1&0\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&1\\0&b + 1&0\\0&0&0\\0&0&0\end{array}\right).</equation>由此可得<equation>\alpha_{1},\alpha_{3}</equation>线性相关，不符合题意.

当 a = -2时，<equation>\left(\alpha_ {1}, \alpha_ {2}, \alpha_ {3}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&- 3&3\\0&b + 1&- 3\\0&0&0\end{array}\right)\rightarrow \left(\begin{array}{c c c}1&1&- 2\\0&1&- 1\\0&b - 2&0\\0&0&0\end{array}\right).</equation>由<equation>r(\alpha_{1},\alpha_{2},\alpha_{3}) = 2</equation>可得<equation>b - 2 = 0</equation>，即<equation>b = 2</equation>因此，<equation>a=-2,b=2,ab=-4.</equation>

---

**2014年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>均为3维向量，则对任意常数 k,l，向量组<equation>\alpha_{1}+k\alpha_{3},\alpha_{2}+l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的（    )

A. 必要非充分条件 B. 充分非必要条件

C. 充分必要条件 D. 既非充分也非必要条件

答案: A

**解析:**假设<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关.考虑向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}.</equation>由于<equation>a\left(\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3}\right) + b\left(\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}\right) = a\boldsymbol{\alpha}_{1} + b\boldsymbol{\alpha}_{2} + (ak + bl)\boldsymbol{\alpha}_{3} = 0</equation>，故由<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关可知，<equation>a=b=ak+bl=0.</equation>因此，<equation>\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}</equation>线性无关.向量组<equation>\boldsymbol{\alpha}_{1} + k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2} + l\boldsymbol{\alpha}_{3}</equation>线性无关是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的必要条件.

但是向量组<equation>\boldsymbol{\alpha}_{1}+k\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{2}+l\boldsymbol{\alpha}_{3}</equation>线性无关不是向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\boldsymbol{\alpha}_{3}</equation>线性无关的充分条件.

下面我们给出反例.令<equation>\alpha_{1},\alpha_{2}</equation>线性无关，而<equation>\alpha_{3}=0</equation>，则此时<equation>\alpha_{1}+k\alpha_{3}=\alpha_{1},\alpha_{2}+l\alpha_{3}=\alpha_{2}</equation>线性无关.对任意非零常数k，有<equation>0\alpha_{1}+0\alpha_{2}+k\alpha_{3}=0</equation>，从而<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性相关.

因此，<equation>\alpha_{1} + k\alpha_{3},\alpha_{2} + l\alpha_{3}</equation>线性无关是向量组<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>线性无关的必要非充分条件.应选A.

---

**2012年第7题 | 选择题 | 4分 | 答案: C**

7. 设<equation>\alpha_{1}=\left( \begin{array}{c}0\\ 0\\ c_{1}\end{array} \right),\alpha_{2}=\left( \begin{array}{c}0\\ 1\\ c_{2}\end{array} \right),\alpha_{3}=\left( \begin{array}{c}1\\ -1\\ c_{3}\end{array} \right),\alpha_{4}=\left( \begin{array}{c}-1\\ 1\\ c_{4}\end{array} \right),</equation>其中<equation>c_{1},c_{2},c_{3},c_{4}</equation>为任意常数，则下列向量组线性相关

为（    ）

A.<equation>\alpha_{1},\alpha_{2},\alpha_{3}</equation>B.<equation>\alpha_{1},\alpha_{2},\alpha_{4}</equation>C.<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>D.<equation>\alpha_{2},\alpha_{3},\alpha_{4}</equation>

答案: C

**解析:**解（法一）由题设可得，<equation>\alpha_{3} + \alpha_{4} = \left( \begin{array}{c} 0 \\ 0 \\ c_{3} + c_{4} \end{array} \right),\alpha_{1} = \left( \begin{array}{c} 0 \\ 0 \\ c_{1} \end{array} \right).</equation>当<equation>c_{3} + c_{4}\neq 0</equation>时，<equation>\boldsymbol{\alpha}_{1} = \frac{c_{1}}{c_{3} + c_{4}} \left( \boldsymbol{\alpha}_{3} + \boldsymbol{\alpha}_{4} \right), \boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{3}, \boldsymbol{\alpha}_{4}</equation>线性相关；当<equation>c_{3} + c_{4} = 0</equation>时，<equation>\boldsymbol{\alpha}_{3} + \boldsymbol{\alpha}_{4} = 0</equation><equation>\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.从而<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{3},\boldsymbol{\alpha}_{4}</equation>线性相关.

综上所述，<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关，应选C.

（法二）由于<equation>n</equation>个<equation>n</equation>维列向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关等价于<equation>|\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>，而<equation>\left| \alpha_ {1}, \alpha_ {3}, \alpha_ {4} \right| = \left| \begin{array}{c c c} 0 & 1 & - 1 \\ 0 & - 1 & 1 \\ c _ {1} & c _ {3} & c _ {4} \end{array} \right| = c _ {1} \left| \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right| = 0,</equation>故<equation>\alpha_{1},\alpha_{3},\alpha_{4}</equation>线性相关.应选C.

同理可计算其他选项中的3个向量组成的矩阵的行列式，可知它们均不恒为零

---


