---

**2018年第22题 | 解答题 | 11分**

22. (本题满分11分)

设实二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=\left( x_{1}-x_{2}+x_{3} \right)^{2}+\left( x_{2}+x_{3} \right)^{2}+\left( x_{1}+a x_{3} \right)^{2}</equation>其中 a是参数.

I. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解;

II. 求<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>的规范形.

**答案:**（I）当 a≠2时，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=\left( 0,0,0\right)^{\mathrm{T}}</equation>；当 a=2时，<equation>f \left( x_{1}, x_{2}, x_{3}\right)=0</equation>的解为<equation>\left( x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=k \left( -2,-1,1\right)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>；当 a=2时， f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

**解析:**解（I）<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>当且仅当<equation>\left\{ \begin{array}{l l} x_{1}-x_{2}+x_{3}=0, \\ x_{2}+x_{3}=0, \\ x_{1}+a x_{3}=0. \end{array} \right.</equation>记 A为该方程组的系数矩阵.对 A作初等行变换.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & a \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 1 & - 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & a - 1 \end{array} \right) \xrightarrow {r _ {1} + r _ {2}} \left( \begin{array}{c c c} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & a - 2 \end{array} \right).</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）

当 a≠2时，<equation>r ( \mathbf{A} )=3</equation>，方程组只有零解.

当 a=2时，<equation>r ( \mathbf{A} )=2.</equation>方程组的基础解系仅包含一个向量.取<equation>x_{3}</equation>为自由变元，令<equation>x_{3}=1</equation>解得<equation>\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}=\left(-2,-1,1\right)^{\mathrm{T}}</equation>为该方程组的一个基础解系.

因此，当 a≠2时，<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解为<equation>\left(x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=\left(0, 0, 0\right)^{\mathrm{T}}</equation>；当 a=2时，<equation>f \left( x_{1}, x_{2}, x_{3} \right)=0</equation>的解为<equation>\left(x_{1}, x_{2}, x_{3}\right)^{\mathrm{T}}=k \left(-2,-1,1\right)^{\mathrm{T}}</equation>其中 k为任意常数.

（Ⅱ）由<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>的表达式知，<equation>f\left(x_{1},x_{2},x_{3}\right)\geqslant 0.</equation>当 a≠2时，由第（I）问可知，<equation>f ( x_{1}, x_{2}, x_{3} )=0</equation>只有零解，f为正定二次型.因此，当 a≠2时， f的规范形为<equation>f=y_{1}^{2}+y_{2}^{2}+y_{3}^{2}.</equation>当 a=2时，f不满秩.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} - x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {2} + x _ {3}\right) ^ {2} + \left(x _ {1} + 2 x _ {3}\right) ^ {2} \\ &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3}. \end{aligned}</equation>记f对应的对称矩阵为<equation>B=\left( \begin{array}{c c c} 2 & -1 & 3 \\ -1 & 2 & 0 \\ 3 & 0 & 6 \end{array} \right).</equation>下面用三种方法求 f的规范形.

（法一）由<equation>f ( x_{1}, x_{2}, x_{3} ) \geqslant0</equation>可知 f的负惯性指数为0（否则，若规范形有负系数，不妨设规范形为<equation>f=y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>，取<equation>( y_{1}, y_{2}, y_{3} )=(0,0,1)</equation>，则<equation>f ( y_{1}, y_{2}, y_{3} )=-1<0</equation>，矛盾）.由于B的秩等于f的正、负惯性指数之和，故 f的正惯性指数等于r（B）.

计算<equation>| B |</equation>得<equation>| B |=0</equation>，故<equation>r ( B ) \leqslant2</equation>. 又因为B有一个2阶子式<equation>\left| \begin{array}{c c} {2} & {-1} \\ {-1} & {2} \end{array} \right|=3\neq0</equation>，所以<equation>r ( B ) \geqslant2.</equation>因此，<equation>r ( B )=2.</equation>综上所述，f的正惯性指数为2，负惯性指数为0.f的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>（法二）计算 B的特征值，从而得到 f的正、负惯性指数.

计算 B的特征多项式.<equation>| \lambda E - B | = \left| \begin{array}{c c c} \lambda - 2 & 1 & - 3 \\ 1 & \lambda - 2 & 0 \\ - 3 & 0 & \lambda - 6 \end{array} \right| = \lambda \left(\lambda^ {2} - 1 0 \lambda + 1 8\right).</equation>解<equation>\lambda^{2}-1 0 \lambda+1 8=0</equation>可得<equation>\lambda_{1,2}=\frac{1 0 \pm \sqrt{1 0 0}-7 2}{2}=5 \pm \sqrt{7}.</equation>由于<equation>5+\sqrt{7}>0, 5-\sqrt{7}>0</equation>，故f有两个正特征值，一个零特征值，从而f的正惯性指数为2，负惯性指数为0.

因此，<equation>f</equation>的规范形为<equation>f = z_{1}^{2} + z_{2}^{2}</equation>.

（法三）配方法.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= 2 x _ {1} ^ {2} + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} - 2 x _ {1} x _ {2} + 6 x _ {1} x _ {3} = 2 \left(x _ {1} ^ {2} - x _ {1} x _ {2} + 3 x _ {1} x _ {3}\right) + 2 x _ {2} ^ {2} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} x _ {2} ^ {2} - \frac {9}{2} x _ {3} ^ {2} + 3 x _ {2} x _ {3} + 6 x _ {3} ^ {2} \\ &= 2 \left(x _ {1} - \frac {x _ {2}}{2} + \frac {3}{2} x _ {3}\right) ^ {2} + \frac {3}{2} \left(x _ {2} + x _ {3}\right) ^ {2}. \end{aligned}</equation>令<equation>\left\{ \begin{array}{l l} z_{1}=\sqrt{2}\left(x_{1}-\frac{x_{2}}{2}+\frac{3}{2} x_{3}\right), \\ z_{2}=\sqrt{\frac{3}{2}}\left(x_{2}+x_{3}\right), \\ z_{3}=x_{3}, \end{array} \right.</equation>则<equation>f \left(z_{1}, z_{2}, z_{3}\right)=z_{1}^{2}+z_{2}^{2}.</equation>因此，<equation>f</equation>的规范形为<equation>f=z_{1}^{2}+z_{2}^{2}.</equation>

---

**2017年第23题 | 解答题 | 11分**

23. (本题满分11分)

设二次型<equation>f \left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}-x_{2}^{2}+a x_{3}^{2}+2 x_{1} x_{2}-8 x_{1} x_{3}+2 x_{2} x_{3}</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>求 a的值及一个正交矩阵 Q.

**答案:**a=2，<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>，即f在正交变换 x = Qy下的标准

形为<equation>f=6 y_{1}^{2}-3 y_{2}^{2}.</equation>

**解析:**解 记二次型 f对应的实对称矩阵为 A，则<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 2 & 1 & - 4 \\ 1 & - 1 & 1 \\ - 4 & 1 & a \end{array} \right).</equation>由于 f在正交变换<equation>x=Q y</equation>下的标准形为<equation>\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}</equation>，故 A的特征值为<equation>\lambda_{1},\lambda_{2},0.</equation>从而<equation>|A|=0.</equation>计算 A的行列式得<equation>| A | = - 3 a + 6.</equation>因此，<equation>a = 2</equation>，<equation>A = \left( \begin{array}{c c c} 2 & 1 & -4 \\ 1 & -1 & 1 \\ -4 & 1 & 2 \end{array} \right).</equation>计算 A的特征多项式得<equation>| \lambda E - A | = \left| \begin{array}{c c c} \lambda - 2 & - 1 & 4 \\ - 1 & \lambda + 1 & - 1 \\ 4 & - 1 & \lambda - 2 \end{array} \right| = \lambda^ {3} - 3 \lambda^ {2} - 1 8 \lambda = \lambda (\lambda - 6) (\lambda + 3).</equation>于是，A的3个特征值分别为6，-3，0.

当<equation>\lambda=6</equation>时，<equation>\begin{array}{l} 6 E - A = \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 4 & - 1 & 4 \end{array} \right) \xrightarrow {r _ {3} - r _ {1}} \left( \begin{array}{c c c} 4 & - 1 & 4 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} + 4 r _ {2}} \left( \begin{array}{c c c} 0 & 1 & 0 \\ - 1 & 7 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} - 7 r _ {1} ^ {* *}} r _ {2} ^ {*} \times (- 1) \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation>（<equation>r_{i}^{*}</equation>表示对第 i 行作初等行变换后所得新的第 i 行，每作一次初等行变换，加一个*.）<equation>(6E - A)x = 0</equation>的一个基础解系为<equation>\eta_1 = (-1,0,1)^{\mathrm{T}}.</equation>当<equation>\lambda=-3</equation>时，<equation>\begin{array}{l} - 3 E - A = \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 4 & - 1 & - 5 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \frac {r _ {3} ^ {*} - r _ {2}}{r _ {3} ^ {*}} \left( \begin{array}{c c c} - 5 & - 1 & 4 \\ - 1 & - 2 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 5 r _ {2}} \frac {r _ {1} - 5 r _ {2}}{r _ {2} \times (- 1)} \left( \begin{array}{c c c} 0 & 9 & 9 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {1} ^ {*} \times \frac {1}{9}} \frac {r _ {2} ^ {*} - r _ {1} ^ {* *}}{r _ {2} ^ {*} - r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(-3E - A)x = 0</equation>的一个基础解系为<equation>\eta_2 = (1, -1, 1)^{\mathrm{T}}.</equation>当<equation>\lambda=0</equation>时，<equation>\begin{array}{l} 0 E - A = \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 4 & - 1 & - 2 \end{array} \right) \xrightarrow {r _ {3} + r _ {1}} \frac {r _ {3} ^ {*} + 2 r _ {2}}{r _ {3} ^ {*} + 2 r _ {2}} \left( \begin{array}{c c c} - 2 & - 1 & 4 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \xrightarrow {r _ {1} - 2 r _ {2}} \frac {r _ {1} ^ {*} \times \left(- \frac {1}{3}\right)}{r _ {1} ^ {*} \times \left(- \frac {1}{3}\right)} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ - 1 & 1 & - 1 \\ 0 & 0 & 0 \end{array} \right) \\ \xrightarrow {r _ {2} \times (- 1) + r _ {1} ^ {* *}} \left( \begin{array}{c c c} 0 & 1 & - 2 \\ 1 & 0 & - 1 \\ 0 & 0 & 0 \end{array} \right). \\ \end{array}</equation><equation>(0E - A)x = 0</equation>的一个基础解系为<equation>\eta_3 = (1,2,1)^{\mathrm{T}}.</equation>由于实对称矩阵对应于不同特征值的特征向量相互正交，故只需要将所得特征向量单位化.

将<equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\boldsymbol{\eta}_{3}</equation>分别单位化，作为Q的列向量，得正交矩阵<equation>Q=\left( \begin{array}{c c c} -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{3}} & \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \end{array} \right)</equation>，且<equation>Q^{\mathrm{T}}AQ=</equation><equation>\left( \begin{array}{c c c} 6 & 0 & 0 \\ 0 & - 3 & 0 \\ 0 & 0 & 0 \end{array} \right)</equation>即f在正交变换<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>f=6 y_{1}^{2}-3 y_{2}^{2}.</equation>

---

**2016年第8题 | 选择题 | 4分 | 答案: C**

8. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=a \left( x_{1}^{2}+x_{2}^{2}+x_{3}^{2} \right)+2 x_{1} x_{2}+2 x_{2} x_{3}+2 x_{1} x_{3}</equation>的正、负惯性指数分别为1，2，则（    )

A. a > 1 B. a < -2 C.<equation>- 2 < a < 1</equation>D. a=1或a=-2

答案: C

**解析:**解（法一）f对应的对称矩阵为<equation>A=\left( \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right).</equation>A正交相似于一个对角矩阵，该矩阵的主对角元为 A的特征值.

计算 A的特征多项式，得<equation>\begin{aligned} | \lambda E - A | &= \left| \begin{array}{c c c} \lambda - a & - 1 & - 1 \\ - 1 & \lambda - a & - 1 \\ - 1 & - 1 & \lambda - a  \right| \xlongequal {c _ {2} - c _ {3}} \left| \begin{array}{c c c} \lambda - a & 0 & - 1 \\ - 1 & \lambda - a + 1 & - 1 \\ - 1 & - (\lambda - a + 1) & \lambda - a  \right| \\ \underline {{\text {按 第一 行 展 开}}} (\lambda - a) (\lambda - a + 1) (\lambda - a - 1) - 2 (\lambda - a + 1) \\ &= (\lambda - a + 1) ^ {2} (\lambda - a - 2). \end{aligned}</equation>因此，A的特征值为 a-1，a-1，a+2.

由于 a+2>a-1，故若 f的正、负惯性指数分别为1，2，则<equation>\left\{\begin{array}{l l}a-1<0,\\ a+2>0.\end{array}\right.</equation>解得-2<a<1.应选C.

（法二）如法一，写出 A.

由于二次型 f的正、负惯性指数分别为1，2，故 A的特征值有一个为正值，两个为负值，从而<equation>| A | > 0.</equation>计算 A的行列式.<equation>| A | = \left| \begin{array}{c c c} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{array} \right| = (a - 1) ^ {2} (a + 2).</equation>由于<equation>| A | > 0</equation>，故<equation>a+2>0</equation>，即<equation>a>-2.</equation>由此可以排除选项B和选项D.

另一方面，若 a > 1，则 a > 0，<equation>a^{2}-1>0</equation><equation>| A | > 0</equation>，A的各阶顺序主子式皆为正.由正定矩阵的判别法可知，A为正定矩阵，从而 f的正惯性指数为3.与f的正、负惯性指数分别为1，2矛盾，故可排除选项A.

因此，应选C.

---

**2015年第8题 | 选择题 | 4分 | 答案: A**

8. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=P y</equation>下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>其中<equation>P=\left( e_{1}, e_{2}, e_{3} \right)</equation>若<equation>Q=\left( e_{1},-e_{3}, e_{2} \right)</equation>则<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在正交变换<equation>x=Q y</equation>下的标准形为（    )

A.<equation>2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}</equation>B.<equation>2 y_{1}^{2}+y_{2}^{2}-y_{3}^{2}</equation>C.<equation>2 y_{1}^{2}-y_{2}^{2}-y_{3}^{2}</equation>D.<equation>2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2}</equation>

答案: A

**解析:**解（法一）由题设知，二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>对应的对称矩阵 A满足<equation>P^{\mathrm{T}} A P=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right).</equation>又由题设，<equation>Q=P\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)</equation>，故<equation>Q^{\mathrm{T}} A Q=\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right)\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{array} \right)\left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array} \right)=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right).</equation>因此，<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>在 x = Qy下的标准形为<equation>f=2 y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

（法二）由题设知，二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>在正交变换<equation>\boldsymbol{x}=\boldsymbol{P}\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}+y_{2}^{2}-y_{3}^{2}.</equation>因此，该二次型所对应的对称矩阵A的特征值为2，1，-1，而<equation>e_{1},e_{2},e_{3}</equation>分别为属于特征值2，1，-1的特征向量.

若<equation>Q=\left(e_{1},-e_{3},e_{2}\right)</equation>，则由<equation>A(-e_{3})=-Ae_{3}=-(-e_{3})</equation>可知<equation>-e_{3}</equation>也为属于特征值-1的特征向量，故<equation>Q^{\mathrm{T}}AQ=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{array} \right). f\left(x_{1},x_{2},x_{3}\right)</equation>在<equation>\boldsymbol{x}=\boldsymbol{Q}\boldsymbol{y}</equation>下的标准形为<equation>f=2y_{1}^{2}-y_{2}^{2}+y_{3}^{2}.</equation>应选A.

---

**2014年第14题 | 填空题 | 4分**

14. 设二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)=x_{1}^{2}-x_{2}^{2}+2 a x_{1} x_{3}+4 x_{2} x_{3}</equation>的负惯性指数为1，则 a的取值范围是 ___

**解析:**解 （法一）用配方法将原二次型化为标准形.<equation>\begin{aligned} f \left(x _ {1}, x _ {2}, x _ {3}\right) &= \left(x _ {1} + a x _ {3}\right) ^ {2} - a ^ {2} x _ {3} ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + 4 x _ {3} ^ {2} \\ &= \left(x _ {1} + a x _ {3}\right) ^ {2} - \left(x _ {2} - 2 x _ {3}\right) ^ {2} + \left(4 - a ^ {2}\right) x _ {3} ^ {2}. \end{aligned}</equation>因此，若二次型<equation>f(x_{1},x_{2},x_{3})</equation>的负惯性指数为1，则<equation>4 - a^{2}\geqslant 0</equation>，即<equation>a\in [-2,2]</equation>（法二）写出二次型<equation>f\left(x_{1},x_{2},x_{3}\right)</equation>对应的对称矩阵A.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & a \\ 0 & - 1 & 2 \\ a & 2 & 0 \end{array} \right).</equation>计算<equation>A</equation>的行列式得，<equation>|A| = a^{2} - 4.</equation>A的迹等于零，说明A的特征值之和为零.

下面我们证明，当3阶非零实对称矩阵<equation>A</equation>的迹为零时，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0.</equation>当3阶非零实对称矩阵<equation>A</equation>的迹为零时，由<equation>A</equation>的负惯性指数为1可知，<equation>A</equation>的特征值可能为两正、一负，或者一正、一零、一负.在这两种情形下，<equation>|A| \leqslant 0.</equation>若 A为3阶非零实对称矩阵，且<equation>|A| \leqslant 0</equation>，则 A的特征值的符号有五种可能：（1）两正、一负；（2）一正、一零、一负；（3）两零、一负；（4）三负；（5）全为零.两个零特征值、一个负特征值与三个负特征值的情形与 A的迹为零矛盾.特征值全为零的情形与 A是非零实对称矩阵矛盾，因为若 A的特征值全为零，则 A相似于零矩阵，从而 A为零矩阵.因此，A的特征值仅可能为两正、一负，或一正、一零、一负.在这两种情形下，A的负惯性指数都为1.

综上所述，<equation>A</equation>的负惯性指数为1等价于<equation>|A| \leqslant 0</equation>，即<equation>a \in [-2,2]</equation>

---

**2013年第23题 | 解答题 | 11分**


设二次型<equation>f\left(x_{1},x_{2},x_{3}\right)=2\left(a_{1}x_{1}+a_{2}x_{2}+a_{3}x_{3}\right)^{2}+\left(b_{1}x_{1}+b_{2}x_{2}+b_{3}x_{3}\right)^{2}</equation>，记<equation>\begin{aligned} \alpha &= \left(  a _ {1} \\ a _ {2} \\ a _ {3}  \right), \quad \beta &= \left(  b _ {1} \\ b _ {2} \\ b _ {3}  \right) \end{aligned}</equation>I. 证明二次型 f对应的矩阵为<equation>2\alpha\alpha^{\mathrm{T}}+\beta\beta^{\mathrm{T}};</equation>II. 若<equation>\alpha, \beta</equation>正交且均为单位向量，证明 f在正交变换下的标准形为<equation>2 y_{1}^{2}+y_{2}^{2}.</equation>

**答案:**（23）（Ⅰ）证明略；

（Ⅱ）证明略.

**解析:**证（I）记<equation>\boldsymbol{x}=\left(x_{1},x_{2},x_{3}\right)^{\mathrm{T}}</equation><equation>f</equation>对应的矩阵为A,A为对称矩阵，则<equation>a _ {1} x _ {1} + a _ {2} x _ {2} + a _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}, \quad b _ {1} x _ {1} + b _ {2} x _ {2} + b _ {3} x _ {3} = \boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta} = \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}.</equation><equation>f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\alpha}\right) \left(\boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {x}\right) + \left(\boldsymbol {x} ^ {\mathrm {T}} \boldsymbol {\beta}\right) \left(\boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {x}\right) = \boldsymbol {x} ^ {\mathrm {T}} \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \boldsymbol {x}.</equation>又由于<equation>(2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}})^{\mathrm{T}} = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>，故<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>是对称矩阵.于是<equation>2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>为所求A.

（Ⅱ）（法一）由<equation>A = 2\alpha \alpha^{\mathrm{T}} + \beta \beta^{\mathrm{T}}</equation>且<equation>\alpha</equation>与<equation>\beta</equation>相互正交<equation>(\alpha^{\mathrm{T}}\beta = 0, \beta^{\mathrm{T}}\alpha = 0)</equation>得，<equation>A \alpha = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \alpha = 2 \alpha , \quad A \beta = \left(2 \alpha \alpha^ {\mathrm {T}} + \beta \beta^ {\mathrm {T}}\right) \beta = \beta .</equation>因此，2,1均为<equation>A</equation>的特征值，而<equation>\alpha ,\beta</equation>分别为属于特征值2，1的特征向量.

下面还需确定 A的另一个特征值.

考虑 A的秩.

由于对任何非零<equation>n</equation>维列向量<equation>\alpha ,\beta ,</equation>矩阵<equation>\beta \alpha^{\mathrm{T}}</equation>的秩均为1，故<equation>r (\boldsymbol {A}) = r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) \leqslant r \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}}\right) + r \left(\boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) = 2.</equation>于是，<equation>\mathbf{A}</equation>不满秩，0也是<equation>\mathbf{A}</equation>的特征值.

因此，存在正交矩阵<equation>P</equation>使得<equation>P^{\mathrm{T}}AP=\left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right). f</equation>在正交变换<equation>x=Py</equation>下的标准形为<equation>f=2y_{1}^{2}+y_{2}^{2}.</equation>（法二）取<equation>\gamma</equation>为与<equation>\alpha, \beta</equation>均正交的单位向量，可取<equation>\gamma = \frac{\alpha \times \beta}{\| \alpha \times \beta \|}</equation><equation>(\alpha \times \beta</equation>为向量<equation>\alpha, \beta</equation>的向量积，<equation>\| \alpha \times \beta \|</equation>是向量<equation>\alpha \times \beta</equation>的模），则<equation>P=(\alpha ,\beta ,\gamma)</equation>为正交矩阵.<equation>\begin{aligned} P ^ {\mathrm {T}} A P &= \left(  \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \boldsymbol {\gamma} ^ {\mathrm {T}}  \right) \left(2 \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}\right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) &= \left(  2 \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\beta} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}} \\ 2 \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\alpha} \boldsymbol {\alpha} ^ {\mathrm {T}} + \boldsymbol {\gamma} ^ {\mathrm {T}} \boldsymbol {\beta} \boldsymbol {\beta} ^ {\mathrm {T}}  \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma). \end{aligned}</equation>由于<equation>\alpha, \beta, \gamma</equation>相互正交，故<equation>\alpha^{\mathrm{T}}\boldsymbol{\beta} = \beta^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\alpha = \gamma^{\mathrm{T}}\boldsymbol{\beta} = 0, \alpha^{\mathrm{T}}\alpha = \beta^{\mathrm{T}}\boldsymbol{\beta} = 1.</equation><equation>\boldsymbol {P} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {P} = \left( \begin{array}{c} 2 \boldsymbol {\alpha} ^ {\mathrm {T}} \\ \boldsymbol {\beta} ^ {\mathrm {T}} \\ \mathbf {0} \end{array} \right) (\boldsymbol {\alpha}, \boldsymbol {\beta}, \gamma) = \left( \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{array} \right).</equation>因此，<equation>f</equation>在正交变换<equation>\pmb{x} = \pmb{P}\pmb{y}</equation>下的标准形为<equation>f = 2y_{1}^{2} + y_{2}^{2}</equation>.

---

**2012年第23题 | 解答题 | 11分**

23. （本题满分11分）

已知<equation>A=\left( \begin{array}{c c c}1&0&1\\ 0&1&1\\ -1&0&a\\ 0&a&-1 \end{array} \right),</equation>二次型<equation>f \left( x_{1}, x_{2}, x_{3}\right)=\boldsymbol{x}^{\mathrm{T}} \left( \boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}</equation>的秩为2.

I. 求实数 a的值；

II. 求正交变换<equation>x=Q y</equation>将 f化为标准形.

**答案:**(23) （I）<equation>a=-1;</equation>（Ⅱ）<equation>Q=\left( \begin{array}{c c c} {\frac{1}{\sqrt{6}}} & {-\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{1}{\sqrt{6}}} & {\frac{1}{\sqrt{2}}} & {-\frac{1}{\sqrt{3}}} \\ {\frac{2}{\sqrt{6}}} & {0} & {\frac{1}{\sqrt{3}}} \end{array} \right)</equation>正交变换<equation>x=Q y</equation>将二次型<equation>f \left( x_{1}, x_{2}, x_{3} \right)</equation>变成标准形<equation>f = 6 y _ {1} ^ {2} + 2 y _ {2} ^ {2}.</equation>

**解析:**解（I）（法一）二次型<equation>f</equation>的秩等于它所对应的实对称矩阵<equation>A^{\mathrm{T}}A</equation>的秩，于是<equation>r(A^{\mathrm{T}}A) = 2.</equation><equation>r \left(\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A}\right) = r (\boldsymbol {A})</equation>由于<equation>A^{\mathrm{T}}A</equation>与A的列数相等，故证明<equation>r(A^{\mathrm{T}}A)=r(A)</equation>只需要证明<equation>A^{\mathrm{T}}Ax=0</equation>与<equation>Ax=0</equation>同解若 x满足<equation>Ax=0</equation>，则<equation>A^{\mathrm{T}}(Ax)=0</equation>即<equation>(A^{\mathrm{T}}A)x=0.</equation>另一方面，若 x满足<equation>\left( A^{\mathrm{T}} A \right) x=0</equation>，则<equation>x^{\mathrm{T}} \left( A^{\mathrm{T}} A \right) x=0</equation>，即<equation>\left( A x \right)^{\mathrm{T}} \left( A x \right)=0</equation>.由于<equation>\alpha^{\mathrm{T}}\alpha=0</equation>当且仅当<equation>\alpha=0</equation>，故<equation>A x=0.</equation><equation>\text {因 此}, r (\mathbf {A}) = r \left(\mathbf {A} ^ {\mathrm {T}} \mathbf {A}\right) = 2</equation>我们可以对<equation>A</equation>作初等行变换，求得<equation>r(A) = 2</equation>时的<equation>a</equation>的值.<equation>\boldsymbol {A} = \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) \xrightarrow [ r _ {4} - a r _ {2} ]{r _ {3} + r _ {1}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & - a - 1 \end{array} \right) \xrightarrow [ r _ {4} ^ {*} + r _ {3} ^ {*} ]{r _ {4} ^ {*} + r _ {3} ^ {*}} \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & a + 1 \\ 0 & 0 & 0 \end{array} \right).</equation>由此看出，仅当<equation>a + 1 = 0</equation>时，<equation>r(A) = 2</equation>，故<equation>a = -1.</equation>（法二）由于<equation>r(\mathbf{A}^{\mathrm{T}}\mathbf{A}) = 2</equation>，而<equation>\mathbf{A}^{\mathrm{T}}\mathbf{A}</equation>为<equation>3\times 3</equation>矩阵，故<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0.</equation><equation>\boldsymbol {A} ^ {\mathrm {T}} \boldsymbol {A} = \left( \begin{array}{c c c c} 1 & 0 & - 1 & 0 \\ 0 & 1 & 0 & a \\ 1 & 1 & a & - 1 \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 1 \\ 0 & 1 & 1 \\ - 1 & 0 & a \\ 0 & a & - 1 \end{array} \right) = \left( \begin{array}{c c c} 2 & 0 & 1 - a \\ 0 & 1 + a ^ {2} & 1 - a \\ 1 - a & 1 - a & 3 + a ^ {2} \end{array} \right).</equation>求得<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = (a^{2} + 3)(a + 1)^{2}</equation>. 因此，由<equation>|\mathbf{A}^{\mathrm{T}}\mathbf{A}| = 0</equation>可得<equation>a = -1</equation>.

（Ⅱ）由第（I）问可得，<equation>A^{\mathrm{T}}A = \left( \begin{array}{c c c} 2 & 0 & 2 \\ 0 & 2 & 2 \\ 2 & 2 & 4 \end{array} \right)</equation>从而<equation>A^{\mathrm{T}}A</equation>的特征多项式为<equation>| \lambda E - A ^ {\mathrm {T}} A | = \left| \begin{array}{c c c} \lambda - 2 & 0 & - 2 \\ 0 & \lambda - 2 & - 2 \\ - 2 & - 2 & \lambda - 4 \end{array} \right| = \lambda (\lambda - 2) (\lambda - 6).</equation><equation>A^{\mathrm{T}}A</equation>的特征值为6,2,0.

下面分别计算属于特征值6，2，0的特征向量

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

