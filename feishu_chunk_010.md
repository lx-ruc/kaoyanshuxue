当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A ^ {\mathrm {T}} A = \left( \begin{array}{c c c} 4 & 0 & - 2 \\ 0 & 4 & - 2 \\ - 2 & - 2 & 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & 1 & - 1 \end{array} \right) \xrightarrow {r _ {3} - r _ {2}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 0 & 2 & - 1 \\ 1 & - 1 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - r _ {1} + 2 r _ {3} ^ {*}} \frac {1}{r _ {2} ^ {*} \leftrightarrow r _ {3} ^ {*}} \left( \begin{array}{c c c} 2 & 0 & - 1 \\ 1 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right), \\ \end{array}</equation>得<equation>\left\{ \begin{array}{l} 2x_{1} - x_{3} = 0, \\ x_{1} - x_{2} = 0. \end{array} \right.</equation>解得<equation>\xi_{1} = (1,1,2)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

当<equation>\lambda=2</equation>时，<equation>2 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} 0 & 0 & - 2 \\ 0 & 0 & - 2 \\ - 2 & - 2 & - 2 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l l} x_{1} + x_{2} = 0, \\ x_{3} = 0. \end{array} \right.</equation>解得<equation>\xi_{2} = (-1,1,0)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

当<equation>\lambda=0</equation>时，<equation>0 \boldsymbol {E} - \boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c} - 2 & 0 & - 2 \\ 0 & - 2 & - 2 \\ - 2 & - 2 & - 4 \end{array} \right) \rightarrow \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right) \xrightarrow {r _ {3} - r _ {1} - r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right),</equation>得<equation>\left\{ \begin{array}{l l} x_{1} + x_{3} = 0, \\ x_{2} + x_{3} = 0. \end{array} \right.</equation>解得<equation>\xi_{3} = (-1, -1, 1)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

由于实对称矩阵属于不同特征值的特征向量相互正交，故<equation>\xi_{1},\xi_{2},\xi_{3}</equation>相互正交.将<equation>\xi_{1},\xi_{2},\xi_{3}</equation>单位化，得<equation>\boldsymbol {\alpha} _ {1} = \frac {1}{\sqrt {6}} \left( \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right), \quad \boldsymbol {\alpha} _ {2} = \frac {1}{\sqrt {2}} \left( \begin{array}{c} - 1 \\ 1 \\ 0 \end{array} \right), \quad \boldsymbol {\alpha} _ {3} = \frac {1}{\sqrt {3}} \left( \begin{array}{c} - 1 \\ - 1 \\ 1 \end{array} \right).</equation>取<equation>Q = \left(\alpha_{1},\alpha_{2},\alpha_{3}\right)</equation>，则<equation>Q</equation>为正交矩阵，且<equation>Q^{\mathrm{T}} \left(A^{\mathrm{T}} A\right) Q = \left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，正交变换<equation>x = Qy</equation>将二次型<equation>f\left(x_{1}, x_{2}, x_{3}\right)</equation>变成标准形<equation>f = 6y_{1}^{2} + 2y_{2}^{2}</equation>.

---

**2011年第14题 | 填空题 | 4分**

14. 二次型<equation>f(x_{1},x_{2},x_{3})=x_{1}^{2}+3x_{2}^{2}+x_{3}^{2}+2x_{1}x_{2}+2x_{1}x_{3}+2x_{2}x_{3}</equation>, 则 f的正惯性指数为 ___

**解析:**解（法一）二次型<equation>f</equation>对应的对称矩阵<equation>A = \left( \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 1 \end{array} \right).</equation>计算 A的特征多项式得，<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 1 & - 1 & - 1 \\ - 1 & \lambda - 3 & - 1 \\ - 1 & - 1 & \lambda - 1 \end{array} \right| = \lambda (\lambda - 1) (\lambda - 4).</equation>A的特征值为0，1，4，其中正特征值的个数为2.

因此，<equation>f</equation>的正惯性指数为2.

（法二）配方法.

若对完全平方式<equation>\left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} = x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 2 x _ {2} x _ {3}</equation>较熟悉，则能够较快地写出<equation>f</equation>的标准形.<equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = x _ {1} ^ {2} + 3 x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {1} x _ {2} + 2 x _ {1} x _ {3} + 2 x _ {2} x _ {3} = \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} + 2 x _ {2} ^ {2}.</equation>或者如下计算.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= x _ {1} ^ {2} + 2 x _ {1} \left(x _ {2} + x _ {3}\right) + \left(x _ {2} + x _ {3}\right) ^ {2} + 3 x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {2} x _ {3} - \left(x _ {2} + x _ {3}\right) ^ {2} \\ &= \left(x _ {1} + x _ {2} + x _ {3}\right) ^ {2} + 2 x _ {2} ^ {2}. \end{aligned}</equation>因此，<equation>f</equation>的正惯性指数为2.

---

**2009年第23题 | 解答题 | 11分**

3. (本题满分11分)

设二次型<equation>f ( x_{1}, x_{2}, x_{3} )=a x_{1}^{2}+a x_{2}^{2}+( a-1 ) x_{3}^{2}+2 x_{1} x_{3}-2 x_{2} x_{3}</equation>.

I. 求二次型 f的矩阵的所有特征值；

II. 若二次型 f的规范形为<equation>y_{1}^{2}+y_{2}^{2}</equation>，求 a的值.

**答案:**(23) ( I ) a, a-2, a+1;

( II ) a=2.

**解析:**解（I）二次型<equation>f</equation>的矩阵为<equation>A = \left( \begin{array}{c c c} a & 0 & 1 \\ 0 & a & -1 \\ 1 & -1 & a - 1 \end{array} \right).</equation>计算<equation>A</equation>的特征多项式<equation>|\lambda E - A|</equation>，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ 0 & \lambda - a & 1 \\ - 1 & 1 & \lambda - a + 1  \right| \xlongequal {\text {按 第一 行 展 开}} (\lambda - a) \left[ (\lambda - a) (\lambda - a + 1) - 1 \right] - (\lambda - a) \\ &= (\lambda - a) (\lambda - a + 2) (\lambda - a - 1). \end{aligned}</equation>因此，<equation>A</equation>的特征值为<equation>a, a - 2, a + 1.</equation>（Ⅱ）由<equation>f</equation>的规范形为<equation>y_{1}^{2} + y_{2}^{2}</equation>知，<equation>A</equation>的特征值有两个正数，一个为零.0为最小的特征值.

由于<equation>a - 2 < a < a + 1</equation>，故可知<equation>a - 2 = 0</equation>，即<equation>a = 2</equation>

---


### 行列式

**2021年第16题 | 填空题 | 5分**
16. 多项式 f(x) =<equation>\left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & x & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>的<equation>x^{3}</equation>项的系数为 ___
**解析: **解 由于所给行列式的元素均为常数或 x的倍数，故根据行列式的定义，要出现<equation>x^{3}</equation>项，必须从不同行、不同列中取出3个含 x的项相乘.

将行列式记为<equation>\det ( a_{ij} ).</equation><equation>\textcircled{1} a_{11}=x</equation>不能取.若取<equation>a_{11}</equation>，则第一行中的 x与 2x不能取.于是，剩下的2个含 x的元素必来自主对角线上的3个x.无论从<equation>a_{22},a_{33},a_{44}</equation>中取哪两个，第四个元素都只能来自主对角线，从而这种取法最终将得到<equation>x^{4}</equation>，而不是<equation>x^{3}.</equation><equation>\left| \begin{array}{c c c c} \underline {{x}} & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|</equation><equation>\textcircled{2}</equation>由于<equation>x^{3}</equation>项必来自于不同列的含x元素的乘积，故确定<equation>a_{11}</equation>不取后，x必来自后三列，而第三列中仅<equation>a_{33}=x</equation>，从而必取.

下面分情况讨论.

(1) 若第二列中取<equation>a_{12}=x</equation>，则组合应为<equation>a_{12}a_{21}a_{33}a_{44}</equation>.该组合对应排列2，1，3，4，逆序数为1.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{1}\cdot1\cdot x^{3}=-x^{3}.</equation>(2) 若第二列中取<equation>a_{22}=x</equation>，则组合应为<equation>a_{14}a_{22}a_{33}a_{41}</equation>.该组合对应排列4，2，3，1，逆序数为5.于是，所得<equation>x^{3}</equation>项为<equation>(-1)^{5}\cdot 2\cdot 2x^{3}=-4x^{3}.</equation><equation>\left| \begin{array}{c c c c} x & \underline {{x}} & 1 & 2 x \\ 1 & x & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & \underline {{x}} \end{array} \right|, \quad \left| \begin{array}{c c c c} x & x & 1 & 2 x \\ 1 & \underline {{x}} & 2 & - 1 \\ 2 & 1 & \underline {{x}} & 1 \\ 2 & - 1 & 1 & x \end{array} \right|</equation>因此，<equation>f ( x )</equation>的<equation>x^{3}</equation>项为<equation>- x^{3}-4 x^{3}=-5 x^{3}, x^{3}</equation>的系数为-5.

---

**2020年第14题 | 填空题 | 4分**
14. 行列式<equation>\left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| = \underline {{\quad}}</equation>
**答案: **<equation>a^{4}-4 a^{2}.</equation>
**解析: **解（法一）利用行列式的性质对所求行列式进行转化.

若 a=0 ，则将第二行加到第一行可得零行，从而行列式为0.

若 a≠0，则<equation>\begin{aligned} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a  \right| \frac {r _ {4} + r _ {3}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 0 & 0 & a & a  \right| \frac {r _ {3} + \frac {1}{a} r _ {1}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 1 & a - \frac {1}{a} & \frac {1}{a} \\ 0 & 0 & a & a  \right| \\ \frac {r _ {3} - \frac {1}{a} r _ {2}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ 0 & 0 & a - \frac {2}{a} & \frac {2}{a} \\ 0 & 0 & a & a  \right| &= \left| \begin{array}{c c} a & 0 \\ 0 & a  \right| \cdot \left| \begin{array}{c c} a - \frac {2}{a} & \frac {2}{a} \\ a & a  \right| \\ &= a ^ {2} \left[ \left(a - \frac {2}{a}\right) a - 2 \right] = a ^ {2} \left(a ^ {2} - 4\right) = a ^ {4} - 4 a ^ {2}. \end{aligned}</equation>不论是哪种情况，所求行列式均为<equation>a^{4}-4 a^{2}.</equation>（法二）注意到所求行列式的各行元素之和均为 a，故可将各列均加到第1列，然后计算行列式.<equation>\begin{array}{l} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ 0 & a & 1 & - 1 \\ - 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \frac {c _ {1} + c _ {2} + c _ {3} + c _ {4}}{\hline} \left| \begin{array}{c c c c} a & 0 & - 1 & 1 \\ a & a & 1 & - 1 \\ a & 1 & a & 0 \\ a & - 1 & 0 & a \end{array} \right| = a \left| \begin{array}{c c c c} 1 & 0 & - 1 & 1 \\ 1 & a & 1 & - 1 \\ 1 & 1 & a & 0 \\ 1 & - 1 & 0 & a \end{array} \right| \\ \frac {c _ {3} + c _ {1}}{c _ {4} - c _ {1}} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 2 & - 2 \\ 1 & 1 & a + 1 & - 1 \\ 1 & - 1 & 1 & a - 1 \end{array} \right| \frac {c _ {3} + c _ {4}}{\hline} a \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 1 & a & 0 & - 2 \\ 1 & 1 & a & - 1 \\ 1 & - 1 & a & a - 1 \end{array} \right| \\ \frac {\mathrm {按 第一 行 展开}}{\mathrm {=} a ^ {4} - 4 a ^ {2}} a \left\{a \left[ a (a - 1) + a \right] - 2 (a + a) \right\} = a \left(a ^ {3} - 4 a\right) \\ \end{array}</equation>

---

**2019年第14题 | 填空题 | 4分**
14. 已知矩阵<equation>A=\left( \begin{array}{c c c c} 1 & -1 & 0 & 0 \\ -2 & 1 & -1 & 1 \\ 3 & -2 & 2 & -1 \\ 0 & 0 & 3 & 4 \end{array} \right), A_{ij}</equation>表示<equation>|A|</equation>中（i,j）元的代数余子式，则<equation>A_{11}-A_{12}=</equation>___
**答案: **-4.
**解析: **按 A的第一行展开计算<equation>|A|</equation>，可得<equation>| \boldsymbol {A} | = 1 \cdot A _ {1 1} + (- 1) \cdot A _ {1 2} = A _ {1 1} - A _ {1 2}.</equation>因此，<equation>\begin{aligned} A _ {1 1} - A _ {1 2} &= | A | = \left| \begin{array}{c c c c} 1 & - 1 & 0 & 0 \\ - 2 & 1 & - 1 & 1 \\ 3 & - 2 & 2 & - 1 \\ 0 & 0 & 3 & 4  \right| \underline {{\frac {c _ {2} + c _ {1}}{2}}} \left| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ - 2 & - 1 & - 1 & 1 \\ 3 & 1 & 2 & - 1 \\ 0 & 0 & 3 & 4  \right| \\ &= 1 \cdot \left| \begin{array}{c c c} - 1 & - 1 & 1 \\ 1 & 2 & - 1 \\ 0 & 3 & 4  \right| \underline {{\frac {c _ {3} + c _ {1}}{2}}} \left| \begin{array}{c c c} - 1 & - 1 & 0 \\ 1 & 2 & 0 \\ 0 & 3 & 4  \right| \end{aligned}</equation><equation>\frac {\mathrm {按 第三 列 展 开}}{2} 4 \cdot \left| \begin{array}{c c} - 1 & - 1 \\ 1 & 2 \end{array} \right| = - 4.</equation>

---

**2014年第7题 | 选择题 | 4分 | 答案: B**
7. 行列式<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right|=</equation>(    )

A.<equation>( a d-b c )^{2}</equation>B.<equation>-( a d-b c )^{2}</equation>C.<equation>a^{2} d^{2}-b^{2} c^{2}</equation>D.<equation>b^{2} c^{2}-a^{2} d^{2}</equation>
答案: B
**解析: **解（法一）将原行列式作初等变换使之与分块对角矩阵的行列式建立联系.根据行列式的性质，交换两行或两列，所得新行列式为原行列式的负值.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} 0 & a & b & 0 \\ 0 & c & d & 0 \\ a & 0 & 0 & b \\ c & 0 & 0 & d \end{array} \right| = \left| \begin{array}{c c c c} a & 0 & b & 0 \\ c & 0 & d & 0 \\ 0 & a & 0 & b \\ 0 & c & 0 & d \end{array} \right| = - \left| \begin{array}{c c c c} a & b & 0 & 0 \\ c & d & 0 & 0 \\ 0 & 0 & a & b \\ 0 & 0 & c & d \end{array} \right| = - (a d - b c) ^ {2}.</equation>应选B.

（法二）按第一行展开.<equation>\left| \begin{array}{c c c c} 0 & a & b & 0 \\ a & 0 & 0 & b \\ 0 & c & d & 0 \\ c & 0 & 0 & d \end{array} \right| = (- a) \left| \begin{array}{c c c} a & 0 & b \\ 0 & d & 0 \\ c & 0 & d \end{array} \right| + b \left| \begin{array}{c c c} a & 0 & b \\ 0 & c & 0 \\ c & 0 & d \end{array} \right| = - a ^ {2} d ^ {2} + a b c d + a b c d - b ^ {2} c ^ {2} = - (a d - b c) ^ {2}.</equation>应选B.

---


**2023年第20题 | 解答题 | 12分**

设平面有界区域 D位于第一象限，由曲线<equation>x^{2}+y^{2}-xy=1, x^{2}+y^{2}-xy=2</equation>与直线<equation>y=\sqrt{3} x, y=0</equation>围成，计算<equation>\iint_{D} \frac{1}{3 x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **##<equation>\frac{\sqrt{3}\pi\ln 2}{24}.</equation>
**解析: **20 设平面有界区域 D位于第一象限，由曲线<equation>x^{2}+y^{2}-xy=1, x^{2}+y^{2}-xy=2</equation>与直线<equation>y=\sqrt{3} x</equation>y=0围成，计算<equation>\iint_{D}\frac{1}{3x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y.</equation>分析 本题主要考查二重积分的计算.

根据区域的特点，我们可以在极坐标系下计算二重积分.

解 在极坐标系下计算.

由<equation>\left\{ \begin{array}{l l} x=r\cos \theta \\ y=r\sin \theta \end{array} \right.</equation>可知，曲线<equation>x^{2}+y^{2}-xy=1, x^{2}+y^{2}-xy=2</equation>的极坐标方程分别为<equation>r ^ {2} - r ^ {2} \sin \theta \cos \theta = 1, \quad r ^ {2} - r ^ {2} \sin \theta \cos \theta = 2,</equation>即<equation>r=\frac{1}{\sqrt{1-\sin \theta}\cos \theta}, r=\frac{\sqrt{2}}{\sqrt{1-\sin \theta}\cos \theta}</equation>. 直线 y=<equation>\sqrt{3} x</equation>的极坐标方程为<equation>\theta=\frac{\pi}{3}</equation>. 于是，区域 D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {1 - \sin \theta \cos \theta}} \leqslant r \leqslant \frac {\sqrt {2}}{\sqrt {1 - \sin \theta \cos \theta}}, 0 \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {1}{3 x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r \mathrm {d} r \mathrm {d} \theta}{3 r ^ {2} \cos^ {2} \theta + r ^ {2} \sin^ {2} \theta} &= \int_ {0} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {1 - \sin \theta} \cos \theta}} ^ {\frac {\sqrt {2}}{\sqrt {1 - \sin \theta} \cos \theta}} \frac {r \mathrm {d} r}{3 r ^ {2} \cos^ {2} \theta + r ^ {2} \sin^ {2} \theta} \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {1}{3 \cos^ {2} \theta + \sin^ {2} \theta} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {1 - \sin \theta} \cos \theta}} ^ {\frac {\sqrt {2}}{\sqrt {1 - \sin \theta} \cos \theta}} \frac {\mathrm {d} \left(r ^ {2}\right)}{r ^ {2}} \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {1}{3 \cos^ {2} \theta + \sin^ {2} \theta} \cdot \ln r ^ {2} \left| \frac {\frac {\sqrt {2}}{\sqrt {1 - \sin \theta} \cos \theta}}{\frac {1}{\sqrt {1 - \sin \theta} \cos \theta}} \right| \mathrm {d} \theta = \frac {\ln 2}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {\mathrm {d} \theta}{\cos^ {2} \theta \left(3 + \tan^ {2} \theta\right)} \\ &= \frac {\ln 2}{2} \int_ {0} ^ {\frac {\pi}{3}} \frac {\mathrm {d} (\tan \theta)}{3 + \tan^ {2} \theta} \frac {t = \tan \theta}{2} \frac {\ln 2}{2} \int_ {0} ^ {\sqrt {3}} \frac {\mathrm {d} t}{3 + t ^ {2}} = \frac {\ln 2}{2 \sqrt {3}} \int_ {0} ^ {\sqrt {3}} \frac {\mathrm {d} \left(\frac {t}{\sqrt {3}}\right)}{1 + \left(\frac {t}{\sqrt {3}}\right) ^ {2}} \\ &= \frac {\sqrt {3} \ln 2}{6} \arctan \frac {t}{\sqrt {3}} \Bigg | _ {0} ^ {\sqrt {3}} = \frac {\sqrt {3} \ln 2}{6} \cdot \frac {\pi}{4} = \frac {\sqrt {3} \pi \ln 2}{2 4}. \end{aligned}</equation>

---

**2022年第19题 | 解答题 | 12分**
19. (本题满分12分）

已知平面区域 D = {（x,y）| y-2≤x≤<equation>\sqrt{4-y^{2}}</equation>, 0≤y≤2} ，计算 I =<equation>\iint_{D} \frac{(x-y)^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **## I = 2<equation>\pi</equation>- 2.
**解析: **## 解 在极坐标系下计算.

由 D的表达式可知，如图（a）所示，D是由直线<equation>y=x+2</equation>，圆<equation>x^{2}+y^{2}=4</equation>以及x轴围成的部分直线<equation>y=x+2</equation>在极坐标系下的表示为<equation>r=\frac{2}{\sin \theta -\cos \theta}</equation>，圆<equation>x^{2}+y^{2}=4</equation>在极坐标系下的表示为<equation>r=2.</equation>(a)

(b)

如图（b）所示，将<equation>D</equation>分为两部分<equation>D_{1}</equation>和<equation>D_{2}</equation>.<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2, 0 \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>D _ {2} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {2}{\sin \theta - \cos \theta}, \frac {\pi}{2} \leqslant \theta \leqslant \pi \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {\left(x - y\right) ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r ^ {2} \left(\cos \theta - \sin \theta\right) ^ {2}}{r ^ {2}} \cdot r \mathrm {d} r \mathrm {d} \theta &= \iint_ {D} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot r \mathrm {d} r \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {2} r \mathrm {d} r + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \mathrm {d} \theta \int_ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} r \mathrm {d} r \\ &= 2 \int_ {0} ^ {\frac {\pi}{2}} \left(1 - 2 \sin \theta \cos \theta\right) \mathrm {d} \theta + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {r ^ {2}}{2} \Bigg | _ {0} ^ {\frac {2}{\sin \theta - \cos \theta}} \mathrm {d} \theta \\ &= 2 \left(\frac {\pi}{2} - \sin^ {2} \theta \Bigg | _ {0} ^ {\frac {\pi}{2}}\right) + \int_ {\frac {\pi}{2}} ^ {\pi} \left(\cos \theta - \sin \theta\right) ^ {2} \cdot \frac {2}{\left(\sin \theta - \cos \theta\right) ^ {2}} \mathrm {d} \theta \\ &= \pi - 2 + 2 \times \left(\pi - \frac {\pi}{2}\right) = 2 \pi - 2. \end{aligned}</equation>

---

**2021年第21题 | 解答题 | 12分**
21. (本题满分12分)

曲线<equation>( x^{2}+y^{2} )^{2}=x^{2}-y^{2}</equation><equation>( x \geqslant0,y \geqslant0)</equation>与 x轴围成的区域为 D，求<equation>\iint_{D} xy\mathrm{d}x\mathrm{d}y.</equation>
**答案: **# 1 48
**解析: **解曲线<equation>( x^{2}+y^{2})^{2}=x^{2}-y^{2}</equation>（<equation>x\geqslant0,y\geqslant0</equation>）与 x轴围成的区域 D如图所示.

写出曲线<equation>( x^{2}+y^{2})^{2}=x^{2}-y^{2}</equation>的极坐标方程.将 x = rcos<equation>\theta</equation>，y = rsin<equation>\theta</equation>代入<equation>( x^{2}+y^{2})^{2}=x^{2}-y^{2}</equation>可得，<equation>r^{4}=r^{2}\cos 2\theta</equation>，即<equation>r^{2}=\cos 2\theta</equation>.于是，区域D的极坐标表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sqrt {\cos 2 \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} x y \mathrm {d} x \mathrm {d} y \xlongequal {\text {极 坐 标}} \iint_ {D} r \cos \theta \cdot r \sin \theta \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{4}} \sin \theta \cos \theta \mathrm {d} \theta \int_ {0} ^ {\sqrt {\cos 2 \theta}} r ^ {3} \mathrm {d} r \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\pi}{4}} \sin 2 \theta \cdot \frac {r ^ {4}}{4} \Bigg | _ {0} ^ {\sqrt {\cos 2 \theta}} \mathrm {d} \theta = \frac {1}{8} \int_ {0} ^ {\frac {\pi}{4}} \sin 2 \theta \cdot \cos^ {2} 2 \theta \mathrm {d} \theta \\ &= - \frac {1}{1 6} \int_ {0} ^ {\frac {\pi}{4}} \cos^ {2} 2 \theta \mathrm {d} (\cos 2 \theta) = - \frac {1}{1 6} \cdot \frac {\cos^ {3} 2 \theta}{3} \Bigg | _ {0} ^ {\frac {\pi}{4}} \\ &= - \frac {1}{1 6} \times \left(0 - \frac {1}{3}\right) = \frac {1}{4 8}. \end{aligned}</equation>

---

**2020年第19题 | 解答题 | 10分**
19. (本题满分10分)

设平面区域 D由直线 x=1，x=2，y=x与 x轴围成，计算
**答案: **##<equation>\frac{3}{4}[\sqrt{2}+\ln(\sqrt{2}+1)]。</equation>
**解析: **分析 本题主要考查二重积分的计算.

本题中的平面区域虽然由直线围成，但根据被积函数的特点（含<equation>\sqrt{x^{2}+y^{2}}</equation>），可以考虑在极坐标系下计算.

解 根据已知条件，区域 D在直角坐标系下的表示为<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x, 1 \leqslant x \leqslant 2 \right\}.</equation>y=x的极坐标方程为<equation>\theta=\frac{\pi}{4},</equation>x=1的极坐标方程为 rcos<equation>\theta=1,</equation>x=2的极坐标方程为 rcos<equation>\theta=2.</equation>由此可知，D的极坐标表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\cos \theta} \leqslant r \leqslant \frac {2}{\cos \theta}, 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\} = \left\{(r, \theta) \mid \sec \theta \leqslant r \leqslant 2 \sec \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}.</equation>在极坐标系下计算所求二重积分.<equation>\begin{aligned} \iint_ {D} \frac {\sqrt {x ^ {2} + y ^ {2}}}{x} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} \frac {r}{r \cos \theta} \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} \theta \int_ {\sec \theta} ^ {2 \sec \theta} r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \cdot \frac {r ^ {2}}{2} \Bigg | _ {\sec \theta} ^ {2 \sec \theta} \mathrm {d} \theta \\ &= \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \cdot \frac {3}{2} \sec^ {2} \theta \mathrm {d} \theta = \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} (\tan \theta) \\ &= \frac {3}{2} \left(\sec \theta \tan \theta \left| _ {0} ^ {\frac {\pi}{4}} - \int_ {0} ^ {\frac {\pi}{4}} \tan \theta \cdot \sec \theta \tan \theta \mathrm {d} \theta\right)\right) \\ &= \frac {3}{2} \left[ \sqrt {2} - \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \left(\sec^ {2} \theta - 1\right) \mathrm {d} \theta \right] \\ &= \frac {3 \sqrt {2}}{2} - \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta + \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} \theta . \end{aligned}</equation>由上式可得，<equation>\frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3 \sqrt {2}}{2} - \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta + \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec \theta \mathrm {d} \theta .</equation>由此可知，<equation>3 \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3 \sqrt {2}}{2} + \frac {3}{2} \ln | \sec \theta + \tan \theta | \Bigg | _ {0} ^ {\frac {\pi}{4}} = \frac {3 \sqrt {2}}{2} + \frac {3}{2} \ln (\sqrt {2} + 1).</equation>因此，<equation>\iint_ {D} \frac {\sqrt {x ^ {2} + y ^ {2}}}{x} \mathrm {d} x \mathrm {d} y = \frac {3}{2} \int_ {0} ^ {\frac {\pi}{4}} \sec^ {3} \theta \mathrm {d} \theta = \frac {3 \sqrt {2}}{4} + \frac {3}{4} \ln (\sqrt {2} + 1) = \frac {3}{4} \left[ \sqrt {2} + \ln (\sqrt {2} + 1) \right].</equation>

---

**2019年第18题 | 解答题 | 10分**
18. (本题满分10分）

已知平面区域<equation>D=\{(x,y)\mid |x|\leqslant y,(x^{2}+y^{2})^{3}\leqslant y^{4}\}</equation>，计算二重积分<equation>\iint_{D}\frac{x+y}{\sqrt{x^{2}+y^{2}}}\mathrm{d}x\mathrm{d}y</equation>
**答案: **##<equation>\frac{4 3 \sqrt{2}}{1 2 0}.</equation>
**解析: **分析 本题主要考查二重积分的计算.

通过观察可知，本题中的区域 D关于 y轴对称，故可以利用对称性将所求二重积分化简.根据被积函数的特点，应选择在极坐标系下计算二重积分.

解如图所示，区域D由直线<equation>y=x,y=-x</equation>，以及曲线<equation>( x^{2}+y^{2})^{3}=y^{4}</equation>围

成. 由区域 D的表达式可知，区域 D关于 y轴对称. 记<equation>D_{1}</equation>为 D位于 y轴右方的区域.

由于<equation>f ( x,y) = x</equation>为关于x的奇函数，<equation>g ( x,y) = y</equation>为关于x的偶函数，故由对称性可得，<equation>\iint_ {D} \frac {x + y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \iint_ {D} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y.</equation>在极坐标系下计算<equation>\iint_{D_{1}} \frac{y}{\sqrt{x^{2}+y^{2}}} \mathrm{d} x \mathrm{d} y.</equation>写出区域<equation>D_{1}</equation>在极坐标系下的表示.

边界曲线 y=x的极坐标表示为<equation>\theta=\frac{\pi}{4},</equation>y轴的极坐标表示为<equation>\theta=\frac{\pi}{2},</equation><equation>( x^{2}+y^{2} )^{3}=y^{4}</equation>的极坐标表示为<equation>r^{6}=r^{4}\sin^{4}\theta</equation>即 r=<equation>\sin^{2}\theta.</equation>于是，<equation>D _ {1} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sin^ {2} \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D _ {1}} \frac {r \sin \theta}{r} \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin \theta \mathrm {d} \theta \int_ {0} ^ {\sin^ {2} \theta} r \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin \theta \cdot \frac {\sin^ {4} \theta}{2} \mathrm {d} \theta = \frac {1}{2} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin^ {5} \theta \mathrm {d} \theta = - \frac {1}{2} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin^ {4} \theta \mathrm {d} (\cos \theta) \\ &= - \frac {1}{2} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \left(1 - \cos^ {2} \theta\right) ^ {2} \mathrm {d} (\cos \theta) \stackrel {\text {用} = \cos \theta} {=} \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(1 - u ^ {2}\right) ^ {2} \mathrm {d} u \\ &= \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(u ^ {4} - 2 u ^ {2} + 1\right) \mathrm {d} u = \frac {1}{2} \left(\frac {u ^ {5}}{5} - \frac {2 u ^ {3}}{3} + u\right) \Bigg | _ {0} ^ {\frac {\sqrt {2}}{2}} \\ &= \frac {1}{2} \times \left(\frac {\sqrt {2}}{8} \times \frac {1}{5} - \frac {\sqrt {2}}{4} \times \frac {2}{3} + \frac {\sqrt {2}}{2}\right) = \frac {4 3 \sqrt {2}}{2 4 0}. \end{aligned}</equation>因此，<equation>\text {原 积 分} = 2 \iint_ {D _ {1}} \frac {y}{\sqrt {x ^ {2} + y ^ {2}}} \mathrm {d} x \mathrm {d} y = \frac {4 3 \sqrt {2}}{1 2 0}.</equation>

---

**2019年第19题 | 解答题 | 10分**
19. (本题满分10分）

设 n为正整数，记<equation>S_{n}</equation>为曲线<equation>y=\mathrm{e}^{-x}\sin x</equation><equation>(0\leqslant x\leqslant n\pi)</equation>与 x轴所围图形的面积，求<equation>S_{n}</equation>，并求<equation>\lim_{n\to\infty}S_{n}.</equation>
**答案: **<equation>S _ {n} = \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi} \left[ 1 - \mathrm {e} ^ {- (n - 1) \pi} \right]}{1 - \mathrm {e} ^ {- \pi}} + \frac {1}{2} \mathrm {e} ^ {- n \pi}, \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>
**解析: **解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于（<equation>k\pi</equation>，<equation>( k+1)\pi</equation>）的部分与 x轴之间的图形面积等于<equation>\int_{k\pi}^{(k+1)\pi} \mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{aligned} S _ {n} &= \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \underline {{= t = x - k \pi}} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ &= \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\mathrm{e}^{-\pi}+1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\frac{1}{2}\left(\mathrm{e}^{-\pi}+1\right).</equation>因此，<equation>S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}}.</equation><equation>\lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）计算<equation>S_{n}</equation><equation>S _ {n} = \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x.</equation>下面计算<equation>\int\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2 \int\mathrm{e}^{-x}\sin x\mathrm{d}x=-\mathrm{e}^{-x}(\sin x+\cos x)-C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) + C \right],</equation>其中 C为任意常数.

由于当<equation>x \in(k\pi,(k+1)\pi)</equation>（k为偶数）时，<equation>\sin x > 0</equation><equation>|\sin x |=\sin x</equation>；当<equation>x \in(k\pi,(k+1)\pi)</equation>（k为奇数）时，<equation>\sin x < 0</equation><equation>|\sin x |=-\sin x</equation>，故<equation>\begin{aligned} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x &= (- 1) ^ {k} \cdot - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {k \pi} ^ {(k + 1) \pi} \\ \underline {{\cos k \pi = (- 1) ^ {k}}} (- 1) ^ {k} \cdot - \frac {1}{2} \left[ \mathrm {e} ^ {- (k + 1) \pi} \cdot (- 1) ^ {k + 1} - \mathrm {e} ^ {- k \pi} \cdot (- 1) ^ {k} \right] \\ &= \frac {1}{2} \left[ \mathrm {e} ^ {- k \pi} + \mathrm {e} ^ {- (k + 1) \pi} \right]. \end{aligned}</equation>因此，<equation>\begin{array}{l} S _ {n} = \sum_ {k = 0} ^ {n - 1} \left\{\frac {1}{2} \left[ \mathrm {e} ^ {- k \pi} + \mathrm {e} ^ {- (k + 1) \pi} \right] \right\} = \frac {1}{2} + \sum_ {k = 1} ^ {n - 1} \mathrm {e} ^ {- k \pi} + \frac {1}{2} \mathrm {e} ^ {- n \pi} \\ = \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi} \left[ 1 - \mathrm {e} ^ {- (n - 1) \pi} \right]}{1 - \mathrm {e} ^ {- \pi}} + \frac {1}{2} \mathrm {e} ^ {- n \pi}. \\ \end{array}</equation><equation>\begin{aligned} \lim _ {n \rightarrow \infty} S _ {n} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi} \left[ 1 - \mathrm {e} ^ {- (n - 1) \pi} \right]}{1 - \mathrm {e} ^ {- \pi}} + \frac {1}{2} \mathrm {e} ^ {- n \pi} \right] \\ &= \frac {1}{2} + \frac {\mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \end{aligned}</equation>

---

**2018年第17题 | 解答题 | 10分**
17. (本题满分10分)

设平面区域 D由曲线<equation>\left\{ \begin{array}{l} x = t - \sin t, \\ y = 1 - \cos t \end{array} \right.</equation>
**答案: **<equation>3 \pi^{2}+5 \pi.</equation>
**解析: **解区域 D如图所示.把区域 D看作 X型区域， t=0对应的点为（0,0）， t=<equation>\pi</equation>对应的点为（<equation>\pi,2</equation>）， t=2<equation>\pi</equation>对应的点为（2<equation>\pi,0</equation>），则<equation>D = \{(x, y) \mid 0 \leqslant y \leqslant y (x), 0 \leqslant x \leqslant 2 \pi \}</equation>分别计算<equation>\iint_{D}2y\mathrm{d}x\mathrm{d}y</equation>和<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y.</equation><equation>\begin{aligned} \iint_ {D} 2 y \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2 \pi} \mathrm {d} x \int_ {0} ^ {y (x)} 2 y \mathrm {d} y = \int_ {0} ^ {2 \pi} y ^ {2} (x) \mathrm {d} x = \int_ {0} ^ {2 \pi} y ^ {2} [ x (t) ] \cdot x ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {2 \pi} (1 - \cos t) ^ {2} \cdot (1 - \cos t) \mathrm {d} t = \int_ {0} ^ {2 \pi} (1 - \cos t) ^ {3} \mathrm {d} t \\ &= 8 \int_ {0} ^ {2 \pi} \sin^ {6} \frac {t}{2} \mathrm {d} t \xlongequal {u = \frac {t}{2}} 1 6 \int_ {0} ^ {\pi} \sin^ {6} u \mathrm {d} u = 3 2 \int_ {0} ^ {\frac {\pi}{2}} \sin^ {6} u \mathrm {d} u \\ &= 3 2 \times \frac {\pi}{2} \times \frac {5}{6} \times \frac {3}{4} \times \frac {1}{2} = 5 \pi . \end{aligned}</equation>下面用三种方法计算<equation>\iint_{D} x \mathrm{d} x \mathrm{d} y.</equation><equation>\begin{aligned} \iint_ {D} x \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2 \pi} x \mathrm {d} x \int_ {0} ^ {y (x)} \mathrm {d} y = \int_ {0} ^ {2 \pi} x y (x) \mathrm {d} x = \int_ {0} ^ {2 \pi} x (t) y [ x (t) ] \cdot x ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {2 \pi} (t - \sin t) (1 - \cos t) ^ {2} \mathrm {d} t \stackrel {s = t - \pi} {=} \int_ {- \pi} ^ {\pi} (s + \pi + \sin s) (1 + \cos s) ^ {2} \mathrm {d} s. \end{aligned}</equation>由于<equation>( s+\sin s ) ( 1+\cos s )^{2}</equation>是关于s的奇函数，故<equation>\int_{-\pi}^{\pi} ( s+\sin s ) ( 1+\cos s )^{2}\mathrm{d}s=0.</equation><equation>\begin{aligned} \int_ {- \pi} ^ {\pi} (s + \pi + \sin s) (1 + \cos s) ^ {2} d s &= \int_ {- \pi} ^ {\pi} \pi (1 + \cos s) ^ {2} d s \xlongequal {\mathrm {对称性}} 2 \int_ {0} ^ {\pi} \pi (1 + \cos s) ^ {2} d s \\ &= 8 \pi \int_ {0} ^ {\pi} \cos^ {4} \frac {s}{2} \mathrm {d} s \xlongequal {u = \frac {s}{2}} 1 6 \pi \int_ {0} ^ {\frac {\pi}{2}} \cos^ {4} u \mathrm {d} u \\ &= 1 6 \pi \times \frac {\pi}{2} \times \frac {3}{4} \times \frac {1}{2} = 3 \pi^ {2}. \end{aligned}</equation>（法二）由法一知，<equation>\iint_{D}x\mathrm{d}x\mathrm{d}y=\int_{0}^{2\pi} \left(t-\sin t\right)\left(1-\cos t\right)^{2}\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {2 \pi} (t - \sin t) (1 - \cos t) ^ {2} \mathrm {d} t &= \int_ {0} ^ {2 \pi} t (1 - \cos t) ^ {2} \mathrm {d} t - \int_ {0} ^ {2 \pi} \sin t (1 - \cos t) ^ {2} \mathrm {d} t \\ &= \int_ {0} ^ {2 \pi} \left(t - 2 t \cos t + t \cos^ {2} t\right) \mathrm {d} t - \int_ {0} ^ {2 \pi} \left(1 - \cos t\right) ^ {2} \mathrm {d} \left(1 - \cos t\right) \\ &= \int_ {0} ^ {2 \pi} \left(t - 2 t \cos t + t \cdot \frac {1 + \cos 2 t}{2}\right) \mathrm {d} t - \frac {\left(1 - \cos t\right) ^ {3}}{3} \Bigg | _ {0} ^ {2 \pi} \\ &= \int_ {0} ^ {2 \pi} \frac {3}{2} t \mathrm {d} t - 2 \int_ {0} ^ {2 \pi} t \cos t \mathrm {d} t + \frac {1}{2} \int_ {0} ^ {2 \pi} t \cos 2 t \mathrm {d} t - 0 \\ \stackrel {*} {=} 3 \pi^ {2} - 0 - 0 &= 3 \pi^ {2}. \end{aligned}</equation>“<equation>\stackrel{*}{=}</equation>”处用到了<equation>\int_{0}^{2\pi} t\cos t\mathrm{d}t=0, \int_{0}^{2\pi} t\cos 2t\mathrm{d}t=0.</equation><equation>\int_ {0} ^ {2 \pi} t \cos t \mathrm {d} t \xlongequal {\mathrm {分 部 积 分}} \int_ {0} ^ {2 \pi} t \mathrm {d} (\sin t) = t \sin t \Big | _ {0} ^ {2 \pi} - \int_ {0} ^ {2 \pi} \sin t \mathrm {d} t = 0,</equation><equation>\int_ {0} ^ {2 \pi} t \cos 2 t \mathrm {d} t \xlongequal {\text {分 部 积 分}} \frac {1}{2} \int_ {0} ^ {2 \pi} t \mathrm {d} (\sin 2 t) = \frac {1}{2} \left(t \sin 2 t \Big | _ {0} ^ {2 \pi} - \int_ {0} ^ {2 \pi} \sin 2 t \mathrm {d} t\right) = 0.</equation>（法三）注意到区域 D关于直线<equation>x=\pi</equation>对称，故区域 D的形心位于该直线上，从而其形心的横坐标<equation>\overline{x}=\pi.</equation>根据形心公式，<equation>\overline{x}=\frac{\iint\limits_{D}x\mathrm{d}x\mathrm{d}y}{\iint\limits_{D}\mathrm{d}x\mathrm{d}y}</equation>.于是，<equation>\begin{aligned} \iint_ {D} x \mathrm {d} x \mathrm {d} y &= \pi \iint_ {D} \mathrm {d} x \mathrm {d} y = \pi \int_ {0} ^ {2 \pi} \mathrm {d} x \int_ {0} ^ {y (x)} \mathrm {d} y = \pi \int_ {0} ^ {2 \pi} y (x) \mathrm {d} x = \pi \int_ {0} ^ {2 \pi} y [ x (t) ] \cdot x ^ {\prime} (t) \mathrm {d} t \\ &= \pi \int_ {0} ^ {2 \pi} (1 - \cos t) \cdot (1 - \cos t) \mathrm {d} t = \pi \int_ {0} ^ {2 \pi} (1 - \cos t) ^ {2} \mathrm {d} t = 4 \pi \int_ {0} ^ {2 \pi} \sin^ {4} \frac {t}{2} \mathrm {d} t \\ \underline {{\frac {u = \frac {t}{2}}{2}}} 8 \pi \int_ {0} ^ {\pi} \sin^ {4} u \mathrm {d} u &= 1 6 \pi \int_ {0} ^ {\frac {\pi}{2}} \sin^ {4} u \mathrm {d} u = 1 6 \pi \times \frac {\pi}{2} \times \frac {3}{4} \times \frac {1}{2} = 3 \pi^ {2}. \end{aligned}</equation>因此，<equation>\iint_{D} ( x+2 y ) \mathrm{d} x \mathrm{d} y=3 \pi^{2}+5 \pi.</equation>

---

**2017年第20题 | 解答题 | 11分**
20. (本题满分11分）

已知平面区域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 2y\}</equation>，计算二重积分<equation>\iint_{D}(x+1)^{2}\mathrm{d}x\mathrm{d}y.</equation>
**答案: **<equation>\frac{5\pi}{4}.</equation>
**解析: **解如图所示，积分区域 D是圆心在点（0，1），半径为1的圆盘，关于 y轴对称，面积为<equation>\pi</equation>.令<equation>D^{\prime}</equation>为 D位于右半平面的部分.

展开被积函数<equation>( x+1 )^{2}</equation>，得<equation>( x+1 )^{2}=x^{2}+2 x+1.</equation>由于<equation>x^{2}</equation>是关于x的偶函数，2x是关于x的奇函数，故<equation>\iint_{D} x^{2}\mathrm{d}x\mathrm{d}y=2\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y, \iint_{D} 2 x\mathrm{d}x\mathrm{d}y=0.</equation>于是，<equation>\iint_{D} ( x+1 )^{2}\mathrm{d}x\mathrm{d}y=2\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y+0+\iint_{D}\mathrm{d}x\mathrm{d}y=2\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y+\pi.</equation>在极坐标系下计算<equation>\iint_{D^{\prime}} x^{2}\mathrm{d}x\mathrm{d}y.D^{\prime} = \left\{(r,\theta)\mid 0\leqslant r\leqslant 2\sin \theta ,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}.</equation><equation>\begin{aligned} \iint_ {D ^ {\prime}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} r ^ {3} \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{2}} 4 \sin^ {4} \theta \cos^ {2} \theta \mathrm {d} \theta \\ &= 4 \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {4} \theta - \sin^ {6} \theta\right) \mathrm {d} \theta = 4 \times \frac {\pi}{2} \times \left(\frac {3}{4} \times \frac {1}{2} - \frac {5}{6} \times \frac {3}{4} \times \frac {1}{2}\right) = \frac {\pi}{8}. \end{aligned}</equation>因此，<equation>\iint_ {D} (x + 1) ^ {2} \mathrm {d} x \mathrm {d} y = 2 \times \frac {\pi}{8} + \pi = \frac {5 \pi}{4}.</equation>

---

**2016年第18题 | 解答题 | 10分**
18. (本题满分10分）

设 D是由直线 y=1，y=x，y=-x围成的有界区域，计算二重积分<equation>\iint_{D} \frac{x^{2}-xy-y^{2}}{x^{2}+y^{2}} \mathrm{d} x \mathrm{d} y.</equation>
**答案: **# 1-<equation>\frac{\pi}{2}.</equation>
**解析: **解 由于积分区域 D关于 y轴对称，而<equation>\frac{xy}{x^{2}+y^{2}}</equation>是关于 x的奇函数，故<equation>\iint_{D}\frac{xy}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y=0.</equation>记原积分为 I，则<equation>I=\iint_{D}\frac{x^{2}-y^{2}}{x^{2}+y^{2}}\mathrm{d}x\mathrm{d}y.</equation>下面我们用两种方法来计算 I.

（法一）在直角坐标系下计算 I.<equation>I = \iint_ {D} \frac {x ^ {2} - y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y = \iint_ {D} \left(1 - \frac {2 y ^ {2}}{x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y.</equation>如图所示，区域 D为由直线 y=1，y=x，y=-x围成的三角形 AOB. 求得点 A和点 B的坐标，分别为（1，1）和（-1，1）. D的面积等于<equation>S_{\triangle AOB}=\frac{1}{2}\times 2\times 1=1.</equation>从而，<equation>I = 1 - \iint_ {D} \frac {2 y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y \stackrel {\text {对 称 性}} {=} 1 - 4 \iint_ {D _ {1}} \frac {y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y,</equation>其中<equation>D_{1}</equation>是区域D位于第一象限内的部分.把<equation>D_{1}</equation>看作Y型区域，<equation>D_{1}=\{(x,y)\mid 0\leq x\leq y,0\leq y\leq 1\}.</equation><equation>\begin{aligned} \iint_ {D _ {1}} \frac {y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} y ^ {2} \mathrm {d} y \int_ {0} ^ {y} \frac {1}{x ^ {2} + y ^ {2}} \mathrm {d} x \xlongequal {u = \frac {x}{y}} \int_ {0} ^ {1} y ^ {2} \cdot \frac {1}{y} \mathrm {d} y \int_ {0} ^ {1} \frac {1}{u ^ {2} + 1} \mathrm {d} u \\ &= \frac {1}{2} \cdot \arctan u \Bigg | _ {0} ^ {1} = \frac {1}{2} \times \frac {\pi}{4} = \frac {\pi}{8}. \end{aligned}</equation>因此，<equation>I = 1 - 4\times \frac{\pi}{8} = 1 - \frac{\pi}{2}.</equation>（法二）在极坐标系下计算 I.

在极坐标系下，<equation>x=r\cos \theta, y=r\sin \theta</equation>，直线<equation>y=1</equation>对应<equation>r=\frac{1}{\sin \theta}</equation>.区域D的极坐标表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {1}{\sin \theta}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {3 \pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} \frac {x ^ {2} - y ^ {2}}{x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\sin \theta}} \frac {r ^ {2} \cos^ {2} \theta - r ^ {2} \sin^ {2} \theta}{r ^ {2}} \cdot r \mathrm {d} r = \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \left(1 - 2 \sin^ {2} \theta\right) \mathrm {d} \theta \int_ {0} ^ {\frac {1}{\sin \theta}} r \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \frac {1 - 2 \sin^ {2} \theta}{2 \sin^ {2} \theta} \mathrm {d} \theta = \int_ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} \frac {1}{2 \sin^ {2} \theta} \mathrm {d} \theta - \frac {\pi}{2} = - \frac {1}{2} \cot \theta \left| _ {\frac {\pi}{4}} ^ {\frac {3}{4} \pi} - \frac {\pi}{2} = 1 - \frac {\pi}{2}. \right. \end{aligned}</equation>

---

**2015年第18题 | 解答题 | 10分**
18. (本题满分10分)

计算二重积分<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y, \text {其 中} D = \{(x, y) \mid x ^ {2} + y ^ {2} \leqslant 2, y \geqslant x ^ {2} \}.</equation>
**答案: **## (18)<equation>\frac{\pi}{4}-\frac{2}{5}.</equation>
**解析: **解 由图（a）可知，区域 D关于 y轴对称，而 xy为关于 x的奇函数，故<equation>\iint_{D} xy\mathrm{d}x\mathrm{d}y=0</equation>.又因为<equation>x^{2}</equation>为关于 x的偶函数，所以<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y,</equation>其中<equation>D_{1}</equation>是D位于右半平面的部分.我们可以用两种方法来计算<equation>\iint\limits_{\Omega}x^{2}\mathrm{d}x\mathrm{d}y.</equation>(a)

（法一）在直角坐标系下计算.

(b)

(c)

如图（b）所示，先求出圆弧<equation>x^{2}+y^{2}=2</equation>与抛物线<equation>y=x^{2}</equation>的交点.由<equation>\left\{\begin{array}{l l}x^{2}+y^{2}=2\\ y=x^{2},\end{array}\right.</equation>可求得<equation>(x,y)=(1,1)</equation>或<equation>(x,y)=(-1,1).</equation>在第一象限中的交点为<equation>(x,y)=(1,1).</equation>由圆方程<equation>x^{2}+y^{2}=2</equation>可得，<equation>y=\sqrt{2-x^{2}}</equation>.由于圆弧在第一象限，故根号前取+号.将区域<equation>D_{1}</equation>写成X型区域，<equation>D _ {1} = \left\{(x, y) \mid x ^ {2} \leqslant y \leqslant \sqrt {2 - x ^ {2}}, 0 \leqslant x \leqslant 1 \right\}.</equation>从而<equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {2 - x ^ {2}}} x ^ {2} \mathrm {d} y = \int_ {0} ^ {1} x ^ {2} \left(\sqrt {2 - x ^ {2}} - x ^ {2}\right) \mathrm {d} x \\ &= \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {4} \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \sqrt {2 - x ^ {2}} \mathrm {d} x - \frac {1}{5} \\ \underline {{x = \sqrt {2} \sin t}} \int_ {0} ^ {\frac {\pi}{4}} 4 \sin^ {2} t \cos^ {2} t \mathrm {d} t - \frac {1}{5} &= \int_ {0} ^ {\frac {\pi}{4}} (\sin 2 t) ^ {2} \mathrm {d} t - \frac {1}{5} \\ &= \int_ {0} ^ {\frac {\pi}{4}} \frac {1 - \cos 4 t}{2} \mathrm {d} t - \frac {1}{5} = \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>（法二）在极坐标系下计算.

写出<equation>x^{2}+y^{2}=2</equation>的极坐标形式：<equation>r=\sqrt{2}</equation>写出<equation>y=x^{2}</equation>的极坐标形式：<equation>r\sin \theta=r^{2}\cos^{2}\theta</equation>化简为<equation>r=\tan \theta\sec \theta.</equation>可求得圆弧与抛物线的交点坐标为<equation>\left(\sqrt{2},\frac{\pi}{4}\right).</equation>如图（c）所示，连接极点与该交点，将区域<equation>D_{1}</equation>分成两部分，<equation>D_{1}=D_{1}^{\prime}\cup D_{1}^{\prime\prime}.</equation><equation>D_{1}^{\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>\theta=\frac{\pi}{2}</equation>以及圆弧r=<equation>\sqrt{2}</equation>围成；<equation>D_{1}^{\prime\prime}</equation>由<equation>\theta=\frac{\pi}{4},</equation><equation>r=\tan \theta\sec \theta</equation>围成，从而<equation>D _ {1} ^ {\prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sqrt {2}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}, \quad D _ {1} ^ {\prime \prime} = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \tan \theta \sec \theta , 0 \leqslant \theta \leqslant \frac {\pi}{4} \right\}</equation><equation>\begin{aligned} \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} r ^ {3} \cos^ {2} \theta \mathrm {d} r + \int_ {0} ^ {\frac {\pi}{4}} \mathrm {d} \theta \int_ {0} ^ {\tan \theta \sec \theta} r ^ {3} \cos^ {2} \theta \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {1 + \cos 2 \theta}{2} \mathrm {d} \theta + \int_ {0} ^ {\frac {\pi}{4}} \cos^ {2} \theta \cdot \frac {\tan^ {4} \theta \sec^ {4} \theta}{4} \mathrm {d} \theta \\ &= \frac {\pi}{8} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {\frac {\pi}{4}} \tan^ {4} \theta \sec^ {2} \theta \mathrm {d} \theta \frac {u = \tan \theta}{\pi} - \frac {1}{4} + \frac {1}{4} \int_ {0} ^ {1} u ^ {4} \mathrm {d} u \\ &= \frac {\pi}{8} - \frac {1}{5}. \end{aligned}</equation>因此，<equation>\iint_ {D} x (x + y) \mathrm {d} x \mathrm {d} y = 2 \iint_ {D _ {1}} x ^ {2} \mathrm {d} x \mathrm {d} y = \frac {\pi}{4} - \frac {2}{5}.</equation>

---

**2014年第17题 | 解答题 | 10分**
17. (本题满分10分)

设平面区域 D = {（x,y）| 1≤x²+y²≤4,x≥0,y≥0}.计算<equation>\iint_{D} \frac{x\sin(\pi\sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y.</equation>
**答案: **<equation>(1 7) - \frac {3}{4}.</equation>
**解析: **解记<equation>\iint_{D}\frac{x\sin(\pi \sqrt{x^{2}+y^{2}})}{x+y}\mathrm{d}x\mathrm{d}y=I.</equation>积分区域如图所示.

（法一）首先，由于积分区域 D关于<equation>y=x</equation>对称，故对 x，y具有轮换对称性，从而<equation>I = \iint_ {D} \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y = \iint_ {D} \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \mathrm {d} x \mathrm {d} y.</equation>因此，<equation>I = \frac {1}{2} \iint_ {D} \left[ \frac {x \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} + \frac {y \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right)}{x + y} \right] \mathrm {d} x \mathrm {d} y = \frac {1}{2} \iint_ {D} \sin \left(\pi \sqrt {x ^ {2} + y ^ {2}}\right) \mathrm {d} x \mathrm {d} y.</equation>在极坐标系下，<equation>D=\left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\} .</equation><equation>I = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {1} ^ {2} \sin (\pi r) \cdot r \mathrm {d} r = \frac {\pi}{4} \int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r,</equation>其中，<equation>\int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r = - \frac {1}{\pi} \int_ {1} ^ {2} r \mathrm {d} [ \cos (\pi r) ] = - \frac {1}{\pi} \left[ r \cos (\pi r) \left| _ {1} ^ {2} - \int_ {1} ^ {2} \cos (\pi r) \mathrm {d} r \right. \right] = - \frac {3}{\pi}.</equation>因此，<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}.</equation>（法二）在不使用轮换对称性对<equation>I</equation>进行化简的情况下计算<equation>I</equation>.

在极坐标系下，<equation>D = \left\{(r,\theta)\mid 1\leqslant r\leqslant 2,0\leqslant \theta \leqslant \frac{\pi}{2}\right\}.</equation><equation>I = \int_ {0} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {1} ^ {2} \frac {r \cos \theta \sin (\pi r)}{r (\cos \theta + \sin \theta)} \cdot r \mathrm {d} r = \int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta \int_ {1} ^ {2} r \sin (\pi r) \mathrm {d} r.</equation>由于<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta \xlongequal {\text {等 式}} \frac {t = \frac {\pi}{2} - \theta}{\int_ {\frac {\pi}{2}} ^ {0} \frac {\sin t}{\cos t + \sin t} \mathrm {d} t} = \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta ,</equation>故<equation>\int_ {0} ^ {\frac {\pi}{2}} \frac {\cos \theta}{\cos \theta + \sin \theta} \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \left(\frac {\cos \theta}{\cos \theta + \sin \theta} + \frac {\sin \theta}{\cos \theta + \sin \theta}\right) \mathrm {d} \theta = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} 1 \mathrm {d} \theta = \frac {\pi}{4}.</equation>因此，<equation>I = \frac{\pi}{4}\times \left(-\frac{3}{\pi}\right) = -\frac{3}{4}.</equation>

---

**2013年第17题 | 解答题 | 10分**
17. (本题满分10分)

设平面区域 D由直线 x=3y，y=3x及 x+y=8围成，计算<equation>\iint\limits_{D}x^{2}\mathrm{d}x\mathrm{d}y.</equation>
**答案: **## (17)<equation>\frac{4 1 6}{3}.</equation>
**解析: **解 （法一）在直角坐标系下计算.

如图，可以分别求出 y=3x与 x+y=8的交点，以及 x=3y与 x+y=8的交点.<equation>\left\{ \begin{array}{l l} y = 3 x, \\ x + y = 8, \end{array} \Rightarrow \left\{ \begin{array}{l l} x = 2, \\ y = 6, \end{array} \right. \quad \left\{ \begin{array}{l l} x = 3 y, \\ x + y = 8, \end{array} \Rightarrow \left\{ \begin{array}{l l} x = 6, \\ y = 2. \end{array} \right. \right.</equation>于是直线<equation>x = 2</equation>将区域<equation>D</equation>分为两部分<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 3 x, 0 \leqslant x \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {x}{3} \leqslant y \leqslant 8 - x, 2 \leqslant x \leqslant 6 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y &= \int_ {0} ^ {2} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {3 x} \mathrm {d} y + \int_ {2} ^ {6} x ^ {2} \mathrm {d} x \int_ {\frac {x}{3}} ^ {8 - x} \mathrm {d} y = \int_ {0} ^ {2} x ^ {2} \cdot \frac {8}{3} x \mathrm {d} x + \int_ {2} ^ {6} \left(8 - \frac {4}{3} x\right) x ^ {2} \mathrm {d} x \\ &= \frac {2}{3} x ^ {4} \left| _ {0} ^ {2} + \frac {8}{3} x ^ {3} \right| _ {2} ^ {6} - \frac {1}{3} x ^ {4} \left| _ {2} ^ {6} = \frac {4 1 6}{3}. \right. \end{aligned}</equation>（法二）在极坐标系下计算.

三条直线的方程分别为<equation>\theta=\arctan \frac{1}{3},</equation><equation>\theta=\arctan 3</equation>，以及<equation>r(\cos \theta+\sin \theta)=8.</equation>此时，区域D在极坐标系下的表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \frac {8}{\cos \theta + \sin \theta}, \arctan \frac {1}{3} \leqslant \theta \leqslant \arctan 3 \right\}.</equation><equation>\begin{aligned} \iint_ {D} x ^ {2} \mathrm {d} x \mathrm {d} y \stackrel {\text {极 坐 标}} {=} \iint_ {D} r ^ {2} \cos^ {2} \theta \cdot r \mathrm {d} r \mathrm {d} \theta &= \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \cos^ {2} \theta \mathrm {d} \theta \int_ {0} ^ {\frac {8}{\cos \theta + \sin \theta}} r ^ {3} \mathrm {d} r \\ &= \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {\cos^ {2} \theta}{\left(\cos \theta + \sin \theta\right) ^ {4}} \mathrm {d} \theta = \frac {8 ^ {4}}{4} \int_ {\arctan \frac {1}{3}} ^ {\arctan 3} \frac {1}{\left(1 + \tan \theta\right) ^ {4}} \cdot \sec^ {2} \theta \mathrm {d} \theta \\ \underline {{=}} \frac {u = \tan \theta}{4} \frac {8 ^ {4}}{4} \int_ {\frac {1}{3}} ^ {3} \frac {1}{(1 + u) ^ {4}} \mathrm {d} u &= \frac {8 ^ {4}}{4} \cdot \left(- \frac {1}{3}\right) \frac {1}{(1 + u) ^ {3}} \Big | _ {\frac {1}{3}} ^ {3} = \frac {4 1 6}{3}. \end{aligned}</equation>

---

**2012年第6题 | 选择题 | 4分 | 答案: D**
6. 设区域 D由曲线<equation>y=\sin x,x=\pm \frac{\pi}{2},y=1</equation>围成，则<equation>\iint_{D}(xy^{5}-1)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\pi</equation>B.2 C.-2 D.<equation>-\pi</equation>
答案: D
**解析: **解区域D如图（a）所示。如图（b）所示，将D分为两部分，<equation>D=D_{1}\cup D_{2}.</equation><equation>D_{1}</equation>由<equation>y=1</equation><equation>y=\left| \sin x\right|</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上的一段围成.<equation>D_{2}</equation>由<equation>x=-\frac{\pi}{2},y=-\sin x,y=\sin x</equation>围成.<equation>D_{1}</equation>关于y轴对

(a)

(b)

称，<equation>D_{2}</equation>关于 x轴对称.

由于<equation>x y^{5}</equation>为关于x的奇函数，故<equation>\iint_{D_{1}} x y^{5} \mathrm{d} x \mathrm{d} y=0.</equation>又由于<equation>x y^{5}</equation>为关于y的奇函数，故<equation>\iint_{D_{2}} x y^{5} \mathrm{d} x \mathrm{d} y=0.</equation>从而，<equation>\iint_{D} x y^{5} \mathrm{d} x \mathrm{d} y=0.</equation>将 D写成 X型区域，<equation>D = \left\{(x, y) \mid \sin x \leqslant y \leqslant 1, - \frac {\pi}{2} \leqslant x \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} \left(x y ^ {5} - 1\right) \mathrm {d} x \mathrm {d} y = \iint_ {D} x y ^ {5} \mathrm {d} x \mathrm {d} y - \iint_ {D} \mathrm {d} x \mathrm {d} y = - \iint_ {D} \mathrm {d} x \mathrm {d} y = - \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 - \sin x\right) \mathrm {d} x = - \pi .</equation>应选 D.

---

**2012年第18题 | 解答题 | 10分**
18. (本题满分10分）计算二重积分<equation>\iint_{D} xy\mathrm{d}\sigma</equation>，其中区域 D由曲线<equation>r=1+\cos \theta</equation>（<equation>0\leqslant \theta \leqslant \pi</equation>）与极轴围成.
**答案: **<equation>(1 8) \frac {1 6}{1 5}.</equation>
**解析: **积分区域 D如图所示. 写出区域 D的表示.<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 1 + \cos \theta , 0 \leqslant \theta \leqslant \pi \right\}</equation>因此，

$$
\begin{array}{l} \iint_ {D} x y \mathrm {d} \sigma \stackrel {\text {极 坐 标}} {=} \iint_ {D} r ^ {2} \cos \theta \sin \theta \cdot r \mathrm {d} r \mathrm {d} \theta = \int_ {0} ^ {\pi} \cos \theta \sin \theta \mathrm {d} \theta \int_ {0} ^ {1 + \cos \theta} r ^ {3} \mathrm {d} r \\ = \int_ {0} ^ {\pi} \frac {\left(1 + \cos \theta\right) ^ {4}}{4} \cos \theta \sin \theta \mathrm {d} \theta \frac {u = 1 + \cos \theta}{\underline {

---

**2011年第13题 | 填空题 | 4分**
13. 设平面区域 D 由直线 y=x，圆<equation>x^{2}+y^{2}=2y</equation>及 y轴所围成，则二重积分<equation>\iint_{D} xy\mathrm{d}\sigma=</equation>___
**答案: **# 7 12.
**解析: **解 区域 D 如图所示.

在极坐标系下，圆方程<equation>x^{2}+y^{2}=2 y</equation>化为<equation>r^{2}=2 r \sin \theta</equation>，化简得到<equation>r=2 \sin \theta</equation>直线<equation>y=x</equation>的方程化为<equation>\theta=\frac{\pi}{4}.</equation>y轴方程化为<equation>\theta=\frac{\pi}{2}.</equation>从而可写出区域D的表示.<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 \sin \theta , \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{2} \right\}.</equation>因此，<equation>\iint_ {D} x y \mathrm {d} \sigma = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin \theta \cos \theta \mathrm {d} \theta \int_ {0} ^ {2 \sin \theta} r ^ {3} \mathrm {d} r = 4 \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \sin^ {5} \theta \cos \theta \mathrm {d} \theta = 4 \cdot \left. \frac {\sin^ {6} \theta}{6} \right| _ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} = \frac {7}{1 2}.</equation>

---

**2011年第21题 | 解答题 | 11分**
21. (本题满分11分)

已知函数 f(x,y)具有二阶连续偏导数，且<equation>f(1,y)=f(x,1)=0,\iint_{D}f(x,y)\mathrm{d}x\mathrm{d}y=a</equation>，其中 D={（x,y）|0≤x≤ 1,0≤y≤1}，计算二重积分<equation>I=\iint_{D}xyf_{xy}^{\prime\prime}(x,y)\mathrm{d}x\mathrm{d}y.</equation>
**答案: **(21) a.
**解析: **解 由于<equation>f_{xy}^{\prime \prime}(x,y)</equation>是<equation>f_x^{\prime}(x,y)</equation>对<equation>y</equation>的偏导数，故对每个固定的<equation>x,f_{xy}^{\prime \prime}(x,y)\mathrm{d}y = \mathrm{d}[f_x^{\prime}(x,y)]</equation><equation>\begin{aligned} I &= \iint_ {D} x y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y f _ {x y} ^ {\prime \prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} y \mathrm {d} \left[ f _ {x} ^ {\prime} (x, y) \right] \\ \underline {{\text {分 部 积 分}}} \int_ {0} ^ {1} x \left[ y f _ {x} ^ {\prime} (x, y) \right| _ {y = 0} ^ {y = 1} - \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y ] \mathrm {d} x &= \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, 1) \mathrm {d} x - \int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y. \end{aligned}</equation>由于<equation>f ( x, 1 ) = 0</equation>，即一元函数<equation>f ( x, 1 )</equation>是关于 x的常函数，故<equation>f_{x}^{\prime} ( x, 1 ) = 0.</equation>又由于 D为矩形区域，故交换二次积分的积分次序可得，<equation>\int_ {0} ^ {1} x \mathrm {d} x \int_ {0} ^ {1} f _ {x} ^ {\prime} (x, y) \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x.</equation>从而，<equation>\begin{aligned} I &= 0 - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x f _ {x} ^ {\prime} (x, y) \mathrm {d} x = - \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} x \mathrm {d} [ f (x, y) ] \\ \underline {{\text {分 部 积 分}}} - \int_ {0} ^ {1} \left[ x f (x, y) \left| _ {x = 0} ^ {x = 1} - \int_ {0} ^ {1} f (x, y) \mathrm {d} x \right] \mathrm {d} y &= - \int_ {0} ^ {1} f (1, y) \mathrm {d} y + \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x \right. \\ \underline {{\underline {{f (1 , y) = 0}}}} \int_ {0} ^ {1} \mathrm {d} y \int_ {0} ^ {1} f (x, y) \mathrm {d} x &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = a. \end{aligned}</equation>

---

**2010年第20题 | 解答题 | 11分**
0. (本题满分10分）

计算二重积分<equation>I=\iint_{D} r^{2}\sin \theta \sqrt{1-r^{2}\cos 2\theta}\mathrm{d}r\mathrm{d}\theta</equation>，其中<equation>D=\left\{(r,\theta)\mid 0\leqslant r\leqslant \sec \theta ,0\leqslant \theta \leqslant \frac{\pi}{4}\right\} .</equation>
**答案: **<equation>2 0) I = \frac {1}{3} - \frac {\pi}{1 6}.</equation>
**解析: **解 在极坐标系下，积分区域<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant \sec \theta, 0 \leqslant \theta \leqslant \frac{\pi}{4}\right\}</equation>由<equation>0 \leqslant r \leqslant \sec \theta</equation>得，<equation>0 \leqslant r \cos \theta \leqslant 1</equation>. 又由于<equation>0 \leqslant \theta \leqslant \frac{\pi}{4}</equation>，故可知在直角坐标系下，<equation>D</equation>为由<equation>x = 1, y = x</equation>以及<equation>x</equation>轴围成的三角形区域，积分区域如图所示.将<equation>D</equation>写成X型区域，<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}</equation>由<equation>\left\{ \begin{array}{l l} x = r\cos \theta , \\ y = r\sin \theta , \end{array} \right.</equation>可将<equation>r^{2}\cos 2\theta</equation>表示为<equation>r ^ {2} \cos 2 \theta = r ^ {2} \cos^ {2} \theta - r ^ {2} \sin^ {2} \theta = x ^ {2} - y ^ {2}.</equation>因此，<equation>\begin{aligned} I &= \iint_ {D} y \sqrt {1 - \left(x ^ {2} - y ^ {2}\right)} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} y \sqrt {1 - \left(x ^ {2} - y ^ {2}\right)} \mathrm {d} y \\ &= \frac {1}{2} \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \sqrt {y ^ {2} - x ^ {2}} + 1 \mathrm {d} \left(y ^ {2} - x ^ {2} + 1\right) = \frac {1}{2} \int_ {0} ^ {1} \frac {2}{3} \left(y ^ {2} - x ^ {2} + 1\right) ^ {\frac {3}{2}} \Bigg | _ {y = 0} ^ {y = x} \mathrm {d} x \\ &= \frac {1}{3} - \frac {1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \mathrm {d} x \xlongequal {x = \sin t} \frac {1}{3} - \frac {1}{3} \int_ {0} ^ {\frac {\pi}{2}} \left(\cos^ {2} t\right) ^ {\frac {3}{2}} \cdot \cos t \mathrm {d} t \\ &= \frac {1}{3} - \frac {1}{3} \int_ {0} ^ {\frac {\pi}{2}} \cos^ {4} t \mathrm {d} t = \frac {1}{3} - \frac {1}{3} \times \frac {\pi}{2} \times \frac {3}{4} \times \frac {1}{2} = \frac {1}{3} - \frac {\pi}{1 6}. \end{aligned}</equation>

---

**2009年第19题 | 解答题 | 10分**
19. (本题满分10分)

计算二重积分<equation>\iint_{D} ( x-y ) \mathrm{d} x \mathrm{d} y</equation>，其中<equation>D=\left\{( x, y ) \mid( x-1 )^{2}+( y-1 )^{2} \leqslant 2, y \geqslant x \right\} .</equation>
**答案: **<equation>(1 9) - \frac {8}{3}.</equation>
**解析: **解（法一）如图（a）所示，作极坐标变换<equation>\left\{\begin{array}{l l}x=r\cos \theta ,\\ y=r\sin \theta ,\end{array} \right.</equation>则圆方程<equation>( x-1 )^{2}+( y-1 )^{2}=2</equation>变成<equation>r=2(\cos \theta +\sin \theta )</equation>从而D在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid 0 \leqslant r \leqslant 2 (\cos \theta + \sin \theta), \frac {\pi}{4} \leqslant \theta \leqslant \frac {3 \pi}{4} \right\}.</equation>因此，<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \mathrm {d} \theta \int_ {0} ^ {2 (\cos \theta + \sin \theta)} r ^ {2} \mathrm {d} r = \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta - \sin \theta) \left[ \frac {r ^ {3}}{3} \Big | _ {0} ^ {2 (\cos \theta + \sin \theta)} \right] \mathrm {d} \theta \\ &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (1 + \sin 2 \theta) \cos 2 \theta \mathrm {d} \theta \\ \underline {{= u = \sin 2 \theta}} \frac {4}{3} \int_ {1} ^ {- 1} (1 + u) \mathrm {d} u &= - \frac {8}{3}. \end{aligned}</equation>(a)

(b)

或者也可以这样计算.<equation>\begin{aligned} \iint_ {D} (x - y) \mathrm {d} x \mathrm {d} y &= \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {3} (\cos \theta - \sin \theta) \mathrm {d} \theta = \frac {8}{3} \int_ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} (\cos \theta + \sin \theta) ^ {3} \mathrm {d} (\cos \theta + \sin \theta) \\ &= \frac {2}{3} \left(\cos \theta + \sin \theta\right) ^ {4} \Bigg | _ {\frac {\pi}{4}} ^ {\frac {3 \pi}{4}} = - \frac {8}{3}. \end{aligned}</equation>（法二）作换元<equation>\left\{\begin{array}{l l}x=1+r\cos \theta ,\\ y=1+r\sin \theta ,\end{array} \right.</equation>则圆方程<equation>( x-1 )^{2}+( y-1 )^{2}=2</equation>变为<equation>r^{2}=2</equation>，而直线 y=x变为<equation>\theta =\frac{\pi}{4}</equation>和<equation>\theta =\frac{5\pi}{4}</equation>如图（b）所示，原区域 D变成区域<equation>D^{\prime}=\left\{(r,\theta)\mid 0\leqslant r\leqslant \sqrt{2},\frac{\pi}{4}\leqslant \theta \leqslant \frac{5\pi}{4}\right\}</equation>计算该变换的雅可比行列式.<equation>J (r, \theta) = \left| \begin{array}{c c} \cos \theta & - r \sin \theta \\ \sin \theta & r \cos \theta \end{array} \right| = r.</equation>因此，<equation>\begin{aligned} \text {原 积 分} &= \iint_ {D ^ {\prime}} r (\cos \theta - \sin \theta) \cdot r \mathrm {d} r \mathrm {d} \theta = \int_ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} (\cos \theta - \sin \theta) \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} r ^ {2} \mathrm {d} r \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} (\cos \theta - \sin \theta) \left(\frac {r ^ {3}}{3} \Big | _ {0} ^ {\sqrt {2}}\right) \mathrm {d} \theta = \frac {2 \sqrt {2}}{3} (\sin \theta + \cos \theta) \Big | _ {\frac {\pi}{4}} ^ {\frac {5 \pi}{4}} = - \frac {8}{3}. \end{aligned}</equation>

---


**2009年第22题 | 解答题 | 11分**


假设<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right), \quad \boldsymbol {\xi} _ {1} = \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right).</equation>I. 求满足<equation>A\xi_{2}=\xi_{1}, A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{2},\xi_{3}</equation>；

II. 对第一问中的任意向量<equation>\xi_{2},\xi_{3}</equation>，证明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

**答案:**（22）（I）满足<equation>A\xi_{2}=\xi_{1}</equation>的所有向量为<equation>\xi_{2}=k_{1}(1,-1,2)^{\mathrm{T}}+(0,0,1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数；满足<equation>A^{2}\xi_{3}=\xi_{1}</equation>的所有向量<equation>\xi_{3}</equation>为<equation>\xi_{3}=k_{2}(1,-1,0)^{\mathrm{T}}+k_{3}(0,0,1)^{\mathrm{T}}+\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2},k_{3}</equation>为任意常数.

（Ⅱ）证明略.

**解析:**解（I）解<equation>A x=\xi_{1}</equation>，这是一个非齐次线性方程组.<equation>\left(\boldsymbol {A}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ - 1 & 1 & 1 & 1 \\ 0 & - 4 & - 2 & - 2 \end{array} \right) \xrightarrow [ r _ {2} ^ {*} \leftrightarrow r _ {3} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 1 & - 1 & - 1 & - 1 \\ 0 & - 4 & - 2 & - 2 \\ 0 & 0 & 0 & 0 \end{array} \right) \xrightarrow [ r _ {1} + r _ {2} ^ {* * *} ]{r _ {2} ^ {* *} \times \left(- \frac {1}{2}\right)} \left( \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第<equation>i</equation>行作初等行变换后所得新的第<equation>i</equation>行，每做一次初等行变换，加一个*.）

于是<equation>r(\mathbf{A}) = r(\mathbf{A},\xi_1) = 2.Ax = \xi_1</equation>有无穷多解.其对应的齐次方程组等价于<equation>\left\{ \begin{array}{l l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 0, \end{array} \right.</equation>故可取<equation>(1, - 1,2)^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>\left\{ \begin{array}{l l} x_{1} + x_{2} = 0, \\ 2x_{2} + x_{3} = 1 \end{array} \right.</equation>的一个特解为<equation>(0,0,1)^{\mathrm{T}}.</equation>因此，<equation>Ax = \xi_{1}</equation>的通解为<equation>\xi_{2} = k_{1}(1, -1, 2)^{\mathrm{T}} + (0, 0, 1)^{\mathrm{T}}</equation>，其中<equation>k_{1}</equation>为任意常数.<equation>\left(\boldsymbol {A} ^ {2}, \boldsymbol {\xi} _ {1}\right) = \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ - 2 & - 2 & 0 & 1 \\ 4 & 4 & 0 & - 2 \end{array} \right) \xrightarrow [ r _ {3} - 2 r _ {1} ]{r _ {2} + r _ {1}} \left( \begin{array}{c c c c} 2 & 2 & 0 & - 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right).</equation>于是<equation>r \left( A^{2} \right)=r \left( A^{2}, \xi_{1} \right)=1. A^{2} x=\xi_{1}</equation>有无穷多解.其对应的齐次方程组等价于<equation>2 \left( x_{1}+x_{2} \right)=0</equation>故可取（1，-1，0）<equation>^{\mathrm{T}}</equation>和（0，0，1）<equation>^{\mathrm{T}}</equation>为它的一个基础解系.另外，<equation>2 \left( x_{1}+x_{2} \right)=-1</equation>的一个特解为<equation>\left(-\frac{1}{2},0,0\right)^{\mathrm{T}}.</equation>因此，<equation>A^{2}x = \xi_{1}</equation>的通解为<equation>\xi_{3} = k_{2}(1, -1, 0)^{\mathrm{T}} + k_{3}(0, 0, 1)^{\mathrm{T}} + \left(-\frac{1}{2}, 0, 0\right)^{\mathrm{T}}</equation>，其中<equation>k_{2}, k_{3}</equation>为任意常数.

（Ⅱ）（法一）通过计算可知，<equation>\boldsymbol {A} \boldsymbol {\xi} _ {1} = \left( \begin{array}{c c c} 1 & - 1 & - 1 \\ - 1 & 1 & 1 \\ 0 & - 4 & - 2 \end{array} \right) \left( \begin{array}{c} - 1 \\ 1 \\ - 2 \end{array} \right) = \left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right).</equation>从而<equation>A^{3}\xi_{3} = A^{2}\xi_{2} = A\xi_{1} = 0.</equation>我们可以利用该性质推出<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

不妨设<equation>a\boldsymbol{\xi}_1 + b\boldsymbol{\xi}_2 + c\boldsymbol{\xi}_3 = \mathbf{0}</equation>. 该等式两端同时左乘<equation>A^2</equation>，得<equation>a A ^ {2} \xi_ {1} + b A ^ {2} \xi_ {2} + c A ^ {2} \xi_ {3} = c A ^ {2} \xi_ {3} = c \xi_ {1} = \mathbf {0}.</equation>由于<equation>\boldsymbol{\xi}_{1}</equation>为非零向量，故<equation>c=0.</equation>于是<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation>再在<equation>a\boldsymbol{\xi}_{1}+b\boldsymbol{\xi}_{2}=\mathbf{0}</equation>两端同时左乘 A，得<equation>aA\boldsymbol{\xi}_{1}+bA\boldsymbol{\xi}_{2}=bA\boldsymbol{\xi}_{1}=b\boldsymbol{\xi}_{2}=\mathbf{0}.</equation><equation>a A \xi_ {1} + b A \xi_ {2} = b A \xi_ {2} = b \xi_ {1} = 0.</equation>同理得<equation>b = 0</equation>. 由于<equation>b = c = 0</equation>, 故<equation>a\xi_{1} = 0</equation>. 从而<equation>a = 0</equation>.

因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

（法二）由第（I）问，我们得到<equation>\xi_{1},\xi_{2},\xi_{3}</equation>的表达式，从而可以通过计算<equation>|\xi_{1},\xi_{2},\xi_{3}|</equation>来说明<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.<equation>\begin{aligned} | \xi_ {1}, \xi_ {2}, \xi_ {3} | &= \left| \begin{array}{c c c} - 1 & k _ {1} & k _ {2} - \frac {1}{2} \\ 1 & - k _ {1} & - k _ {2} \\ - 2 & 2 k _ {1} + 1 & k _ {3}  \right| \frac {c _ {2} + k _ {1} c _ {1}}{c _ {3} + k _ {2} c _ {1}} \left| \begin{array}{c c c} - 1 & 0 & - \frac {1}{2} \\ 1 & 0 & 0 \\ - 2 & 1 & k _ {3} - 2 k _ {2}  \right| \\ \underline {{\text {按 第二 行 展 开}}} (- 1) \left| \begin{array}{c c} 0 & - \frac {1}{2} \\ 1 & k _ {3} - 2 k _ {2}  \right| &= - \frac {1}{2} \neq 0. \end{aligned}</equation>因此，<equation>\xi_{1},\xi_{2},\xi_{3}</equation>线性无关.

---


# 数学一


## 高等数学


### 一元函数微分学


#### 曲线的凹凸性、拐点及渐近线

**2025年第1题 | 选择题 | 5分 | 答案: B**

1. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \sin t \mathrm{d} t,g ( x )=\int_{0}^{x} \mathrm{e}^{t^{2}} \mathrm{d} t \cdot \sin^{2} x</equation>，则（    )

A. x=0是 f(x)的极值点，也是 g(x)的极值点

B. x=0是 f(x)的极值点，(0,0)是曲线 y=g(x)的拐点

C. x=0是 f(x)的极值点，(0,0)是曲线 y=f(x)的拐点

D. (0,0)是曲线 y=f(x)的拐点，也是曲线 y=g(x)的拐点

答案: B

**解析:**解 先分析<equation>f(x)</equation>的性质，分别计算<equation>f^{\prime}(x)</equation>，<equation>f^{\prime \prime}(x)</equation>. 根据链式法则，<equation>f ^ {\prime} (x) = \sin x \mathrm {e} ^ {x ^ {2}},</equation><equation>f ^ {\prime \prime} (x) = 2 x \sin x \mathrm {e} ^ {x ^ {2}} + \cos x \mathrm {e} ^ {x ^ {2}} = \left(2 x \sin x + \cos x\right) \mathrm {e} ^ {x ^ {2}}.</equation>取<equation>\delta</equation>为充分小的正数，当<equation>x\in(-\delta,0)</equation>时，<equation>f^{\prime}(x)<0,f(x)</equation>单调减少，当<equation>x\in(0,\delta)</equation>时，<equation>f^{\prime}(x) > 0,f(x)</equation>单调增加.于是，<equation>x=0</equation>是<equation>f(x)</equation>的极小值点.或者，也可以由<equation>f^{\prime}(0)=0,f^{\prime\prime}(0)=1>0</equation>以及极值的第二充分条件得到<equation>x=0</equation>是<equation>f(x)</equation>的极小值点.

当<equation>x \in(-\delta ,\delta)</equation>时，<equation>x\sin x\geqslant0,\cos x > 0,f^{\prime \prime}(x)</equation>在<equation>(-\delta ,\delta)</equation>内恒大于0，<equation>y=f(x)</equation>是凹曲线。于是，点（0，0）不是曲线<equation>y=f(x)</equation>的拐点.

再分析<equation>g(x)</equation>的性质，分别计算<equation>g^{\prime}(x), g^{\prime \prime}(x)</equation>.根据链式法则，<equation>g ^ {\prime} (x) = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + 2 \sin x \cos x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t,</equation><equation>\begin{aligned} g ^ {\prime \prime} (x) &= 2 \sin x \cos x \mathrm {e} ^ {x ^ {2}} + 2 x \sin^ {2} x \mathrm {e} ^ {x ^ {2}} + \sin 2 x \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \\ &= 2 \left(\sin 2 x + x \sin^ {2} x\right) \mathrm {e} ^ {x ^ {2}} + 2 \cos 2 x \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t. \end{aligned}</equation>取<equation>\delta</equation>为充分小的正数，由于<equation>\mathrm{e}^{t^2}</equation>恒大于0，故当<equation>x\in(-\delta,0)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t < 0</equation>，结合<equation>\sin 2x < 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加，当<equation>x\in(0,\delta)</equation>时，<equation>\int_0^x\mathrm{e}^{t^2}\mathrm{d}t > 0</equation>，结合<equation>\sin 2x > 0</equation>可得，<equation>g^{\prime}(x) > 0,g(x)</equation>单调增加.于是，<equation>x = 0</equation>不是<equation>g(x)</equation>的极值点.

当<equation>x \in(-\delta,0)</equation>时，<equation>\sin 2x+x\sin^{2}x<0,\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t<0,\cos 2x>0,g^{\prime \prime}(x)<0,y=g(x)</equation>是凸曲线，当<equation>x \in(0,\delta)</equation>时，<equation>\sin 2x+x\sin^{2}x>0,\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t>0,\cos 2x>0,g^{\prime \prime}(x)>0,y=g(x)</equation>是凹曲线.于是，点（0,0）是曲线<equation>y=g(x)</equation>的拐点.

综上所述，应选B.

---

**2023年第1题 | 选择题 | 5分 | 答案: B**

1. 曲线<equation>y=x\ln \left(\mathrm{e}+\frac{1}{x-1}\right)</equation>的斜渐近线方程为（    )

A.<equation>y=x+\mathrm{e}</equation>B.<equation>y=x+\frac{1}{\mathrm{e}}</equation>C.<equation>y=x</equation>D.<equation>y=x-\frac{1}{\mathrm{e}}</equation>

答案: B

**解析:**先计算<equation>\lim_{x\to \infty}\frac{y}{x}</equation>.<equation>\lim _ {x \rightarrow \infty} \frac {y}{x} = \lim _ {x \rightarrow \infty} \frac {x \ln \left(\mathrm {e} + \frac {1}{x - 1}\right)}{x} = \lim _ {x \rightarrow \infty} \ln \left(\mathrm {e} + \frac {1}{x - 1}\right) = 1.</equation>由此可得斜渐近线的斜率为1.

下面计算<equation>\lim_{x\to \infty}(y-x).</equation>

<equation>\begin{aligned} \lim_{x \rightarrow \infty} (y - x) &= \lim_{x \rightarrow \infty}

  \left[ x \ln \left(\mathrm{e} + \frac{1}{x - 1}\right) - x \right] \\ &= \lim_{x
  \rightarrow \infty} x \left[ \ln \left(\mathrm{e} + \frac{1}{x - 1}\right) - 1 \right]
   \\ &= \lim_{x \rightarrow \infty} x \left[ \ln \left(\mathrm{e} + \frac{1}{x -
  1}\right) - \ln \mathrm{e} \right] \\ &= \lim_{x \rightarrow \infty} x \ln \left[ 1 +
  \frac{1}{\mathrm{e}(x - 1)} \right] \\ &= \underline{\underline{\ln \left[ 1 +
  \frac{1}{\mathrm{e}(x - 1)} \right] \sim \frac{1}{\mathrm{e}(x - 1)}}} \lim_{x
  \rightarrow \infty} x \cdot \frac{1}{\mathrm{e}(x - 1)} \\ &= \frac{1}{\mathrm{e}}.
  \end{aligned}

</equation>

因此，曲线<equation>y=x\ln \left(\mathrm{e}+\frac{1}{x-1}\right)</equation>的斜渐近线方程为<equation>y=x+\frac{1}{\mathrm{e}}.</equation>应选B.

---

**2022年第20题 | 解答题 | 12分**

20. (本题满分12分）

设函数 f(x)在<equation>(-\infty,+\infty)</equation>上有二阶连续导数，证明：<equation>f^{\prime \prime}(x)\geqslant0</equation>的充分必要条件是对任意不同的实数 a,b，都有<equation>f\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>成立.

**解析:**先证明必要性，即证明，若<equation>f^{\prime \prime}(x)\geqslant 0</equation>，则对不同的实数a,b，有<equation>f \left(\frac {a + b}{2}\right) \leqslant \frac {1}{b - a} \int_ {a} ^ {b} f (x) \mathrm {d} x.</equation>（法一）不妨设<equation>b > a</equation>. 在区间<equation>[a,b]</equation>上，使用<equation>f(x)</equation>在点<equation>\frac{a + b}{2}</equation>处的一阶泰勒公式.<equation>f (x) = f \left(\frac {a + b}{2}\right) + f ^ {\prime} \left(\frac {a + b}{2}\right) \left(x - \frac {a + b}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2},</equation>其中<equation>\xi_{x}</equation>介于 x与<equation>\frac{a+b}{2}</equation>之间.

将（1）式代入<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>，可得

<equation>\begin{aligned} \int_{a}^{b} f(x) \mathrm{d}x &= \int_{a}^{b} \left[ f\left(\frac{a +

  b}{2}\right) + f^{\prime}\left(\frac{a + b}{2}\right)\left(x - \frac{a + b}{2}\right)
  + \frac{1}{2} f^{\prime \prime}\left(\xi_{x}\right)\left(x - \frac{a +
  b}{2}\right)^{2} \right] \mathrm{d}x \\ &= f\left(\frac{a + b}{2}\right)(b - a) +
  f^{\prime}\left(\frac{a + b}{2}\right) \int_{a}^{b} \left(x - \frac{a + b}{2}\right)
  \mathrm{d}x \\ &\quad + \frac{1}{2} \int_{a}^{b} f^{\prime
  \prime}\left(\xi_{x}\right)\left(x - \frac{a + b}{2}\right)^{2} \mathrm{d}x.
  \end{aligned}

</equation>

注意到<equation>\int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) \mathrm {d} x = \frac {x ^ {2}}{2} \Big | _ {a} ^ {b} - \frac {(a + b) (b - a)}{2} = \frac {b ^ {2} - a ^ {2}}{2} - \frac {b ^ {2} - a ^ {2}}{2} = 0,</equation>故<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f \left(\frac {a + b}{2}\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x)\geqslant 0</equation>可得<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a+b}{2}\right)(b-a)</equation>，即<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>法二）不妨设<equation>b > a.</equation><equation>f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>等价于<equation>f\left(\frac{a + b}{2}\right)(b - a) - \int_{a}^{b}f(x)\mathrm{d}x\leqslant 0</equation>令<equation>F ( x ) = \int_{a}^{x} f ( t ) \mathrm{d} t - f \left( \frac{a + x}{2} \right) ( x - a ) , x \in [ a, b ]</equation>，则<equation>F ( a ) = 0</equation>，且<equation>\begin{aligned} F ^ {\prime} (x) &= f (x) - f \left(\frac {a + x}{2}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} f ^ {\prime} \left(\eta_ {x}\right) \frac {x - a}{2} - f ^ {\prime} \left(\frac {a + x}{2}\right) \frac {x - a}{2} \\ &= \left[ f ^ {\prime} \left(\eta_ {x}\right) - f ^ {\prime} \left(\frac {a + x}{2}\right) \right] \frac {x - a}{2}, \end{aligned}</equation>其中<equation>\eta_{x}\in \left(\frac{a + x}{2},x\right)</equation>由于<equation>f^{\prime \prime}(x)\geqslant 0</equation>，故<equation>f^{\prime}(x)</equation>单调不减，从而<equation>f^{\prime}(\eta_{x})\geqslant f^{\prime}\left(\frac{a+x}{2}\right)</equation>即<equation>f^{\prime}(\eta_{x})-f^{\prime}\left(\frac{a+x}{2}\right)\geqslant 0.</equation>于是，对<equation>x\in(a,b),F^{\prime}(x)\geqslant 0,F(x)</equation>在<equation>[a,b]</equation>上单调不减.

又因为<equation>F(a) = 0</equation>，所以<equation>F(b)\geqslant F(a) = 0</equation>，即<equation>\int_{a}^{b}f(x)\mathrm{d}x\geqslant f\left(\frac{a + b}{2}\right)(b - a)</equation>.

下面证明充分性，即证明，若对不同的实数 a,b,f<equation>\left(\frac{a+b}{2}\right)\leqslant\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则<equation>f^{\prime\prime}(x)\geqslant0.</equation>（法一）反证法.

假设存在<equation>x_{0}</equation>，使得<equation>f^{\prime \prime}(x_{0})<0</equation>，由二阶导数连续可得<equation>\lim_{x\to x_{0}}f^{\prime \prime}(x)=f^{\prime \prime}(x_{0})<0</equation>，结合极限的局部保号性可知，存在<equation>\delta >0</equation>，在区间<equation>(x_{0}-\delta,x_{0}+\delta)</equation>内，均有<equation>f^{\prime \prime}(x)<0</equation>.从而取<equation>[a_{0},b_{0}]\subset(x_{0}-\delta,x_{0}+\delta)</equation>可得在<equation>[a_{0},b_{0}]</equation>上，均有<equation>f^{\prime \prime}(x)<0.</equation>在区间<equation>[ a_{0}, b_{0} ]</equation>上重复必要性中的做法.<equation>\begin{aligned} \int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x &= \int_ {a _ {0}} ^ {b _ {0}} \left[ f \left(\frac {a _ {0} + b _ {0}}{2}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \right] \mathrm {d} x \\ &= f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + f ^ {\prime} \left(\frac {a _ {0} + b _ {0}}{2}\right) \int_ {a _ {0}} ^ {b _ {0}} \left(x - \frac {a _ {0} + b _ {0}}{2}\right) \mathrm {d} x \\ + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x, \end{aligned}</equation>其中<equation>\xi_{x}</equation>介于 x与<equation>\frac{a_{0}+b_{0}}{2}</equation>之间.

于是，<equation>\int_ {a _ {0}} ^ {b _ {0}} f (x) \mathrm {d} x = f \left(\frac {a _ {0} + b _ {0}}{2}\right) \left(b _ {0} - a _ {0}\right) + \frac {1}{2} \int_ {a _ {0}} ^ {b _ {0}} f ^ {\prime \prime} \left(\xi_ {x}\right) \left(x - \frac {a _ {0} + b _ {0}}{2}\right) ^ {2} \mathrm {d} x.</equation>结合<equation>f^{\prime \prime}(x) < 0</equation>可得<equation>\int_{a_0}^{b_0} f(x)\mathrm{d}x < f\left(\frac{a_0 + b_0}{2}\right)\left(b_0 - a_0\right)</equation>，即<equation>f\left(\frac{a_0 + b_0}{2}\right) > \frac{1}{b_0 - a_0}\int_{a_0}^{b_0} f(x)\mathrm{d}x.</equation>这与前提矛盾.

因此，假设不正确.<equation>f^{\prime \prime}(x)</equation>在<equation>(-\infty , +\infty)</equation>上恒非负.

（法二）若对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>，则对任意实数<equation>x_0</equation>以及任意<equation>\delta > 0</equation>，均有<equation>\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)\geqslant 0</equation>，从而<equation>\frac{\int_{x_0 - \delta}^{x_0 + \delta}f(x)\mathrm{d}x - 2\delta f(x_0)}{\delta^3}\geqslant 0.</equation>而<equation>\begin{aligned} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {\int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} f (x) \mathrm {d} x - 2 \delta f \left(x _ {0}\right)}{\delta^ {3}} \stackrel {\text {洛必达}} {=} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f \left(x _ {0} + \delta\right) + f \left(x _ {0} - \delta\right) - 2 f \left(x _ {0}\right)}{3 \delta^ {2}} \\ \stackrel {\text {洛必达}} {=} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime} \left(x _ {0} + \delta\right) - f ^ {\prime} \left(x _ {0} - \delta\right)}{6 \delta} \\ \stackrel {\text {洛必达}} {=} \lim _ {\delta \rightarrow 0 ^ {+}} \frac {f ^ {\prime \prime} \left(x _ {0} + \delta\right) + f ^ {\prime \prime} \left(x _ {0} - \delta\right)}{6} \\ \stackrel {f ^ {\prime \prime} \text {连 续}} {=} \frac {1}{3} f ^ {\prime \prime} \left(x _ {0}\right), \end{aligned}</equation>故由极限的保号性可知，<equation>f^{\prime \prime}\left(x_{0}\right)\geqslant 0.</equation>由<equation>x_0</equation>的任意性可知，对不同的实数<equation>a,b,f\left(\frac{a + b}{2}\right)\leqslant \frac{1}{b - a}\int_{a}^{b}f(x)\mathrm{d}x</equation>是<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分条件.

综上所述，<equation>f^{\prime \prime}(x)\geqslant 0</equation>的充分必要条件是对不同的实数a,b，<equation>f\left(\frac{a+b}{2}\right)\leqslant \frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x.</equation>

---

**2015年第1题 | 选择题 | 4分 | 答案: C**

1. 设函数 f(x)在<equation>(-\infty,+\infty)</equation>上连续，其2阶导函数<equation>f^{\prime\prime}(x)</equation>的图形如图所示，则曲线 y=f(x)的拐点个数为（    ）

A. 0 B. 1 C. 2 D. 3

答案: C

**解析:**图可知，在<equation>(-\infty, +\infty)</equation>上，<equation>f^{\prime \prime}(x) = 0</equation>有两个实根<equation>x_{1}, x_{2}</equation>，且<equation>f^{\prime \prime}(x)</equation>在<equation>x=0</equation>处无定义.

下面我们分别讨论点<equation>(x_{1}, f(x_{1}))</equation>，<equation>(0, f(0))</equation>和<equation>(x_{2}, f(x_{2}))</equation>是否为拐点.

在<equation>x = x_{1}</equation>的左、右邻域内，<equation>f^{\prime \prime}(x)</equation>均大于零.<equation>f^{\prime \prime}(x)</equation>在该点两侧不变号，故点<equation>(x_{1}, f(x_{1}))</equation>不是曲线<equation>y = f(x)</equation>的拐点.
