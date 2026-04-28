#### 数学期望与方差

**2024年第8题 | 选择题 | 5分 | 答案: B**

8. 设随机变量 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}6 x(1-x),&0<x<1,\\0,&\text{其他},\end{array}\right.</equation>则 X的三阶中心矩<equation>E \left\{ \left[ X-E ( X ) \right]^{3} \right\}=(\quad)</equation>A.<equation>-\frac{1}{3 2}</equation>B.0 C.<equation>\frac{1}{1 6}</equation>D.<equation>\frac{1}{2}</equation>

答案: B

**解析:**解 根据数学期望的定义，<equation>\begin{aligned} E (X) &= \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {1} x \cdot 6 x (1 - x) \mathrm {d} x = \int_ {0} ^ {1} \left(6 x ^ {2} - 6 x ^ {3}\right) \mathrm {d} x = \left. \left(2 x ^ {3} - \frac {3 x ^ {4}}{2}\right) \right| _ {0} ^ {1} \\ &= 2 - \frac {3}{2} = \frac {1}{2}. \end{aligned}</equation>进一步可得，<equation>\begin{array}{l} E \left\{\left[ X - E (X) \right] ^ {3} \right\} = \int_ {- \infty} ^ {+ \infty} \left(x - \frac {1}{2}\right) ^ {3} f (x) \mathrm {d} x = \int_ {0} ^ {1} \left(x - \frac {1}{2}\right) ^ {3} \cdot 6 x (1 - x) \mathrm {d} x \\ \underline {{=}} t = x - \frac {1}{2} 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \cdot \left(t + \frac {1}{2}\right) \left(\frac {1}{2} - t\right) \mathrm {d} t = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} t ^ {3} \left(\frac {1}{4} - t ^ {2}\right) \mathrm {d} t \\ = 6 \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} \left(\frac {1}{4} t ^ {3} - t ^ {5}\right) \mathrm {d} t \stackrel {\text {对称性}} {=} 0. \\ \end{array}</equation>因此，应选B.

---


### 随机变量及其分布

**2025年第9题 | 选择题 | 5分 | 答案: C**

9. 设<equation>X_{1}, X_{2}, \dots , X_{2 0}</equation>是来自总体B(1,0.1)的简单随机样本，令<equation>T=\sum_{i=1}^{2 0} X_{i}</equation>利用泊松分布近似表示二项分布的方法可得<equation>P\{ T\leqslant 1\}\approx</equation>(    )

A.<equation>\frac{1} {\mathrm{e}^{2}}</equation>B.<equation>\frac{2} {\mathrm{e}^{2}}</equation>C.<equation>\frac{3} {\mathrm{e}^{2}}</equation>D.<equation>\frac{4} {\mathrm{e}^{2}}</equation>

答案: C

**解析:**解 由<equation>X_{i}(i = 1,2,\dots ,20)\sim B(1,0.1)</equation>可知，<equation>X_{i}</equation>可看作一次随机试验的结果，试验成功的概率为0.1，<equation>T = \sum_{i = 1}^{20}X_{i}</equation>可看作20次独立重复试验中试验成功的次数，服从<equation>B(20,0.1)</equation>.根据泊松定理，<equation>n = 20,p_{n} = 0.1,\lambda = 2,T</equation>近似服从参数为2的泊松分布.

因此，<equation>P \{T \leqslant 1 \} = P \{T = 0 \} + P \{T = 1 \} \approx \frac {2 ^ {0} \cdot \mathrm {e} ^ {- 2}}{1} + \frac {2 ^ {1} \cdot \mathrm {e} ^ {- 2}}{1} = \frac {3}{\mathrm {e} ^ {2}}.</equation>应选C.

---

**2025年第10题 | 选择题 | 5分 | 答案: C**

10. 设总体 X的分布函数为 F(x),<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自总体 X的简单随机样本，样本的经验分布函数为<equation>F_{n}(x)</equation>对于给定的 x(0 < F(x) < 1), D(F_{n}(x))=（    )

A. F(x)[1-F(x)] B.<equation>[F(x)]^{2}</equation>C.<equation>\frac{1}{n} F(x)[1-F(x)]</equation>D.<equation>\frac{1}{n}[F(x)]^{2}</equation>

答案: C

**解析:**解记<equation>X_{i}</equation>的分布函数为<equation>F_{X_{i}}(x).</equation>由于<equation>X_{i} ( i=1,2,\dots,n)</equation>与X同分布，故<equation>F_{X_{i}}(x)=F(x).</equation>令<equation>Y_{i}=\left\{\begin{array}{ll}1,&X_{i}\leqslant x,\\ 0,&X_{i}>x,\end{array}\right. i=1,2,\dots,n</equation>则<equation>Y_{i}</equation>的分布律满足<equation>P \left\{Y _ {i} = 1 \right\} = P \left\{X _ {i} \leqslant x \right\} = F _ {X _ {i}} (x) = F (x),</equation><equation>P \left\{Y _ {i} = 0 \right\} = P \left\{X _ {i} > x \right\} = 1 - F _ {X _ {i}} (x) = 1 - F (x).</equation>由此可得<equation>Y_{i}\sim B(1,F(x))</equation>.于是，<equation>E \left(Y _ {i}\right) = F (x), \quad D \left(Y _ {i}\right) = F (x) [ 1 - F (x) ].</equation>注意到<equation>F_{n}(x)=\frac{1}{n}\sum_{i=1}^{n} Y_{i}</equation>，且<equation>Y_{1},Y_{2},\dots ,Y_{n}</equation>独立同分布，故<equation>D \left[ F _ {n} (x) \right] = D \left(\frac {1}{n} \sum_ {i = 1} ^ {n} Y _ {i}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left(Y _ {i}\right) = \frac {1}{n} D \left(Y _ {i}\right) = \frac {1}{n} F (x) [ 1 - F (x) ].</equation>因此，应选C.

---

**2024年第9题 | 选择题 | 5分 | 答案: B**

9. 设随机变量 X, Y相互独立，且<equation>X\sim N(0,2),Y\sim N(-1,1)</equation>，设<equation>p_{1}=P\{2X>Y\}, p_{2}=P\{X-2Y>1\}</equation>，则（    )

A.<equation>p_{1}>p_{2}>\frac{1}{2}</equation>B.<equation>p_{2}>p_{1}>\frac{1}{2}</equation>C.<equation>p_{1}<p_{2}<\frac{1}{2}</equation>D.<equation>p_{2}<p_{1}<\frac{1}{2}</equation>

答案: B

**解析:**解 由于<equation>X\sim N(0,2),Y\sim N(-1,1)</equation>，故<equation>E(X) = 0,D(X) = 2,E(Y) = -1,D(Y) = 1</equation>，从而<equation>E (Y - 2 X) = E (Y) - 2 E (X) = - 1 - 0 = - 1,</equation><equation>D (Y - 2 X) = D (Y) + 4 D (X) = 1 + 4 \times 2 = 9,</equation><equation>E (2 Y - X) = 2 E (Y) - E (X) = 2 \times (- 1) - 0 = - 2,</equation><equation>D (2 Y - X) = 4 D (Y) + D (X) = 4 \times 1 + 2 = 6.</equation>于是，<equation>Y - 2 X\sim N(-1,9), 2 Y - X\sim N(-2,6).</equation>将它们标准化可得<equation>\frac{Y - 2 X + 1}{3}\sim N(0,1),</equation><equation>\frac{2 Y - X + 2}{\sqrt{6}}\sim N(0,1).</equation>由此可得，<equation>\begin{array}{l} p _ {1} = P | 2 X - Y > 0 | = P | Y - 2 X < 0 | = P \left\{\frac {Y - 2 X + 1}{3} < \frac {1}{3} \right\} \\ = P \left\{\frac {Y - 2 X + 1}{3} \leqslant \frac {1}{3} \right\} = \Phi \left(\frac {1}{3}\right), \\ \end{array}</equation><equation>\begin{array}{l} p _ {2} = P \left| X - 2 Y > 1 \right| = P \left| 2 Y - X < - 1 \right| = P \left\{\frac {2 Y - X + 2}{\sqrt {6}} < \frac {1}{\sqrt {6}} \right\} \\ = P \left\{\frac {2 Y - X + 2}{\sqrt {6}} \leqslant \frac {1}{\sqrt {6}} \right\} = \Phi \left(\frac {1}{\sqrt {6}}\right), \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>是标准正态分布的分布函数.

由于<equation>\varPhi(x)</equation>单调增加，且<equation>0 < \frac{1}{3} < \frac{1}{\sqrt{6}}</equation>，故<equation>\frac{1}{2}=\varPhi(0)<\varPhi\left(\frac{1}{3}\right)<\varPhi\left(\frac{1}{\sqrt{6}}\right).</equation>因此，<equation>p_{2}>p_{1}> \frac{1}{2}</equation>应选B.

---

**2024年第16题 | 填空题 | 5分**

16. 设随机试验每次成功的概率为 p，现进行3次独立重复试验，在至少成功1次的条件下，3次试验全部成功的概率为<equation>\frac{4}{1 3}</equation>，则 p=___

**答案:**# p=2/3

**解析:**解设 X为3次独立重复试验中试验成功的次数，则<equation>X\sim B(3,p).</equation>在至少成功1次的条件下， 3次试验全部成功的概率为<equation>P\mid X=3\mid X\geqslant 1\mid =\frac{P\mid X=3,X\geqslant 1\mid}{P\mid X\geqslant 1\mid}=\frac{P\mid X=3\mid}{P\mid X\geqslant 1\mid}=\frac{\mathrm{C}_{3}^{3} p^{3}}{1-\mathrm{C}_{3}^{0}(1-p)^{3}}=\frac{4}{13}.</equation>于是，<equation>\frac{p^{3}}{1-(1-p)^{3}}=\frac{4}{13}.</equation>整理可得<equation>3 p^{3}+4 p^{2}-4 p=0</equation>即<equation>p(p+2)(3 p-2)=0.</equation>由于 p > 0，故 p =<equation>\frac{2}{3}.</equation>

---

**2019年第8题 | 选择题 | 4分 | 答案: A**

8. 随机变量 X与 Y相互独立，且都服从正态分布<equation>N(\mu ,\sigma^{2})</equation>，则<equation>P\{|X-Y|<1\}</equation>(    )

A. 与<equation>\mu</equation>无关，而与<equation>\sigma^{2}</equation>有关 B. 与<equation>\mu</equation>有关，而与<equation>\sigma^{2}</equation>无关

C. 与<equation>\mu,\sigma^{2}</equation>都有关 D. 与<equation>\mu,\sigma^{2}</equation>都无关

答案: A

**解析:**解 由于 X，Y相互独立且都服从正态分布<equation>N(\mu ,\sigma^{2})</equation>，故<equation>E(X-Y)=0,D(X-Y)=2\sigma^{2},</equation><equation>X-Y\sim N(0,2\sigma^{2}).</equation>将 X-Y标准化，可得<equation>\frac{X-Y}{\sqrt{2}\sigma}\sim N(0,1).</equation>，于是，<equation>\begin{array}{l} P \left\{\mid X - Y \mid < 1 \right\} = P \left\{- 1 < X - Y < 1 \right\} = P \left\{\frac {- 1}{\sqrt {2} \sigma} < \frac {X - Y}{\sqrt {2} \sigma} < \frac {1}{\sqrt {2} \sigma} \right\} \\ = \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - \Phi \left(\frac {- 1}{\sqrt {2} \sigma}\right) = 2 \Phi \left(\frac {1}{\sqrt {2} \sigma}\right) - 1. \\ \end{array}</equation>因此，<equation>P \left\{ \mid X - Y \mid < 1 \right\}</equation>仅与<equation>\sigma^{2}</equation>有关.应选A.

---

**2018年第7题 | 选择题 | 4分 | 答案: A**

7. 设随机变量 X的概率密度 f(x)满足<equation>f(1+x)=f(1-x)</equation>，且<equation>\int_{0}^{2} f(x)\mathrm{d}x=0.6</equation>，则<equation>P\{ X<0\}=</equation>(    )

A. 0.2 B. 0.3 C. 0.4 D. 0.5

答案: A

**解析:**解 由于<equation>f ( 1+x)=f ( 1-x)</equation>，故 f(x)的图像关于 x=1对称.于是，<equation>P\{ X < 0 \}=P\{ X > 2 \}.</equation>又因为<equation>P\{ 0\leqslant X\leqslant 2\}=\int_{0}^{2} f ( x ) \mathrm{d} x=0. 6</equation>，且<equation>P\{ X < 0 \}+P\{ 0\leqslant X\leqslant 2\}+P\{ X > 2\}=1,</equation>以<equation>P\{ X < 0 \}=\frac{1-P\{ 0\leqslant X\leqslant 2\}}{2}=\frac{1-0. 6}{2}=0. 2.</equation>因此，应选A.

---

**2013年第7题 | 选择题 | 4分 | 答案: A**

7. 设<equation>X_{1}, X_{2}, X_{3}</equation>是随机变量，且<equation>X_{1}\sim N(0,1), X_{2}\sim N(0,2^{2}), X_{3}\sim N(5,3^{2}), p_{i}=P\{-2\leqslant X_{i}\leqslant 2\} (i=1,2,3)</equation>，则（    )

A.<equation>p_{1}>p_{2}>p_{3}</equation>B.<equation>p_{2}>p_{1}>p_{3}</equation>C.<equation>p_{3}>p_{1}>p_{2}</equation>D.<equation>p_{1}>p_{3}>p_{2}</equation>

答案: A

**解析:**解 由<equation>X_{2}\sim N(0,2^{2}),X_{3}\sim N(5,3^{2})</equation>知，<equation>\frac{X_2}{2}\sim N(0,1),\frac{X_3 - 5}{3}\sim N(0,1)</equation>.于是，<equation>p_{1} = P\{-2\leqslant X_{1}\leqslant 2\} = \Phi (2) - \Phi (-2) = 1 - \Phi (-2) - \Phi (-2) = 1 - 2\Phi (-2),</equation><equation>p_{2} = P\{-2\leqslant X_{2}\leqslant 2\} = P\left\{-1\leqslant \frac{X_{2}}{2}\leqslant 1\right\} = \Phi (1) - \Phi (-1) = 1 - 2\Phi (-1),</equation><equation>p_{3} = P\{-2\leqslant X_{3}\leqslant 2\} = P\left\{-\frac{7}{3}\leqslant \frac{X_{3} - 5}{3}\leqslant -1\right\} = \Phi (-1) - \Phi \left(-\frac{7}{3}\right).</equation>于<equation>\Phi (-1) > \Phi (-2)</equation>，故<equation>p_{1} > p_{2}</equation>.

设标准正态分布的概率密度为<equation>\varphi (x)</equation>，则<equation>\varphi (x)</equation>为偶函数，且在<equation>(-\infty ,0]</equation>上单调增加（如图所示）.又由于<equation>p_{2} = \int_{-1}^{1}\varphi (x)\mathrm{d}x,p_{3} = \int_{-\frac{7}{3}}^{-1}\varphi (x)\mathrm{d}x</equation>，而<equation>\varphi (x)</equation>在（-1,1）上的取值都大于<equation>\varphi (x)</equation>在<equation>\left(-\frac{7}{3},-1\right)</equation>上的取值，且积分区间的长度满足<equation>|1-(-1)|> \left| -1-\left(-\frac{7}{3}\right) \right|</equation>，故<equation>p_{2}>p_{3}.</equation>综上所述，<equation>p_{1}>p_{2}>p_{3}.</equation>应选A.

---

**2011年第7题 | 选择题 | 4分 | 答案: D**

7. 设<equation>F_{1}(x)</equation>与<equation>F_{2}(x)</equation>为两个分布函数，其相应的概率密度<equation>f_{1}(x)</equation>与<equation>f_{2}(x)</equation>是连续函数，则必为概率密度的是（    )

A.<equation>f_{1}(x)f_{2}(x)</equation>B.<equation>2f_{2}(x)F_{1}(x)</equation>C.<equation>f_{1}(x)F_{2}(x)</equation>D.<equation>f_{1}(x)F_{2}(x)+f_{2}(x)F_{1}(x)</equation>

答案: D

**解析:**分布函数和概率密度的性质知，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)\geqslant 0</equation>，且<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} \left[ f _ {1} (x) F _ {2} (x) + f _ {2} (x) F _ {1} (x) \right] \mathrm {d} x &= \int_ {- \infty} ^ {+ \infty} \left[ F _ {1} (x) F _ {2} (x) \right] ^ {\prime} \mathrm {d} x \\ &= F _ {1} (+ \infty) F _ {2} (+ \infty) - F _ {1} (- \infty) F _ {2} (- \infty) \\ &= 1 - 0 = 1. \end{aligned}</equation>因此，<equation>f_{1}(x)F_{2}(x) + f_{2}(x)F_{1}(x)</equation>为概率密度.应选D.

---

**2010年第7题 | 选择题 | 4分 | 答案: C**

7. 设随机变量 X的分布函数 F(x) =<equation>\left\{\begin{array}{l l}0,&x<0,\\ \frac{1}{2},&0\leqslant x<1,\\ 1-\mathrm{e}^{-x},&x\geqslant 1,\end{array} \right.</equation>则 P{X=1} =（    )

A. 0 B.<equation>\frac{1}{2}</equation>C.<equation>\frac{1}{2}-\mathrm{e}^{-1}</equation>D.<equation>1-\mathrm{e}^{-1}</equation>

答案: C

**解析:**解<equation>P \{ X = 1 \} = P \{ X \leqslant 1 \} - P \{ X < 1 \} = F ( 1 ) - F ( 1^{-} ) = 1 - \mathrm{e}^{-1} - \frac{1}{2} = \frac{1}{2} - \mathrm{e}^{-1}.</equation>应选C.

---

**2010年第8题 | 选择题 | 4分 | 答案: A**

8. 设<equation>f_{1}(x)</equation>为标准正态分布的概率密度，<equation>f_{2}(x)</equation>为<equation>[-1,3]</equation>上均匀分布的概率密度，若<equation>f (x) = \left\{ \begin{array}{l l} a f _ {1} (x), & x \leqslant 0, \\ b f _ {2} (x), & x > 0 \end{array} \right. (a > 0, b > 0)</equation>为概率密度，则 a,b应满足（    ）

A. 2a+3b=4 B. 3a+2b=4 C. a+b=1 D. a+b=2

答案: A

**解析:**解 由于标准正态分布的概率密度的图形关于 y轴对称，故<equation>\int_{0}^{+\infty} f_{1}(x)\mathrm{d}x=\int_{-\infty}^{0} f_{1}(x)\mathrm{d}x=\frac{1}{2}.</equation>又由题设知，<equation>f_{2}(x)=\left\{\begin{array}{ll}\frac{1}{4},&-1\leqslant x\leqslant 3,\\ 0,&\text{其他}.\end{array} \right.</equation>由于 f(x)为概率密度，故<equation>1=\int_{-\infty}^{+\infty} f(x)\mathrm{d}x=\int_{-\infty}^{0} a f_{1}(x)\mathrm{d}x+\int_{0}^{+\infty} b f_{2}(x)\mathrm{d}x=\frac{1}{2} a+\int_{0}^{3} \frac{b}{4}\mathrm{d}x=\frac{1}{2} a+\frac{3}{4} b,</equation>即<equation>\frac{1}{2} a+\frac{3}{4} b=1</equation>从而 2a+3b=4.应选A.

---


### 随机事件和概率

**2025年第16题 | 填空题 | 5分**

16. 设 A,B,C 为三个随机事件，且 A 与 B 相互独立，B 与 C 相互独立，A 与 C 互不相容，已知<equation>P ( A )=P ( C )=\frac{1}{4},</equation><equation>P ( B )=\frac{1}{2}</equation>，则在事件 A,B,C 至少有一个发生的条件下，A,B,C 中恰有一个发生的概率为___

**解析:**解 由 A与B相互独立，B与C相互独立可得<equation>P ( A B )=P ( A ) P ( B ) , P ( B C )=P ( B ) P ( C ).</equation>由 A与C互不相容可得<equation>A \cap C=\varnothing</equation>由此可得<equation>P ( A C)=0.</equation>所求概率为<equation>P ( A \overline{B} \overline{C} \cup \overline{A} \overline{B} \overline{C} \cup \overline{A} \overline{B} C \mid A \cup B \cup C).</equation>根据条件概率公式，<equation>P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C \mid A \cup B \cup C\right) = \frac {P \left[ \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right) \cap \left(A \cup B \cup C\right) \right]}{P \left(A \cup B \cup C\right)}.</equation>由于<equation>A\overline{B}\overline{C},\overline{A}B\overline{C},\overline{A}\overline{B}C</equation>均包含于<equation>A\cup B\cup C</equation>，故<equation>P \left[ \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right) \cap (A \cup B \cup C) \right] = P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right).</equation>又因为这三个事件互不相容，故<equation>P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C\right) = P \left(A \bar {B} \bar {C}\right) + P \left(\bar {A} B \bar {C}\right) + P \left(\bar {A} \bar {B} C\right).</equation>由<equation>A \cap C = \varnothing</equation>可得<equation>A \subseteq \overline{C}, C \subseteq \overline{A}</equation>，于是<equation>A\overline{B}\overline{C} = A\overline{B},\overline{A}\overline{B}C = \overline{B}C.</equation>进一步可得<equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) \stackrel {\mathrm {独立 性}} {=} P (A) P (\bar {B}) = \frac {1}{4} \cdot \frac {1}{2} = \frac {1}{8},</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) \stackrel {\text {独立 性}} {=} P (\bar {B}) P (C) = \frac {1}{2} \cdot \frac {1}{4} = \frac {1}{8}.</equation>此外，<equation>\begin{aligned} P (\bar {A} B \bar {C}) &= P [ B \cap (\overline {{A \cup C}}) ] = P (B) - P [ B \cap (A \cup C) ] = P (B) - P (A B \cup B C) \\ &= P (B) - P (A B) - P (B C) \xlongequal {\text {独立性}} P (B) - P (A) P (B) - P (B) P (C) \\ &= P (B) [ 1 - P (A) - P (C) ] = \frac {1}{2} \cdot \frac {1}{2} = \frac {1}{4}. \end{aligned}</equation><equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ \frac {P (A C) = 0}{P (A B C) = 0} P (A) + P (B) + P (C) - P (A) P (B) - P (B) P (C) \\ &= \frac {1}{4} + \frac {1}{2} + \frac {1}{4} - \frac {1}{4} \cdot \frac {1}{2} - \frac {1}{2} \cdot \frac {1}{4} = \frac {3}{4}. \end{aligned}</equation>结合（1）式，（2）式可得<equation>P \left(A \bar {B} \bar {C} \cup \bar {A} B \bar {C} \cup \bar {A} \bar {B} C \mid A \cup B \cup C\right) = \left(\frac {1}{8} + \frac {1}{4} + \frac {1}{8}\right) / \frac {3}{4} = \frac {2}{3}.</equation>

---

**2022年第16题 | 填空题 | 5分**

16. 设 A,B,C为随机事件，且 A与B互不相容，A与C互不相容，B与C相互独立，<equation>P ( A )=P ( B )=P ( C )=\frac{1}{3}</equation>，则<equation>P ( B \cup C \mid A \cup B \cup C )=</equation>___

**答案:**## 5 8.

**解析:**由于 A，B互不相容，A，C互不相容，B，C相互独立，故<equation>P (A B) = 0, \quad P (A C) = 0, \quad P (B C) = P (B) P (C) = \frac {1}{9}, \quad P (A B C) = 0.</equation>由条件概率公式，<equation>\begin{aligned} P (B \cup C \mid A \cup B \cup C) &= \frac {P [ (B \cup C) \cap (A \cup B \cup C) ]}{P (A \cup B \cup C)} = \frac {P (B \cup C)}{P (A \cup B \cup C)} \\ &= \frac {P (B) + P (C) - P (B C)}{P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C)} \\ &= \frac {\frac {1}{3} + \frac {1}{3} - \frac {1}{9}}{\frac {1}{3} + \frac {1}{3} + \frac {1}{3} - \frac {1}{9}} = \frac {5}{8}. \end{aligned}</equation>

---

**2021年第8题 | 选择题 | 5分 | 答案: D**

8. 设 A,B为随机事件，且<equation>0 < P ( B ) < 1</equation>，下列命题中为假命题的是（    )

A. 若<equation>P ( A \mid B )=P ( A )</equation>，则<equation>P ( A \mid \bar{B})=P ( A )</equation>B. 若<equation>P ( A \mid B )>P ( A )</equation>，则<equation>P ( \bar{A} \mid \bar{B})>P ( \bar{A} )</equation>C. 若<equation>P ( A \mid B )>P ( A \mid \bar{B})</equation>，则<equation>P ( A \mid B )>P ( A )</equation>D. 若<equation>P ( A \mid A \cup B )>P ( \bar{A} \mid A \cup B)</equation>，则<equation>P ( A )>P ( B )</equation>

答案: D

**解析:**解 考虑选项 D.<equation>P (A \mid A \cup B) = \frac {P (A \cap (A \cup B))}{P (A \cup B)} = \frac {P (A)}{P (A) + P (B) - P (A B)},</equation><equation>P (\bar {A} \mid A \cup B) = \frac {P (\bar {A} \cap (A \cup B))}{P (A \cup B)} = \frac {P (\bar {A} B)}{P (A) + P (B) - P (A B)} = \frac {P (B) - P (A B)}{P (A) + P (B) - P (A B)}.</equation>若<equation>P(A \mid A \cup B) > P(\overline{A} \mid A \cup B)</equation>，则<equation>P(A) > P(B) - P(AB)</equation>.但这并不能保证<equation>P(A) > P(B)</equation>.由此出发考虑选项D的反例.例如：<equation>A = B</equation>，则<equation>P(A \mid A \cup B) = 1 > 0 = P(\overline{A} \mid A \cup B)</equation>，但<equation>P(A) = P(B)</equation>.

因此，应选D.

下面说明选项A、B、C不正确.

选项A：由于<equation>P ( A )=P ( A \mid B)=\frac{P ( A B)}{P ( B)},</equation>故<equation>P ( A B)=P ( A ) P ( B ),</equation>从而A,B独立.由A,B独立可得A，<equation>\overline{B}</equation>独立，故<equation>P ( A \mid \overline{B})=P ( A ).</equation>选项A成立.

选项B：若<equation>P ( A \mid B ) > P ( A )</equation>，即<equation>\frac{P ( A B )}{P ( B )} > P ( A )</equation>，则<equation>P ( A B ) > P ( A ) P ( B ).</equation><equation>\begin{aligned} P (\bar {A} \mid \bar {B}) &= \frac {P (\bar {A} \bar {B})}{P (\bar {B})} = \frac {1 - P (A \cup B)}{1 - P (B)} = \frac {1 - P (A) - P (B) + P (A B)}{1 - P (B)} \\ > \frac {1 - P (A) - P (B) + P (A) P (B)}{1 - P (B)} &= 1 - P (A) = P (\bar {A}). \end{aligned}</equation>选项B成立.

选项C：若<equation>P ( A \mid B ) > P ( A \mid \overline{B} )</equation>，即<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A B )}{P (\overline{B})}</equation>，则<equation>\frac{P ( A B )}{P ( B )} >\frac{P ( A )-P ( A B )}{1-P ( B )}</equation>.由此可得<equation>P ( A B ) - P ( B ) P ( A B ) > P ( A ) P ( B ) - P ( B ) P ( A B )</equation>即<equation>P ( A B ) > P ( A ) P ( B )</equation>于是，<equation>P ( A ) < \frac { P ( A B ) } { P ( B ) } = P ( A \mid B )</equation>. 选项C成立.

---

**2020年第7题 | 选择题 | 4分 | 答案: D**

7. 设 A,B,C为三个随机事件，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{4}, P ( A B )=0, P ( A C )=P ( B C )=\frac{1}{1 2}</equation>，则 A,B,C中恰有一个事件发生的概率为（    ）

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{2}{3}</equation>C.<equation>\frac{1}{2}</equation>D.<equation>\frac{5}{12}</equation>

答案: D

**解析:**解（法一）设A,B,C中恰有一个事件发生的概率为 p. P（A<equation>\cup</equation>B<equation>\cup</equation>C）为至少发生一个事件的概率. “至少发生一个”可拆分为“恰好发生一个”，“至少发生两个”这样两个互不相容事件.于是，<equation>P (A \cup B \cup C) = p + P (A B \cup B C \cup A C).</equation>由 P（AB）=0可得 P（ABC）=0.由三个事件的加法公式可得<equation>\begin{aligned} P (A \cup B \cup C) &= P (A) + P (B) + P (C) - P (A B) - P (B C) - P (A C) + P (A B C) \\ &= \frac {1}{4} + \frac {1}{4} + \frac {1}{4} - 0 - \frac {1}{1 2} - \frac {1}{1 2} + 0 = \frac {7}{1 2}. \end{aligned}</equation><equation>\begin{aligned} P (A B \cup B C \cup A C) &= P (A B) + P (B C) + P (A C) - P (A B C) - P (A B C) + P (A B C) \\ &= 0 + \frac {1}{1 2} + \frac {1}{1 2} + 0 = \frac {1}{6}. \end{aligned}</equation>从而，<equation>p=\frac{7}{12}-\frac{1}{6}=\frac{5}{12}.</equation>因此，应选D.

（法二）<equation>A,B,C</equation>中恰有一个事件发生的概率为<equation>p=P(A\overline{B}\overline{C})+P(\overline{A}B\overline{C})+P(\overline{A}\overline{B}C).</equation><equation>P \left(A \bar {B} \bar {C}\right) = P \left(A \bar {B}\right) - P \left(A \bar {B} C\right) = P (A) - P (A B) - \left[ P (A C) - P (A C B) \right],</equation><equation>P (\bar {A} B \bar {C}) = P (\bar {A} B) - P (\bar {A} B C) = P (B) - P (A B) - [ P (B C) - P (B C A) ],</equation><equation>P (\bar {A} \bar {B} C) = P (\bar {B} C) - P (\bar {B} C A) = P (C) - P (C B) - [ P (C A) - P (C A B) ].</equation>由<equation>P ( A B ) = 0</equation>可得<equation>P ( A B C ) = 0.</equation>因此，<equation>p = P (A) + P (B) + P (C) - 2 \left[ P (A B) + P (B C) + P (A C) \right] = \frac {3}{4} - 4 \times \frac {1}{1 2} = \frac {5}{1 2}.</equation>应选 D.

---

**2019年第7题 | 选择题 | 4分 | 答案: C**

7. 设 A,B为随机事件，则<equation>P ( A )=P ( B )</equation>的充分必要条件是（    )

A.<equation>P ( A \cup B )=P ( A )+P ( B )</equation>B.<equation>P ( A B )=P ( A ) P ( B )</equation>C.<equation>P ( A \bar{B} )=P ( B \bar{A} )</equation>D.<equation>P ( A B )=P ( \bar{A} \bar{B} )</equation>

答案: C

**解析:**解 由于<equation>A\overline{B}=A-A\cap B, B\overline{A}=B-B\cap A</equation>，故<equation>P(A\overline{B})=P(A)-P(AB), P(B\overline{A})= P(B)-P(AB).</equation>因此，<equation>P ( A )=P ( B )</equation>等价于<equation>P ( A \overline{B} )=P ( B \overline{A} ).</equation>应选C.

下面说明选项A、B、D不正确.

取<equation>A = B</equation>，且<equation>P(A) = P(B) = \frac{1}{3}</equation>.

选项 A：<equation>P ( A \cup B )=P ( A )=\frac{1}{3}, P ( A )+P ( B )=\frac{2}{3}.</equation>选项A不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项B：<equation>P ( A B )=P ( A )=\frac{1}{3}, P ( A ) P ( B )=\frac{1}{9}.</equation>选项B不是<equation>P ( A )=P ( B )</equation>的必要条件.

选项 D：<equation>P ( A B )=P ( A )=\frac{1}{3}, P (\overline{A}\overline{B})=P(\overline{A})=\frac{2}{3}.</equation>选项 D不是<equation>P ( A )=P ( B )</equation>的必要条件.

---

**2018年第14题 | 填空题 | 4分**

14. 随机事件 A,B,C 相互独立，且<equation>P ( A )=P ( B )=P ( C )=\frac{1}{2}</equation>，则<equation>P ( A C \mid A \cup B )=</equation>___.

**答案:**# 1 3.

**解析:**根据事件运算的分配律，<equation>P (A C \cap (A \cup B)) = P ((A C \cap A) \cup (A C \cap B)) = P (A C \cup A B C) = P (A C).</equation>根据和事件的概率公式，<equation>P ( A \cup B ) = P ( A ) + P ( B ) - P ( A B ) .</equation>根据条件概率的计算公式，<equation>\begin{aligned} P (A C \mid A \cup B) &= \frac {P (A C \cap (A \cup B))}{P (A \cup B)} = \frac {P (A C)}{P (A) + P (B) - P (A B)} \\ \frac {\mathrm {独立 性}}{} \frac {P (A) P (C)}{P (A) + P (B) - P (A) P (B)} &= \frac {\frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} + \frac {1}{2} - \frac {1}{2} \times \frac {1}{2}} = \frac {1}{3}. \end{aligned}</equation>

---

**2017年第7题 | 选择题 | 4分 | 答案: C**

7. 设 A,B,C为三个随机事件，且 A与 C相互独立，B与 C相互独立，则 A<equation>\cup</equation>B与 C相互独立的充分必要条件是（    ）

A. A与B相互独立 B. A与B互不相容 C. AB与C相互独立 D. AB与C互不相容

答案: C

**解析:**由已知条件知，<equation>P ( A C ) = P ( A ) P ( C )</equation><equation>P ( B C ) = P ( B ) P ( C )</equation>计算 P（（AUB）<equation>\cap C ）</equation>，得<equation>\begin{aligned} P ((A \cup B) \cap C) &= P ((A \cap C) \cup (B \cap C)) \\ &= P (A \cap C) + P (B \cap C) - P ((A \cap C) \cap (B \cap C)) \\ &= P (A C) + P (B C) - P (A \cap B \cap C) \\ &= P (A) P (C) + P (B) P (C) - P (A \cap B \cap C). \end{aligned}</equation>另一方面，事件 A U B与事件 C相互独立等价于<equation>\begin{aligned} P ((A \cup B) \cap C) &= P (A \cup B) P (C) = [ P (A) + P (B) - P (A B) ] P (C) \\ &= P (A) P (C) + P (B) P (C) - P (A B) P (C). \end{aligned}</equation>因此，事件 A<equation>\cup</equation>B与事件 C相互独立等价于<equation>P ( A B ) P ( C )=P ( A \cap B \cap C )=P ( A B C )</equation>即事件 AB与事件 C相互独立.应选C.

---

**2016年第7题 | 选择题 | 4分 | 答案: A**

7. 设 A,B为两个随机事件，且<equation>0 < P ( A ) < 1, 0 < P ( B ) < 1</equation>，如果<equation>P ( A \mid B )=1</equation>，则（    ）

A.<equation>P ( \bar{B} \mid \bar{A})=1</equation>B.<equation>P ( A \mid \bar{B})=0</equation>C.<equation>P ( A \cup B )=1</equation>D.<equation>P ( B \mid A )=1</equation>

答案: A

**解析:**解 由题设知，<equation>P ( A \mid B ) = \frac { P ( A B ) } { P ( B ) } = 1.</equation>于是<equation>P ( A B ) = P ( B ).</equation>因此，<equation>P (A \cup B) = P (A) + P (B) - P (A B) \xlongequal {P (A B) = P (B)} P (A),</equation><equation>P (\bar {B} \mid \bar {A}) = \frac {P (\bar {B} \bar {A})}{P (\bar {A})} = \frac {P (\overline {{A \cup B}})}{P (\bar {A})} = \frac {1 - P (A \cup B)}{1 - P (A)} = \frac {1 - P (A)}{1 - P (A)} = 1,</equation><equation>P (A \mid \bar {B}) = \frac {P \left(A \bar {B}\right)}{P (\bar {B})} = \frac {P (A) - P (A B)}{P (\bar {B})} = \frac {P (A) - P (B)}{1 - P (B)},</equation><equation>P (B \mid A) = \frac {P (B A)}{P (A)} = \frac {P (B)}{P (A)}.</equation>综上所述，选项A正确.应选A.

也可以如下举反例说明选项B、C、D均不正确.

设<equation>B\subseteq A</equation>，<equation>P(A) = \frac{1}{2}</equation>，<equation>P(B) = \frac{1}{4}</equation>，则<equation>P(A\mid \overline{B}) = \frac{1}{3}</equation>，<equation>P(A\cup B) = \frac{1}{2}</equation>，<equation>P(B\mid A) = \frac{1}{2}</equation>.

---

**2016年第14题 | 填空题 | 4分**

14. 设袋中有红、白、黑球各1个，从中有放回地取球，每次取1个，直到三种颜色的球都取到时停止，则取球次数恰好为4的概率为___

**解析:**解（法一）由于第4次取到的球可以为红、白、黑球中的任一种，故第4次取球有<equation>C_{3}^{1}</equation>种可能的情况.第4次取球的颜色固定后，前三次取球只剩下两种颜色可选，且两种颜色的球都要被取到.于是在前三次取球中，一定有两次取到剩下某一种颜色的球，有一次取到剩下的另一种颜色的球，从而前三次取球有<equation>C_{2}^{1}\cdot C_{3}^{2}</equation>种可能的情况.

因此，取球次数恰好为4的情况共有<equation>\mathrm{C}_{3}^{1}\cdot \mathrm{C}_{2}^{1}\cdot \mathrm{C}_{3}^{2}</equation>种，取球次数恰好为4的概率为<equation>\frac{\mathrm{C}_{3}^{1}\cdot \mathrm{C}_{2}^{1}\cdot \mathrm{C}_{3}^{2}}{3^{4}}=\frac{2}{9}.</equation>满足题设条件的取球情况如下表.

<table border="1"><tr><td>第4次取球</td><td colspan="3">前三次取球</td></tr><tr><td rowspan="2">红</td><td>白白黑</td><td>白黑白</td><td>黑白白</td></tr><tr><td>黑黑白</td><td>黑白黑</td><td>白黑黑</td></tr><tr><td rowspan="2">白</td><td>红红黑</td><td>红黑红</td><td>黑红红</td></tr><tr><td>黑黑红</td><td>黑红黑</td><td>红黑黑</td></tr><tr><td rowspan="2">黑</td><td>红红白</td><td>红白红</td><td>白红红</td></tr><tr><td>白白红</td><td>白红白</td><td>红白白</td></tr></table>

（法二）因为恰好四次便可取完三种颜色的球，所以前三次中一定有同一颜色的球取了两次.前三次中任取两次共有<equation>C_{3}^{2}</equation>种情况，这两次选取的颜色共有<equation>C_{3}^{1}</equation>种情况；前三次中剩下的一次取剩下的两种颜色中的一种，共<equation>C_{2}^{1}</equation>种情况；前三次的球选好后，第四次的球只剩一种选择.因此，共有<equation>C_{3}^{2}\cdot C_{3}^{1}\cdot C_{2}^{1}</equation>种情况，所求概率为<equation>\frac{C_{3}^{2}\cdot C_{3}^{1}\cdot C_{2}^{1}}{3^{4}}=\frac{2}{9}.</equation>

---

**2015年第7题 | 选择题 | 4分 | 答案: C**

7. 若 A,B为任意两个随机事件，则（    ）

A.<equation>P ( A B ) \leqslant P ( A ) P ( B )</equation>B.<equation>P ( A B ) \geqslant P ( A ) P ( B )</equation>C.<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>D.<equation>P ( A B ) \geqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>

答案: C

**解析:**由于<equation>A\cap B\subseteq A,A\cap B\subseteq B</equation>，故<equation>P (A B) \leqslant P (A), \quad P (A B) \leqslant P (B).</equation>因此，<equation>2 P ( A B ) \leqslant P ( A ) + P ( B )</equation>，即<equation>P ( A B ) \leqslant \frac { P ( A ) + P ( B ) } { 2 }</equation>.应选C.

下面我们说明选项 A、B、D不正确.

选项A：若 B<equation>\subseteq A</equation>，0 < P(A) < 1，0 < P(B) < 1<equation>，则 P ( A B ) = P ( A \cap B ) = P ( B ) > P ( A ) P ( B )</equation>因此选项A不正确.

选项B、D：若 P(A）>0，P(B）>0且 A<equation>\cap</equation>B=<equation>\varnothing</equation>，则 P(AB）=P（A<equation>\cap</equation>B）=0<P(A)P(B)<equation>P(AB)<\frac{P(A)+P(B)}{2}</equation>因此选项B和选项D不正确.

---

**2014年第7题 | 选择题 | 4分 | 答案: B**

7. 设随机事件 A与 B相互独立，且<equation>P ( B )=0. 5, P ( A-B)=0. 3</equation>，则<equation>P ( B-A )=</equation>(    )

A. 0.1 B. 0.2 C. 0.3 D. 0.4

答案: B

**解析:**（法一）由 A与B相互独立知，<equation>P ( A B ) = P ( A ) P ( B ).</equation>.于是，<equation>P (A - B) = P (A) - P (A B) = P (A) - P (A) P (B) = P (A) [ 1 - P (B) ] = 0. 5 P (A).</equation>从而<equation>P ( A ) = 2 P ( A - B ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P (B) - P (A B) = P (B) - P (A) P (B) = 0. 5 - 0. 6 \times 0. 5 = 0. 2.</equation>应选B.

（法二）由<equation>A</equation>与<equation>B</equation>相互独立知，<equation>A, \bar{B}</equation>也相互独立.于是，<equation>0. 3 = P (A - B) = P (A \cap \bar {B}) = P (A \bar {B}) = P (A) P (\bar {B}) = 0. 5 P (A).</equation>因此，<equation>P ( A ) = 0. 6.</equation>进一步可得，<equation>P (B - A) = P \left(B \bar {A}\right) = P (B) P (\bar {A}) = 0. 5 \times (1 - 0. 6) = 0. 2.</equation>应选B.

---

**2012年第14题 | 填空题 | 4分**

14. 设 A,B,C是随机事件，A与C互不相容，<equation>P ( A B )=\frac{1} {2}, P ( C )=\frac{1} {3}</equation>，则<equation>P ( A B \mid \bar{C})=</equation>___

**答案:**# 3 4.

**解析:**解 由条件概率的定义可知，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{P (\bar{C})}=\frac{P ( A B \bar{C})}{1-P(C)}.</equation>又由于 A与C互不相容，即<equation>A \cap C=\varnothing</equation>，故<equation>A \cap B \subseteq A \subseteq \bar{C}</equation>，从而<equation>A \cap B \cap \bar{C}=A \cap B, P ( A B \bar{C})=P ( A B ).</equation>因此，<equation>P ( A B \mid \bar{C})=\frac{P ( A B \bar{C})}{1-P(C)}=\frac{P ( A B)}{1-P(C)}=\frac{\frac{1}{2}}{1-\frac{1}{3}}=\frac{3}{4}.</equation>

---

**2009年第7题 | 选择题 | 4分 | 答案: D**

7. 设事件 A与事件 B互不相容，则（    ）

A.<equation>P(\bar{A}\bar{B})=0</equation>B.<equation>P(AB)=P(A)P(B)</equation>C.<equation>P(A)=1-P(B)</equation>D.<equation>P(\bar{A}\cup\bar{B})=1</equation>

答案: D

**解析:**解 由于事件 A与事件 B互不相容，故<equation>A \cap B=\varnothing</equation>.又因为<equation>\overline{A}\cup \overline{B}=\overline{A\cap B}</equation>，所以<equation>P(\overline{A}\cup \overline{B})= P(\overline{A\cap B})=1-P(AB)=1-0=1.</equation>应选 D.

下面我们分别说明选项A、B、C不正确.

由于<equation>\overline{A}\cap \overline{B}=\overline{A\cup B}</equation>，故<equation>P(\overline{A}\overline{B})=P(\overline{A\cup B})=1-P(A\cup B).</equation>当<equation>P(A\cup B)\neq 1</equation>时，<equation>P(\overline{A}\overline{B})\neq 0.</equation>选项A不正确.

若<equation>P ( A ) \neq 0</equation>且<equation>P ( B ) \neq 0</equation>，则<equation>P ( A B ) = 0 \neq P ( A ) P ( B ).</equation>选项B不正确.

由于<equation>A \cap B = \varnothing</equation>，即<equation>A \subseteq \overline{B}</equation>，故<equation>P(A) \leqslant P(\overline{B}) = 1 - P(B)</equation>.选项C不正确.

---


### 多维随机变量及其分布


