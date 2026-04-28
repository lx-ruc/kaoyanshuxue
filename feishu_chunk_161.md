---

**2018年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \sigma) = \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}}, (- \infty < x < + \infty).</equation>其中<equation>\sigma \in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本.记<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}.</equation>I. 求<equation>\hat{\sigma}</equation>;

II. 求<equation>E(\hat{\sigma}),D(\hat{\sigma}).</equation>

**答案:**（I）<equation>\sigma</equation>的最大似然估计量为<equation>\hat{\sigma}=\frac{\sum_{i=1}^{n} \mid X_{i}\mid}{n}；</equation>（Ⅱ）<equation>E(\hat{\sigma})=\sigma</equation>，<equation>D(\hat{\sigma})=\frac{\sigma^{2}}{n}.</equation>

**解析:**解（ I ）设<equation>x_{1}, x_{2}, \dots , x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots , X_{n}</equation>的一组样本值.似然函数为<equation>L (\sigma) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \sigma\right) = \frac {1}{2 ^ {n} \sigma^ {n}} \mathrm {e} ^ {- \frac {\left| x _ {1} \right| + \left| x _ {2} \right| + \cdots + \left| x _ {n} \right|}{\sigma}}, - \infty < x _ {i} < + \infty , i = 1, 2, \dots , n.</equation>对 L（<equation>\sigma</equation>）取对数，得<equation>\ln L (\sigma) = - \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} \right|}{\sigma} - n \ln (2 \sigma).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma}=\frac{\sum_{i=1}^{n} \mid x_{i}\mid}{\sigma^{2}}-\frac{n}{\sigma}=0</equation>即<equation>\sum_{i=1}^{n} \mid x_{i}\mid-n\sigma=0</equation>解得<equation>\sigma=\frac{\sum_{i=1}^{n} \mid x_{i}\mid}{n}.</equation>因此，<equation>\sigma</equation>的最大似然估计量为<equation>\hat {\sigma} = \frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}.</equation>（Ⅱ）由于<equation>X_{1}, X_{2}, \dots , X_{n}</equation>为来自总体X的简单随机样本，故它们相互独立，且与总体X同分布<equation>E(X_{i})=E(X), E(|X_{i}|)=E(|X|), i=1,2,\dots ,n.</equation>根据期望的线性性质，<equation>E (\hat {\sigma}) = E \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {\sum_ {i = 1} ^ {n} E \left(\left| X _ {i} \right|\right)}{n} = \frac {n E \left(\left| X \right|\right)}{n} = E (\left| X \right|).</equation>根据期望的定义，<equation>\begin{aligned} E (\mid X \mid) &= \int_ {- \infty} ^ {+ \infty} | x | \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} | x | \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = 2 \int_ {0} ^ {+ \infty} \frac {x}{2 \sigma} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \int_ {0} ^ {+ \infty} x \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x\right) \\ &= \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x = - \sigma \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} = \sigma . \end{aligned}</equation>因此，<equation>E(\hat{\sigma}) = \sigma .</equation>下面计算<equation>D(\hat{\sigma})。</equation>由于<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立，且与总体<equation>X</equation>同分布，故<equation>D(\mid X_{i}\mid) = D(\mid X\mid)</equation>，<equation>i = 1, 2, \dots, n.</equation><equation>D (\hat {\sigma}) = D \left(\frac {\sum_ {i = 1} ^ {n} \left| X _ {i} \right|}{n}\right) = \frac {1}{n ^ {2}} D \left(\sum_ {i = 1} ^ {n} \left| X _ {i} \right|\right) = \frac {1}{n ^ {2}} \cdot n D (\mid X \mid) = \frac {D (\mid X \mid)}{n}.</equation>根据方差的计算公式，<equation>D (\mid X \mid) = E \left(\mid X \mid^ {2}\right) - \left[ E (\mid X \mid) \right] ^ {2} = E \left(X ^ {2}\right) - \left[ E (\mid X \mid) \right] ^ {2}.</equation><equation>\begin{aligned} E \left(X ^ {2}\right) &= \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot f (x; \sigma) \mathrm {d} x = \int_ {- \infty} ^ {+ \infty} x ^ {2} \cdot \frac {1}{2 \sigma} \mathrm {e} ^ {- \frac {| x |}{\sigma}} \mathrm {d} x = \frac {1}{\sigma} \int_ {0} ^ {+ \infty} x ^ {2} \cdot \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \\ &= - \int_ {0} ^ {+ \infty} x ^ {2} \mathrm {d} \left(\mathrm {e} ^ {- \frac {x}{\sigma}}\right) = - \left(x ^ {2} \mathrm {e} ^ {- \frac {x}{\sigma}} \Big | _ {0} ^ {+ \infty} - 2 \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {x}{\sigma}} \cdot x \mathrm {d} x\right) \\ &= 2 \int_ {0} ^ {+ \infty} x \mathrm {e} ^ {- \frac {x}{\sigma}} \mathrm {d} x \stackrel {*} {=} 2 \sigma^ {2}. \end{aligned}</equation>于是，<equation>D ( \mid X \mid ) = 2 \sigma^{2} - \sigma^{2} = \sigma^{2}.</equation>因此，<equation>D(\hat{\sigma}) = \frac{D(|X|)}{n} = \frac{\sigma^{2}}{n}.</equation>

---

**2017年第23题 | 解答题 | 11分**


某工程师为了解一台天平的精度，用该天平对一物体的质量做 n次测量，该物体的质量<equation>\mu</equation>是已知的，设 n次测量结果<equation>X_{1},X_{2},\cdots ,X_{n}</equation>相互独立且均服从正态分布<equation>N\left(\mu ,\sigma^{2}\right).</equation>该工程师记录的是 n次测量的绝对误差<equation>Z_{i}=\left|X_{i}-\mu\right|(i=1,2,\cdots,n),</equation>利用<equation>Z_{1},Z_{2},\cdots,Z_{n}</equation>估计<equation>\sigma.</equation>I. 求<equation>Z_{1}</equation>的概率密度；

II. 利用一阶矩求<equation>\sigma</equation>的矩估计量；

III. 求<equation>\sigma</equation>的最大似然估计量.

**答案:**( I )<equation>f_{Z_{1}}(z) = \left\{ \begin{array}{ll} \sqrt{\frac{2}{\pi}} \frac{1}{\sigma} \mathrm{e}^{-\frac{z^{2}}{2\sigma^{2}}}, & z \geqslant 0, \\ 0, & z < 0; \end{array} \right.</equation>( II )<equation>\hat{\sigma} = \sqrt{\frac{\pi}{2}} \bar{Z}</equation>;

( III )<equation>\hat{\sigma} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} Z_{i}^{2}}</equation>.

**解析:**解（I）由题设知，<equation>X_{1}\sim N(\mu ,\sigma^{2})</equation>，从而<equation>\frac{X_{1}-\mu}{\sigma}\sim N(0,1).</equation>当 z < 0时，<equation>F_{Z_{1}}(z)=0.</equation>当<equation>z\geqslant0</equation>时，<equation>\begin{array}{l} F _ {Z _ {1}} (z) = P \left\{Z _ {1} \leqslant z \right\} = P \left\{\mid X _ {1} - \mu \mid \leqslant z \right\} \\ = P \left\{\left| \frac {X _ {1} - \mu}{\sigma} \right| \leqslant \frac {z}{\sigma} \right\} = P \left\{- \frac {z}{\sigma} \leqslant \frac {X _ {1} - \mu}{\sigma} \leqslant \frac {z}{\sigma} \right\} \\ = 2 \Phi \left(\frac {z}{\sigma}\right) - 1, \\ \end{array}</equation>其中<equation>\varPhi(x)</equation>为标准正态分布函数.

于是，<equation>Z_{1}</equation>的分布函数为<equation>F_{Z_{1}}(z)=\left\{ \begin{array}{ll} 2\Phi \left(\frac{z}{\sigma}\right)-1, & z\geqslant 0, \\ 0, & z<0. \end{array} \right.</equation>因此，<equation>Z_{1}</equation>的概率密度为<equation>f _ {Z _ {1}} (z) = F _ {Z _ {1}} ^ {\prime} (z) = \left\{ \begin{array}{l l} \frac {2}{\sigma} \varphi \left(\frac {z}{\sigma}\right), & z \geqslant 0, \\ 0, & z < 0 \end{array} = \left\{ \begin{array}{l l} \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}}, & z \geqslant 0, \\ 0, & z < 0, \end{array} \right. \right.</equation>其中<equation>\varphi(x)</equation>为标准正态分布的概率密度.

（Ⅱ）由于<equation>\begin{array}{l} E \left(Z _ {1}\right) = \int_ {- \infty} ^ {+ \infty} z f _ {Z _ {1}} (z) \mathrm {d} z = \int_ {0} ^ {+ \infty} z \cdot \sqrt {\frac {2}{\pi}} \frac {1}{\sigma} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} z = \sqrt {\frac {2}{\pi}} \sigma \int_ {0} ^ {+ \infty} \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \mathrm {d} \left(\frac {z ^ {2}}{2 \sigma^ {2}}\right) \\ = - \sqrt {\frac {2}{\pi}} \sigma \mathrm {e} ^ {- \frac {z ^ {2}}{2 \sigma^ {2}}} \Big | _ {0} ^ {+ \infty} = \sqrt {\frac {2}{\pi}} \sigma , \\ \end{array}</equation>故<equation>\sigma=\sqrt{\frac{\pi}{2}} E(Z_{1})</equation>用<equation>\overline{Z}=\frac{1}{n}\sum_{i=1}^{n} Z_{i}</equation>代替<equation>E(Z_{1})</equation>，得到<equation>\sigma</equation>的矩估计量<equation>\hat {\sigma} = \sqrt {\frac {\pi}{2}} \bar {Z}.</equation>（Ⅲ）设<equation>z_{1}, z_{2}, \dots , z_{n}</equation>是相应于<equation>Z_{1}, Z_{2}, \dots , Z_{n}</equation>的一组样本值，则似然函数为<equation>L (\sigma) = L \left(z _ {1}, z _ {2}, \dots , z _ {n}; \sigma\right) = \prod_ {i = 1} ^ {n} f _ {Z _ {i}} \left(z _ {i}\right) = \left\{ \begin{array}{l l} \left(\frac {2}{\pi}\right) ^ {\frac {n}{2}} \frac {1}{\sigma^ {n}} \mathrm {e} ^ {- \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right)}, & z _ {1} > 0, z _ {2} > 0, \dots , z _ {n} > 0, \\ 0, & \text {其 他}. \end{array} \right.</equation>当<equation>z_{1} > 0, z_{2} > 0, \dots, z_{n} > 0</equation>时，<equation>\ln L (\sigma) = \frac {n}{2} \ln \frac {2}{\pi} - n \ln \sigma - \frac {1}{2 \sigma^ {2}} \left(z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {n} ^ {2}\right).</equation>令<equation>\frac{\mathrm{d}[\ln L(\sigma)]}{\mathrm{d}\sigma} = 0</equation>，即<equation>-\frac{n}{\sigma} +\frac{1}{\sigma^3}\left(z_1^2 +z_2^2 +\dots +z_n^2\right) = 0</equation>，解得<equation>\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}z_i^2}</equation><equation>\sigma</equation><equation>\hat {\sigma} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} Z _ {i} ^ {2}}.</equation>

---

**2015年第23题 | 解答题 | 11分**


设总体<equation>X</equation>的概率密度为<equation>f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{1 - \theta}, & \theta \leqslant x \leqslant 1, \\ 0, & \text {其 他}, \end{array} \right.</equation>其中<equation>\theta</equation>为未知参数.<equation>X_{1},X_{2},\cdots ,X_{n}</equation>为来自该总体的简单随机样本.

I. 求<equation>\theta</equation>的矩估计量;

II. 求<equation>\theta</equation>的最大似然估计量.

**答案:**<equation>\begin{array}{l} (2 3) (\mathrm {I}) \hat {\theta} = 2 \bar {X} - 1; \\ (\mathrm {I I}) \hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}. \\ \end{array}</equation>

**解析:**（ I ）由于<equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x; \theta) \mathrm {d} x = \int_ {\theta} ^ {1} \frac {x}{1 - \theta} \mathrm {d} x = \frac {1 + \theta}{2},</equation>故<equation>\theta = 2 E ( X ) - 1.</equation>用样本均值<equation>\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}</equation>代替<equation>E ( X )</equation>，可得<equation>\theta</equation>的矩估计量<equation>\hat {\theta} = 2 \bar {X} - 1.</equation>（Ⅱ）设<equation>x_{1}, x_{2}, \dots, x_{n}</equation>是相应于样本<equation>X_{1}, X_{2}, \dots, X_{n}</equation>的一组样本值，则似然函数为<equation>L (\theta) = \prod_ {i = 1} ^ {n} f \left(x _ {i}; \theta\right) = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant 1, \\ 0, & \text {其 他} \end{array} = \left\{ \begin{array}{l l} \frac {1}{(1 - \theta) ^ {n}}, & \theta \leqslant \min _ {1 \leqslant i \leqslant n} x _ {i}, \\ 0, & \text {其 他}. \end{array} \right. \right.</equation>又由于<equation>\frac{1}{(1-\theta)^{n}}</equation>是关于<equation>\theta</equation>的单调增加函数，故当<equation>\theta=\min_{1\leqslant i\leqslant n}x_{i}</equation>时，<equation>L(\theta)</equation>取值最大因此，<equation>\theta</equation>的最大似然估计量为<equation>\hat {\theta} = \min _ {1 \leqslant i \leqslant n} X _ {i}.</equation>

---


**2024年第22题 | 解答题 | 12分**


设总体 X服从<equation>[0,\theta]</equation>上的均匀分布，<equation>\theta\in(0,+\infty)</equation>为未知参数，<equation>X_{1},X_{2},\cdots,X_{n}</equation>为来自总体 X的简单随机样本，记为<equation>X_{(n)}=\max\{X_{1},X_{2},\cdots,X_{n}\}, T_{c}=cX_{(n)}.</equation>I. 求 c，使得<equation>E\left(T_{c}\right)=\theta;</equation>II. 记 h(c)=E<equation>[\left(T_{c}-\theta\right)^{2}]</equation>，求 c使得 h(c)最小.

**答案:**(1)<equation>c=\frac{n+1}{n}.</equation>(2)<equation>c=\frac{n+2}{n+1}</equation>时，<equation>h(c)</equation>取最小值.

**解析:**（I）由于 X服从<equation>[0,\theta]</equation>上的均匀分布，故 X的分布函数为<equation>F _ {X} (x) = \left\{ \begin{array}{l l} 0, & x < 0, \\ \frac {x}{\theta}, & 0 \leqslant x < \theta , \\ 1, & x \geqslant \theta . \end{array} \right.</equation>记随机变量<equation>Y = X_{(n)} = \max \left|X_{1},X_{2},\dots ,X_{n}\right|</equation>. 计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>当<equation>y < 0</equation>时，<equation>F_{Y}(y) = 0.</equation>当<equation>0\leqslant y < \theta</equation>时，<equation>\begin{array}{l} F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\max _ {1 \leqslant i \leqslant n} X _ {i} \leqslant y \right\} = P \left\{X _ {1} \leqslant y, X _ {2} \leqslant y, \dots , X _ {n} \leqslant y \right\} \\ \underline {{\text {独立 性}}} P \left\{X _ {1} \leqslant y \right\} P \left\{X _ {2} \leqslant y \right\} \dots P \left\{X _ {n} \leqslant y \right\} = F _ {X} ^ {n} (y) = \left(\frac {y}{\theta}\right) ^ {n}. \\ \end{array}</equation>当<equation>y\geqslant \theta</equation>时，<equation>F_{Y}(y) = 1.</equation>于是，<equation>F_{Y}(y) = \left\{ \begin{array}{ll} 0, & y < 0, \\ \left(\frac{y}{\theta}\right)^{n}, & 0 \leqslant y < \theta , \\ 1, & y \geqslant \theta . \end{array} \right.</equation>对<equation>F_{\gamma}(y)</equation>求导，可得<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y) = \left\{ \begin{array}{l l} \frac {n y ^ {n - 1}}{\theta^ {n}}, & 0 < y < \theta , \\ 0, & \text {其 他}. \end{array} \right.</equation>因此，<equation>\begin{aligned} E \left(T _ {c}\right) &= E (c Y) = c \int_ {- \infty} ^ {+ \infty} y \cdot f _ {Y} (y) \mathrm {d} y = c \int_ {0} ^ {\theta} y \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = c \cdot \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 1}}{n + 1} \Bigg | _ {0} ^ {\theta} \\ &= \frac {c n}{n + 1} \theta . \end{aligned}</equation>若<equation>E\left(T_{c}\right) = \theta</equation>，则<equation>\frac{cn}{n + 1}\theta = \theta</equation>，解得<equation>c = \frac{n + 1}{n}</equation>.

（Ⅱ）展开 h（c）可得<equation>h (c) = E \left[ \left(T _ {c} - \theta\right) ^ {2} \right] = E \left[ \left(c Y - \theta\right) ^ {2} \right] = c ^ {2} E \left(Y ^ {2}\right) - 2 c \theta E (Y) + \theta^ {2}.</equation>计算<equation>E ( Y^{2})</equation><equation>E \left(Y ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} y ^ {2} \cdot f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {\theta} y ^ {2} \cdot \frac {n y ^ {n - 1}}{\theta^ {n}} \mathrm {d} y = \frac {n}{\theta^ {n}} \cdot \frac {y ^ {n + 2}}{n + 2} \Bigg | _ {0} ^ {\theta} = \frac {n}{n + 2} \theta^ {2}.</equation>于是，<equation>h (c) = c ^ {2} \cdot \frac {n}{n + 2} \theta^ {2} - 2 c \cdot \frac {n}{n + 1} \theta^ {2} + \theta^ {2} = \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right) \theta^ {2}.</equation>令<equation>\frac{\mathrm{d}[h(c)]}{\mathrm{d}c}=\left(\frac{2 n}{n+2} c-\frac{2 n}{n+1}\right)\theta^{2}=0</equation>，解得 c =<equation>\frac{n+2}{n+1}.</equation>该点是 h(c）的唯一驻点. 又因为<equation>h^{\prime \prime}(c)=\frac{2 n}{n+2}\theta^{2}>0</equation>，所以该唯一驻点是 h(c）的极小值点，也是最小值点.

因此，当<equation>c=\frac{n+2}{n+1}</equation>时，<equation>h(c)</equation>最小.

---

**2023年第8题 | 选择题 | 5分 | 答案: C**

8. 设随机变量<equation>X</equation>服从参数为1的泊松分布，则<equation>E[|X - E(X)|] = (\quad)</equation>A.<equation>\frac{1} {\mathrm{e}}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2} {\mathrm{e}}</equation>D. 1

答案: C

**解析:**由于 X服从参数为1的泊松分布，故<equation>E ( X )=1.</equation>从而<equation>| X - E (X) | = | X - 1 | = \left\{ \begin{array}{l l} 1, & X = 0, \\ X - 1, & X = 1, 2, \dots . \end{array} \right.</equation>由参数为1的泊松分布的分布律可知，<equation>P\{X = 0\} = \frac{1^{0}\cdot\mathrm{e}^{-1}}{0!} = \frac{1}{\mathrm{e}}.</equation>根据数学期望的定义，<equation>\begin{aligned} E [ \mid X - E (X) \mid ] &= 1 \cdot P \{X = 0 \} + \sum_ {k = 1} ^ {\infty} (k - 1) P \{X = k \} \\ &= \frac {1}{\mathrm {e}} + \sum_ {k = 0} ^ {\infty} (k - 1) P \{X = k \} - (0 - 1) P \{X = 0 \} \\ &= \frac {1}{\mathrm {e}} + E (X - 1) + \frac {1}{\mathrm {e}} = \frac {1}{\mathrm {e}} + E (X) - 1 + \frac {1}{\mathrm {e}} \\ \underline {{\underline {{E (X) = 1}}}} \frac {2}{\mathrm {e}}. \end{aligned}</equation>因此，应选C.

---

**2023年第22题 | 解答题 | 12分**

22. (本题满分12分)

设随机变量 X的概率密度为<equation>f ( x )=\frac{\mathrm{e}^{x}}{\left( 1+\mathrm{e}^{x}\right)^{2}},-\infty<x<+\infty</equation>，令<equation>Y=\mathrm{e}^{X}.</equation>I. 求 X的分布函数;

II. 求 Y的概率密度;

III. Y的数学期望是否存在?

**答案:**（I）<equation>X</equation>的分布函数<equation>F_{X}(x)=\frac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}};</equation>（Ⅱ）<equation>Y</equation>的概率密度为<equation>f_{Y}(y)=\left\{\begin{array}{ll}\frac{1}{(1+y)^{2}},&y>0,\\ 0,&y\leqslant 0.\end{array}\right.</equation>（Ⅲ）Y的数学期望不存在.

**解析:**解（ I ）记 X的分布函数为<equation>F_{X}(x).</equation>由概率密度的定义可知，<equation>F _ {X} (x) = \int_ {- \infty} ^ {x} f (t) \mathrm {d} t = \int_ {- \infty} ^ {x} \frac {\mathrm {e} ^ {t}}{\left(1 + \mathrm {e} ^ {t}\right) ^ {2}} \mathrm {d} t \xlongequal {=} \int_ {0} ^ {\mathrm {e} ^ {x}} \frac {\mathrm {d} u}{\left(1 + u\right) ^ {2}} = \frac {- 1}{1 + u} \Big | _ {0} ^ {\mathrm {e} ^ {x}} = \frac {\mathrm {e} ^ {x}}{1 + \mathrm {e} ^ {x}}.</equation>（Ⅱ）（法一）定义法.

计算<equation>Y</equation>的分布函数<equation>F_{Y}(y)</equation>由于<equation>Y=\mathrm{e}^{X}>0</equation>，故当<equation>y\leqslant0</equation>时，<equation>F_{Y}(y)=P\{Y\leqslant y\}=0.</equation>当 y > 0时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{\mathrm {e} ^ {X} \leqslant y \right\} = P \left\{X \leqslant \ln y \right\} = F _ {X} (\ln y) = \frac {y}{1 + y}.</equation>因此，<equation>F_{Y}(y)=\left\{ \begin{array}{ll}\frac{y}{1+y},&y>0,\\ 0,&y\leqslant 0. \end{array} \right.</equation>当 y > 0时，<equation>f_{Y}(y)=F_{Y}^{\prime}(y)=\frac{1}{(1+y)^{2}}.</equation>当 y≤0时，<equation>f_{Y}(y)</equation><equation>= F_{Y}^{\prime}(y)=0.</equation>综上所述，Y的概率密度为<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} \frac {1}{(1 + y) ^ {2}}, & y > 0, \\ 0, & y \leqslant 0. \end{array} \right.</equation>（法二）公式法.

函数<equation>g ( x )=\mathrm{e}^{x}</equation>在<equation>(-\infty, +\infty)</equation>上处处可导且<equation>g^{\prime}(x)=\mathrm{e}^{x}>0.</equation><equation>\alpha = \min \left\{g (- \infty), g (+ \infty) \right\} = 0, \beta = \max \left\{g (- \infty), g (+ \infty) \right\} = + \infty .</equation><equation>g(x)</equation>的反函数为<equation>x = \ln y, (\ln y)^{\prime} = \frac{1}{y}</equation>.

由公式法可得，当 y > 0时，<equation>f _ {Y} (y) = f _ {X} (\ln y) \left| \frac {1}{y} \right| = \frac {1}{y} \cdot \frac {\mathrm {e} ^ {\ln y}}{\left(1 + \mathrm {e} ^ {\ln y}\right) ^ {2}} = \frac {1}{y} \cdot \frac {y}{(1 + y) ^ {2}} = \frac {1}{(1 + y) ^ {2}}.</equation>当<equation>y\leqslant0</equation>时，<equation>f_{Y}(y)=0.</equation>因此，Y的概率密度为<equation>f_{Y}(y)=\left\{ \begin{array}{ll}\frac{1}{(1+y)^{2}},&y>0,\\ 0,&y\leqslant 0. \end{array} \right.</equation>（Ⅲ）若 Y的数学期望存在，则由数学期望的定义可知<equation>\begin{array}{l} E (Y) = \int_ {- \infty} ^ {+ \infty} y f _ {Y} (y) \mathrm {d} y = \int_ {0} ^ {+ \infty} \frac {y \mathrm {d} y}{(1 + y) ^ {2}} = \int_ {0} ^ {+ \infty} \frac {1 + y - 1}{(1 + y) ^ {2}} \mathrm {d} y \\ = \int_ {0} ^ {+ \infty} \left[ \frac {1}{1 + y} - \frac {1}{(1 + y) ^ {2}} \right] \mathrm {d} y = \left[ \ln (1 + y) + \frac {1}{1 + y} \right] \Bigg | _ {0} ^ {+ \infty} = + \infty . \\ \end{array}</equation>因此，E（Y）不存在.

---

**2020年第14题 | 填空题 | 4分**

14. 设随机变量<equation>X</equation>的概率分布为<equation>P\{X=k\}=\frac{1}{2^{k}}(k=1,2,3,\cdots),Y</equation>表示<equation>X</equation>被3除的余数，则<equation>E(Y)=</equation>___.

**答案:**# 8 7

**解析:**解 X的取值为全体正整数，而 Y表示 X被3除的余数，故 Y的可能取值为0，1，2，分别对应 X = 3i+3, X=3i+1, X=3i+2（i=0，1，2，…）的情况.

下面计算 Y的分布律.<equation>P \{Y = 0 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 3 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 3}} = \frac {1}{8} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}},</equation><equation>P \{Y = 1 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 1 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 1}} = \frac {1}{2} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}},</equation><equation>P \{Y = 2 \} = \sum_ {i = 0} ^ {\infty} P \{X = 3 i + 2 \} = \sum_ {i = 0} ^ {\infty} \frac {1}{2 ^ {3 i + 2}} = \frac {1}{4} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}}.</equation>根据期望的定义，<equation>\begin{array}{l} E (Y) = 0 \times P \{Y = 0 \} + 1 \times P \{Y = 1 \} + 2 \times P \{Y = 2 \} \\ = 1 \times \frac {1}{2} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} + 2 \times \frac {1}{4} \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} = \sum_ {i = 0} ^ {\infty} \frac {1}{8 ^ {i}} \\ = \frac {1}{1 - \frac {1}{8}} = \frac {8}{7}. \\ \end{array}</equation>

---

**2019年第14题 | 填空题 | 4分**

14. 设随机变量 X的概率密度为 f(x)<equation>\left\{\begin{array}{l l} {\frac{x}{2},}&{0<x<2,}\\ {0,}&{\mathrm {其 他},}\end{array}\right.</equation>F(x)为 X的分布函数，E(X)为 X的数学期望，则<equation>P\{F(X)>E(X)-1\}=</equation>___

**答案:**# 2 3.

**解析:**（法一）分别计算<equation>E ( X )</equation>，<equation>F ( x )</equation><equation>E (X) = \int_ {- \infty} ^ {+ \infty} x f (x) \mathrm {d} x = \int_ {0} ^ {2} \frac {x ^ {2}}{2} \mathrm {d} x = \frac {x ^ {3}}{6} \Big | _ {0} ^ {2} = \frac {4}{3}.</equation>当<equation>x < 0</equation>时，<equation>F ( x )=0.</equation>当<equation>0 \leqslant x < 2</equation>时，<equation>F(x) = \int_{-\infty}^{x} f(t)\mathrm{d}t = \int_{0}^{x}\frac{t}{2}\mathrm{d}t = \frac{x^2}{4}.</equation>当<equation>x\geqslant 2</equation>时，<equation>F(x) = 1.</equation>于是，<equation>F ( x ) = \left\{ \begin{array}{ll} 0, & x < 0, \\ \frac{x^{2}}{4}, & 0 \leqslant x < 2, \\ 1, & x \geqslant 2. \end{array} \right.</equation>因此，<equation>\begin{array}{l} P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = P \left\{\frac {X ^ {2}}{4} > \frac {1}{3}, 0 \leqslant X < 2 \right\} + P \left\{X \geqslant 2 \right\} \\ = P \left\{\frac {2}{\sqrt {3}} < X < 2 \right\} + \int_ {2} ^ {+ \infty} f (x) \mathrm {d} x = 1 - \int_ {0} ^ {\frac {2}{\sqrt {3}}} \frac {x}{2} \mathrm {d} x + 0 \\ = 1 - \frac {x ^ {2}}{4} \Bigg | _ {0} ^ {\frac {2}{\sqrt {3}}} = \frac {2}{3}. \\ \end{array}</equation>（法二）我们先证明<equation>Y=F(X)</equation>服从（0，1）上的均匀分布.

注意到 F(x)在（0，2）上严格单调增加，其值域为（0，1），故可定义<equation>F^{-1}(y), y\in(0,1).</equation>考虑 Y的分布函数<equation>F_{Y}(y).</equation>当<equation>y < 0</equation>时，由于<equation>F ( X )</equation>仅在[0，1]上取值，故<equation>F_{Y} ( y )=0.</equation>当<equation>0\leqslant y < 1</equation>时，<equation>F _ {Y} (y) = P \left\{Y \leqslant y \right\} = P \left\{F (X) \leqslant y \right\} = P \left\{X \leqslant F ^ {- 1} (y) \right\} = F \left(F ^ {- 1} (y)\right) = y.</equation>当<equation>y \geqslant 1</equation>时，<equation>P\{Y \leqslant y\} = 1</equation>，即<equation>F_{Y}(y) = 1.</equation>因此，<equation>F_{Y}(y)=\left\{ \begin{array}{ll}0,& y<0,\\ y,& 0\leqslant y<1,\\ 1,& y\geqslant 1. \end{array} \right.</equation>这说明<equation>Y=F(X)</equation>服从（0，1）上的均匀分布.

由法一可知<equation>E ( X )=\frac{4}{3}</equation>，故<equation>P \left\{F (X) > E (X) - 1 \right\} = P \left\{F (X) > \frac {1}{3} \right\} = 1 - P \left\{F (X) \leqslant \frac {1}{3} \right\} = 1 - \frac {1}{3} = \frac {2}{3}.</equation>

---

**2017年第14题 | 填空题 | 4分**

14. 设随机变量 X的概率分布为<equation>P\{X=-2\}=\frac{1}{2}, P\{X=1\}=a, P\{X=3\}=b</equation>，若<equation>E(X)=0</equation>，则 D(X) =___

**答案:**# 9 2.

**解析:**解 由于<equation>P\{X=-2\}=\frac{1}{2}, P\{X=1\}=a, P\{X=3\}=b</equation>为随机变量X的分布律，故<equation>\frac{1}{2}+a+b=1</equation>即 a+b<equation>= 1</equation>，即 a+b<equation>= \frac{1}{2}.</equation>又因为<equation>E ( X )=0</equation>，所以<equation>(-2)\times \frac{1}{2}+1\times a+3\times b=0</equation>，即<equation>a+3b=1.</equation>联立<equation>\left\{ \begin{array}{l l} a+b=\frac{1}{2}, \\ a+3b=1, \end{array} \right.</equation>解得 a=b=<equation>\frac{1}{4}.</equation>代入<equation>D ( X )=\sum_{k=1}^{\infty} \left[ x_{k}-E ( X ) \right]^{2} p_{k}</equation>得，<equation>D (X) = (- 2 - 0) ^ {2} \times \frac {1}{2} + (1 - 0) ^ {2} \times \frac {1}{4} + (3 - 0) ^ {2} \times \frac {1}{4} = 2 + \frac {1}{4} + \frac {9}{4} = \frac {9}{2}.</equation>也可以利用公式<equation>D ( X )=E \left( X^{2} \right)-\left[ E ( X ) \right]^{2}</equation>来计算.<equation>E \left(X ^ {2}\right) = 4 \times \frac {1}{2} + 1 \times \frac {1}{4} + 9 \times \frac {1}{4} = \frac {9}{2}, \quad D (X) = \frac {9}{2} - 0 = \frac {9}{2}.</equation>

---


# 张宇数学公式手册


## 第一部分 高等数学


### 第三章 一元函数积分学

一、函数

二、极限

三、无穷小量与无穷大量

四、连续


一、导数与微分

二、导数的计算

三、微分中值定理

四、洛必达法则

五、函数及其性态的研究

六、曲率、曲率半径、曲率圆


一、不定积分

---


### 第七章 级 数

二、定积分

三、反常积分


一、向量代数

二、空间平面与直线

三、空间曲面与曲线


一、偏导数与全微分

二、隐函数求导法

三、方向导数

四、偏导数在几何中的应用

五、多元函数的极值


一、重积分的计算

二、重积分的应用(数学二不作要求)

三、曲线、曲面积分


一、数项级数

二、幂级数

三、傅里叶级数

---


## 第二部分 线性代数


### 第二章 矩 阵 91

一、一阶微分方程的类型及其解法 74

二、可降阶的高阶微分方程 76

三、线性微分方程解的结构定理 77

四、常系数齐次线性微分方程 78

五、二阶常系数非齐次线性微分方程 79

六、欧拉方程 81

七、差分方程 81


一、行列式的定义与性质 84

二、行列式的展开定理 86

三、几种特殊的行列式 87

四、有关行列式的若干个重要公式 90


一、矩阵的定义与运算 91

二、矩阵的秩 97

三、分块矩阵 98

四、矩阵的初等变换与初等矩阵 102

---


## 第三部分 概率论与数理统计


### 第一章 随机事件和概率

一、<equation>n</equation>维向量的定义及其运算

二、向量组的线性相(无)关性

三、极大无关组与向量组的秩

四、内积与施密特正交化

五、<equation>n</equation>维向量空间(数学二不作要求)


一、线性方程组的 4 种表示形式

二、线性方程组有解的判别条件

三、齐次线性方程组的解的结构

四、非齐次线性方程组<equation>AX=b</equation>的解的结构


一、特征值和特征向量

二、矩阵的对角化问题


一、二次型及其表示法

二、正定二次型及其判定


一、随机事件的关系及其运算

---


### 第四章 随机变量的数字特征

二、概率及其基本性质

三、概型、条件概率公式


一、分布函数

二、离散型随机变量

三、连续型随机变量

四、常见随机变量的概率分布

五、随机变量的函数的分布


一、二维随机变量的联合分布函数

二、二维离散型随机变量

三、二维连续型随机变量

四、条件分布

五、随机变量的独立性

六、二维常见分布

七、函数的分布


一、数学期望与函数期望

二、方差、协方差和矩

三、相关系数

---


