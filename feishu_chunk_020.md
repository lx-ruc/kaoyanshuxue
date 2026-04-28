A.<equation>- 2-\sqrt{1 0}</equation>B.<equation>- 2+\sqrt{1 0}</equation>C.<equation>- 2-\sqrt{6}</equation>D.<equation>- 2+\sqrt{6}</equation>
答案: B
**解析: **由于<equation>X\sim N(0,2),Y\sim N(-2,2)</equation>，故<equation>E(X) = 0,D(X) = 2,E(Y) = -2,D(Y) = 2</equation>，从而<equation>E (2 X + Y) = E (2 X) + E (Y) = 2 E (X) + E (Y) = - 2,</equation><equation>D (2 X + Y) = D (2 X) + D (Y) = 4 D (X) + D (Y) = 4 \times 2 + 2 = 1 0,</equation><equation>E (Y - X) = E (Y) - E (X) = - 2,</equation><equation>D (Y - X) = D (Y) + D (X) = 4.</equation>于是，<equation>2 X+Y\sim N(-2,1 0), Y-X\sim N(-2,4).</equation>将它们标准化可得<equation>\frac{2 X+Y+2}{\sqrt{1 0}}\sim N(0,1), \frac{Y-X+2}{2}</equation><equation>\sim N(0,1).</equation>由此可得，<equation>P \left\{2 X + Y < a \right\} = P \left\{2 X + Y \leqslant a \right\} = P \left\{\frac {2 X + Y + 2}{\sqrt {1 0}} \leqslant \frac {a + 2}{\sqrt {1 0}} \right\} = \Phi \left(\frac {a + 2}{\sqrt {1 0}}\right),</equation><equation>P \{X > Y \} = P \{Y - X < 0 \} = P \{Y - X \leqslant 0 \} = P \left\{\frac {Y - X + 2}{2} \leqslant 1 \right\} = \Phi (1),</equation>其中<equation>\varPhi(x)</equation>是标准正态分布<equation>N(0,1)</equation>的分布函数.

由<equation>P\{2X + Y < a\} = P\{X > Y\}</equation>可得<equation>\varPhi\left(\frac{a + 2}{\sqrt{10}}\right) = \varPhi(1).</equation>又因为<equation>\varPhi(x)</equation>单调增加，所以<equation>\frac{a + 2}{\sqrt{10}} = 1</equation>，即<equation>a = -2 + \sqrt{10}.</equation>因此，应选B.

---

**2024年第16题 | 填空题 | 5分**
16. 设随机试验每次成功的概率为 p，现进行3次独立重复试验，在至少成功1次的条件下，3次试验全部成功的概率为<equation>\frac{4}{1 3}</equation>，则 p=___
**答案: **#<equation>p = \frac{2}{3}</equation>
**解析: **解设 X为3次独立重复试验中试验成功的次数，则<equation>X\sim B(3,p).</equation>在至少成功1次的条件下， 3次试验全部成功的概率为<equation>P\{X=3\mid X\geqslant 1\}=\frac{P\{X=3,X\geqslant 1\}}{P\{X\geqslant 1\}}=\frac{P\{X=3\}}{P\{X\geqslant 1\}}=\frac{C_{3}^{3} p^{3}}{1-C_{3}^{0}(1-p)^{3}}=\frac{4}{13}.</equation>于是，<equation>\frac{p^{3}}{1-(1-p)^{3}}=\frac{4}{13}.</equation>整理可得<equation>3 p^{3}+4 p^{2}-4 p=0</equation>即 p（p+2）(3p-2）=0.由于 p>0，故 p<equation>=\frac{2}{3}.</equation>

---

**2023年第16题 | 填空题 | 5分**
16. 设随机变量与 Y相互独立， X且<equation>X\sim B\left(1,\frac{1}{3}\right),Y\sim B\left(2,\frac{1}{2}\right)</equation>则<equation>P\{X=Y\}=</equation>___
**解析: **解 由于<equation>X\sim B\left(1,\frac{1}{3}\right)</equation>，故<equation>P \left\{X = 0 \right\} = \mathrm {C} _ {1} ^ {0} \left(\frac {1}{3}\right) ^ {0} \left(\frac {2}{3}\right) ^ {1} = \frac {2}{3},</equation><equation>P \{X = 1 \} = C _ {1} ^ {1} \left(\frac {1}{3}\right) ^ {1} \left(\frac {2}{3}\right) ^ {0} = \frac {1}{3}.</equation>由于<equation>Y\sim B\left(2,\frac{1}{2}\right)</equation>，故<equation>P \left\{Y = 0 \right\} = \mathrm {C} _ {2} ^ {0} \left(\frac {1}{2}\right) ^ {0} \left(\frac {1}{2}\right) ^ {2} = \frac {1}{4},</equation><equation>P \left\{Y = 1 \right\} = \mathrm {C} _ {2} ^ {1} \left(\frac {1}{2}\right) ^ {1} \left(\frac {1}{2}\right) ^ {1} = \frac {1}{2}.</equation>因此，<equation>\begin{aligned} P \{X = Y \} &= P \{X = 0, Y = 0 \} + P \{X = 1, Y = 1 \} \\ \underline {{\text {独立性}}} P \{X = 0 \} P \{Y = 0 \} + P \{X = 1 \} P \{Y = 1 \} \\ &= \frac {2}{3} \times \frac {1}{4} + \frac {1}{3} \times \frac {1}{2} = \frac {1}{3}. \end{aligned}</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: A**
8. 设随机变量 X与 Y相互独立，且都服从正态分布<equation>N\left(\mu ,\sigma^{2}\right)</equation>，则<equation>P\{|X-Y|<1\}</equation>(    )

A. 与<equation>\mu</equation>无关，而与<equation>\sigma^{2}</equation>有关 B. 与<equation>\mu</equation>有关，而与<equation>\sigma^{2}</equation>无关

C. 与<equation>\mu,\sigma^{2}</equation>都有关 D. 与<equation>\mu,\sigma^{2}</equation>都无关
答案: A
**解析: **解 由于 X，Y相互独立且都服从正态分布<equation>N(\mu, \sigma^{2})</equation>，故<equation>E(X-Y)=0,D(X-Y)=2\sigma^{2},</equation><equation>X-Y\sim N(0,2\sigma^{2}).</equation>将 X-Y标准化，可得<equation>\frac{X-Y}{\sqrt{2}\sigma}\sim N(0,1).</equation>，于是，<equation>\begin{array}{l} P \left\{\mid X - Y \mid < 1 \right\} = P \left\{- 1 < X - Y < 1 \right\} = P \left\{\frac {- 1}{\sqrt {2} \sigma} < \frac {X - Y}{\sqrt {2} \sigma} < \frac {1}{\sqrt {2} \sigma} \right\} \\ = \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - \Phi \left(\frac {- 1}{\sqrt {2} \sigma}\right) = 2 \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - 1. \\ \end{array}</equation>因此，<equation>P\{|X - Y| < 1\}</equation>仅与<equation>\sigma^2</equation>有关.应选A.

---

**2018年第7题 | 选择题 | 4分 | 答案: A**
7. 设随机变量 X的概率密度 f(x)满足<equation>f(1+x)=f(1-x)</equation>，且<equation>\int_{0}^{2} f(x)\mathrm{d}x=0.6</equation>，则<equation>P\{ X<0\}=</equation>(    )

A. 0.2 B. 0.3 C. 0.4 D. 0.5
答案: A
**解析: **解（法一）由于<equation>f(1+x)=f(1-x)</equation>，故 f(x)的图像关于 x=1对称.于是，<equation>P\{X<0\}= P\{X>2\}.</equation>又因为<equation>P \{0 \leqslant X \leqslant 2 \} = \int_{0}^{2} f ( x ) \mathrm{d} x = 0. 6</equation>，且<equation>P \{X < 0 \} + P \{0 \leqslant X \leqslant 2 \} + P \{X > 2 \} = 1,</equation>所以<equation>P \{ X < 0 \} = \frac {1 - P \{0 \leqslant X \leqslant 2 \}}{2} = \frac {1 - 0 . 6}{2} = 0. 2.</equation>因此，应选A.

（法二）利用换元法.

由于<equation>\begin{aligned} \int_ {- \infty} ^ {0} f (x) \mathrm {d} x \xlongequal {u = 1 - x} \int_ {+ \infty} ^ {1} f (1 - u) \mathrm {d} (1 - u) &= \int_ {1} ^ {+ \infty} f (1 - u) \mathrm {d} u \\ \frac {f (1 + u) = f (1 - u)}{\mathrm {二}} \int_ {1} ^ {+ \infty} f (1 + u) \mathrm {d} u &= \int_ {2} ^ {+ \infty} f (t) \mathrm {d} t, \end{aligned}</equation>故<equation>P\{X < 0\} = P\{X > 2\}</equation>.

其余同法一.

---

**2017年第14题 | 填空题 | 4分**
14. 设随机变量 X的分布函数为<equation>F ( x )=0. 5 \Phi ( x )+0. 5 \Phi \left( \frac{x-4}{2} \right)</equation>，其中<equation>\Phi ( x )</equation>为标准正态分布函数，则<equation>E ( X )=</equation>
**答案: **```latex
2
```

**解析:**解记<equation>\varphi(x)</equation>为标准正态分布的概率密度函数，则<equation>\int_{-\infty}^{+\infty}\varphi(x)\mathrm{d}x=1,\int_{-\infty}^{+\infty}x\varphi(x)\mathrm{d}x=0.</equation>由题设知，X的概率密度为<equation>f(x)=F^{\prime}(x)=0. 5 \varphi(x)+0. 2 5 \varphi \left( \frac{x-4}{2} \right)</equation>，于是<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} \left[ 0. 5 x \varphi (x) + 0. 2 5 x \varphi \left(\frac {x - 4}{2}\right) \right] \mathrm {d} x \\ &= 0 + 0. 2 5 \int_ {- \infty} ^ {+ \infty} x \varphi \left(\frac {x - 4}{2}\right) \mathrm {d} x \xlongequal {t = \frac {x - 4}{2}} 0. 5 \int_ {- \infty} ^ {+ \infty} (2 t + 4) \varphi (t) \mathrm {d} t \\ &= \int_ {- \infty} ^ {+ \infty} t \varphi (t) \mathrm {d} t + 2 \int_ {- \infty} ^ {+ \infty} \varphi (t) \mathrm {d} t = 0 + 2 = 2. \end{aligned}</equation>

---

**2016年第7题 | 选择题 | 4分 | 答案: B**

7. 设随机变量<equation>X\sim N(\mu,\sigma^{2})(\sigma>0)</equation>，记<equation>p=P\{X\leqslant\mu+\sigma^{2}\}</equation>，则（    )

A. p随着<equation>\mu</equation>的增加而增加 B. p随着<equation>\sigma</equation>的增加而增加

C. p随着<equation>\mu</equation>的增加而减少 D. p随着<equation>\sigma</equation>的增加而减少

答案: B

**解析:**解（法一）令<equation>Y=\frac{X-\mu}{\sigma}</equation>，则由<equation>X\sim N(\mu ,\sigma^{2})</equation>知，<equation>Y\sim N(0,1).</equation>又<equation>p = P \left\{X \leqslant \mu + \sigma^ {2} \right\} = P \left\{\frac {X - \mu}{\sigma} \leqslant \sigma \right\} = P \left\{Y \leqslant \sigma \right\}</equation>故 p与<equation>\mu</equation>的取值无关，且p随着<equation>\sigma</equation>的增加而增加.应选B.

（法二）由于<equation>X\sim N(\mu ,\sigma^2)</equation>，故<equation>\begin{array}{l} p = P \left\{X \leqslant \mu + \sigma^ {2} \right\} = \int_ {- \infty} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \\ = \int_ {- \infty} ^ {\mu} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x + \int_ {\mu} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \\ = \frac {1}{2} + \int_ {\mu} ^ {\mu + \sigma^ {2}} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \xlongequal {t = \frac {x - \mu}{\sigma}} \frac {1}{2} + \int_ {0} ^ {\sigma} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {t ^ {2}}{2}} \mathrm {d} t, \\ \end{array}</equation>从而<equation>p</equation>与<equation>\mu</equation>的取值无关，且<equation>p</equation>随着<equation>\sigma</equation>的增加而增加.应选B.

---

**2013年第7题 | 选择题 | 4分 | 答案: A**

7. 设<equation>X_{1}, X_{2}, X_{3}</equation>是随机变量，且<equation>X_{1}\sim N(0,1), X_{2}\sim N\left(0,2^{2}\right), X_{3}\sim N\left(5,3^{2}\right), p_{i}=P\left\{-2\leqslant X_{i}\leqslant 2\right\} (i=1,2,3)</equation>则（    ）

A.<equation>p_{1}>p_{2}>p_{3}</equation>B.<equation>p_{2}>p_{1}>p_{3}</equation>C.<equation>p_{3}>p_{1}>p_{2}</equation>D.<equation>p_{1}>p_{3}>p_{2}</equation>

答案: A

**解析:**解 由<equation>X_{2} \sim N(0,2^{2}), X_{3} \sim N(5,3^{2})</equation>知，<equation>\frac{X_2}{2} \sim N(0,1), \frac{X_3 - 5}{3} \sim N(0,1)</equation>.于是，<equation>p_{1} = P\{-2 \leqslant X_{1} \leqslant 2\} = \Phi (2) - \Phi (-2) = 1 - \Phi (-2) - \Phi (-2) = 1 - 2\Phi (-2),</equation><equation>p_{2} = P\{-2 \leqslant X_{2} \leqslant 2\} = P\{-1 \leqslant \frac{X_{2}}{2} \leqslant 1\} = \Phi (1) - \Phi (-1) = 1 - 2\Phi (-1),</equation><equation>p_{3} = P\{-2 \leqslant X_{3} \leqslant 2\} = P\{- \frac{7}{3} \leqslant \frac{X_3 - 5}{3} \leqslant -1\} = \Phi (-1) - \Phi \left(-\frac{7}{3}\right).</equation>于<equation>\Phi (-1) > \Phi (-2)</equation>，故<equation>p_{1} > p_{2}</equation>.

由于<equation>\varPhi(-1) > \varPhi(-2)</equation>，故<equation>p_1 > p_2</equation>。

设标准正态分布的概率密度为<equation>\varphi(x)</equation>，则<equation>\varphi(x)</equation>为偶函数，且在<equation>(-\infty ,0]</equation>上单调增加（如图所示）.又由于<equation>p_{2}=\int_{-1}^{1}\varphi(x)\mathrm{d}x, p_{3}=</equation><equation>\int_{-\frac{7}{3}}^{-1}\varphi(x)\mathrm{d}x</equation>，而<equation>\varphi(x)</equation>在（-1,1）上的取值都大于<equation>\varphi(x)</equation>在<equation>\left(-\frac{7}{3},-1\right)</equation>上的取值，且积分区间的长度满足<equation>|1-(-1)|> \left| -1-\left(-\frac{7}{3}\right) \right|</equation>，故<equation>p_{2}>p_{3}.</equation>综上所述，<equation>p_{1}>p_{2}>p_{3}.</equation>应选A.

---

**2013年第14题 | 填空题 | 4分**

14. 设随机变量<equation>Y</equation>服从参数为 1 的指数分布,<equation>a</equation>为常数且大于零, 则<equation>P\{Y \leqslant a+1 \mid Y > a\} =</equation>___

**解析:**解 由题设知，Y的概率密度为<equation>f_{Y}(y)=\left\{\begin{array}{ll}\mathrm{e}^{-y},&y>0,\\ 0,&y\leqslant 0.\end{array}\right.</equation>又 a > 0，故<equation>P \left\{Y \leqslant a + 1 \mid Y > a \right\} = \frac {P \left\{a < Y \leqslant a + 1 \right\}}{P \left\{Y > a \right\}} = \frac {\int_ {a} ^ {a + 1} \mathrm {e} ^ {- y} \mathrm {d} y}{\int_ {a} ^ {+ \infty} \mathrm {e} ^ {- y} \mathrm {d} y} = \frac {\mathrm {e} ^ {- a} - \mathrm {e} ^ {- a - 1}}{\mathrm {e} ^ {- a}} = 1 - \frac {1}{\mathrm {e}}.</equation>

---

**2011年第7题 | 选择题 | 4分 | 答案: D**

7. 设<equation>F_{1}(x)</equation>与<equation>F_{2}(x)</equation>为两个分布函数，其相应的概率密度<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>是连续函数，则必为概率密度的是（    )

A.<equation>f_{1}(x)f_{2}(x)</equation>B.<equation>2f_{2}(x)F_{1}(x)</equation>C.<equation>f_{1}(x)F_{2}(x)</equation>D.<equation>f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)</equation>

答案: D

**解析:**解 由分布函数和概率密度的性质知，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)\geqslant 0</equation>，且<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \left[ f _ {1} (x) F _ {2} (x) + f _ {2} (x) F _ {1} (x) \right] \mathrm {d} x &= \int_ {- \infty} ^ {+ \infty} \left[ F _ {1} (x) F _ {2} (x) \right] ^ {\prime} \mathrm {d} x \\ &= F _ {1} (+ \infty) F _ {2} (+ \infty) - F _ {1} (- \infty) F _ {2} (- \infty) \\ &= 1 - 0 = 1. \end{aligned}</equation>因此，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)</equation>为概率密度.应选D.

---

**2010年第7题 | 选择题 | 4分 | 答案: C**

7. 设随机变量 X的分布函数 F(x) =<equation>\left\{\begin{array}{l l}0,&x<0,\\ \frac{1}{2},&0\leqslant x<1,\\ 1-\mathrm{e}^{-x},&x\geqslant 1,\end{array} \right.</equation>则 P{X=1} =（    )

A. 0 B.<equation>\frac{1}{2}</equation>C.<equation>\frac{1}{2}-\mathrm{e}^{-1}</equation><equation>1 - \mathrm {e} ^ {- 1}</equation>

答案: C

**解析:**解<equation>P \{ X = 1 \} = P \{ X \leqslant 1 \} - P \{ X < 1 \} = F ( 1 ) - F ( 1^{-} ) = 1 - \frac{1} {\mathrm{e}} - \frac{1}{2} = \frac{1}{2} - \frac{1} {\mathrm{e}}</equation>，故选C.

---

**2010年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>f_{1}(x)</equation>为标准正态分布的概率密度，<equation>f_{2}(x)</equation>为<equation>[-1,3]</equation>上均匀分布的概率密度，若<equation>f (x) = \left\{ \begin{array}{l l} a f _ {1} (x), & x \leqslant 0, \\ b f _ {2} (x), & x > 0 \end{array} \right. \quad (a > 0, b > 0)</equation>为概率密度，则 a,b应满足（    ）

A. 2a+3b=4 B. 3a+2b=4 C. a+b=1 D. a+b=2

答案: A

**解析:**解 由于标准正态分布的概率密度的图形关于 x=0对称，故<equation>\int_{0}^{+\infty} f_{1}(x)\mathrm{d}x=\int_{-\infty}^{0} f_{1}(x)\mathrm{d}x=\frac{1}{2}.</equation>又由题设知，<equation>f_{2}(x)=\left\{\begin{array}{ll}\frac{1}{4},&-1\leqslant x\leqslant 3,\\ 0,&\text{其他}.\end{array} \right.</equation>由于 f(x)为概率密度，故<equation>1=\int_{-\infty}^{+\infty} f(x)\mathrm{d}x=\int_{-\infty}^{0} a f_{1}(x)\mathrm{d}x+\int_{0}^{+\infty} b f_{2}(x)\mathrm{d}x=\frac{1}{2} a+\int_{0}^{3} \frac{b}{4}\mathrm{d}x=\frac{1}{2} a+\frac{3}{4} b,</equation>即<equation>\frac{1}{2} a+\frac{3}{4} b=1</equation>从而2a+3b=4.应选A.

---


### 参数估计与假设检验


#### 假设检验

**2025年第10题 | 选择题 | 5分 | 答案: D**

10. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自正态总体<equation>N (\mu ,2)</equation>的简单随机样本，记<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, Z_{\alpha}</equation>表示标准正态分布的上侧<equation>\alpha</equation>分位数，假设检验问题：<equation>H_{0}:\mu \leqslant 1, H_{1}:\mu >1</equation>的显著性水平为<equation>\alpha</equation>的检验的拒绝域为（    )

A.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{2}{n}Z_{\alpha}\right\}</equation>B.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{\sqrt{2}}{n}Z_{\alpha}\right\}</equation>C.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\frac{2}{\sqrt{n}}Z_{\alpha}\right\}</equation>D.<equation>\left\{(X_{1},X_{2},\cdots,X_{n})\mid \bar{X}>1+\sqrt{\frac{2}{n}}Z_{\alpha}\right\}</equation>

答案: D

**解析:**解 由已知条件可知，总体方差<equation>\sigma^{2}=2.</equation>根据分析，方差为2的单个正态总体对均值<equation>\mu</equation>的假设检验问题：<equation>H_{0}:\mu\leqslant1,H_{1}:\mu>1</equation>的显著性水平为<equation>\alpha</equation>的检验的拒绝域为<equation>\overline{x}>1+\sqrt{\frac{2}{n}}z_{\alpha}</equation>其中<equation>z_{\alpha}</equation>为标准正态分布的上侧<equation>\alpha</equation>分位数.

因此，应选D.

---

**2021年第10题 | 选择题 | 5分 | 答案: B**

10. 设<equation>X_{1}, X_{2}, \cdots , X_{1 6}</equation>是来自总体<equation>N (\mu , 4)</equation>的简单随机样本，考虑假设检验问题：<equation>H_{0}:\mu \leqslant 1 0, H_{1}:\mu > 1 0, \Phi (x)</equation>表示标准正态分布函数，若该检验问题的拒绝域为<equation>W=\{\bar{X}>1 1 \}</equation>，其中<equation>\bar{X}=\frac{1}{1 6} \sum_{i=1}^{1 6} X_{i}</equation>，则<equation>\mu =1 1. 5</equation>时，该检验犯第二类错误的概率为（    ）

A. 1-<equation>\Phi (0. 5)</equation>B. 1-<equation>\Phi (1)</equation>C. 1-<equation>\Phi (1. 5)</equation>D. 1-<equation>\Phi (2)</equation>

答案: B

**解析:**解 根据已知条件，<equation>\mu=1 1. 5</equation>，原假设<equation>H_{0}:\mu\leqslant1 0</equation>不为真.由于该检验问题的拒绝域为<equation>W=\left\{\overline{X}>11\right\}</equation>，故当<equation>\overline{X}\leqslant1 1</equation>时，不拒绝<equation>H_{0}</equation>.此时，该检验犯了第二类错误，其概率为<equation>P\{\overline{X}\leqslant11\}</equation>下面我们计算<equation>P\{\overline{X}\leqslant11\}</equation>由已知条件可得<equation>n=1 6</equation>，故<equation>\overline{X}\sim N\left(\mu ,\frac{4}{1 6}\right)</equation>，即<equation>\overline{X}\sim N\left(1 1. 5 , \frac{1}{4}\right)</equation>.标准化可得，<equation>\frac{\overline{X}-1 1. 5}{\frac{1}{2}}\sim N(0,1).</equation><equation>P\{\overline{X}\leqslant11\}=P\left\{\frac{\overline{X}-1 1. 5}{\frac{1}{2}}\leqslant\frac{1 1-1 1. 5}{\frac{1}{2}}\right\}=\Phi(-1)=1-\Phi(1).</equation>因此，应选B.

---

**2018年第8题 | 选择题 | 4分 | 答案: D**

8. 设总体 X服从正态分布<equation>N\left(\mu ,\sigma^{2}\right).</equation><equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本，据此样本检验假设：<equation>H_{0}:\mu=\mu_{0},H_{1}:\mu\neq\mu_{0}</equation>，则（    )

A. 如果在检验水平<equation>\alpha=0. 0 5</equation>下拒绝<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必拒绝<equation>H_{0}</equation>B. 如果在检验水平<equation>\alpha=0. 0 5</equation>下拒绝<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必接受<equation>H_{0}</equation>C. 如果在检验水平<equation>\alpha=0. 0 5</equation>下接受<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必拒绝<equation>H_{0}</equation>D. 如果在检验水平<equation>\alpha=0. 0 5</equation>下接受<equation>H_{0}</equation>，那么<equation>\alpha=0. 0 1</equation>下必接受<equation>H_{0}</equation>

答案: D

**解析:**解 由于<equation>\sigma^2</equation>未知，故应采用<equation>t</equation>检验法，检验统计量可取为<equation>Z = \frac{\bar{X} - \mu_0}{S / \sqrt{n}}</equation>（注：<equation>S^{2}</equation>为样本方差，为方差<equation>\sigma^2</equation>的无偏估计量）.<equation>\bar{X} = \frac{1}{n}\sum_{i = 1}^{n}X_{i},\bar{X}\sim N\left(\mu ,\frac{\sigma^{2}}{n}\right)</equation>，故当假设<equation>H_{0}</equation>为真时，<equation>Z\sim t(n - 1)</equation>.

当<equation>\alpha = 0.05</equation>时，拒绝域为<equation>\left|\frac{\bar{x} - \mu_0}{S / \sqrt{n}}\right| > t_{\frac{\alpha}{2}} = t_{0.025}</equation>，其中<equation>t_{0.025}</equation>为上0.025分位点.<equation>\alpha = 0.05</equation>对应的接受域为<equation>\left(\mu_0 - t_{0.025}\frac{S}{\sqrt{n}},\mu_0 + t_{0.025}\frac{S}{\sqrt{n}}\right)</equation>.

当<equation>\alpha=0.01</equation>时，拒绝域为<equation>\left| \frac{\overline{{x}}-\mu_{0}}{S / \sqrt{n}} \right| > t_{\frac{\alpha}{2}}=t_{0.005}</equation>，其中<equation>t_{0.005}</equation>为上0.005分位点.<equation>\alpha=0.01</equation>对应的接受域为<equation>\left(\mu_{0}-t_{0.005}\frac{S}{\sqrt{n}},\mu_{0}+t_{0.005}\frac{S}{\sqrt{n}}\right).</equation>因为<equation>t_{0.025}<t_{0.005}</equation>，所以<equation>\alpha=0.05</equation>对应的接受域包含于<equation>\alpha=0.01</equation>对应的接受域.若当检验水平<equation>\alpha=0.05</equation>时，接受<equation>H_{0}</equation>，则当检验水平<equation>\alpha=0.01</equation>时，必接受<equation>H_{0}.</equation>因此，应选D.

---


#### 矩估计和最大似然估计

**2022年第22题 | 解答题 | 12分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自均值为<equation>\theta</equation>的指数分布总体的简单随机样本，<equation>Y_{1}, Y_{2}, \dots, Y_{m}</equation>为来自均值为2<equation>\theta</equation>的指数分布总体的简单随机样本，且两样本相互独立，其中<equation>\theta(\theta>0)</equation>是未知参数。利用样本<equation>X_{1}, X_{2}, \dots, X_{n}, Y_{1}, Y_{2}, \dots, Y_{m}</equation>求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}</equation>，并求<equation>D(\hat{\theta})</equation>

**答案:**<equation>\hat {\theta} = \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)}, D (\hat {\theta}) = \frac {\theta^ {2}}{m + n}.</equation>

**解析:**解<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体X的简单随机样本.由于<equation>E ( X )=\theta</equation>，故X服从参数为<equation>\frac{1}{\theta}</equation>的指数分布.于是，X的概率密度函数为<equation>f _ {X} (x) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm {e} ^ {- \frac {x}{\theta}}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.</equation><equation>Y_{1}, Y_{2}, \dots , Y_{m}</equation>是来自总体<equation>Y</equation>的简单随机样本.由于<equation>E(Y)=2\theta</equation>，故Y服从参数为<equation>\frac{1}{2\theta}</equation>的指数分布.于是，<equation>Y</equation>的概率密度函数为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{2 \theta} \mathrm {e} ^ {- \frac {y}{2 \theta}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>设<equation>x_{1}, x_{2}, \dots , x_{n}, y_{1}, y_{2}, \dots , y_{m}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}, Y_{1}, Y_{2}, \dots , Y_{m}</equation>的一组样本值，则似然函数<equation>L (\theta) = \left\{ \begin{array}{l l} \frac {1}{2 ^ {m} \theta^ {m + n}} \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta} - \frac {\sum_ {j = 1} ^ {m} y _ {j}}{2 \theta}}, & x _ {i} > 0, y _ {j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{i} > 0, y_{j} > 0, i = 1, 2, \dots , n, j = 1, 2, \dots , m</equation>时，取对数得<equation>\ln L (\theta) = - m \ln 2 - (m + n) \ln \theta - \frac {\sum_ {i = 1} ^ {n} x _ {i}}{\theta} - \frac {\sum_ {j = 1} ^ {m} y _ {j}}{2 \theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即<equation>-\frac{m+n}{\theta}+\frac{\sum_{i=1}^{n}x_{i}}{\theta^{2}}+\frac{\sum_{j=1}^{m}y_{j}}{2\theta^{2}}=0</equation>解得<equation>\theta =\frac{2\sum_{i=1}^{n}x_{i}+\sum_{j=1}^{m}y_{j}}{2(m+n)}.</equation>因此，<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}=\frac{2\sum_{i=1}^{n}X_{i}+\sum_{j=1}^{m}Y_{j}}{2(m+n)}.</equation>下面计算<equation>D(\hat{\theta}).</equation><equation>\begin{aligned} D (\hat {\theta}) &= D \left[ \frac {2 \sum_ {i = 1} ^ {n} X _ {i} + \sum_ {j = 1} ^ {m} Y _ {j}}{2 (m + n)} \right] = \frac {1}{(m + n) ^ {2}} D \left(\sum_ {i = 1} ^ {n} X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} D \left(\sum_ {j = 1} ^ {m} Y _ {j}\right) \\ &= \frac {1}{(m + n) ^ {2}} \sum_ {i = 1} ^ {n} D \left(X _ {i}\right) + \frac {1}{4 (m + n) ^ {2}} \sum_ {j = 1} ^ {m} D \left(Y _ {j}\right) = \frac {n D (X)}{(m + n) ^ {2}} + \frac {m D (Y)}{4 (m + n) ^ {2}} \\ &= \frac {n \theta^ {2}}{(m + n) ^ {2}} + \frac {m \cdot 4 \theta^ {2}}{4 (m + n) ^ {2}} = \frac {\theta^ {2}}{m + n}. \end{aligned}</equation>或者，注意到<equation>\hat{\theta} = \frac{2\sum_{i=1}^{n}X_{i} + \sum_{j=1}^{m}Y_{j}}{2(m + n)} = \frac{2n\bar{X} + m\bar{Y}}{2(m + n)}</equation>，利用<equation>D(\bar{X}) = \frac{D(X)}{n}, D(\bar{Y}) = \frac{D(Y)}{m}</equation>可得，<equation>D(\hat{\theta}) = D\left[\frac{2n\bar{X} + m\bar{Y}}{2(m + n)}\right] = \frac{n^{2}D(\bar{X})}{(m + n)^{2}} + \frac{m^{2}D(\bar{Y})}{4(m + n)^{2}} = \frac{n^{2}}{(m + n)^{2}}\cdot \frac{D(X)}{n} + \frac{m^{2}}{4(m + n)^{2}}\cdot \frac{D(Y)}{m}</equation><equation>= \frac{n\theta^{2}}{(m + n)^{2}} + \frac{m\cdot 4\theta^{2}}{4(m + n)^{2}} = \frac{\theta^{2}}{m + n}.</equation>

---


#### 区间估计和置信区间

**2016年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{n}</equation>为来自总体<equation>N\left(\mu ,\sigma^{2}\right)</equation>的简单随机样本，样本均值<equation>\bar{X}=9. 5</equation>，参数<equation>\mu</equation>的置信度为0.95的双侧置信区间的置信上限为10.8，则<equation>\mu</equation>的置信度为0.95的双侧置信区间为 ___.

**答案:**## (8.2,10.8)

**解析:**解 由上述表格知，无论<equation>\sigma^{2}</equation>已知还是未知，参数<equation>\mu</equation>的置信度为1<equation>- \alpha</equation>的置信区间的置信上限和置信下限都关于样本均值对称，即<equation>\frac{\mathrm{置信上限}+\mathrm{置信下限}}{2}=\bar{X}</equation>从而置信下限<equation>= 2\overline{X}</equation>-置信上限<equation>= 2\times 9.5-10.8=8.2</equation>于是<equation>\mu</equation>的置信度为0.95的双侧置信区间为（8.2，10.8）.

---


### 随机事件和概率

**2025年第16题 | 填空题 | 5分**
16. 设 A,B为两个随机事件，且 A与 B相互独立，已知<equation>P ( A )=2 P ( B )</equation><equation>P ( A \cup B )=\frac{5}{8}</equation>，则在事件 A,B至少有一个发生的条件下，A,B中恰有一个发生的概率为___
**解析: **解 根据条件概率公式，A，B中至少有一个发生的条件下，A，B中恰好有一个发生的概率为<equation>\begin{aligned} P \left(A \bar {B} \cup \bar {A} B \mid A \cup B\right) &= \frac {P \left[ \left(A \bar {B} \cup \bar {A} B\right) \cap (A \cup B) \right]}{P (A \cup B)} = \frac {P \left(A \bar {B} \cup \bar {A} B\right)}{P (A \cup B)} \\ &= \frac {P \left(A \bar {B}\right) + P \left(\bar {A} B\right)}{P \left(A \cup B\right)} \xlongequal {\text {独立 性}} \frac {P (A) P (\bar {B}) + P (\bar {A}) P (B)}{P (A \cup B)}. \end{aligned}</equation>下面计算<equation>P ( A ) , P ( B )</equation>由于 A，B相互独立，故<equation>P ( A B )=P ( A ) P ( B )</equation>，结合<equation>P ( A )=2 P ( B )</equation>可得<equation>\frac{5}{8}=P(A\cup B)=P(A)+P(B)-P(AB)=P(A)+P(B)-P(A)P(B)=3P(B)-2[P(B)]^{2}.</equation>整理可得<equation>1 6 \left[ P (B) \right]^{2}-2 4 P (B)+5=0</equation>即<equation>\left[ 4 P (B)-1 \right] \left[ 4 P (B)-5 \right]=0.</equation>解得<equation>P (B)=\frac{1}{4}</equation>舍去<equation>P (B)=\frac{5}{4}).</equation>进一步可得<equation>P (A)=2 P (B)=\frac{1}{2}.</equation>因此<equation>P \left(A \bar {B} \cup \bar {A} B \mid A \cup B\right) = \frac {P (A) P (\bar {B}) + P (\bar {A}) P (B)}{P (A \cup B)} = \frac {\frac {1}{2} \cdot \frac {3}{4} + \frac {1}{2} \cdot \frac {1}{4}}{\frac {5}{8}} = \frac {4}{5}.</equation>

---

**2022年第16题 | 填空题 | 5分**
16. 设 A,B,C为随机事件，且 A与 B互不相容，A与 C互不相容，B与 C相互独立，<equation>P ( A )=P ( B )=P ( C )=\frac{1}{3}</equation>，则<equation>P ( B \cup C \mid A \cup B \cup C )=</equation>___
**解析: **由于<equation>A,B</equation>互不相容，<equation>A,C</equation>互不相容，<equation>B,C</equation>相互独立，故<equation>P (A B) = 0, \quad P (A C) = 0, \quad P (B C) = P (B) P (C) = \frac {1}{9}, \quad P (A B C) = 0.</equation>由条件概率公式，<equation>\begin{aligned} P (B \cup C \mid A \cup B \cup C) &= \frac {P [ (B \cup C) \cap (A \cup B \cup C) ]}{P (A \cup B \cup C)} = \frac {P (B \cup C)}{P (A \cup B \cup C)} \\ &= \frac {P (B) + P (C) - P (B C)}{P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C)} \\ &= \frac {\frac {1}{3} + \frac {1}{3} - \frac {1}{9}}{\frac {1}{3} + \frac {1}{3} + \frac {1}{3} - \frac {1}{9}} = \frac {5}{8}. \end{aligned}</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: D**
8. 设 A,B为随机事件，且<equation>0 < P ( B ) < 1</equation>，下列命题中为假命题的是（    )

A. 若<equation>P ( A \mid B )=P ( A )</equation>，则<equation>P ( A \mid \bar{B})=P ( A )</equation>B. 若<equation>P ( A \mid B )>P ( A )</equation>，则<equation>P ( \bar{A} \mid \bar{B})>P ( \bar{A} )</equation>C. 若<equation>P ( A \mid B )>P ( A \mid \bar{B})</equation>，则<equation>P ( A \mid B )>P ( A )</equation>D. 若<equation>P ( A \mid A \cup B )>P ( \bar{A} \mid A \cup B)</equation>，则<equation>P ( A )>P ( B )</equation>
答案: D
**解析: **解 考虑选项 D.<equation>P (A \mid A \cup B) = \frac {P (A \cap (A \cup B))}{P (A \cup B)} = \frac {P (A)}{P (A) + P (B) - P (A B)},</equation><equation>P (\bar {A} \mid A \cup B) = \frac {P (\bar {A} \cap (A \cup B))}{P (A \cup B)} = \frac {P (\bar {A} B)}{P (A) + P (B) - P (A B)} = \frac {P (B) - P (A B)}{P (A) + P (B) - P (A B)}.</equation>若<equation>P(A \mid A \cup B) > P(\overline{A} \mid A \cup B)</equation>，则<equation>P(A) > P(B) - P(AB)</equation>. 但这并不能保证<equation>P(A) > P(B)</equation>.由此出发考虑选项D的反例.例如：<equation>A = B</equation>，则<equation>P(A \mid A \cup B) = 1 > 0 = P(\overline{A} \mid A \cup B)</equation>，但<equation>P(A) = P(B)</equation>.

因此，应选D.

下面说明选项A、B、C不正确.

选项A：由于<equation>P ( A )=P ( A \mid B )=\frac{P ( A B )}{P ( B )}</equation>，故<equation>P ( A B )=P ( A ) P ( B )</equation>，从而A，B独立.由A，B独立可得A，<equation>\overline{B}</equation>独立，故<equation>P ( A \mid \overline{B})=P ( A ).</equation>选项A成立.

选项B：若<equation>P ( A \mid B ) > P ( A )</equation>，即<equation>\frac{P ( A B )}{P ( B )} > P ( A )</equation>，则<equation>P ( A B ) > P ( A ) P ( B ).</equation><equation>\begin{aligned} P (\bar {A} \mid \bar {B}) &= \frac {P (\bar {A} \bar {B})}{P (\bar {B})} = \frac {1 - P (A \cup B)}{1 - P (B)} = \frac {1 - P (A) - P (B) + P (A B)}{1 - P (B)} \\ > \frac {1 - P (A) - P (B) + P (A) P (B)}{1 - P (B)} &= 1 - P (A) = P (\bar {A}). \end{aligned}</equation>选项B成立.

选项C：若<equation>P ( A \mid B ) > P ( A \mid \bar{B} )</equation>，即<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A B )}{P (\bar{B})}</equation>，则<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A ) - P ( A B )}{1 - P ( B )}.</equation>由此可得<equation>P ( A B ) - P ( B ) P ( A B ) > P ( A ) P ( B ) - P ( B ) P ( A B )</equation>即<equation>P ( A B ) > P ( A ) P ( B ).</equation>于是，<equation>P ( A ) < \frac { P ( A B ) } { P ( B ) } = P ( A \mid B ) .</equation>选项C成立.

---

**2020年第7题 | 选择题 | 4分 | 答案: D**
7. 设 A,B,C为三个随机事件，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{4}, P ( A B )=0, P ( A C )=P ( B C )=\frac{1}{1 2}</equation>，则 A,B,C中恰有一个事件发生的概率为（    ）

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{1 2}</equation>
答案: D
**解析: **<equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ &= \frac {1}{4} + \frac {1}{4} + \frac {1}{4} - 0 - \frac {1}{1 2} - \frac {1}{1 2} + 0 = \frac {7}{1 2}. \end{aligned}</equation><equation>\begin{aligned} P (A B \cup B C \cup A C) &= P (A B) + P (B C) + P (A C) - P (A B C) - P (A B C) + P (A B C) \\ &= 0 + \frac {1}{1 2} + \frac {1}{1 2} + 0 = \frac {1}{6}. \end{aligned}</equation>从而，<equation>p=\frac{7}{12}-\frac{1}{6}=\frac{5}{12}.</equation>因此，应选D.

（法二）A,B,C中恰有一个事件发生的概率为<equation>p=P(A\overline{B}\overline{C})+P(\overline{A}B\overline{C})+P(\overline{A}\overline{B}C).</equation><equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) - P \left(A \bar {B} C\right) = P (A) - P (A B) - \left[ P (A C) - P (A C B) \right],</equation><equation>P (\bar {A} B \bar {C}) = P (\bar {A} B) - P (\bar {A} B C) = P (B) - P (A B) - [ P (B C) - P (B C A) ],</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) - P (\bar {B} C A) = P (C) - P (C B) - [ P (C A) - P (C A B) ].</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>因此，<equation>p = P (A) + P (B) + P (C) - 2 \left[ P (A B) + P (B C) + P (A C) \right] = \frac {3}{4} - 4 \times \frac {1}{1 2} = \frac {5}{1 2}.</equation>应选 D.

解（法一）设 A,B,C中恰有一个事件发生的概率为 p. P（A U B U C）为至少发生一个事件的概率.“至少发生一个”可拆分为“恰好发生一个”，“至少发生两个”这样两个互不相容事件.于是，<equation>P (A \cup B \cup C) = p + P (A B \cup B C \cup A C).</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>由三个事件的加法公式可得

---

**2019年第7题 | 选择题 | 4分 | 答案: C**
7. 设 A,B为随机事件，则<equation>P ( A )=P ( B )</equation>的充分必要条件是（    ）

A.<equation>P ( A \cup B )=P ( A )+P ( B )</equation>B.<equation>P ( A B )=P ( A ) P ( B )</equation>C.<equation>P ( A \bar{B} )=P ( B \bar{A} )</equation>D.<equation>P ( A B )=P ( \bar{A} \bar{B} )</equation>
答案: C
**解析: **解 由于<equation>A\overline{B}=A-A\cap B, B\overline{A}=B-B\cap A</equation>，故<equation>P(A\overline{B})=P(A)-P(AB), P(B\overline{A})= P(B)-P(AB).</equation>因此，<equation>P ( A ) = P ( B )</equation>等价于<equation>P ( A \bar{B} ) = P ( B \bar{A} )</equation>应选C.

下面说明选项A、B、D不正确.

取<equation>A = B</equation>，且<equation>P(A) = P(B) = \frac{1}{3}</equation>.

选项 A：<equation>P ( A \cup B )=P ( A )=\frac{1}{3}, P ( A )+P ( B )=\frac{2}{3}.</equation>选项A不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项B：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( A ) P ( B )=\frac{1}{9}.</equation>选项B不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项D：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( \overline{{A}} \ \overline{{B}} )=P ( \overline{{A}} )=\frac{2}{3}.</equation>选项D不是<equation>P ( A )=P ( B )</equation>的必要条件.

---

**2018年第14题 | 填空题 | 4分**
14. 设随机事件 A与B相互独立，A与C相互独立，<equation>B C=\varnothing</equation>. 若<equation>P(A)=P(B)=\frac{1}{2}, P(AC\mid AB\cup C)=\frac{1}{4}</equation>，则 P(C)=
**解析: **解 由于事件 A与B相互独立，故<equation>P ( A B )=P ( A ) P ( B ).</equation>由于事件 A与C相互独立，故<equation>P ( A C )=P ( A ) P ( C ).</equation>根据事件运算的分配律，<equation>P ( A C \cap( A B \cup C) )=P((A C \cap A B)\cup( A C \cap C))\overset{B C=\varnothing}{=}P( A C ).</equation>根据条件概率的公式，<equation>\begin{aligned} P (A C \mid A B \cup C) &= \frac {P (A C \cap (A B \cup C))}{P (A B \cup C)} = \frac {P (A C)}{P (A B \cup C)} = \frac {P (A) P (C)}{P (A B) + P (C) - P (A B C)} \\ &= \frac {P (A) P (C)}{P (A) P (B) + P (C) - 0} = \frac {1}{4}. \end{aligned}</equation>代入<equation>P ( A )=P ( B )=\frac{1}{2}</equation>，可得<equation>\frac{\frac{1}{2} P ( C )}{\frac{1}{4}+P ( C )}=\frac{1}{4}.</equation>解得<equation>P ( C )=\frac{1}{4}.</equation>

---

**2017年第7题 | 选择题 | 4分 | 答案: A**
7. 设 A,B为随机事件.若<equation>0 < P ( A ) < 1, 0 < P ( B ) < 1</equation>，则<equation>P ( A \mid B ) > P ( A \mid \bar{B} )</equation>的充分必要条件是（    )

A.<equation>P ( B \mid A ) > P ( B \mid \bar{A} )</equation>B.<equation>P ( B \mid A ) < P ( B \mid \bar{A} )</equation>C.<equation>P ( \bar{B} \mid A ) > P ( B \mid \bar{A} )</equation>D.<equation>P ( \bar{B} \mid A ) < P ( B \mid \bar{A} )</equation>
答案: A
**解析: **解 （法一）由题设知，<equation>P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow \frac {P (A B)}{P (B)} > \frac {P (A \bar {B})}{P (\bar {B})} \Leftrightarrow \frac {P (A B)}{P (A B) + P (\bar {A} B)} > \frac {P (A \bar {B})}{P (A \bar {B}) + P (\bar {A} \bar {B})}.</equation>记<equation>P ( A B ) = a,P(\overline{A} B)=b,P(A\overline{B})=c,P(\overline{A}\overline{B})=d</equation>，则<equation>\frac{P(A B)}{P(A B)+P(\overline{A} B)} >\frac{P(A\overline{B})}{P(A\overline{B})+P(\overline{A}\overline{B})},</equation>即<equation>\frac{a}{a+b} >\frac{c}{c+d},</equation>由于 0 < P(A) < 1,0 < P(B) < 1，故 a+b=P(B),c+d=P<equation>\overline{{B}}</equation>, a+c=P(A),b+d=P<equation>\overline{{A}}</equation>均大于0.于是，<equation>\frac {a}{a + b} > \frac {c}{c + d} \Leftrightarrow a (c + d) > c (a + b) \Leftrightarrow a d > b c.</equation>ad > bc等价于<equation>a b + a d > a b + b c, \quad \text {即} \frac {a}{a + c} > \frac {b}{b + d}, \quad \text {也 即} P (B \mid A) > P (B \mid \bar {A}).</equation>因此，应选A.

（法二）由题设知，<equation>\begin{array}{l} P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow \frac {P (A B)}{P (B)} > \frac {P (A \bar {B})}{P (\bar {B})} = \frac {P (A) - P (A B)}{1 - P (B)} \\ \Leftrightarrow P (A B) [ 1 - P (B) ] > [ P (A) - P (A B) ] P (B) \\ \end{array}</equation><equation>\Leftrightarrow P (A B) > P (A) P (B).</equation>调换 A,B的位置，同上可得<equation>P (B \mid A) > P (B \mid \bar {A}) \Leftrightarrow P (B A) > P (B) P (A).</equation>又<equation>P ( A B ) = P ( B A )</equation>，故<equation>P (A \mid B) > P (A \mid \bar {B}) \Leftrightarrow P (B \mid A) > P (B \mid \bar {A}).</equation>因此，应选A.

---

**2015年第7题 | 选择题 | 4分 | 答案: C**
7. 若 A,B为任意两个随机事件，则（    ）

A.<equation>P ( A B ) \leqslant P ( A ) P ( B )</equation>B.<equation>P ( A B ) \geqslant P ( A ) P ( B )</equation>C.<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>D.<equation>P ( A B ) \geqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>
答案: C
**解析: **解 由于 A<equation>\cap B \subseteq A</equation>，A<equation>\cap B \subseteq B</equation>，故<equation>P (A B) \leqslant P (A), \quad P (A B) \leqslant P (B).</equation>因此，<equation>2 P ( A B ) \leqslant P ( A )+P ( B )</equation>，即<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>应选C.

下面我们说明选项A、B、D不正确.

若 B<equation>\subseteq</equation>A,0 < P(A) < 1,0 < P(B) < 1<equation>，则 P(AB)=P(A</equation>\cap<equation>B）=P(B）>P(A)P(B).选项A不正确.

若 P(A) > 0，P(B) > 0且 A</equation>\cap<equation>B=</equation>\varnothing<equation>，则 P(AB) = P(A</equation>\cap<equation>B) = 0 < P(A)P(B)，P(AB) <</equation>\frac{P(A)+P(B)}{2} $ .选项B和选项D不正确.

---

**2014年第7题 | 选择题 | 4分 | 答案: B**
7. 设随机事件 A与 B相互独立，且<equation>P ( B )=0. 5, P ( A-B)=0. 3</equation>，则<equation>P ( B-A )=</equation>(    )

A. 0.1 B. 0.2 C. 0.3 D. 0.4
答案: B
**解析: **解（法一）由 A与B相互独立知，<equation>P ( A B ) = P ( A ) P ( B ).</equation>，于是，<equation>P (A - B) = P (A) - P (A B) = P (A) - P (A) P (B) = P (A) [ 1 - P (B) ] = 0. 5 P (A).</equation>从而<equation>P ( A ) = 2 P ( A - B ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P (B) - P (A B) = P (B) - P (A) P (B) = 0. 5 - 0. 6 \times 0. 5 = 0. 2.</equation>应选B.

（法二）由<equation>A</equation>与<equation>B</equation>相互独立知，<equation>A, B</equation>也相互独立.于是，<equation>0. 3 = P (A - B) = P (A \cap \bar {B}) = P (A \bar {B}) = P (A) P (\bar {B}) = 0. 5 P (A).</equation>因此，<equation>P ( A ) = 0. 6</equation>进一步可得，<equation>P (B - A) = P \left(B \bar {A}\right) = P (B) P (\bar {A}) = 0. 5 \times (1 - 0. 6) = 0. 2.</equation>应选B.

---

**2012年第14题 | 填空题 | 4分**
14. 设 A,B,C是随机事件，A与C互不相容，<equation>P ( A B )=\frac{1} {2}, P ( C )=\frac{1} {3}</equation>，则<equation>P ( A B \mid \bar{C})=</equation>___
**解析: **解 由条件概率的定义可知，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{P (\bar{C})}=\frac{P ( A B \bar{C})}{1-P(C)}.</equation>又 A与C互不相容，即<equation>A \cap C=\varnothing</equation>，故<equation>A \cap B \subset A \subset \bar{C}</equation>，从而<equation>A \cap B \cap \bar{C}=A \cap B.</equation>因此<equation>P ( A B \mid \bar{C})=\frac{P ( A B)}{1-P(C)}=\frac{\frac{1}{2}}{\frac{2}{3}}=\frac{3}{4}.</equation>

---


### 多维随机变量及其分布


#### 边缘分布和条件分布

**2025年第22题 | 解答题 | 12分**
22. 投保人的损失事件发生时，保险公司的赔付额 Y与投保人的损失额 X的关系为<equation>Y=\left\{\begin{array}{ll}0,&X\leqslant 100\\ X-100,&X>100\end{array} \right.</equation>. 设定损事件发生时，投保人的损失额 X的概率密度为<equation>f(x)=\left\{\begin{array}{ll}\frac{2\times 100^{2}}{(100+x)^{3}},&x>0\\ 0,&x\leqslant 0\end{array} \right.</equation>I. 求<equation>P\{Y>0\}</equation>及 EY.

Ⅱ. 这种损失事件在一年内发生的次数记为 N，保险公司在一年内就这种损失事件产生的理赔次数记为 M，假设 N服从参数为8的泊松分布，在<equation>N=n</equation>（<equation>n\geqslant1</equation>）的条件下，M服从二项分布<equation>B(n,p)</equation>，其中<equation>p=P\{Y>0\}</equation>，求 M的概率分布.
**答案: **（I）<equation>P \{ Y > 0 \} = \frac{1}{4}, E ( Y ) = 5 0;</equation>（Ⅱ）M服从参数为2的泊松分布.
**解析: **解（I）根据 Y的定义，<equation>\begin{aligned} P \{Y > 0 \} &= P \{X > 1 0 0 \} = \int_ {1 0 0} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2}}{(1 0 0 + x) ^ {3}} \mathrm {d} x = - \frac {2 \times 1 0 0 ^ {2}}{2} (1 0 0 + x) ^ {- 2} \Bigg | _ {1 0 0} ^ {+ \infty} \\ &= - \frac {1 0 0 ^ {2}}{(1 0 0 + x) ^ {2}} \Bigg | _ {1 0 0} ^ {+ \infty} = \frac {1}{4}. \end{aligned}</equation>由于随机变量<equation>Y</equation>是随机变量<equation>X</equation>的函数，故根据数学期望的定义，<equation>\begin{aligned} E (Y) &= \int_ {- \infty} ^ {+ \infty} y f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) f (x) \mathrm {d} x = \int_ {1 0 0} ^ {+ \infty} \frac {2 \times 1 0 0 ^ {2} (x - 1 0 0)}{(1 0 0 + x) ^ {3}} \mathrm {d} x \\ &= - 1 0 0 ^ {2} \int_ {1 0 0} ^ {+ \infty} (x - 1 0 0) \mathrm {d} \left[ (1 0 0 + x) ^ {- 2} \right] = - 1 0 0 ^ {2} \left[ \frac {x - 1 0 0}{(1 0 0 + x) ^ {2}} \right| _ {1 0 0} ^ {+ \infty} - \int_ {1 0 0} ^ {+ \infty} \frac {\mathrm {d} x}{(1 0 0 + x) ^ {2}} ] \\ &= \frac {- 1 0 0 ^ {2}}{1 0 0 + x} \Big | _ {1 0 0} ^ {+ \infty} = 0 - \left(- \frac {1 0 0 ^ {2}}{2 0 0}\right) = 5 0. \end{aligned}</equation>（Ⅱ）由于<equation>N</equation>服从参数为8的泊松分布，故<equation>P\{N = n\} = \frac{8^{n}\mathrm{e}^{-8}}{n!}</equation>，进一步可得<equation>P\{N = 0\} = \mathrm{e}^{-8}</equation>由于当<equation>N = 0</equation>时，<equation>M</equation>必然等于0，故<equation>P\{M = 0\mid N = 0\} = 1</equation>，从而<equation>P \{M = 0, N = 0 \} = P \{M = 0 \mid N = 0 \} P \{N = 0 \} = 1 \cdot P \{N = 0 \} = \mathrm {e} ^ {- 8}.</equation>由 M的定义可知，当<equation>M=k</equation>时，<equation>N=n\geqslant k</equation>由在<equation>N=n(n\geqslant 1)</equation>的条件下，M服从二项分布<equation>B(n,p)</equation>可得，<equation>P \left\{M = k \mid N = n \right\} = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k}, \quad k = 0, 1, \dots , n, n = 1, 2, \dots .</equation>由条件概率公式以及 p=<equation>\frac{1}{4}</equation>可得<equation>\begin{aligned} P \{M = k, N = n \} &= P \{M = k \mid N = n \} P \{N = n \} = C _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} \\ &= \frac {n !}{k ! (n - k) !} \cdot \left(\frac {1}{4}\right) ^ {k} \cdot \left(\frac {3}{4}\right) ^ {n - k} \cdot \frac {8 ^ {n} \mathrm {e} ^ {- 8}}{n !} = \frac {3 ^ {n - k} 2 ^ {n} \mathrm {e} ^ {- 8}}{k ! (n - k) !} \\ &= \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !}. \end{aligned}</equation>由此可得，当<equation>k\neq 0</equation>时，<equation>\begin{aligned} P \{M = k \} &= \sum_ {n = k} ^ {\infty} P \{M = k, N = n \} = \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} 2 ^ {k} \mathrm {e} ^ {- 8}}{k ! (n - k) !} = \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = k} ^ {\infty} \frac {6 ^ {n - k} \mathrm {e} ^ {- 6}}{(n - k) !} \\ &= \frac {2 ^ {k} \mathrm {e} ^ {- 2}}{k !} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation><equation>\begin{aligned} P \{M = 0 \} &= \sum_ {n = 0} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} P \{M = 0, N = n \} = \mathrm {e} ^ {- 8} + \sum_ {n = 1} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !} \cdot \mathrm {e} ^ {- 2} \\ &= \mathrm {e} ^ {- 2} \sum_ {n = 0} ^ {\infty} \frac {6 ^ {n} \mathrm {e} ^ {- 6}}{n !}. \end{aligned}</equation>由泊松分布的定义可知，服从参数为6的泊松分布的随机变量Z的分布律为<equation>P\{Z=n\}=\frac{6^{n}\mathrm{e}^{-6}}{n!}.</equation>由分布律的性质可得，<equation>\sum_{n=0}^{\infty}\frac{6^{n}\mathrm{e}^{-6}}{n!}=1.</equation>于是，<equation>P\{M=k\}=\frac{2^{k}\mathrm{e}^{-2}}{k!}, k=0,1,2,\dots.</equation>因此，M服从参数为2的泊松分布.

---

**2010年第22题 | 解答题 | 11分**
22. (本题满分11分)

设二维随机变量<equation>(X, Y)</equation>的概率密度为<equation>f (x, y) = A \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}}, (- \infty < x < + \infty , - \infty < y < + \infty).</equation>求常数<equation>A</equation>及条件概率密度<equation>f_{Y|X}(y|x)</equation>.
**答案: **<equation>(2 2) A = \frac {1}{\pi}, f _ {Y \mid X} (y \mid x) = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- (x - y) ^ {2}}, y \in (- \infty , + \infty)</equation>
**解析: **解 由概率密度的性质可知，<equation>\int_{- \infty}^{+ \infty}\int_{- \infty}^{+ \infty}f(x,y)\mathrm{d}x\mathrm{d}y=1.</equation>由于<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x \mathrm {d} y &= \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} A \mathrm {e} ^ {- x ^ {2} - (y - x) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} y = A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- (y - x) ^ {2}} \mathrm {d} (y - x) \\ &= A \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- x ^ {2}} \mathrm {d} x \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \frac {\int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \sqrt {\pi}}{A \pi}, \end{aligned}</equation>故<equation>A\pi = 1</equation>，从而<equation>A = \frac{1}{\pi}.</equation>由条件概率密度的定义可知，<equation>f_{Y \mid X}(y \mid x) = \frac{f(x,y)}{f_X(x)}.</equation>又由于<equation>f_{X}(x)=\int_{-\infty}^{+\infty} f(x,y)\mathrm{d} y=\frac{1}{\pi}\int_{-\infty}^{+\infty}\mathrm{e}^{-2x^{2}+2xy-y^{2}}\mathrm{d} y=\frac{1}{\pi}\mathrm{e}^{-x^{2}}\int_{-\infty}^{+\infty}\mathrm{e}^{-(y-x)^{2}}\mathrm{d} y=\frac{1}{\pi}\mathrm{e}^{-x^{2}}\cdot \sqrt{\pi}=\frac{1}{\sqrt{\pi}}\mathrm{e}^{-x^{2}},</equation>故对任意给定的<equation>x\in(-\infty,+\infty)</equation>，在 X=x的条件下，Y的条件概率密度为<equation>f _ {Y \mid X} (y \mid x) = \frac {f (x , y)}{f _ {X} (x)} = \frac {\frac {1}{\pi} \mathrm {e} ^ {- 2 x ^ {2} + 2 x y - y ^ {2}}}{\frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2}}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- x ^ {2} + 2 x y - y ^ {2}} = \frac {1}{\sqrt {\pi}} \mathrm {e} ^ {- (x - y) ^ {2}}, y \in (- \infty , + \infty).</equation>

---

**2009年第22题 | 解答题 | 11分**

袋中有1个红球、2个黑球与3个白球.现有放回地从袋中取两次，每次取一个球.以 X，Y，Z分别表示两次取球所取得的红球、黑球与白球的个数.

I. 求<equation>P\{X=1\mid Z=0\}</equation>；

II. 求二维随机变量（X，Y）的概率分布.
**答案: **(22) ( I )<equation>P \{ X = 1 \mid Z = 0 \} = \frac{4}{9};</equation>（Ⅱ）二维随机变量<equation>(X, Y)</equation>的概率分布为

<table border="1"><tr><td rowspan="2">Y
X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>
**解析: **解（I）（法一）由条件概率的定义知，<equation>P \{X = 1 \mid Z = 0 \} = \frac {P \{X = 1 , Z = 0 \}}{P \{Z = 0 \}} = \frac {P \{X = 1 , Y = 1 \}}{P \{Z = 0 \}} = \frac {\mathrm {C} _ {2} ^ {1} \cdot \frac {1}{6} \cdot \frac {2}{6}}{\frac {3}{6} \cdot \frac {3}{6}} = \frac {4}{9}.</equation>（法二）<equation>P \{ X=1 \mid Z=0 \}</equation>是指在 Z=0即两次所取的球中没有白球的条件下，两次取球为一黑一红的概率，即为在1个红球、2个黑球中有放回地取得一黑一红的概率，于是<equation>P \left\{X = 1 \mid Z = 0 \right\} = \mathrm {C} _ {2} ^ {1} \cdot \frac {1}{3} \cdot \frac {2}{3} = \frac {4}{9}.</equation>（Ⅱ）由于<equation>X, Y</equation>所有可能的取值均为0,1,2，故二维随机变量<equation>(X, Y)</equation>的概率分布为，<equation>P \{X = 0, Y = 0 \} = P \{Z = 2 \} = \frac {3}{6} \cdot \frac {3}{6} = \frac {1}{4},</equation><equation>P \left\{X = 0, Y = 1 \right\} = P \left\{Y = 1, Z = 1 \right\} = C _ {2} ^ {1} \cdot \frac {2}{6} \cdot \frac {3}{6} = \frac {1}{3},</equation><equation>P \{X = 0, Y = 2 \} = \frac {2}{6} \cdot \frac {2}{6} = \frac {1}{9},</equation><equation>P \{X = 1, Y = 0 \} = P \{X = 1, Z = 1 \} = C _ {2} ^ {1} \cdot \frac {1}{6} \cdot \frac {3}{6} = \frac {1}{6},</equation><equation>P \{X = 1, Y = 1 \} = \mathrm {C} _ {2} ^ {1} \cdot \frac {1}{6} \cdot \frac {2}{6} = \frac {1}{9}, \quad P \{X = 1, Y = 2 \} = 0,</equation><equation>P \{X = 2, Y = 0 \} = \frac {1}{6} \cdot \frac {1}{6} = \frac {1}{3 6}, \quad P \{X = 2, Y = 1 \} = 0, \quad P \{X = 2, Y = 2 \} = 0.</equation>从而 X和 Y的联合分布律为

<table border="1"><tr><td rowspan="2">Y
X</td><td>0</td><td>1</td><td>2</td></tr><tr><td><equation>\frac{1}{4}</equation></td><td><equation>\frac{1}{6}</equation></td><td><equation>\frac{1}{36}</equation></td></tr><tr><td>1</td><td><equation>\frac{1}{3}</equation></td><td><equation>\frac{1}{9}</equation></td><td>0</td></tr><tr><td>2</td><td><equation>\frac{1}{9}</equation></td><td>0</td><td>0</td></tr></table>

---


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
