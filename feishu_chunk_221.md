#### 二、可降阶的高阶微分方程

线性微分方程，求出此一阶微分方程的通解，然后将通解中的<equation>z</equation>用<equation>y^{1 - n}</equation>替换，即得原微分方程的通解.


如果存在可微函数 u（x，y），使得

<equation>\mathrm {d} u (x, y) = P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y,</equation>

则称一阶微分方程

<equation>P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y = 0</equation>

为全微分方程.


1. 形如<equation>y^{(n)}=f(x)</equation>的可降阶方程

这类微分方程只要积分<equation>n</equation>次就得到方程的通解.

2. 不显含函数 y的二阶可降阶的方程<equation>y^{\prime \prime}=f(x,y^{\prime})</equation>这类方程特点是不显含 y，若令<equation>y^{\prime}=p</equation>，则

<equation>y ^ {\prime \prime} = \frac {\mathrm {d} p}{\mathrm {d} x} = p ^ {\prime},</equation>

于是所给方程可降为一阶方程，再按一阶微分方程的方法求解.

3. 不显含自变量 x的二阶可降阶的方程<equation>y^{\prime \prime}=f(y,y^{\prime})</equation>这类方程特点是不显含 x，若令<equation>y^{\prime}=p</equation>，则

<equation>y ^ {\prime \prime} = \frac {\mathrm {d} p}{\mathrm {d} y} \cdot \frac {\mathrm {d} y}{\mathrm {d} x} = p \frac {\mathrm {d} p}{\mathrm {d} y}.</equation>

---


