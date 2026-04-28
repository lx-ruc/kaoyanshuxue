#### （4）方阵的乘幂运算

<equation>\textcircled{4}</equation>零因子定律不成立，即由<equation>AB = O</equation>并不能得到<equation>A = O</equation>或<equation>B = O.</equation>


如果矩阵<equation>A</equation>为方阵，则定义<equation>A^{n} = \underbrace{A \cdot A \cdots A}_{n \text{个} A}</equation>为矩阵<equation>A</equation>的<equation>n</equation>次幂.规定<equation>A^{0} = E</equation>（单位矩阵）.

乘幂的运算性质：

<equation>\textcircled{1}</equation><equation>A^{k} \cdot A^{l} = A^{k+l}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}^{k}\right)^{l}=\mathbf{A}^{k l}.</equation>

注 一般情况下，<equation>(\mathbf{A}\cdot \mathbf{B})^{k}\neq A^{k}\cdot B^{k}.</equation>

(5) 矩阵的转置

设<equation>A_{m\times n} = \left[ \begin{array}{cccc} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{array} \right]_{m\times n}</equation>，定义A的转置

矩阵为

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {2 1} & \dots & a _ {m 1} \\ a _ {1 2} & a _ {2 2} & \dots & a _ {m 2} \\ \vdots & \vdots & & \vdots \\ a _ {1 n} & a _ {2 n} & \dots & a _ {m n} \end{array} \right] _ {n \times m},</equation>

即转置矩阵<equation>A^{\mathrm{T}}</equation>的第<equation>i</equation>行第<equation>j</equation>列元素等于原矩阵<equation>A</equation>的第<equation>j</equation>行第<equation>i</equation>列元素.

转置的运算规则：

---

<equation>\textcircled{1} (\mathbf{A}^{\mathrm{T}})^{\mathrm{T}} = \mathbf{A}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}+\mathbf{B}\right)^{\mathrm{T}}=\mathbf{A}^{\mathrm{T}}+\mathbf{B}^{\mathrm{T}};</equation>

<equation>\textcircled{3}</equation><equation>\mathbf{A B} )^{\mathrm{T}}=\mathbf{B}^{\mathrm{T}} \mathbf{A}^{\mathrm{T}};</equation>

<equation>\textcircled{4} ( k \mathbf{A} )^{\mathrm{T}}=k \cdot \mathbf{A}^{\mathrm{T}}.</equation>

(6) 方阵的行列式

若<equation>\mathbf{A} = (a_{i j})_{n\times n},\mathbf{B} = (b_{i j})_{n\times n}</equation>，则

<equation>| \mathbf {A} | = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right|,</equation>

且<equation>|kA| = k^{n}|A|, |AB| = |A||B|.</equation>

(7) 矩阵的求逆运算

<equation>\textcircled{1}</equation>逆矩阵的定义及定理

若<equation>A, B</equation>均为<equation>n</equation>阶方阵，且满足<equation>AB = BA = E</equation>，则称<equation>A</equation>是可逆矩阵，又称<equation>B</equation>是<equation>A</equation>的逆矩阵，记作<equation>B = A^{-1}</equation>.

(a)若矩阵<equation>A</equation>可逆，则<equation>A</equation>的逆矩阵<equation>A^{-1}</equation>是唯一的.

(b) 矩阵<equation>A</equation>可逆的充分必要条件是<equation>|A| \neq 0</equation>.

(c) 若<equation>|A| \neq 0</equation>，则<equation>A^{-1} = \frac{1}{|A|} A^{*}</equation>，其中

<equation>\boldsymbol {A} ^ {*} = \left[ \begin{array}{c c c c} A _ {1 1} & A _ {2 1} & \dots & A _ {n 1} \\ A _ {1 2} & A _ {2 2} & \dots & A _ {n 2} \\ \vdots & \vdots & & \vdots \\ A _ {1 n} & A _ {2 n} & \dots & A _ {m} \end{array} \right],</equation>

---


