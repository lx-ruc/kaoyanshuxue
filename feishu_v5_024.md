#### 2. 棣莫弗一拉普拉斯定理


量序列，且其数学期望存在，记为<equation>\mu</equation>，则对任意<equation>\varepsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \mu \right| < \varepsilon \right\} = 1.</equation>


设随机变量<equation>n_{A}\sim B(n,p)</equation>，则对任意<equation>\varepsilon >0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {n _ {A}}{n} - p \right| < \varepsilon \right\} = 1.</equation>


设<equation>X_{1}, X_{2}, \dots , X_{n}, \dots</equation>为相互独立同分布的随机变量序列，且其数学期望和方差都存在，分别记为<equation>\mu</equation>和<equation>\sigma^2</equation>.则对任意的<equation>x</equation>有

<equation>\lim _ {n \rightarrow \infty} P \left\{\frac {\sum_ {i = 1} ^ {n} X _ {i} - n \mu}{\sqrt {n} \delta} \leqslant x \right\} = \int_ {- \infty} ^ {x} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {i}{2}} \mathrm {d} t.</equation>


设随机变量<equation>\eta_{n}(n = 1,2,\dots)\sim B(n,p)</equation>，则对任意的<equation>x</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\frac {\eta_ {n} - n p}{\sqrt {n p (1 - p)}} \leqslant x \right\} = \int_ {- \infty} ^ {x} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {i}{2}} \mathrm {d} t.</equation>

---


#### 二、统计分布与抽样分布定理


1. 样本均值

<equation>\bar {X} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k}.</equation>

2. 样本方差

<equation>S ^ {2} = \frac {1}{n - 1} \sum_ {k = 1} ^ {n} \left(X _ {k} - \bar {X}\right) ^ {2}.</equation>

3. r阶样本原点矩

<equation>A _ {r} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k} ^ {r}.</equation>

4. r阶样本中心矩

<equation>B _ {r} = \frac {1}{n} \sum_ {k = 1} ^ {n} \left(X _ {k} - \bar {X}\right) ^ {r}.</equation>


1.<equation>\chi^{2}</equation>分布

设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立且均服从<equation>N(0,1)</equation>，令<equation>Y = \sum_{k=1}^{n} X_{k}^{2}</equation>，称随机变量<equation>Y</equation>的分布为自由度为<equation>n</equation>的<equation>\chi^{2}</equation>

---


#### (1)一维正态总体情形


分布，并记为<equation>Y\sim \chi^{2}(n)</equation>. 其数字特征<equation>EY = n, DY = 2n.</equation>


设随机变量<equation>X\sim N(0,1),Y\sim \chi^{2}(n)</equation>且相互独立，令<equation>T = \frac{X}{\sqrt{Y / n}}</equation>，称随机变量<equation>T</equation>的分布为自由度为<equation>n</equation>的<equation>t</equation>分布，并记为<equation>T\sim t(n)</equation>.记随机变量<equation>T</equation>的密度函数为<equation>f_{n}(x)</equation>，则<equation>f_{n}(x)</equation>满足：


<equation>\textcircled{2} \lim_{n \to \infty} f_{n}(x) = \frac{1}{\sqrt{2 \pi}} \mathrm{e}^{-\frac{x^{2}}{2}}.</equation>


设随机变量<equation>X\sim \chi^{2}(m),Y\sim \chi^{2}(n)</equation>且相互独立.令<equation>F = \frac{X / m}{Y / n}</equation>，称其分布为自由度为<equation>(m,n)</equation>的<equation>F</equation>分布，记为<equation>F\sim F(m,n)</equation>，由定义易知<equation>\frac{1}{F}\sim F(n,m)</equation>.


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自正态总体<equation>X \sim N(\mu, \delta^{2})</equation>的容量为<equation>n</equation>的简单随机样本，<equation>\bar{X}</equation>为样本均值，<equation>S^{2}</equation>为样本方差，则

<equation>\textcircled{1} Z = \frac {\bar {X} - \mu}{\delta / \sqrt {n}} \sim N (0, 1).</equation>

---


#### (2) 二维正态总体情形


<equation>\textcircled{2} Y=\frac{(n-1)S^{2}}{\delta^{2}}\sim\chi^{2}(n-1).</equation>

<equation>\textcircled{3}</equation>随机变量 Y与 Z相互独立，即<equation>\overline{{X}}</equation>与<equation>S^{2}</equation>相互独立<equation>\textcircled{4}</equation><equation>\frac{\overline{{X}} - \mu}{S / \sqrt{n}}\sim t(n-1).</equation>


设<equation>X_{1}, X_{2}, \dots X_{m}</equation>为来自正态总体<equation>X \sim N(\mu_{1}, \delta_{1}^{2})</equation>的容量为<equation>m</equation>的简单随机样本，<equation>\overline{X}</equation>为样本均值，<equation>S_{1}^{2}</equation>为样本方差；<equation>Y_{1}, Y_{2}, \dots, Y_{n}</equation>为来自正态总体<equation>Y \sim N(\mu_{2}, \delta_{2}^{2})</equation>的容量为<equation>n</equation>的简单随机样本，<equation>\overline{Y}</equation>为样本均值，<equation>S_{2}^{2}</equation>为样本方差，且两总体相互独立，则：

<equation>\textcircled{1} Z = \frac {\left(\bar {X} - \bar {Y}\right) - \left(\mu_ {1} - \mu_ {2}\right)}{\sqrt {\frac {\delta_ {1} ^ {2}}{m} + \frac {\delta_ {2} ^ {2}}{n}}} \sim N (0, 1).</equation>

<equation>\textcircled{2} \frac {(m - 1) S _ {1} ^ {2}}{\delta_ {1} ^ {2}} + \frac {(n - 1) S _ {2} ^ {2}}{\delta_ {2} ^ {2}} \sim \chi^ {2} (m + n - 2).</equation>

<equation>\textcircled{4}</equation>当<equation>\delta_1^2 = \delta_2^2 = \delta^2</equation>时，有

<equation>T = \frac {\left(\bar {X} - \bar {Y}\right) - \left(\mu_ {1} - \mu_ {2}\right)}{S _ {w} \sqrt {\frac {1}{m} + \frac {1}{n}}} \sim t (m + n - 2).</equation>

其中<equation>S_{w}^{2}=\frac{(m-1)S_{1}^{2}+(n-1)S_{2}^{2}}{m+n-2}.</equation>

---


### 第七章 答数估计


#### 二、最大似然估计法


估计公式：

<equation>\hat {\mu} _ {k} = A _ {k},</equation>

其中<equation>\mu_{k}</equation>为总体的<equation>k</equation>阶原点矩，<equation>A_{k}</equation>为样本<equation>k</equation>阶原点矩.


1. 样本似然函数

<equation>L (\theta) = L \left(x _ {1}, x _ {2}, \dots , x _ {n}; \theta\right).</equation>

2. 最大似然估计值与最大似然估计量

若<equation>L(x_{1},x_{2},\dots ,x_{n};\hat{\theta}) = \max L\{(x_{1},x_{2},\dots ,x_{n};\theta)\}</equation>，则称<equation>\hat{\theta} (x_{1},x_{2},\dots ,x_{n})</equation>为参数<equation>\theta</equation>的最大似然估计值，而称<equation>\hat{\theta}</equation><equation>(X_{1},X_{2},\dots ,X_{n})</equation>为参数<equation>\theta</equation>的最大似然估计量.

3. 由矩法和最大似然估计法得到的正态总体参数的估计量

<equation>\hat {\mu} = A _ {1} = \bar {X},</equation>

<equation>\hat {\sigma} ^ {2} = A _ {2} - A _ {1} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(X _ {i} - \bar {X}\right) ^ {2}.</equation>

---


#### 三、置信区间


<equation>\textcircled{1}</equation>定义：若<equation>E(\partial) = \theta</equation>，称<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计量.

<equation>\textcircled{2}</equation>结论：因为<equation>E(\overline{X}) = \mu , E(S^2) = \delta^2</equation>，所以<equation>\overline{X}</equation>是样本均值<equation>\mu</equation>的无偏估计量，样本方差<equation>S^{2}</equation>是总体方差<equation>\sigma^{2}</equation>的无偏估计量.


设<equation>\hat{\theta}_1 = \hat{\theta}_1\left(X_1, X_2, \dots, X_n\right)</equation>与<equation>\hat{\theta}_2 = \hat{\theta}_2\left(X_1, X_2, \dots, X_n\right)</equation>都是<equation>\theta</equation>的无偏估计量，若对任意<equation>\theta \in \Theta</equation>，有<equation>D(\hat{\theta}_1) \leqslant D(\hat{\theta}_2)</equation>，且至少对于某一个<equation>\theta \in \Theta</equation>，上式中不等号成立，则称<equation>\hat{\theta}_1</equation>较<equation>\hat{\theta}_2</equation>有效.


若对于任意<equation>\theta \in \Theta</equation>都满足：对任意<equation>\epsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \hat {\theta} - \theta \right| < \varepsilon \right\} = 1,</equation>

则称<equation>\hat{\theta}</equation>是<equation>\theta</equation>的一致估计量.


设总体<equation>X</equation>的分布律中含有未知参数<equation>\theta</equation>，来自该总体的几个样本为<equation>X_{1}, X_{2}, \dots, X_{n}, 0 < \alpha < 1.</equation>若存在统计量<equation>\hat{\theta}_{1}</equation>和<equation>\hat{\theta}_{2}</equation>，使得<equation>P(\hat{\theta}_{1} \leqslant \theta \leqslant \hat{\theta}_{2}) = 1 - \alpha</equation>，则称<equation>1 - \alpha</equation>为置信度，<equation>(\hat{\theta}_{1}, \hat{\theta}_{2})</equation>为<equation>\theta</equation>的置信区间.

---

四、常用单个正态总体参数的置信区间表

<table border="1"><tr><td>参数</td><td colspan="2"><equation>\mu</equation></td><td><equation>\delta^{2}</equation></td></tr><tr><td>条件</td><td>已知<equation>\delta^{2}</equation></td><td>未知<equation>\delta^{2}</equation></td><td><equation>\mu</equation>未知</td></tr><tr><td>置信区间</td><td><equation>\left[\bar{X}-\frac{\delta}{\sqrt{n}}z_{\frac{\alpha}{2}}, \bar{X}+\frac{\delta}{\sqrt{n}}z_{\frac{\alpha}{2}}\right]</equation></td><td><equation>\left[\bar{X}-\frac{S}{\sqrt{n}}t_{\frac{\alpha}{2}}(n-1), \bar{X}+\frac{S}{\sqrt{n}}t_{\frac{\alpha}{2}}(n-1)\right]</equation></td><td><equation>\left[\frac{(n-1)S^{2}}{\chi_{\frac{\alpha}{2}}^{2}(n-1)},\frac{(n-1)S^{2}}{\chi_{1-\frac{\alpha}{2}}^{2}(n-1)}\right]</equation></td></tr></table>

---


#### 3. 不等式


<equation>\textcircled{1}</equation><equation>( a \pm b )^{2}=a^{2} \pm 2 a b+b^{2}</equation>

<equation>\textcircled{3} a^{2}-b^{2}=(a-b)(a+b);</equation>

<equation>\textcircled{4}</equation><equation>(a\pm b)^{3}=a^{3}\pm 3a^{2}b+3ab^{2}\pm b^{3};</equation>

<equation>\textcircled{6} a^{n}-b^{n}=(a-b)(a^{n-1}+a^{n-2}b+a^{n-3}b^{2}+\cdots+ a b^{n-2}+b^{n-1})</equation>（n为正整数）.


(1) 一元二次方程<equation>a x^{2}+b x+c=0 ( a \neq0 )</equation>的求根公式

<equation>x _ {1, 2} = \frac {- b \pm \sqrt {b ^ {2} - 4 a c}}{2 a}.</equation>

(2) 根与系数之间的关系

<equation>x _ {1} + x _ {2} = - \frac {b}{a}, x _ {1} x _ {2} = \frac {c}{a}.</equation>

---

<equation>\textcircled{2}</equation><equation>\frac{a+b}{2}\geqslant\sqrt{ab}</equation>（a,b<equation>\in\mathbf{R}^{+}</equation>）;

<equation>\textcircled{4}</equation>柯西不等式<equation>(a^{2} + b^{2})(c^{2} + d^{2}) \geqslant (ac + bd)^{2}</equation>;

<equation>\textcircled{5}</equation><equation>|a| - |b| \leqslant |a + b| \leqslant |a| + |b|</equation>;

<equation>\textcircled{6}</equation><equation>\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}\geqslant\sqrt[n]{a_{1}a_{2}\cdots a_{n}}</equation><equation>(a_{i}>0,i=1,</equation>2,…,n).

4. 指数

<equation>\textcircled{1}</equation><equation>a^{m} \cdot a^{n} = a^{m+n}</equation>;

<equation>\textcircled{2}</equation><equation>a^{m}\div a^{n}=a^{m-n};</equation>

<equation>\textcircled{3}</equation><equation>( a^{m} )^{n}=a^{n m}</equation>

<equation>\textcircled{4} ( a b )^{m}=a^{m} b^{m}</equation>

<equation>\textcircled{5}</equation><equation>\left( \frac{a}{b} \right)^{m}=\frac{a^{m}}{b^{m}};</equation>

<equation>\textcircled{6} a^{-m}=\frac{1}{a^{m}};</equation>

<equation>\textcircled{7} a^{0}=1(a>0).</equation>

5. 对数<equation>(\log_{a} N,a > 0,a\neq 1)</equation>

<equation>\textcircled{1} N=a^{\log N};</equation>

<equation>\textcircled{2} \log_{a}(M N)=\log_{a} M+\log_{a} N;</equation>

<equation>\textcircled{3}</equation><equation>\log_ {a}\left(\frac {M}{N}\right) = \log_ {a} M - \log_ {a} N;</equation>

<equation>\textcircled{4} \log_{a} ( M^{n} )=n \log_{a} M;</equation>

---

<equation>\textcircled{5} \log_{a}\sqrt[n]{M}=\frac{1}{n}\log_{a}M;</equation>

<equation>\textcircled{6}</equation>换底公式：<equation>\log_{a}M = \frac{\log_{b}M}{\log_{b}a}</equation>；

<equation>\textcircled{7} \log_{a} 1=0,\log_{a} a=1.</equation>

6. 数列

(1) 等差数列

<equation>\textcircled{1}</equation>通项公式

<equation>a _ {n} = a _ {1} + (n - 1) d.</equation>

<equation>\textcircled{2}</equation>前 n项的和

<equation>S _ {n} = \frac {n}{2} \left(a _ {1} + a _ {n}\right) = n a _ {1} + \frac {1}{2} n (n - 1) d.</equation>

(2) 等比数列

<equation>\textcircled{1}</equation>通项公式

<equation>a _ {n} = a _ {1} q ^ {n - 1}.</equation>

<equation>\textcircled{2}</equation>前 n项的和

<equation>S _ {n} = \left\{ \begin{array}{l l} n a _ {1}, & q = 1, \\ \frac {a _ {1} - a _ {n} q}{1 - q} = \frac {a _ {1} \left(1 - q ^ {n}\right)}{1 - q}, q \neq 1. \end{array} \right.</equation>

(3) 常用数列前 n项的和

<equation>1 + 2 + \dots + n = \frac {n (n + 1)}{2};</equation>

<equation>1 + 3 + 5 + \dots + (2 n - 1) = n ^ {2};</equation>

---


#### 7. 排列、组合与二项式公式


<equation>1 ^ {2} + 2 ^ {2} + \dots + n ^ {2} = \frac {n (n + 1) (2 n + 1)}{6}.</equation>


(1) 排列数

<equation>\textcircled{1}</equation><equation>A_{n}^{k} = n(n - 1)\dots (n - k + 1)</equation>（元素不可重复的排列）

<equation>\textcircled{2} n^{k}</equation>（元素可以重复的排列）

<equation>\textcircled{3} n! = n ( n - 1 ) \dots 3 \cdot 2 \cdot 1</equation>（全排列）

(2) 组合数

<equation>C _ {n} ^ {k} = \frac {\mathrm {A} _ {n} ^ {k}}{k !} = \frac {n (n - 1) \cdots (n - k + 1)}{k !} = \frac {n !}{(n - k) ! k !}.</equation>

(3) 二项式定理

<equation>(a + b) ^ {n} = \sum_ {k = 0} ^ {n} \mathrm {C} _ {n} ^ {k} \cdot a ^ {n - k} \cdot b ^ {k}, n \in \mathrm {N}.</equation>

---


#### 2. 梯形的面积


<equation>\textcircled{1}</equation><equation>S=\frac{1}{2} a b \sin C</equation>（若<equation>C=\frac{\pi}{2}</equation>，即直角三角形的面积<equation>S=\frac{1}{2} a b</equation>

<equation>\textcircled{2}</equation><equation>S=\sqrt{s(s-a)(s-b)(s-c)},</equation>其中 a,b,c为其三边长，<equation>s=\frac{1}{2} ( a+b+c).</equation>


<equation>S=\frac{1}{2} ( a+b) h</equation>，其中a，b为上下底，高为h.

3. 圆（半径为 r）

<equation>\textcircled{1}</equation>圆周长

<equation>l = 2 \pi r;</equation>

<equation>\textcircled{2}</equation>圆弧长

<equation>l = r \theta ,</equation>

其中<equation>\theta</equation>为圆弧所对的圆心角（单位为弧度）.

<equation>\textcircled{3}</equation>扇形面积

---


#### 4. 旋转体


<equation>S = \frac {1}{2} r ^ {2} \theta ,</equation>

其中<equation>\theta</equation>为圆心角.


(1) 圆柱（底面圆半径为<equation>r</equation>，柱高为<equation>h</equation>）

<equation>\textcircled{1}</equation>侧面积<equation>= 2\pi rh;</equation>

<equation>\textcircled{2}</equation>全面积<equation>= 2\pi r(r + h);</equation>

<equation>\textcircled{3}</equation>体积<equation>= \pi r^{2}h.</equation>

(2) 圆锥（底面圆半径为 r，高为 h，母线长为<equation>l=\sqrt{r^{2}+h^{2}}</equation>）

<equation>\textcircled{1}</equation>侧面积<equation>= \pi r l;</equation>

<equation>\textcircled{2}</equation>全面积<equation>= \pi r(l+r);</equation>

<equation>\textcircled{3}</equation>体积<equation>= \frac{1}{3}\pi r^{2}h.</equation>

(3) 圆台（上、下底面圆半径为<equation>r_{1}, r_{2}</equation>，高为h，母线长为<equation>l=\sqrt{h^{2}+(r_{2}-r_{1})^{2}}</equation>

<equation>\textcircled{1}</equation>侧面积<equation>= \pi (r_{1} + r_{2})l</equation>;

<equation>\textcircled{2}</equation>全面积<equation>= \pi r_{1}(l+r_{1})+\pi r_{2}(l+r_{2}).</equation>

<equation>\textcircled{3}</equation>体积<equation>= \frac{1}{3}\pi h\left(r_{1}^{2}+r_{2}^{2}+r_{1}r_{2}\right).</equation>

(4) 球（半径为 r）

<equation>\textcircled{1}</equation>全面积<equation>= 4\pi r^{2}.</equation>

<equation>\textcircled{2}</equation>体积<equation>= \frac{4}{3}\pi r^{3}.</equation>

---


#### 三角函数


1. 和差角公式

<equation>\sin (\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta ;</equation>

<equation>\cos (\alpha \pm \beta) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta ;</equation>

<equation>\tan (\alpha \pm \beta) = \frac {\tan \alpha \pm \tan \beta}{1 \mp \tan \alpha \cdot \tan \beta};</equation>

<equation>\cot (\alpha \pm \beta) = \frac {\cot \alpha \cdot \cot \beta \mp 1}{\cot \beta \pm \cot \alpha}.</equation>

2. 和差化积公式

<equation>\sin \alpha + \sin \beta = 2 \sin \frac {\alpha + \beta}{2} \cos \frac {\alpha - \beta}{2};</equation>

<equation>\sin \alpha - \sin \beta = 2 \cos \frac {\alpha + \beta}{2} \sin \frac {\alpha - \beta}{2};</equation>

<equation>\cos \alpha + \cos \beta = 2 \cos \frac {\alpha + \beta}{2} \cos \frac {\alpha - \beta}{2};</equation>

<equation>\cos \alpha - \cos \beta = - 2 \sin \frac {\alpha + \beta}{2} \sin \frac {\alpha - \beta}{2}.</equation>

3. 倍角公式

<equation>\sin 2 \alpha = 2 \sin \alpha \cos \alpha ;</equation>

<equation>\cos 2 \alpha = 2 \cos^ {2} \alpha - 1 = 1 - 2 \sin^ {2} \alpha = \cos^ {2} \alpha - \sin^ {2} \alpha ;</equation>

---

<equation>\tan 2 \alpha = \frac {2 \tan \alpha}{1 - \tan^ {2} \alpha};</equation>

<equation>\cot 2 \alpha = \frac {\cot^ {2} \alpha - 1}{2 \cot \alpha};</equation>

<equation>\sin 3 \alpha = 3 \sin \alpha - 4 \sin^ {3} \alpha ;</equation>

<equation>\cos 3 \alpha = 4 \cos^ {3} \alpha - 3 \cos \alpha ;</equation>

<equation>\tan 3 \alpha = \frac {3 \tan \alpha - \tan^ {3} \alpha}{1 - 3 \tan^ {2} \alpha}.</equation>

4. 半角公式

<equation>\sin \frac {\alpha}{2} = \pm \sqrt {\frac {1 - \cos \alpha}{2}};</equation>

<equation>\cos \frac {\alpha}{2} = \pm \sqrt {\frac {1 + \cos \alpha}{2}};</equation>

<equation>\tan \frac {\alpha}{2} = \pm \sqrt {\frac {1 - \cos \alpha}{1 + \cos \alpha}} = \frac {1 - \cos \alpha}{\sin \alpha} = \frac {\sin \alpha}{1 + \cos \alpha};</equation>

<equation>\cot \frac {\alpha}{2} = \pm \sqrt {\frac {1 + \cos \alpha}{1 - \cos \alpha}} = \frac {1 + \cos \alpha}{\sin \alpha} = \frac {\sin \alpha}{1 - \cos \alpha}.</equation>

5. 正弦定理

<equation>\frac {a}{\sin A} = \frac {b}{\sin B} = \frac {c}{\sin C} = 2 R.</equation>

6. 余弦定理

<equation>c ^ {2} = a ^ {2} + b ^ {2} - 2 a b \cos C.</equation>

---


#### 7. 反三角函数性质


<equation>\arcsin x = \frac {\pi}{2} - \arccos x;</equation>

<equation>\arctan x = \frac {\pi}{2} - \arccot x.</equation>

---


### 平面解析几何


#### 2. 直线


设坐标平面内任意两点<equation>P_{1}(x_{1},y_{1})</equation>和<equation>P_{2}(x_{2},y_{2})</equation>则这两点的距离为

<equation>\left| P _ {1} P _ {2} \right| = \sqrt {\left(x _ {2} - x _ {1}\right) ^ {2} + \left(y _ {2} - y _ {1}\right) ^ {2}}.</equation>

特别地，点<equation>P(x,y)</equation>到原点距离为<equation>|OP| = \sqrt{x^2 + y^2}</equation>.


(1) 方程表示式

<equation>\textcircled{1}</equation>一般式

<equation>A x + B y + C = 0.</equation>

<equation>\textcircled{2}</equation>点斜式

<equation>y - y _ {1} = k \left(x - x _ {1}\right).</equation>

<equation>\textcircled{3}</equation>两点式

<equation>\frac {y - y _ {1}}{x - x _ {1}} = \frac {y _ {2} - y _ {1}}{x _ {2} - x _ {1}}.</equation>

<equation>\textcircled{4}</equation>斜截式

<equation>y = k x + b.</equation>

<equation>\textcircled{5}</equation>截距式

---


#### （2）椭圆


<equation>\frac {x}{a} + \frac {y}{b} = 1.</equation>


设坐标平面内点<equation>P\left(x_{0}, y_{0}\right)</equation>和直线 l：<equation>A x+B y+ C=0</equation>，点P到直线l的距离为d，则有

<equation>d = \frac {\left| A x _ {0} + B y _ {0} + C \right|}{\sqrt {A ^ {2} + B ^ {2}}}.</equation>


(1) 圆

<equation>\textcircled{1}</equation>圆的标准方程

<equation>(x - a) ^ {2} + (y - b) ^ {2} = r ^ {2},</equation>

其中（a,b）为圆心坐标，r为半径.

<equation>\textcircled{2}</equation>圆的一般方程

<equation>x ^ {2} + y ^ {2} + D x + E y + F = 0,</equation>

其中<equation>D^{2}+E^{2}-4 F>0</equation>，圆心坐标为<equation>\left(-\frac{D}{2},-\frac{E}{2}\right)</equation>半径为<equation>\frac{\sqrt{D^{2}+E^{2}-4 F}}{2}.</equation>


<equation>\textcircled{1}</equation>标准方程

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} = 1, a > b > 0.</equation>

<equation>\textcircled{2}</equation>焦点坐标

---

<equation>F (\pm c, 0),</equation>

其中<equation>c = \sqrt{a^{2} - b^{2}}.</equation>

<equation>\textcircled{3}</equation>准线方程

<equation>x = \pm \frac {a ^ {2}}{c}.</equation>

(3) 双曲线

<equation>\textcircled{1}</equation>标准方程

<equation>\frac {x ^ {2}}{a ^ {2}} - \frac {y ^ {2}}{b ^ {2}} = 1.</equation>

<equation>\textcircled{2}</equation>焦点坐标

<equation>F (\pm c, 0),</equation>

其中<equation>c = \sqrt{a^2 + b^2}</equation>

<equation>\textcircled{3}</equation>渐近线方程

<equation>y = \pm \frac {b}{a} x.</equation>

<equation>\textcircled{4}</equation>准线方程

<equation>x = \pm \frac {a ^ {2}}{c}.</equation>

(4) 抛物线

<equation>\textcircled{1}</equation>标准方程

<equation>y ^ {2} = 2 p x (p > 0).</equation>

<equation>\textcircled{2}</equation>焦点坐标

<equation>F \left(\frac {p}{2}, 0\right).</equation>

---

<equation>\textcircled{3}</equation>切线

<equation>y_{1}y = p(x + x_{1})</equation>，切点<equation>(x_{1},y_{1})</equation>

4. 极坐标与直角坐标

<equation>\textcircled{1}</equation><equation>\left\{ \begin{array}{l} x=\rho\cos \theta, \\ y=\rho\sin \theta. \end{array} \right.</equation>

<equation>\textcircled{2}</equation><equation>\left\{ \begin{array}{l} \rho^{2}=x^{2}+y^{2}, \\ \tan \theta=\frac{y}{x}(x\neq 0). \end{array} \right.</equation>

4. 9元包邮@5分钱/每张

檀樟刷顯小模屏;硅酷刷顯免舜判闰U盔满舟璃等18金匣咖膛夹芹铀藉、渍项嫡鉴、错澳喇殖列…

---