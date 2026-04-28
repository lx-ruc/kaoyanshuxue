#### 2. 矩阵可对角化的有关定理

<equation>\textcircled{7}</equation><equation>\mathbf{A}^{\mathrm{T}}</equation>与 A有相同的特征值.

若<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>满足<equation>f(\mathbf{A}) = \mathbf{O}</equation>，则有<equation>f(\lambda) = 0.</equation>


对于<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>，若存在一个<equation>n</equation>阶可逆矩阵<equation>\mathbf{P}</equation>，使

<equation>P ^ {- 1} A P = \Lambda (\Lambda \text {为 对 角 矩 阵})</equation>

成立，则称<equation>A</equation>可相似对角化，简称<equation>A</equation>可对角化，否则就称<equation>A</equation>不可对角化.

若<equation>n</equation>阶矩阵<equation>A</equation>可以对角化，则对角矩阵<equation>A</equation>的<equation>n</equation>个主对角线元素必是<equation>A</equation>的<equation>n</equation>个特征值：<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>（包括重根），其相似变换矩阵<equation>P</equation>的<equation>n</equation>个列向量<equation>X_{1},X_{2},\dots</equation><equation>X_{n}</equation>是<equation>A</equation>的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>的特征向量，且<equation>X_{1},X_{2}</equation><equation>\dots ,X_{n}</equation>线性无关. 即有

<equation>P ^ {- 1} A P = A,</equation>

其中<equation>A = \left[ \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \ddots & \\ & & & \lambda_ {n} \end{array} \right], P = \left(X_{1}, X_{2}, \dots , X_{n}\right)</equation>为可逆

矩阵，且<equation>A X_{j}=\lambda_{j} X_{j} (j=1,2,\dots,n).</equation>


<equation>\textcircled{1}</equation><equation>n</equation>阶矩阵<equation>A</equation>可以对角化的充要条件是<equation>A</equation>有<equation>n</equation>个

---

线性无关的特征向量.

<equation>\textcircled{2}</equation>若<equation>n</equation>阶矩阵<equation>A</equation>有<equation>n</equation>个两两不等的特征值，则<equation>A</equation>必可对角化.

<equation>\textcircled{3}</equation>设<equation>\lambda_{i}</equation>是矩阵<equation>A</equation>的任一个特征值，其代数重数为<equation>n_{i}</equation>（即<equation>\lambda_{i}</equation>是<equation>n_{i}</equation>重特征值），其几何重数为<equation>m_{i}</equation>（即属于<equation>\lambda_{i}</equation>的线性无关的特征向量的最大个数，也是齐次线性方程组<equation>(\lambda_{i}E - A)X = 0</equation>的基础解系中的向量个数，<equation>m_{i} = n - r(\lambda_{i}E - A))</equation>，则恒有<equation>m_{i} \leqslant n_{i}</equation>.

<equation>\textcircled{4}</equation>设<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>的两两不等的特征值为<equation>\lambda_{1}, \lambda_{2}, \dots, \lambda_{s}(1 \leqslant s \leqslant n)</equation>，则矩阵<equation>\mathbf{A}</equation>可对角化的充要条件是对<equation>\mathbf{A}</equation>的每一个特征值<equation>\lambda_{i}</equation>，都有<equation>m_{i} = n_{i}(i = 1, 2, \dots, s)</equation>.

---


### 第六章 二次型


