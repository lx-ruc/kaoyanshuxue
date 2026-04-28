#### 四、常见随机变量的概率分布

<equation>\textcircled{3}</equation>对于任意实数<equation>x_{1}, x_{2}\left(x_{1}\leqslant x_{2}\right)</equation>

<equation>\begin{array}{l} P \left\{x _ {1} < X \leqslant x _ {2} \right\} = F \left(x _ {2}\right) - F \left(x _ {1}\right) \\ = \int_ {x _ {1}} ^ {x _ {2}} f (x) \mathrm {d} x; \\ \end{array}</equation>

<equation>\textcircled{4}</equation>若<equation>f(x)</equation>在点<equation>x</equation>处连续，则<equation>F^{\prime}(x) = f(x)</equation>.


<table border="1"><tr><td>类型</td><td>定义</td></tr><tr><td>0-1分布</td><td>P(X=1)=p,P(X=0)=1-p(0<p&lt;1)</td></tr><tr><td>二项分布B(n,P)</td><td>P{X=k}=Cnk^{k}(1-p)^{n-k}(0<p&lt;1,k=0,1,2,···,n)</td></tr><tr><td>泊松分布P(λ)</td><td>P{X=k}=\frac{\lambda^{k}}{k!}e^{-\lambda}(\lambda&gt;0,k=0,1,2,···)</td></tr><tr><td>超几何分布</td><td>P{X=m}=\frac{C_{M}^{n}C_{N-M}^{n-m}}{C_{N}^{n}}(N,M,m均为正整数,0≤n≤N,0≤m≤M,0≤n-m≤N-M)</td></tr></table>

---


#### 2. 连续型

<table border="1"><tr><td>类型</td><td>定义</td></tr><tr><td>几何分布</td><td>P{X=k}=p(1-p)^{k-1}(k=1,2, \cdots,0<p&lt;1)</td></tr><tr><td>均匀分布U(a,b)</td><td>f(x)=\begin{cases}\frac{1}{b-a},&amp;a&lt;x<b\\0,&amp;其他\end{cases}$</td></tr><tr><td>指数分布E(λ)</td><td>f(x)=\begin{cases}\lambda e^{-\lambda x},&amp;x&gt;0\\0,&amp;其他\end{cases}(\lambda&gt;0)</td></tr><tr><td>正态分布N(\mu,\delta^{2})</td><td>f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}(\sigma&gt;0,-\infty&lt;x&lt;+\infty)</td></tr></table>


<equation>Y = g (x), P \left\{Y = y _ {j} \right\} = \sum_ {y _ {j} = g \left(x _ {j}\right)} P \left\{X = x _ {i} \right\}.</equation>


<equation>\textcircled{1}</equation><equation>Y = g(X)</equation>为单调可导的函数时，设<equation>X = h(Y)</equation>为其反函数，则

---

<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} f _ {X} [ h (y) ] \left| h ^ {\prime} (y) \right|, & \alpha < y < \beta , \\ 0, & \text {其 他}. \end{array} \right.</equation>

其中<equation>\alpha=\min( g(-\infty), g(+\infty))</equation>

<equation>\beta = \max (g (- \infty), g (+ \infty)).</equation>

<equation>\textcircled{2}</equation>对任意函数<equation>Y=g(X)</equation>

<equation>\begin{array}{l} F _ {Y} (y) = P \{Y \leqslant y \} = P \{g (X) \leqslant y \} \\ = \int_ {g (x) \leqslant y} f _ {X} (x) \mathrm {d} x, \\ \end{array}</equation>

<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y).</equation>

---


### 第三章 二维随机变量及其分布


#### (1)定义

<equation>F (x, y) = P \{X \leqslant x, Y \leqslant y \}.</equation>


<equation>\textcircled{1}</equation><equation>F(x,y)</equation>是变量<equation>x</equation>和<equation>y</equation>的单调不减函数；

<equation>\textcircled{2}</equation><equation>0 \leqslant F(x, y) \leqslant 1, F(-\infty, -\infty) = 0, F(+\infty, +\infty) = 1</equation>;

<equation>\textcircled{3} F ( x,y )</equation>关于变量 x和y都右连续；

<equation>\textcircled{4}</equation>对任意<equation>(x_{1}, y_{1}), (x_{2}, y_{2})(x_{1} < x_{2}, y_{1} < y_{2})</equation><equation>F(x_{2}, y_{2}) - F(x_{1}, y_{2}) - F(x_{2}, y_{1}) + F(x_{1}, y_{1}) \geqslant 0.</equation>


若随机变量<equation>(X, Y)</equation>的取值为有限多对或可列无穷多对时，则称<equation>(X, Y)</equation>为二维离散型随机变量.

---


#### 2. 联合概率密度函数的性质

<equation>P _ {i j} = P \left\{X = x _ {i}, Y = y _ {j} \right\}.</equation>

(2) 性质

<equation>0 \leqslant P _ {i j} \leqslant 1; \sum_ {i} \sum_ {j} P _ {i j} = 1.</equation>

(3) 边缘分布律

<equation>P _ {i.} = P \{X = x _ {i} \} = \sum_ {j = 1} ^ {\infty} P _ {i j};</equation>

<equation>P _ {. j} = P \left\{Y = y _ {j} \right\} = \sum_ {i = 1} ^ {\infty} P _ {i j}.</equation>


若存在非负可积函数<equation>f ( x,y)</equation>，使对任意的<equation>x,y</equation>有

<equation>F (x, y) = \int_ {- \infty} ^ {y} \int_ {- \infty} ^ {x} f (u, v) \mathrm {d} u \mathrm {d} v,</equation>

则称<equation>(X, Y)</equation>为二维连续型随机变量，称<equation>f(x,y)</equation>为<equation>(X, Y)</equation>的联合概率密度函数.


<equation>\textcircled{1} f ( x,y ) \geqslant0;</equation>

<equation>\textcircled{2}</equation><equation>\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}x\mathrm{d}y=1;</equation>

<equation>\textcircled{3}</equation>若<equation>f(x,y)</equation>在点<equation>(x,y)</equation>连续，则有

<equation>\frac {\partial^ {2} F}{\partial x \partial y} = f (x, y).</equation>

---


#### 1. 定义

<equation>\textcircled{4} P \{(X, Y) \in G \} = \iint_ {G} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

3. 边缘密度函数

<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y,</equation>

<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x.</equation>


1. 二维离散型随机变量的条件分布律

<equation>P \left(Y = y _ {j} \mid X = x _ {i}\right) = \frac {p _ {i j}}{p _ {i .}}, j = 1, 2, \dots ;</equation>

<equation>P = \left(X = x _ {i} \mid Y = y _ {j}\right) = \frac {p _ {i j}}{p _ {. j}}, j = 1, 2, \dots .</equation>

2. 二维连续型随机变量的条件密度函数

<equation>f _ {Y | X} (y | x) = \frac {f (x , y)}{f _ {X} (x)}, \quad \left(f _ {X} (x) > 0\right)</equation>

<equation>f _ {X \mid Y} (x \mid y) = \frac {f (x , y)}{f _ {Y} (y)}. \quad \left(f _ {Y} (y) > 0\right)</equation>


设<equation>F(x,y)</equation>及<equation>F_{X}(x),F_{Y}(y)</equation>分别是二维随机变量<equation>(X,Y)</equation>的联合分布函数和边缘分布函数，若对所有<equation>x,y</equation>

---


#### 2. 二维正态分布

有

<equation>P \{X \leqslant x, Y \leqslant y \} = P \{X \leqslant x \} P \{Y \leqslant y \}</equation>

则称随机变量 X和Y相互独立.


(1) 用定义

<equation>F (x, y) = F _ {X} (x) F _ {Y} (y).</equation>

(2) 离散型

<equation>P _ {i j} = P _ {i}. P _ {. j}.</equation>

(3) 连续型

<equation>f (x, y) = f _ {X} (x) f _ {Y} (y).</equation>


若二维随机变量<equation>(X,Y)</equation>的密度函数为

<equation>f (x, y) = \left\{ \begin{array}{c c} \frac {1}{m (D)}, & (x, y) \in D, \\ 0, & \text {其 他}, \end{array} \right.</equation>

其中<equation>m(D)</equation>表示区域<equation>D</equation>的面积，则称<equation>(X, Y)</equation>服从区域<equation>D</equation>上的均匀分布，并记为<equation>X\sim U(D)</equation>.


<equation>\textcircled{1}</equation>若二维随机变量<equation>(X, Y)</equation>的密度函数为

<equation>f (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}} \exp \left\{- \frac {1}{2 \left(1 - \rho^ {2}\right)} \right\}</equation>

---


#### (2)卷积公式

<equation>\left[ \frac {\left(x - \mu_ {1}\right) ^ {2}}{\sigma_ {1} ^ {2}} - 2 \rho \frac {\left(x - \mu_ {1}\right) \left(y - \mu_ {2}\right)}{\sigma_ {1} \sigma_ {2}} + \frac {\left(y - \mu_ {2}\right) ^ {2}}{\sigma_ {2} ^ {2}} \right] \Bigg \}.</equation>

其中参数<equation>\mu_{1}\in \mathbf{R},\mu_{2}\in \mathbf{R},\sigma_{1} > 0,\sigma_{2} > 0,\rho \in [-1,1]</equation>，则称二维随机变量<equation>(X,Y)</equation>服从二维正态分布，并记为<equation>(X,Y)\sim N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>.

<equation>\textcircled{2}</equation>二维正态分布的边缘密度

<equation>f _ {X} (x) = \frac {1}{\sqrt {2 \pi} \delta_ {1}} \mathrm {e} ^ {- \frac {(x - \mu_ {1}) ^ {2}}{2 \delta_ {1} ^ {2}}}, - \infty < x < + \infty .</equation>

<equation>f _ {Y} (x) = \frac {1}{\sqrt {2 \pi} \delta_ {2}} \mathrm {e} ^ {- \frac {(y - \mu_ {2}) ^ {2}}{2 \delta_ {2} ^ {2}}}, - \infty < y < + \infty .</equation>


(1) 一般公式

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f (z - y, y) \mathrm {d} y,</equation>

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f (x, z - x) \mathrm {d} x.</equation>


当<equation>x</equation>和<equation>y</equation>相互独立时，设<equation>(X, Y)</equation>关于<equation>X, Y</equation>的边缘密度分别为<equation>f_{X}(x), f_{Y}(y)</equation>，则

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f _ {X} (z - y) f _ {Y} (y) \mathrm {d} y,</equation>

---

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f _ {X} (x) f _ {Y} (z - x) \mathrm {d} x.</equation>

2.<equation>M=\max (X, Y)</equation>及<equation>N=\min (X, Y)</equation>的分布

设<equation>X, Y</equation>是两个相互独立的随机变量，它们的分布函数分别为<equation>F_{X}(x)</equation>和<equation>F_{Y}(y)</equation>，则

<equation>\begin{array}{l} F _ {\max } (z) = F _ {X} (z) f _ {Y} (z), \\ F _ {\min } (z) = 1 - \left[ 1 - F _ {X} (z) \right] \left[ 1 - F _ {Y} (z) \right]. \\ \end{array}</equation>

---


### 第四章 随机变量的数字特征


#### 1. 数学期望定义

<equation>\textcircled{1}</equation>若离散型随机变量

<equation>X \sim \left( \begin{array}{c c c c c} x _ {1} & x _ {2} & \dots & x _ {n} & \dots \\ p _ {1} & p _ {2} & \dots & p _ {n} & \dots \end{array} \right),</equation>

且级数<equation>\sum_{k} x_{k} p_{k}</equation>绝对收敛，称随机变量<equation>X</equation>的数学期望存在，并称

<equation>E X = \sum_ {k} x _ {k} p _ {k}</equation>

为其数学期望.

<equation>\textcircled{2}</equation>若连续型随机变量 X的密度函数为 f(x)，且积分<equation>\int_{\mathrm{R}} f ( x ) \mathrm{d} x</equation>绝对收敛，称随机变量 X的数学期望存在，并称

<equation>E X = \int_ {\mathrm {R}} f (x) \mathrm {d} x</equation>

为其数学期望.

---


#### 3. 性质

<equation>\textcircled{1}</equation>若随机变量<equation>X\sim \left( \begin{array}{c c c c c} x_{1} & x_{2} & \dots & x_{n} & \dots \\ p_{1} & p_{2} & \dots & p_{n} & \dots \end{array} \right), Y = g(X)</equation>，则

<equation>E Y = \sum_ {k} g \left(x _ {k}\right) p _ {k}.</equation>

<equation>\textcircled{2}</equation>若随机变量 X的密度函数为<equation>f_{X}(x),Y=g(X)</equation>则

<equation>E Y = \int_ {\mathbf {R}} g (x) f _ {X} (x) \mathrm {d} x.</equation>

<equation>\textcircled{3}</equation>若随机变量<equation>(X, Y) \sim p_{ij}, Z = g(X, Y)</equation>，则

<equation>E Z = \sum_ {i} \sum_ {j} g \left(x _ {i}, y _ {j}\right) p _ {i j}.</equation>

<equation>\textcircled{4}</equation>若随机变量<equation>(X, Y)</equation>的联合密度函数为<equation>f(x, y), Z = g(X, Y)</equation>，则

<equation>E Z = \iint_ {\mathbb {R} ^ {2}} g (x, y) f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{5}</equation>若随机变量<equation>X\sim \left( \begin{array}{cc}\xi & \eta \\ p & q \end{array} \right)</equation>，则

<equation>E X = p E \xi + q E \eta .</equation>

<equation>\textcircled{1}</equation>线性性：对任意<equation>a,b,c\in \mathbf{R}</equation>及随机变量<equation>X,Y</equation>，若EX，EY存在，则


<equation>E (a X + b Y + c) = a E X + b E Y + c.</equation>

---

<equation>\textcircled{2}</equation>若随机变量 X与 Y相互独立，且 EX，EY存在，则

<equation>E (X Y) = E X \cdot E Y.</equation>


若数学期望<equation>E(X - EX)^{2}</equation>存在，则称其为随机变量<equation>X</equation>的方差，并记为<equation>DX</equation>.同时称<equation>\sqrt{DX}</equation>为随机变量<equation>X</equation>的标准差.


若数学期望<equation>E[(X - EX)(Y - EY)]</equation>存在，则称其为随机变量<equation>X</equation>与<equation>Y</equation>的协方差，并记为<equation>\operatorname{Cov}(X, Y)</equation>.


<equation>\textcircled{1}</equation>对任意随机变量 X，<equation>D X\geqslant0.</equation>

<equation>\textcircled{2}</equation>若 C为固定常数，则<equation>D C=0.</equation>

<equation>\textcircled{3}</equation>常数<equation>a\in\mathbf{R}</equation>，则<equation>D(aX)=a^{2}DX.</equation>

<equation>\textcircled{4} D ( X \pm Y ) = D X + D Y \pm 2 \operatorname{C o v} ( X, Y ).</equation>

<equation>\textcircled{5}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则

<equation>D (X \pm Y) = D X + D Y.</equation>

<equation>\textcircled{6} D X=E X^{2}-(E X)^{2}.</equation>

<equation>\textcircled{7}</equation><equation>\operatorname{C o v} ( X, Y )=\operatorname{C o v} ( Y, X ).</equation>

<equation>\textcircled{8} \operatorname{C o v} ( a X, Y )=a \operatorname{C o v} ( X, Y ).</equation>

---


#### 4. 常见分布的数字特征

<equation>\textcircled{9} \operatorname {C o v} (X + Y, Z) = \operatorname {C o v} (X, Z) + \operatorname {C o v} (Y, Z).</equation>

<equation>\textcircled{10}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则

<equation>\operatorname {C o v} (X, Y) = 0.</equation>

<equation>\begin{array}{l} \textcircled{1 2} \operatorname {C o v} \left(a X + b Y, c \xi + d \eta\right) = a c \operatorname {C o v} \left(X, \xi\right) + \\ a d \operatorname {C o v} (X, \eta) + b c \operatorname {C o v} (Y, \xi) + b d \operatorname {C o v} (Y, \eta). \\ \end{array}</equation>

其中<equation>a, b, c, d</equation>为常数，<equation>X, Y, \xi , \eta</equation>为随机变量.


(1) 0-1分布

若<equation>X\sim \binom{0}{q}\frac{1}{p}</equation>，则

<equation>E X = p, D X = p q.</equation>

(2) 几何分布

若<equation>P(X = n) = pq^{n - 1}(n = 1,2,\dots)</equation>，则

<equation>E X = \frac {1}{p}, D X = \frac {q}{p ^ {2}}.</equation>

(3) 二项分布

若<equation>Y\sim B(n,p)</equation>，则<equation>EY = np,DY = npq.</equation>

(4) 超几何分布

若<equation>P ( Y=k)=\frac{C_{M}^{k} C_{N-M}^{n-k}}{C_{N}^{n}}</equation>，其中<equation>\max \{0,n-N+M\}</equation><equation>\leq k\leq \min \{M,n\}</equation>k为整数，<equation>n-k\leq N-M</equation>记<equation>p=\frac{M}{N}</equation><equation>q=1-p</equation>，则

---


#### 1. 定义

<equation>E Y = n p, D Y = n p q \frac {N - n}{N - 1}.</equation>


若<equation>X\sim P(\lambda)</equation>，则

<equation>E X = \lambda , D X = \lambda .</equation>


<equation>X\sim U(a,b)</equation>，则

<equation>E X = \frac {a + b}{2}, D X = \frac {(b - a) ^ {2}}{1 2}.</equation>


若<equation>X\sim E(\lambda)</equation>，则

<equation>E X = \frac {1}{\lambda}, D X = \frac {1}{\lambda^ {2}}.</equation>

(8) 正态分布

若<equation>X\sim N(\mu ,\sigma^{2})</equation>，则

<equation>E X = \mu , D X = \sigma^ {2}.</equation>


若<equation>DX > 0, DY > 0</equation>，则称<equation>\frac{\operatorname{Cov}(X, Y)}{\sqrt{DX \cdot DY}}</equation>为随机变量<equation>X</equation>与<equation>Y</equation>的相关系数，并记为<equation>\rho_{xy}</equation>. 若<equation>\rho_{xy} = 1</equation>，则称<equation>X</equation>与<equation>Y</equation>正相关；若<equation>\rho_{xy} = -1</equation>，则称<equation>X</equation>与<equation>Y</equation>负相关；若<equation>\rho_{xy} = 0</equation>，则称

---


#### 2. 性质

X与Y不相关.


<equation>\textcircled{1}</equation><equation>|\rho_{x x}| \leqslant 1.</equation>

<equation>\textcircled{2} \operatorname{C o v}^{2} ( X, Y ) \leqslant D X \cdot D Y.</equation>

<equation>\textcircled{3}</equation><equation>| E ( X Y ) | \leqslant \sqrt { E X^{2} \cdot E Y^{2}}.</equation>

<equation>\textcircled{4}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则<equation>\rho_{x y} = 0.</equation>

<equation>\textcircled{5}</equation>若<equation>(X, Y) \sim N(\mu_1, \sigma_1^2; \mu_2, \sigma_2^2; \rho)</equation>，则其中的参数<equation>\rho</equation>为其相关系数，且<equation>X</equation>与<equation>Y</equation>相互独立的充分必要条件为<equation>\rho = 0</equation>。

<equation>\textcircled{6}</equation>若<equation>X\sim \left( \begin{array}{cc}0 & 1\\ q_{1} & p_{1} \end{array} \right), Y\sim \left( \begin{array}{cc}0 & 1\\ q_{2} & p_{2} \end{array} \right), p_{k} + q_{k} = 1(k = 1,2)</equation>，则X与Y相互独立的充分必要条件为<equation>\rho_{xy} = 0.</equation>

---


### 第五章 大数定律和中心极限定理


#### 2. 辛钦大数定律

设随机变量<equation>X</equation>的数学期望与方差存在，则对任意实数<equation>\varepsilon > 0</equation>，下面的不等式成立：

<equation>P \left(\left| X - E X \right| \geqslant \varepsilon\right) \leqslant \frac {D X}{\varepsilon^ {2}}, \text {或}</equation>

<equation>P \left(| X - E X | < \varepsilon\right) \geqslant 1 - \frac {D X}{\varepsilon^ {2}},</equation>

并称之为切比雪夫不等式.


设<equation>X_{1}, X_{2}, \dots, X_{n}, \dots</equation>为相互独立的随机变量序列，其数学期望和方差都存在并且相等，分别记为<equation>\mu</equation>和<equation>\sigma^2</equation>，则对任意<equation>\varepsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \mu \right| < \varepsilon \right\} = 1.</equation>


设<equation>X_{1}, X_{2}, \dots, X_{n}, \dots</equation>为相互独立同分布的随机变

---


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

