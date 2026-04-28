# 数学二

## 高等数学

### 多元函数微积分学

#### 多元函数的极值问题

**2025年第19题 | 解答题 | 12分**
19. (本题满分12分)

设函数 f(x,y)可微且满足：<equation>\mathrm {d} f (x, y) = - 2 x \mathrm {e} ^ {- y} \mathrm {d} x + \mathrm {e} ^ {- y} \left(x ^ {2} - y - 1\right) \mathrm {d} y, f (0, 0) = 2</equation>求 f(x,y)，并求 f(x,y)的极值.
**答案: **f（x,y）=-x²e^{-y}+（y+2）e^{-y}； f（0,-1）为极大值
**解析: **解 由<equation>\mathrm{d}f(x,y) = -2x\mathrm{e}^{-y}\mathrm{d}x + \mathrm{e}^{-y}(x^2 - y - 1)\mathrm{d}y</equation>可得<equation>\frac{\partial f}{\partial x} = -2x\mathrm{e}^{-y},\frac{\partial f}{\partial y} = \mathrm{e}^{-y}(x^2 - y - 1)</equation>.于是，<equation>f (x, y) = \int \frac {\partial f}{\partial x} \mathrm {d} x = \int (- 2 x) \mathrm {e} ^ {- y} \mathrm {d} x = - x ^ {2} \mathrm {e} ^ {- y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于y的一元函数.

对<equation>f(x,y)</equation>关于<equation>y</equation>求偏导数可得<equation>\frac{\partial f}{\partial y} = x^{2}\mathrm{e}^{-y} + \varphi^{\prime}(y)</equation>. 与<equation>\frac{\partial f}{\partial y} = \mathrm{e}^{-y}(x^{2} - y - 1)</equation>比较可得<equation>\varphi^{\prime}(y) = -\mathrm{e}^{-y}(y + 1)</equation>. 进一步可得<equation>\begin{aligned} \varphi (y) &= \int \varphi^ {\prime} (y) \mathrm {d} y = \int \left[ - \mathrm {e} ^ {- y} (y + 1) \right] \mathrm {d} y = \int (y + 1) \mathrm {d} \left(\mathrm {e} ^ {- y}\right) = (y + 1) \mathrm {e} ^ {- y} - \int \mathrm {e} ^ {- y} \mathrm {d} y \\ &= (y + 1) \mathrm {e} ^ {- y} + \mathrm {e} ^ {- y} + C = (y + 2) \mathrm {e} ^ {- y} + C, \end{aligned}</equation>其中 C为待定常数.

将<equation>\varphi(y)</equation>的表达式代入<equation>f(x,y)</equation>可得<equation>f (x, y) = - x ^ {2} \mathrm {e} ^ {- y} + (y + 2) \mathrm {e} ^ {- y} + C = \left(- x ^ {2} + y + 2\right) \mathrm {e} ^ {- y} + C.</equation>代入<equation>f ( 0, 0 )=2</equation>可得<equation>2=2+C</equation>，解得<equation>C=0</equation>因此，<equation>f ( x,y )=\left(-x^{2}+y+2\right) \mathrm{e}^{-y}.</equation>下面计算 f（x,y）的极值.

计算 f（x,y）的驻点.

解<equation>\left\{ \begin{array}{l l} \frac{\partial f}{\partial x} = 0, \\ \frac{\partial f}{\partial y} = 0, \end{array} \right.</equation>即<equation>\left\{ \begin{array}{l l} - 2x\mathrm{e}^{-y} = 0, \\ \mathrm{e}^{-y}(x^2 - y - 1) = 0. \end{array} \right.</equation>由<equation>-2x\mathrm{e}^{-y} = 0</equation>可得<equation>x = 0</equation>. 将<equation>x = 0</equation>代入<equation>\mathrm{e}^{-y}(x^2 - y - 1)</equation>= 0 可得<equation>y = -1</equation>. 于是，点<equation>(0, -1)</equation>为<equation>f(x,y)</equation>的唯一驻点.

计算 f(x,y)的二阶偏导数.<equation>\frac {\partial^ {2} f}{\partial x ^ {2}} = - 2 \mathrm {e} ^ {- y}, \quad \frac {\partial^ {2} f}{\partial x \partial y} = 2 x \mathrm {e} ^ {- y}, \quad \frac {\partial^ {2} f}{\partial y ^ {2}} = - \left(x ^ {2} - y\right) \mathrm {e} ^ {- y}.</equation>对点（0，-1），<equation>A = \left. \frac {\partial^ {2} f}{\partial x ^ {2}} \right| _ {(0, - 1)} = - 2 \mathrm {e}, \quad B = \left. \frac {\partial^ {2} f}{\partial x \partial y} \right| _ {(0, - 1)} = 0, \quad C = \left. \frac {\partial^ {2} f}{\partial y ^ {2}} \right| _ {(0, - 1)} = - \mathrm {e}.</equation>由于<equation>AC - B^{2} > 0</equation>，且<equation>A < 0</equation>，故点（0，-1）为<equation>f(x,y)</equation>的极大值点，极大值为<equation>f(0, - 1) = \mathrm{e}</equation>.

---

**2024年第12题 | 填空题 | 5分**
12. 函数<equation>f(x,y)=2x^{3}-9x^{2}-6y^{4}+12x+24y</equation>的极值点是 ___
**答案: **## (1,1)
**解析: **解 计算 f(x,y) 的驻点.

整理<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=6x^{2}-18x+12=0,\\ f_{y}^{\prime}(x,y)=-24y^{3}+24=0\end{array}\right.</equation>可得<equation>\left\{\begin{array}{l l}x^{2}-3x+2=0,\\ y^{3}-1=0,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=1,\\ y=1,\end{array}\right.</equation>或<equation>\left\{\begin{array}{l l}x=2,\\ y=1,\end{array}\right.</equation>即<equation>f(x,y)</equation>的全部驻点为点（1，1），（2，1）.

计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 1 2 x - 1 8, f _ {x y} ^ {\prime \prime} (x, y) = 0, f _ {y y} ^ {\prime \prime} (x, y) = - 7 2 y ^ {2}.</equation>对点（1,1），<equation>A=f_{xx}^{\prime \prime}(1,1)=-6,B=f_{xy}^{\prime \prime}(1,1)=0,C=f_{yy}^{\prime \prime}(1,1)=-72,AC-B^{2}=(-6)\times</equation>（-72）-0>0，且<equation>A<0</equation>，故由二元函数极值存在的充分条件可知，点（1,1）是<equation>f(x,y)</equation>的极大值点.

对点（2,1），<equation>A=f_{xx}^{\prime \prime}(2,1)=6,B=f_{xy}^{\prime \prime}(2,1)=0,C=f_{yy}^{\prime \prime}(2,1)=-72,AC-B^{2}=6\times(-72)</equation><equation>- 0 < 0</equation>，故由二元函数极值存在的充分条件可知，点（2,1）不是<equation>f(x,y)</equation>的极值点.

因此，<equation>f(x,y)</equation>的唯一极值点为（1,1）.

---

**2023年第18题 | 解答题 | 12分**
18. (本题满分12分)

求函数<equation>f ( x,y)=x \mathrm{e}^{\cos y}+\frac{x^{2}}{2}</equation>的极值.
**答案: **f(x,y)有极小值，极小值为<equation>f(-\mathrm{e},2 k \pi)=-\frac{\mathrm{e}^{2}}{2}</equation>，其中 k<equation>\in\mathbf{Z}.</equation>
**解析: **解<equation>\textcircled{1}</equation>计算 f(x,y）的驻点.<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {\cos y} + x, \quad f _ {y} ^ {\prime} (x, y) = - x \sin y \mathrm {e} ^ {\cos y}.</equation>令<equation>\left\{\begin{array}{l l} {\mathrm{e}^{\cos y}+x=0,} \\ {-x\sin y\mathrm{e}^{\cos y}=0.} \end{array} \right.</equation>由<equation>\mathrm{e}^{\cos y}>0</equation>以及<equation>- x\sin y\mathrm{e}^{\cos y}=0</equation>可得 x=0或<equation>\sin y=0.</equation>但当 x=0时，<equation>\mathrm{e}^{\cos y}+x=0</equation>，且 A > 0. 不成立，于是<equation>\sin y=0</equation>，从而 y = k<equation>\pi</equation>，其中 k<equation>\in\mathbf{Z}.</equation>当 y = 2k<equation>\pi</equation>时，<equation>\mathrm{e}^{\cos y}=\mathrm{e},x=-\mathrm{e}</equation>；当 y = （2k+1）<equation>\pi</equation>时，<equation>\mathrm{e}^{\cos y}=\mathrm{e}^{-1},x=-\mathrm{e}^{-1}</equation>由此可得 f(x,y)的全部驻点为（-e，2k<equation>\pi</equation>），（<equation>-\mathrm{e}^{-1},(2k+1)\pi</equation>），其中 k<equation>\in</equation>Z.<equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 1,</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = - \sin y \mathrm {e} ^ {\cos y},</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = - x \cos y \mathrm {e} ^ {\cos y} - x \sin y \cdot (- \sin y) \mathrm {e} ^ {\cos y} = x \left(\sin^ {2} y - \cos y\right) \mathrm {e} ^ {\cos y}.</equation><equation>\textcircled{3}</equation>计算<equation>AC-B^{2}.</equation>（i）对点<equation>(-\mathrm{e},2k\pi),A=f_{xx}^{\prime \prime}(-\mathrm{e},2k\pi)=1,B=f_{xy}^{\prime \prime}(-\mathrm{e},2k\pi)=0,C=f_{yy}^{\prime \prime}(-\mathrm{e},2k\pi)=\mathrm{e}^{2},</equation><equation>AC-B^{2}=\mathrm{e}^{2}>0</equation>，且 A > 0.由二元函数极值存在的充分条件可知，点<equation>(-\mathrm{e},2k\pi),k\in \mathbf{Z}</equation>是 f(x,y)的极小值点.极小值为<equation>f(-\mathrm{e},2k\pi)=-\frac{\mathrm{e}^{2}}{2}.</equation>（ii）对点<equation>(-\mathrm{e}^{-1},(2 k+1)\pi), A=f_{x x}^{\prime \prime}(-\mathrm{e}^{-1},(2 k+1)\pi)=1, B=f_{x y}^{\prime \prime}(-\mathrm{e}^{-1},(2 k+1)\pi)= 0, C=f_{y y}^{\prime \prime}(-\mathrm{e}^{-1},(2 k+1)\pi)=-\mathrm{e}^{-2}, A C-B^{2}=-\mathrm{e}^{-2}<0.</equation>由二元函数极值存在的充分条件可知，点<equation>(-\mathrm{e}^{-1},(2 k+1)\pi), k\in \mathbf{Z}</equation>不是 f(x,y）的极值点.

综上所述，<equation>f ( x,y )</equation>有极小值，极小值为<equation>f(-\mathrm{e},2 k \pi)=-\frac{\mathrm{e}^{2}}{2}.</equation>

---

**2022年第20题 | 解答题 | 12分**
20. (本题满分12分)

已知可微函数 f(u,v)满足<equation>\frac{\partial f(u,v)}{\partial u}-\frac{\partial f(u,v)}{\partial v}=2(u-v)\mathrm{e}^{-(u+v)},</equation>且<equation>f(u,0)=u^{2}\mathrm{e}^{-u}.</equation>I. 记<equation>g(x,y)=f(x,y-x),</equation>求<equation>\frac{\partial g(x,y)}{\partial x};</equation>II. 求 f(u,v)的表达式与极值.
**答案: **（ I ）<equation>( 4 x-2 y ) \mathrm{e}^{-y}；</equation>（Ⅱ）<equation>f ( u,v )</equation>的表达式为<equation>\left(u^{2}+v^{2}\right)\mathrm{e}^{-(u+v)}</equation>，该函数有极小值，极小值为<equation>f ( 0,0 )=0.</equation>
**解析: **（ I ）根据链式法则，<equation>\frac {\partial g (x , y)}{\partial x} = \frac {\partial f (x , y - x)}{\partial x} = f _ {1} ^ {\prime} (x, y - x) - f _ {2} ^ {\prime} (x, y - x).</equation>令<equation>u=x,v=y-x</equation>，并代入<equation>\frac{\partial f(u,v)}{\partial u}-\frac{\partial f(u,v)}{\partial v}=2(u-v)\mathrm{e}^{-(u+v)}</equation>可得<equation>f _ {1} ^ {\prime} (x, y - x) - f _ {2} ^ {\prime} (x, y - x) = 2 (2 x - y) \mathrm {e} ^ {- y}.</equation>因此，<equation>\frac{\partial g(x,y)}{\partial x} = (4x - 2y)\mathrm{e}^{-y}.</equation>（Ⅱ）通过积分先计算<equation>g ( x,y )</equation>即<equation>f ( x,y-x )</equation>的表达式.<equation>\begin{aligned} f (x, y - x) &= g (x, y) = \int \frac {\partial g (x , y)}{\partial x} \mathrm {d} x = \int (4 x - 2 y) \mathrm {e} ^ {- y} \mathrm {d} x = \left(2 x ^ {2} - 2 x y\right) \mathrm {e} ^ {- y} + \varphi (y) \\ &= 2 x (x - y) \mathrm {e} ^ {- y} + \varphi (y), \end{aligned}</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

令 u=x,v=y-x可得<equation>f (u, v) = - 2 u v \mathrm {e} ^ {- (u + v)} + \varphi (u + v).</equation>代入<equation>f ( u, 0 ) = u^{2} \mathrm{e}^{-u}</equation>可得<equation>\varphi ( u )=u^{2}\mathrm{e}^{-u}.</equation>于是，<equation>f (u, v) = - 2 u v \mathrm {e} ^ {- (u + v)} + \varphi (u + v) = - 2 u v \mathrm {e} ^ {- (u + v)} + (u + v) ^ {2} \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2}\right) \mathrm {e} ^ {- (u + v)}.</equation>计算 f（u,v）的驻点.<equation>f _ {1} ^ {\prime} (u, v) = 2 u \mathrm {e} ^ {- (u + v)} - \left(u ^ {2} + v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(2 u - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)},</equation><equation>f _ {2} ^ {\prime} (u, v) = 2 v \mathrm {e} ^ {- (u + v)} - \left(u ^ {2} + v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(2 v - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)}.</equation>解<equation>\left\{\begin{array}{l l}2 u-u^{2}-v^{2}=0,\\ 2 v-u^{2}-v^{2}=0.\end{array} \right.</equation>两式相减得 u=v，将 u=v 代入 2u-u²-v²=0 可得 2u-2u²=0，从而 u=0或 u=1.<equation>\left\{\begin{array}{l l}u=0,\\ v=0\end{array} \right.</equation>和<equation>\left\{\begin{array}{l l}u=1,\\ v=1\end{array} \right.</equation>为该方程组的两组解.

因此，点（0，0）和点（1，1）为 f（u,v）的全部驻点.

计算 f（u,v）的二阶偏导数.<equation>f _ {1 1} ^ {\prime \prime} (u, v) = (2 - 2 u) \mathrm {e} ^ {- (u + v)} - \left(2 u - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2} - 4 u + 2\right) \mathrm {e} ^ {- (u + v)},</equation><equation>f _ {1 2} ^ {\prime \prime} (u, v) = - 2 v \mathrm {e} ^ {- (u + v)} - \left(2 u - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2} - 2 u - 2 v\right) \mathrm {e} ^ {- (u + v)},</equation><equation>f _ {2 2} ^ {\prime \prime} (u, v) = (2 - 2 v) \mathrm {e} ^ {- (u + v)} - \left(2 v - u ^ {2} - v ^ {2}\right) \mathrm {e} ^ {- (u + v)} = \left(u ^ {2} + v ^ {2} - 4 v + 2\right) \mathrm {e} ^ {- (u + v)}.</equation>对点（0，0），<equation>A = f _ {1 1} ^ {\prime \prime} (0, 0) = 2, \quad B = f _ {1 2} ^ {\prime \prime} (0, 0) = 0, \quad C = f _ {2 2} ^ {\prime \prime} (0, 0) = 2.</equation>由于<equation>AC-B^{2}>0</equation>，且<equation>A>0</equation>，故点（0,0）为<equation>f(u,v)</equation>的极小值点，极小值为<equation>f(0,0)=0.</equation>对点（1，1），<equation>A = f _ {1 1} ^ {\prime \prime} (1, 1) = 0, \quad B = f _ {1 2} ^ {\prime \prime} (1, 1) = - 2 \mathrm {e} ^ {- 2}, \quad C = f _ {2 2} ^ {\prime \prime} (1, 1) = 0.</equation>由于<equation>AC-B^{2}<0</equation>，故点（1，1）不是极值点.

综上所述，<equation>f ( u,v )</equation>有极小值，极小值为<equation>f ( 0,0 )=0.</equation>

---

**2020年第17题 | 解答题 | 10分**
17. (本题满分10分)

求函数<equation>f ( x,y)=x^{3}+8 y^{3}- x y</equation>的极值.
**答案: **<equation>\text {极 小 值} f \left(\frac {1}{6}, \frac {1}{1 2}\right) = - \frac {1}{2 1 6}.</equation>
**解析: **解<equation>\textcircled{1}</equation>计算 f(x,y）的驻点.

解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x4=x，解得x=0或x<equation>= \frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l}x = 0,\\ y = 0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l}x = \frac{1}{6},\\ y = \frac{1}{12}. \end{array} \right.</equation>f(x,y)有两个驻点（0，0），<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 6 x, \quad f _ {x y} ^ {\prime \prime} (x, y) = - 1, \quad f _ {y y} ^ {\prime \prime} (x, y) = 4 8 y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

- 考虑驻点（0,0）.<equation>A = f _ {x x} ^ {\prime \prime} (0, 0) = 0, \quad B = f _ {x y} ^ {\prime \prime} (0, 0) = - 1, \quad C = f _ {y y} ^ {\prime \prime} (0, 0) = 0.</equation>AC-B²=0-1=-1<0，故点（0,0）不是极值点.

- 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A = f _ {x x} ^ {\prime \prime} \left(\frac {1}{6}, \frac {1}{1 2}\right) = 1, \quad B = f _ {x y} ^ {\prime \prime} \left(\frac {1}{6}, \frac {1}{1 2}\right) = - 1, \quad C = f _ {y y} ^ {\prime \prime} \left(\frac {1}{6}, \frac {1}{1 2}\right) = 4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A > 0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f \left(\frac {1}{6}, \frac {1}{1 2}\right) = \frac {1}{6 ^ {3}} + \frac {8}{1 2 ^ {3}} - \frac {1}{6 \times 1 2} = - \frac {1}{2 1 6}.</equation>

---

**2018年第19题 | 解答题 | 10分**
19. (本题满分10分)

将长为2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.
**答案: **三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>
**解析: **解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长<equation>a=\frac{y}{4}</equation>正三角形的边长<equation>b=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L ( x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda(x+y+z-2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得 x,y,z的值代入 S（x，y，z）可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数 S（x，y，z）在有界闭区域 D = {（x，y，z）| x+y+z=2，x≥0，y≥0，z≥0}上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1} {\pi+4+3\sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值当 x=0时，<equation>S ( 0, y, z )</equation>在 y+z=2下的最小值为<equation>S \left( 0, \frac{8}{4+3\sqrt{3}}, \frac{6\sqrt{3}}{4+3\sqrt{3}} \right) = \frac{1}{4+3\sqrt{3}}.</equation>当 y=0时，<equation>S ( x, 0, z )</equation>在 x+z=2下的最小值为<equation>S \left( \frac{2\pi}{\pi+3\sqrt{3}}, 0, \frac{6\sqrt{3}}{\pi+3\sqrt{3}} \right) = \frac{1}{\pi+3\sqrt{3}}.</equation>当 z=0时，<equation>S ( x, y, 0 )</equation>在 x+y=2下的最小值为<equation>S \left( \frac{2\pi}{\pi+4}, \frac{8}{\pi+4}, 0 \right) = \frac{1}{\pi+4}.</equation>4个值比较可得，<equation>\frac{1} {\pi+4+3\sqrt{3}}</equation>为整个区域D上的最小值，也为<equation>x+y+z=2, x > 0, y > 0, z > 0</equation>时的<equation>S ( x, y, z )</equation>的最小值. 三个图形的面积之和存在最小值，最小值为<equation>\frac{1} {\pi+4+3\sqrt{3}}.</equation>

---

**2016年第17题 | 解答题 | 10分**
17. (本题满分10分）

已知函数<equation>z=z(x,y)</equation>由方程<equation>( x^{2}+y^{2}) z+\ln z+2(x+y+1)=0</equation>确定，求<equation>z=z(x,y)</equation>的极值.
**答案: **极大值<equation>f(-1,-1)=1.</equation>
**解析: **对方程两端分别关于 x和关于 y求偏导数，得<equation>2 x z + \left(x ^ {2} + y ^ {2}\right) \frac {\partial z}{\partial x} + \frac {1}{z} \frac {\partial z}{\partial x} + 2 = 0,</equation><equation>2 y z + \left(x ^ {2} + y ^ {2}\right) \frac {\partial z}{\partial y} + \frac {1}{z} \frac {\partial z}{\partial y} + 2 = 0.</equation>当<equation>\frac{\partial z}{\partial x}=0</equation>时，<equation>2 x z+2=0,x=-\frac{1}{z}.</equation>同理，当<equation>\frac{\partial z}{\partial y}=0</equation>时，<equation>2 y z+2=0,y=-\frac{1}{z}.</equation>将（x，y）<equation>= \left(-\frac{1}{z}, -\frac{1}{z}\right)</equation>代入原方程求 x，y.<equation>\frac {2}{z ^ {2}} \cdot z + \ln z + 2 \left(- \frac {2}{z} + 1\right) = 0.</equation>化简（3）式得<equation>\ln z=\frac{2}{z}-2</equation>. 通过观察 y=<equation>\ln z</equation>以及 y=<equation>\frac{2}{z}-2</equation>的图像，可知这两条曲线交于点 (1,0). 考虑函数<equation>f(z)=\ln z-\frac{2}{z}+2.</equation><equation>f^{\prime}(z)=\frac{1}{z}+\frac{2}{z^{2}}>0</equation>，从而 f(z)在（0，<equation>+\infty</equation>）上单调增加，于是 z=1是 f(z)=0的唯一解. 因此，驻点坐标为（-1，-1）.

下面计算驻点（-1，-1）处的二阶偏导数.

对（1）式两端关于 x求导，得<equation>2 z + 2 x \frac {\partial z}{\partial x} + 2 x \frac {\partial z}{\partial x} + \left(x ^ {2} + y ^ {2}\right) \frac {\partial^ {2} z}{\partial x ^ {2}} - \frac {1}{z ^ {2}} \left(\frac {\partial z}{\partial x}\right) ^ {2} + \frac {1}{z} \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>对（2）式两端关于 y求导，得<equation>2 z + 2 y \frac {\partial z}{\partial y} + 2 y \frac {\partial z}{\partial y} + \left(x ^ {2} + y ^ {2}\right) \frac {\partial^ {2} z}{\partial y ^ {2}} - \frac {1}{z ^ {2}} \left(\frac {\partial z}{\partial y}\right) ^ {2} + \frac {1}{z} \frac {\partial^ {2} z}{\partial y ^ {2}} = 0.</equation>对（1）式两端关于 y求导，得<equation>2 x \frac {\partial z}{\partial y} + 2 y \frac {\partial z}{\partial x} + \left(x ^ {2} + y ^ {2}\right) \frac {\partial^ {2} z}{\partial x \partial y} - \frac {1}{z ^ {2}} \frac {\partial z}{\partial x} \frac {\partial z}{\partial y} + \frac {1}{z} \frac {\partial^ {2} z}{\partial x \partial y} = 0.</equation>将<equation>x=-1, y=-1, z=1</equation>代入（4）式，（5）式，（6）式，并注意到<equation>\frac{\partial z}{\partial x}\bigg|_{(-1,-1)}=\frac{\partial z}{\partial y}\bigg|_{(-1,-1)}=0</equation>可得，<equation>\begin{aligned} 2 + 2 \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(- 1, - 1)} + \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(- 1, - 1)} &= 0, \quad 2 + 2 \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(- 1, - 1)} + \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(- 1, - 1)} = 0. \\ 2 \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(- 1, - 1)} + \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(- 1, - 1)} &= 0. \end{aligned}</equation>从而，<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(-1,-1)}=\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(-1,-1)}=-\frac{2}{3},\frac{\partial^{2}z}{\partial x\partial y}\bigg|_{(-1,-1)}=0.</equation>因此，<equation>\left[ \frac{\partial^{2} z}{\partial x^{2}}\frac{\partial^{2} z}{\partial y^{2}}-\left(\frac{\partial^{2} z}{\partial x \partial y}\right)^{2} \right] \Bigg|_{(-1,-1)}>0, \frac{\partial^{2} z}{\partial x^{2}} \Bigg|_{(-1,-1)}<0.</equation>由二元函数极值存在的充分条件可知，点（-1，-1）是函数<equation>z=z(x,y)</equation>的极大值点，极大值为1.

---

**2015年第17题 | 解答题 | 10分**
17. (本题满分11分)

已知函数 f(x,y)满足<equation>f_{xy}^{\prime\prime}(x,y)=2(y+1)\mathrm{e}^{x},f_{x}^{\prime}(x,0)=(x+1)\mathrm{e}^{x},f(0,y)=y^{2}+2y</equation>，求 f(x,y)的极值.
**答案: **(17) 极小值<equation>f ( 0,-1 )=-1.</equation>
**解析: **解 利用题给条件，我们来逐步求 f（x，y）.

由于<equation>f_{xy}^{\prime \prime}(x,y)=2(y+1)\mathrm{e}^{x}</equation>，故<equation>f _ {x} ^ {\prime} (x, y) = \int f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} y = \int 2 (y + 1) \mathrm {e} ^ {x} \mathrm {d} y = \mathrm {e} ^ {x} \left(y ^ {2} + 2 y\right) + g (x),</equation>其中<equation>g(x)</equation>是以<equation>x</equation>为变量的一元函数.当<equation>y = 0</equation>时，<equation>f_x^{\prime}(x,0) = g(x) = (x + 1)\mathrm{e}^x</equation>，故<equation>f _ {x} ^ {\prime} (x, y) = \left(y ^ {2} + 2 y\right) \mathrm {e} ^ {x} + (x + 1) \mathrm {e} ^ {x} = \left(y + 1\right) ^ {2} \mathrm {e} ^ {x} + x \mathrm {e} ^ {x}.</equation>从而，<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int \left[ (y + 1) ^ {2} \mathrm {e} ^ {x} + x \mathrm {e} ^ {x} \right] \mathrm {d} x = (y + 1) ^ {2} \mathrm {e} ^ {x} + (x - 1) \mathrm {e} ^ {x} + h (y),</equation>其中 h(y)是以y为变量的一元函数.代入 x=0，得 f（0，y）=（y+1）²-1+h(y）=y²+2y，故 h(y)=0.

因此，<equation>f ( x, y ) = ( y + 1 )^{2} \mathrm{e}^{x} + ( x - 1 ) \mathrm{e}^{x}.</equation>计算 f（x，y）的偏导数得，<equation>f _ {x} ^ {\prime} (x, y) = (y + 1) ^ {2} \mathrm {e} ^ {x} + x \mathrm {e} ^ {x}, \quad f _ {y} ^ {\prime} (x, y) = 2 (y + 1) \mathrm {e} ^ {x}.</equation>由于 f(x,y)的驻点满足<equation>f_{x}^{\prime}(x,y)=f_{y}^{\prime}(x,y)=0</equation>，故解<equation>\left\{ \begin{array}{l l} (y+1)^{2}\mathrm{e}^{x}+x\mathrm{e}^{x}=0, \\ 2(y+1)\mathrm{e}^{x}=0 \end{array} \right.</equation>得 x=0，y=-1. 因此，点（0，-1）为 f(x,y)的驻点.

根据二元函数极值存在的充分条件，分别计算<equation>f_{xx}^{\prime \prime}(0, - 1), f_{yy}^{\prime \prime}(0, - 1), f_{xy}^{\prime \prime}(0, - 1)</equation>.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (y + 1) ^ {2} \mathrm {e} ^ {x} + (x + 1) \mathrm {e} ^ {x}, f _ {x x} ^ {\prime \prime} (0, - 1) = 1,</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = 2 \mathrm {e} ^ {x}, \quad f _ {y y} ^ {\prime \prime} (0, - 1) = 2,</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = 2 (y + 1) \mathrm {e} ^ {x}, f _ {x y} ^ {\prime \prime} (0, - 1) = 0.</equation>由于<equation>f_{xx}^{\prime \prime}(0,-1)f_{yy}^{\prime \prime}(0,-1)-[f_{xy}^{\prime \prime}(0,-1)]^{2}=2>0</equation>，且<equation>f_{xx}^{\prime \prime}(0,-1)=1>0</equation>，故点（0，-1）为<equation>f(x,y)</equation>的极小值点，<equation>f(0,-1)=-1</equation>为<equation>f(x,y)</equation>的极小值.

---

**2014年第6题 | 选择题 | 4分 | 答案: A**
6. 设函数 u(x,y)在有界闭区域 D上连续，在 D的内部具有2阶连续偏导数，且满足<equation>\frac{\partial^{2} u}{\partial x \partial y}\neq0</equation>及<equation>\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}=0</equation>则（    )

A. u(x,y)的最大值和最小值都在 D的边界上取得

B. u(x,y)的最大值和最小值都在 D的内部取得

C. u(x,y)的最大值在 D的内部取得，最小值在 D的边界上取得

D. u(x,y)的最小值在 D的内部取得，最大值在 D的边界上取得
答案: A
**解析: **解 由于<equation>u ( x, y )</equation>是有界闭区域D上的连续函数，故<equation>u ( x, y )</equation>在D上必有最大值和最小值.若<equation>u ( x, y )</equation>在区域D的内部取得最大值或最小值，则该最值点是<equation>u ( x, y )</equation>的驻点.

由题设，对区域 D内的任何一点，都有<equation>\frac{\partial^2 u}{\partial x^2} +\frac{\partial^2 u}{\partial y^2} = 0</equation>，故<equation>\frac{\partial^2 u}{\partial x^2}\cdot \frac{\partial^2 u}{\partial y^2}\leqslant 0</equation>，而<equation>\frac{\partial^2 u}{\partial x\partial y}\neq 0</equation>，从而<equation>\left(\frac{\partial^2 u}{\partial x\partial y}\right)^2 > 0</equation>，因此<equation>\frac{\partial^2 u}{\partial x^2}\frac{\partial^2 u}{\partial y^2} -\left(\frac{\partial^2 u}{\partial x\partial y}\right)^2 < 0.</equation>特别地，该不等式对区域 D内的驻点也成立.

由二元函数极值存在的充分条件知，区域 D内的驻点都不是 u（x，y）的极值点.因此 u（x,y）的最大值和最小值都在 D的边界上取得.应选A.

---

**2013年第19题 | 解答题 | 10分**
19. (本题满分10分)

求曲线<equation>x^{3}- x y+y^{3}=1 ( x \geqslant0, y \geqslant0)</equation>上的点到坐标原点的最长距离和最短距离.
**答案: **(19) 最长距离<equation>\sqrt{2}</equation>，最短距离1.
**解析: **解作拉格朗日函数<equation>L ( x,y,\lambda) = x^{2}+y^{2}+\lambda \left( x^{3}-xy+y^{3}-1 \right).</equation>令<equation>L _ {x} ^ {\prime} = 2 x + 3 \lambda x ^ {2} - \lambda y = 0,</equation><equation>L _ {y} ^ {\prime} = 2 y + 3 \lambda y ^ {2} - \lambda x = 0,</equation><equation>L _ {\lambda} ^ {\prime} = \varphi (x, y) = x ^ {3} - x y + y ^ {3} - 1 = 0.</equation>整理（1）式，（2）式得<equation>2 x = \lambda \left(y - 3 x ^ {2}\right),</equation><equation>2 y = \lambda \left(x - 3 y ^ {2}\right).</equation>当<equation>\lambda=0</equation>时，由（4）式，（5）式可得<equation>x=y=0</equation>；当<equation>\lambda\neq0</equation>，<equation>x=0</equation>时，由（4）式可得<equation>y=0</equation>；当<equation>\lambda\neq0</equation><equation>y=0</equation>时，由（5）式可得<equation>x=0</equation>.由于点（0，0）不在曲线<equation>x^{3}-xy+y^{3}-1=0</equation>上，故以上情况均不符合题意.

下面只考虑<equation>\lambda\neq0</equation>，<equation>x\neq0</equation>，<equation>y\neq0</equation>的情况.

当<equation>\lambda \neq 0</equation>，<equation>x\neq 0</equation>，<equation>y\neq 0</equation>时，<equation>\frac{(4)}</equation>式（5）式得，<equation>\frac{x}{y} = \frac{y - 3x^2}{x - 3y^2}</equation>，整理得<equation>x^{2} - 3y^{2}x - y^{2} + 3x^{2}y = 0</equation>，即<equation>(x - y) (x + y + 3 x y) = 0.</equation>当<equation>x > 0</equation>，<equation>y > 0</equation>时，<equation>x + y + 3xy > 0</equation>，故只有<equation>x = y</equation>成立.代入（3）式，可得<equation>2x^{3} - x^{2} - 1 = 0.</equation>分解因式，得<equation>(x - 1)(2x^{2} + x + 1) = 0.</equation>由于<equation>2x^{2} + x + 1 > 0</equation>，故<equation>x = 1</equation>，从而<equation>y = 1.</equation>点（1，1）为曲线<equation>x^{3} - xy + y^{3} = 1(x\geqslant 0,y\geqslant 0)</equation>上唯一可能的极值点.此时，<equation>d = \sqrt{1 + 1} = \sqrt{2}.</equation>考虑曲线端点到原点的距离，当<equation>x=0</equation>时，代入曲线方程得<equation>y=1,d=\sqrt{1+0}=1</equation>；当<equation>y=0</equation>时，代入曲线方程得<equation>x=1,d=\sqrt{1+0}=1.</equation>综上所述，最长距离为<equation>\sqrt{2}</equation>，最短距离为1.

---

**2012年第16题 | 解答题 | 10分**
16. (本题满分10分）

求函数<equation>f ( x,y)=x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极值.
**答案: **(16) 极大值<equation>f(1,0) = \mathrm{e}^{-\frac{1}{2}}</equation>，极小值<equation>f(-1,0) = -\mathrm{e}^{-\frac{1}{2}}.</equation>
**解析: **解<equation>\textcircled{1}</equation>先找到<equation>f(x,y)</equation>的全部驻点.

记<equation>g ( x,y)=\mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}.</equation>由于<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = \left(1 - x ^ {2}\right) g (x, y),</equation><equation>f _ {y} ^ {\prime} (x, y) = - x y \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = (- x y) g (x, y).</equation>由于 g(x,y) > 0，故满足<equation>\left\{\begin{array}{l l}1-x^{2}=0\\-xy=0\end{array}\right.</equation>的点（x，y）为 f(x，y）的驻点.解该方程组得（x，y）= （<equation>\pm1,0).</equation>因此，点（1，0）和点（-1，0）为<equation>f(x,y)</equation>的全部驻点.<equation>\textcircled{2}</equation>计算二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (- 2 x) g (x, y) + \left(1 - x ^ {2}\right) g _ {x} ^ {\prime} (x, y),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = \left(1 - x ^ {2}\right) g _ {y} ^ {\prime} (x, y),</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = (- x) g (x, y) + (- x y) g _ {y} ^ {\prime} (x, y).</equation><equation>\textcircled{3}</equation>计算<equation>A C-B^{2}.</equation>由于<equation>f ( x, y )</equation>的驻点<equation>\left(x_{0}, y_{0}\right)</equation>均满足<equation>1-x_{0}^{2}=0,-x_{0}y_{0}=0</equation>，而<equation>g ( x, y )</equation>恒大于零，故在驻点 (1,0)处，<equation>f_{xx}^{\prime \prime}(1,0)=-2g(1,0)<0,f_{xy}^{\prime \prime}(1,0)=0,f_{yy}^{\prime \prime}(1,0)=-g(1,0).</equation>因此，<equation>f _ {x x} ^ {\prime \prime} (1, 0) f _ {y y} ^ {\prime \prime} (1, 0) - \left[ f _ {x y} ^ {\prime \prime} (1, 0) \right] ^ {2} = 2 g ^ {2} (1, 0) > 0.</equation>由于<equation>f_{xx}^{\prime \prime}(1,0)=-2 g(1,0)<0</equation>，故点（1，0）为<equation>f(x,y)</equation>的极大值点，<equation>f(1,0)=\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极大值.同理可得，点（-1，0）为<equation>f(x,y)</equation>的极小值点，<equation>f(-1,0)=-\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极小值.

因此，函数<equation>f ( x, y ) = x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极大值为<equation>\mathrm{e}^{- \frac{1}{2}}</equation>，极小值为<equation>- \mathrm{e}^{- \frac{1}{2}}.</equation>

---

**2011年第5题 | 选择题 | 4分 | 答案: A**
5. 设函数 f(x)，g(x)均有二阶连续导数，满足 f(0)>0,g(0)<0，且<equation>f^{\prime}(0)=g^{\prime}(0)=0</equation>，则函数 z=f(x)g(y)在点 (0,0)处取得极小值的一个充分条件是（    ）

A.<equation>f^{\prime\prime}(0)<0,g^{\prime\prime}(0)>0</equation>B.<equation>f^{\prime\prime}(0)<0,g^{\prime\prime}(0)<0</equation>C.<equation>f^{\prime\prime}(0)>0,g^{\prime\prime}(0)>0</equation>D.<equation>f^{\prime\prime}(0)>0,g^{\prime\prime}(0)<0</equation>
答案: A
**解析: **解分别求出<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y},\frac{\partial^{2}z}{\partial x^{2}},\frac{\partial^{2}z}{\partial y^{2}}</equation>以及<equation>\frac{\partial^{2}z}{\partial x\partial y}.</equation>由<equation>z = f(x)g(y)</equation>得<equation>\frac {\partial z}{\partial x} = f ^ {\prime} (x) g (y), \quad \frac {\partial z}{\partial y} = f (x) g ^ {\prime} (y),</equation><equation>\frac {\partial^ {2} z}{\partial x ^ {2}} = f ^ {\prime \prime} (x) g (y), \quad \frac {\partial^ {2} z}{\partial y ^ {2}} = f (x) g ^ {\prime \prime} (y), \quad \frac {\partial^ {2} z}{\partial x \partial y} = f ^ {\prime} (x) g ^ {\prime} (y).</equation>根据二元函数取极小值的充分条件，若在点（0，0）处，<equation>\left. \left(\frac {\partial^ {2} z}{\partial x ^ {2}} \frac {\partial^ {2} z}{\partial y ^ {2}}\right) \right| _ {(0, 0)} - \left. \left(\frac {\partial^ {2} z}{\partial x \partial y}\right) ^ {2} \right| _ {(0, 0)} > 0,</equation>且<equation>\left.\frac{\partial^2 z}{\partial x^2}\right|_{(0,0)} > 0</equation>，则二元函数<equation>z = f(x)g(y)</equation>在点（0，0）处有极小值.

首先，<equation>\left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(0, 0)} > 0 \Leftrightarrow f ^ {\prime \prime} (0) g (0) > 0 \xleftrightarrow {g (0) < 0} f ^ {\prime \prime} (0) < 0.</equation>又由于<equation>f^{\prime}(0)=g^{\prime}(0)=0</equation>，故<equation>\left. \frac{\partial^{2} z}{\partial x \partial y}\right|_{(0,0)}=0.</equation>（1）式成立当且仅当<equation>\left. \left(\frac{\partial^{2} z}{\partial x^{2}}\frac{\partial^{2} z}{\partial y^{2}}\right)\right|_{(0,0)}>0.</equation>因为<equation>\left. \frac{\partial^{2} z}{\partial x^{2}}\right|_{(0,0)}>0</equation>，所以必有<equation>\left. \frac{\partial^{2} z}{\partial y^{2}}\right|_{(0,0)}>0</equation>，而<equation>\left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(0, 0)} > 0 \Leftrightarrow f (0) g ^ {\prime \prime} (0) > 0 \Longleftrightarrow \frac {f (0) > 0}{g ^ {\prime \prime} (0)} g ^ {\prime \prime} (0) > 0.</equation>因此，<equation>z=f(x)g(y)</equation>在点（0，0）处取得极小值的一个充分条件是<equation>f^{\prime \prime}(0)<0,g^{\prime \prime}(0)>0.</equation>应选A.

---

**2009年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 z=f(x,y)的全微分为<equation>\mathrm{d} z=x\mathrm{d} x+y\mathrm{d} y</equation>，则点（0,0）（    )

A. 不是 f(x,y)的连续点 B. 不是 f(x,y)的极值点

C. 是 f(x,y)的极大值点 D. 是 f(x,y)的极小值点
答案: D
**解析: **解 由全微分的表达式知，<equation>f_{x}^{\prime}(x,y)=x,f_{y}^{\prime}(x,y)=y</equation>，从而点（0，0）为 f(x,y)的驻点.根据二元函数极值存在的充分条件，计算<equation>f_{xx}^{\prime\prime},f_{xy}^{\prime\prime},f_{yy}^{\prime\prime}</equation>，得<equation>f_{xx}^{\prime\prime}\equiv 1,f_{xy}^{\prime\prime}\equiv 0,f_{yy}^{\prime\prime}\equiv 1.</equation>从而<equation>f_{xx}^{\prime\prime}(0,0)f_{yy}^{\prime\prime}(0,0)-[f_{xy}^{\prime\prime}(0,0)]^{2}=1>0, f_{xx}^{\prime\prime}(0,0)>0.</equation>因此，<equation>f(x,y)</equation>在点（0，0）处取极小值.应选D.

---


#### 二重积分的计算

**2025年第20题 | 解答题 | 12分**
20. (本题满分12分)

已知平面有界区域 D = {（x,y）<equation>\mid x^{2}+y^{2}\leqslant 4 x, x^{2}+y^{2}\leqslant 4 y</equation>，计算<equation>\iint_{D} ( x-y )^{2} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **<equation>1 2 \pi - \frac {1 1 2}{3}</equation>
**解析: **解如图所示，区域D由两个圆围成，计算两圆的交点。联立两圆方程可得<equation>\left\{ \begin{array}{l l} x^{2} + y^{2} = 4x, \\ x^{2} + y^{2} = 4y, \end{array} \right.</equation>两式相减可得<equation>x = y</equation>，代入第一个方程可得<equation>2x^{2}</equation><equation>-4x = 0</equation>，解得<equation>x = 0</equation>或<equation>x = 2</equation>.于是，两圆的交点为（0,0），（2,2）.连接两交点的直线方程为<equation>y = x</equation>.进一步可得区域D关于直线<equation>y = x</equation>对称.

记区域<equation>D</equation>位于直线<equation>y = x</equation>下方的部分为<equation>D_{1}</equation>，则由轮换对称性的结论可得<equation>\begin{aligned} \iint_ {D} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y &= \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D \backslash D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {1}} (y - x) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation><equation>D_{1}</equation>的极坐标表示为<equation>D_{1} = \left\{(r,\theta)\mid 0 \leqslant r \leqslant 4 \sin \theta ,0 \leqslant \theta \leqslant \frac{\pi}{4}\right\}</equation>.<equation>\begin{aligned} \iint_ {D _ {1}} (x - y) ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D _ {1}} \left(r ^ {2} - 2 r ^ {2} \cos \theta \sin \theta\right) \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta \int_ {0} ^ {4 \sin \theta} r ^ {3} \mathrm {d} r \\ &= \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \sin \theta \cos \theta\right) \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {4 \sin \theta} \mathrm {d} \theta = 6 4 \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \sin \theta \cos \theta\right) \sin^ {4} \theta \mathrm {d} \theta \\ &= 6 4 \int_ {0} ^ {\frac {\pi}{4}} \sin^ {4} \theta \mathrm {d} \theta - 1 2 8 \int_ {0} ^ {\frac {\pi}{4}} \sin^ {5} \theta \cos \theta \mathrm {d} \theta . \end{aligned}</equation>分别计算<equation>64\int_{0}^{\frac{\pi}{4}}\sin^{4}\theta \mathrm{d}\theta</equation>与<equation>128\int_{0}^{\frac{\pi}{4}}\sin^{5}\theta \cos \theta \mathrm{d}\theta .</equation><equation>\begin{aligned} 6 4 \int_ {0} ^ {\frac {\pi}{4}} \sin^ {4} \theta \mathrm {d} \theta &= 6 4 \int_ {0} ^ {\frac {\pi}{4}} \left(\frac {1 - \cos 2 \theta}{2}\right) ^ {2} \mathrm {d} \theta = 1 6 \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \cos 2 \theta + \cos^ {2} 2 \theta\right) \mathrm {d} \theta \\ &= 1 6 \int_ {0} ^ {\frac {\pi}{4}} \left(1 - 2 \cos 2 \theta + \frac {1 + \cos 4 \theta}{2}\right) \mathrm {d} \theta \\ &= 6 \pi - 3 2 \int_ {0} ^ {\frac {\pi}{4}} \cos 2 \theta \mathrm {d} \theta + 8 \int_ {0} ^ {\frac {\pi}{4}} \cos 4 \theta \mathrm {d} \theta \\ &= 6 \pi - 3 2 \cdot \frac {\sin 2 \theta}{2} \Bigg | _ {0} ^ {\frac {\pi}{4}} + 8 \cdot \frac {\sin 4 \theta}{4} \Bigg | _ {0} ^ {\frac {\pi}{4}} = 6 \pi - 1 6. \end{aligned}</equation><equation>128\int_{0}^{\frac{\pi}{4}}\sin^{5}\theta \cos \theta \mathrm{d}\theta = 128\int_{0}^{\frac{\pi}{4}}\sin^{5}\theta \mathrm{d}(\sin \theta) = 128\cdot \frac{\sin^{6}\theta}{6}\bigg|_{0}^{\frac{\pi}{4}} = 128\cdot \frac{1}{6}\cdot \frac{1}{8} = \frac{8}{3}.</equation>因此，<equation>\iint_{D}(x - y)^{2}\mathrm{d}x\mathrm{d}y = 2\cdot \left(6\pi - 16 - \frac{8}{3}\right) = 12\pi - \frac{112}{3}.</equation>

---

**2024年第17题 | 解答题 | 10分**
17. (本题满分10分)

假设平面某有界区域 D位于第一象限，并且由曲线<equation>x y=\frac{1}{3}, x y=3</equation>与直线<equation>y=\frac{1}{3} x, y=3 x</equation>围成，试计算<equation>\iint_{D} ( 1+x-y ) \mathrm{d} x \mathrm{d} y.</equation>
**答案: **##<equation>\frac{8}{3}\ln 3.</equation>
**解析: **解区域 D如图（a）所示，注意到区域 D的四条边界曲线中，交换曲线<equation>xy=\frac{1}{3}</equation>与<equation>xy=3</equation>中x， y的位置，可得<equation>yx=\frac{1}{3}</equation>与<equation>yx=3</equation>，即曲线方程不变，故这两条曲线均关于直线<equation>y=x</equation>对称，而直线<equation>y=\frac{1}{3} x</equation>与直线<equation>y=3x</equation>关于直线<equation>y=x</equation>对称，故这四条曲线所围成的区域 D也关于直线<equation>y=x</equation>对称，从而对变量 x，y具有轮换对称性.

(a)

(b)

由轮换对称性的结论（2）可得<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\iint_{D}y\mathrm{d}x\mathrm{d}y</equation>，故<equation>\iint_ {D} (1 + x - y) \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y + \iint_ {D} x \mathrm {d} x \mathrm {d} y - \iint_ {D} y \mathrm {d} x \mathrm {d} y = \iint_ {D} \mathrm {d} x \mathrm {d} y.</equation>下面用两种方法计算<equation>\iint_{D}\mathrm{d}x\mathrm{d}y.</equation>（法一）在极坐标系下计算.

曲线<equation>xy = \frac{1}{3}</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = \frac{1}{3}</equation>，整理可得<equation>r = \sqrt{\frac{2}{3\sin 2\theta}}</equation>，曲线<equation>xy = 3</equation>的极坐标方程为<equation>r^2\cos \theta \sin \theta = 3</equation>，整理可得<equation>r = \sqrt{\frac{6}{\sin 2\theta}}</equation>直线<equation>y = \frac{1}{3} x</equation>的极坐标方程为<equation>\theta = \arctan \frac{1}{3},y = 3x</equation>的极坐标方程为<equation>\theta = \arctan 3.</equation>区域 D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \sqrt {\frac {2}{3 \sin 2 \theta}} \leqslant r \leqslant \sqrt {\frac {6}{\sin 2 \theta}}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation>于是，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \mathrm {d} \theta \int_ {\sqrt {\frac {2}{3 \sin 2 \theta}}} ^ {\sqrt {\frac {6}{\sin 2 \theta}}} r \mathrm {d} r &= \frac {1}{2} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} r ^ {2} \left| \begin{array}{c} \sqrt {\frac {6}{\sin 2 \theta}} \\ \sqrt {\frac {2}{3 \sin 2 \theta}}  \right| \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \csc 2 \theta \mathrm {d} \theta = \frac {4}{3} \ln | \csc 2 \theta - \cot 2 \theta | \Bigg | _ {\arctan \frac {1}{3}} ^ {\arctan 3}. \end{aligned}</equation>由于<equation>\csc 2\theta-\cot 2\theta=\frac{1-\cos 2\theta}{\sin 2\theta}=\frac{2\sin^{2}\theta}{2\sin \theta\cos \theta}=\tan \theta</equation>，故<equation>\iint_{D}\mathrm{d}x\mathrm{d}y=\frac{4}{3}\ln |\tan \theta |\Bigg|_{\arctan \frac{1}{3}}^{\arctan 3}</equation>当<equation>\theta =\arctan \frac{1}{3}</equation>时，<equation>\tan \theta =\frac{1}{3}</equation>，当<equation>\theta =\arctan 3</equation>时，<equation>\tan \theta =3.</equation>因此，<equation>\iint_ {D} \mathrm {d} x \mathrm {d} y = \frac {4}{3} \left(\ln 3 - \ln \frac {1}{3}\right) = \frac {8}{3} \ln 3.</equation>（法二）在直角坐标系下计算.

联立<equation>\left\{ \begin{array}{l l} x y = \frac{1}{3}, \\ y = \frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = 1, \\ y = \frac{1}{3}. \end{array} \right.</equation>联立<equation>\left\{ \begin{array}{l l} x y = \frac{1}{3}, \\ y = 3 x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = \frac{1}{3}, \\ y = 1. \end{array} \right.</equation>联立<equation>\left\{ \begin{array}{l l} x y = 3, \\ y = \frac{1}{3} x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = 3, \\ y = 1. \end{array} \right.</equation>联立<equation>\left\{ \begin{array}{l l} x y = 3, \\ y = 3 x, \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} x = 1, \\ y = 3. \end{array} \right.</equation>如图（b）所示，直线<equation>x = 1</equation>将区域D分为两部分<equation>D_{1}, D_{2}</equation>.<equation>D_{1}</equation>由曲线<equation>xy = \frac{1}{3}</equation>，直线<equation>y = 3x</equation>与<equation>x = 1</equation>围成，<equation>D_{2}</equation>由曲线<equation>xy = 3</equation>，直线<equation>y = \frac{1}{3} x</equation>与<equation>x = 1</equation>围成，<equation>\iint_{D}\mathrm{d}x\mathrm{d}y</equation>等于D的面积，即<equation>D_{1}</equation>的面积与<equation>D_{2}</equation>的面积之和.

因此，<equation>\begin{aligned} \iint_ {D} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {1}{3}} ^ {1} \left(3 x - \frac {1}{3 x}\right) \mathrm {d} x + \int_ {1} ^ {3} \left(\frac {3}{x} - \frac {x}{3}\right) \mathrm {d} x = \left(\frac {3 x ^ {2}}{2} - \frac {1}{3} \ln x\right) \left| _ {\frac {1}{3}} ^ {1} + \left(3 \ln x - \frac {x ^ {2}}{6}\right) \right| _ {1} ^ {3} \\ &= \frac {3}{2} - \frac {1}{6} + \frac {1}{3} \ln \frac {1}{3} + 3 \ln 3 - \frac {3}{2} + \frac {1}{6} = - \frac {1}{3} \ln 3 + 3 \ln 3 = \frac {8}{3} \ln 3. \end{aligned}</equation>

---


#### 全微分的概念与计算

**2021年第6题 | 选择题 | 5分 | 答案: C**
6. 设函数 f(u,v)可微，且<equation>f \left( x+1, \mathrm{e}^{x} \right)=x \left( x+1 \right)^{2}, f \left( x, x^{2} \right)=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f \left( 1, 1 \right)=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>
答案: C
**解析: **根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f ( x+1,\mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x,x^{2} )=2 x^{2} \ln x</equation>两端均关于 x求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令 x=0，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令 x=1，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第11题 | 填空题 | 4分**
11. 设<equation>z=\arctan[ x y+\sin(x+y) ]</equation>, 则<equation>\mathrm{d} z|_{(0,\pi)}=</equation>___
**答案: **<equation>(\pi - 1) \mathrm {d} x - \mathrm {d} y.</equation>
**解析: **根据链式法则，<equation>\frac{\partial z}{\partial x}=\frac{y+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}},</equation><equation>\frac{\partial z}{\partial y}=\frac{x+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}}.</equation>代入 x=0，y=<equation>\pi</equation>，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,\pi)}=\pi-1, \frac{\partial z}{\partial y}\bigg|_{(0,\pi)}=-1.</equation>因此，<equation>\mathrm{d}z\bigg|_{(0,\pi)}=(\pi-1)\mathrm{d}x-\mathrm{d}y.</equation>

---

**2017年第12题 | 填空题 | 4分**
12. 设函数<equation>f(x,y)</equation>具有一阶连续偏导数，且<equation>\mathrm{d} f(x,y)=y \mathrm{e}^{y} \mathrm{d} x+x(1+y) \mathrm{e}^{y} \mathrm{d} y</equation><equation>f(0,0)=0</equation>，则<equation>f(x,y)=</equation>___.
**答案: **##<equation>x y \mathrm{e}^{y}.</equation>
**解析: **由于<equation>\mathrm {d} f (x, y) = y \mathrm {e} ^ {y} \mathrm {d} x + x (1 + y) \mathrm {e} ^ {y} \mathrm {d} y,</equation>故<equation>f_x^{\prime}(x,y) = y\mathrm{e}^{y}, f_y^{\prime}(x,y) = x(1 + y)\mathrm{e}^{y}.</equation>对<equation>f_{x}^{\prime}(x,y)</equation>关于 x积分，得<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int y \mathrm {e} ^ {y} \mathrm {d} x = x y \mathrm {e} ^ {y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

对<equation>x y \mathrm{e}^{y}+\varphi(y)</equation>关于y求偏导数，得<equation>\frac {\partial \left[ x y \mathrm {e} ^ {y} + \varphi (y) \right]}{\partial y} = x \mathrm {e} ^ {y} + x y \mathrm {e} ^ {y} + \varphi^ {\prime} (y) = x (1 + y) \mathrm {e} ^ {y} + \varphi^ {\prime} (y).</equation>与<equation>f_{y}^{\prime}(x,y)</equation>比较，得<equation>\varphi^{\prime}(y)=0</equation>，故<equation>\varphi(y)\equiv C</equation>，其中C为常数.

代入<equation>x=0,y=0</equation>，得<equation>f(0,0)=0+C.</equation>，于是，<equation>C=0.</equation>因此，<equation>f ( x,y) = x y \mathrm{e}^{y}.</equation>

---

**2015年第13题 | 填空题 | 4分**
13. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{x+2y+3z} + xyz = 1</equation>确定，则<equation>\mathrm{d}z|_{(0,0)} =</equation>___
**答案: **<equation>- \frac {1}{3} \mathrm {d} x - \frac {2}{3} \mathrm {d} y.</equation>
**解析: **解下面我们分别用上述三种方法解本题.

（法一）对原方程两端分别关于<equation>x,y</equation>求偏导数，可得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(1 + 3 \frac {\partial z}{\partial x}\right) + y z + x y \frac {\partial z}{\partial x} = 0.</equation><equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(2 + 3 \frac {\partial z}{\partial y}\right) + x z + x y \frac {\partial z}{\partial y} = 0.</equation>当 x=0,y=0时，由原方程知<equation>\mathrm{e}^{3 z}=1</equation>，故 z(0,0）=0.代入（1）式得<equation>3\frac{\partial z}{\partial x}=-1.</equation>代入（2）式得<equation>3\frac{\partial z}{\partial y}=-2.</equation>因此，<equation>\mathrm{d}z|_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法二）对原方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{x + 2y + 3z} + xyz\right) = 0</equation>，展开得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z\right) + y z \mathrm {d} x + x z \mathrm {d} y + x y \mathrm {d} z = 0.</equation>当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>代入（3）式得<equation>\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法三）当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>令<equation>F(x,y,z) = \mathrm{e}^{x + 2y + 3z} + xyz - 1</equation>，则由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = - \left. \frac {F _ {x} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {\mathrm {e} ^ {x + 2 y + 3 z} + y z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {1}{3},</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = - \left. \frac {F _ {y} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {2 \mathrm {e} ^ {x + 2 y + 3 z} + x z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {2}{3}.</equation>因此，<equation>\mathrm{d}z|_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>

---

**2014年第11题 | 填空题 | 4分**
11. 设<equation>z=z(x,y)</equation>是由方程<equation>\mathrm{e}^{2 y z}+x+y^{2}+z=\frac{7}{4}</equation>确定的函数，则<equation>\mathrm{d} z|_{\left(\frac{1}{2},\frac{1}{2}\right)}=</equation>___
**答案: **<equation>- \frac {1}{2} \left(\mathrm {d} x + \mathrm {d} y\right).</equation>
**解析: **解（法一）将<equation>x=\frac{1}{2}, y=\frac{1}{2}</equation>代入原方程得<equation>z=0.</equation>对方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{2yz}\right) + \mathrm{d}x + \mathrm{d}\left(y^{2}\right) + \mathrm{d}z = 0.</equation>进一步得<equation>\mathrm {e} ^ {2 y z} \mathrm {d} (2 y z) + \mathrm {d} x + 2 y \mathrm {d} y + \mathrm {d} z = 0,</equation>即<equation>2 z \mathrm {e} ^ {2 y z} \mathrm {d} y + 2 y \mathrm {e} ^ {2 y z} \mathrm {d} z + \mathrm {d} x + 2 y \mathrm {d} y + \mathrm {d} z = 0.</equation>代入<equation>x=y=\frac{1}{2}, z=0</equation>，可得<equation>\mathrm {d} z + \mathrm {d} x + \mathrm {d} y + \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\bigg|_{\left(\frac{1}{2},\frac{1}{2}\right)} = -\frac{1}{2} (\mathrm{d}x + \mathrm{d}y).</equation>（法二）由<equation>\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y</equation>知，需求<equation>\left.\frac{\partial z}{\partial x}\right|_{\left(\frac{1}{2},\frac{1}{2}\right)}</equation>和<equation>\left.\frac{\partial z}{\partial y}\right|_{\left(\frac{1}{2},\frac{1}{2}\right)}</equation>.

对方程两端分别关于<equation>x</equation>，y求导，得<equation>\mathrm {e} ^ {2 y z} \cdot 2 y \cdot \frac {\partial z}{\partial x} + 1 + \frac {\partial z}{\partial x} = 0, \quad \mathrm {e} ^ {2 y z} \cdot 2 z + \mathrm {e} ^ {2 y z} \cdot 2 y \cdot \frac {\partial z}{\partial y} + 2 y + \frac {\partial z}{\partial y} = 0.</equation>当<equation>x=y=\frac{1}{2}</equation>时，代入原方程解得<equation>z=0</equation>将<equation>x=y=\frac{1}{2}</equation><equation>z=0</equation>代入（1）式，可分别求得<equation>\frac{\partial z}{\partial x}=-\frac{1}{2},\frac{\partial z}{\partial y}=-\frac{1}{2}.</equation>因此，<equation>\mathrm{d}z\Big|_{\left(\frac{1}{2},\frac{1}{2}\right)} = -\frac{1}{2} (\mathrm{d}x + \mathrm{d}y).</equation>

---


#### 二重积分的概念与性质

**2019年第5题 | 选择题 | 4分 | 答案: A**
5. 已知平面区域<equation>D=\left\{(x,y)\mid|x|+|y|\leqslant \frac{\pi}{2}\right\}, I_{1}=\iint_{D}\sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y, I_{2}=\iint_{D}\sin \sqrt{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y, I_{3}=</equation><equation>\iint_{D}(1-\cos \sqrt{x^{2}+y^{2}})\mathrm{d}x\mathrm{d}y</equation>，则（    ）

A.<equation>I_{3}<I_{2}<I_{1}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{2}<I_{3}</equation>D.<equation>I_{2}<I_{3}<I_{1}</equation>
答案: A
**解析: **解如图所示，区域 D由四条直线<equation>x\pm y=\frac{\pi}{2}, x\pm y=-\frac{\pi}{2}</equation>围成.该

区域包含于圆心在原点，半径为<equation>\frac{\pi}{2}</equation>的圆盘区域<equation>\left\{(x,y)\left|x^{2}+y^{2}\leqslant\left(\frac{\pi}{2}\right)^{2}\right.\right\}</equation>.于是，在区域D内，点(x,y）满足<equation>0\leqslant\sqrt{x^{2}+y^{2}}\leqslant\frac{\pi}{2}.</equation>令<equation>u=\sqrt{x^{2}+y^{2}}.</equation>由于在<equation>\left(0,\frac{\pi}{2}\right)</equation>内，<equation>\sin u < u</equation>，故对区域D内的点，均有<equation>\sin \sqrt{x^{2}+y^{2}}<</equation><equation>\sqrt{x^{2}+y^{2}}.</equation>由定积分的保号性可知，<equation>I_{2} < I_{1}.</equation>考虑<equation>1-\cos u</equation>与<equation>\sin u</equation>的大小关系.令<equation>f(u)=\sin u+\cos u-1</equation>，则<equation>f^{\prime}(u)=\cos u-\sin u.</equation>当<equation>0 < u < \frac{\pi}{4}</equation>时，<equation>f^{\prime}(u)>0,f(u)</equation>单调增加；当<equation>\frac{\pi}{4} < u < \frac{\pi}{2}</equation>时，<equation>f^{\prime}(u)<0,f(u)</equation>单调减少.于是，<equation>f(u)</equation>在<equation>\left[0,\frac{\pi}{2}\right]</equation>上的最大值为<equation>f\left(\frac{\pi}{4}\right)=\sqrt{2}-1</equation>，最小值为<equation>f(0)=f\left(\frac{\pi}{2}\right)=0.</equation>在<equation>\left[0,\frac{\pi}{2}\right]</equation>上，<equation>f(u)\geqslant0</equation>即<equation>\sin u\geqslant1-\cos u</equation>，且等号仅当<equation>u=0</equation>和<equation>u=\frac{\pi}{2}</equation>时取得.

因此，对区域 D内的点，均有<equation>\sin \sqrt{x^{2}+y^{2}}\geqslant 1-\cos \sqrt{x^{2}+y^{2}}.</equation>由定积分的保号性可知，<equation>I_{3} < I_{2}.</equation>综上所述，<equation>I_{3} < I_{2} < I_{1}.</equation>应选A.

---

**2013年第6题 | 选择题 | 4分 | 答案: B**
6. 设<equation>D_{k}</equation>是圆域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>在第 k象限的部分.记<equation>I_{k}=\iint_{D_{k}}(y-x)\mathrm{d}x\mathrm{d}y(k=1,2,3,4)</equation>，则（    )

A.<equation>I_{1}>0</equation>B.<equation>I_{2}>0</equation>C.<equation>I_{3}>0</equation>D.<equation>I_{4}>0</equation>
答案: B
**解析: **解（法一）由于在第一象限内 x>0，y>0，第二象限内 x<0，y>0，第三象限内 x<0， y<0，第四象限内 x>0，y<0，故被积函数 y-x在第二象限内恒大于零，从而<equation>\iint_{D_{2}}(y-x)\mathrm{d}x\mathrm{d}y>0.</equation>应选B.

（法二）在极坐标系下计算<equation>I_{k}(k = 1,2,3,4).</equation><equation>\begin{aligned} I _ {k} \stackrel {\text {极 坐 标}} {=} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \mathrm {d} r &= \frac {1}{3} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \\ &= - \frac {\left(\sin \theta + \cos \theta\right)}{3} \left| \frac {k \pi}{2} \right. _ {\frac {(k - 1) \pi}{2}}. \end{aligned}</equation>分别求得<equation>I _ {1} = 0, \quad I _ {2} = \frac {2}{3}, \quad I _ {3} = 0, \quad I _ {4} = - \frac {2}{3}.</equation><equation>I_{2} > 0</equation>应选B.

---

**2010年第6题 | 选择题 | 4分 | 答案: D**
6.<equation>\lim_{n\rightarrow \infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>C.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>D.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>
答案: D
**解析: **## 解 （法一）考虑将原极限写成二重积分.

令<equation>\Delta\sigma_{ij}=\left[\frac{i-1}{n},\frac{i}{n}\right]\times\left[\frac{j-1}{n},\frac{j}{n}\right]\left(i,j=1,2,\dots,n\right)</equation>，则<equation>\left\{\Delta\sigma_{ij}\right\}_{1\leqslant i,j\leqslant n}</equation>为<equation>D=[0,1]\times[0,1]</equation>上的一个划分，<equation>\Delta\sigma_{ij}</equation>的面积为<equation>\frac{1}{n^{2}}</equation>取<equation>\Delta\sigma_{ij}</equation>上的一点<equation>\left(\frac{i}{n},\frac{j}{n}\right).</equation>由于<equation>\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right) \left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \cdot \frac {1}{n ^ {2}},</equation>故<equation>\begin{aligned} \text {原 极 限} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right)\left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \right] = \iint_ {D} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} \sigma \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

（法二）由于所求极限的表达式中 i，j无关，故可以考虑将原极限写成定积分的乘积.由于<equation>\begin{aligned} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} &= \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) \\ \underline {{i , j \text {无关}}} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right), \end{aligned}</equation>故<equation>\begin{aligned} &= \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \cdot \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) = \left(\int_ {0} ^ {1} \frac {1}{1 + x} d x\right)\left(\int_ {0} ^ {1} \frac {1}{1 + y ^ {2}} d y\right) \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

---


### 一元函数微分学