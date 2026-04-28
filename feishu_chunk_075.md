#### 多元函数的极值问题

**2024年第18题 | 解答题 | 12分**

8. (本题满分12分)

已知函数<equation>f ( x, y )=x^{3}+y^{3}-( x+y )^{2}+3</equation>，设 T是曲面<equation>z=f(x,y)</equation>在点（1，1，1）处的切平面，D为T与坐标平面所围成的有界区域在 xOy面上的投影.

I. 求 T的方程；

II. 求 f(x,y)在 D上的最大值和最小值.

**答案:**(1)<equation>\varGamma</equation>的方程为<equation>x+y+z=3</equation>(2) 最大值<equation>f(3,0)=f(0,3)=21</equation>，最小值为<equation>f\left(\frac{4}{3},\frac{4}{3}\right)=\frac{17}{27}.</equation>

**解析:**解（I）记<equation>F ( x,y,z) = z - f ( x,y),</equation>，则<equation>F_{x}^{\prime}(x,y,z) = -3x^{2} + 2(x + y),\quad F_{y}^{\prime}(x,y,z) = -3y^{2} + 2(x + y),\quad F_{z}^{\prime}(x,y,z) = 1.</equation>代入<equation>x=1,y=1,z=1</equation>，可得<equation>F_{x}^{\prime}(1,1,1)=1, F_{y}^{\prime}(1,1,1)=1, F_{z}^{\prime}(1,1,1)=1.</equation>于是，曲面<equation>F(x,y,z)</equation><equation>= 0</equation>（即<equation>z = f(x,y)</equation>）在点（1,1,1）处的切平面T的点法式方程为<equation>(x - 1) + (y - 1) + (z - 1) = 0</equation>，即<equation>x + y + z = 3.</equation>（Ⅱ）T与坐标平面所围有界区域在 xOy面上的投影 D = {（x,y）| x+y≤3,x≥0,y≥0} .先求区域 D内部的驻点.

解<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=3x^{2}-2(x+y)=0,\\ f_{y}^{\prime}(x,y)=3y^{2}-2(x+y)=0,\end{array} \right.</equation>两式相减并整理可得<equation>x^{2}-y^{2}=0</equation>，解得 x=y或 x=-y. 由于 x≥0,y≥0，故在区域内部不可能有 x=-y.将 x=y代入<equation>3x^{2}-2(x+y)=0</equation>可得<equation>3x^{2}-4x</equation>=0，解得 x<equation>=\frac{4}{3}</equation>（舍去 x=0）.进一步可得驻点坐标为<equation>\left(\frac{4}{3},\frac{4}{3}\right).</equation>计算可得<equation>f \left(\frac {4}{3}, \frac {4}{3}\right) = 2 \cdot \left(\frac {4}{3}\right) ^ {3} - \left(\frac {8}{3}\right) ^ {2} + 3 = \frac {1 7}{2 7}.</equation>下面求边界上的最值.

（i）在边界<equation>y=0,0\leqslant x\leqslant 3</equation>上，<equation>f(x,y)=x^{3}-x^{2}+3.</equation>记<equation>\varphi(x)=x^{3}-x^{2}+3</equation>，则<equation>\varphi^{\prime}(x)=3x^{2}-2x=x(3x-2),x=\frac{2}{3}</equation>是<equation>\varphi(x)</equation>在（0,3）内的驻点，<equation>\varphi\left(\frac{2}{3}\right)=\left(\frac{2}{3}\right)^{3}-\left(\frac{2}{3}\right)^{2}+3=\frac{77}{27}.</equation>在端点 x=0和x=3处，<equation>\varphi(0)=3, \varphi(3)=21.</equation>（ii）在边界<equation>x=0,0\leqslant y\leqslant 3</equation>上，<equation>f(x,y)=y^{3}-y^{2}+3.</equation>最值情况与（i）相同.

（iii）在边界<equation>x + y = 3,0\leqslant x\leqslant 3</equation>上，<equation>f(x,y) = x^{3} + (3 - x)^{3} - 3^{2} + 3.</equation>记<equation>\psi(x)=x^{3}+(3-x)^{3}-6</equation>，则<equation>\psi^{\prime}(x)=3x^{2}-3(3-x)^{2}=18x-27=9(2x-3),x=\frac{3}{2}</equation>是<equation>\psi(x)</equation>在（0,3）内的驻点，<equation>\psi\left(\frac{3}{2}\right)=2\left(\frac{3}{2}\right)^{3}-6=\frac{3}{4}.</equation>在端点 x=0和x=3处，<equation>\psi(0)=21, \psi(3)=21.</equation>比较可得，<equation>f ( 3, 0 ) = f ( 0, 3 ) = 2 1</equation>是<equation>f ( x, y )</equation>在区域D上的最大值，<equation>f \left( \frac{4}{3}, \frac{4}{3} \right) = \frac{1 7}{2 7}</equation>是<equation>f ( x, y )</equation>在区域D上的最小值.

---

**2023年第18题 | 解答题 | 12分**

18. (本题满分12分)

求函数<equation>f ( x,y)=(y-x^{2})(y-x^{3})</equation>的极值.

**答案:**f(x,y)有极小值，极小值为<equation>f\left(\frac{2}{3},\frac{10}{27}\right)=-\frac{4}{729}.</equation>

**解析:**解<equation>\textcircled{1}</equation>计算 f(x,y)的驻点.<equation>\begin{aligned} f _ {x} ^ {\prime} (x, y) &= - 2 x \left(y - x ^ {3}\right) - 3 x ^ {2} \left(y - x ^ {2}\right) = 2 x ^ {4} - 2 x y + 3 x ^ {4} - 3 x ^ {2} y = 5 x ^ {4} - 3 x ^ {2} y - 2 x y \\ &= x \left(5 x ^ {3} - 3 x y - 2 y\right), \end{aligned}</equation><equation>f _ {y} ^ {\prime} (x, y) = y - x ^ {3} + y - x ^ {2} = 2 y - x ^ {3} - x ^ {2}.</equation>令<equation>\left\{\begin{array}{l l}x(5x^{3}-3xy-2y)=0,\\ 2y-x^{3}-x^{2}=0.\end{array} \right.</equation>由<equation>2y-x^{3}-x^{2}=0</equation>可得<equation>y=\frac{x^{2}(x+1)}{2}</equation>将<equation>y=\frac{x^{2}(x+1)}{2}</equation>代入<equation>x(5x^{3}-3xy-2y)=0</equation>可得<equation>x\left[5x^{3}-\frac{3x^{3}(x+1)}{2}-x^{2}(x+1)\right]=0.</equation>整理可得<equation>x^{3}(3x^{2}-5x+2)=</equation>0，即<equation>x^{3}(x-1)(3x-2)=0.</equation>解得<equation>x=0,x=1</equation>或<equation>x=\frac{2}{3}.</equation>由此可得f(x,y)的全部驻点为（0，0）， (1,1），<equation>\left(\frac{2}{3},\frac{10}{27}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 5 x ^ {3} - 3 x y - 2 y + x \left(1 5 x ^ {2} - 3 y\right) = 2 0 x ^ {3} - 6 x y - 2 y = 2 \left(1 0 x ^ {3} - 3 x y - y\right),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = x (- 3 x - 2) = - 3 x ^ {2} - 2 x,</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = 2.</equation><equation>\textcircled{3}</equation>计算<equation>AC-B^{2}.</equation>（i）对点（0,0），<equation>A=f_{xx}^{\prime \prime}(0,0)=0,B=f_{xy}^{\prime \prime}(0,0)=0,C=f_{yy}^{\prime \prime}(0,0)=2,AC-B^{2}=0.</equation>我们无法由二元函数极值存在的充分条件判断该点是否为极值点.

由<equation>f ( x,y )</equation>的表达式可知，<equation>f ( 0,0 )=0.</equation>取<equation>y=2 x^{2}</equation>，当x为充分小的正数时，<equation>f (x, y) = \left(2 x ^ {2} - x ^ {2}\right) \left(2 x ^ {2} - x ^ {3}\right) = x ^ {4} (2 - x) > 0.</equation>取<equation>y=2 x^{3}</equation>，当x为充分小的正数时，<equation>f (x, y) = \left(2 x ^ {3} - x ^ {2}\right) \left(2 x ^ {3} - x ^ {3}\right) = x ^ {5} (2 x - 1) < 0.</equation>因此，不论在点（0，0）的多么小的邻域内，均既有<equation>f ( x,y)>0</equation>的点，也有<equation>f ( x,y)<0</equation>的点.根据极值点的定义，点（0，0）不是<equation>f ( x,y)</equation>的极值点.

（ii）对点（1，1），<equation>A=f_{xx}^{\prime \prime}(1,1)=1 2, B=f_{xy}^{\prime \prime}(1,1)=-5, C=f_{yy}^{\prime \prime}(1,1)=2, A C-B^{2}=-1<</equation>0.由二元函数极值存在的充分条件可知，点（1，1）不是<equation>f(x,y)</equation>的极值点.

（iii）对点<equation>\left(\frac{2}{3},\frac{10}{27}\right),A=f_{xx}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=\frac{100}{27},B=f_{xy}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=-\frac{8}{3},C=f_{yy}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=2,</equation><equation>AC-B^{2}=\frac{8}{27}>0</equation>，且 A > 0.由二元函数极值存在的充分条件可知，点<equation>\left(\frac{2}{3},\frac{10}{27}\right)</equation>是 f(x,y)的极小值点.极小值为<equation>f \left(\frac {2}{3}, \frac {1 0}{2 7}\right) = \left(\frac {1 0}{2 7} - \frac {4}{9}\right) \times \left(\frac {1 0}{2 7} - \frac {8}{2 7}\right) = - \frac {4}{7 2 9}.</equation>

---

**2022年第13题 | 填空题 | 5分**

13. 当<equation>x \geqslant 0, y \geqslant 0</equation>时，<equation>x^{2}+y^{2} \leqslant k \mathrm{e}^{x+y}</equation>恒成立，则<equation>k</equation>的取值范围是 ___

**答案:**[<equation>4 \mathrm{e}^{-2},+\infty)</equation>.

**解析:**解不等式<equation>x^{2}+y^{2}\leqslant k \mathrm{e}^{x+y}</equation>等价于<equation>\left(x^{2}+y^{2}\right)\mathrm{e}^{-(x+y)}\leqslant k.</equation>记<equation>f(x,y) = (x^{2} + y^{2})\mathrm{e}^{-(x + y)}, D = \{(x,y) \mid x \geqslant 0, y \geqslant 0\}</equation>.

计算 f(x,y)在 D 内的驻点.<equation>f _ {x} ^ {\prime} (x, y) = 2 x \mathrm {e} ^ {- (x + y)} - \left(x ^ {2} + y ^ {2}\right) \mathrm {e} ^ {- (x + y)} = \left(2 x - x ^ {2} - y ^ {2}\right) \mathrm {e} ^ {- (x + y)},</equation><equation>f _ {y} ^ {\prime} (x, y) = 2 y \mathrm {e} ^ {- (x + y)} - \left(x ^ {2} + y ^ {2}\right) \mathrm {e} ^ {- (x + y)} = \left(2 y - x ^ {2} - y ^ {2}\right) \mathrm {e} ^ {- (x + y)}.</equation>解<equation>\left\{ \begin{array}{l} 2x - x^2 - y^2 = 0, \\ 2y - x^2 - y^2 = 0. \end{array} \right.</equation>两式相减得<equation>x = y</equation>，将<equation>x = y</equation>代入<equation>2x - x^2 - y^2 = 0</equation>可得<equation>2x - 2x^2 = 0</equation>，从而<equation>x = 0</equation>或<equation>x = 1.</equation><equation>\left\{ \begin{array}{l} x = 0, \\ y = 0 \end{array} \right.</equation>和<equation>\left\{ \begin{array}{l} x = 1, \\ y = 1 \end{array} \right.</equation>为该方程组的两组解.由于所求为区域D内部的驻点，故舍去点(0,0).点(1,1)为<equation>f(x,y)</equation>在区域D内部的唯一驻点.<equation>f(1,1) = 2\mathrm{e}^{-2}.</equation>下面计算<equation>f(x,y)</equation>在区域<equation>D</equation>的边界<equation>x = 0</equation>与<equation>y = 0</equation>上的最大值.

当<equation>x = 0</equation>时，<equation>f(0,y) = y^{2}\mathrm{e}^{-y}</equation>.记<equation>f_{1}(y) = y^{2}\mathrm{e}^{-y}</equation>，则<equation>f_{1}^{\prime}(y) = (2y - y^{2})\mathrm{e}^{-y}</equation>.解<equation>2y - y^{2} = 0</equation>得<equation>y = 0</equation>或<equation>y = 2</equation>.当<equation>0 < y < 2</equation>时，<equation>f_{1}^{\prime}(y) > 0</equation>，<equation>f_{1}(y)</equation>单调增加，当<equation>y > 2</equation>时，<equation>f_{1}^{\prime}(y) < 0</equation>，<equation>f_{1}(y)</equation>单调减少.于是，<equation>f(0,2) = 4\mathrm{e}^{-2}</equation>为<equation>f(x,y)</equation>在边界<equation>x = 0</equation>上的最大值.

同理可得，<equation>f ( 2, 0 ) = 4 \mathrm{e}^{-2}</equation>为<equation>f ( x,y )</equation>在边界<equation>y=0</equation>上的最大值.

比较<equation>f ( 1,1), f ( 0,2), f ( 2,0)</equation>可得，<equation>f ( 0,2)=f ( 2,0)=4 \mathrm{e}^{-2}</equation>为<equation>f ( x,y)</equation>在区域D上的最大值综上所述，<equation>k</equation>的取值范围为<equation>[ 4 \mathrm{e}^{-2},+\infty).</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分)

已知曲线 C：<equation>\left\{ \begin{array}{l l} x^{2}+2 y^{2}-z=6, \\ 4 x+2 y+z=3 0, \end{array} \right.</equation>求 C上的点到 xOy坐标面距离的最大值.

**答案:**## 最大值为66.

**解析:**解设目标函数为<equation>f ( x,y,z) = z^{2}.</equation>记<equation>\varphi ( x,y,z) = x^{2}+2 y^{2}-z-6,\psi ( x,y,z) = 4 x+2 y+z-3 0</equation>则约束条件为<equation>\varphi ( x,y,z) = 0,\psi ( x,y,z) = 0.</equation>建立拉格朗日函数<equation>L (x, y, z, \lambda , \mu) = z ^ {2} + \lambda \left(x ^ {2} + 2 y ^ {2} - z - 6\right) + \mu \left(4 x + 2 y + z - 3 0\right).</equation>对拉格朗日函数的各个变量分别求偏导，并令其为零，可得如下方程组.<equation>\left[ L _ {x} ^ {\prime} (x, y, z, \lambda , \mu) \right] = 2 \lambda x + 4 \mu = 0,</equation><equation>L _ {y} ^ {\prime} (x, y, z, \lambda , \mu) = 4 \lambda y + 2 \mu = 0,</equation><equation>L _ {z} ^ {\prime} (x, y, z, \lambda , \mu) = 2 z - \lambda + \mu = 0,</equation><equation>L _ {\lambda} ^ {\prime} (x, y, z, \lambda , \mu) = x ^ {2} + 2 y ^ {2} - z - 6 = 0,</equation><equation>L _ {\mu} ^ {\prime} (x, y, z, \lambda , \mu) = 4 x + 2 y + z - 3 0 = 0.</equation>(2) 式<equation>\times2-（1）</equation>式，并整理可得<equation>\lambda(4 y-x)=0.</equation>（i）若<equation>\lambda=0</equation>，则由（1）式，（2）式可得<equation>\mu=0</equation>，再由（3）式可得 z=0.此时，由（4）式，（5）式可得<equation>\left\{\begin{array}{l l}x^{2}+2 y^{2}=6\\2 x+y=1 5.\end{array}\right.</equation>椭圆<equation>x^{2}+2 y^{2}=6</equation>的长轴为x轴，短轴为y轴，长、短半轴长分别为<equation>\sqrt{6},\sqrt{3}</equation>，而直线<equation>2 x+y=1 5</equation>在x轴，y轴上的截距分别为<equation>\frac{1 5}{2}</equation>，15.从而直线<equation>2 x+y=1 5</equation>位于椭圆<equation>x^{2}+2 y^{2}=6</equation>上方，该方程无解.

（ii）若<equation>4 y - x = 0</equation>，则先由（4）式，（5）式消去变量<equation>z</equation>再代入该关系.

(4) 式 +（5）式可得<equation>x^{2}+4 x+2 y^{2}+2 y=3 6</equation>代入<equation>x=4 y</equation>可得，<equation>1 6 y^{2}+1 6 y+2 y^{2}+2 y=3 6</equation>整理可得<equation>y^{2}+y-2=0</equation>解得<equation>y=-2</equation>或<equation>y=1.</equation>当<equation>y = -2, x = -8</equation>时，由（5）式可得<equation>z = 66</equation>；当<equation>y = 1, x = 4</equation>时，由（5）式可得<equation>z = 12</equation>.

比较可得，在曲线 C上，点（-8，-2，66）到<equation>x O y</equation>面的距离最大，最大值为66.

---

**2020年第15题 | 解答题 | 10分**

15. (本题满分10分）

求函数<equation>f ( x,y)=x^{3}+8 y^{3}-x y</equation>的极值.

**答案:**<equation>\text {极 小 值} f \left(\frac {1}{6}, \frac {1}{1 2}\right) = - \frac {1}{2 1 6}.</equation>

**解析:**解<equation>\textcircled{1}</equation>计算 f(x,y)的驻点.

解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x⁴=x，解得x=0或x<equation>=\frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l l} x=0, \\ y=0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} x=\frac{1}{6}, \\ y=\frac{1}{12}. \end{array} \right.</equation><equation>f(x,y)</equation>有两个驻点(0,0)，<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f_{xx}^{\prime\prime}(x,y)=6x,</equation><equation>f_{xy}^{\prime\prime}(x,y)=-1,</equation><equation>f_{yy}^{\prime\prime}(x,y)=48y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

• 考虑驻点(0,0).<equation>A=f_{xx}^{\prime\prime}(0,0)=0,</equation><equation>B=f_{xy}^{\prime\prime}(0,0)=-1,</equation><equation>C=f_{yy}^{\prime\prime}(0,0)=0.</equation><equation>AC-B^{2}=0-1=-1<0</equation>，故点(0,0)不是极值点.

• 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A=f_{xx}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=1,</equation><equation>B=f_{xy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=-1,</equation><equation>C=f_{yy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A>0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=\frac{1}{6^{3}}+\frac{8}{12^{3}}-\frac{1}{6 \times 12}=-\frac{1}{216}.</equation>

---

**2018年第16题 | 解答题 | 10分**

16. (本题满分10分)

将长为 2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.

**答案:**三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

**解析:**解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长 a<equation>=\frac{y}{4}</equation>正三角形的边长 b<equation>=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L(x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda (x + y + z - 2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得<equation>x,y,z</equation>的值代入<equation>S(x,y,z)</equation>可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数<equation>S ( x, y, z )</equation>在有界闭区域<equation>D=\{(x,y,z)\mid x+y+z=2,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1}{\pi+4+3\sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值.

当<equation>x = 0</equation>时，<equation>S(0,y,z)</equation>在<equation>y + z = 2</equation>下的最小值为<equation>S\left(0,\frac{8}{4 + 3\sqrt{3}},\frac{6\sqrt{3}}{4 + 3\sqrt{3}}\right) = \frac{1}{4 + 3\sqrt{3}}.</equation>当<equation>y=0</equation>时，<equation>S ( x, 0, z )</equation>在<equation>x+z=2</equation>下的最小值为<equation>S \left( \frac{2 \pi}{\pi+3 \sqrt{3}}, 0, \frac{6 \sqrt{3}}{\pi+3 \sqrt{3}} \right)=\frac{1}{\pi+3 \sqrt{3}}.</equation>当<equation>z = 0</equation>时，<equation>S(x,y,0)</equation>在<equation>x + y = 2</equation>下的最小值为<equation>S\left(\frac{2\pi}{\pi + 4},\frac{8}{\pi + 4},0\right) = \frac{1}{\pi + 4}</equation>4个值比较可得，<equation>\frac{1}{\pi+4+3\sqrt{3}}</equation>为整个区域D上的最小值，也为<equation>x+y+z=2,x>0,y>0,z>0</equation>时的<equation>S(x,y,z)</equation>的最小值.三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

---

**2015年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数<equation>f ( x,y)=x+y+ x y</equation>，曲线 C：<equation>x^{2}+y^{2}+ x y=3</equation>，求 f(x,y)在曲线 C上的最大方向导数.

**解析:**解 由于函数在一点处的方向导数的最大值等于函数在该点的梯度的模，故求<equation>f ( x,y )</equation>在曲线 C上的最大方向导数等价于求<equation>f ( x,y )</equation>在曲线C上梯度的模的最大值.为了计算方便，考虑梯度模的平方函数.令<equation>g ( x,y ) = f_{x}^{\prime 2}+f_{y}^{\prime 2}=(1+y)^{2}+(1+x)^{2}</equation>，下面求<equation>g ( x,y )</equation>在条件<equation>x^{2}+y^{2}+xy=3</equation>下的最值.作拉格朗日函数<equation>L (x, y, \lambda) = (1 + y) ^ {2} + (1 + x) ^ {2} + \lambda \left(x ^ {2} + y ^ {2} + x y - 3\right).</equation>令<equation>\left[ L _ {x} ^ {\prime} = 2 (1 + x) + \lambda (2 x + y) = 0, \right.</equation><equation>\left\{L _ {y} ^ {\prime} = 2 (1 + y) + \lambda (2 y + x) = 0, \right.</equation><equation>L _ {\lambda} ^ {\prime} = x ^ {2} + y ^ {2} + x y - 3 = 0.</equation>由（1）、(2）消去<equation>\lambda</equation>得到<equation>(x - y)(x + y - 1) = 0</equation>，从而<equation>x = y</equation>或<equation>x + y = 1</equation>若 x = y，代入（3）式，解得 x = y =<equation>\pm 1</equation>；若 x+y=1，代入（3）式，解得 x=2，y=-1或 x=-1， y=2.于是（1，1），（-1，-1），（2，-1），（-1，2）都是可能的最值点.又<equation>g (1, 1) = 8, \quad g (- 1, - 1) = 0, \quad g (2, - 1) = g (- 1, 2) = 9,</equation>故<equation>g ( x,y )</equation>在条件<equation>x^{2}+y^{2}+xy=3</equation>下的最大值为9，从而<equation>f ( x,y )</equation>在曲线C上的最大方向导数为3.

---

**2013年第17题 | 解答题 | 10分**

17. (本题满分10分）

求函数<equation>f ( x,y)=\left(y+\frac{x^{3}}{3}\right)\mathrm{e}^{x+y}</equation>的极值.

**解析:**解 由题设知，<equation>f _ {x} ^ {\prime} (x, y) = x ^ {2} \mathrm {e} ^ {x + y} + \left(y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y} = \left(x ^ {2} + y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {y} ^ {\prime} (x, y) = \mathrm {e} ^ {x + y} + \left(y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y} = \left(1 + y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y}.</equation>令<equation>\left\{ \begin{array}{l} f_x^{\prime}(x,y) = 0, \\ f_y^{\prime}(x,y) = 0, \end{array} \right.</equation>即<equation>\left\{ \begin{array}{l} x^{2} + y + \frac{x^{3}}{3} = 0, \\ 1 + y + \frac{x^{3}}{3} = 0, \end{array} \right.</equation>解得驻点为<equation>\left(1, - \frac{4}{3}\right), \left(-1, - \frac{2}{3}\right).</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + 2 x ^ {2} + 2 x + y\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {x y} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + x ^ {2} + y + 1\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {y y} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + y + 2\right) \mathrm {e} ^ {x + y}.</equation>在驻点<equation>\left( 1,-\frac{4}{3} \right)</equation>处，<equation>A = f _ {x x} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = 3 \mathrm {e} ^ {- \frac {1}{3}}, \quad B = f _ {x y} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = \mathrm {e} ^ {- \frac {1}{3}}, \quad C = f _ {y y} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = \mathrm {e} ^ {- \frac {1}{3}},</equation>于是<equation>AC - B^{2} = 2\mathrm{e}^{-\frac{2}{3}} > 0,A > 0</equation>，故点<equation>\left(1, - \frac{4}{3}\right)</equation>为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f\left(1, - \frac{4}{3}\right) = -\mathrm{e}^{-\frac{1}{3}}.</equation>在驻点<equation>\left(-1,-\frac{2}{3}\right)</equation>处，<equation>A = f _ {x x} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = - \mathrm {e} ^ {- \frac {5}{3}}, \quad B = f _ {x y} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = \mathrm {e} ^ {- \frac {5}{3}}, \quad C = f _ {y y} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = \mathrm {e} ^ {- \frac {5}{3}},</equation>于是<equation>AC-B^{2}=-2\mathrm{e}^{-\frac{10}{3}}<0</equation>，故点<equation>\left(-1,-\frac{2}{3}\right)</equation>不是极值点.

综上所述，<equation>f ( x,y)</equation>只在点<equation>\left( 1,-\frac{4}{3} \right)</equation>处取得极值<equation>f\left( 1,-\frac{4}{3}\right)=-\mathrm{e}^{-\frac{1}{3}}</equation>，且为极小值.

---

**2012年第16题 | 解答题 | 10分**

16. (本题满分10分）

求函数<equation>f ( x,y)=x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极值.

**答案:**(16) 极大值<equation>f(1,0) = \mathrm{e}^{-\frac{1}{2}}</equation>，极小值<equation>f(-1,0) = -\mathrm{e}^{-\frac{1}{2}}.</equation>

**解析:**解<equation>\textcircled{1}</equation>先找到 f(x,y)的全部驻点.

记<equation>g ( x,y) = \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}.</equation>由于<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = \left(1 - x ^ {2}\right) g (x, y),</equation><equation>f _ {y} ^ {\prime} (x, y) = - x y \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = (- x y) g (x, y).</equation>由于 g(x,y) > 0，故满足<equation>\left\{\begin{array}{l l}1-x^{2}=0\\-xy=0\end{array}\right.</equation>的点（x，y）为 f(x，y）的驻点.解该方程组得（x，y）= （<equation>\pm1,0).</equation>因此，点（1，0）和点（-1，0）为<equation>f ( x,y)</equation>的全部驻点.<equation>\textcircled{2}</equation>计算二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (- 2 x) g (x, y) + \left(1 - x ^ {2}\right) g _ {x} ^ {\prime} (x, y),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = \left(1 - x ^ {2}\right) g _ {y} ^ {\prime} (x, y),</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = (- x) g (x, y) + (- x y) g _ {y} ^ {\prime} (x, y).</equation><equation>\textcircled{3}</equation>计算<equation>A C-B^{2}.</equation>由于<equation>f(x,y)</equation>的驻点<equation>(x_0,y_0)</equation>均满足<equation>1 - x_0^2 = 0, - x_0y_0 = 0</equation>，而<equation>g(x,y)</equation>恒大于零，故在驻点 (1,0) 处，<equation>f_{xx}^{\prime \prime}(1,0) = -2g(1,0) < 0, f_{xy}^{\prime \prime}(1,0) = 0, f_{yy}^{\prime \prime}(1,0) = -g(1,0)</equation>.因此，<equation>f _ {x x} ^ {\prime \prime} (1, 0) f _ {y y} ^ {\prime \prime} (1, 0) - \left[ f _ {x y} ^ {\prime \prime} (1, 0) \right] ^ {2} = 2 g ^ {2} (1, 0) > 0.</equation>由于<equation>f_{xx}^{\prime \prime}(1,0)=-2 g(1,0)<0</equation>，故点（1，0）为<equation>f(x,y)</equation>的极大值点，<equation>f(1,0)=\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极大值.同理可得，点（-1，0）为<equation>f(x,y)</equation>的极小值点，<equation>f(-1,0)=-\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极小值.

因此，函数<equation>f ( x,y) = x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极大值为<equation>\mathrm{e}^{- \frac{1}{2}}</equation>，极小值为<equation>- \mathrm{e}^{- \frac{1}{2}}.</equation>

---

**2011年第3题 | 选择题 | 4分 | 答案: A**

3. 设函数 f(x)具有二阶连续导数，且 f(x) > 0，<equation>f^{\prime}(0)=0</equation>，则函数 z=f(x)<equation>\ln f(y)</equation>在点 (0,0)处取得极小值的一个充分条件是（    ）

A.<equation>f(0)>1,f^{\prime\prime}(0)>0</equation>B.<equation>f(0)>1,f^{\prime\prime}(0)<0</equation>C.<equation>f(0)<1,f^{\prime\prime}(0)>0</equation>D.<equation>f(0)<1,f^{\prime\prime}(0)<0</equation>

答案: A

**解析:**由题设知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = f ^ {\prime} (x) \ln f (y) \Big | _ {(0, 0)} = f ^ {\prime} (0) \ln f (0) = 0,</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = \frac {f (x) f ^ {\prime} (y)}{f (y)} \Bigg | _ {(0, 0)} = \frac {f (0) f ^ {\prime} (0)}{f (0)} = 0.</equation>从而点（0，0）为函数<equation>z ( x,y)</equation>的驻点.又<equation>A = \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(0, 0)} = f ^ {\prime \prime} (x) \ln f (y) \Big | _ {(0, 0)} = f ^ {\prime \prime} (0) \ln f (0),</equation><equation>B = \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(0, 0)} = \left. \frac {f ^ {\prime} (x) f ^ {\prime} (y)}{f (y)} \right| _ {(0, 0)} = \frac {f ^ {\prime} (0) f ^ {\prime} (0)}{f (0)} = 0,</equation><equation>C = \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(0, 0)} = f (x) \cdot \frac {f ^ {\prime \prime} (y) f (y) - \left[ f ^ {\prime} (y) \right] ^ {2}}{f ^ {2} (y)} \Bigg | _ {(0, 0)} = \frac {f ^ {2} (0) f ^ {\prime \prime} (0) - f (0) \left[ f ^ {\prime} (0) \right] ^ {2}}{f ^ {2} (0)} = f ^ {\prime \prime} (0).</equation>令<equation>A=f^{\prime \prime}(0)\ln f(0)>0, A C-B^{2}=[f^{\prime \prime}(0)]^{2}\ln f(0)>0</equation>，解得<equation>f(0)>1,f^{\prime \prime}(0)>0.</equation>因此，<equation>f(0)>1,f^{\prime \prime}(0)>0</equation>为函数<equation>z(x,y)</equation>在点（0,0）处取得极小值的一个充分条件.应选A.

---

**2009年第15题 | 解答题 | 10分**

15. (本题满分9分）

求二元函数<equation>f ( x,y)=x^{2}\left( 2+y^{2}\right)+y\ln y</equation>的极值.

**答案:**(15) 极小值<equation>f\left(0,\frac{1}{\mathrm{e}}\right) = -\frac{1}{\mathrm{e}}.</equation>

**解析:**解 令<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=2 x(2+y^{2})=0,\\ f_{y}^{\prime}(x,y)=2 x^{2} y+\ln y+1=0,\end{array} \right.</equation>解得驻点为<equation>\left(0,\frac{1}{e}\right).</equation>f(x,y)的二阶偏导数为<equation>f_{xx}^{\prime \prime}(x,y)=2(2+y^{2}),</equation><equation>f_{xy}^{\prime \prime}(x,y)=4 x y,</equation><equation>f_{yy}^{\prime \prime}(x,y)=2 x^{2}+\frac{1}{y},</equation>于是<equation>A=f_{xx}^{\prime \prime}\left(0,\frac{1}{e}\right)=2\left(2+\frac{1}{e^{2}}\right),</equation><equation>B=f_{xy}^{\prime \prime}\left(0,\frac{1}{e}\right)=0,</equation><equation>C=f_{yy}^{\prime \prime}\left(0,\frac{1}{e}\right)=\mathrm{e}.</equation>由于<equation>AC-B^{2}>0,</equation><equation>A>0</equation>，故f(x,y)在<equation>\left(0,\frac{1}{e}\right)</equation>处取得极小值<equation>f\left(0,\frac{1}{e}\right)=-\frac{1}{e}.</equation>

---


