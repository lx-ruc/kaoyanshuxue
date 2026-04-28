---

**2023年第10题 | 选择题 | 5分 | 答案: A**

10. 设<equation>X_{1}, X_{2}</equation>为来自总体<equation>N\left(\mu ,\sigma^{2}\right)</equation>的简单随机样本，其中<equation>\sigma(\sigma>0)</equation>是未知参数.若<equation>\hat{\sigma}=a\left| X_{1}-X_{2}\right|</equation>为<equation>\sigma</equation>的无偏估计，则 a=（    ）

A.<equation>\frac{\sqrt{\pi}}{2}</equation>B.<equation>\frac{\sqrt{2\pi}}{2}</equation>C.<equation>\sqrt{\pi}</equation>D.<equation>\sqrt{2\pi}</equation>

答案: A

**解析:**解 由于<equation>X_{1}, X_{2}</equation>为来自总体<equation>N(\mu ,\sigma^{2})</equation>的简单随机样本，故<equation>X_{1}, X_{2}</equation>相互独立.

令<equation>Z = X_{1} - X_{2}</equation>，则<equation>Z\sim N(0,2\sigma^{2})</equation>，从而Z的概率密度<equation>f(z) = \frac{1}{\sqrt{2\pi}\cdot \sqrt{2}\sigma}\mathrm{e}^{-\frac{z^{2}}{4\sigma^{2}}}</equation>.<equation>\begin{aligned} E (\mid Z \mid) &= \int_ {- \infty} ^ {+ \infty} | z | f (z) \mathrm {d} z = 2 \int_ {0} ^ {+ \infty} \frac {1}{\sqrt {2 \pi} \cdot \sqrt {2} \sigma} \cdot z \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} z = \frac {1}{2 \sqrt {\pi} \sigma} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}} \mathrm {d} \left(z ^ {2}\right) \\ &= \frac {1}{2 \sqrt {\pi} \sigma} \cdot \left(- 4 \sigma^ {2} \mathrm {e} ^ {- \frac {z ^ {2}}{4 \sigma^ {2}}}\right) \Big | _ {0} ^ {+ \infty} = \frac {2}{\sqrt {\pi}} \sigma . \end{aligned}</equation>由此可得<equation>E (\hat {\sigma}) = E \left(a \mid X _ {1} - X _ {2} \mid\right) = E \left(a \mid Z \mid\right) = \frac {2 a}{\sqrt {\pi}} \sigma .</equation>又因为<equation>\hat{\sigma}</equation>为<equation>\sigma</equation>的无偏估计，所以<equation>E(\hat{\sigma})=\sigma</equation>，即<equation>\frac{2a}{\sqrt{\pi}}\sigma=\sigma</equation>，解得 a<equation>=\frac{\sqrt{\pi}}{2}.</equation>因此，应选A.

---

**2021年第9题 | 选择题 | 5分 | 答案: C**

9. 设<equation>( X_{1}, Y_{1}), ( X_{2}, Y_{2}), \cdots, ( X_{n}, Y_{n} )</equation>为来自总体<equation>N (\mu_{1}, \mu_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; \rho)</equation>的简单随机样本，令<equation>\theta=\mu_{1}-\mu_{2}, \bar{X}=\frac{1}{n}\sum_{i=1}^{n} X_{i}, \bar{Y}=\frac{1}{n}\sum_{i=1}^{n} Y_{i}, \hat{\theta}=\bar{X}-\bar{Y}</equation>则（    )

A.<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>B.<equation>\hat{\theta}</equation>不是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{n}</equation>C.<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>D.<equation>\hat{\theta}</equation>不是<equation>\theta</equation>的无偏估计，<equation>D(\hat{\theta})=\frac{\sigma_{1}^{2}+\sigma_{2}^{2}-2\rho\sigma_{1}\sigma_{2}}{n}</equation>

答案: C

**解析:**解 由于总体（X，Y）服从<equation>N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>，故<equation>X\sim N(\mu_{1},\sigma_{1}^{2}),Y\sim N(\mu_{2},\sigma_{2}^{2})</equation>，从而<equation>\bar{X}\sim</equation><equation>N\left(\mu_{1},\frac{\sigma_{1}^{2}}{n}\right),\bar{Y}\sim N\left(\mu_{2},\frac{\sigma_{2}^{2}}{n}\right).</equation>计算<equation>E(\hat{\theta})</equation><equation>E (\hat {\theta}) = E (\bar {X} - \bar {Y}) = E (\bar {X}) - E (\bar {Y}) = \mu_ {1} - \mu_ {2} = \theta .</equation>因此，<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计.

计算<equation>D(\hat{\theta})</equation><equation>D (\hat {\theta}) = D (\bar {X} - \bar {Y}) = D (\bar {X}) + D (\bar {Y}) - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}).</equation>由于<equation>\left(X_{1},Y_{1}\right), \left(X_{2},Y_{2}\right),\dots ,\left(X_{n},Y_{n}\right)</equation>为简单随机样本，故它们相互独立，从而当<equation>i\neq j</equation>时，<equation>X_{i}</equation>与<equation>Y_{j}</equation>独立.于是，<equation>\operatorname{Cov}(X_{i},Y_{i})=\operatorname{Cov}(X,Y),\operatorname{Cov}(X_{i},Y_{j})=0(i\neq j).</equation><equation>\begin{aligned} \operatorname {C o v} (\bar {X}, \bar {Y}) &= \operatorname {C o v} \left(\frac {\sum_ {i = 1} ^ {n} X _ {i}}{n}, \frac {\sum_ {j = 1} ^ {n} Y _ {j}}{n}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {j}\right) = \frac {1}{n ^ {2}} \cdot \sum_ {i = 1} ^ {n} \operatorname {C o v} \left(X _ {i}, Y _ {i}\right) \\ &= \frac {1}{n ^ {2}} \cdot n \operatorname {C o v} (X, Y) = \frac {\operatorname {C o v} (X , Y)}{n}. \end{aligned}</equation>因此，<equation>D (\hat {\theta}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - 2 \operatorname {C o v} (\bar {X}, \bar {Y}) = \frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{n} - \frac {2}{n} \operatorname {C o v} (X, Y) = \frac {\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2} - 2 \rho \sigma_ {1} \sigma_ {2}}{n}.</equation>应选C.

---

**2016年第23题 | 解答题 | 11分**

3. (本题满分11分)

设总体 X的概率密度为<equation>f ( x; \theta) = \left\{ \begin{array}{l l} \frac{3 x^{2}}{\theta^{3}}, & 0 < x < \theta , \\ 0, & \mathrm {其 他}, \end{array} \right.</equation>其中<equation>\theta \in(0,+\infty)</equation>为未知参数，<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体 X的简单随机样本，令<equation>T=\max \left\{X_{1}, X_{2}, X_{3}\right\}</equation>.

I. 求 T的概率密度；

II. 确定 a，使得 aT为<equation>\theta</equation>的无偏估计.

**答案:**<equation>(\mathrm {I}) f _ {T} (t) = \left\{ \begin{array}{l l} \frac {9 t ^ {8}}{\theta^ {9}}, & 0 < t < \theta , \\ 0, & \mathrm {其 他}; \end{array} \right. (\mathrm {I I}) a = \frac {1 0}{9}.</equation>

**解析:**解（I）设<equation>T</equation>的分布函数为<equation>F_{T}(t), T</equation>的概率密度为<equation>f_{T}(t).</equation>由于<equation>X_{1}, X_{2}, X_{3}</equation>为来自总体X的简单随机样本，故它们相互独立且与X同分布.从而<equation>\begin{array}{l} F _ {T} (t) = P \left\{T \leqslant t \right\} = P \left\{X _ {1} \leqslant t, X _ {2} \leqslant t, X _ {3} \leqslant t \right\} = P \left\{X _ {1} \leqslant t \right\} \cdot P \left\{X _ {2} \leqslant t \right\} \cdot P \left\{X _ {3} \leqslant t \right\} \\ = \left[ P \left\{X \leqslant t \right\} \right] ^ {3} = \left[ F _ {X} (t) \right] ^ {3}, \\ \end{array}</equation>其中<equation>F_{X}(t)</equation>为X的分布函数.

下面用两种方法求<equation>f_{T}(t)</equation>（法一）先求<equation>F_{T}(t)</equation>，再求导得到<equation>f_{T}(t)</equation>当<equation>t < 0</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x;\theta)\mathrm{d}x = 0.</equation>于是<equation>F_{T}(t) = [F_{X}(t)]^{3} = 0.</equation>当 0≤t <<equation>\theta</equation>时，<equation>F_{X}(t)=\int_{-\infty}^{t} f(x;\theta)\mathrm{d}x=\int_{0}^{t}\frac{3x^{2}}{\theta^{3}}\mathrm{d}x=\frac{t^{3}}{\theta^{3}}.</equation>于是<equation>F_{T}(t)=[F_{X}(t)]^{3}=\frac{t^{9}}{\theta^{9}}.</equation>当 t≥<equation>\theta</equation>时，<equation>F_{X}(t)=1.</equation>于是<equation>F_{T}(t)=[F_{X}(t)]^{3}=1.</equation>因此，<equation>F _ {T} (t) = \left\{ \begin{array}{l l} 0, & t < 0, \\ \frac {t ^ {9}}{\theta^ {9}}, & 0 \leqslant t < \theta , \\ 1, & t \geqslant \theta . \end{array} \right.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = F_{T}^{\prime}(t) = \left\{ \begin{array}{ll} \frac{9t^{8}}{\theta^{9}}, & 0 < t < \theta , \\ 0, & \text{其他}. \end{array} \right.</equation>（法二）直接求导得到<equation>f_{T}(t)</equation>后再求解.<equation>f _ {T} (t) = F _ {T} ^ {\prime} (t) = 3 F _ {X} ^ {\prime} (t) \left[ F _ {X} (t) \right] ^ {2} = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2}.</equation>当<equation>t < 0</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>当<equation>0 \leqslant t < \theta</equation>时，<equation>F_{X}(t) = \int_{-\infty}^{t} f(x; \theta)\mathrm{d}x = \int_{0}^{t} \frac{3x^{2}}{\theta^{3}}\mathrm{d}x = \frac{t^{3}}{\theta^{3}}.</equation>于是<equation>f _ {T} (t) = 3 f (t; \theta) \left[ F _ {X} (t) \right] ^ {2} = 3 \cdot \frac {3 t ^ {2}}{\theta^ {3}} \cdot \left(\frac {t ^ {3}}{\theta^ {3}}\right) ^ {2} = \frac {9 t ^ {8}}{\theta^ {9}}.</equation>当<equation>t \geqslant \theta</equation>时，<equation>f(t; \theta) = 0.</equation>于是<equation>f_{T}(t) = 0.</equation>综上所述，<equation>T</equation>的概率密度为<equation>f_{T}(t) = \left\{ \begin{array}{ll} \frac{9t^8}{\theta^9}, & 0 < t < \theta , \\ 0, & \text{其他}. \end{array} \right.</equation>（Ⅱ）由第（I）问中所求结果知，<equation>E (a T) = a E (T) = a \int_ {- \infty} ^ {+ \infty} t f _ {T} (t) \mathrm {d} t = a \int_ {0} ^ {\theta} \frac {9 t ^ {9}}{\theta^ {9}} \mathrm {d} t = \frac {9 a}{1 0 \theta^ {9}} t ^ {1 0} \Bigg | _ {0} ^ {\theta} = \frac {9}{1 0} a \theta .</equation>要使<equation>E(aT) = \theta</equation>，则<equation>\frac{9}{10} a\theta = \theta</equation>，解得<equation>a = \frac{10}{9}</equation>.

因此，当<equation>a=\frac{10}{9}</equation>时，<equation>aT</equation>为<equation>\theta</equation>的无偏估计.

---

**2014年第14题 | 填空题 | 4分**

14. 设总体 X的概率密度为 f(x;<equation>\theta)=\left\{\begin{array}{ll}\frac{2x}{3\theta^{2}},&\theta<x<2\theta,\\ 0,&\text{其他},\end{array} \right.</equation>其中<equation>\theta</equation>是未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本，若<equation>c\sum_{i=1}^{n}X_{i}^{2}</equation>是<equation>\theta^{2}</equation>的无偏估计，则 c=___

**解析:**由题设知，<equation>\theta^ {2} = E \left(c \sum_ {i = 1} ^ {n} X _ {i} ^ {2}\right) = n c E \left(X ^ {2}\right) = n c \int_ {\theta} ^ {2 \theta} x ^ {2} \cdot \frac {2 x}{3 \theta^ {2}} \mathrm {d} x = \frac {5}{2} \theta^ {2} n c,</equation>从而<equation>c = \frac{2}{5n}</equation>

---

**2010年第23题 | 解答题 | 11分**


设总体 X的概率分布为：

<table border="1"><tr><td>X</td><td>1</td><td>2</td><td>3</td></tr><tr><td>P</td><td>1-θ</td><td>θ-θ2</td><td>θ2</td></tr></table>

其中参数<equation>\theta \in (0,1)</equation>未知.以<equation>N_{i}</equation>表示来自总体<equation>X</equation>的简单随机样本（样本容量为<equation>n</equation>）中等于<equation>i</equation>的个数<equation>(i = 1,2,3)</equation>试求常数<equation>a_{1},a_{2},a_{3}</equation>，使<equation>T = \sum_{i = 1}^{3}a_{i}N_{i}</equation>为<equation>\theta</equation>的无偏估计量，并求<equation>T</equation>的方差.

**答案:**<equation>(2 3) a _ {1} = 0, a _ {2} = a _ {3} = \frac {1}{n}, D (T) = \frac {\theta (1 - \theta)}{n}.</equation>

**解析:**解 令<equation>T = \sum_{i = 1}^{3} a_{i} N_{i}</equation>为<equation>\theta</equation>的无偏估计量，则有<equation>\theta = E (T) = \sum_ {i = 1} ^ {3} a _ {i} E \left(N _ {i}\right).</equation>由<equation>N_{i}</equation>的定义知，<equation>N_{i}</equation>服从二项分布，即<equation>N_{1}\sim B(n,1 - \theta),N_{2}\sim B(n,\theta -\theta^{2}),N_{3}\sim B(n,\theta^{2})</equation>，从而<equation>E(N_{1}) = n(1 - \theta),E(N_{2}) = n(\theta -\theta^{2}),E(N_{3}) = n\theta^{2}</equation>.代入（1）式得<equation>\theta = a _ {1} n (1 - \theta) + a _ {2} n \left(\theta - \theta^ {2}\right) + a _ {3} n \theta^ {2},</equation>整理得<equation>0 = a _ {1} n + \left(a _ {2} n - a _ {1} n - 1\right) \theta + \left(a _ {3} n - a _ {2} n\right) \theta^ {2},</equation>从而<equation>a _ {1} n = 0, \quad a _ {2} n - a _ {1} n - 1 = 0, \quad a _ {3} n - a _ {2} n = 0,</equation>解得<equation>a_{1}=0,a_{2}=\frac{1}{n},a_{3}=\frac{1}{n}.</equation>又由<equation>N_{i}</equation>的定义知，<equation>N_{1}+N_{2}+N_{3}=n</equation>，故<equation>T = \sum_ {i = 1} ^ {3} a _ {i} N _ {i} = \frac {1}{n} \left(N _ {2} + N _ {3}\right) = \frac {1}{n} \left(n - N _ {1}\right) = 1 - \frac {1}{n} N _ {1},</equation>从而<equation>D (T) = D \left(1 - \frac {1}{n} N _ {1}\right) = \frac {1}{n ^ {2}} D \left(N _ {1}\right) = \frac {1}{n ^ {2}} \cdot n (1 - \theta) \theta = \frac {\theta (1 - \theta)}{n}.</equation>综上所述，<equation>a_{1}=0, a_{2}=\frac{1}{n}, a_{3}=\frac{1}{n}, D(T)=\frac{\theta(1-\theta)}{n}.</equation>

---

**2009年第14题 | 填空题 | 4分**

14. 设<equation>X_{1}, X_{2}, \cdots, X_{m}</equation>为来自二项分布总体<equation>B(n,p)</equation>的简单随机样本，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别为样本均值和样本方差，若<equation>\bar{X}+k S^{2}</equation>为<equation>n p^{2}</equation>的无偏估计量，则 k=___

**答案:**<equation>- 1.</equation>

**解析:**解 由题设知，<equation>n p^{2}=E(\overline{X}+k S^{2})=E(\overline{X})+k E(S^{2}).</equation>又<equation>E(\overline{X})=E(X)=np,</equation><equation>E(S^{2})=D(X)=np(1-p),</equation>故有<equation>n p^{2}=np+np(1-p)k</equation>，解得 k=-1.

---


**2014年第23题 | 解答题 | 11分**


23. (本题满分11分)

设总体 X的分布函数为<equation>F ( x ; \theta) = \left\{ \begin{array}{l l} 1 - \mathrm{e}^{- \frac {x^{2}}{\theta}}, & x \geqslant 0, \\ 0, & x < 0, \end{array} \right.</equation>其中<equation>\theta</equation>是未知参数且大于零.<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体 X的简单随机样本.

I. 求<equation>E ( X )</equation>与<equation>E \left( X^{2} \right)</equation>II. 求<equation>\theta</equation>的最大似然估计量<equation>\hat{\theta}_{n}</equation>III. 是否存在实数 a，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim_{n \to \infty} P \{ | \hat{\theta}_{n}-a | \geqslant \varepsilon \}=0</equation>？

**答案:**(23) (I)<equation>E ( X )=\frac{\sqrt{\pi\theta}}{2}, E ( X^{2} )=\theta;</equation>(Ⅱ)<equation>\widehat{\theta}_n = \frac{1}{n}\sum_{i=1}^{n} X_i^2</equation>;

（Ⅲ）存在实数<equation>a = \theta</equation>，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim_{n\to \infty}P\{|\widehat{\theta}_n - a| \geqslant \varepsilon \} = 0.</equation>

**解析:**解（I）由题设知，X的概率密度<equation>f ( x ; \theta) = \left\{ \begin{array}{ll} \frac{2 x}{\theta} \mathrm{e}^{- \frac{x^{2}}{\theta}}, & x \geqslant 0, \\ 0, & x < 0, \end{array} \right.</equation>于是<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} x \cdot \frac {2 x}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x = \int_ {0} ^ {+ \infty} x \mathrm {d} \left(- \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}}\right) = - x \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \Bigg | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x \\ &= 0 + \sqrt {\theta} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \left(\frac {x}{\sqrt {\theta}}\right) ^ {2}} \mathrm {d} \left(\frac {x}{\sqrt {\theta}}\right) \stackrel {t = \frac {x}{\sqrt {\theta}}} {=} \sqrt {\theta} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t \\ &= \sqrt {\theta} \cdot \frac {\sqrt {\pi}}{2} = \frac {\sqrt {\pi \theta}}{2}, \quad \text {这 里 利用 了 等 式} \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {\sqrt {\pi}}{2}. \end{aligned}</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {0} ^ {+ \infty} x ^ {2} \cdot \frac {2 x}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} x = \theta \int_ {0} ^ {+ \infty} \frac {x ^ {2}}{\theta} \mathrm {e} ^ {- \frac {x ^ {2}}{\theta}} \mathrm {d} \left(\frac {x ^ {2}}{\theta}\right) \stackrel {u = \frac {x ^ {2}}{\theta}} {=} \theta \int_ {0} ^ {+ \infty} u \mathrm {e} ^ {- u} \mathrm {d} u \\ &= \theta \left(- u \mathrm {e} ^ {- u} \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- u} \mathrm {d} u\right) = \theta . \end{aligned}</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是来自于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一个样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {2 ^ {n} x _ {1} x _ {2} \cdots x _ {n}}{\theta^ {n}} \mathrm {e} ^ {- \frac {x _ {1} ^ {2} + x _ {2} ^ {2} + \cdots + x _ {n} ^ {2}}{\theta}}, & x _ {1} \geqslant 0, x _ {2} \geqslant 0, \dots , x _ {n} \geqslant 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{1} > 0,x_{2} > 0,\dots ,x_{n} > 0</equation>时，<equation>\ln L (\theta) = \ln \left(2 ^ {n} x _ {1} x _ {2} \dots x _ {n}\right) - n \ln \theta - \frac {x _ {1} ^ {2} + x _ {2} ^ {2} + \dots + x _ {n} ^ {2}}{\theta}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\theta)\right]}{\mathrm{d}\theta}=0</equation>即有<equation>-\frac{n}{\theta}+\frac{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}}{\theta^{2}}=0</equation>解得<equation>\theta=\frac{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}}{n}</equation>，于是<equation>\theta</equation>的最大似然估计量为<equation>\widehat {\theta} _ {n} = \frac {X _ {1} ^ {2} + X _ {2} ^ {2} + \cdots + X _ {n} ^ {2}}{n} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}.</equation>（Ⅲ）由<equation>X_{1},X_{2},\dots ,X_{n}</equation>独立同分布知，<equation>X_{1}^{2},X_{2}^{2},\dots ,X_{n}^{2}</equation>独立同分布.又由（I）知，<equation>E\left(X_{i}^{2}\right) = E\left(X^{2}\right) = \theta</equation>，故由辛钦大数定律知，对任意<equation>\varepsilon >0</equation>，有<equation>\lim_{n\to \infty}P\left\{\left|\frac{1}{n}\sum_{i = 1}^{n}X_{i}^{2} - \theta\right| < \varepsilon\right\} = 1</equation>，从而<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \theta \right| \geqslant \varepsilon \right\} = 0,</equation>即存在实数<equation>a = \theta</equation>，使得对任何<equation>\varepsilon > 0</equation>，都有<equation>\lim P\{ |\widehat{\theta}_n - a | \geqslant \varepsilon \} = 0.</equation>

---

**2020年第23题 | 解答题 | 11分**


设某元件的使用寿命<equation>T</equation>的分布函数为<equation>F (t) = \left\{ \begin{array}{l l} 1 - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t \geqslant 0 \\ 0, & \text {其 他} \end{array} \right.</equation>其中<equation>\theta, m</equation>为参数且大于零.

I. 求概率<equation>P\{T > t\}</equation>与<equation>P\{T > s + t \mid T > s\}</equation>，其中<equation>s > 0, t > 0</equation>.

II. 任取 n个这种元件做寿命试验，测得它们的寿命分别为<equation>t_{1}, t_{2}, \dots , t_{n}</equation>，若 m已知，求<equation>\theta</equation>的最大似然估计值<equation>\hat{\theta}.</equation>

**答案:**（I）<equation>P \left\{ T > t \right\} = \mathrm{e}^{-\left(\frac{t}{\theta}\right)^{m}}, P \left\{ T > s + t \mid T > s \right\} = \mathrm{e}^{\frac{s^{m} - (s + t)^{m}}{\theta^{m}}};</equation>（Ⅱ）<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta}=\sqrt[m]{\frac{1}{n}\sum_{i=1}^{n}t_{i}^{m}}.</equation>

**解析:**（I）由分布函数的定义以及<equation>s > 0,t > 0</equation>可得，<equation>P \left\{T > t \right\} = 1 - P \left\{T \leqslant t \right\} = 1 - F (t) = \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {n}}.</equation><equation>P \left\{T > s + t \mid T > s \right\} = \frac {P \left\{T > s + t \right\}}{P \left\{T > s \right\}} = \frac {\mathrm {e} ^ {- \left(\frac {s + t}{\theta}\right) ^ {m}}}{\mathrm {e} ^ {- \left(\frac {s}{\theta}\right) ^ {m}}} = \mathrm {e} ^ {\frac {s ^ {m} - \left(s + t\right) ^ {m}}{\theta^ {m}}}.</equation>（Ⅱ）计算概率密度<equation>f ( t ; \theta)</equation><equation>f (t; \theta) = F ^ {\prime} (t; \theta) = \left\{ \begin{array}{l l} - \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}} \cdot (- m) \cdot \left(\frac {t}{\theta}\right) ^ {m - 1} \cdot \frac {1}{\theta}, & t > 0, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {m t ^ {m - 1}}{\theta^ {m}} \mathrm {e} ^ {- \left(\frac {t}{\theta}\right) ^ {m}}, & t > 0, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>似然函数<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(t _ {i}; \theta\right) = \left\{ \begin{array}{l l} \left(t _ {1} t _ {2} \dots t _ {n}\right) ^ {m - 1} \cdot \left(\frac {m}{\theta^ {m}}\right) ^ {n} \cdot \mathrm {e} ^ {- \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}}, & t _ {i} > 0, i = 1, 2, \dots , n, \\ 0, & \text {其 他}. \end{array} \right.</equation>取对数得<equation>\ln L (\theta) = (m - 1) \ln \left(t _ {1} t _ {2} \dots t _ {n}\right) + n \left(\ln m - m \ln \theta\right) - \frac {1}{\theta^ {m}} \sum_ {i = 1} ^ {n} t _ {i} ^ {m}.</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta} = -\frac{mn}{\theta} + \frac{m}{\theta^{m + 1}}\sum_{i = 1}^{n}t_{i}^{m} = 0</equation>，可得<equation>mn\theta^{m} = m\sum_{i = 1}^{n}t_{i}^{m}</equation>. 从而<equation>\theta^{m} = \frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m},\hat{\theta} = \sqrt[m]{\frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m}}</equation>因此，<equation>\theta</equation>的最大似然估计值为<equation>\hat{\theta} = \sqrt[m]{\frac{1}{n}\sum_{i = 1}^{n}t_{i}^{m}}</equation>

---

**2019年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f \left(x; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}}, & x \geqslant \mu \\ 0, & x < \mu \end{array} \right.</equation>其中<equation>\mu</equation>是已知参数，<equation>\sigma > 0</equation>是未知参数，<equation>A</equation>是常数.<equation>X_{1}, X_{2}, \dots , X_{n}</equation>是来自总体<equation>X</equation>的简单随机样本.

I. 求 A；

II. 求<equation>\sigma^{2}</equation>的最大似然估计量.

**答案:**（ I ）<equation>A=\sqrt{\frac{2}{\pi}};</equation>（ II ）<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat{\sigma^{2}}=\frac{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}}{n}.</equation>

**解析:**解（I）利用<equation>\int_{- \infty}^{+ \infty} f ( x ; \sigma^{2} ) \mathrm{d} x=1</equation>来计算A.<equation>\begin{aligned} \int_ {- \infty} ^ {+ \infty} f (x; \sigma^ {2}) \mathrm {d} x &= \int_ {\mu} ^ {+ \infty} \frac {A}{\sigma} \mathrm {e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}} \mathrm {d} x \underline {{= t = x - \mu}} A \int_ {0} ^ {+ \infty} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {t ^ {2}}{2 \sigma^ {2}}} \mathrm {d} t = A \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {1}{2} \cdot \left(\frac {t}{\sigma}\right) ^ {2}} \mathrm {d} \left(\frac {t}{\sigma}\right) \\ \frac {\frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \mathrm {d} x = 1}{\underline {{}}} A \cdot \frac {\sqrt {2 \pi}}{2} &= 1. \end{aligned}</equation>因此，<equation>A = \frac{2}{\sqrt{2\pi}} = \sqrt{\frac{2}{\pi}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一组样本值，则关于<equation>\sigma^2</equation>的似然函数为<equation>\begin{array}{l} L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma^ {2}\right) = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {n} \sqrt {\frac {2}{\pi}} \cdot \frac {1}{\sigma} \cdot \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他} \end{array} \right. \\ = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \cdot \left(\frac {1}{\sigma^ {2}}\right) ^ {\frac {n}{2}} \cdot \mathrm {e} ^ {- \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}}, & x _ {1} \geqslant \mu , x _ {2} \geqslant \mu , \dots , x _ {n} \geqslant \mu , \\ 0, & \text {其 他}. \end{array} \right. \\ \end{array}</equation>当<equation>x_{1}\geqslant \mu ,x_{2}\geqslant \mu ,\dots ,x_{n}\geqslant \mu</equation>时，<equation>\ln L \left(\sigma^ {2}\right) = \frac {n}{2} \ln \frac {2}{\pi} - \frac {n}{2} \ln \sigma^ {2} - \frac {\sum_ {i = 1} ^ {n} \left(x _ {i} - \mu\right) ^ {2}}{2 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L\left(\sigma^2\right)\right]}{\mathrm{d}\left(\sigma^2\right)} = 0</equation>，即<equation>-\frac{n}{2}\cdot \frac{1}{\sigma^2} +\frac{\sum_{i=1}^{n}\left(x_{i} - \mu\right)^{2}}{2}\cdot \frac{1}{\sigma^{4}} = 0</equation>，解得<equation>\sigma^2 = \frac{\sum_{i=1}^{n}\left(x_{i} - \mu\right)^{2}}{n}</equation>因此，<equation>\sigma^2</equation>的最大似然估计量为<equation>\widehat {\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {n} \left(X _ {i} - \mu\right) ^ {2}}{n}.</equation>

---

**2018年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \sigma) = \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}}, - \infty < x < + \infty</equation><equation>\sigma \in (0, + \infty)</equation>为未知参数，<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体<equation>X</equation>的简单随机样本.记<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}</equation>.

I. 求<equation>\hat{\sigma}</equation>；

II. 求<equation>E(\hat{\sigma})</equation>和<equation>D(\hat{\sigma})</equation>

**答案:**（I）<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}=\frac{\sum_{i=1}^{n} \mid X_{i}\mid}{n}；</equation>（Ⅱ）<equation>E(\hat{\sigma})=\sigma,D(\hat{\sigma})=\frac{\sigma^{2}}{n}.</equation>

**解析:**解（I）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值. 似然函数为<equation>L (\sigma) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma\right) = \frac {1}{2 ^ {n} \sigma^ {n}} \mathrm {e} ^ {- \frac {\left| x _ {1} \right| + \left| x _ {2} \right| + \cdots + \left| x _ {n} \right|}{\sigma}}, - \infty < x _ {i} < + \infty , i = 1, 2, \dots , n.</equation>对 L （<equation>\sigma</equation>）取对数，得<equation>\ln L (\sigma) = - \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} \right|}{\sigma} - n \ln (2 \sigma).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = \frac{\sum_{i=1}^{n}|x_i|}{\sigma^2} - \frac{n}{\sigma} = 0</equation>，即<equation>\sum_{i=1}^{n}|x_i| - n\sigma = 0.</equation>解得<equation>\sigma = \frac{\sum_{i=1}^{n}|x_i|}{n}.</equation>因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}.</equation>（Ⅱ）由于<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体X的简单随机样本，故它们相互独立，且与总体X同分布<equation>E \left( X_{i}\right) = E \left( X\right), E \left( \mid X_{i} \mid\right) = E \left( \mid X \mid\right), i = 1, 2, \dots , n.</equation>根据期望的线性性质，<equation>E \left(\hat {\sigma}\right) = E \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {\sum_ {i = 1} ^ {n} E \left(\left| X _ {i} \right|\right)}{n} = \frac {n E \left(\left| X \right|\right)}{n} = E \left(\left| X \right|\right).</equation>根据期望的定义，<equation>\begin{aligned} E (\mid X \mid) &= \int_ {- \infty} ^ {+ \infty} | x | \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} | x | \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \frac {x}{2 \sigma} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \sigma \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} = \sigma . \end{aligned}</equation>因此，<equation>E(\hat{\sigma}) = \sigma.</equation>下面计算<equation>D(\hat{\sigma})</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，且与总体<equation>X</equation>同分布，故<equation>D(\mid X_{i}\mid) = D(\mid X\mid)</equation>，<equation>i = 1, 2, \dots, n.</equation><equation>D (\hat {\sigma}) = D \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} \left| X _ {i} \right|\right) = \frac {1}{n ^ {2}} \cdot n D (\left| X \right|) = \frac {D (\left| X \right|)}{n}.</equation>根据方差的计算公式，<equation>D (| X |) = E \left(| X | ^ {2}\right) - \left[ E \left(| X |\right) \right] ^ {2} = E \left(X ^ {2}\right) - \left[ E \left(| X |\right) \right] ^ {2}.</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x ^ {2} \cdot \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= - \int_ {0} ^ {+ \infty} x ^ {2} \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x ^ {2} \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \cdot x \mathrm {d} x\right) \\ &= 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \stackrel {*} {=} 2 \sigma^ {2}. \end{aligned}</equation>于是，<equation>D ( \mid X \mid ) = 2 \sigma^{2} - \sigma^{2} = \sigma^{2}.</equation>因此，<equation>D(\hat{\sigma}) = \frac{D(|X|)}{n} = \frac{\sigma^2}{n}.</equation>

---

**2017年第23题 | 解答题 | 11分**


某工程师为了解一台天平的精度，用该天平对一物体的质量做 n次测量，该物体的质量<equation>\mu</equation>是已知的.设 n次测量结果<equation>X_{1},X_{2},\cdots,X_{n}</equation>相互独立且均服从正态分布<equation>N\left(\mu ,\sigma^{2}\right)</equation>，该工程师记录的是 n次测量的绝对误差<equation>Z_{i}=\left|X_{i}-\mu\right|(i=1,2,\cdots,n).</equation>利用<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>估计<equation>\sigma.</equation>I. 求<equation>Z_{1}</equation>的概率密度；

II. 利用一阶矩求<equation>\sigma</equation>的矩估计量；

III. 求<equation>\sigma</equation>的最大似然估计量.

**答案:**( I )<equation>f_{Z_{1}}(z)=\left\{\begin{array}{ll}\sqrt{\frac{2}{\pi}}\frac{1}{\sigma}\mathrm{e}^{-\frac{z^{2}}{2\sigma^{2}}},&z\geqslant0,\\ 0,&z<0;\end{array}\right.</equation>( II )<equation>\hat{\sigma}=\sqrt{\frac{\pi}{2}}\bar{Z};</equation>( III )<equation>\hat{\sigma}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}Z_{i}^{2}}.</equation>

**解析:**解（I）由题设知，<equation>X_{1}\sim N(\mu ,\sigma^{2})</equation>，从而<equation>\frac{X_{1}-\mu}{\sigma}\sim N(0,1).</equation>当 z < 0时，<equation>F_{Z_{1}}(z)=0.</equation>当<equation>z\geqslant 0</equation>时，<equation>\begin{array}{l} F _ {Z _ {1}} (z) = P \left\{Z _ {1} \leqslant z \right\} = P \left\{\left| X _ {1} - \mu \right| \leqslant z \right\} \\ = P \left\{\left| \frac {X _ {1} - \mu}{\sigma} \right| \leqslant \frac {z}{\sigma} \right\} = P \left\{- \frac {z}{\sigma} \leqslant \frac {X _ {1} - \mu}{\sigma} \leqslant \frac {z}{\sigma} \right\} \\ = 2 \Phi \left(\frac {z}{\sigma}\right) - 1, \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>为标准正态分布函数.

于是，<equation>Z_{1}</equation>的分布函数为<equation>F_{Z_{1}}(z) = \left\{ \begin{array}{ll} 2\Phi \left(\frac{z}{\sigma}\right) - 1, & z\geqslant 0, \\ 0, & z < 0. \end{array} \right.</equation>因此，<equation>Z_{1}</equation>的概率密度为<equation>f _ {Z _ {1}} (z) = F _ {Z _ {1}} ^ {\prime} (z) = \left\{ \begin{array}{l l} \frac {2}{\sigma} \varphi \left(\frac {z}{\sigma}\right), & z \geqslant 0, \\ 0, & z < 0 \end{array} = \left\{ \begin{array}{l l} \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}}, & z \geqslant 0, \\ 0, & z < 0, \end{array} \right. \right.</equation>其中<equation>\varphi (x)</equation>为标准正态分布的概率密度.

（Ⅱ）由于<equation>\begin{aligned} E \left(Z _ {1}\right) &= \int_ {- \infty} ^ {+ \infty} z f _ {Z _ {1}} (z) \mathrm {d} z = \int_ {0} ^ {+ \infty} z \cdot \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} z = \sqrt {\frac {2}{\pi}} \sigma \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} \left(\frac {z ^ {2}}{2 \sigma^ {2}}\right) \\ &= - \sqrt {\frac {2}{\pi}} \sigma \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \Bigg | _ {0} ^ {+ \infty} = \sqrt {\frac {2}{\pi}} \sigma , \end{aligned}</equation>故<equation>\sigma = \sqrt{\frac{\pi}{2}} E\left(Z_{1}\right)</equation>. 用<equation>\overline{Z} = \frac{1}{n}\sum_{i=1}^{n} Z_{i}</equation>代替<equation>E\left(Z_{1}\right)</equation>，得到<equation>\sigma</equation>的矩估计量<equation>\hat {\sigma} = \sqrt {\frac {\pi}{2}} \bar {Z}.</equation>（Ⅲ）设<equation>z_{1}, z_{2}, \dots, z_{n}</equation>是相应于<equation>Z_{1}, Z_{2}, \dots, Z_{n}</equation>的一组样本值，则似然函数为<equation>L (\sigma) = L \left(z _ {1}, z _ {2}, \dots , z _ {n}; \sigma\right) = \prod_ {i = 1} ^ {n} f _ {Z _ {i}} \left(z _ {i}\right) = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \frac {1}{\sigma^ {n}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right)}, & z _ {1} > 0, z _ {2} > 0, \dots , z _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>z_{1} > 0, z_{2} > 0, \dots, z_{n} > 0</equation>时，<equation>\ln L (\sigma) = \frac {n}{2} \ln \frac {2}{\pi} - n \ln \sigma - \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = 0</equation>，即<equation>-\frac{n}{\sigma} +\frac{1}{\sigma^3}\left(z_1^2 +z_2^2 +\dots +z_n^2\right) = 0</equation>，解得<equation>\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}z_i^2}</equation>.

因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}}.</equation>

---

**2015年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{1 - \theta}, & \theta \leqslant x \leqslant 1 \\ 0, & \text {其 他} \end{array} \right.</equation>其中<equation>\theta</equation>为未知参数.<equation>X_{1},X_{2},\cdots ,X_{n}</equation>为来自该总体的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**<equation>\begin{aligned} 2 3) (\mathrm {I}) \hat {\theta} &= 2 \bar {X} - 1; \\ (\mathrm {I I}) \hat {\theta} &= \min _ {1 \leqslant i \leqslant n} X _ {i}. \end{aligned}</equation>

**解析:**（ I ）由于<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x; \theta) \mathrm {d} x = \int_ {\theta} ^ {1} \frac {x}{1 - \theta} \mathrm {d} x = \frac {1 + \theta}{2},</equation>故<equation>\theta = 2 E ( X ) - 1.</equation>用样本均值<equation>\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>代替<equation>E ( X )</equation>，可得<equation>\theta</equation>的矩估计量<equation>\hat {\theta} = 2 \bar {X} - 1.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant \min _ {1 \leqslant i \leqslant n} x _ {i}, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>又由于<equation>\frac{1}{(1-\theta)^{n}}</equation>是关于<equation>\theta</equation>的单调增加函数，故当<equation>\theta=\min_{1\leqslant i\leqslant n}x_{i}</equation>时，<equation>L(\theta)</equation>取值最大因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}.</equation>

---

**2013年第23题 | 解答题 | 11分**

23. (本题满分11分)

设总体 X的概率密度为 f(x;<equation>\theta)=\left\{\begin{array}{ll}\frac{\theta^{2}}{x^{3}} \mathrm{e}^{-\frac{\theta}{x}},&x>0,\\ 0,&\mathrm{其他},\end{array} \right.</equation>其中<equation>\theta</equation>为未知参数且大于零.<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**(23) （ I ）<equation>\hat{\theta}=\overline{X};</equation>(Ⅱ)<equation>\hat{\theta}=\frac{2 n}{\sum_{i=1}^{n}\frac{1}{X_{i}}}.</equation>

**解析:**解（I）由题设知，<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} x \cdot \frac {\theta^ {2}}{x ^ {3}} \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} x = \int_ {0} ^ {+ \infty} \frac {\theta^ {2}}{x ^ {2}} \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} x = \int_ {0} ^ {+ \infty} \theta \mathrm {e} ^ {- \frac {\theta}{x}} \mathrm {d} \left(- \frac {\theta}{x}\right) \\ \underline {{\underline {{t}} = - \frac {\theta}{x}}} \int_ {- \infty} ^ {0} \theta \mathrm {e} ^ {t} \mathrm {d} t &= \theta \mathrm {e} ^ {t} \Big | _ {- \infty} ^ {0} = \theta , \end{aligned}</equation>即<equation>\theta = E(X)</equation>. 以<equation>\overline{X} = \frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>代替<equation>E(X)</equation>, 得到<equation>\theta</equation>的矩估计量<equation>\hat{\theta} = \overline{X}</equation>.

（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则关于<equation>\theta</equation>的似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {\theta^ {2 n}}{\left(x _ {1} x _ {2} \cdots x _ {n}\right) ^ {3}} \mathrm {e} ^ {- \theta \left(\frac {1}{x _ {1}} + \frac {1}{x _ {2}} + \cdots + \frac {1}{x _ {n}}\right)}, & x _ {1} > 0, x _ {2} > 0, \dots , x _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>x_{1} > 0,x_{2} > 0,\dots ,x_{n} > 0</equation>时，<equation>\ln L (\theta) = 2 n \ln \theta - 3 \ln \left(x _ {1} x _ {2} \dots x _ {n}\right) - \theta \left(\frac {1}{x _ {1}} + \frac {1}{x _ {2}} + \dots + \frac {1}{x _ {n}}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\theta)]}{\mathrm{d}\theta} = 0</equation>，即<equation>\frac{2n}{\theta} - \left(\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}\right) = 0</equation>，解得<equation>\theta = \frac{2n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}}.</equation>因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \frac {2 n}{\frac {1}{X _ {1}} + \frac {1}{X _ {2}} + \cdots + \frac {1}{X _ {n}}} = \frac {2 n}{\sum_ {i = 1} ^ {n} \frac {1}{X _ {i}}}.</equation>

---

**2012年第23题 | 解答题 | 11分**


设随机变量 X与 Y相互独立且分别服从正态分布<equation>N\left(\mu,\sigma^{2}\right)</equation>与<equation>N\left(\mu,2\sigma^{2}\right)</equation>，其中<equation>\sigma</equation>是未知参数且<equation>\sigma >0</equation>记<equation>Z=X-Y.</equation>I. 求 Z的概率密度<equation>f\left(z;\sigma^{2}\right)</equation>；

II. 设<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>为来自总体 Z的简单随机样本，求<equation>\sigma^{2}</equation>的最大似然估计量<equation>\hat{\sigma}^{2}</equation>；

III. 证明<equation>\hat{\sigma}^{2}</equation>为<equation>\sigma^{2}</equation>的无偏估计量.

**答案:**(23) ( I )<equation>f ( z ; \sigma^{2} )=\frac{1}{\sqrt{6 \pi} \sigma}\mathrm{e}^{-\frac{z^{2}}{6 \sigma^{2}}},-\infty<z<+\infty;</equation>（Ⅱ）<equation>\widehat{\sigma^{2}}=\frac{1}{3n}\sum_{i=1}^{n}Z_{i}^{2};</equation>（Ⅲ）证明略.

**解析:**（I）由于相互独立且服从正态分布的随机变量的线性组合仍服从正态分布，且<equation>E (Z) = E (X) - E (Y) = \mu - \mu = 0,</equation><equation>D (Z) = D (X - Y) = D (X) + D (Y) = \sigma^ {2} + 2 \sigma^ {2} = 3 \sigma^ {2},</equation>故<equation>Z\sim N(0,3\sigma^{2})</equation>，从而Z的概率密度<equation>f \left(z; \sigma^ {2}\right) = \frac {1}{\sqrt {2 \pi} \sqrt {3 \sigma^ {2}}} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \cdot 3 \sigma^ {2}}} = \frac {1}{\sqrt {6 \pi} \sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{6 \sigma^ {2}}}, - \infty < z < + \infty .</equation>（Ⅱ）设<equation>z_{1}, z_{2}, \dots, z_{n}</equation>是来自于样本<equation>Z_{1}, Z_{2}, \dots, Z_{n}</equation>的一个样本值，则似然函数为<equation>L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} f \left(z _ {i}; \sigma^ {2}\right) = (6 \pi) ^ {- \frac {n}{2}} \cdot \left(\sigma^ {2}\right) ^ {- \frac {n}{2}} \mathrm {e} ^ {- \frac {z _ {1} ^ {2} + z _ {2} ^ {2} + \cdots + z _ {n} ^ {2}}{6 \sigma^ {2}}}.</equation>取对数得<equation>\ln L \left(\sigma^ {2}\right) = - \frac {n}{2} \ln (6 \pi) - \frac {n}{2} \ln \sigma^ {2} - \frac {z _ {1} ^ {2} + z _ {2} ^ {2} + \cdots + z _ {n} ^ {2}}{6 \sigma^ {2}}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L(\sigma^{2})\right]}{\mathrm{d}(\sigma^{2})}=0</equation>即有<equation>-\frac{n}{2\sigma^{2}}+\frac{z_{1}^{2}+z_{2}^{2}+\cdots+z_{n}^{2}}{6(\sigma^{2})^{2}}=0</equation>解得<equation>\sigma^{2}=\frac{z_{1}^{2}+z_{2}^{2}+\cdots+z_{n}^{2}}{3n}.</equation>于是<equation>\sigma^{2}</equation>的最大似然估计量为<equation>\widehat {\sigma^ {2}} = \frac {Z _ {1} ^ {2} + Z _ {2} ^ {2} + \cdots + Z _ {n} ^ {2}}{3 n} = \frac {1}{3 n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}.</equation>（Ⅲ）由于<equation>E \left(\widehat {\sigma^ {2}}\right) = E \left(\frac {1}{3 n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}\right) = \frac {1}{3} E \left(Z ^ {2}\right) = \frac {1}{3} \left[ D (Z) + \left(E (Z)\right) ^ {2} \right] = \frac {3 \sigma^ {2}}{3} = \sigma^ {2},</equation>故<equation>\widehat{\sigma^2}</equation>为<equation>\sigma^2</equation>的无偏估计量，结论得证.

---

**2011年第23题 | 解答题 | 11分**


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自正态总体<equation>N\left(\mu_{0},\sigma^{2}\right)</equation>的简单随机样本，其中<equation>\mu_{0}</equation>已知，<equation>\sigma^{2}>0</equation>未知，<equation>\bar{X}</equation>和<equation>S^{2}</equation>分别表示样本均值和样本方差.

I. 求参数<equation>\sigma^{2}</equation>的最大似然估计<equation>\hat{\sigma}^{2}</equation>；

II. 计算<equation>E(\hat{\sigma}^{2})</equation>和<equation>D(\hat{\sigma}^{2})</equation>

**答案:**(23) (I)<equation>\hat{\sigma}^{2} = \frac{1}{n}\sum_{i=1}^{n}\left(X_{i} - \mu_{0}\right)^{2}</equation>;<equation>(\mathrm {I I}) E \left(\widehat {\sigma^ {2}}\right) = \sigma^ {2}, D \left(\widehat {\sigma^ {2}}\right) = \frac {2 \sigma^ {4}}{n}.</equation>

**解析:**解（I）设 X为正态总体，<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一个样本值.由<equation>X\sim N(\mu_{0},\sigma^{2})</equation>知，X的概率密度为<equation>f \left(x; \mu_ {0}, \sigma^ {2}\right) = \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {\left(x - \mu_ {0}\right) ^ {2}}{2 \sigma^ {2}}},</equation>从而似然函数为<equation>L \left(\sigma^ {2}\right) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \mathrm {e} ^ {- \frac {\left(x _ {i} - \mu_ {0}\right) ^ {2}}{2 \sigma^ {2}}} = \left(2 \pi\right) ^ {- \frac {n}{2}} \left(\sigma^ {2}\right) ^ {- \frac {n}{2}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} \left(x _ {i} - \mu_ {0}\right) ^ {2}},</equation>两边取对数得<equation>\ln L \left(\sigma^ {2}\right) = - \frac {n}{2} \ln 2 \pi - \frac {n}{2} \ln \sigma^ {2} - \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} \left(x _ {i} - \mu_ {0}\right) ^ {2}.</equation>令<equation>\frac{\mathrm{d}\left[\ln L\left(\sigma^{2}\right)\right]}{\mathrm{d}\left(\sigma^{2}\right)} = 0</equation>，即有<equation>-\frac{n}{2\sigma^2} +\frac{1}{2\left(\sigma^2\right)^2}\sum_{i=1}^{n}\left(x_{i} - \mu_{0}\right)^{2} = 0</equation>（注意这里是关于<equation>\sigma^2</equation>求导），解得<equation>\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}\left(x_{i} - \mu_{0}\right)^{2}</equation>.于是参数<equation>\sigma^2</equation>的最大似然估计为<equation>\widehat {\sigma^ {2}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(X _ {i} - \mu_ {0}\right) ^ {2}.</equation>（Ⅱ）（法一）由于<equation>X_{i}\sim N(\mu_{0},\sigma^{2})</equation>，故<equation>\frac{X_{i} - \mu_{0}}{\sigma}\sim N(0,1),i = 1,2,\dots,n</equation>，从而由（I）知，<equation>\frac {n \widehat {\sigma^ {2}}}{\sigma^ {2}} = \sum_ {i = 1} ^ {n} \frac {\left(X _ {i} - \mu_ {0}\right) ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n).</equation>于是<equation>E\left(\frac{n\widehat{\sigma}^{2}}{\sigma^{2}}\right)=n,D\left(\frac{n\widehat{\sigma}^{2}}{\sigma^{2}}\right)=2n</equation>，即有<equation>E \left(\widehat {\sigma^ {2}}\right) = \sigma^ {2}, \quad D \left(\widehat {\sigma^ {2}}\right) = \frac {2 \sigma^ {4}}{n}.</equation>（法二）由（I）知，<equation>E \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n} \sum_ {i = 1} ^ {n} E \left[ \left(X _ {i} - \mu_ {0}\right) ^ {2} \right] = E \left[ \left(X - \mu_ {0}\right) ^ {2} \right] \xlongequal {\text {方 差 的 定 义}} D (X) = \sigma^ {2}.</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，故<equation>(X_{1} - \mu_{0})^{2}, (X_{2} - \mu_{0})^{2}, \dots, (X_{n} - \mu_{0})^{2}</equation>相互独立，从而<equation>D \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} D \left[ \left(X _ {i} - \mu_ {0}\right) ^ {2} \right] = \frac {1}{n} D \left[ \left(X - \mu_ {0}\right) ^ {2} \right].</equation>又<equation>X\sim N(\mu_{0},\sigma^{2})</equation>，故<equation>\frac{X-\mu_{0}}{\sigma}\sim N(0,1)</equation>，从而<equation>\frac{(X-\mu_{0})^{2}}{\sigma^{2}}\sim \chi^{2}(1),D\left[ \frac{(X-\mu_{0})^{2}}{\sigma^{2}}\right] = 2.</equation>于是<equation>D \left(\widehat {\sigma^ {2}}\right) = \frac {1}{n} D \left[ \left(X - \mu_ {0}\right) ^ {2} \right] = \frac {1}{n} \cdot 2 \sigma^ {4} = \frac {2 \sigma^ {4}}{n}.</equation>综上所述，<equation>E(\widehat{\sigma^{2}}) = \sigma^{2}, D(\widehat{\sigma^{2}}) = \frac{2\sigma^{4}}{n}.</equation>

---

**2009年第23题 | 解答题 | 11分**

23. (本题满分11分)

设总体 X的概率密度为<equation>f ( x )=\left\{\begin{array}{ll}\lambda^{2} x \mathrm{e}^{- \lambda x},&x>0,\\0,&\mathrm {其 他},\end{array} \right.</equation>其中参数<equation>\lambda(\lambda>0)</equation>未知，<equation>X_{1},X_{2},\cdots,X_{n}</equation>是来自总体 X的简单随机样本.

I. 求参数<equation>\lambda</equation>的矩估计量;

II. 求参数<equation>\lambda</equation>的最大似然估计量.

**答案:**(23) (I)<equation>\lambda</equation>的矩估计量为<equation>\hat{\lambda} = \frac{2}{\bar{X}}</equation>; (II)<equation>\lambda</equation>的最大似然估计量为<equation>\hat{\lambda} = \frac{2}{\bar{X}}</equation>.

**解析:**（I）由题设知，<equation>\begin{aligned} E (X) &= \int_ {0} ^ {+ \infty} \lambda^ {2} x ^ {2} \mathrm {e} ^ {- \lambda x} \mathrm {d} x \xlongequal {t = \lambda x} \frac {1}{\lambda} \int_ {0} ^ {+ \infty} t ^ {2} \mathrm {e} ^ {- t} \mathrm {d} t \\ &= \frac {1}{\lambda} \left(- \mathrm {e} ^ {- t} \cdot t ^ {2} \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} 2 t \mathrm {e} ^ {- t} \mathrm {d} t\right) = \frac {2}{\lambda} \int_ {0} ^ {+ \infty} t \mathrm {e} ^ {- t} \mathrm {d} t \\ &= \frac {2}{\lambda} \left(- \mathrm {e} ^ {- t} \cdot t \Big | _ {0} ^ {+ \infty} + \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- t} \mathrm {d} t\right) = \frac {2}{\lambda}. \end{aligned}</equation>于是<equation>\lambda = \frac{2}{E(X)}</equation>，用<equation>\overline{X} = \frac{1}{n}\sum_{i=1}^{n} X_{i}</equation>代替<equation>E(X)</equation>，得到参数<equation>\lambda</equation>的矩估计量为<equation>\hat {\lambda} = \frac {2}{\bar {X}}.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一个样本值，则似然函数为<equation>L (\lambda)=L \left(x_{1}, x_{2}, \dots, x_{n}; \lambda\right)=\prod_{i=1}^{n} f \left(x_{i}; \lambda\right)=\left\{ \begin{array}{l l} \lambda^{2 n} x_{1} x_{2} \dots x_{n} \mathrm{e}^{- \lambda \left(x_{1}+x_{2}+\dots+x_{n}\right)}, & x_{1}>0, x_{2}>0, \dots, x_{n}>0, \\ 0, & \text{其他}. \end{array} \right.</equation>当<equation>x_{1}>0, x_{2}>0, \dots, x_{n}>0</equation>时，<equation>\ln L (\lambda)=\ln \left(x_{1} x_{2} \dots x_{n}\right)+2 n \ln \lambda-\lambda \left(x_{1}+x_{2}+\dots+x_{n}\right).</equation><equation>\frac{\mathrm{d}[\ln L(\lambda)]}{\mathrm{d}\lambda}=0</equation>即<equation>\frac{2 n}{\lambda}-\left(x_{1}+x_{2}+\dots+x_{n}\right)=0</equation>解得<equation>\lambda=\frac{2 n}{x_{1}+x_{2}+\dots+x_{n}}.</equation>于是参数<equation>\lambda</equation>的最大似然估计量为<equation>\hat {\lambda} = \frac {2 n}{X _ {1} + X _ {2} + \cdots + X _ {n}} = \frac {2 n}{n \bar {X}} = \frac {2}{\bar {X}}.</equation>

---


# 数学三


## 高等数学


### 函数、极限、连续


