#### (2)坐标变换

此式称为由基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的基变换公式，称矩阵

<equation>A = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right]</equation>

为由旧基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到新基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的过渡矩阵.

过渡矩阵必是可逆矩阵，上面的基变换公式用矩阵及向量符号可表示为

<equation>\left(\eta_ {1}, \eta_ {2}, \dots , \eta_ {n}\right) = \left(\varepsilon_ {1}, \varepsilon_ {2}, \dots , \varepsilon_ {n}\right) A,</equation>

其中过渡矩阵<equation>A</equation>的第<equation>j</equation>列是<equation>\eta_{j}</equation>在基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>下的坐标列向量.


设<equation>\alpha</equation>是<equation>\mathbf{R}^n</equation>中的任一个向量，<equation>\alpha</equation>在基<equation>\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n</equation>下的坐标为<equation>X = (x_{1}, x_{2}, \dots, x_{n})^{\mathrm{T}}</equation>，在基<equation>\eta_1, \eta_2, \dots, \eta_n</equation>下的坐标为<equation>Y = (y_{1}, y_{2}, \dots, y_{n})^{\mathrm{T}}</equation>，则有

<equation>X = A Y \text {或} Y = A ^ {- 1} X.</equation>

此式即为坐标变换公式，式中的<equation>A</equation>即为基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的过渡矩阵.

---

(3) 两组标准正交基之间的过渡矩阵是正交矩阵

设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>是<equation>V^{n}</equation>中的一组基，且<equation>(\varepsilon_{i},\varepsilon_{i}) = 1</equation><equation>(\varepsilon_{i},\varepsilon_{j}) = 0(i,j = 1,2,\dots ,n;i\neq j)</equation>，则称<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>为<equation>V^{n}</equation>中的一组标准正交基（或规范正交基）。

设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>及<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>都是<equation>\mathbf{R}^n</equation>的标准正交基，且有<equation>(\eta_{1},\eta_{2},\dots ,\eta_{n}) = (\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n})A</equation>，则<equation>A</equation>必是一个正交矩阵.

---


### 第四章 线性方程组


