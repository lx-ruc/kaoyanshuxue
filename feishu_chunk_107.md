#### 二维随机变量及其分布

**2024年第10题 | 选择题 | 5分 | 答案: D**
10. 设随机变量 X，Y相互独立，且均服从参数为<equation>\lambda</equation>的指数分布.令<equation>Z=|X-Y|</equation>，则下列随机变量与 Z同分布的是（    )

A.<equation>X+Y</equation>B.<equation>\frac{X+Y}{2}</equation>C. 2X D. X
答案: D
**解析: **解 由于<equation>X, Y</equation>相互独立，且均服从参数为<equation>\lambda</equation>的指数分布，故<equation>(X, Y)</equation>的联合概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>F_{z}(z)</equation>为<equation>Z=|X-Y|</equation>的分布函数，<equation>D_{z}=\{(x,y)|-z\leq x-y\leq z\}</equation>，则<equation>F _ {z} (z) = P \left\{Z \leqslant z \right\} = P \left\{| X - Y | \leqslant z \right\} = P \left\{- z \leqslant X - Y \leqslant z \right\} = \iint_ {D.} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>当<equation>z < 0</equation>时，<equation>D_{z} = \varnothing , F_{Z}(z) = 0.</equation>当<equation>z \geqslant 0</equation>时，记<equation>D = \{(x,y)|x \geqslant 0,y \geqslant 0\}</equation>，则<equation>D \cap D_{z} \neq \emptyset</equation>，为图（a）中的灰色区域.

(a)

(b)

(c)

下面用两种方法计算<equation>z\geqslant 0</equation>时的<equation>F_{z}(z)</equation>.

（法一）如图（a）所示，由于<equation>D \cap D_{z}</equation>关于直线<equation>y=x</equation>对称，故记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{0}.</equation>将<equation>D_{0}</equation>写成Y型区域，<equation>D_{0}=\left\{(x,y)\mid y\leqslant x\leqslant y+z,0\leqslant y<+\infty\right\}.</equation><equation>\begin{aligned} F _ {Z} (z) &= \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \xlongequal {\text {轮 换 对称 性}} 2 \iint_ {D _ {0}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ &= 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y} ^ {y + z} \mathrm {e} ^ {- \lambda x} \mathrm {d} x = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \Bigg | _ {x = y} ^ {x = y + z} \mathrm {d} y \\ &= - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \left(\mathrm {e} ^ {- \lambda y - \lambda z} - \mathrm {e} ^ {- \lambda y}\right) \mathrm {d} y = - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {d} y \\ &= \left(\mathrm {e} ^ {- \lambda z} - 1\right) \int_ {0} ^ {+ \infty} \left(- 2 \lambda \mathrm {e} ^ {- 2 \lambda y}\right) \mathrm {d} y = \left(\mathrm {e} ^ {- \lambda z} - 1\right) \mathrm {e} ^ {- 2 \lambda y} \Bigg | _ {0} ^ {+ \infty} \\ &= \left(\mathrm {e} ^ {- \lambda z} - 1\right) \cdot (- 1) = 1 - \mathrm {e} ^ {- \lambda z}. \end{aligned}</equation>（法二）如图(b)所示，<equation>D_{1}=D\backslash D_{z}</equation>关于直线<equation>y=x</equation>对称，记其位于直线<equation>y=x</equation>下方的部分为<equation>D_{2}.</equation>将<equation>D_{2}</equation>写成Y型区域，<equation>D_{2}=\left\{(x,y)\mid y+z\leqslant x<+\infty ,0\leqslant y<+\infty \right\}.</equation><equation>\begin{aligned} F _ {Z} (z) &= \iint_ {D _ {z}} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D \cap D _ {z}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = 1 - \iint_ {D _ {1}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y \\ \underline {{\text {轮换 对称性}}} 1 - 2 \iint_ {D _ {2}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y &= 1 - 2 \lambda^ {2} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \mathrm {d} y \int_ {y + z} ^ {+ \infty} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \\ &= 1 + 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda x} \left| _ {x = y + z} ^ {+ \infty} \mathrm {d} y = 1 - 2 \lambda \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \lambda y} \cdot \mathrm {e} ^ {- \lambda (y + z)} \mathrm {d} y \right. \\ &= 1 - 2 \lambda \mathrm {e} ^ {- \lambda z} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- 2 \lambda y} \mathrm {d} y = 1 + \mathrm {e} ^ {- \lambda z} \cdot \mathrm {e} ^ {- 2 \lambda y} \Big | _ {0} ^ {+ \infty} = 1 - \mathrm {e} ^ {- \lambda z}. \end{aligned}</equation>因此，<equation>F_{z}(z)=\left\{ \begin{array}{ll}1-\mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. f_{z}(z)=\left\{ \begin{array}{ll}\lambda \mathrm{e}^{-\lambda z},& z\geqslant 0,\\ 0,& \text{其他}, \end{array} \right. Z</equation>服从参数为<equation>\lambda</equation>的指数分布.进一步可得，Z与X同分布.选项D正确，选项C错误.

下面说明选项A、B不正确.

对选项A，当<equation>z \geqslant 0</equation>时，由于<equation>D_{3} = \{(x,y) \mid x + y \leqslant z, x \geqslant 0, y \geqslant 0\}</equation>真包含于<equation>D \cap D_{z}</equation>，故<equation>X + Y</equation>的分布函数<equation>F_{1}(z)</equation>满足，对任意<equation>z > 0, F_{1}(z) < F_{Z}(z)</equation>. 从而<equation>X + Y</equation>与<equation>Z</equation>不同分布.

对选项B，当<equation>z\geqslant 0</equation>时，记<equation>D_{4} = \{(x,y)|x + y\leqslant 2z,x\geqslant 0,y\geqslant 0\}</equation>，则<equation>\frac{X+Y}{2}</equation>的分布函数<equation>\begin{array}{l} F _ {2} (z) = \iint_ {D _ {4}} \lambda^ {2} \mathrm {e} ^ {- \lambda (x + y)} \mathrm {d} x \mathrm {d} y = \lambda^ {2} \int_ {0} ^ {2 x} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \int_ {0} ^ {2 z - x} \mathrm {e} ^ {- \lambda y} \mathrm {d} y = 1 - (2 \lambda z + 1) \mathrm {e} ^ {- 2 \lambda z} \\ \neq F _ {z} (z). \\ \end{array}</equation>从而<equation>\frac{X+Y}{2}</equation>与Z不同分布.

综上所述，应选D.

---


### 数理统计的基本概念

**2023年第9题 | 选择题 | 5分 | 答案: D**

9. 设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体<equation>N(\mu_{1},\sigma^{2})</equation>的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自总体<equation>N(\mu_{2},2\sigma^{2})</equation>的简单随机样本，且两样本相互独立，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i},\bar{Y}=\frac{1}{m}\sum_{i=1}^{m}Y_{i},S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar{X})^{2},S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}(Y_{i}-\bar{Y})^{2}</equation>，则（    )

A.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>B.<equation>\frac{S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>C.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n,m)</equation>D.<equation>\frac{2S_{1}^{2}}{S_{2}^{2}}\sim F(n-1,m-1)</equation>

答案: D

**解析:**解<equation>S_{1}^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\overline{X}\right)^{2}</equation>为<equation>X_{1},X_{2},\dots,X_{n}</equation>的样本方差，<equation>S_{2}^{2}=\frac{1}{m-1}\sum_{i=1}^{m}\left(Y_{i}-\overline{Y}\right)^{2}</equation>为<equation>Y_{1},</equation><equation>Y_{2},\dots,Y_{m}</equation>的样本方差.由正态总体的抽样分布定理可知，<equation>\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1), \quad \frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} \sim \chi^ {2} (m - 1).</equation>又因为两个样本相互独立，所以由<equation>F</equation>分布的定义可知<equation>\frac {\frac {(n - 1) S _ {1} ^ {2}}{\sigma^ {2}} / (n - 1)}{\frac {(m - 1) S _ {2} ^ {2}}{2 \sigma^ {2}} / (m - 1)} = \frac {S _ {1} ^ {2} / \sigma^ {2}}{S _ {2} ^ {2} / 2 \sigma^ {2}} = \frac {2 S _ {1} ^ {2}}{S _ {2} ^ {2}} \sim F (n - 1, m - 1).</equation>因此，应选D.

---

**2017年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \dots , X_{n} ( n \geqslant 2 )</equation>为来自总体<equation>N (\mu , 1)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>，则下列结论中不正确的是（    )

A.<equation>\sum_{i=1}^{n} \left(X_{i}-\mu\right)^{2}</equation>服从<equation>\chi^{2}</equation>分布 B.<equation>2 \left(X_{n}-X_{1}\right)^{2}</equation>服从<equation>\chi^{2}</equation>分布

C.<equation>\sum_{i=1}^{n} \left(X_{i}-\bar{X}\right)^{2}</equation>服从<equation>\chi^{2}</equation>分布 D.<equation>n(\bar{X}-\mu)^{2}</equation>服从<equation>\chi^{2}</equation>分布

答案: B

**解析:**解 由题设知，<equation>X_{1},X_{2},\dots ,X_{n}</equation>相互独立且与总体同分布.

依次分析各选项.

由<equation>X_{i}\sim N(\mu ,1)</equation>知，<equation>X_{i} - \mu \sim N(0,1)</equation>，<equation>i = 1,2,\dots,n</equation>，故<equation>\sum_{i = 1}^{n}\left(X_{i} - \mu\right)^{2}\sim \chi^{2}(n)</equation>.选项A正确由<equation>X_{1}\sim N(\mu ,1)</equation>，<equation>X_{n}\sim N(\mu ,1)</equation>知，<equation>X_{n} - X_{1}\sim N(0,2)</equation>，故<equation>\frac{X_n - X_1}{\sqrt{2}}\sim N(0,1)</equation>，于是<equation>\frac{\left(X_n - X_1\right)^2}{2}\sim \chi^2(1)</equation>.但<equation>2\left(X_{n} - X_{1}\right)^{2}</equation>不服从<equation>\chi^2</equation>分布.选项B不正确.

事实上，若<equation>2 \left(X_{n}-X_{1}\right)^{2}\sim \chi^{2} (m)</equation>，则<equation>E \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = m, \quad D \left[ 2 \left(X _ {n} - X _ {1}\right) ^ {2} \right] = 2 m.</equation>但由<equation>\frac{\left(X_{n}-X_{1}\right)^{2}}{2}\sim \chi^{2}(1)</equation>知，<equation>E \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 1, \quad D \left[ \frac {\left(X _ {n} - X _ {1}\right) ^ {2}}{2} \right] = 2,</equation>从而<equation>E[2(X_{n}-X_{1})^{2}]=4,D[2(X_{n}-X_{1})^{2}]=32.</equation>这与<equation>D[2(X_{n}-X_{1})^{2}]=2E[2(X_{n}-X_{1})^{2}]</equation>矛盾，故<equation>2(X_{n}-X_{1})^{2}</equation>不服从<equation>\chi^{2}</equation>分布.

由性质(2）知，<equation>( n - 1 ) S^{2}\sim \chi^{2} ( n - 1 ).</equation>又因为<equation>S^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}</equation>，所以<equation>\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}\sim \chi^{2} ( n - 1 ).</equation>选项C正确.

由性质（2）知，<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}\sim N\left(\mu ,\frac{1}{n}\right)</equation>，于是<equation>\sqrt{n} (\overline{X}-\mu)\sim N (0,1)</equation>，从而<equation>n(\overline{X}-\mu)^{2}\sim X^{2}(1).</equation>选项D正确.

综上所述，应选B.

---

**2013年第8题 | 选择题 | 4分 | 答案: C**

8. 设随机变量<equation>X\sim t(n),Y\sim F(1,n)</equation>，给定<equation>\alpha(0<\alpha<0.5)</equation>，常数c满足<equation>P\{X>c\}=\alpha</equation>，则<equation>P\left\{Y>c^{2}\right\}=(\quad)</equation>A.<equation>\alpha</equation>B.<equation>1-\alpha</equation>C.<equation>2\alpha</equation>D.<equation>1-2\alpha</equation>

答案: C

**解析:**解由 X ~ t(n)的定义可知，存在随机变量 U，V满足 U ~ N(0,1), V ~<equation>\chi^{2} (n)</equation>，且 U，V相互独立，使得<equation>X=\frac{U}{\sqrt{\frac{V}{n}}}</equation>，于是<equation>X^{2}=\frac{U^{2}}{\frac{V}{n}} \sim F(1,n)</equation>，从而

应选C.<equation>P \left\{ Y > c^{2} \right\}=P \left\{ X^{2}>c^{2} \right\}=P \left\{ X > c \right\}+P \left\{ X < - c \right\}=2 P \left\{ X > c \right\}=2 \alpha.</equation>

---


### 大数定律和中心极限定理

**2022年第9题 | 选择题 | 5分 | 答案: A**

9. 设随机变量<equation>X_{1}, X_{2}, \dots , X_{n}</equation>独立同分布，且<equation>X_{1}</equation>的4阶矩存在，记<equation>\mu_{k}=E \left( X_{1}^{k} \right) ( k=1, 2, 3, 4)</equation>，则根据切比雪夫不等式，对任意<equation>\varepsilon >0</equation>，都有<equation>P\left\{\left| \frac{1}{n}\sum_{i=1}^{n} X_{i}^{2}-\mu_{2} \right| \geqslant \varepsilon \right\} \leqslant</equation>(    )

A.<equation>\frac{\mu_{4}-\mu_{2}^{2}}{n\varepsilon^{2}}</equation>B.<equation>\frac{\mu_{4}-\mu_{2}^{2}}{\sqrt{n}\varepsilon^{2}}</equation>C.<equation>\frac{\mu_{2}-\mu_{1}^{2}}{n\varepsilon^{2}}</equation>D.<equation>\frac{\mu_{2}-\mu_{1}^{2}}{\sqrt{n}\varepsilon^{2}}</equation>

答案: A

**解析:**根据期望的性质，<equation>E \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n} E \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left(X _ {i} ^ {2}\right) \xlongequal {E \left(X _ {1} ^ {2}\right) = \mu_ {2}} \frac {1}{n} \cdot n \mu_ {2} = \mu_ {2}.</equation>根据切比雪夫不等式，对任意<equation>\varepsilon > 0</equation><equation>P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \mu_ {2} \right| \geqslant \varepsilon \right\} \leqslant \frac {D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right)}{\varepsilon^ {2}}.</equation>由于随机变量<equation>X_{1}, X_{2}, \dots, X_{n}</equation>独立同分布，故<equation>X_{1}^{2}, X_{2}^{2}, \dots, X_{n}^{2}</equation>相互独立.<equation>\begin{array}{l} D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left(X _ {i} ^ {2}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \left\{E \left(X _ {i} ^ {4}\right) - \left[ E \left(X _ {i} ^ {2}\right) \right] ^ {2} \right\} \\ = \frac {1}{n ^ {2}} \cdot n \left(\mu_ {4} - \mu_ {2} ^ {2}\right) = \frac {\mu_ {4} - \mu_ {2} ^ {2}}{n}. \\ \end{array}</equation>代入（1）式可得，<equation>P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \mu_ {2} \right| \geqslant \varepsilon \right\} \leqslant \frac {\mu_ {4} - \mu_ {2} ^ {2}}{n \varepsilon^ {2}}.</equation>因此，应选A.

---

**2020年第8题 | 选择题 | 4分 | 答案: B**

8. 设<equation>X_{1}, X_{2}, \dots , X_{1 0 0}</equation>为来自总体 X的简单随机样本，其中<equation>P\{X=0\}=P\{X=1\}=\frac{1}{2}, \Phi (x)</equation>表示标准正态分布函数，利用中心极限定理可得<equation>P\{\sum_{i=1}^{1 0 0} X_{i}\leqslant 5 5 \}</equation>的近似值为（    )

A. 1-<equation>\Phi (1)</equation>B.<equation>\Phi (1)</equation>C. 1-<equation>\Phi (0. 2)</equation>D.<equation>\Phi (0. 2)</equation>

答案: B

**解析:**解 计算 E（X），D（X）.<equation>E (X) = 0 \times \frac {1}{2} + 1 \times \frac {1}{2} = \frac {1}{2}.</equation><equation>E \left(X ^ {2}\right) = 0 ^ {2} \times \frac {1}{2} + 1 ^ {2} \times \frac {1}{2} = \frac {1}{2}.</equation><equation>D (X) = E \left(X ^ {2}\right) - \left[ E (X) \right] ^ {2} = \frac {1}{2} - \frac {1}{4} = \frac {1}{4}.</equation>由已知条件可知，<equation>n = 100</equation>根据列维-林德伯格中心极限定理，<equation>\sum_{i=1}^{1 0 0} X_{i}</equation>近似服从均值为<equation>1 0 0 \times \frac {1}{2}=5 0</equation>方差为<equation>1 0 0 \times \frac {1}{4}=</equation>25的正态分布，即N（50，25），从而<equation>\frac{\sum_{i=1}^{1 0 0} X_{i}-5 0}{5}</equation>近似服从N（0，1）.因此

因此，<equation>P \left\{\sum_ {i = 1} ^ {1 0 0} X _ {i} \leqslant 5 5 \right\} = P \left\{\frac {\sum_ {i = 1} ^ {1 0 0} X _ {i} - 5 0}{5} \leqslant \frac {5 5 - 5 0}{5} \right\} = \Phi (1).</equation>应选B.

---


**2017年第22题 | 解答题 | 11分**

设随机变量 X，Y相互独立，且 X的概率分布为<equation>P\{X=0\}=P\{X=2\}=\frac{1}{2},</equation>Y的概率密度为<equation>f (y) = \left\{ \begin{array}{l l} 2 y, & 0 < y < 1, \\ 0, & \text {其 他}. \end{array} \right.</equation>I. 求<equation>P\{Y\leqslant E(Y)\}</equation>；

II. 求<equation>Z=X+Y</equation>的概率密度
**答案: **（I）<equation>\frac{4}{9}</equation><equation>(\mathrm {I I}) f _ {Z} (z) = \left\{ \begin{array}{l l} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text {其 他}. \end{array} \right.</equation>
**解析: **解（I）由题设知，<equation>E ( Y )=\int_{- \infty}^{+ \infty} y f ( y ) \mathrm{d} y=\int_{0}^{1} 2 y^{2} \mathrm{d} y=\frac{2}{3}.</equation>因此，<equation>P \left\{Y \leqslant E (Y) \right\} = P \left\{Y \leqslant \frac {2}{3} \right\} = \int_ {0} ^ {\frac {2}{3}} 2 y \mathrm {d} y = \frac {4}{9}.</equation>（Ⅱ）Z的分布函数为<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X + Y \leqslant z \} \\ &= P \{X + Y \leqslant z, X = 0 \} + P \{X + Y \leqslant z, X = 2 \} \\ &= P \{Y \leqslant z, X = 0 \} + P \{Y \leqslant z - 2, X = 2 \} \\ \underline {{\underline {{X , Y \text {相 互 独立}}}}} P \{Y \leqslant z \} \cdot P \{X = 0 \} + P \{Y \leqslant z - 2 \} \cdot P \{X = 2 \} \\ &= \frac {1}{2} P \{Y \leqslant z \} + \frac {1}{2} P \{Y \leqslant z - 2 \}. \end{aligned}</equation>下面用两种方法求 Z的概率密度.

（法一）如图所示，当<equation>z\leqslant 0</equation>时，<equation>F_{Z}(z) = 0 + 0 = 0.</equation>当<equation>0 < z\leqslant 1</equation>时，<equation>F_{Z}(z) = \frac{1}{2}\int_{0}^{z}2y\mathrm{d}y + 0 = \frac{z^{2}}{2}</equation>.

当<equation>1 < z\leqslant 2</equation>时，<equation>F_{Z}(z) = \frac{1}{2}\int_{0}^{1}2y\mathrm{d}y + 0 = \frac{1}{2}.</equation>当<equation>2 < z\leqslant 3</equation>时，<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\int_{0}^{z - 2}2y\mathrm{d}y = \frac{1}{2} +\frac{(z - 2)^{2}}{2}.</equation>当<equation>z > 3</equation>时，<equation>F_{Z}(z) = 1.</equation>综上所述，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{ \begin{array}{l l} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text {其 他}. \end{array} \right.</equation>（法二）由<equation>Z</equation>的分布函数<equation>F_{Z}(z) = \frac{1}{2} P\{Y \leqslant z\} +\frac{1}{2} P\{Y \leqslant z - 2\}</equation>知，<equation>Z</equation>的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \frac {1}{2} f (z) + \frac {1}{2} f (z - 2).</equation>当<equation>z\leqslant 0</equation>时，<equation>z - 2\leqslant 0,f_Z(z) = 0 + 0 = 0.</equation>当<equation>0 < z < 1</equation>时，<equation>z - 2\leqslant 0,f_Z(z) = \frac{1}{2}\cdot 2z + 0 = z.</equation>当<equation>1\leqslant z\leqslant 2</equation>时，<equation>z - 2\leqslant 0,f_Z(z) = 0 + 0 = 0.</equation>当<equation>2 < z < 3</equation>时，<equation>0 < z - 2 < 1</equation>，<equation>f_{Z}(z) = 0 + \frac{1}{2}\cdot 2(z - 2) = z - 2.</equation>当<equation>z\geqslant 3</equation>时，<equation>z - 2\geqslant 1, f_Z(z) = 0 + 0 = 0.</equation>综上所述，<equation>f_{z}(z) = \left\{ \begin{array}{ll} z, & 0 < z < 1, \\ z - 2, & 2 < z < 3, \\ 0, & \text{其他}. \end{array} \right.</equation>

---

**2015年第22题 | 解答题 | 11分**

设随机变量 X的概率密度为<equation>f (x) = \left\{ \begin{array}{l l} 2 ^ {- x} \ln 2, & x > 0 \\ 0, & x \leqslant 0 \end{array} \right.</equation>对 X 进行独立重复的观测，直到第2个大于3的观测值出现时停止，记 Y为观测次数.

I. 求 Y的概率分布；

II. 求 E(Y).
**答案: **<equation>(2 2) (\mathrm {I}) P \{Y = k \} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, k = 2, 3, \dots ;</equation><equation>(\mathrm {I I}) E (Y) = 1 6.</equation>
**解析: **解（I）由题设知，<equation>P \left\{X \leqslant 3 \right\} = \int_ {- \infty} ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {3} 2 ^ {- x} \ln 2 \mathrm {d} x = - 2 ^ {- x} \Big | _ {0} ^ {3} = - \frac {1}{8} - (- 1) = \frac {7}{8},</equation><equation>P \{X > 3 \} = 1 - P \{X \leqslant 3 \} = 1 - \frac {7}{8} = \frac {1}{8}.</equation>Y可能的取值为2，3，4，….又由于<equation>Y=k(k\geqslant 2)</equation>意味着前k-1次只有1次出现大于3的观测值，且第k次出现大于3的观测值，故Y的概率分布为<equation>P \left\{Y = k \right\} = \mathrm {C} _ {k - 1} ^ {1} \times \frac {1}{8} \times \left(\frac {7}{8}\right) ^ {k - 2} \times \frac {1}{8} = \frac {1}{6 4} (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}, \quad k = 2, 3, \dots .</equation>（Ⅱ）（法一）由期望的定义知，<equation>E (Y) = \sum_ {k = 2} ^ {\infty} k \cdot P \{Y = k \} = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2}.</equation>考虑幂级数<equation>\sum_{k = 2}^{\infty}k(k - 1)x^{k - 2}</equation>，其收敛域为（-1，1），故该级数在<equation>x = \frac{7}{8}</equation>处收敛.当<equation>x\in(-1,1)</equation>时，<equation>\begin{aligned} \sum_ {k = 2} ^ {\infty} k (k - 1) x ^ {k - 2} &= \sum_ {k = 2} ^ {\infty} \left(x ^ {k}\right) ^ {\prime \prime} = \left(\sum_ {k = 2} ^ {\infty} x ^ {k}\right) ^ {\prime \prime} = \left(\frac {x ^ {2}}{1 - x}\right) ^ {\prime \prime} = \left(\frac {x ^ {2} - 1 + 1}{1 - x}\right) ^ {\prime \prime} \\ &= \left(- x - 1 + \frac {1}{1 - x}\right) ^ {\prime \prime} = \left(\frac {1}{1 - x}\right) ^ {\prime \prime} = \frac {2}{(1 - x) ^ {3}}. \end{aligned}</equation>因此，<equation>E (Y) = \frac {1}{6 4} \sum_ {k = 2} ^ {\infty} k (k - 1) \left(\frac {7}{8}\right) ^ {k - 2} = \frac {1}{6 4} \times \frac {2}{\left(1 - \frac {7}{8}\right) ^ {3}} = 1 6.</equation>（法二）利用几何分布的性质.

设<equation>Y_{1}</equation>表示出现第1个大于3的观测值时所需的观测次数，<equation>Y_{2}</equation>表示出现第1个大于3的观测值之后到出现第2个大于3的观测值时所需的观测次数，则<equation>Y = Y_{1} + Y_{2}</equation>，且<equation>Y_{1}, Y_{2}</equation>均服从参数为<equation>p = \frac{1}{8}</equation>的几何分布.于是<equation>E\left(Y_{1}\right) = E\left(Y_{2}\right) = \frac{1}{p} = 8.</equation>因此，<equation>E (Y) = E \left(Y _ {1}\right) + E \left(Y _ {2}\right) = 1 6.</equation>

---

**2014年第8题 | 选择题 | 4分 | 答案: D**
8. 设连续型随机变量<equation>X_{1}</equation>与<equation>X_{2}</equation>相互独立且方差均存在，<equation>X_{1}</equation>与<equation>X_{2}</equation>概率密度分别为<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>，随机变量<equation>Y_{1}</equation>的概率密度为<equation>f_{Y_{1}}(y)=\frac{1}{2}[f_{1}(y)+f_{2}(y)]</equation>，随机变量<equation>Y_{2}=\frac{1}{2}(X_{1}+X_{2})</equation>，则（    )

A.<equation>E \left( Y_{1} \right)>E \left( Y_{2} \right), D \left( Y_{1} \right)>D \left( Y_{2} \right)</equation>B.<equation>E \left( Y_{1} \right)=E \left( Y_{2} \right), D \left( Y_{1} \right)=D \left( Y_{2} \right)</equation>C.<equation>E \left( Y_{1} \right)=E \left( Y_{2} \right), D \left( Y_{1} \right)<D \left( Y_{2} \right)</equation>D.<equation>E \left( Y_{1} \right)=E \left( Y_{2} \right), D \left( Y_{1} \right)>D \left( Y_{2} \right)</equation>
答案: D
**解析: **解（法一）设<equation>E ( X_{1} )=\mu_{1}, E ( X_{2} )=\mu_{2}, D ( X_{1} )=\sigma_{1}^{2}, D ( X_{2} )=\sigma_{2}^{2}</equation>，则<equation>E ( X_{1}^{2} )=\mu_{1}^{2}+\sigma_{1}^{2},</equation><equation>E ( X_{2}^{2} )=\mu_{2}^{2}+\sigma_{2}^{2}</equation>，从而<equation>\begin{aligned} E \left(Y _ {1}\right) &= \int_ {- \infty} ^ {+ \infty} y f _ {Y _ {1}} (y) \mathrm {d} y = \frac {1}{2} \left[ \int_ {- \infty} ^ {+ \infty} y f _ {1} (y) \mathrm {d} y + \int_ {- \infty} ^ {+ \infty} y f _ {2} (y) \mathrm {d} y \right] \\ &= \frac {1}{2} \left[ E \left(X _ {1}\right) + E \left(X _ {2}\right) \right] = \frac {1}{2} \left(\mu_ {1} + \mu_ {2}\right), \end{aligned}</equation><equation>\begin{aligned} E \left(Y _ {1} ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} y ^ {2} f _ {Y _ {1}} (y) \mathrm {d} y = \frac {1}{2} \left[ \int_ {- \infty} ^ {+ \infty} y ^ {2} f _ {1} (y) \mathrm {d} y + \int_ {- \infty} ^ {+ \infty} y ^ {2} f _ {2} (y) \mathrm {d} y \right] \\ &= \frac {1}{2} \left[ E \left(X _ {1} ^ {2}\right) + E \left(X _ {2} ^ {2}\right) \right] = \frac {1}{2} \left(\mu_ {1} ^ {2} + \sigma_ {1} ^ {2} + \mu_ {2} ^ {2} + \sigma_ {2} ^ {2}\right), \end{aligned}</equation><equation>\begin{aligned} D \left(Y _ {1}\right) &= E \left(Y _ {1} ^ {2}\right) - \left[ E \left(Y _ {1}\right) \right] ^ {2} = \frac {1}{2} \left(\mu_ {1} ^ {2} + \sigma_ {1} ^ {2} + \mu_ {2} ^ {2} + \sigma_ {2} ^ {2}\right) - \frac {1}{4} \left(\mu_ {1} + \mu_ {2}\right) ^ {2} \\ &= \frac {1}{2} \left(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}\right) + \frac {1}{4} \left(\mu_ {1} - \mu_ {2}\right) ^ {2}. \end{aligned}</equation>又<equation>E \left(Y _ {2}\right) = E \left[ \frac {1}{2} \left(X _ {1} + X _ {2}\right) \right] = \frac {1}{2} \left[ E \left(X _ {1}\right) + E \left(X _ {2}\right) \right] = \frac {1}{2} \left(\mu_ {1} + \mu_ {2}\right),</equation><equation>D \left(Y _ {2}\right) = D \left[ \frac {1}{2} \left(X _ {1} + X _ {2}\right) \right] \xlongequal {\text {X} _ {1}, X _ {2} \text {独 立}} \frac {1}{4} \left[ D \left(X _ {1}\right) + D \left(X _ {2}\right) \right] = \frac {1}{4} \left(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}\right),</equation>故<equation>E \left(Y _ {1}\right) = E \left(Y _ {2}\right), \quad D \left(Y _ {1}\right) - D \left(Y _ {2}\right) = \frac {1}{4} \left(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}\right) + \frac {1}{4} \left(\mu_ {1} - \mu_ {2}\right) ^ {2} \geqslant 0,</equation>等号成立当且仅当<equation>\sigma_{1} = \sigma_{2} = 0,\mu_{1} = \mu_{2}</equation>，但这与<equation>X_{1},X_{2}</equation>是连续型随机变量矛盾.因此，应选D.

（法二）特殊值法.

令<equation>X_{1}\sim N(0,1),X_{2}\sim N(0,1)</equation>，且<equation>X_{1}</equation>与<equation>X_{2}</equation>相互独立，则<equation>f_{1}(y) = f_{2}(y)</equation>，从而<equation>f _ {Y _ {1}} (y) = \frac {1}{2} \left[ f _ {1} (y) + f _ {2} (y) \right] = f _ {1} (y),</equation>于是<equation>Y_{1}\sim N(0,1).</equation>又<equation>Y_{2}=\frac{1}{2}\left(X_{1}+X_{2}\right)\sim N\left(0,\frac{1}{2}\right)</equation>，故<equation>E\left(Y_{1}\right)=E\left(Y_{2}\right)=0,D\left(Y_{1}\right)=1 > \frac{1}{2} = D\left(Y_{2}\right).</equation>因此，应选D.

---

**2014年第22题 | 解答题 | 11分**

22. (本题满分11分)

设随机变量 X的概率分布为<equation>P\{X=1\}=P\{X=2\}=\frac{1}{2}.</equation>在给定 X=i的条件下，随机变量 Y服从均匀分布<equation>U(0,i)\ (i=1,2).</equation>I. 求 Y的分布函数<equation>F_{Y}(y)</equation>；

II. 求 E(Y).
**答案: **(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<0,\\ \frac{3}{4} y,& 0\leqslant y<1,\\ \frac{1}{2}+\frac{1}{4} y,& 1\leqslant y<2,\\ 1,& y\geqslant 2; \end{array} \right.</equation>（Ⅱ）<equation>\frac{3}{4}.</equation>
**解析: **解（I）由题设知，当<equation>X = 1</equation>时，<equation>Y\sim U(0,1)</equation>；当<equation>X = 2</equation>时，<equation>Y\sim U(0,2)</equation>.于是，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{Y \leqslant y, X = 1 \right\} + P \left\{Y \leqslant y, X = 2 \right\} \\ = P \left\{Y \leqslant y \mid X = 1 \right\} P \left\{X = 1 \right\} + P \left\{Y \leqslant y \mid X = 2 \right\} P \left\{X = 2 \right\}. \\ \end{array}</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y)=0\times \frac{1}{2}+0\times \frac{1}{2}=0.</equation>当<equation>0 \leqslant y < 1</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{y}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{3}{4} y.</equation>当<equation>1\leqslant y < 2</equation>时，<equation>F_{Y}(y) = \left(\int_{0}^{1}1\mathrm{d}y\right)\cdot \frac{1}{2} + \left(\int_{0}^{y}\frac{1}{2}\mathrm{d}y\right)\cdot \frac{1}{2} = \frac{1}{2} + \frac{1}{4} y.</equation>当<equation>y\geqslant 2</equation>时，<equation>F_{Y}(y) = 1\times \frac{1}{2} +1\times \frac{1}{2} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \frac{3}{4} y, & 0 \leqslant y < 1,\\ \frac{1}{2} +\frac{1}{4} y, & 1 \leqslant y < 2,\\ 1, & y \geqslant 2. \end{array} \right.</equation>（Ⅱ）由第（I）问中<equation>Y</equation>的分布函数的表达式知，<equation>Y</equation>的概率密度函数为<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {3}{4}, & 0 \leqslant y < 1, \\ \frac {1}{4}, & 1 \leqslant y < 2, \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {1} \frac {3}{4} y \mathrm {d} y + \int_ {1} ^ {2} \frac {1}{4} y \mathrm {d} y = \frac {3}{8} + \frac {3}{8} = \frac {3}{4}.</equation>

---

**2011年第8题 | 选择题 | 4分 | 答案: B**
8. 设随机变量 X与 Y相互独立，且 E(X)与 E(Y)存在，记 U=<equation>\max \{ X, Y \}</equation><equation>V=\min \{ X, Y \}</equation>，则 E(UV) =（    )

A.<equation>E ( U ) \cdot E ( V )</equation>B.<equation>E ( X ) \cdot E ( Y )</equation>C.<equation>E ( U ) \cdot E ( Y )</equation>D.<equation>E ( X ) \cdot E ( V )</equation>
答案: B
**解析: **解（法一）由 U，V的定义知，<equation>U V=X Y</equation>.又 X与 Y相互独立，故<equation>E ( U V )=E ( X Y )=E ( X ) E ( Y )</equation>从而选B.

（法二）由于<equation>U=\max \{ X, Y \}=\frac{X+Y+\left| X-Y \right|}{2}, V=\min \{ X, Y \}=\frac{X+Y-\left| X-Y \right|}{2}</equation>，故<equation>U V=\frac{(X+Y)^{2}-\left| X-Y \right|^{2}}{4}=X Y</equation>.又 X与 Y相互独立，故<equation>E ( U V )=E ( X Y )=E ( X ) E ( Y )</equation>应选B.

---

**2010年第14题 | 填空题 | 4分**
14. 设随机变量<equation>X</equation>的概率分布为<equation>P\{X=k\}=\frac{C}{k!}, k=0,1,2,\cdots</equation>，则<equation>E(X^{2})=</equation>___
**解析: **由概率的性质可知，<equation>1 = \sum_ {k = 0} ^ {\infty} P \{X = k \} = \sum_ {k = 0} ^ {\infty} \frac {C}{k !} = C \mathrm {e},</equation>即<equation>C = \frac{1}{\mathrm{e}}</equation>. 于是<equation>X</equation>服从参数为1的泊松分布，<equation>E(X) = D(X) = 1</equation>，从而<equation>E \left(X ^ {2}\right) = D (X) + \left[ E (X) \right] ^ {2} = 1 + 1 = 2.</equation>

---

**2009年第7题 | 选择题 | 4分 | 答案: C**
7. 设随机变量 X的分布函数为<equation>F(x)=0. 3 \varPhi(x)+0. 7 \varPhi\left(\frac{x-1}{2}\right)</equation>，其中<equation>\varPhi(x)</equation>为标准正态分布的分布函数，则<equation>E(X)=</equation>(    )

A.0 B.0.3 C.0.7 D.1
答案: C
**解析: **解记<equation>\varphi(x)</equation>为标准正态分布的概率密度函数，则<equation>\int_{- \infty}^{+ \infty} \varphi(x)\mathrm{d}x=1, \int_{- \infty}^{+ \infty} x\varphi(x)\mathrm{d}x=0.</equation>由题设知，X的概率密度为<equation>f(x)=F^{\prime}(x)=0. 3 \varphi(x)+\frac{0. 7}{2} \varphi \left( \frac{x-1}{2} \right)</equation>，于是<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \left[ 0. 3 x \varphi (x) + \frac {0 . 7}{2} x \varphi \left(\frac {x - 1}{2}\right) \right] \mathrm {d} x \\ &= 0 + \int_ {- \infty} ^ {+ \infty} \frac {0 . 7}{2} x \varphi \left(\frac {x - 1}{2}\right) \mathrm {d} x \xlongequal {t = \frac {x - 1}{2}} 0. 7 \int_ {- \infty} ^ {+ \infty} (2 t + 1) \varphi (t) \mathrm {d} t \\ &= 0. 7 \left[ 2 \int_ {- \infty} ^ {+ \infty} t \varphi (t) \mathrm {d} t + \int_ {- \infty} ^ {+ \infty} \varphi (t) \mathrm {d} t \right] = 0. 7. \end{aligned}</equation>因此，应选C.

---

**2020年第22题 | 解答题 | 11分**

设随机变量<equation>X_{1}, X_{2}, X_{3}</equation>相互独立，其中<equation>X_{1}</equation>与<equation>X_{2}</equation>均服从标准正态分布，<equation>X_{3}</equation>的概率分布为<equation>P\{X_{3}=0\}=</equation><equation>P\{X_{3}=1\}=\frac{1}{2}.</equation><equation>Y=X_{3}X_{1}+(1-X_{3})X_{2}.</equation>I. 求二维随机变量<equation>( X_{1}, Y )</equation>的分布函数，结果用标准正态分布函数<equation>\Phi ( x )</equation>表示；

II. 证明随机变量 Y服从标准正态分布.
**答案: **<equation>(\mathrm {I}) F (x, y) = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (x) [ \Phi (y) + 1 ], & x \leqslant y, \\ \frac {1}{2} \Phi (y) [ \Phi (x) + 1 ], & x > y; \end{array} \right.</equation>（Ⅱ）证明略.
**解析: **（I）设<equation>(X_{1},Y)</equation>的分布函数为<equation>F(x,y)</equation>.根据定义，<equation>\begin{array}{l} F (x, y) = P \left\{X _ {1} \leqslant x, Y \leqslant y \right\} = P \left\{X _ {1} \leqslant x, X _ {3} X _ {1} + \left(1 - X _ {3}\right) X _ {2} \leqslant y \right\} \\ = P \left\{X _ {1} \leqslant x, X _ {2} \leqslant y, X _ {3} = 0 \right\} + P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y, X _ {3} = 1 \right\} \\ \underline {{\text {独立性}}} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} P \left\{X _ {3} = 0 \right\} + P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\} P \left\{X _ {3} = 1 \right\} \\ = \frac {1}{2} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} + \frac {1}{2} P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\}. \\ \end{array}</equation>下面分情况讨论.

- 当<equation>x \leqslant y</equation>时，<equation>P\{X_{1} \leqslant x, X_{1} \leqslant y\} = P\{X_{1} \leqslant x\} = \varPhi(x).</equation><equation>\begin{array}{l} F (x, y) = \frac {1}{2} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} + \frac {1}{2} P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\} \\ = \frac {1}{2} \Phi (x) \Phi (y) + \frac {1}{2} \Phi (x) = \frac {1}{2} \Phi (x) [ \Phi (y) + 1 ]. \\ \end{array}</equation>- 当<equation>x > y</equation>时，<equation>P\{X_{1}\leqslant x,X_{1}\leqslant y\} = P\{X_{1}\leqslant y\} = \varPhi(y).</equation><equation>\begin{array}{l} F (x, y) = \frac {1}{2} P \left\{X _ {1} \leqslant x \right\} P \left\{X _ {2} \leqslant y \right\} + \frac {1}{2} P \left\{X _ {1} \leqslant x, X _ {1} \leqslant y \right\} \\ = \frac {1}{2} \Phi (x) \Phi (y) + \frac {1}{2} \Phi (y) = \frac {1}{2} \Phi (y) [ \Phi (x) + 1 ]. \\ \end{array}</equation>因此，<equation>F ( x,y) = \left\{ \begin{array}{l l} \frac{1}{2} \varPhi ( x ) [ \varPhi ( y ) + 1 ] , & x \leqslant y, \\ \frac{1}{2} \varPhi ( y ) [ \varPhi ( x ) + 1 ] , & x > y. \end{array} \right.</equation>（Ⅱ）计算 Y的边缘分布.<equation>F _ {Y} (y) = F (+ \infty , y) = \frac {1}{2} \Phi (y) [ \Phi (+ \infty) + 1 ] \xlongequal {\Phi (+ \infty) = 1} \Phi (y).</equation>由于<equation>Y</equation>的边缘分布函数为标准正态分布函数，故<equation>Y</equation>服从标准正态分布.

---

**2019年第22题 | 解答题 | 11分**
2. (本题满分11分)

设随机变量 X与 Y相互独立，X服从参数为1的指数分布，Y的概率分布为<equation>P\{Y=-1\}=p,P\{Y=1\}=</equation><equation>1-p(0<p<1).</equation>.令 Z=XY.

I. 求 Z的概率密度;

II. p为何值时，X与 Z不相关;

III. X与 Z是否相互独立?
**答案: **（I）<equation>Z</equation>的概率密度为<equation>f_{Z}(z)=\left\{\begin{array}{ll}p\mathrm{e}^{z},&z\leqslant 0,\\ (1-p)\mathrm{e}^{-z},&z>0;\end{array} \right.</equation>（Ⅱ）当<equation>p=\frac{1}{2}</equation>时，X与Z不相关；

（Ⅲ）X与Z不相互独立.
**解析: **（I）先计算<equation>Z</equation>的分布函数<equation>F_{Z}(z)</equation>.<equation>\begin{array}{l} F _ {Z} (z) = P \left\{X Y \leqslant z \right\} = P \left\{X \geqslant - z, Y = - 1 \right\} + P \left\{X \leqslant z, Y = 1 \right\} \\ \underline {{\text {独立 性}}} P \left\{X \geqslant - z \right\} P \left\{Y = - 1 \right\} + P \left\{X \leqslant z \right\} P \left\{Y = 1 \right\} \\ = p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z), \\ \end{array}</equation>其中<equation>F_{X}(x)</equation>是X的分布函数.

于是，Z的概率密度为<equation>f _ {Z} (z) = F _ {Z} ^ {\prime} (z) = \left\{p \left[ 1 - F _ {X} (- z) \right] + (1 - p) F _ {X} (z) \right\} ^ {\prime} = p f _ {X} (- z) + (1 - p) f _ {X} (z).</equation>由于<equation>X</equation>服从参数为1的指数分布，故<equation>X</equation>的概率密度为<equation>f_{X}(x) = \left\{ \begin{array}{ll} \mathrm{e}^{-x}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation>当<equation>z\leqslant 0</equation>时，<equation>-z\geqslant 0,f_{X}(-z) = \mathrm{e}^{z},f_{X}(z) = 0</equation>；当<equation>z > 0</equation>时，<equation>-z < 0,f_{X}(z) = \mathrm{e}^{-z},f_{X}(-z) = 0.</equation>因此，<equation>f _ {Z} (z) = \left\{ \begin{array}{l l} p \mathrm {e} ^ {z}, & z \leqslant 0, \\ (1 - p) \mathrm {e} ^ {- z}, & z > 0. \end{array} \right.</equation>（Ⅱ）计算<equation>\operatorname{Cov}(X, Z).</equation><equation>\begin{aligned} \operatorname {C o v} (X, Z) &= E (X Z) - E (X) E (Z) = E \left(X ^ {2} Y\right) - E (X) E (X Y) \\ \xlongequal {\text {独立性}} E \left(X ^ {2}\right) E (Y) - \left[ E (X) \right] ^ {2} E (Y) \\ &= D (X) E (Y). \end{aligned}</equation>下面分别计算 D（X），E（Y）.

由于<equation>X</equation>服从参数为1的指数分布，故<equation>D(X) = 1.</equation><equation>E (Y) = 1 \times (1 - p) + (- 1) \times p = 1 - 2 p.</equation>因此，<equation>\operatorname{Cov}(X,Z) = E(Y) = 1 - 2p.</equation>当<equation>p=\frac{1}{2}</equation>时，<equation>\operatorname{Cov}(X,Z)=0</equation>，X与Z不相关.

（Ⅲ）由第（Ⅱ）问可知，当<equation>p\neq \frac{1}{2}</equation>时，X与Z相关，从而不相互独立.

下面只需考虑 p =<equation>\frac{1}{2}</equation>的情况.

（法一）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X < 1,Z < 1\} = P\{X < 1\} P\{Z < 1\}</equation>是否成立.<equation>P \left\{X < 1 \right\} = \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = 1 - \mathrm {e} ^ {- 1}.</equation><equation>\begin{aligned} P \{Z < 1 \} &= P \{X Y < 1 \} = F _ {Z} (1) = \frac {1}{2} \left[ 1 - F _ {X} (- 1) \right] + \frac {1}{2} F _ {X} (1) \\ &= \frac {1}{2} \times (1 - 0) + \frac {1}{2} \int_ {0} ^ {1} \mathrm {e} ^ {- x} \mathrm {d} x = \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right). \end{aligned}</equation><equation>\begin{aligned} P \{X < 1, Z < 1 \} &= P \{X < 1, X Y < 1 \} = P \{X \leqslant 0, X Y < 1 \} + P \{0 < X < 1, X Y < 1 \} \\ &= P \{0 < X < 1, X Y < 1 \} = P \{0 < X < 1, Y = 1 \} + P \{0 < X < 1, Y = - 1 \} \\ &= P \{0 < X < 1 \} = P \{X < 1 \} = 1 - \mathrm {e} ^ {- 1}. \end{aligned}</equation>由于<equation>1 - \mathrm{e}^{-1}\neq(1 - \mathrm{e}^{-1})\cdot\left[\frac{1}{2} +\frac{1}{2}(1 - \mathrm{e}^{-1})\right],</equation>故X，Z不相互独立.

（法二）当<equation>p=\frac{1}{2}</equation>时，检验<equation>P\{X > 1,Z < 1\} = P\{X > 1\} P\{Z < 1\}</equation>是否成立.

当 X > 1时，<equation>X Y < 1</equation>等价于<equation>Y < \frac{1}{X}.</equation>又因为此时<equation>\frac{1}{X} < 1</equation>，而Y只可能取1和-1两个值，所以<equation>Y < \frac{1}{X}</equation>能推出<equation>Y = -1.</equation>于是，<equation>P \left\{X > 1 \right\} = \int_ {1} ^ {+ \infty} \mathrm {e} ^ {- x} \mathrm {d} x = \mathrm {e} ^ {- 1}.</equation><equation>P \{Z < 1 \} \xlongequal {\text {同 法 一}} \frac {1}{2} + \frac {1}{2} \left(1 - \mathrm {e} ^ {- 1}\right).</equation><equation>P \{X > 1, Z < 1 \} = P \{X > 1, X Y < 1 \} = P \left\{X > 1, Y < \frac {1}{X} \right\} = P \{X > 1, Y = - 1 \}</equation><equation>\stackrel {\text {独立 性}} {=} P \left\{X > 1 \right\} P \left\{Y = - 1 \right\} = \frac {1}{2} \mathrm {e} ^ {- 1}.</equation>由于<equation>\frac{1}{2}\mathrm{e}^{-1}\neq \mathrm{e}^{-1}\cdot \left[\frac{1}{2}+\frac{1}{2}\left(1-\mathrm{e}^{-1}\right)\right]</equation>，故X，Z不相互独立.

综上所述，X，Z不相互独立.

---

**2016年第22题 | 解答题 | 11分**
. (本题满分11分)

设二维随机变量 (X,Y)在区域 D = {(x,y) | 0 < x < 1,<equation>x^{2} < y < \sqrt{x}</equation>}上服从均匀分布，令<equation>U=\left\{\begin{array}{l l}1,&X\leqslant Y,\\ 0,&X>Y. \end{array} \right.</equation>I. 写出 (X,Y)的概率密度；

II. 问 U与 X是否相互独立？并说明理由；

III. 求 Z=U+X的分布函数 F(z).
**答案: **（I）<equation>f ( x,y)=\left\{\begin{array}{ll}3,&0<x<1,x^{2}<y<\sqrt{x},\\ 0,&\text{其他};\end{array}\right.</equation>（Ⅱ）U与X不相互独立；

（Ⅲ）<equation>F ( z )=\left\{\begin{array}{ll}0,&z<0,\\ \frac{3}{2} z^{2}-z^{3},&0\leqslant z<1,\\ 2 ( z-1 )^{\frac{3}{2}}-\frac{3}{2} z^{2}+3 z-1,&1\leqslant z<2,\\ 1,&z\geqslant 2.\end{array}\right.</equation>
**解析: **（I）区域D如图（a）所示，其面积为<equation>S = \int_ {0} ^ {1} \sqrt {x} \mathrm {d} x - \int_ {0} ^ {1} x ^ {2} \mathrm {d} x = \frac {2}{3} x ^ {\frac {3}{2}} \left| _ {0} ^ {1} - \frac {x ^ {3}}{3} \right| _ {0} ^ {1} = \frac {2}{3} - \frac {1}{3} = \frac {1}{3}.</equation>又由于<equation>(X, Y)</equation>在区域<equation>D</equation>上服从均匀分布，故<equation>(X, Y)</equation>的概率密度为<equation>f (x, y) = \left\{ \begin{array}{l l} 3, & 0 < x < 1, x ^ {2} < y < \sqrt {x}, \\ 0, & \text {其 他}. \end{array} \right.</equation>(a)

(b)

（Ⅱ）考虑<equation>P\{U = 0, X\leqslant t\}</equation><equation>P \{U = 0 \} = P \{X > Y \} = \iint f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {1} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {1}{2}.</equation>对<equation>t \leqslant 0</equation>，<equation>P\{X \leqslant t\} = 0</equation>，<equation>P\{U = 0, X \leqslant t\} = 0.</equation>于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>t \geqslant 1</equation>，<equation>P\{X \leqslant t\} = 1, P\{U = 0, X \leqslant t\} = P\{U = 0\}</equation>.于是，<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{U = 0 \right\} \cdot P \left\{X \leqslant t \right\}.</equation>对<equation>0 < t < 1</equation>，有效积分区域为图（b）中的蓝色区域.<equation>P \left\{U = 0, X \leqslant t \right\} = P \left\{X > Y, X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} t ^ {2} - t ^ {3},</equation><equation>P \left\{X \leqslant t \right\} = \int_ {0} ^ {t} \mathrm {d} x \int_ {x ^ {2}} ^ {\sqrt {x}} 3 \mathrm {d} y = \int_ {0} ^ {t} 3 \left(\sqrt {x} - x ^ {2}\right) \mathrm {d} x = 2 t ^ {\frac {3}{2}} - t ^ {3}.</equation>于是，<equation>\begin{aligned} P \{U = 0, X \leqslant t \} - P \{U = 0 \} \cdot P \{X \leqslant t \} &= \frac {3}{2} t ^ {2} - t ^ {3} - \frac {1}{2} \left(2 t ^ {\frac {3}{2}} - t ^ {3}\right) \\ &= \frac {3}{2} t ^ {2} - \frac {1}{2} t ^ {3} - t ^ {\frac {3}{2}} \neq 0. (\mathrm {见 注} \textcircled{1}) \end{aligned}</equation>因此，当<equation>0 < t < 1</equation>时，U与X不相互独立.

（Ⅲ）由题设知，<equation>\begin{array}{l} F (z) = P \left\{Z \leqslant z \right\} = P \left\{U + X \leqslant z \right\} \\ = P \left\{U + X \leqslant z, U = 0 \right\} + P \left\{U + X \leqslant z, U = 1 \right\} \\ = P \left\{X \leqslant z, U = 0 \right\} + P \left\{X \leqslant z - 1, U = 1 \right\} \\ = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\}. \\ \end{array}</equation>当<equation>z < 0</equation>时，<equation>z - 1 < 0</equation>，于是<equation>P\{X\leqslant z,X > Y\} = 0,P\{X\leqslant z - 1,X\leqslant Y\} = 0.</equation>从而<equation>F(z) = 0.</equation><equation>0 \leqslant z < 1</equation><equation>z - 1 < 0</equation><equation>P \left\{X \leqslant z - 1, X \leqslant Y \right\} = 0</equation><equation>F (z) = P \left\{X \leqslant z, X > Y \right\} = \int_ {0} ^ {z} \mathrm {d} x \int_ {x ^ {2}} ^ {x} 3 \mathrm {d} y = \int_ {0} ^ {z} 3 \left(x - x ^ {2}\right) \mathrm {d} x = \frac {3}{2} z ^ {2} - z ^ {3}.</equation>当<equation>1\leqslant z < 2</equation>时，<equation>0\leqslant z - 1 < 1</equation><equation>\begin{array}{l} F (z) = P \left\{X \leqslant z, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = P \left\{X \leqslant 1, X > Y \right\} + P \left\{X \leqslant z - 1, X \leqslant Y \right\} \\ = \frac {1}{2} + \int_ {0} ^ {z - 1} \mathrm {d} x \int_ {x} ^ {\sqrt {x}} 3 \mathrm {d} y = \frac {1}{2} + \int_ {0} ^ {z - 1} 3 (\sqrt {x} - x) \mathrm {d} x \\ = \frac {1}{2} + 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} (z - 1) ^ {2} = 2 (z - 1) ^ {\frac {3}{2}} - \frac {3}{2} z ^ {2} + 3 z - 1. \\ \end{array}</equation>当<equation>z\geqslant 2</equation>时，<equation>z - 1\geqslant 1,F(z) = 1.</equation>综上所述，<equation>F (z) = \left\{ \begin{array}{ll} 0, & z < 0, \\ \frac{3}{2} z^{2} - z^{3}, & 0 \leqslant z < 1, \\ 2 (z - 1)^{\frac{3}{2}} - \frac{3}{2} z^{2} + 3 z - 1, & 1 \leqslant z < 2, \\ 1, & z \geqslant 2. \end{array} \right.</equation>

---

**2015年第14题 | 填空题 | 4分**
14. 设二维随机变量<equation>(X, Y)</equation>服从正态分布<equation>N(1, 0; 1, 1; 0)</equation>, 则<equation>P\{XY - Y < 0\} =</equation>___
**解析: **解 由题设知，X，Y不相关. 又由于（X，Y）服从正态分布，故X，Y相互独立. 从而<equation>\begin{aligned} P \{X Y - Y < 0 \} &= P \{(X - 1) Y < 0 \} = P \{X < 1, Y > 0 \} + P \{X > 1, Y < 0 \} \\ &= P \{X < 1 \} \cdot P \{Y > 0 \} + P \{X > 1 \} \cdot P \{Y < 0 \}. \end{aligned}</equation>由<equation>( X, Y ) \sim N ( 1, 0 ; 1, 1 ; 0 )</equation>可知，<equation>X\sim N ( 1, 1 )</equation><equation>Y\sim N ( 0, 1 )</equation>从而X，Y的概率密度的图形分别关于<equation>x=1</equation>，<equation>x=0</equation>对称，于是<equation>P \{ X < 1 \} = P \{ X > 1 \} = \frac{1}{2}</equation><equation>P \{ Y < 0 \} = P \{ Y > 0 \} = \frac{1}{2}.</equation>因此，<equation>P \left\{X Y - Y < 0 \right\} = \frac {1}{2} \times \frac {1}{2} + \frac {1}{2} \times \frac {1}{2} = \frac {1}{2}.</equation>

---

**2013年第22题 | 解答题 | 11分**
2. (本题满分11分)

设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}\frac{1}{9} x^{2},&0<x<3,\\ 0,&\text{其他}.\end{array} \right.</equation>令随机变量<equation>Y=\left\{\begin{array}{ll}2,&X\leqslant 1,\\ X,&1<X<2,\\ 1,&X\geqslant 2. \end{array} \right.</equation>I. 求 Y的分布函数；

II. 求概率<equation>P \{ X \leqslant Y \}</equation>
**答案: **(22) (I)<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<1,\\ \frac{y^{3}+18}{27},& 1\leqslant y<2,\\ 1,& y\geqslant 2; \end{array} \right.</equation>（Ⅱ）<equation>\frac{8}{27}.</equation>
**解析: **解（I）记<equation>Y</equation>的分布函数为<equation>F_{Y}(y).</equation>由Y的定义知，<equation>P\{1\leqslant Y\leqslant 2\} = 1.</equation>当<equation>y < 1</equation>时，<equation>F_{Y}(y) = P\{Y\leqslant y\} = 0.</equation>当 1≤y<2时，<equation>\begin{aligned} F _ {Y} (y) &= P \{Y \leqslant y \} = P \{Y < 1 \} + P \{Y = 1 \} + P \{1 < Y \leqslant y \} \\ &= 0 + P \{X \geqslant 2 \} + P \{1 < X \leqslant y \} \\ &= \int_ {2} ^ {3} \frac {1}{9} x ^ {2} \mathrm {d} x + \int_ {1} ^ {y} \frac {1}{9} x ^ {2} \mathrm {d} x \\ &= \frac {1 9}{2 7} + \frac {y ^ {3} - 1}{2 7} = \frac {y ^ {3} + 1 8}{2 7}. \end{aligned}</equation>当<equation>y \geqslant 2</equation>时，<equation>F_{Y}(y) = P\{Y \leqslant y\} = 1.</equation>因此，<equation>Y</equation>的分布函数为<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 1,\\ \frac{y^{3} + 18}{27}, & 1\leqslant y < 2,\\ 1, & y\geqslant 2. \end{array} \right.</equation>（Ⅱ）（法一）由 Y的定义知，<equation>\begin{aligned} P \{X \leqslant Y \} &= P \{X < Y \} + P \{X = Y \} = P \{X \leqslant 1 \} + P \{1 < X < 2 \} \\ &= P \{X < 2 \} = \int_ {0} ^ {2} \frac {1}{9} x ^ {2} \mathrm {d} x = \frac {8}{2 7}. \end{aligned}</equation>（法二）<equation>P \{ X \leqslant Y \} = 1 - P \{ X > Y \} = 1 - P \{ X \geqslant 2 \} = P \{ X < 2 \} = \int_ {0} ^ {2} \frac {1}{9} x^{2} \mathrm {d} x = \frac {8}{2 7}.</equation>

---

**2012年第7题 | 选择题 | 4分 | 答案: A**
7. 设随机变量 X与 Y相互独立，且分别服从参数为1与参数为4的指数分布，则<equation>P\{X < Y\} =</equation>（    ）

A.<equation>\frac{1}{5}</equation>B.<equation>\frac{1}{3}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{4}{5}</equation>
答案: A
**解析: **解 由题设知，<equation>f_{X}(x)=\left\{ \begin{array}{ll}\mathrm{e}^{-x},&x>0\\ 0,&x\leqslant 0, \end{array} \right. f_{Y}(y)=\left\{ \begin{array}{ll}4\mathrm{e}^{-4y},&y>0\\ 0,&y\leqslant 0. \end{array} \right.</equation>由于 X与Y相互独立，故 (X,Y）的概率密度为<equation>f (x, y) = f _ {X} (x) f _ {Y} (y) = \left\{ \begin{array}{l l} 4 \mathrm {e} ^ {- x - 4 y}, & x > 0, y > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>记<equation>D=\{(x,y)\mid x<y\}</equation>，则<equation>\begin{aligned} P \{X < Y \} &= \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {+ \infty} \mathrm {d} y \int_ {0} ^ {y} 4 \mathrm {e} ^ {- x - 4 y} \mathrm {d} x = \int_ {0} ^ {+ \infty} 4 \mathrm {e} ^ {- 4 y} \left(1 - \mathrm {e} ^ {- y}\right) \mathrm {d} y \\ &= \int_ {0} ^ {+ \infty} \left(4 \mathrm {e} ^ {- 4 y} - 4 \mathrm {e} ^ {- 5 y}\right) \mathrm {d} y = 1 - \frac {4}{5} = \frac {1}{5}. \end{aligned}</equation>应选A.

---

**2009年第8题 | 选择题 | 4分 | 答案: B**
8. 设随机变量 X与 Y相互独立，且 X服从标准正态分布 N(0,1), Y的概率分布为<equation>P\{Y=0\}=P\{Y=1\}=\frac{1}{2}</equation>. 记<equation>F_{Z}(z)</equation>为随机变量 Z=XY的分布函数，则函数<equation>F_{Z}(z)</equation>的间断点个数为（    )

A.0 B.1 C.2 D.3
答案: B
**解析: **解 先用两种方法求<equation>F_{Z}(z).</equation>（法一）由定义知<equation>\begin{aligned} F _ {Z} (z) &= P \{Z \leqslant z \} = P \{X Y \leqslant z \} \\ &= P \{X Y \leqslant z, Y = 0 \} + P \{X Y \leqslant z, Y = 1 \} \\ &= P \{z \geqslant 0, Y = 0 \} + P \{X \leqslant z, Y = 1 \} \\ &= P \{z \geqslant 0, Y = 0 \} + P \{X \leqslant z \} \cdot P \{Y = 1 \} \quad (X \text {与} Y \text {相 互 独立}) \\ &= P \{z \geqslant 0, Y = 0 \} + \frac {1}{2} \Phi (z), \end{aligned}</equation>其中<equation>\varPhi (z)</equation>为标准正态分布函数.

当<equation>z < 0</equation>时，<equation>P\{z\geqslant 0, Y = 0\} = P(\varnothing) = 0</equation>，从而<equation>F_{Z}(z) = \frac{1}{2}\Phi (z).</equation>当<equation>z \geqslant 0</equation>时，<equation>P\{z \geqslant 0, Y = 0\} = P\{Y = 0\} = \frac{1}{2}</equation>，从而<equation>F_{Z}(z) = \frac{1}{2} +\frac{1}{2}\Phi (z).</equation>（法二）由全概率公式知<equation>\begin{array}{l} F _ {Z} (z) = P \{Z \leqslant z \} = P \{X Y \leqslant z \} \\ = P \left\{X Y \leqslant z \mid Y = 0 \right\} \cdot P \left\{Y = 0 \right\} + P \left\{X Y \leqslant z \mid Y = 1 \right\} \cdot P \left\{Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \mid Y = 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \mid Y = 1 \right\} \\ = \frac {1}{2} P \left\{z \geqslant 0 \right\} + \frac {1}{2} P \left\{X \leqslant z \right\} \quad (X \text {与} Y \text {相 互 独立}) \\ = \left\{ \begin{array}{l l} \frac {1}{2} \Phi (z), & z < 0, \\ \frac {1}{2} + \frac {1}{2} \Phi (z), & z \geqslant 0. \end{array} \right. \\ \end{array}</equation>由于<equation>\varPhi(z)</equation>连续，故<equation>F_{z}(z)</equation>仅在<equation>z = 0</equation>处间断，从而选B.

---


**2024年第22题 | 解答题 | 12分**


设总体 X服从<equation>[0,\theta]</equation>上的均匀分布，其中<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.记<equation>X_{(n)}=\max\{X_{1},X_{2},\cdots,X_{n}\}, T_{c}=cX_{(n)}</equation>.

I. 求 c，使得<equation>T_{c}</equation>是<equation>\theta</equation>的无偏估计；

II. 记<equation>h(c)=E\left[ (T_{c}-\theta)^{2} \right]</equation>，求 c使得 h(c)最小.

**答案:**(1) 当<equation>c=\frac{n+1}{n}</equation>时，<equation>T_{c}</equation>是<equation>\theta</equation>的无偏估计.

(2) 当<equation>c=\frac{n+2}{n+1}</equation>时，h（c）最小.

**解析:**（I）由于<equation>X</equation>服从<equation>[0,\theta]</equation>上的均匀分布，故<equation>X</equation>的分布函数为<equation>F _ {X} (x) = \left\{ \begin{array}{l l} 0, & x < 0, \\ \frac {x}{\theta}, & 0 \leqslant x < \theta , \\ 1, & x \geqslant \theta . \end{array} \right.</equation>记随机变量<equation>Y = X_{(n)} = \max \left\{X_{1}, X_{2}, \dots, X_{n}\right\}</equation>. 计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>.

当<equation>y < 0</equation>时，<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < \theta</equation>时，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\max _ {1 \leqslant i \leqslant n} X _ {i} \leqslant y \right\} = P \left\{X _ {1} \leqslant y, X _ {2} \leqslant y, \dots , X _ {n} \leqslant y \right\} \\ \underline {{\text {独立 性}}} P \left\{X _ {1} \leqslant y \right\} P \left\{X _ {2} \leqslant y \right\} \dots P \left\{X _ {n} \leqslant y \right\} = F _ {X} ^ {n} (y) = \left(\frac {y}{\theta}\right) ^ {n}. \\ \end{array}</equation>当<equation>y\geqslant \theta</equation>时，<equation>F_{Y}(y) = 1.</equation>于是，<equation>F_{Y}(y) = \left\{ \begin{array}{ll}0, & y < 0,\\ \left(\frac{y}{\theta}\right)^{n}, & 0\leqslant y < \theta ,\\ 1, & y\geqslant \theta . \end{array} \right.</equation>对<equation>F_{Y}(y)</equation>求导，可得<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {n y ^ {n - 1}}{\theta^ {n}}, & 0 < y < \theta , \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>\begin{aligned} E \left(T _ {c}\right) &= E (c Y) = c \int_ {- \infty} ^ {+ \infty} y \cdot f _ {Y} (y) \mathrm {d} y = c \int_ {0} ^ {\theta} y \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = c \cdot \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 1}}{n + 1} \Bigg | _ {0} ^ {\theta} \\ &= \frac {c n}{n + 1} \theta . \end{aligned}</equation>若<equation>T_{c}</equation>为<equation>\theta</equation>的无偏估计，则<equation>E\left(T_{c}\right)=\theta</equation>，从而<equation>\frac{cn}{n+1}\theta =\theta</equation>，解得<equation>c=\frac{n+1}{n}.</equation>（Ⅱ）展开 h(c）可得<equation>h (c) = E \left[ \left(T _ {c} - \theta\right) ^ {2} \right] = E \left[ \left(c Y - \theta\right) ^ {2} \right] = c ^ {2} E \left(Y ^ {2}\right) - 2 c \theta E (Y) + \theta^ {2}.</equation>计算<equation>E ( Y^{2})</equation><equation>E \left(Y ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} y ^ {2} \cdot f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {\theta} y ^ {2} \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 2}}{n + 2} \Bigg | _ {0} ^ {\theta} = \frac {n}{n + 2} \theta^ {2}.</equation>于是，<equation>h (c) = c ^ {2} \cdot \frac {n}{n + 2} \theta^ {2} - 2 c \cdot \frac {n}{n + 1} \theta^ {2} + \theta^ {2} = \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right) \theta^ {2}.</equation>令<equation>\frac{\mathrm{d}[h(c)]}{\mathrm{d}c}=\left(\frac{2n}{n+2} c-\frac{2n}{n+1}\right)\theta^{2}=0</equation>，解得<equation>c=\frac{n+2}{n+1}</equation>该点是h(c)的唯一驻点.又因为<equation>h^{\prime \prime}(c)</equation><equation>= \frac{2n}{n+2}\theta^{2} > 0</equation>，所以该唯一驻点是h(c)的极小值点，也是最小值点.

因此，当<equation>c=\frac{n+2}{n+1}</equation>时，h(c）最小.

