#### 1. 克拉默法则

<equation>\sum_ {j = 1} ^ {n} a _ {i j} x _ {j} = 0 \quad (i = 1, 2, \dots , m).</equation>


(1) 非齐次线性方程组

<equation>A X = b,</equation>

式中<equation>\mathbf{A}=(a_{ij})_{m\times n},\mathbf{X}=(x_{1},x_{2},\dots,x_{n})^{\mathrm{T}},\mathbf{b}=(b_{1},b_{2},\dots,</equation><equation>b_{m})^{\mathrm{T}}.</equation>

(2) 齐次线性方程组

<equation>A X = 0,</equation>

式中<equation>A, X</equation>同上，<equation>0 = (0,\dots ,0)^{\mathrm{T}}.</equation>


(1) 非齐次线性方程组

<equation>x _ {1} \boldsymbol {\alpha} _ {1} + x _ {2} \boldsymbol {\alpha} _ {2} + \dots + x _ {n} \boldsymbol {\alpha} _ {n} = \boldsymbol {b},</equation>

式中<equation>\boldsymbol{a}_{j} = (a_{1j}, a_{2j}, \dots , a_{mj})^{\mathrm{T}}</equation>（<equation>j=1,2,\dots,n )</equation>,<equation>\boldsymbol{b} = (b_{1},</equation><equation>b_{2},\dots,b_{m})^{\mathrm{T}}.</equation>


<equation>x _ {1} \boldsymbol {\alpha} _ {1} + x _ {2} \boldsymbol {\alpha} _ {2} + \dots + x _ {n} \boldsymbol {\alpha} _ {n} = 0,</equation>

式中<equation>\pmb{\alpha}_{j}</equation>同上，<equation>0 = (0,\dots ,0)^{\mathrm{T}}</equation>是一个<equation>m</equation>维的零向量.


<equation>\textcircled{1}</equation>若非齐次线性方程组

---

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = b _ {1}, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = b _ {2}, \\ \dots \\ a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {n n} x _ {n} = b _ {n} \end{array} \right.</equation>

的系数行列式<equation>D = |A| = \left| \begin{array}{c c c c} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n} \end{array} \right| \neq 0,</equation>

则方程组有唯一解：<equation>x_{j} = \frac{D_{j}}{D} = (j = 1,2,\dots ,n)</equation>，其中<equation>D_{j}</equation>是把<equation>D</equation>中第<equation>j</equation>列元素<equation>(a_{1j},a_{2j},\dots ,a_{m})^{\mathrm{T}}</equation>换成常数项<equation>(b_{1},</equation><equation>b_{2},\dots ,b_{n})^{\mathrm{T}}</equation>而得到的新行列式.

<equation>\textcircled{2}</equation>若已知齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = 0, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = 0, \\ \dots \\ a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {m} x _ {n} = 0 \end{array} \right.</equation>

的系数行列式<equation>D = |A| = \left| \begin{array}{c c c c} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{array} \right| \neq 0,</equation>

则该齐次线性方程组只有零解：<equation>x_{j} = 0(j = 1,2,\dots,n).</equation>

---


