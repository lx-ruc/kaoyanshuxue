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


#### 附录 和等数学

第五章 大数定律和中心极限定理

一、切比雪夫不等式

二、大数定律

三、中心极限定理

第六章 数理统计的基本概念

一、统计量的样本数字特征及极限

二、统计分布与抽样分布定理

第七章 参数估计

一、矩估计法

二、最大似然估计法

三、置信区间

四、常用单个正态总体参数的置信区间表


初等代数

初等几何

三角函数

平面解析几何

---


## 第一部分高等数学


### 第一章 函数、极限、连续


#### (2)有界性

设在某个过程中有两个变量 x和 y，对变量 x在允许范围内的每一个确定的值，变量 y按照某一确定的法则总有相应的值与之对应，则称 y为 x的函数，记为<equation>y = f(x)</equation>.


设函数<equation>y = f(x)</equation>的定义区间<equation>I</equation>关于原点对称，如果对于<equation>I</equation>内任意一点<equation>x</equation>，恒有<equation>f(-x) = f(x)</equation>，则称<equation>f(x)</equation>为区间<equation>I</equation>内的偶函数；如果恒有<equation>f(-x) = -f(x)</equation>，则称<equation>f(x)</equation>为区间<equation>I</equation>内的奇函数.


设函数<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>M</equation>，当<equation>x \in I</equation>时，恒有<equation>f(x) \leqslant M</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有上界；设函数<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>m</equation>，当<equation>x \in I</equation>时，恒有<equation>f(x) \geqslant m</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有下界；设函数

---


#### （3）初等函数

<equation>f(x)</equation>在<equation>I</equation>上有定义，如果存在常数<equation>M > 0</equation>，当<equation>x\in I</equation>时，恒有<equation>|f(x)|\leqslant M</equation>，则称<equation>f(x)</equation>在<equation>I</equation>上有界.


设函数<equation>f(x)</equation>在区间<equation>I</equation>上有定义，若存在<equation>T > 0</equation>，对任意的<equation>x\in I</equation>，必有<equation>x\pm T\in I</equation>，并且<equation>f(x + T) = f(x)</equation>，则称<equation>f(x)</equation>为周期函数.使得上述关系式成立的最小正数<equation>T</equation>称为<equation>f(x)</equation>的最小正周期，简称为函数<equation>f(x)</equation>的周期.


设函数<equation>f(x)</equation>在区间<equation>I</equation>内有定义，如果对于该区间内的任意两点<equation>x_{1} < x_{2}</equation>，恒有<equation>f(x_{1}) < f(x_{2})</equation>（或<equation>f(x_{1}) > f(x_{2})</equation>），则称<equation>f(x)</equation>在区间<equation>I</equation>内单调增加（或单调减少）。


设函数<equation>y = f(x)</equation>的定义域为<equation>D</equation>，值域为<equation>R</equation>.若对任意<equation>y\in R</equation>，有唯一确定的<equation>x\in D</equation>，使得<equation>y = f(x)</equation>，则记为<equation>x = f^{-1}(y)</equation>，称其为<equation>y = f(x)</equation>的反函数.


若函数<equation>u = \varphi (x)</equation>在<equation>x_{0}</equation>处有定义，函数<equation>y = f(u)</equation>在<equation>u_{0} = \varphi (x_{0})</equation>处有定义，则函数<equation>y = f[\varphi (x)]</equation>在<equation>x_{0}</equation>处有定义，称<equation>y = f[\varphi (x)]</equation>是由函数<equation>y = f(u)</equation>和<equation>u = \varphi (x)</equation>复合而成的复合函数，<equation>u</equation>为中间变量.


由六类基本初等函数经过有限次四则运算及有限

---


#### （5）隐函数

次复合运算得到的，并能用一个数学表达式表示的函数，称为初等函数.

注 六类基本初等函数为：

<equation>y=C</equation>（常数）；

<equation>y=x^{n}</equation>；

<equation>y=a^{x}</equation>（<equation>a>0</equation>且<equation>a\neq1)</equation>；

<equation>y=\log_{a} x</equation>（<equation>a>0</equation>且<equation>a\neq1)</equation>；

<equation>y=\sin x,\cos x,\tan x,\cot x,\sec x,\csc x;</equation>

<equation>y=\arcsin x,\arccos x,\arctan x,\arccot x.</equation>


在定义域内的不同范围用不同表达式表示的函数称为分段函数.

注 常见的分段函数有：

<equation>\textcircled{1}</equation>绝对值函数<equation>|x|=\left\{ \begin{array}{ll} x, & x\geqslant 0, \\ -x, & x<0. \end{array} \right.</equation>

<equation>\textcircled{2}</equation>符号函数<equation>\operatorname{sgn} x=\left\{ \begin{array}{ll} 1, & x>0, \\ 0, & x=0, \\ -1, & x<0. \end{array} \right.</equation>

<equation>\textcircled{3}</equation>取整函数<equation>[x]</equation>表示不超过 x的最大整；


如果在方程<equation>F(x,y) = 0</equation>中，当<equation>x</equation>取某区间内的任一值时，相应地总有满足这一方程的唯一的<equation>y</equation>值存在，

---


#### (1)唯一性

那么就说方程 F(x,y)=0在该区间内确定了一个隐函数 y=y(x).


若对于任意给定的正数<equation>\varepsilon</equation>，总存在正整数<equation>N</equation>，当<equation>n > N</equation>时，恒有<equation>|x_{n} - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>n\to \infty</equation>时数列<equation>x_{n}</equation>的极限，记为<equation>\lim x_n = A</equation>


设函数<equation>f(x)</equation>在<equation>|x|</equation>充分大时都有定义，若对于任意给定的正数<equation>\varepsilon</equation>，总存在正数<equation>X</equation>，当<equation>|x| > X</equation>时，恒有<equation>|f(x) - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>x\to \infty</equation>时函数<equation>f(x)</equation>的极限，记为<equation>\lim f(x) = A</equation>。


设函数<equation>f(x)</equation>在<equation>x_0</equation>的某个去心邻域内有定义，若对于任意给定的正数<equation>\varepsilon</equation>，总存在正数<equation>\delta</equation>，当<equation>0 < |x - x_0| < \delta</equation>时，恒有<equation>|f(x) - A| < \varepsilon</equation>，则称常数<equation>A</equation>为当<equation>x \rightarrow x_0</equation>时函数<equation>f(x)</equation>的极限，记为<equation>\lim f(x) = A</equation>。


设<equation>\lim_{x\to x_0}f(x) = A,</equation><equation>\lim_{x\to x_0}f(x) = B,</equation>则<equation>A = B.</equation>

---


#### （1）极限的四则运算法则

若<equation>\lim_{x\to x_0}f(x)</equation>存在，则存在<equation>\delta > 0</equation>，使<equation>f(x)</equation>在<equation>U = \{x|0\leqslant |x - x_0| < \delta \}</equation>内有界.


<equation>\textcircled{1}</equation>若<equation>\lim_{x\to x_0}f(x) = A > 0</equation>，则存在<equation>x_0</equation>的一个去心邻域，在该邻域内恒有<equation>f(x) > 0.</equation>

<equation>\textcircled{2}</equation>若存在<equation>x_0</equation>的一个去心邻域，在该邻域内<equation>f(x) > 0</equation>且<equation>\lim_{x\to x_0}f(x)</equation>存在，则<equation>\lim_{x\to x_0}f(x)\geqslant 0.</equation>


设在<equation>x_0</equation>的某个去心邻域内恒有<equation>g(x)\leqslant f(x)\leqslant h(x)</equation>，且<equation>\lim_{x\to x_0}g(x) = \lim_{x\to x_0}h(x) = A</equation>，则<equation>\lim_{x\to x_0}f(x) = A.</equation>

同理，若存在<equation>M > 0</equation>，使得<equation>|x| > M</equation>时，恒有<equation>g(x)\leqslant f(x)\leqslant h(x)</equation>，且<equation>\lim_{x\to \infty}g(x) = \lim_{x\to \infty}h(x) = A</equation>，则<equation>\lim_{x\to \infty}f(x) = A.</equation>


单调有界数列（函数）必有极限


(1)<equation>\lim_{x\to 0}\frac{\sin x}{x}=1.</equation>

(2)<equation>\lim_{x\to 0}(1+x)^{\frac{1}{x}}=\mathrm{e}.</equation>

---

设<equation>\lim_{x\to x_1}f(x)\stackrel{\text{存在}}{=}A,\lim_{x\to x_1}g(x)\stackrel{\text{存在}}{=}B</equation>，则

<equation>\textcircled{2}</equation><equation>\lim_{x\to x_0}[f(x)g(x)]=A\cdot B.</equation>

<equation>\textcircled{3} \lim_{x \to x_-} \frac{f(x)}{g(x)} = \frac{A}{B}</equation><equation>(B \neq 0).</equation>

(2) 一些特殊情形下的运算结论

<equation>\textcircled{1}</equation>若<equation>\lim_{x\to x}f(x) = +\infty ,\lim_{x\to x}g(x) = +\infty</equation>，则

<equation>\lim _ {x \rightarrow x _ {0}} [ f (x) + g (x) ] = + \infty .</equation>

<equation>\textcircled{2}</equation>若<equation>\lim_{x\to x_0}f(x) = -\infty ,\lim_{x\to x_0}g(x) = -\infty</equation>，则

<equation>\lim _ {x \rightarrow x _ {1}} [ f (x) + g (x) ] = - \infty .</equation>

<equation>\textcircled{3}</equation>若<equation>\lim_{x\to x_{0}}f(x)=0,g(x)</equation>在<equation>x_{0}</equation>的某个去心邻域内有界，则

<equation>\lim _ {x \rightarrow x _ {1}} [ f (x) g (x) ] = 0.</equation>

<equation>\textcircled{4}</equation>若<equation>\lim_{x\to x_{0}}f(x)=\infty</equation>，g(x)在<equation>x_{0}</equation>的某个去心邻域内有界，则

<equation>\lim _ {x \rightarrow x _ {0}} [ f (x) \pm g (x) ] = \infty .</equation>

<equation>\textcircled{5}</equation>若<equation>\lim_{x\to x_0}f(x)\stackrel{\text{存在}}{=}A\neq 0,\lim_{x\to x_0}g(x)=0</equation>，则

<equation>\lim _ {x \rightarrow x _ {0}} \frac {f (x)}{g (x)} = \infty .</equation>

---


#### 4. 无穷小量的比较

如果<equation>\lim_{x\to x_{0}}f(x)=0</equation>，则称函数 f(x)是<equation>x\to x_{0}</equation>时的无穷小量.


<equation>\textcircled{1}</equation>有限多个无穷小量的和、差、积仍然是无穷小量.

<equation>\textcircled{2}</equation>有界函数与无穷小量的乘积还是无穷小量.


<equation>\lim_{x\to x_0}f(x) = A</equation>的充分必要条件为<equation>f(x) = A + \alpha (x)</equation>其中<equation>\lim_{x\to x_0}\alpha (x) = 0.</equation>


设<equation>\alpha (x),\beta (x)</equation>是同一自变量变化过程中的无穷小量，<equation>\beta (x)\neq 0</equation>，且<equation>\lim \frac{\alpha (x)}{\beta (x)}</equation>也是此变化过程中的极限，则

<equation>\textcircled{1}</equation>若<equation>\lim \frac{\alpha (x)}{\beta (x)} = C (C</equation>为常数，且<equation>C\neq 0)</equation>，则称<equation>\alpha (x)</equation>与<equation>\beta (x)</equation>为同阶无穷小量；

<equation>\textcircled{2}</equation>若<equation>\lim \frac{\alpha(x)}{\beta(x)} = 1</equation>，则称<equation>\alpha(x)</equation>与<equation>\beta(x)</equation>为等价无穷小量，记作<equation>\alpha(x)\sim \beta(x)</equation>；

---


#### 7. 无穷大量的定义

<equation>\textcircled{3}</equation>若<equation>\lim\frac{\alpha (x)}{\beta (x)}=0</equation>，则称<equation>\alpha (x)</equation>是比<equation>\beta (x)</equation>高阶的无穷小量，记作<equation>\alpha (x)=o(\beta (x))</equation>；

<equation>\textcircled{4}</equation>若<equation>\lim\frac{\alpha (x)}{\beta (x)}=\infty</equation>，则称<equation>\alpha (x)</equation>是比<equation>\beta (x)</equation>低阶的无穷小量.


设<equation>\alpha (x),\beta (x),\tilde{\alpha}(x),\tilde{\beta}(x)</equation>都是同一自变量变化过程中的无穷小量，且<equation>\alpha (x)\sim \tilde{\alpha}(x),\beta (x)\sim \tilde{\beta}(x)</equation>，则

<equation>\begin{array}{l} \lim \frac {\alpha (x) f (x)}{\beta (x) g (x)} = \lim \frac {\tilde {\alpha} (x) f (x)}{\beta (x) g (x)} = \lim \frac {\alpha (x) f (x)}{\tilde {\beta} (x) g (x)} \\ = \lim \frac {\tilde {\alpha} (x) f (x)}{\tilde {\beta} (x) g (x)}. \\ \end{array}</equation>


设<equation>\alpha ,\beta</equation>都是同一自变量变化过程中的无穷小量，若存在<equation>k > 0</equation>，使得<equation>\lim \frac{\alpha}{\beta^k} = C(C</equation>为非零的常数），则称在同一自变量变化过程中<equation>\alpha</equation>是<equation>\beta</equation>的<equation>k</equation>阶无穷小量.


任给<equation>M > 0</equation>，存在正数<equation>\delta</equation>，当<equation>0 < |x - x_0| < \delta</equation>时，恒有<equation>|f(x)| > M</equation>，则称<equation>x\to x_0</equation>时<equation>f(x)</equation>是无穷大量，记为<equation>\lim_{x\to x_0} f(x) = \infty</equation>.

---


#### (2)左、右连续的定义

在自变量的同一变化过程中，如果<equation>f(x)</equation>为无穷大量，则<equation>\frac{1}{f(x)}</equation>为无穷小量；反之，如果<equation>f(x)</equation>为无穷小量，且<equation>f(x)\neq 0</equation>，则<equation>\frac{1}{f(x)}</equation>为无穷大量.


(1) 连续的定义

<equation>\textcircled{1}</equation>设函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的某个邻域内有定义，若

<equation>\lim _ {\Delta x \rightarrow 0} \Delta y = \lim _ {\Delta x \rightarrow 0} \left[ f \left(x _ {0} + \Delta x\right) - f \left(x _ {0}\right)\right] = 0,</equation>

则称<equation>f(x)</equation>在点<equation>x_{0}</equation>处连续.

<equation>\textcircled{2}</equation>设函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的某个邻域内有定义，若

<equation>\lim _ {x \rightarrow x _ {0}} f (x) = f \left(x _ {0}\right),</equation>

则称<equation>f ( x )</equation>在点<equation>x_{0}</equation>处连续.


设<equation>f ( x )</equation>在点<equation>x_{0}</equation>的左侧（或右侧）某邻域（包括点<equation>x_{0}</equation>）有定义，并且

<equation>\lim _ {x \rightarrow x _ {0}} f (x) = f \left(x _ {0}\right),</equation>

则称<equation>f ( x )</equation>在点<equation>x_{0}</equation>处左连续（或右连续）.

函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处连续的充要条件是<equation>f(x)</equation>在点

---


#### (2) 间断点的分类

<equation>x_{0}</equation>处既左连续又右连续


若函数<equation>f(x), g(x)</equation>在点<equation>x_0</equation>处连续，则<equation>f(x)\pm g(x), f(x)\cdot g(x), \frac{f(x)}{g(x)} (g(x_0)\neq 0)</equation>在点<equation>x_0</equation>处也连续.


若函数<equation>u = \varphi (x)</equation>在点<equation>x_0</equation>处连续，函数<equation>y = f(u)</equation>在点<equation>u_0 = \varphi (x_0)</equation>处连续，则函数<equation>y = f[\varphi (x)]</equation>在点<equation>x_0</equation>处连续.


设函数<equation>y = f(x)</equation>在区间<equation>(a,b)</equation>内为单调的连续函数，其值域为<equation>(m,n)</equation>，则其反函数<equation>x = f^{-1}(y)</equation>在区间<equation>(m,n)</equation>内也是连续的.

一切初等函数在其定义区间内都是连续的.


若函数<equation>f(x)</equation>在点<equation>x_{0}</equation>的任何邻域内总有异于<equation>x_{0}</equation>而属于函数<equation>f(x)</equation>定义域内的点，且函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处不连续，则称<equation>x_{0}</equation>是<equation>f(x)</equation>的一个间断点.


左、右极限都存在的间断点称为第一类间断点.其

---


#### (3)零点定理

中，左、右极限都存在且相等的间断点称为可去间断点；左、右极限都存在且不相等的间断点称为跳跃间断点.

左、右极限至少有一个不存在的间断点称为第二类间断点. 若<equation>x\to x_0^{-}</equation>或<equation>x\to x_0^{+}</equation>时，<equation>f(x)\rightarrow \infty</equation>，则称<equation>x_0</equation>为<equation>f(x)</equation>的无穷间断点.


如果函数<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，则在该区间上至少存在两点<equation>x_{1}, x_{2}</equation>，使得对于任意的<equation>x \in [a,b]</equation>，恒有<equation>f(x_{1}) \leqslant f(x) \leqslant f(x_{2})</equation>。


如果函数<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，<equation>m,M</equation>是<equation>f(x)</equation>在该区间上的最小值与最大值，则对任意的<equation>\mu \in [m,M]</equation>在<equation>[a,b]</equation>上至少存在一点<equation>\xi</equation>，满足<equation>f(\xi) = \mu</equation>


如果<equation>f(x)</equation>在闭区间<equation>[a,b]</equation>上连续，且满足<equation>f(a)\cdot f(b) < 0</equation>，则在开区间（a,b）内至少存在一点<equation>\xi</equation>，使得<equation>f(\xi) = 0.</equation>

---


### 第二章 一元函数微分学


#### 一、导数与微分

1. 导数的定义式

<equation>\begin{array}{l} f ^ {\prime} \left(x _ {0}\right) = \frac {\mathrm {d} y}{\mathrm {d} x} \Bigg | _ {x = x _ {0}} = \lim _ {\Delta x \rightarrow 0} \frac {f \left(x _ {0} + \Delta x\right) - f \left(x _ {0}\right)}{\Delta x} \\ = \lim _ {x \rightarrow x _ {0}} \frac {f (x) - f \left(x _ {0}\right)}{x - x _ {0}}. \\ \end{array}</equation>

2. 微分的定义式

若<equation>\Delta y = A\Delta x + o(\Delta x)</equation>，则<equation>\mathrm{d}y = A\Delta x.</equation>

3. 可微的充要条件

可导<equation>\Leftrightarrow</equation>可微，<equation>\mathrm{d}y = f^{\prime}(x)\mathrm{d}x.</equation>

4. 可导与连续的关系

<equation>f(x)</equation>在<equation>x_{0}</equation>点可导<equation>\Rightarrow f(x)</equation>在<equation>x_{0}</equation>点处连续.

5. 可导、可微、连续等的关系

可微<equation>\Leftrightarrow</equation>可导<equation>\Rightarrow</equation>函数连续<equation>\Rightarrow \lim_{x\to x_0} f(x)</equation>存在<equation>\Rightarrow f(x)</equation>在<equation>x_0</equation>点的某邻域内有界.

---


#### 1. 基本初等函数的导数公式

<equation>\textcircled{1}</equation><equation>( C )^{\prime}=0</equation>（C为常数）；

<equation>\textcircled{2}</equation><equation>( x^{a} )^{\prime}=\alpha x^{a-1}</equation>（<equation>\alpha</equation>为实数）；

<equation>\textcircled{3}</equation><equation>( a^{x} )^{\prime}=a^{x} \ln a</equation><equation>( a>0,a\neq1)</equation>

<equation>\textcircled{4} \left( \mathrm{e}^{x} \right)^{\prime}=\mathrm{e}^{x};</equation>

<equation>\textcircled{5}</equation><equation>(\log_{a} x)^{\prime} = \frac{1}{x \ln a}</equation>（<equation>a > 0,a\neq 1</equation>）；

<equation>\textcircled{6}</equation><equation>(\ln x)^{\prime}=\frac{1}{x};</equation>

<equation>\textcircled{7}</equation><equation>(\sin x)^{\prime}=\cos x;</equation>

<equation>\textcircled{8}</equation><equation>(\cos x)^{\prime}=-\sin x;</equation>

<equation>\textcircled{9}</equation><equation>(\tan x)^{\prime}=\frac{1}{\cos^{2} x}</equation>;

<equation>\textcircled{1 0} \left( \cot x \right)^{\prime}=-\frac{1}{\sin^{2} x};</equation>

<equation>\textcircled{11}</equation><equation>(\sec x)^{\prime}=\sec x\tan x;</equation>

<equation>\textcircled{12} (\csc x)^{\prime} = -\csc x\cot x;</equation>

<equation>\textcircled{1 3}</equation><equation>\operatorname{a r c s i n} x )^{\prime}=\frac{1}{\sqrt{1-x^{2}}}</equation>

<equation>\textcircled{14} (\arccos x)^{\prime} = -\frac{1}{\sqrt{1-x^{2}}}</equation>;

---


#### 5. 隐函数的导数

<equation>\textcircled{15}</equation><equation>(\arctan x)^{\prime}=\frac{1}{1+x^{2}}</equation>

<equation>\textcircled{16} (\operatorname{arccot} x)^{\prime}=-\frac{1}{1+x^{2}}.</equation>


设 u(x), v(x)都可导，则

<equation>\textcircled{1}</equation><equation>( u \pm v )^{\prime}=u^{\prime} \pm v^{\prime}</equation>

<equation>\textcircled{2}</equation><equation>(uv)^{\prime} = u^{\prime}v + uv^{\prime}</equation>，特别地，有<equation>(cu)^{\prime} = cu^{\prime}</equation>（<equation>c</equation>为常数）；

<equation>\textcircled{3} \left( \frac{u}{v} \right)^{\prime}=\frac{u^{\prime} v-u v^{\prime}}{v^{2}} \quad(v \neq 0).</equation>


设<equation>u = \varphi (x)</equation>在<equation>x</equation>处可导，<equation>y = f(u)</equation>在对应的<equation>u = \varphi (x)</equation>处可导，则复合函数<equation>y = f[\varphi (x)]</equation>在<equation>x</equation>处可导，且

<equation>\{f[\varphi(x)]\}' = f'(u)\varphi'(x)</equation>，即<equation>\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}u} \cdot \frac{\mathrm{d}u}{\mathrm{d}x}</equation>.


若<equation>x = \varphi (y)</equation>在某区间内单调、可导，且<equation>\varphi^{\prime}(y)\neq 0</equation>，则其反函数<equation>y = f(x)</equation>在对应的区间内也可导，且<equation>f^{\prime}(x) = \frac{1}{\varphi^{\prime}(y)}</equation>


设<equation>y = y(x)</equation>是由方程<equation>F(x,y) = 0</equation>确定的可导函数，方程两端同时对<equation>x</equation>求导，遇到<equation>y</equation>的函数则视为复合

---


#### （2）高阶导数的运算法则

函数，y为中间变量，可得到一个含<equation>y^{\prime}</equation>的方程，从中解出<equation>y^{\prime}</equation>即可.


如果<equation>y^{\prime} = f^{\prime}(x)</equation>作为<equation>x</equation>的函数在点<equation>x</equation>可导，则<equation>y^{\prime}</equation>的导数称为<equation>y = f(x)</equation>的二阶导数，记为<equation>y^{\prime \prime}</equation>，或<equation>f^{\prime \prime}(x)</equation>，或<equation>\frac{\mathrm{d}^2y}{\mathrm{d}x^2}</equation>.

一般地，函数<equation>y = f(x)</equation>的<equation>n</equation>阶导数为<equation>y^{(n)} = [y^{(n - 1)}]'</equation>，也可写作<equation>f^{(n)}(x)</equation>或<equation>\frac{\mathrm{d}^n y}{\mathrm{d}x^n}</equation>.


设<equation>u=u ( x )</equation><equation>v=v ( x ) n</equation>阶可导，则

<equation>\textcircled{1}</equation><equation>(u \pm v)^{(n)} = u^{(n)} \pm v^{(n)}</equation>;

<equation>\textcircled{2}</equation><equation>( C u ) ^{ ( n )}=C u ^{ ( n )}</equation>（C为常数）；

<equation>\textcircled{3} ( u v )^{ ( n )}=\mathrm{C}_{n}^{0} u^{ ( n )} v+\mathrm{C}_{n}^{1} u^{ ( n-1 )} v^{\prime}+\dots+\mathrm{C}_{n}^{n-1} u^{\prime} v^{ ( n-1 )}+\mathrm{C}_{n}^{n} u v^{ ( n )}</equation>（莱布尼茨公式）.

(3) 几个常见初等函数的<equation>n</equation>阶导数公式

<equation>\textcircled{1}</equation><equation>(a^{x})^{(n)} = a^{x} \cdot \ln^{n} a</equation>;

---


#### 2. 拉格朗日中值定理

<equation>\textcircled{4} \left( \frac{1}{a x+b} \right)^{(n)}=\frac{(-1)^{n} a^{n} n!}{(a x+b)^{n+1}};</equation>


设<equation>y = y(x)</equation>是由参数方程<equation>\left\{ \begin{array}{l} x = \varphi (t), \\ y = \psi (t) \end{array} \right.</equation>（<equation>\alpha < t < \beta</equation>）确定的函数. 则

<equation>\textcircled{1}</equation>若<equation>\varphi (t),\psi (t)</equation>都可导，且<equation>\varphi^{\prime}(t)\neq 0</equation>，则

<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = \frac {\psi^ {\prime} (t)}{\varphi^ {\prime} (t)}.</equation>

<equation>\textcircled{2}</equation>若<equation>\varphi(t),\psi(t)</equation>二阶可导，且<equation>\varphi^{\prime}(t)\neq 0</equation>，则

<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = \frac {\psi^ {\prime \prime} (t) \varphi^ {\prime} (t) - \psi^ {\prime} (t) \varphi^ {\prime \prime} (t)}{\left[ \varphi^ {\prime} (t) \right] ^ {3}}.</equation>


设 f(x)在闭区间<equation>[a,b]</equation>上连续，在开区间（a,b）内可导，若<equation>f(a) = f(b)</equation>，则至少存在一点<equation>\xi\in( a,b)</equation>，使得

<equation>f ^ {\prime} (\xi) = 0.</equation>


设 f(x)在闭区间<equation>[a,b]</equation>上连续，在开区间（a,b）内可导，则至少存在一点<equation>\xi\in(a,b)</equation>，使得

---


#### (2) 带皮亚诺余项的泰勒定理

<equation>f (b) - f (a) = f ^ {\prime} (\xi) (b - a).</equation>


设<equation>f(x),g(x)</equation>在闭区间<equation>[a,b]</equation>上连续，在开区间<equation>(a,b)</equation>内可导，且<equation>g^{\prime}(x)\neq 0,x\in(a,b)</equation>，则至少存在一点<equation>\xi \in (a,b)</equation>，使得

<equation>\frac {f (b) - f (a)}{g (b) - g (a)} = \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)}.</equation>


设<equation>f(x)</equation>在点<equation>x_{0}</equation>的某一邻域内有直到<equation>n + 1</equation>阶的导数，则对该邻域内的任意点<equation>x</equation>，都有

<equation>\begin{array}{l} f (x) = f \left(x _ {0}\right) + \frac {f ^ {\prime} \left(x _ {0}\right)}{1 !} \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \\ \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + \frac {f ^ {(n + 1)} (\xi)}{(n + 1) !} \left(x - x _ {0}\right) ^ {n + 1}, \\ \end{array}</equation>

其中<equation>\xi</equation>介于 x，<equation>x_{0}</equation>之间.


设<equation>f(x)</equation>在点<equation>x_{0}</equation>的某一邻域内有直到<equation>n</equation>阶的导数，则对该邻域内的任意点<equation>x</equation>，都有

<equation>\begin{array}{l} f (x) = f \left(x _ {0}\right) + \frac {f ^ {\prime} \left(x _ {0}\right)}{1 !} \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \\ \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + o \left(x - x _ {0}\right) ^ {n}. \\ \end{array}</equation>

---


#### 四、洛必达法则

(3) 几个常用函数的带皮亚诺余项的麦克劳林展开式

<equation>\mathrm {e} ^ {x} = 1 + x + \frac {x ^ {2}}{2 !} + \dots + \frac {x ^ {n}}{n !} + o \left(x ^ {n}\right).</equation>

<equation>\sin x = x - \frac {1}{3 !} x ^ {3} + \dots + \frac {(- 1) ^ {n}}{(2 n + 1) !} x ^ {2 n + 1} + o \left(x ^ {2 n + 1}\right),</equation>

<equation>\cos x = 1 - \frac {x ^ {2}}{2 !} + \dots + (- 1) ^ {n} \frac {x ^ {2 n}}{(2 n) !} + o \left(x ^ {2 n}\right),</equation>

<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} - \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + o \left(x ^ {n}\right),</equation>

<equation>\begin{array}{l} (1 + x) ^ {m} = 1 + m x + \frac {m (m - 1)}{2 !} x ^ {2} + \dots + \\ \frac {m (m - 1) \cdots (m - n + 1)}{n !} x ^ {n} + o \left(x ^ {n}\right). \\ \end{array}</equation>


1. 求“<equation>\frac{0}{0}</equation>”型未定式极限的洛必达法则设<equation>\textcircled{1}\lim_{x\to x_0}f(x) = 0,\lim_{x\to x_0}g(x) = 0</equation>；

<equation>\textcircled{2} f ( x ) , g ( x )</equation>在<equation>x_{0}</equation>的某去心邻域内可导，且<equation>g^{\prime}(x)\neq0;</equation>

<equation>\textcircled{3}</equation><equation>\lim_{x\to x_1}\frac{f'(x)}{g'(x)} = A</equation>或为<equation>\infty</equation>

---


#### (1)定义

则<equation>\lim_{x\to x_0}\frac{f(x)}{g(x)} = \lim_{x\to x_0}\frac{f'(x)}{g'(x)}</equation>.


设<equation>\textcircled{1}\lim_{x\to x_1}f(x) = \infty ,\lim_{x\to x_1}g(x) = \infty ;</equation>

<equation>\textcircled{2} f ( x )</equation>, g ( x ) 在<equation>x_{0}</equation>的某去心邻域内可导，且<equation>g^{\prime}(x)\neq0;</equation>

<equation>\textcircled{3} \lim_{x \to x_0} \frac{f^{\prime}(x)}{g^{\prime}(x)} = A</equation>或为<equation>\infty,</equation>

则<equation>\lim_{x\to x_1}\frac{f(x)}{g(x)} = \lim_{x\to x_1}\frac{f'(x)}{g'(x)}</equation>.


设<equation>f(x)</equation>在区间 I 上满足<equation>f^{\prime}(x)\geqslant 0</equation>（或<equation>f^{\prime}(x)\leqslant 0</equation>），且不在任意子区间上恒取等号，则<equation>f(x)</equation>在区间 I 上单调增加（或单调减少）.


设函数<equation>y = f(x)</equation>在点<equation>x_0</equation>的某个邻域内有定义.如果对于该邻域内任何异于<equation>x_0</equation>的点<equation>x</equation>，恒有<equation>f(x) < f(x_0)</equation>（或<equation>f(x) > f(x_0)</equation>），则称<equation>x_0</equation>为<equation>f(x)</equation>的一个极大值点（或极小值点），称<equation>f(x_0)</equation>为<equation>f(x)</equation>的极大值（或极小值).

---

设<equation>f(x)</equation>在<equation>x_0</equation>点取极值，且<equation>f^{\prime}(x_0)</equation>存在，则<equation>f^{\prime}(x_0) = 0.</equation>


设<equation>f(x)</equation>在<equation>x_{0}</equation>处连续，在<equation>x = x_{0}</equation>的去心邻域内可导，则

(a) 若在<equation>x_0</equation>的左侧邻域内<equation>f^{\prime}(x) > 0</equation>，右侧邻域内<equation>f^{\prime}(x) < 0</equation>，则<equation>f(x_0)</equation>为极大值.

(b)若在<equation>x_{0}</equation>的左侧邻域内<equation>f^{\prime}(x) < 0</equation>，右侧邻域内<equation>f^{\prime}(x) > 0</equation>，则<equation>f(x_{0})</equation>为极小值.

(c) 若在<equation>x = x_{0}</equation>的左、右邻域内<equation>f^{\prime}(x)</equation>同号，则<equation>f(x_{0})</equation>不是极值.


设<equation>f(x)</equation>在<equation>x_{0}</equation>处有二阶导数，<equation>f^{\prime}(x_{0}) = 0,f^{\prime \prime}(x_{0})\neq 0</equation>则

(a)当<equation>f^{\prime \prime} \left(x_{0}\right) > 0</equation>时，函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处取得极小值.

(b)当<equation>f^{\prime \prime} \left(x_{0}\right) < 0</equation>时，函数<equation>f(x)</equation>在点<equation>x_{0}</equation>处取得极大值.


设函数<equation>y = f(x)</equation>在区间<equation>(a,b)</equation>内可导，<equation>x_{0}</equation>是<equation>(a,b)</equation>内任一点. 若曲线弧上点<equation>(x_{0},f(x_{0}))</equation>处的切线总位于

---


#### 5. 渐近线

曲线弧的下方，则称此曲线弧在<equation>(a,b)</equation>内是凹的；若曲线弧上点<equation>(x_0,f(x_0))</equation>处的切线总位于曲线弧的上方，则称此曲线弧在<equation>(a,b)</equation>内是凸的.


设<equation>f(x)</equation>在区间<equation>I</equation>上满足<equation>f^{\prime \prime}(x) \geqslant 0</equation>（或<equation>f^{\prime \prime}(x) \leqslant 0</equation>），且不在任一子区间上恒取等号，则曲线<equation>y = f(x)</equation>在区间<equation>I</equation>上是凹（或凸）的.


连续曲线弧上凹、凸部分的分界点称为曲线弧的拐点.


设点<equation>(x_{0}, f(x_{0}))</equation>为曲线<equation>y = f(x)</equation>的拐点，且<equation>f^{\prime \prime}(x_{0})</equation>存在，则<equation>f^{\prime \prime}(x_0) = 0.</equation>


设<equation>f(x)</equation>在<equation>x_{0}</equation>点的某邻域内二阶可导，并且在<equation>x_{0}</equation>的左、右邻域内<equation>f^{\prime \prime}(x)</equation>反号，则点<equation>(x_0,f(x_0))</equation>是曲线<equation>y = f(x)</equation>的拐点.


<equation>\textcircled{1}</equation>若<equation>\lim_{x\to +\infty}f(x)=C</equation>（或<equation>\lim_{x\to -\infty}f(x)=C)</equation>，则直线 y=C叫做曲线 y=f(x)的一条水平渐近线.

<equation>\textcircled{2}</equation>若<equation>\lim_{x\to x_0^+}f(x) = \infty</equation>（或<equation>\lim_{x\to x_0^+}f(x) = \infty</equation>），则直线<equation>x =</equation>

---


#### 3. 曲率半径

<equation>x_0</equation>叫做曲线<equation>y = f(x)</equation>的一条垂直渐近线.

<equation>\textcircled{3}</equation>若<equation>\lim_{x\to +\infty}[f(x) - ax - b] = 0</equation>（或<equation>\lim_{x\to -\infty}[f(x) - ax - b] = 0</equation>）<equation>(a\neq 0)</equation>，则直线<equation>y = ax + b</equation>叫做曲线<equation>y = f(x)</equation>的一条斜渐近线.


设<equation>y = f(x)</equation>是平面内的光滑曲线，则弧微分

<equation>\mathrm {d} s = \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x;</equation>

若曲线方程为<equation>\left\{ \begin{array}{l}x = x(t),\\ y = y(t), \end{array} \right.</equation>则弧微分

<equation>\mathrm {d} s = \sqrt {\left[ x ^ {\prime} (t) \right] ^ {2} + \left[ y ^ {\prime} (t) \right] ^ {2}} \mathrm {d} t.</equation>


曲线<equation>y = f(x)</equation>上任一点<equation>(x,f(x))</equation>处的曲率为

<equation>K = \frac {\left| y ^ {\prime \prime} \right|}{\left[ 1 + \left(y ^ {\prime}\right) ^ {2} \right] ^ {\frac {3}{2}}};</equation>

曲线<equation>\left\{ \begin{array}{l}x = x(t),\\ y = y(t) \end{array} \right.</equation>上任一点处的曲率为

<equation>K = \frac {\left| x ^ {\prime} (t) y ^ {\prime \prime} (t) - y ^ {\prime} (t) x ^ {\prime \prime} (t) \right|}{\left\{\left[ x ^ {\prime} (t) \right] ^ {2} + \left[ y ^ {\prime} (t) \right] ^ {2} \right\} ^ {\frac {3}{2}}}.</equation>


<equation>R = \frac {1}{K} (K \neq 0).</equation>

---


### 第三章 一元函数积分学


#### 2. 不定积分的基本性质

设函数<equation>f(x)</equation>在区间<equation>I</equation>上有定义，若存在函数<equation>F(x)</equation>，使得在区间<equation>I</equation>上处处有<equation>F^{\prime}(x) = f(x)</equation>，若<equation>\mathrm{d}F(x) = f(x)\mathrm{d}x</equation>，则称<equation>F(x)</equation>是<equation>f(x)</equation>在区间<equation>I</equation>上的一个原函数.


函数<equation>f(x)</equation>在区间 I上的原函数的全体，称为<equation>f(x)</equation>在区间 I上的不定积分，记为<equation>\int f(x)\mathrm{d}x.</equation>


<equation>\textcircled{1}</equation><equation>\left[\int f(x)\mathrm{d}x\right]^{\prime} = f(x)</equation>，或<equation>\mathrm{d}\int f(x)\mathrm{d}x = f(x)\mathrm{d}x</equation>；

<equation>\textcircled{2}\int f^{\prime}(x)\mathrm{d}x = f(x) + C</equation>，或<equation>\int \mathrm{d}f(x) = f(x) + C</equation>

<equation>\textcircled{3}\int kf(x)\mathrm{d}x = k\int f(x)\mathrm{d}x</equation>（<equation>k</equation>为常数，且<equation>k\neq 0</equation>）；

---


#### 3. 不定积分的基本积分公式

<equation>\textcircled{1}</equation><equation>\int x^{a}\mathrm{d}x=\frac{1}{1+\alpha} x^{1+\alpha}+C \quad(\alpha \neq-1);</equation>

<equation>\textcircled{2} \int \frac{1}{x} \mathrm{d} x=\ln | x |+C;</equation>

<equation>\textcircled{3}</equation><equation>\int a^{x}\mathrm{d}x = \frac{a^{x}}{\ln a} +C,\int \mathrm{e}^{x}\mathrm{d}x = \mathrm{e}^{x} +C;</equation>

<equation>\textcircled{4} \int \cos x \mathrm{d} x=\sin x+C;</equation>

<equation>\textcircled{5} \int \sin x \mathrm{d} x=-\cos x+C;</equation>

<equation>\textcircled{6} \int \sec^{2} x \mathrm{d} x=\int \frac{1}{\cos^{2} x} \mathrm{d} x=\tan x+C;</equation>

<equation>\textcircled{8} \int \sec x\tan x\mathrm{d} x=\sec x+C;</equation>

<equation>\textcircled{9} \int \csc x\cot x\mathrm{d} x=-\csc x+C;</equation>

<equation>\textcircled{11} \int \csc x \mathrm{d} x = \ln | \csc x - \cot x | + C;</equation>

<equation>\textcircled{1 2} \int \frac{1}{a^{2}+x^{2}} \mathrm{d} x=\frac{1}{a} \arctan \frac{x}{a}+C,</equation>

<equation>\int \frac {1}{1 + x ^ {2}} \mathrm {d} x = \arctan x + C;</equation>

---


#### 4. 不定积分的计算方法

<equation>\textcircled{1 3} \int \frac {1}{\sqrt {a ^ {2} - x ^ {2}}} \mathrm {d} x = \arcsin \frac {x}{a} + C (a > 0),</equation>

<equation>\int \frac {1}{\sqrt {1 - x ^ {2}}} \mathrm {d} x = \arcsin x + C;</equation>

<equation>\textcircled{1 4} \int \frac {\mathrm {d} x}{a ^ {2} - x ^ {2}} = \frac {1}{2 a} \ln \left| \frac {a + x}{a - x} \right| + C;</equation>

<equation>\textcircled{1 5} \int \frac {1}{\sqrt {x ^ {2} \pm a ^ {2}}} d x = \ln | x + \sqrt {x ^ {2} \pm a ^ {2}} | + C.</equation>


(1) 第一换元积分法（凑微分法）

设<equation>f(u)</equation>有原函数<equation>F(u), u = \varphi(x)</equation>可导，则有

<equation>\begin{array}{l} \int f [ \varphi (x) ] \varphi^ {\prime} (x) \mathrm {d} x = \int f [ \varphi (x) ] \mathrm {d} \varphi (x) \\ = \int f (u) \mathrm {d} u = F (u) + C \\ = F [ \varphi (x) ] + C. \\ \end{array}</equation>

(2) 第二换元积分法

设函数<equation>x = \varphi (t)</equation>具有连续导数，且<equation>\varphi^{\prime}(t)\neq 0</equation>，又设<equation>f[\varphi (t)]\varphi^{\prime}(t)</equation>具有原函数<equation>\Phi (t)</equation>，则有

<equation>\begin{array}{l} \int f (x) \mathrm {d} x = \int f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm {d} t = \Phi (t) + C \\ = \Phi \left[ \varphi^ {- 1} (x) \right] + C. \\ \end{array}</equation>

(3) 分部积分法

设函数<equation>u = u(x), v = v(x)</equation>具有连续导数，则有

---


#### 3. 定积分的性质

<equation>\int u \mathrm {d} v = u v - \int v \mathrm {d} u.</equation>


<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \lim _ {\lambda \rightarrow 0} \sum_ {i = 1} ^ {n} f \left(\xi_ {i}\right) \Delta x _ {i},</equation>

其中<equation>\xi_{i}\in [x_{i - 1},x_{i}]</equation>

<equation>\Delta x _ {i} = x _ {i} - x _ {i - 1},</equation>

<equation>\lambda = \max _ {1 \leqslant i \leqslant n} \left\{\Delta x _ {1}, \Delta x _ {2}, \dots , \Delta x _ {n} \right\}.</equation>


<equation>\textcircled{1}</equation><equation>f(x)</equation>在<equation>[a,b]</equation>上连续<equation>\Rightarrow f(x)</equation>在<equation>[a,b]</equation>上可积；

<equation>\textcircled{2}</equation><equation>f(x)</equation>在<equation>[a,b]</equation>上有界且只有有限个间断点<equation>\Rightarrow f(x)</equation>在<equation>[a,b]</equation>上可积；

<equation>\textcircled{3} f ( x )</equation>在<equation>[ a,b]</equation>上单调有界<equation>\Rightarrow f ( x )</equation>在<equation>[ a,b]</equation>上可积.


设<equation>f ( x )</equation>，<equation>g ( x )</equation>在区间<equation>[ a,b]</equation>上可积，则

<equation>\textcircled{3}</equation><equation>\int_{a}^{b}1\cdot \mathrm{d}x=\int_{a}^{b}\mathrm{d}x=b-a.</equation>

---


#### 4. 重要的定理、公式、关系

<equation>\textcircled{4}</equation>若<equation>f(x)</equation>在由<equation>a,b,c</equation>构成的最大的区间上可积，则

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \int_ {a} ^ {c} f (x) \mathrm {d} x + \int_ {c} ^ {b} f (x) \mathrm {d} x.</equation>

<equation>\textcircled{5}</equation>若在区间<equation>[a,b]</equation>上<equation>f(x)\leqslant g(x)</equation>，则

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x \leqslant \int_ {a} ^ {b} g (x) \mathrm {d} x.</equation>

<equation>\textcircled{6}</equation>如果 f(x)在区间<equation>[a,b]</equation>上的最大值与最小值分别为 M,m，则

<equation>m (b - a) \leqslant \int_ {a} ^ {b} f (x) \mathrm {d} x \leqslant M (b - a).</equation>

此性质称为定积分的估值定理.

<equation>\textcircled{7}</equation>（积分中值定理）如果<equation>f(x)</equation>在区间<equation>[a,b]</equation>上连续，则在<equation>[a,b]</equation>上至少存在一点<equation>\xi</equation>，使

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = f (\xi) (b - a).</equation>

称<equation>\frac{1}{b-a}\int_{a}^{b}f(x)\mathrm{d}x</equation>为函数<equation>y=f(x)</equation>在区间<equation>[a,b]</equation>上的平均值.


(1) 变上限函数的求导定理

设<equation>f(x)</equation>在区间<equation>[a,b]</equation>上连续，则变上限函数<equation>F(x) = \int_{a}^{x} f(t)\mathrm{d}t</equation>在区间<equation>[a,b]</equation>上可导，且<equation>F^{\prime}(x) = f(x)</equation>.

---


#### (3)换元积分法

设<equation>f ( x )</equation>在区间<equation>[ a,b]</equation>上连续，<equation>F ( x )</equation>是它的任一个原函数，则

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = F (x) \Bigg | _ {a} ^ {b} = F (b) - F (a).</equation>

(3) 定积分和不定积分之间的关系

<equation>\int f (x) \mathrm {d} x = \int_ {a} ^ {x} f (t) \mathrm {d} t + C.</equation>


如果<equation>f(x)</equation>在<equation>[a,b]</equation>上连续，并且容易求出它的一个原函数<equation>F(x)</equation>，则

<equation>\left. \int_ {a} ^ {b} f (x) \mathrm {d} x = F (x) \right| _ {a} ^ {b} = F (b) - F (a).</equation>


定积分的分部积分法，其公式与方法和不定积分类似，只是多了个上、下限而已.

<equation>\left. \int_ {a} ^ {b} u (x) \mathrm {d} v (x) = \left[ u (x) v (x) \right] \right| _ {a} ^ {b} - \int_ {a} ^ {b} v (x) \mathrm {d} u (x).</equation>


设<equation>f(x)</equation>在<equation>[a,b]</equation>上连续，函数<equation>x = \varphi(t)</equation>满足条件；

<equation>\textcircled{1} \varphi (\alpha) = a, \varphi (\beta) = b.</equation>

<equation>\textcircled{2}\varphi (t)</equation>在<equation>[\alpha ,\beta ]</equation>或<equation>[\beta ,\alpha ]</equation>上为单值、有连续导数的函

---


#### 6. 有关定积分的重要结论

数，则有

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \int_ {\alpha} ^ {\beta} f [ \varphi (t) ] \varphi^ {\prime} (t) \mathrm {d} t.</equation>


<equation>\textcircled{1}</equation>设<equation>f(x)</equation>是在区间<equation>[-a,a](a > 0)</equation>上连续的偶函数，则

<equation>\int_ {- a} ^ {a} f (x) \mathrm {d} x = 2 \int_ {0} ^ {a} f (x) \mathrm {d} x.</equation>

<equation>\textcircled{2}</equation>设<equation>f(x)</equation>是在区间<equation>[-a,a](a > 0)</equation>上连续的奇函数，则

<equation>\int_ {- a} ^ {a} f (x) \mathrm {d} x = 0.</equation>

<equation>\textcircled{3}</equation>设<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>内是以<equation>T</equation>为周期的连续的周期函数，则对任意常数<equation>a</equation>和任意正整数<equation>n</equation>，都有

<equation>\int_ {a} ^ {a + T} f (x) \mathrm {d} x = \int_ {0} ^ {T} f (x) \mathrm {d} x,</equation>

<equation>\int_ {a} ^ {a + n T} f (x) \mathrm {d} x = n \int_ {0} ^ {T} f (x) \mathrm {d} x.</equation>

<equation>\textcircled{4}</equation>设<equation>f(x)</equation>在<equation>[-1,1]</equation>上连续，则

<equation>\int_ {0} ^ {\frac {\pi}{2}} f (\sin x) \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} f (\cos x) \mathrm {d} x,</equation>

<equation>\int_ {0} ^ {\pi} x f (\sin x) \mathrm {d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} f (\sin x) \mathrm {d} x,</equation>

---


#### 7. 定积分的应用

<equation>\int_ {0} ^ {\pi} f (\sin x) \mathrm {d} x = 2 \int_ {0} ^ {\frac {\pi}{2}} f (\sin x) \mathrm {d} x.</equation>

<equation>\textcircled{5}</equation>华里士公式

<equation>\begin{array}{l} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n} x \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2 n} x \mathrm {d} x \\ = \frac {1}{2} \cdot \frac {3}{4} \cdot \dots \cdot \frac {2 n - 1}{2 n} \cdot \frac {\pi}{2}, \\ \end{array}</equation>

<equation>\begin{array}{l} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n + 1} x \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2 n + 1} x \mathrm {d} x \\ = 1 \cdot \frac {2}{3} \cdot \frac {4}{5} \cdot \dots \cdot \frac {2 n}{2 n + 1}. \\ \end{array}</equation>


(1) 求平面图形的面积

<equation>\textcircled{1}</equation>由曲线<equation>y = f(x), x = a, x = b(a < b)</equation>及<equation>x</equation>轴所围成封闭平面图形的面积为

<equation>S = \int_ {a} ^ {b} | f (x) | \mathrm {d} x.</equation>

<equation>\textcircled{2}</equation>由曲线<equation>y=f(x),y=g(x)</equation>及直线<equation>x=a,x= b(a<b)</equation>所围成封闭平面图形的面积为

<equation>S = \int_ {a} ^ {b} | f (x) - g (x) | \mathrm {d} x.</equation>

<equation>\textcircled{3}</equation>要求由曲线<equation>y = f(x)</equation>与<equation>y = g(x)</equation>所围成的封闭平面图形的面积，需先求出两条曲线的交点，即求解方

---

程组<equation>\left\{ \begin{array}{l l} y=f(x), \\ y=g(x) \end{array} \right.</equation>得出解中 x的最小值记为 a，解中 x的最大值记为 b，则

<equation>S = \int_ {a} ^ {b} | f (x) - g (x) | \mathrm {d} x.</equation>

<equation>\textcircled{4}</equation>在极坐标系下，如果曲线<equation>r = r(\theta),\theta = \alpha ,\theta = \beta (\alpha < \beta)</equation>围成的平面封闭图形面积为 S，则

<equation>S = \int_ {\alpha} ^ {\beta} \frac {1}{2} r ^ {2} (\theta) \mathrm {d} \theta .</equation>

如果曲线<equation>r = r_{1}(\theta),r = r_{2}(\theta),\theta = \alpha ,\theta = \beta (\alpha < \beta)</equation>围成的平面封闭图形面积为S，则

<equation>S = \int_ {a} ^ {\beta} \frac {1}{2} \mid r _ {1} ^ {2} (\theta) - r _ {2} ^ {2} (\theta) \mid \mathrm {d} \theta .</equation>

<equation>\textcircled{5}</equation>曲边由参数方程<equation>\left\{ \begin{array}{l l} x = \varphi (t), \\ y = \psi (t) \end{array} \right.</equation>给出的曲边梯形的面积为

<equation>S = \int_ {a} ^ {b} y \mathrm {d} x \xlongequal {x = \varphi (t)} \int_ {a} ^ {\beta} \psi (t) \cdot \varphi^ {\prime} (t) \mathrm {d} t.</equation>

(2) 求平行截面面积已知的立体体积

若垂直于<equation>x</equation>轴的平面截立体<equation>\Omega</equation>所得截面积是<equation>x</equation>的连续函数<equation>A(x)(a \leqslant x \leqslant b)</equation>，则<equation>\Omega</equation>的体积为

<equation>V = \int_ {a} ^ {b} A (x) \mathrm {d} x, \text {其 中} a < b.</equation>

---


#### （3）求旋转体的体积

<equation>\textcircled{1}</equation>如下图所示的平面图形绕 x轴旋转所得立体的体积为

<equation>V = \int_{a}^{b}\pi f^{2}(x)\mathrm{d}x</equation>，其中<equation>a < b.</equation>

<equation>\textcircled{2}</equation>如下图所示的平面图形绕<equation>x</equation>轴旋转所得立体的体积为

---

<equation>V = \pi \int_ {a} ^ {b} \left[ f ^ {2} (x) - g ^ {2} (x) \right] \mathrm {d} x,</equation>

其中<equation>a < b,f(x)\geqslant g(x)\geqslant 0.</equation>

<equation>\textcircled{3}</equation>如下图所示的平面图形绕 y轴旋转所得立体的体积为

<equation>V = 2 \pi \int_ {a} ^ {b} x \mid f (x) \mid \mathrm {d} x, \text {其 中} 0 \leqslant a \leqslant b.</equation>

<equation>\textcircled{4}</equation>如下图所示的平面图形绕 y轴旋转所得立体的体积为

---


#### （5）求平面曲线段的弧长

<equation>V = 2 \pi \int_ {a} ^ {b} x [ f (x) - g (x) ] \mathrm {d} x,</equation>

其中<equation>0 \leqslant a < b, f(x) \geqslant g(x)</equation>.


<equation>\textcircled{1}</equation>如下图所示的曲线弧绕<equation>x</equation>轴旋转所得旋转曲面的表面积为

<equation>S = 2 \pi \int_ {x} ^ {b} | f (x) | \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x,</equation>

其中 a < b.

<equation>\textcircled{2}</equation>如上图所示的曲线弧绕<equation>y</equation>轴旋转所得旋转曲面的表面积为

<equation>S = 2 \pi \int_ {a} ^ {b} x \sqrt {1 + \left[ f ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x,</equation>

其中<equation>0\leqslant a < b</equation>


<equation>\textcircled{1}</equation>曲线段<equation>y = f(x)</equation>,<equation>a \leqslant x \leqslant b</equation>, 设<equation>f(x)</equation>有连续导

---


#### 三、反常积分

数，则所给平面曲线段的弧长为

<equation>S = \int_ {a} ^ {b} \sqrt {1 + f ^ {\prime 2} (x)} \mathrm {d} x.</equation>

<equation>\textcircled{2}</equation>如果曲线弧段AB的方程可表示为<equation>x=x(t)</equation><equation>y=y(t)(\alpha \leqslant t\leqslant \beta)</equation>，且<equation>x=x(t),y=y(t)</equation>在区间<equation>(\alpha ,\beta)</equation>内有连续导数，则曲线弧<equation>\widehat{AB}</equation>的长度为

<equation>S = \int_ {\alpha} ^ {\beta} \sqrt {x ^ {\prime 2} (t) + y ^ {\prime 2} (t)} \mathrm {d} t.</equation>

<equation>\textcircled{3}</equation>如果曲线弧AB可以用极坐标表示为<equation>r=r(\theta)</equation><equation>(\alpha\leqslant\theta\leqslant\beta)</equation>，则曲线弧长为

<equation>S = \int_ {\alpha} ^ {\beta} \sqrt {r ^ {2} (\theta) + r ^ {\prime 2} (\theta)} \mathrm {d} \theta .</equation>


1. 无穷区间上的反常积分

<equation>\textcircled{1}</equation>设<equation>f(x)</equation>在<equation>[a, +\infty)</equation>上连续，称

<equation>\int_ {a} ^ {+ \infty} f (x) \mathrm {d} x = \lim _ {b \rightarrow + \infty} \int_ {a} ^ {b} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>[a, +\infty)</equation>上的反常积分. 若上式右边的极限存在，称此反常积分收敛；若极限不存在，称此反常积分发散.

<equation>\textcircled{2}</equation>设 f(x)在<equation>(-\infty,b]</equation>上连续，称

<equation>\int_ {- \infty} ^ {b} f (x) \mathrm {d} x = \lim _ {a \rightarrow - \infty} \int_ {a} ^ {b} f (x) \mathrm {d} x</equation>

---


#### 2. 无界函数的反常积分

为<equation>f(x)</equation>在<equation>(-\infty ,b)</equation>上的反常积分. 若上式右边的极限存在，称此反常积分收敛；若极限不存在，称此反常积分发散.

<equation>\textcircled{3}</equation>设<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>内连续，称

<equation>\int_ {- \infty} ^ {+ \infty} f (x) \mathrm {d} x = \int_ {- \infty} ^ {c} f (x) \mathrm {d} x + \int_ {c} ^ {+ \infty} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>内的反常积分.如果反常积分<equation>\int_{-\infty}^{c} f(x)\mathrm{d}x</equation>和<equation>\int_{c}^{+\infty} f(x)\mathrm{d}x</equation>都收敛，则称反常积分<equation>\int_{-\infty}^{+\infty} f(x)\mathrm{d}x</equation>收敛；否则就称反常积分<equation>\int_{-\infty}^{+\infty} f(x)\mathrm{d}x</equation>发散.


<equation>\textcircled{1}</equation>设<equation>f(x)</equation>在<equation>[a,b)</equation>上连续，且<equation>\lim f(x) = \infty</equation>，则称

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \lim _ {\varepsilon \rightarrow 0 ^ {+}} \int_ {a} ^ {b - \varepsilon} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>[a,b)</equation>上的反常积分. 若上式右边的极限存在，称此反常积分收敛；若极限不存在，称此反常积分发散. 使<equation>f(x)\rightarrow \infty</equation>的点<equation>b</equation>称为<equation>f(x)</equation>的奇点（也称瑕点).

<equation>\textcircled{2}</equation>设<equation>f(x)</equation>在<equation>(a,b]</equation>上连续，且<equation>\lim_{x\to \infty}f(x) = \infty</equation>，则称

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \lim _ {\varepsilon \rightarrow 0 ^ {+}} \int_ {a + \varepsilon} ^ {b} f (x) \mathrm {d} x</equation>

为<equation>f(x)</equation>在<equation>[a,b]</equation>上的反常积分. 若上式右边的极限存

---

在，称此反常积分收敛；若极限不存在，称此反常积分发散.

<equation>\textcircled{3}</equation>设<equation>f(x)</equation>在<equation>[a,b]</equation>上除点<equation>c(a < c < b)</equation>外连续，<equation>\lim_{x\to c}f(x) = \infty</equation>，则反常积分<equation>\int_{a}^{b}f(x)\mathrm{d}y</equation>定义为

<equation>\int_ {a} ^ {b} f (x) \mathrm {d} x = \int_ {a} ^ {c} f (x) \mathrm {d} x + \int_ {c} ^ {b} f (x) \mathrm {d} x.</equation>

如果反常积分<equation>\int_{a}^{c} f(x)\mathrm{d}x</equation>和<equation>\int_{c}^{b} f(x)\mathrm{d}x</equation>都收敛，则称反常积分<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>收敛，否则就称反常积分<equation>\int_{a}^{b} f(x)\mathrm{d}x</equation>发散.

---


### 第四章 向量代数和空间解析几何


#### 2. 两向量的夹角

1. 向量的数量积、向量积与混合积

设<equation>\boldsymbol{a}=\{a_{x},a_{y},a_{z}\}</equation><equation>\boldsymbol{b}=\{b_{x},b_{y},b_{z}\}</equation><equation>\boldsymbol{c}=\{c_{x},c_{y},c_{z}\}</equation>，则

(1) 数量积

<equation>\boldsymbol {a} \cdot \boldsymbol {b} = a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {z} b _ {z}.</equation>

(2) 向量积

<equation>\boldsymbol {a} \times \boldsymbol {b} = \left| \begin{array}{c c c} \boldsymbol {i} & \boldsymbol {j} & \boldsymbol {k} \\ a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \end{array} \right|.</equation>

(3) 混合积

<equation>(a \times b) \cdot c = \left| \begin{array}{c c c} a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \\ c _ {x} & c _ {y} & c _ {z} \end{array} \right|.</equation>


(1) 两向量夹角的余弦

---


#### 1. 平面的方程

<equation>\cos \theta = \frac {a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {z} b _ {z}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}} \sqrt {b _ {x} ^ {2} + b _ {y} ^ {2} + b _ {z} ^ {2}}}.</equation>

(2) 两非零向量平行与垂直的条件

<equation>\textcircled{1}</equation>垂直

<equation>a \bot b \Leftrightarrow a \cdot b = 0 \Leftrightarrow a _ {x} b _ {x} + a _ {y} b _ {y} + a _ {x} b _ {z} = 0.</equation>

<equation>\textcircled{2}</equation>平行

<equation>a / / b \Leftrightarrow a \times b = 0 \Leftrightarrow \frac {a _ {x}}{b _ {x}} = \frac {a _ {y}}{b _ {y}} = \frac {a _ {x}}{b _ {x}}.</equation>

(3) 方向余弦

<equation>\textcircled{1}</equation>计算公式

<equation>\cos a = \frac {a _ {x}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}}},</equation>

<equation>\cos \beta = \frac {a _ {y}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}}},</equation>

<equation>\cos \gamma = \frac {a _ {x}}{\sqrt {a _ {x} ^ {2} + a _ {y} ^ {2} + a _ {z} ^ {2}}}.</equation>

<equation>\textcircled{2}</equation>关系

<equation>\cos^ {2} \alpha + \cos^ {2} \beta + \cos^ {2} \gamma = 1.</equation>


(1) 点法式方程

<equation>A \left(x - x _ {0}\right) + B \left(y - y _ {0}\right) + C \left(z - z _ {0}\right) = 0.</equation>

---


#### （4）直线的两点式方程

(2) 平面的一般式方程

<equation>A x + B y + C z + D = 0.</equation>

(3) 平面的截距式方程

<equation>\frac {x}{a} + \frac {y}{b} + \frac {z}{c} = 1.</equation>


点<equation>M_{0}\left(x_{0},y_{0},z_{0}\right)</equation>到平面<equation>A x+B y+C z+D=0</equation>的距离为

<equation>d = \frac {\left| A x _ {0} + B y _ {0} + C z _ {0} + D \right|}{\sqrt {A ^ {2} + B ^ {2} + C ^ {2}}}.</equation>


(1) 直线的标准式（对称式）方程

<equation>\frac {x - x _ {0}}{m} = \frac {y - y _ {0}}{n} = \frac {z - z _ {0}}{p}.</equation>

(2) 直线的一般式方程

<equation>\left\{ \begin{array}{l} A _ {1} x + B _ {1} y + C _ {1} z + D _ {1} = 0, \\ A _ {2} x + B _ {2} y + C _ {2} z + D _ {2} = 0. \end{array} \right.</equation>

(3) 直线的参数式方程

<equation>\left\{ \begin{array}{l} x = x _ {0} + m t, \\ y = y _ {0} + n t, \\ z = z _ {0} + p t. \end{array} \right.</equation>


过点<equation>M_{1}\left(x_{1},y_{1},z_{1}\right)</equation>与<equation>M_{2}\left(x_{2},y_{2},z_{2}\right)</equation>的直线方程为

---


#### 2. 空间曲线的方程

<equation>\frac {x - x _ {1}}{x _ {2} - x _ {1}} = \frac {y - y _ {1}}{y _ {2} - y _ {1}} = \frac {z - z _ {1}}{z _ {2} - z _ {1}}.</equation>


点<equation>M_{0}\left(x_{0},y_{0},z_{0}\right)</equation>到直线<equation>\frac{x-x_{1}}{m}=\frac{y-y_{1}}{n}=\frac{z-z_{1}}{p}</equation>的垂直距离为

<equation>d = \frac {\left| \left| \begin{array}{c c c} i & j & k \\ x _ {1} - x _ {0} & y _ {1} - y _ {0} & z _ {1} - z _ {0} \\ m & n & p \end{array} \right| \right|}{\sqrt {m ^ {2} + n ^ {2} + p ^ {2}}}.</equation>


(1) 一般式方程

<equation>F (x, y, z) = 0.</equation>

(2) 参数式方程

<equation>\left\{ \begin{array}{l} x = x (u, v), \\ y = y (u, v), \\ z = z (u, v). \end{array} \right.</equation>


(1) 空间曲线的一般式方程

---


#### 3. 常见曲面与曲线

<equation>\left\{ \begin{array}{l} F (x, y, z) = 0, \\ G (x, y, z) = 0. \end{array} \right.</equation>

(2) 空间曲线的参数式方程

<equation>\left\{ \begin{array}{l} x = x (t), \\ y = y (t), \\ z = z (t). \end{array} \right.</equation>

(3) 空间曲线在坐标面上投影曲线的方程

空间曲线<equation>\varGamma</equation>：<equation>\left\{ \begin{array}{l} F (x,y,z) = 0, \\ G (x,y,z) = 0 \end{array} \right.</equation>在 xOy坐标面上的投影曲线，可以采取以下方法来求：

从方程组<equation>\left\{ \begin{array}{l} F(x,y,z) = 0, \\ G(x,y,z) = 0 \end{array} \right.</equation>中消去 z，得方程

<equation>H (x, y) = 0,</equation>

于是<equation>\varGamma</equation>在<equation>xOy</equation>坐标面上的投影曲线方程为

<equation>\left\{ \begin{array}{l} H (x, y) = 0, \\ z = 0. \end{array} \right.</equation>


(1) 球面

<equation>(x - a) ^ {2} + (y - b) ^ {2} + (z - c) ^ {2} = R ^ {2}.</equation>

(2) 椭球面

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1.</equation>

---

(3) 单叶双曲面

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 1.</equation>

(4) 双叶双曲面

<equation>\frac {x ^ {2}}{a ^ {2}} - \frac {y ^ {2}}{b ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 1.</equation>

(5) 椭圆抛物面

<equation>\frac {x ^ {2}}{2 p} + \frac {y ^ {2}}{2 q} = z \quad (p, q \text {同 号}).</equation>

(6) 双曲抛物面

<equation>\frac {x ^ {2}}{2 p} - \frac {y ^ {2}}{2 q} = z (p, q \text {同 号}).</equation>

(7) 锥面

<equation>\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} - \frac {z ^ {2}}{c ^ {2}} = 0.</equation>

---


### 第五章 多元函数微分学


#### 3. 复合函数微分法

函数<equation>z = f(x,y)</equation>的偏导数

<equation>\left. \frac {\partial z}{\partial x} \right| _ {x = 0} = \lim _ {\Delta x \rightarrow 0} \frac {f \left(x _ {0} + \Delta x , y _ {0}\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta x},</equation>

<equation>\left. \frac {\partial z}{\partial y} \right| _ {y = \frac {x}{y}} = \lim _ {\Delta y \rightarrow 0} \frac {f \left(x _ {0} , y _ {0} + \Delta y\right) - f \left(x _ {0} , y _ {0}\right)}{\Delta y}.</equation>

存在，则称这两个极限值为<equation>z = f(x,y)</equation>在点<equation>(x_0,y_0)</equation>处对<equation>x,y</equation>的偏导数.


若<equation>\Delta z = A\Delta x + B\Delta y + o(\sqrt{(\Delta x)^2 + (\Delta y)^2})</equation>，则称<equation>z = f(x,y)</equation>在点<equation>(x,y)</equation>处可微，且<equation>\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y.</equation>


设函数<equation>z = f(u,v)</equation>可微，<equation>u = u(x,y)</equation>，<equation>v = v(x,y)</equation>具有一阶偏导数，并且它们可以构成<equation>z</equation>关于<equation>(x,y)</equation>在某区域<equation>D</equation>内的复合函数，则在<equation>D</equation>内复合函数的求导法则为

---


#### 二、隐函数求导法

<equation>\frac {\partial z}{\partial x} = \frac {\partial z}{\partial u} \cdot \frac {\partial u}{\partial x} + \frac {\partial z}{\partial v} \cdot \frac {\partial v}{\partial x},</equation>

<equation>\frac {\partial z}{\partial y} = \frac {\partial z}{\partial u} \cdot \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \cdot \frac {\partial u}{\partial y}.</equation>


偏导数连续<equation>\Rightarrow</equation>函数可微<equation>\Rightarrow</equation>函数连续<equation>\Rightarrow \lim_{y \to y_0} f(x,y)</equation>存在.偏导数存在.


（二元隐函数存在定理）设函数<equation>F ( x,y,z)</equation>在点<equation>P_{0}(x_{0},y_{0},z_{0})</equation>的某邻域内有连续偏导数，并且

<equation>F \left(x _ {0}, y _ {0}, z _ {0}\right) = 0, F _ {z} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \neq 0,</equation>

则方程<equation>F ( x,y,z)=0</equation>在点<equation>P_{0}\left(x_{0},y_{0},z_{0}\right)</equation>的某一邻域内恒能确定唯一的连续函数<equation>z=f(x,y)</equation>，且满足：

<equation>\textcircled{1}</equation><equation>z_{0} = f(x_{0}, y_{0})</equation>;

<equation>\textcircled{2} F ( x,y,f ( x,y) ) \equiv 0;</equation>

<equation>\textcircled{3} z=f(x,y)</equation>具有连续偏导数，且

<equation>\frac {\partial z}{\partial x} = - \frac {F _ {x} ^ {\prime} (x , y , z)}{F _ {z} ^ {\prime} (x , y , z)},</equation>

<equation>\frac {\partial z}{\partial y} = - \frac {F _ {y} ^ {\prime} (x , y , z)}{F _ {z} ^ {\prime} (x , y , z)}.</equation>

---


#### 四、偏导数在几何中的应用

设函数<equation>z = f(x,y)</equation>在点<equation>P_{0}(x_{0},y_{0})</equation>的某个邻域内有定义，<equation>l = \{m,n\}</equation>是一给定的向量，过<equation>P_{0}</equation>点沿方向1作射线<equation>L</equation>，在射线<equation>L</equation>上<equation>P_{0}</equation>点的邻域内取一点<equation>P(x_{0} + \Delta x,y_{0} + \Delta y)</equation>，当点<equation>P</equation>沿射线<equation>L</equation>趋向<equation>P_{0}</equation>点时，如果极限

<equation>\lim _ {P \rightarrow P _ {n}} \frac {f \left(x _ {0} + \Delta x , y _ {0} + \Delta y\right) - f \left(x _ {0} , y _ {0}\right)}{\left| P P _ {0} \right|}</equation>

存在，则此极限值称为函数<equation>z = f(x,y)</equation>在<equation>P_{0}</equation>点沿方向<equation>l</equation>的方向导数，记为<equation>\left.\frac{\partial f}{\partial l}\right|_{P}</equation>.


设函数<equation>u = F(x,y,z)</equation>在点<equation>M_{0}(x_{0},y_{0},z_{0})</equation>处可微，<equation>l = \{m,n,p\}</equation>是任一给定的向量，则

<equation>\left. \frac {\partial F}{\partial l} \right| _ {M _ {i}} = \operatorname {g r a d} F | _ {M _ {i}} \cdot l ^ {0}.</equation>


(1) 空间曲线<equation>\left\{ \begin{array}{l l} x=\varphi (t), \\ y=\psi (t), \\ z=w (t) \end{array} \right.</equation>在<equation>t=t_{0}</equation>处的切线与法平

---


#### 2. 充分条件

面方程

<equation>\textcircled{1}</equation>切线方程

<equation>\frac {x - x _ {0}}{\varphi^ {\prime} \left(t _ {0}\right)} = \frac {y - y _ {0}}{\psi^ {\prime} \left(t _ {0}\right)} = \frac {z - z _ {0}}{w ^ {\prime} \left(t _ {0}\right)}.</equation>

<equation>\textcircled{2}</equation>法平面方程

<equation>\varphi^ {\prime} \left(t _ {0}\right) \left(x - x _ {0}\right) + \psi^ {\prime} \left(t _ {0}\right) \left(y - y _ {0}\right) + w ^ {\prime} \left(t _ {0}\right) \left(z - z _ {0}\right) = 0.</equation>

(2) 曲面<equation>F ( x,y,z)=0</equation>的切平面与法线方程


<equation>\begin{array}{l} F _ {x} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(x - x _ {0}\right) + F _ {y} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(y - y _ {0}\right) + \\ F _ {z} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(z - z _ {0}\right) = 0. \\ \end{array}</equation>

<equation>\textcircled{2}</equation>法线方程

<equation>\frac {x - x _ {0}}{F _ {x} ^ {\prime} \left(x _ {0} , y _ {0} , z _ {0}\right)} = \frac {y - y _ {0}}{F _ {y} ^ {\prime} \left(x _ {0} , y _ {0} , z _ {0}\right)} = \frac {z - z _ {0}}{F _ {z} ^ {\prime} \left(x _ {0} , y _ {0} , z _ {0}\right)}.</equation>


设<equation>z = f(x,y)</equation>在点<equation>(x_0,y_0)</equation>处取得极值，且<equation>f(x,y)</equation>在点<equation>(x_0,y_0)</equation>处存在偏导数，则必有

<equation>f _ {x} ^ {\prime} \left(x _ {0}, y _ {0}\right) = 0, f _ {y} ^ {\prime} \left(x _ {0}, y _ {0}\right) = 0.</equation>


设<equation>z = f(x,y)</equation>在点<equation>(x_0,y_0)</equation>具有连续二阶偏导数，并设<equation>(x_0,y_0)</equation>是<equation>f(x,y)</equation>的驻点，记<equation>A = f_{xx}^{\prime \prime}(x_0,y_0)</equation>，<equation>B = f_{xy}^{\prime \prime}(x_0,y_0)</equation>，<equation>C = f_{xy}^{\prime \prime}(x_0,y_0)</equation>，则

---


#### 3. 条件极值

<equation>\textcircled{1}</equation>当<equation>AC - B^{2} > 0,A > 0</equation>时，<equation>f(x_{0},y_{0})</equation>为极小值；

<equation>\textcircled{2}</equation>当<equation>AC - B^{2} > 0, A < 0</equation>时，<equation>f(x_{0},y_{0})</equation>为极大值；

<equation>\textcircled{3}</equation>当<equation>AC - B^{2} < 0</equation>时，<equation>f(x_{0},y_{0})</equation>不是极值；

<equation>\textcircled{4}</equation>当<equation>AC-B^{2}=0</equation>时，不能确定<equation>f(x_{0},y_{0})</equation>是否为极值.


求<equation>z = f(x,y)</equation>在条件<equation>\varphi (x,y) = 0</equation>下的极值. 一般方法为：

<equation>\textcircled{1}</equation>构造拉格朗日函数

<equation>F (x, y, \lambda) = f (x, y) + \lambda \varphi (x, y).</equation>

<equation>\textcircled{2}</equation>将 F(x,y,<equation>\lambda</equation>)分别对 x,y,<equation>\lambda</equation>求偏导数，构造下列方程组：

<equation>\left\{ \begin{array}{l} F _ {x} ^ {\prime} = f _ {x} ^ {\prime} (x, y) + \lambda \varphi_ {x} ^ {\prime} (x, y) = 0, \\ F _ {y} ^ {\prime} = f _ {y} ^ {\prime} (x, y) + \lambda \varphi_ {y} ^ {\prime} (x, y) = 0, \\ F _ {\lambda} ^ {\prime} = \varphi (x, y) = 0, \end{array} \right.</equation>

解出<equation>(x,y)</equation>，这是可能极值点的坐标.

<equation>\textcircled{3}</equation>判定上述点是否为极值点，如果是，求出该点的函数值 f(x,y).

---


### 第六章 多元函数积分学


#### 1. 二重积分的计算法

(1) 利用直角坐标系计算二重积分若积分区域 D是 X型域，其不等式表示为<equation>D: \left\{ \begin{array}{l l} a \leqslant x \leqslant b, \\ \varphi_{1}(x) \leqslant y \leqslant \varphi_{2}(x), \end{array} \right.</equation><equation>I = \iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = \int_{a}^{b} \mathrm{d}x \int_{\varphi_{1}(x)}^{\varphi_{1}(x)} f(x,y)\mathrm{d}y.</equation>若积分区域 D是 Y型域，其不等式表示为<equation>D: \left\{ \begin{array}{l l} c \leqslant y \leqslant d, \\ \varphi_{1}(y) \leqslant x \leqslant \varphi_{2}(y), \end{array} \right.</equation><equation>I = \iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = \int_{c}^{d} \mathrm{d}y \int_{\varphi_{1}(y)}^{\varphi_{1}(y)} f(x,y)\mathrm{d}x.</equation>

则

(2) 利用极坐标计算二重积分

<equation>\textcircled{1}</equation>如果极点<equation>O</equation>在区域<equation>D</equation>内，此时<equation>D</equation>可用不等式

---

$$

\left\{ \begin{array}{l l} 0 \leqslant \theta \leqslant 2 \pi , \\ 0 \leqslant r \leqslant \varphi (\theta) \end{array} \right. \text {表 示 ， 则}

$$

<equation>\begin{array}{l} \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} \theta \mathrm {d} r \\ = \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\varphi (\theta)} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} r. \\ \end{array}</equation>

<equation>\textcircled{2}</equation>如果极点 O在区域 D的边界上，此时 D可用不等式<equation>\left\{ \begin{array}{l l} \alpha \leqslant \theta \leqslant \beta , \\ 0 \leqslant r \leqslant \varphi (\theta) \end{array} \right.</equation>表示，则

<equation>\begin{array}{l} \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} \theta \mathrm {d} r \\ = \int_ {\alpha} ^ {\beta} \mathrm {d} \theta \int_ {0} ^ {\varphi (\theta)} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} r. \\ \end{array}</equation>

<equation>\textcircled{3}</equation>如果极点<equation>O</equation>在区域<equation>D</equation>外，此时<equation>D</equation>可用不等式<equation>\left\{ \begin{array}{l l} \alpha \leqslant \theta \leqslant \beta , \\ \varphi_{1}(\theta) \leqslant r \leqslant \varphi_{2}(\theta) \end{array} \right.</equation>来表示，则

<equation>\begin{array}{l} \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} \theta \mathrm {d} r \\ = \int_ {a} ^ {\beta} \mathrm {d} \theta \int_ {\varphi_ {1} (\theta)} ^ {\varphi_ {2} (\theta)} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} r. \\ \end{array}</equation>

2. 三重积分的计算法

(1) 利用直角坐标系计算三重积分

<equation>\textcircled{1}</equation>“先一后二”，即将三重积分化为：

---

<equation>\iiint_ {\Omega} f (x, y, z) \mathrm {d} v = \left\{ \begin{array}{l l} \iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y \int_ {z _ {1} (x, y)} ^ {z _ {2} (x, y)} f (x, y, z) \mathrm {d} z, \\ \iint_ {D _ {x y}} \mathrm {d} y \mathrm {d} z \int_ {z _ {1} (y, z)} ^ {z _ {2} (y, z)} f (x, y, z) \mathrm {d} x, \\ \iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} z \int_ {y _ {1} (x, z)} ^ {y _ {2} (x, z)} f (x, y, z) \mathrm {d} y. \end{array} \right.</equation>

<equation>\textcircled{2}</equation>“先二后一”，即将三重积分化为：

<equation>\iiint_ {\Omega} f (x, y, z) \mathrm {d} v = \left\{ \begin{array}{l} \int_ {c} ^ {d} \mathrm {d} z \iint_ {D (z)} f (x, y, z) \mathrm {d} x \mathrm {d} y, \\ \int_ {a} ^ {b} \mathrm {d} x \iint_ {D (x)} f (x, y, z) \mathrm {d} y \mathrm {d} z, \\ \int_ {m} ^ {n} \mathrm {d} y \iint_ {D (x)} f (x, y, z) \mathrm {d} x \mathrm {d} z. \end{array} \right.</equation>

(2) 利用柱坐标计算三重积分

<equation>\mathrm {d} v = r \mathrm {d} r \mathrm {d} \theta \mathrm {d} z.</equation>

<equation>\textcircled{1}</equation>柱坐标系下的体积元素

<equation>\textcircled{2}</equation>柱坐标系下的三次积分的先后次序一般为

<equation>I = \int \mathrm {d} \theta \int r \mathrm {d} r \int f (r \cos \theta , r \sin \theta , z) \mathrm {d} z.</equation>

<equation>\textcircled{3}</equation>若空间区域<equation>\varOmega</equation>可以用不等式

<equation>\left\{ \begin{array}{l} z _ {1} (r, \theta) \leqslant z \leqslant z _ {2} (r, \theta), \\ r _ {1} (\theta) \leqslant r \leqslant r _ {2} (\theta), \\ \alpha \leqslant \theta \leqslant \beta \end{array} \right.</equation>

---


#### 二、重积分的应用（数学二不作要求）

表示，则

<equation>\begin{array}{l} \iiint_ {\Omega} f (x, y, z) \mathrm {d} v \\ = \iiint_ {\Omega} f (r \cos \theta , r \sin \theta , z) r \mathrm {d} r \mathrm {d} \theta \mathrm {d} z \\ = \int_ {\alpha} ^ {\beta} \mathrm {d} \theta \int_ {r _ {1} (\theta)} ^ {r _ {2} (\theta)} r \mathrm {d} r \int_ {z _ {1} (r, \theta)} ^ {z _ {2} (r, \theta)} f (r \cos \theta , r \sin \theta , z) \mathrm {d} z. \\ \end{array}</equation>

(3) 利用球坐标计算三重积分

<equation>\textcircled{1}</equation>球坐标与直角坐标的关系

<equation>\left\{ \begin{array}{l} x = r \sin \varphi \cos \theta , \\ y = r \sin \varphi \sin \theta , \\ z = r \cos \varphi . \end{array} \right.</equation>

<equation>\textcircled{2}</equation>球坐标系下的体积元素

<equation>\mathrm {d} v = r ^ {2} \sin \varphi \mathrm {d} r \mathrm {d} \theta \mathrm {d} \varphi .</equation>

<equation>\textcircled{3}</equation>球坐标系下三次积分的先后次序一般为<equation>I = \int \mathrm{d}\theta \int \mathrm{d}\varphi \int f(r\sin \varphi \cos \theta ,r\sin \varphi \sin \theta ,r\cos \varphi)r^2\sin \varphi \mathrm{d}r.</equation>

<equation>\textcircled{1}</equation>曲面面积的计算公式


(1) 几何应用

<equation>A = \iint_ {D} \sqrt {1 + \left(f _ {x} ^ {\prime}\right) ^ {2} + \left(f _ {y} ^ {\prime}\right) ^ {2}} \mathrm {d} \sigma .</equation>

---

<equation>\textcircled{2}</equation>体积

<equation>V = \iiint_ {\Omega} \mathrm {d} v = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{3}</equation>平面图形 D的形心<equation>(x,y)</equation>为

<equation>\bar {x} = \frac {\iint_ {D} x \mathrm {d} x \mathrm {d} y}{\iint_ {D} \mathrm {d} x \mathrm {d} y}, \quad \bar {y} = \frac {\iint_ {D} y \mathrm {d} x \mathrm {d} y}{\iint_ {D} \mathrm {d} x \mathrm {d} y}.</equation>

<equation>\textcircled{4}</equation>空间立体<equation>\varOmega</equation>的形心<equation>( \bar{x},\bar{y},\bar{z} )</equation>为

<equation>\bar {x} = \frac {\iiint_ {\Omega} x \mathrm {d} v}{\iiint_ {\Omega} \mathrm {d} v}, \bar {y} = \frac {\iiint_ {\Omega} y \mathrm {d} v}{\iiint_ {\Omega} \mathrm {d} v}, \bar {z} = \frac {\iiint_ {\Omega} z \mathrm {d} v}{\iiint_ {\Omega} \mathrm {d} v}.</equation>

(2) 物理应用

<equation>\textcircled{1}</equation>平面薄片的质心坐标<equation>(\overline{x},\overline{y})</equation>为

<equation>\bar {x} = \frac {\iint_ {D} x \rho (x , y) \mathrm {d} x \mathrm {d} y}{\iint_ {D} \rho (x , y) \mathrm {d} x \mathrm {d} y}, \quad \bar {y} = \frac {\iint_ {D} y \rho (x , y) \mathrm {d} x \mathrm {d} y}{\iint_ {D} \rho (x , y) \mathrm {d} x \mathrm {d} y}</equation>

<equation>\textcircled{2}</equation>立体的质心坐标<equation>( \overline{x},\overline{y},\overline{z} )</equation>为

<equation>\bar {x} = \frac {\iiint_ {\Omega} x \rho (x , y , z) \mathrm {d} v}{\iiint_ {\Omega} \rho (x , y , z) \mathrm {d} v}, \bar {y} = \frac {\iiint_ {\Omega} y \rho (x , y , z) \mathrm {d} v}{\iiint_ {\Omega} \rho (x , y , z) \mathrm {d} v},</equation>

---

<equation>\bar {z} = \frac {\iiint_ {\Omega} z \rho (x , y , z) \mathrm {d} v}{\iiint_ {\Omega} \rho (x , y , z) \mathrm {d} v}</equation>

<equation>\textcircled{3}</equation>平面薄片绕轴的转动惯量

绕<equation>x</equation>轴的转动惯量：<equation>I_{x} = \iint_{D} y^{2}\rho (x,y)\mathrm{d}x\mathrm{d}y.</equation>

绕<equation>y</equation>轴的转动惯量：<equation>I_{y} = \iint_{D} x^{2}\rho (x,y)\mathrm{d}x\mathrm{d}y.</equation>

<equation>\textcircled{4}</equation>立体绕轴的转动惯量

绕<equation>x</equation>轴的转动惯量：<equation>I_{x} = \iint_{D}\left(y^{2} + z^{2}\right)\rho (x,y,z)\mathrm{d}v.</equation>

绕<equation>y</equation>轴的转动惯量：<equation>I_{y} = \iint_{Q}\left(x^{2} + z^{2}\right)\rho (x,y,z)\mathrm{d}v.</equation>

绕<equation>z</equation>轴的转动惯量：<equation>I_{z} = \iint_{D}(x^{2} + y^{2})\rho (x,y,z)\mathrm{d}v.</equation>

<equation>\textcircled{5}</equation>平面薄片对质点的引力<equation>F = \{F_{x}, F_{y}\}</equation>为：

<equation>F _ {x} = \iint_ {D} \frac {G m \rho (x , y) \left(x - x _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} x \mathrm {d} y,</equation>

<equation>F _ {y} = \iint_ {D} \frac {G m \rho (x , y) \left(y - y _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{6}</equation>立体对质点的引力<equation>F = \{F_{x}, F_{y}, F_{z}\}</equation>为

---


#### 1. 曲线积分的计算公式

<equation>F _ {x} = \iiint_ {\Omega} \frac {G m \varphi (x , y , z) \left(x - x _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} v,</equation>

<equation>F _ {y} = \iiint_ {a} \frac {G m \rho (x , y , z) \left(y - y _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} d v,</equation>

<equation>F _ {z} = \iiint_ {\Omega} \frac {G m p (x , y , z) \left(z - z _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} v.</equation>


(1) 化成定积分

<equation>\begin{array}{l} \int_ {\Gamma} f (x, y, z) \mathrm {d} s = \int_ {\alpha} ^ {\beta} f \left[ \varphi (t), \psi (t), w (t) \right]. \\ \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t) + w ^ {\prime 2} (t)} \mathrm {d} t \quad (\alpha \leqslant \beta), \\ \int_ {\Gamma} P (x, y, z) \mathrm {d} x + Q (x, y, z) \mathrm {d} y + R (x, y, z) \mathrm {d} z \\ = \int_ {\alpha} ^ {\beta} \left\{P \left[ \varphi (t), \psi (t), w (t) \right] \varphi^ {\prime} (t) + Q \left[ \varphi (t), \psi (t), w (t) \right] \right. \\ \psi^ {\prime} (t) + R \left[ \varphi (t), \psi (t), w (t) \right] w ^ {\prime} (t) \} \mathrm {d} t, \\ \end{array}</equation>

其中<equation>\alpha</equation>为<equation>\varGamma</equation>的起点参数<equation>t</equation>的值，<equation>\beta</equation>为<equation>\varGamma</equation>的终点参数<equation>t</equation>的值.

---


#### 2. 全微分求积

(2) 格林公式

<equation>\begin{array}{l} \oint_ {L} P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y \\ = \iint_ {D} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm {d} x \mathrm {d} y, \\ \end{array}</equation>

其中 L为正向闭曲线.


<equation>\int_{L} P(x,y)\mathrm{d}x + Q(x,y)\mathrm{d}y</equation>与路径无关的充要条件是<equation>\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}</equation>.

(4) 斯托克斯公式

<equation>\begin{array}{l} \int_ {P} P \mathrm {d} x + Q \mathrm {d} y + R \mathrm {d} z \\ = \iint_ {x} \left| \begin{array}{c c c} \cos \alpha & \cos \beta & \cos \gamma \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right| \mathrm {d} S. \\ \end{array}</equation>

其中<equation>\cos \alpha ,\cos \beta ,\cos \gamma</equation>为<equation>\Sigma</equation>所指定侧法线方向的方向余弦.


<equation>\textcircled{1}</equation>若函数<equation>P ( x,y), Q ( x,y)</equation>在单连通域G内具有一阶连续偏导数，且

<equation>\frac {\partial Q}{\partial x} = \frac {\partial P}{\partial y},</equation>

---

则在<equation>G</equation>内存在二元函数<equation>u(x,y)</equation>，使得

<equation>\mathrm {d} u = P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y.</equation>

<equation>\textcircled{2}</equation>求积公式

<equation>u (x, y) = \int_ {x _ {0}} ^ {x} P \left(x, y _ {0}\right) \mathrm {d} x + \int_ {y _ {0}} ^ {y} Q (x, y) \mathrm {d} y + C.</equation>

3. 曲面积分的计算公式

(1) 化为二重积分

<equation>\textcircled{1}</equation>对面积的曲面积分

<equation>\begin{array}{l} \iint_ {\Sigma} f (x, y, z) \mathrm {d} S \\ = \iint_ {D _ {x y}} f [ x, y, z (x, y) ] \cdot \sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}} \mathrm {d} x \mathrm {d} y, \\ \end{array}</equation>

其中<equation>D_{xy}</equation>是曲面<equation>\Sigma</equation>在<equation>xOy</equation>平面上的投影.

<equation>\textcircled{2}</equation>对坐标的曲面积分

<equation>\begin{array}{l} \iint_ {\Sigma} P (x, y, z) \mathrm {d} y \mathrm {d} z \frac {\Sigma \text {为 单 值 函 数} x = x (y , z)}{\Sigma} \\ \pm \iint_ {D _ {y z}} P [ x (y, z), y, z ] \mathrm {d} y \mathrm {d} z, (\text {前} “ + ” \text {后} “ - ”) \\ \iint_ {\Sigma} Q (x, y, z) \mathrm {d} z \mathrm {d} x \frac {\Sigma \text {为 单 值 函 数} y = y (x , z)}{\Sigma} \\ \pm \iint_ {D _ {x z}} Q [ x, y (x, z), z ] \mathrm {d} z \mathrm {d} x, (\text {右} “ + ” \text {左} “ - ”) \\ \end{array}</equation>

---


#### (2) 曲面积分

<equation>\begin{array}{l} \iint_ {\Sigma} R (x, y, z) \mathrm {d} x \mathrm {d} y \frac {\Sigma \text {为 单 值 函数} z = z (x , y)}{} \\ \pm \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm {d} x \mathrm {d} y. (\text {上} “ + ” \text {下} “ - ”) \\ \end{array}</equation>

(2) 高斯公式

<equation>\begin{array}{l} \oiint_ {\Sigma} P \mathrm {d} y \mathrm {d} z + Q \mathrm {d} z \mathrm {d} x + R \mathrm {d} x \mathrm {d} y \\ = \iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm {d} v, \\ \end{array}</equation>

其中<equation>\Sigma</equation>为闭曲面的外侧，<equation>\Omega</equation>是<equation>\Sigma</equation>所围立体.


(1) 曲线积分

<equation>\int_ {L} P \mathrm {d} x + Q \mathrm {d} y = \int_ {L} \left(P \cos \alpha + Q \cos \beta\right) \mathrm {d} s,</equation>

其中<equation>\alpha (x,y),\beta (x,y)</equation>为有向曲线弧<equation>L</equation>上点<equation>(x,y)</equation>处的切线向量的方向角.

<equation>\begin{array}{l} \int_ {\Gamma} P \mathrm {d} x + Q \mathrm {d} y + R \mathrm {d} z \\ = \int_ {\Gamma} \left(P \cos \alpha + Q \cos \beta + R \cos \gamma\right) \mathrm {d} s, \\ \end{array}</equation>

其中<equation>\alpha (x,y,z),\beta (x,y,z),\gamma (x,y,z)</equation>是有向曲线弧<equation>\varGamma</equation>上点<equation>(x,y,z)</equation>处的切线向量的方向角.

---


#### (2) 散度和旋度

<equation>\begin{array}{l} \iint_ {\Sigma} P \mathrm {d} y \mathrm {d} z + Q \mathrm {d} z \mathrm {d} x + R \mathrm {d} x \mathrm {d} y \\ = \iint_ {\Sigma} \left(P \cos \alpha + Q \cos \beta + R \cos \gamma\right) \mathrm {d} S, \\ \end{array}</equation>

其中<equation>\cos \alpha ,\cos \beta ,\cos \gamma</equation>是有向曲面上点<equation>(x,y,z)</equation>处法向量的方向余弦.


(1) 梯度

<equation>\operatorname {g r a d} f (x, y) = \frac {\partial f}{\partial x} i + \frac {\partial f}{\partial y} j,</equation>

<equation>\operatorname {g r a d} f (x, y, z) = \frac {\partial f}{\partial x} i + \frac {\partial f}{\partial y} j + \frac {\partial f}{\partial z} k.</equation>


若<equation>A=P(x,y,z)i+Q(x,y,z)j+R(x,y,z)k</equation>，则<equation>\textcircled{1}</equation>散度

<equation>\operatorname {d i v} A = \frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z};</equation>

<equation>\textcircled{2}</equation>旋度

<equation>\operatorname {r o t} A = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right|.</equation>

---


### 第七章 级数


#### 1. 数项级数的定义与性质

(1) 定义

<equation>\textcircled{1}</equation><equation>\sum_{n=1}^{\infty} u_{n}=u_{1}+u_{2}+\cdots+u_{n}+\cdots,</equation><equation>S_{n}=\sum_{k=1}^{n} u_{k}</equation>称为级数的部分和.

<equation>\textcircled{2}</equation>若数项级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>的部分和数列<equation>\{S_n\}</equation>有极限，则称级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>收敛，极限值<equation>\lim_{n\to \infty} S_n = A</equation>称为此级数的和，并写作<equation>\sum_{n = 1}^{\infty} u_{n} = A.</equation>当<equation>\lim_{n\to \infty} S_n</equation>不存在时，则称级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>发散.

(2) 级数的基本性质及收敛的必要条件

<equation>\textcircled{1}</equation>设<equation>\sum_{n = 1}^{\infty} u_{n}, \sum_{n = 1}^{\infty} v_{n}</equation>都收敛，其和分别为<equation>A, B</equation>，则

---


#### 2. 正项级数及其敛散性判别法

<equation>\sum_{n = 1}^{\infty}\left(u_{n}\pm v_{n}\right)</equation>必收敛，且<equation>\sum_{n = 1}^{\infty}\left(u_{n}\pm v_{n}\right) = A\pm B</equation>

<equation>\textcircled{2}</equation>设<equation>k</equation>为非零常数，则级数<equation>\sum_{n = 1}^{\infty} u_n</equation>与<equation>\sum_{n = 1}^{\infty} k u_n</equation>有相同的敛散性；

<equation>\textcircled{3}</equation>改变级数的前有限项，不影响级数的敛散性；

<equation>\textcircled{4}</equation>级数收敛的必要条件：若<equation>\sum_{n=1}^{\infty} u_n</equation>收敛，则<equation>\lim_{n\to \infty} u_n = 0</equation>；

<equation>\textcircled{5}</equation>收敛的级数在不改变各项次序的前提下任意加括号得到的新级数仍然收敛，且和不变.


(1) 正项级数收敛的基本定理

设<equation>\{S_n\}</equation>是正项级数<equation>\sum_{n=1}^{\infty} u_n</equation>的部分和数列，则正项级数<equation>\sum_{n=1}^{\infty} u_n</equation>收敛的充要条件是数列<equation>\{S_n\}</equation>有界.

(2) 正项级数的比较判别法

（正项级数比较判别法的非极限形式）设<equation>\sum_{n = 1}^{\infty}u_n</equation><equation>\sum_{n = 1}^{\infty}v_n</equation>都是正项级数，并设<equation>u_{n}\leqslant v_{n}(n\geqslant N_{0})</equation>，则

<equation>\textcircled{1}</equation>若<equation>\sum_{n = 1}^{\infty} v_{n}</equation>收敛，则<equation>\sum_{n = 1}^{\infty} u_{n}</equation>收敛；

---

<equation>\textcircled{2}</equation>若<equation>\sum_{n = 1}^{\infty} u_{n}</equation>发散，则<equation>\sum_{n = 1}^{\infty} v_{n}</equation>发散.

（正项级数比较判别法的极限形式）设<equation>\sum_{n = 1}^{\infty}u_n</equation><equation>\sum_{n = 1}^{\infty}v_n</equation>都是正项级数，并设<equation>\lim_{n\to \infty}\frac{u_n}{v_n} = \rho</equation>或为<equation>+\infty</equation>，则

<equation>\textcircled{1}</equation>当<equation>\rho</equation>为非零常数时，级数<equation>\sum_{n=1}^{\infty} u_{n}</equation><equation>\sum_{n=1}^{\infty} v_{n}</equation>有相同的敛散性；

<equation>\textcircled{2}</equation>当<equation>\rho = 0</equation>时，若<equation>\sum_{n = 1}^{\infty} v_{n}</equation>收敛，则必有<equation>\sum_{n = 1}^{\infty} u_{n}</equation>收敛；

<equation>\textcircled{3}</equation>当<equation>\rho = +\infty</equation>时，若<equation>\sum_{n = 1}^{\infty} v_{n}</equation>发散，则必有<equation>\sum_{n = 1}^{\infty} u_{n}</equation>发散.

(3) 正项级数的比值判别法

设<equation>\sum_{n = 1}^{\infty} u_{n}</equation>是正项级数，若<equation>\lim_{n\to \infty}\frac{u_{n + 1}}{u_n} = \rho</equation>或为<equation>+\infty</equation>，则级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>有

<equation>\textcircled{1}</equation>当<equation>\rho<1</equation>时，收敛；

<equation>\textcircled{2}</equation>当<equation>\rho >1</equation>或<equation>\infty</equation>时，发散；

<equation>\textcircled{3}</equation>当<equation>\rho=1</equation>时，敛散性不确定.

(4) 正项级数的根值判别法

---


#### （1）条件收敛、绝对收敛

将比值判别法中的<equation>\frac{u_{n + 1}}{u_n}</equation>改成<equation>\sqrt[n]{u_n}</equation>，其他文字叙述、结论均不改动，即为根值判别法.


形如

<equation>\sum_{n=1}^{\infty}(-1)^{n-1} u_{n}(u_{n}>0)</equation>或<equation>\sum_{n=1}^{\infty}(-1)^{n} u_{n}(u_{n}>0)</equation>的级数，称为交错级数.


若交错级数<equation>\sum_{n = 1}^{\infty}(-1)^{n - 1}u_n(u_n > 0)</equation>满足条件；

<equation>\textcircled{1}</equation><equation>u_{n}\geqslant u_{n + 1}(n = 1,2,\dots)</equation>;

<equation>\textcircled{2} \lim_{n \to \infty} u_{n}=0,</equation>

则交错级数<equation>\sum_{n=1}^{\infty} (-1)^{n-1} u_n (u_n > 0)</equation>收敛，其和<equation>S \leqslant u_1</equation>，其余项<equation>S - S_n</equation>满足<equation>|S - S_n| \leqslant u_{n+1}</equation>.


若级数<equation>\sum_{n = 1}^{\infty}|u_n|</equation>收敛，则称级数<equation>\sum_{n = 1}^{\infty}u_n</equation>绝对收敛；

若级数<equation>\sum_{n = 1}^{\infty}|u_n|</equation>发散，但级数<equation>\sum_{n = 1}^{\infty}u_n</equation>收敛，则称级数

---


#### 2. 幂级数的收敛半径

若级数<equation>\sum_{n=1}^{\infty} \mid u_{n} \mid</equation>收敛，则级数<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，即绝对收敛的级数一定收敛.


形如<equation>\sum_{n=0}^{\infty} a_{n} ( x-x_{0} )^{n}</equation>的函数项级数称为<equation>x_{0}</equation>处的幂级数.


（阿贝尔定理）对幂级数<equation>\sum_{n=0}^{\infty} a_{n} ( x-x_{0} )^{n}</equation>有如下的结论：

<equation>\textcircled{1}</equation>如果该幂级数在点<equation>x_{1}</equation>收敛，则对满足<equation>|x-x_{0}|<</equation><equation>|x_{1}-x_{0}|</equation>的一切 x所对应的级数<equation>\sum_{n=0}^{\infty} a_{n}(x-x_{0})^{n}</equation>都绝对收敛.

<equation>\textcircled{2}</equation>如果该幂级数在点<equation>x_{2}</equation>发散，则对满足<equation>|x - x_0| > |x_2 - x_0|</equation>的一切<equation>x</equation>所对应的级数<equation>\sum_{n = 0}^{\infty} a_n (x - x_0)^n</equation>都发散.

---


#### 4. 幂级数的性质

求幂级数<equation>\sum_{n = 0}^{\infty} a_n (x - x_0)^n</equation>的收敛半径<equation>R</equation>的方法有：

(1)<equation>\textcircled{1}</equation>求极限

<equation>\rho \left(x - x _ {0}\right) = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n + 1} \left(x - x _ {0}\right) ^ {n + 1}}{a _ {n} \left(x - x _ {0}\right) ^ {n}} \right|.</equation>

<equation>\textcircled{2}</equation>令<equation>\rho ( x - x_{0} ) < 1 \Rightarrow | x - x_{0} | < m</equation>，则收敛半径为<equation>R=m.</equation>

(2) 若<equation>a_{n}</equation>满足<equation>a_{n}\neq 0</equation>，则

<equation>R = \lim _ {n \rightarrow \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right|.</equation>

(3)<equation>\textcircled{1}</equation>求极限

<equation>\rho \left(x - x _ {0}\right) = \lim _ {n \rightarrow \infty} \sqrt [ n ]{a _ {n} \left(x - x _ {0}\right) ^ {n}}.</equation>

<equation>\textcircled{2}</equation>令<equation>\rho ( x - x_{0} ) < 1 \Rightarrow | x - x_{0} | < m</equation>，则收敛半径为<equation>R=m.</equation>


设幂级数<equation>\sum_{n = 0}^{\infty}a_n(x - x_0)^n</equation>的半径为<equation>R_{1},\sum_{n = 0}^{\infty}b_{n}(x - x_{0})^{n}</equation>的收敛半径为<equation>R_{2}</equation>，则

<equation>\textcircled{1}</equation><equation>\sum_{n=0}^{\infty} a_{n}(x-x_{0})^{n}\pm \sum_{n=0}^{\infty} b_{n}(x-x_{0})^{n}=\sum_{n=0}^{\infty}(a_{n}\pm b_{n})(x-x_{0})^{n}</equation>的收敛半径<equation>R\geqslant \min \{R_{1},R_{2}\} .</equation>

---

<equation>\textcircled{2}</equation><equation>[\sum_{n = 0}^{\infty}a_n(x - x_0)^n]\cdot[\sum_{n = 0}^{\infty}b_n(x - x_0)^n] =</equation><equation>\sum_{n = 0}^{\infty}(\sum_{i = 0}^{n}a_{i}b_{n - i})(x - x_0)^n</equation>，收敛半径<equation>R\geqslant \min \{R_{1},R_{2}\}</equation>.

<equation>\textcircled{3}</equation>幂级数<equation>\sum_{n = 0}^{\infty} a_n (x - x_0)^n</equation>的和函数<equation>S(x)</equation>在其收敛域<equation>I</equation>上连续.

<equation>\textcircled{4}</equation>幂级数在其收敛区间内可以逐项求导，且求导后所得到的幂级数的收敛半径仍为<equation>R.</equation>即有

<equation>\begin{array}{l} S ^ {\prime} (x) = \left[ \sum_ {n = 0} ^ {\infty} a _ {n} \left(x - x _ {0}\right) ^ {n} \right] ^ {\prime} = \sum_ {n = 0} ^ {\infty} \left[ a _ {n} \left(x - x _ {0}\right) ^ {n} \right] ^ {\prime} \\ = \sum_ {n = 1} ^ {\infty} n a _ {n} \left(x - x _ {0}\right) ^ {n - 1}. \\ \end{array}</equation>

<equation>\textcircled{5}</equation>幂级数在其收敛区间内可以逐项积分，且积分后所得到的幂级数的收敛半径仍为<equation>R.</equation>即有

<equation>\begin{array}{l} \int_ {x _ {0}} ^ {x} S (x) \mathrm {d} x = \int_ {x _ {0}} ^ {x} \left[ \sum_ {n = 0} ^ {\infty} a _ {n} \left(x - x _ {0}\right) ^ {n} \right] \mathrm {d} x \\ = \sum_ {n = 0} ^ {\infty} \int_ {x _ {0}} ^ {x} \left[ a _ {n} \left(x - x _ {0}\right) ^ {n} \right] \mathrm {d} x \\ = \sum_ {n = 0} ^ {\infty} \frac {1}{n + 1} a _ {n} \left(x - x _ {0}\right) ^ {n + 1}. \\ \end{array}</equation>

5. 函数展开成幂级数

(1) 函数展开成幂级数的定义

设函数<equation>f(x)</equation>在区间<equation>I</equation>上有定义，<equation>x_0\in I</equation>，若存在幂

---


#### (3)泰勒级数与麦克劳林级数

级数<equation>\sum_{n = 0}^{\infty}a_n(x - x_0)^n</equation>，使得

<equation>f (x) = \sum_ {n = 0} ^ {\infty} a _ {n} \left(x - x _ {0}\right) ^ {n}, x \in I,</equation>

则称<equation>f(x)</equation>在区间<equation>I</equation>上能展开成<equation>x</equation>。处的幂级数.


若函数<equation>f ( x )</equation>在区间 I上能展开成<equation>x_{0}</equation>处的幂级数<equation>f ( x ) = \sum_{n = 0}^{\infty} a_{n} \left( x - x_{0} \right)^{n}, x \in I,</equation>则其展开式是唯一的，且<equation>a_{n} = \frac{f^{(n)} \left(x_{0}\right)}{n!}</equation>（<equation>n=0,1,2,\dots).</equation>


如果<equation>f(x)</equation>在<equation>x_{0}</equation>的某一邻域内具有任意阶导数，则称幂级数

<equation>\begin{array}{l} \sum_ {n = 0} ^ {\infty} \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} \\ = f \left(x _ {0}\right) + \frac {f ^ {\prime} \left(x _ {0}\right)}{1 !} \left(x - x _ {0}\right) + \dots + \\ \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + \dots \\ \end{array}</equation>

为函数<equation>f(x)</equation>在<equation>x_{0}</equation>点的泰勒级数.

当<equation>x_{0} = 0</equation>时，称幂级数

<equation>\sum_ {n = 0} ^ {\infty} \frac {f ^ {(n)} (0)}{n !} x ^ {n}</equation>

---

<equation>= f (0) + \frac {f ^ {\prime} (0)}{1 !} x + \dots + \frac {f ^ {(n)} (0)}{n !} x ^ {n} + \dots</equation>

为函数 f(x)的麦克劳林级数.

（函数展开成泰勒级数的充要条件）函数<equation>f(x)</equation>在<equation>x_{0}\in I</equation>处的泰勒级数在 I 上收敛到<equation>f(x)</equation>的充要条件是：<equation>f(x)</equation>在<equation>x_{0}</equation>处的泰勒公式

<equation>f (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} \left(x _ {0}\right)}{k !} \left(x - x _ {0}\right) ^ {k} + R _ {n} (x)</equation>

的余项<equation>R_{n}(x)</equation>在<equation>I</equation>上收敛到零，即对任意的<equation>x\in I</equation>，都有<equation>\lim_{n\to \infty}R_n(x) = 0.</equation>

(4) 幂级数常用的七个展开式

<equation>\mathrm {e} ^ {x} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !}, x \in (- \infty , + \infty);</equation>

<equation>\sin x = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n + 1) !}, x \in (- \infty , + \infty);</equation>

<equation>\cos x = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \frac {x ^ {2 n}}{(2 n) !}, x \in (- \infty , + \infty);</equation>

<equation>\ln (1 + x) = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \frac {x ^ {n + 1}}{n + 1}, - 1 < x \leqslant 1,</equation>

<equation>\begin{array}{l} (1 + x) ^ {\alpha} = 1 + \sum_ {n = 1} ^ {\infty} \frac {\alpha (\alpha - 1) (\alpha - 2) \dots (\alpha - n + 1)}{n !} x ^ {n}, \\ x \in (- 1, 1); \\ \end{array}</equation>

---


#### （1）傅里叶级数的定义

<equation>\frac {1}{1 - x} = \sum_ {n = 0} ^ {\infty} x ^ {n}, x \in (- 1, 1);</equation>

<equation>\frac {1}{1 + x} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {n}, x \in (- 1, 1).</equation>


设函数<equation>f(x)</equation>是周期为<equation>2\pi</equation>的周期函数，且在区间<equation>[-\pi ,\pi ]</equation>上可积，则称

<equation>a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x \mathrm {d} x \quad (n = 1, 2, \dots)</equation>

为<equation>f(x)</equation>的傅里叶系数，称三角级数

<equation>\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right)</equation>

为<equation>f(x)</equation>以<equation>2\pi</equation>为周期的傅里叶级数，记作

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right).</equation>

(2) 傅里叶级数的收敛定理

（狄利克雷收敛定理）设<equation>f(x)</equation>是周期为<equation>2\pi</equation>的周期函数，在区间<equation>[-\pi ,\pi ]</equation>上满足：

---


#### 2. 周期为 21 的傅里叶级数

<equation>\textcircled{1}</equation>只有有限个第一类间断点；

<equation>\textcircled{2}</equation>只有有限个极值点.

则<equation>f ( x )</equation>的以<equation>2 \pi</equation>为周期的傅里叶级数<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} \left(a_{n}\cos nx+b_{n}\sin nx\right)</equation>，其收敛域为<equation>(-\infty , +\infty)</equation>，和函数<equation>S ( x )</equation>是以<equation>2 \pi</equation>为周期的周期函数，且在其一个周期上的表达式为

<equation>S (x) = \left\{ \begin{array}{l l} \frac {f (x - 0) + f (x + 0)}{2}, & x \in (- \pi , \pi), \\ \frac {f (- \pi + 0) + f (\pi - 0)}{2}, & x = \pm \pi . \end{array} \right.</equation>


设函数<equation>f(x)</equation>是周期为<equation>2l</equation>的周期函数，且在区间<equation>[-l, l]</equation>上可积，则称

<equation>a _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots)</equation>

为<equation>f(x)</equation>的傅里叶系数，称三角级数

<equation>\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{l} + b _ {n} \sin \frac {n \pi x}{l}\right)</equation>

为<equation>f(x)</equation>以2l为周期的傅里叶级数.

---

3. 只在<equation>[0, l]</equation>上有定义的函数的傅里叶级数展开

(1) 对称区间上奇、偶函数的傅里叶级数

<equation>\textcircled{1}</equation>若<equation>f(x)</equation>是以<equation>2l</equation>为周期的可积偶函数，则其以<equation>2l</equation>为周期的傅里叶级数为

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l},</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots).</equation>

<equation>\textcircled{2}</equation>若<equation>f(x)</equation>为以<equation>2l</equation>为周期的可积奇函数，则其以<equation>2l</equation>为周期的傅里叶级数为

<equation>f (x) \sim \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l},</equation>

其中

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {1} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

(2) 在<equation>[0, l]</equation>上有定义的函数的傅里叶级数展开

定义在[0，l]上的函数可以有多种方式展开成三角级数，但常用的方式只有三种，即周期奇延拓、周期偶延拓、周期延拓，三种延拓得到的三角级数展开式分别为：

<equation>\textcircled{1}</equation>正弦级数展开：

<equation>f (x) \sim \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l},</equation>

---

其中

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

<equation>\textcircled{2}</equation>余弦级数展开：

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l},</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots).</equation>

<equation>\textcircled{3}</equation>三角级数展开：

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {2 n \pi x}{l} + b _ {n} \sin \frac {2 n \pi x}{l}\right),</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {2 n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {2 n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

---


### 第八章 常微分方程及差分方程


#### 2. 一阶齐次微分方程

形如

<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f (x) g (y)</equation>

或

<equation>M _ {1} (x) N _ {1} (y) \mathrm {d} x + M _ {2} (x) N _ {2} (y) \mathrm {d} y = 0</equation>

的一阶微分方程，称为变量可分离的一阶微分方程.

求通解方法：当<equation>g ( y ) \neq 0</equation>时，

<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f (x) g (y) \Leftrightarrow \frac {\mathrm {d} y}{g (y)} = f (x) \mathrm {d} x,</equation>

<equation>\int \frac {\mathrm {d} y}{g (y)} = \int f (x) \mathrm {d} x,</equation>

则有

将左、右两边的不定积分求出，整理可得方程通解.


形如

<equation>y ^ {\prime} = f \left(\frac {y}{x}\right)</equation>

---


#### 4. 伯努利方程

的一阶微分方程，叫一阶齐次微分方程

求通解方法：设<equation>u = \frac{y}{x}</equation>，将此方程化为关于未知函数<equation>u</equation>的可分离变量的一阶微分方程，求出此一阶微分方程的通解，然后将通解中的<equation>u</equation>用<equation>\frac{y}{x}</equation>替换，即得原微分方程的通解.


形如

<equation>A (x) y ^ {\prime} + B (x) y = C (x)</equation>

的一阶微分方程，叫一阶线性微分方程，其标准形式为

<equation>y ^ {\prime} + p (x) y = q (x).</equation>

当右端的<equation>q(x)</equation>恒为零时，称其为一阶线性齐次微分方程，否则称为一阶线性非齐次微分方程.

求通解方法：通解由公式

<equation>y = \mathrm {e} ^ {- \int p (x) \mathrm {d} x} \left[ \int q (x) \mathrm {e} ^ {\int p (x) \mathrm {d} x} \mathrm {d} x + C \right]</equation>

给出.


形如

<equation>y ^ {\prime} + p (x) y = q (x) y ^ {n} \quad (n \neq 0, 1)</equation>

的方程叫做伯努利方程

求通解方法：令<equation>z = y^{1 - n}</equation>，将此方程化为<equation>z</equation>的一阶

---


#### 二、可降阶的高阶微分方程

线性微分方程，求出此一阶微分方程的通解，然后将通解中的<equation>z</equation>用<equation>y^{1 - n}</equation>替换，即得原微分方程的通解.


如果存在可微函数 u（x，y），使得

<equation>\mathrm {d} u (x, y) = P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y,</equation>

则称一阶微分方程

<equation>P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y = 0</equation>

为全微分方程.


1. 形如<equation>y^{(n)}=f(x)</equation>的可降阶方程

这类微分方程只要积分<equation>n</equation>次就得到方程的通解.

2. 不显含函数 y的二阶可降阶的方程<equation>y^{\prime \prime}=f(x,y^{\prime})</equation>这类方程特点是不显含 y，若令<equation>y^{\prime}=p</equation>，则

<equation>y ^ {\prime \prime} = \frac {\mathrm {d} p}{\mathrm {d} x} = p ^ {\prime},</equation>

于是所给方程可降为一阶方程，再按一阶微分方程的方法求解.

3. 不显含自变量 x的二阶可降阶的方程<equation>y^{\prime \prime}=f(y,y^{\prime})</equation>这类方程特点是不显含 x，若令<equation>y^{\prime}=p</equation>，则

<equation>y ^ {\prime \prime} = \frac {\mathrm {d} p}{\mathrm {d} y} \cdot \frac {\mathrm {d} y}{\mathrm {d} x} = p \frac {\mathrm {d} p}{\mathrm {d} y}.</equation>

---


#### 三、线性微分方程解的结构定理

于是所给方程可降为一阶方程，再按一阶微分方程的方法求解.


一手+V：kaoyan33311

<equation>\textcircled{1}</equation>设<equation>y_{1}, y_{2}</equation>是n阶齐次线性微分方程<equation>y^{(n)}+p_{1}(x)y^{(n-1)}+p_{2}(x)y^{(n-2)}+\cdots+p_{n}(x)y=0</equation>的两个解，则

<equation>y = C _ {1} y _ {1} + C _ {2} y _ {2}</equation>

也是该方程的解，其中<equation>C_{1}, C_{2}</equation>是任意常数.

<equation>\textcircled{2}</equation>设<equation>y_{1}, y_{2}, \dots , y_{n}</equation>是n阶齐次线性微分方程<equation>y^{(n)}+p_{1}(x)y^{(n-1)}+p_{2}(x)y^{(n-2)}+\dots +p_{n}(x)y=0</equation>的n个线性无关的解，则

<equation>y = C _ {1} y _ {1} + C _ {2} y _ {2} + \dots + C _ {n} y _ {n}</equation>

是该方程的通解，其中<equation>C_{1}, C_{2}, \dots, C_{n}</equation>是任意常数.

<equation>\textcircled{3}</equation>如果<equation>y_{1}</equation>是方程

<equation>y ^ {(n)} + p _ {1} (x) y ^ {(n - 1)} + p _ {2} (x) y ^ {(n - 2)} + \dots + p _ {n} (x) y = f _ {1} (x)</equation>

的解，<equation>y_{2}</equation>是方程

<equation>y ^ {(n)} + p _ {1} (x) y ^ {(n - 1)} + p _ {2} (x) y ^ {(n - 2)} + \dots + p _ {n} (x) y = f _ {2} (x)</equation>

的解，则<equation>y_{1}+y_{2}</equation>是方程

<equation>y ^ {(n)} + p _ {1} (x) y ^ {(n - 1)} + p _ {2} (x) y ^ {(n - 2)} + \dots + p _ {n} (x) y = f _ {1} (x) + f _ {2} (x)</equation>

的解.

---


#### 1. 二阶常系数齐次线性微分方程

<equation>\textcircled{4}</equation>设<equation>y^{*}</equation>是非齐次线性微分方程

<equation>y^{(n)}+p_{1}(x)y^{(n-1)}+p_{2}(x)y^{(n-2)}+\dots+p_{n}(x)y=f(x)</equation>的一个特解，<equation>C_{1}y_{1}+C_{2}y_{2}+\dots+C_{n}y_{n}</equation>是该非齐次微分方程对应的齐次线性微分方程的通解，则该非齐次线性微分方程的通解为

<equation>y = C _ {1} y _ {1} + C _ {2} y _ {2} + \dots + C _ {n} y _ {n} + y ^ {*}.</equation>


二阶常系数齐次线性微分方程的形式为：

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = 0,</equation>

其中 p，q为常数，其特征方程为

<equation>\lambda^ {2} + p \lambda + q = 0.</equation>

方程的通解为：

<equation>\textcircled{1}</equation>特征方程有两个相异的实根<equation>\lambda_{1},\lambda_{2}</equation>时，通解形式为

<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {1} x}.</equation>

<equation>\textcircled{2}</equation>特征方程有两个相同的实根<equation>\lambda_{1}=\lambda_{2}</equation>时，通解形式为

<equation>y (x) = \left(C _ {1} + C _ {2} x\right) \mathrm {e} ^ {\lambda_ {1} x}.</equation>

<equation>\textcircled{3}</equation>特征方程有一对共轭复根<equation>\alpha \pm \beta \mathrm{i}</equation>时，通解形式为

<equation>y (x) = \mathrm {e} ^ {\alpha x} \left(C _ {1} \cos \beta x + C _ {2} \sin \beta x\right).</equation>

---


#### 五、二阶常系数非齐次线性微分方程

此种方程的一般形式为

<equation>y ^ {(n)} + p _ {1} y ^ {(n - 1)} + p _ {2} y ^ {(n - 2)} + \dots + p _ {n} y = 0,</equation>

其中<equation>p_{i}(i = 1,2,\dots ,n)</equation>为常数，相应的特征方程为

<equation>\lambda^ {n} + p _ {1} \lambda^ {n - 1} + \dots + p _ {n - 1} \lambda + p _ {n} = 0.</equation>

特征方程的根与通解的关系为：

<equation>\textcircled{1}</equation>若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>是<equation>n</equation>个互异实根，则方程的通解为

<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x} + \dots + C _ {n} \mathrm {e} ^ {\lambda_ {n} x}.</equation>

<equation>\textcircled{2}</equation>若<equation>\lambda = \lambda_0</equation>为特征方程的<equation>k(k\leqslant n)</equation>重实根，则方程的通解中含有

<equation>\left(C _ {1} + C _ {2} x + \dots + C _ {k} x ^ {k - 1}\right) \mathrm {e} ^ {\lambda x}.</equation>

<equation>\textcircled{3}</equation>若<equation>\alpha \pm \beta</equation>为特征方程的<equation>k</equation>重共轭复根，则方程的通解中含有

<equation>\begin{array}{l} \mathrm {e} ^ {\alpha x} \left[ \left(C _ {1} + C _ {2} x + \dots + C _ {k} x ^ {k - 1}\right) \cos \beta x + \right. \\ \left(D _ {1} + D _ {2} x + \dots + D _ {k} x ^ {k - 1}\right) \sin \beta x ]. \\ \end{array}</equation>


二阶常系数非齐次线性微分方程的一般形式为

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x),</equation>

其中 p, q是常数.

求特解<equation>y^{*}</equation>的待定系数法：

---

<equation>\textcircled{1}</equation>若

<equation>f (x) = P _ {m} (x) \mathrm {e} ^ {a x},</equation>

其中<equation>P_{m}(x)</equation>为<equation>x</equation>的<equation>m</equation>次多项式，则待定特解<equation>y^{*}</equation>的形式为

<equation>y ^ {*} = x ^ {k} Q _ {m} (x) \mathrm {e} ^ {a x},</equation>

其中<equation>Q_{m}(x)</equation>是与<equation>P_{m}(x)</equation>同次的多项式，调节系数

<equation>k = \left\{ \begin{array}{ll}0, & \alpha \text{不是特征方程的特征根，} \\ 1, & \alpha \text{是特征方程的单特征根，} \\ 2, & \alpha \text{是特征方程的二重特征根。} \end{array} \right.</equation>

将<equation>y^{*} = x^{k}Q_{m}(x)\mathrm{e}^{ax}</equation>代入方程

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x),</equation>

就可以求出<equation>Q_{m}(x).</equation>

<equation>\textcircled{2}</equation>若

<equation>f (x) = \mathrm {e} ^ {\alpha x} \left[ P _ {n} (x) \cos \beta x + Q _ {m} (x) \sin \beta x \right],</equation>

其中<equation>P_{n}(x), Q_{m}(x)</equation>分别为<equation>x</equation>的<equation>n</equation>次，<equation>m</equation>次多项式，则待定特解<equation>y^{*}</equation>的形式为

<equation>y ^ {*} = x ^ {k} \mathrm {e} ^ {\mathrm {a} x} \left[ M _ {i} (x) \cos \beta x + N _ {i} (x) \sin \beta x \right],</equation>

其中<equation>l = \max \{m,n\}</equation>，<equation>M_{l}(x)</equation>，<equation>N_{l}(x)</equation>是两个待定的<equation>l</equation>次多项式，调节系数

<equation>k = \left\{ \begin{array}{l l} 0, & \alpha + \beta \mathrm {i} \text {不 是 特 征 方 程 的 特 征 根}, \\ 1, & \alpha + \beta \mathrm {i} \text {是 特 征 方 程 的 特 征 根}. \end{array} \right.</equation>

---


#### 七、差分方程

形如

<equation>x ^ {n} y ^ {(n)} + p _ {1} x ^ {n - 1} y ^ {(n - 1)} + p _ {2} x ^ {n - 2} y ^ {(n - 2)} + \dots +</equation>

<equation>p _ {n - 1} x y ^ {\prime} + p _ {n} y = f (x)</equation>

的方程称为欧拉方程.

这个方程可以通过变换<equation>x = \mathrm{e}^{t}</equation>化为以<equation>t</equation>为自变量的常系数线性微分方程，求解后代回原来的变量即得欧拉方程的解.


1. 差分的定义

(1) 一阶差分

<equation>\Delta y _ {t} = y _ {t + 1} - y _ {t}.</equation>

(2) 二阶差分

<equation>\Delta^ {2} y _ {t} = y _ {t + 2} - 2 y _ {t + 1} + y _ {t}.</equation>

2. 一阶线性齐次差分方程的解法

(1) 方程形式

<equation>y _ {i + 1} - a y _ {i} = 0.</equation>

(2) 特征方程

<equation>r - a = 0.</equation>

---


#### 3. 一阶线性非齐次差分方程的解法

(3) 通解

<equation>\bar {y} _ {t} = C a ^ {t}.</equation>


(1) 方程形式

<equation>y _ {t + 1} - a y _ {t} = f (t).</equation>

(2) 通解形式

<equation>y _ {t} = \tilde {y} _ {t} + y _ {t} ^ {*}.</equation>

(3) 特解形式

<equation>\textcircled{1}</equation><equation>f(t) = P_{m}(t)</equation>，其中<equation>P_{m}(t)</equation>是 t的 m次多项式<equation>y_{t}^{*} = Q_{m}(t)</equation>，其中<equation>Q_{m}(t)</equation>是特定的 m次多项式.

<equation>\textcircled{2}</equation>若<equation>f(t) = b^{t}P_{m}(t), y_{i}^{*} = t^{k}b^{t}Q_{m}(t).</equation>

当b不是特征方程的根时，取<equation>k = 0</equation>

当b是特征方程的根时，取<equation>k = 1</equation>.

---


## 第二部分线性代数


### 第一章 行列式


#### 2. 行列式的性质

n阶行列式

<equation>\begin{array}{l} D _ {n} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| \\ = \sum_ {\left(j _ {1} j _ {2} \dots j _ {n}\right)} (- 1) ^ {r \left(j _ {1} j _ {2} \dots j _ {n}\right)} a _ {1 j _ {1}} a _ {2 j _ {2}} \dots a _ {m _ {j}}, \\ \end{array}</equation>

式中<equation>\sum_{(j_1,j_2,\dots j_n)}</equation>表示对所有<equation>n</equation>级排列<equation>(j_{1}j_{2}\dots j_{n})</equation>求和.


<equation>\textcircled{1}</equation>行列互换，行列式的值不变，也即<equation>D = D^{\mathrm{T}}</equation>

<equation>\textcircled{2}</equation>任意两行(列)互换位置后，行列式改变符号.

推论1 如果行列式中有两行（列）的对应元素相同，则行列式的值为0.

<equation>\textcircled{3}</equation>将行列式的某一行(列)乘以一个常数<equation>k</equation>后，行列式的值变为原来的<equation>k</equation>倍.

---

推论2 如果行列式的某一行（列）全为0，则行列式的值等于0.

推论3 行列式的某两行（列）元素对应成比例，则行列式的值等于0.

<equation>\textcircled{4}</equation>如果行列式某一行（列）的所有元素都可以写成两个元素的和，则该行列式可以写成两个行列式的和，这两个行列式的这一行（列）分别为对应两个加数，其余行（列）与原行列式相等，即

<equation>\begin{array}{l} \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {i 1} + b _ {i 1} & a _ {i 2} + b _ {i 2} & \dots & a _ {i n} + b _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {i 1} & a _ {i 2} & \dots & a _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| + \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ b _ {i 1} & b _ {i 2} & \dots & b _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right|. \\ \end{array}</equation>

<equation>\textcircled{5}</equation>将行列式的某行（列）的 k倍加到另一行（列）上，行列式的值不变.

---


#### 2. 行列式按一行（列）展开

在<equation>n</equation>阶行列式<equation>D = |a_{ij}|</equation>中，划掉元素<equation>a_{ij}</equation>所在第<equation>i</equation>行和第<equation>j</equation>列的所有元素后，余下<equation>(n - 1)^{2}</equation>个元素按照原有次序构成一个<equation>(n - 1)</equation>阶行列式，称之为元素<equation>a_{ij}</equation>在<equation>D</equation>中的余子式，记作<equation>M_{ij}</equation>，即

<equation>M _ {j} = \left| \begin{array}{c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 (j - 1)} & a _ {1 (j + 1)} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 (j - 1)} & a _ {2 (j + 1)} & \dots & a _ {2 n} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {(i - 1) 1} & a _ {(i - 1) 2} & \dots & a _ {(i - 1) (j - 1)} & a _ {(i - 1) (j + 1)} & \dots & a _ {(i - 1) n} \\ a _ {(i + 1) 1} & a _ {(i + 1) 2} & \dots & a _ {(i + 1) (j - 1)} & a _ {(i + 1) (j + 1)} & \dots & a _ {(i + 1) n} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n (j - 1)} & a _ {n (j + 1)} & \dots & a _ {m} \end{array} \right|</equation>

记<equation>A_{ij} = (-1)^{i+j}M_{ij}</equation>，称作元素<equation>a_{ij}</equation>的代数余子式.


n阶行列式<equation>D</equation>等于其任一行(列)各元素与其代数余子式乘积之和，即

<equation>\begin{array}{l} D = a _ {i 1} A _ {i 1} + a _ {i 2} A _ {i 2} + \dots + a _ {i n} A _ {i n} \\ = \sum_ {j = 1} ^ {n} a _ {i j} A _ {i j} \quad (i = 1, 2, \dots , n) \quad (\text {按 第} i \text {行 展 开}) \\ = a _ {1 j} A _ {1 j} + a _ {2 j} A _ {2 j} + \dots + a _ {n j} A _ {n j} \\ \end{array}</equation>

---


#### 三、几种特殊的行列式

<equation>= \sum_ {i = 1} ^ {n} a _ {i j} A _ {i j} \quad (j = 1, 2, \dots , n) (\mathrm {按 第} j \mathrm {列 展 开}).</equation>

推论：行列式<equation>D</equation>的某一行（列）各元素与另一行（列）对应元素的代数余子式的乘积之和为零，即

<equation>\begin{array}{l} \sum_ {j = 1} ^ {n} a _ {i j} A _ {k j} = a _ {i 1} A _ {k 1} + a _ {i 2} A _ {k 2} + \dots + a _ {i n} A _ {k n} = 0, \quad (i \neq k) \\ \sum_ {j = 1} ^ {n} a _ {i j} A _ {j k} = a _ {1 i} A _ {1 k} + a _ {2 i} A _ {2 k} + \dots + a _ {n i} A _ {n k} = 0. \quad (i \neq k) \\ \end{array}</equation>


1. 上三角形、下三角形、对角形行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c} a _ {1 1} & 0 & \dots & 0 \\ 0 & a _ {2 2} & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & a _ {m} \end{array} \right| = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ 0 & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & a _ {m} \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & 0 & \dots & 0 \\ a _ {2 1} & a _ {2 2} & \dots & 0 \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| \\ = a _ {1 1} a _ {2 2} \dots a _ {m}. \\ \end{array}</equation>

---

2. 次对角线行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c} 0 & \dots & 0 & a _ {1 n} \\ 0 & \dots & a _ {2 (n - 1)} & 0 \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & 0 & 0 \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & \dots & a _ {1 (n - 1)} & a _ {1 n} \\ a _ {2 1} & \dots & a _ {2 (n - 1)} & 0 \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & 0 & 0 \end{array} \right| \\ = \left| \begin{array}{c c c c} 0 & \dots & 0 & a _ {1 n} \\ 0 & \dots & a _ {2 (n - 1)} & a _ {2 n} \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & a _ {n (n - 1)} & a _ {n n} \end{array} \right| \\ = (- 1) ^ {\frac {n (n - 1)}{2}} a _ {1 n} \dots a _ {n 1}. \\ \end{array}</equation>

3. 范德蒙德行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c c} 1 & 1 & 1 & \dots & 1 \\ a _ {1} & a _ {2} & a _ {3} & \dots & a _ {n} \\ a _ {1} ^ {2} & a _ {2} ^ {2} & a _ {3} ^ {2} & \dots & a _ {n} ^ {2} \\ \vdots & \vdots & \vdots & & \vdots \\ a _ {1} ^ {n - 1} & a _ {2} ^ {n - 1} & a _ {3} ^ {n - 1} & \dots & a _ {n} ^ {n - 1} \end{array} \right| \\ = \prod_ {1 \leq i < j \leq n} \left(a _ {j} - a _ {i}\right). \\ \end{array}</equation>

---


#### 4. 拉普拉斯展开式

<equation>\begin{array}{l} \left| \begin{array}{c c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 k} & & & & \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 k} & \boldsymbol {O} _ {k \times l} & & \\ \vdots & \vdots & & \vdots & & & & \\ a _ {k 1} & a _ {k 2} & \dots & a _ {b k} & & & & \\ c _ {1 1} & c _ {1 2} & \dots & c _ {1 k} & b _ {1 1} & b _ {1 2} & \dots & b _ {1 l} \\ c _ {2 1} & c _ {2 2} & \dots & c _ {2 k} & b _ {2 1} & b _ {2 2} & \dots & b _ {2 l} \\ \vdots & \vdots & & \vdots & \vdots & \vdots & & \vdots \\ c _ {i 1} & c _ {i 2} & \dots & c _ {i k} & b _ {i 1} & b _ {i 2} & \dots & b _ {i l} \end{array} \right| \\ = \left| \begin{array}{c c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 k} & \left| \begin{array}{c c c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 l} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 l} \\ \vdots & \vdots & & \vdots \\ b _ {i 1} & b _ {i 2} & \dots & b _ {i l} \end{array} \right| \\ c _ {1 1} c _ {1 2} \dots c _ {1 k} b _ {1 1} b _ {1 2} \dots b _ {1 l} \\ c _ {2 1} c _ {2 2} \dots c _ {2 k} b _ {2 1} b _ {2 2} \dots b _ {2 l} \\ \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \\ c _ {i 1} c _ {i 2} \dots c _ {i k} b _ {i 1} b _ {i 2} \dots b _ {i l} \\ a _ {1 1} a _ {1 2} \dots a _ {1 k} \\ a _ {2 1} a _ {2 2} \dots a _ {2 k} \\ \vdots \vdots \vdots \vdots \\ a _ {k 1} a _ {k 2} \dots a _ {b k} \end{array} \right| \\ \end{array}</equation>

---


#### 四、有关行列式的若干个重要公式

<equation>= (- 1) ^ {k} \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 k} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 k} \\ \vdots & \vdots & & \vdots \\ a _ {k 1} & a _ {k 2} & \dots & a _ {k k} \end{array} \right| \left| \begin{array}{c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 l} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 l} \\ \vdots & \vdots & & \vdots \\ b _ {l 1} & b _ {l 2} & \dots & b _ {l l} \end{array} \right|.</equation>


为便于考生综合复习及掌握概念间的联系，现将以后各章所涉及的有关行列式的几个重要公式罗列于下.

设<equation>A, B</equation>均为<equation>n</equation>阶方阵，<equation>k</equation>为常数，<equation>E</equation>为<equation>n</equation>阶单位矩阵，<equation>A^{*}</equation>为<equation>A</equation>的伴随矩阵：

<equation>\textcircled{1}</equation><equation>|k\mathbf{A}| = k^{n} \cdot |\mathbf{A}|</equation>.

<equation>\textcircled{2}</equation>若<equation>A</equation>是可逆矩阵，则有<equation>|A^{-1}| = \frac{1}{|A|}</equation>.

<equation>\textcircled{3}</equation><equation>|\mathbf{A} \cdot \mathbf{B}| = |\mathbf{A}| \cdot |\mathbf{B}|.</equation>

<equation>\textcircled{4}</equation><equation>|\mathbf{A}^{*}|=|\mathbf{A}|^{n-1}.</equation>

<equation>\textcircled{5}</equation><equation>A \cdot A^{*} = A^{*} \cdot A = |A| \cdot E.</equation>

<equation>\textcircled{6} |\mathbf{A}| = \prod_{i=1}^{n} \lambda_{i}</equation>（<equation>\lambda_{1}, \lambda_{2}, \dots, \lambda_{n}</equation>是<equation>\mathbf{A}</equation>的全部特征值).

<equation>\textcircled{7}</equation><equation>|A| \neq 0 \Leftrightarrow A</equation>为可逆矩阵<equation>\Leftrightarrow A</equation>为满秩矩阵，即<equation>r(A)=n.</equation>

---


### 第二章 矩阵


#### 1. 矩阵的定义

由<equation>m \times n</equation>个数<equation>a_{ij}(i = 1,2,\dots,m;j = 1,2,\dots,n)</equation>排列成的<equation>m</equation>行<equation>n</equation>列的数表

<equation>\left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {m 1} & a _ {m 2} & \dots & a _ {m n} \end{array} \right]</equation>

称为<equation>m \times n</equation>矩阵，记为<equation>A = (a_{ij})_{m \times n}</equation>，其中<equation>a_{ij}</equation>称为矩阵<equation>A</equation>的第<equation>i</equation>行第<equation>j</equation>列的元素.

<equation>\textcircled{1}</equation>当<equation>n = m</equation>时，<equation>A</equation>也称为<equation>n</equation>阶方阵，<equation>|A|</equation>称为<equation>A</equation>的行列式.

<equation>\textcircled{2}</equation>两个矩阵<equation>A = (a_{ij})_{m\times n},B = (b_{ij})_{s\times k}</equation>，如果<equation>m = s,n = k</equation>，则称它们为同型矩阵.

<equation>\textcircled{3}</equation>如果两个同型矩阵<equation>A = (a_{ij})_{m\times n},B = (b_{ij})_{m\times n}</equation>对应的元素相等，也即

<equation>a _ {i j} = b _ {i j} (i = 1, \dots , m; j = 1, \dots , n),</equation>

---

则称矩阵 A与矩阵 B相等，记作<equation>A=B.</equation>

常见的特殊矩阵有：

<equation>\textcircled{1}</equation>零矩阵：所有元素均为0的矩阵称之为零矩阵，记为0.

<equation>\textcircled{2}</equation>对角矩阵：主对角线以外的元素均为0的矩阵称之为对角矩阵，记作<equation>\operatorname{diag}\left(a_{1}, a_{2}, \dots, a_{n}\right)</equation>，即

<equation>\mathbf {d i a g} \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) = \left[ \begin{array}{c c c c} a _ {1} & & & \\ & a _ {2} & & \\ & & \ddots & \\ & & & a _ {n} \end{array} \right].</equation>

两个对角矩阵的乘积仍为对角矩阵.

<equation>\textcircled{3}</equation>单位矩阵：主对角线上的元素均为1，其余元素均为0的矩阵称之为单位矩阵，记作E.单位矩阵与任何矩阵相乘都可交换，即

<equation>E A = A E = A.</equation>

<equation>\textcircled{4}</equation>上（下）三角矩阵：主对角线以下的元素全为0的矩阵称之为上三角矩阵；主对角线以上的元素全为0的矩阵称之为下三角矩阵.

<equation>\textcircled{5}</equation>对称矩阵：满足条件<equation>A^{\mathrm{T}}=A</equation>的 n阶矩阵 A称为对称矩阵.即

A为对称矩阵<equation>\Leftrightarrow a_{ij} = a_{ji}</equation>（<equation>i,j=1,2,\dots,n)</equation>

<equation>\textcircled{6}</equation>反对称矩阵：满足条件<equation>A^{\mathrm{T}} = -A</equation>的<equation>n</equation>阶矩阵<equation>A</equation>

---


#### 注 两个相加的矩阵必须是同型的.

称为反对称矩阵。即

<equation>\mathbf{A} = ( a_{ij} )_{n\times n}</equation>为反对称矩阵<equation>\Leftrightarrow a_{ij} = -a_{ji}</equation>（i,j=1,2，…,n)

<equation>\textcircled{7}</equation>正交矩阵：设<equation>A</equation>是<equation>n</equation>阶矩阵，如果<equation>A A^{\mathrm{T}} = A^{\mathrm{T}} A = E</equation>，则称<equation>A</equation>是正交矩阵.


设<equation>A=(a_{ij})</equation><equation>B=(b_{ij})</equation>是两个 m×n矩阵，定义矩阵<equation>C=(c_{ij})=(a_{ij}+b_{ij})</equation>为矩阵 A与矩阵 B的和，记作 C=A +B.


加法的运算性质：

<equation>\textcircled{1}</equation><equation>\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}</equation>（交换律）；

<equation>\textcircled{2}</equation><equation>(\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})</equation>（结合律）；

<equation>\textcircled{3}</equation><equation>\mathbf{A}+\mathbf{O}=\mathbf{A}</equation>（其中<equation>\mathbf{O}=(0)_{m\times n}</equation>）；

<equation>\textcircled{4}</equation><equation>A + (-A) = O</equation>（其中<equation>-A = (-a_{ij})_{m \times n}</equation>）。

(2) 矩阵的数乘

设<equation>A = (a_{ij})</equation>是一个<equation>m\times n</equation>矩阵，<equation>k</equation>为任意实数，则定义

<equation>k\mathbf{A} = (k a_{ij}) \quad (i = 1,2,\dots,m; j = 1,2,\dots,n)</equation>为矩阵的数乘.

数乘的运算性质：

<equation>\textcircled{1} k(l\mathbf{A}) = (kl)\mathbf{A} = l(k\mathbf{A})</equation>（k，l为数）；

---


#### (3)矩阵的乘法

<equation>\textcircled{2} (\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})</equation>;

<equation>\textcircled{3} k(\mathbf{A} + \mathbf{B}) = k\mathbf{A} + k\mathbf{B}</equation>;

<equation>\textcircled{4} ( k+l ) \mathbf{A}=k \mathbf{A}+l \mathbf{A}.</equation>


设<equation>\mathbf{A} = (a_{ij})_{m\times n},\mathbf{B} = (b_{ij})_{n\times k}</equation>（注意<equation>\mathbf{A}</equation>的列数和<equation>\mathbf{B}</equation>的行数相等），定义矩阵

<equation>\mathbf {C} = \left(c _ {i j}\right) _ {m \times k},</equation>

其中

<equation>c _ {i j} = a _ {i 1} b _ {1 j} + a _ {i 2} b _ {2 j} + \dots + a _ {i n} b _ {n j} = \sum_ {k = 1} ^ {n} a _ {i k} b _ {k j},</equation>

称为矩阵<equation>A</equation>与矩阵<equation>B</equation>的乘积，记作<equation>C = AB</equation>

数乘的运算性质：

<equation>\textcircled{1}</equation><equation>\mathbf{(A B) C}=\mathbf{A( B C)}</equation>（结合律）；

<equation>\textcircled{2}</equation><equation>\mathbf{A} (\mathbf{B}+\mathbf{C})=\mathbf{A B}+\mathbf{A C},</equation>

（<equation>\mathbf{B}+\mathbf{C} )\mathbf{A}=\mathbf{B}\mathbf{A}+\mathbf{C}\mathbf{A}</equation>（分配律）；

<equation>\textcircled{3}</equation><equation>( k A ) B=A ( k B )=k ( A B )</equation>（数与乘积的结合律).

注<equation>\textcircled{1}</equation>不是任意两个矩阵<equation>A</equation>与<equation>B</equation>都能相乘的，必须有<equation>A</equation>的列数和<equation>B</equation>的行数相等.

<equation>\textcircled{2}</equation>矩阵乘法一般来说不满足交换律，即一般情况下，<equation>\mathbf{A B}\neq \mathbf{B A}.</equation>

<equation>\textcircled{3}</equation>矩阵的运算也不满足消去律. 即由<equation>AB = AC</equation>且<equation>A \neq O</equation>, 得不出<equation>B = C</equation>.

---


#### （4）方阵的乘幂运算

<equation>\textcircled{4}</equation>零因子定律不成立，即由<equation>AB = O</equation>并不能得到<equation>A = O</equation>或<equation>B = O.</equation>


如果矩阵<equation>A</equation>为方阵，则定义<equation>A^{n} = \underbrace{A \cdot A \cdots A}_{n \text{个} A}</equation>为矩阵<equation>A</equation>的<equation>n</equation>次幂.规定<equation>A^{0} = E</equation>（单位矩阵）.

乘幂的运算性质：

<equation>\textcircled{1}</equation><equation>A^{k} \cdot A^{l} = A^{k+l}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}^{k}\right)^{l}=\mathbf{A}^{k l}.</equation>

注 一般情况下，<equation>(\mathbf{A}\cdot \mathbf{B})^{k}\neq A^{k}\cdot B^{k}.</equation>

(5) 矩阵的转置

设<equation>A_{m\times n} = \left[ \begin{array}{cccc} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{array} \right]_{m\times n}</equation>，定义A的转置

矩阵为

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {2 1} & \dots & a _ {m 1} \\ a _ {1 2} & a _ {2 2} & \dots & a _ {m 2} \\ \vdots & \vdots & & \vdots \\ a _ {1 n} & a _ {2 n} & \dots & a _ {m n} \end{array} \right] _ {n \times m},</equation>

即转置矩阵<equation>A^{\mathrm{T}}</equation>的第<equation>i</equation>行第<equation>j</equation>列元素等于原矩阵<equation>A</equation>的第<equation>j</equation>行第<equation>i</equation>列元素.

转置的运算规则：

---

<equation>\textcircled{1} (\mathbf{A}^{\mathrm{T}})^{\mathrm{T}} = \mathbf{A}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}+\mathbf{B}\right)^{\mathrm{T}}=\mathbf{A}^{\mathrm{T}}+\mathbf{B}^{\mathrm{T}};</equation>

<equation>\textcircled{3}</equation><equation>\mathbf{A B} )^{\mathrm{T}}=\mathbf{B}^{\mathrm{T}} \mathbf{A}^{\mathrm{T}};</equation>

<equation>\textcircled{4} ( k \mathbf{A} )^{\mathrm{T}}=k \cdot \mathbf{A}^{\mathrm{T}}.</equation>

(6) 方阵的行列式

若<equation>\mathbf{A} = (a_{i j})_{n\times n},\mathbf{B} = (b_{i j})_{n\times n}</equation>，则

<equation>| \mathbf {A} | = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right|,</equation>

且<equation>|kA| = k^{n}|A|, |AB| = |A||B|.</equation>

(7) 矩阵的求逆运算

<equation>\textcircled{1}</equation>逆矩阵的定义及定理

若<equation>A, B</equation>均为<equation>n</equation>阶方阵，且满足<equation>AB = BA = E</equation>，则称<equation>A</equation>是可逆矩阵，又称<equation>B</equation>是<equation>A</equation>的逆矩阵，记作<equation>B = A^{-1}</equation>.

(a)若矩阵<equation>A</equation>可逆，则<equation>A</equation>的逆矩阵<equation>A^{-1}</equation>是唯一的.

(b) 矩阵<equation>A</equation>可逆的充分必要条件是<equation>|A| \neq 0</equation>.

(c) 若<equation>|A| \neq 0</equation>，则<equation>A^{-1} = \frac{1}{|A|} A^{*}</equation>，其中

<equation>\boldsymbol {A} ^ {*} = \left[ \begin{array}{c c c c} A _ {1 1} & A _ {2 1} & \dots & A _ {n 1} \\ A _ {1 2} & A _ {2 2} & \dots & A _ {n 2} \\ \vdots & \vdots & & \vdots \\ A _ {1 n} & A _ {2 n} & \dots & A _ {m} \end{array} \right],</equation>

---


#### 3. 矩阵经过运算后秩的变化规律

称为<equation>\mathbf{A}</equation>的伴随矩阵（其中<equation>A_{y}</equation>是元素<equation>a_{y}</equation>的代数余子式）.

由<equation>A^{+}</equation>的构成，可得到以下重要的公式：

<equation>A A ^ {*} = A ^ {*} A = | A | E.</equation>

<equation>\textcircled{2}</equation>求逆运算的运算规则

若<equation>\mathbf{A},\mathbf{B}</equation>均为 n阶可逆矩阵，则

(a)<equation>(\mathbf{A}^{-1})^{-1} = \mathbf{A}</equation>;

(b) 若<equation>k\neq 0</equation>为常数，则<equation>(kA)^{-1} = \frac{1}{k} A^{-1}</equation>；

(c)<equation>(\mathbf{A B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1};</equation>

(d)<equation>A^{\mathrm{T}}</equation>也可逆，且<equation>(A^{\mathrm{T}})^{-1} = (A^{-1})^{\mathrm{T}};</equation>

(e)<equation>|\mathbf{A}^{-1}| = |\mathbf{A}|^{-1}.</equation>


在<equation>A_{m \times n}</equation>中，任取<equation>k</equation>行、<equation>k</equation>列，在这<equation>k</equation>行<equation>k</equation>列的交错处有<equation>k^2</equation>个元素，这<equation>k^2</equation>个元素按原有的次序构成一个<equation>k</equation>阶行列式，称为<equation>A</equation>的一个<equation>k</equation>阶子式。


在<equation>A_{m \times n}</equation>中，至少有一个<equation>r</equation>阶子式不为零，而所有<equation>r + 1</equation>阶子式全为零，则称<equation>A</equation>的秩为<equation>r</equation>，记作<equation>\operatorname{rank}(A) = r</equation>，简记为<equation>r(A) = r</equation>或<equation>R(A) = r</equation>。


<equation>\textcircled{1}</equation><equation>r(\mathbf{A}^{\mathrm{T}}) = r(\mathbf{A})</equation>;

---


#### 1. 分块矩阵的定义

<equation>\textcircled{2} r ( A_{m \times n} ) \leqslant\min \{ m,n \} ;</equation>

<equation>\textcircled{3}</equation><equation>r(\mathbf{A}) = 0 \Leftrightarrow \mathbf{A} = \mathbf{O}</equation>;

<equation>\textcircled{4}</equation><equation>r(k\mathbf{A}) = \left\{ \begin{array}{ll} r(\mathbf{A}), & k \neq 0, \\ 0, & k = 0; \end{array} \right.</equation>

<equation>\textcircled{5} r(\mathbf{A} + \mathbf{B}) \leqslant r(\mathbf{A}) + r(\mathbf{B})</equation>;

<equation>\textcircled{6} r ( \mathbf{A B} ) \leqslant\min \{ r ( \mathbf{A} ) , r ( \mathbf{B} ) \} ;</equation>

<equation>\textcircled{7}</equation>若有矩阵<equation>A_{m\times n}, B_{n\times s}</equation>，且<equation>AB = O</equation>，且<equation>r(A) + r(B) \leqslant n</equation>；

<equation>\textcircled{8}</equation>若<equation>P, Q</equation>为满秩方阵，则

<equation>r (P A) = r (A) = r (A Q) = r (P A Q);</equation>

<equation>\textcircled{9}</equation>初等变换不改变矩阵的秩. 若<equation>B</equation>是阶梯形矩阵，则<equation>r(B)</equation>等于<equation>B</equation>中非零行的个数；

<equation>\textcircled{10}</equation>关于伴随矩阵<equation>A^{*}</equation>的秩：

<equation>r \left(\boldsymbol {A} ^ {*}\right) = \left\{ \begin{array}{l l} n, r (\boldsymbol {A}) = n, \\ 1, r (\boldsymbol {A}) = n - 1, \\ 0, r (\boldsymbol {A}) \leqslant n - 2. \end{array} \right.</equation>


用贯穿矩阵的横线和纵线（称为分划线）把一个矩阵分成若干小块，每一小块称为原矩阵的子块，一般记作<equation>A_{ij}</equation>，分为子块的矩阵叫做分块矩阵。由于不同的需要，同一矩阵可以有不同的分块方法。例如：

---


#### (2) 数乘

$$

\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ \dots \dots

<equation>\boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} & a _ {3 4} \\ a _ {4 1} & a _ {4 2} & a _ {4 3} & a _ {4 4} \end{array} \right] = \left(\boldsymbol {p} _ {1}, \boldsymbol {p} _ {2}, \boldsymbol {p} _ {3}, \boldsymbol {p} _ {4}\right) _ {1 \times 4}.</equation>


<equation>A, B \in M_{m,n}</equation>，且有相同的分块划分方法：<equation>A = \left(A_{ij}\right)_{s \times t}, B = \left(B_{ij}\right)_{s \times t}</equation>，则

<equation>A + B = \left(A_{ij} + B_{ij}\right)_{s\times l}</equation>（每个对应子块可加）.


设<equation>A = \left(A_{ij}\right)_{s\times t}\in M_{m,n}</equation>，则

<equation>k \boldsymbol {A} = \left(k \boldsymbol {A} _ {i j}\right) _ {s \times t}.</equation>

(3) 转置

若

<equation>\boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 t} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \dots & \boldsymbol {A} _ {2 t} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {s 1} & \boldsymbol {A} _ {s 2} & \dots & \boldsymbol {A} _ {x} \end{array} \right] = \left(\boldsymbol {A} _ {i j}\right) _ {s \times t} \in M _ {m, n},</equation>

---


#### (4)乘法

则

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 1} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s 1} ^ {\mathrm {T}} \\ \boldsymbol {A} _ {1 2} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 2} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s 2} ^ {\mathrm {T}} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {1 t} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 t} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s t} ^ {\mathrm {T}} \end{array} \right],</equation>

即分块矩阵先转置后，再将每个子矩阵分别单独转置即为原矩阵的转置矩阵.


设

<equation>\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 t} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \dots & \boldsymbol {A} _ {2 t} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {s 1} & \boldsymbol {A} _ {s 2} & \dots & \boldsymbol {A} _ {s t} \end{array} \right] = \left(\boldsymbol {A} _ {i j}\right) _ {s \times t} \in M _ {m, n}, \\ \boldsymbol {B} = \left[ \begin{array}{c c c c} \boldsymbol {B} _ {1 1} & \boldsymbol {B} _ {1 2} & \dots & \boldsymbol {B} _ {1 r} \\ \boldsymbol {B} _ {2 1} & \boldsymbol {B} _ {2 2} & \dots & \boldsymbol {B} _ {2 r} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {B} _ {t 1} & \boldsymbol {B} _ {t 2} & \dots & \boldsymbol {B} _ {t r} \end{array} \right] = \left(\boldsymbol {B} _ {j k}\right) _ {t \times r} \in M _ {m, n}, \\ \boldsymbol {C} = \boldsymbol {A} \boldsymbol {B} = \left[ \begin{array}{c c c c} \boldsymbol {C} _ {1 1} & \boldsymbol {C} _ {1 2} & \dots & \boldsymbol {C} _ {1 r} \\ \boldsymbol {C} _ {2 1} & \boldsymbol {C} _ {2 2} & \dots & \boldsymbol {C} _ {2 r} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {C} _ {s 1} & \boldsymbol {C} _ {s 2} & \dots & \boldsymbol {C} _ {s r} \end{array} \right], \\ \end{array}</equation>

---


#### 3. 分块对角形（对角块）矩阵

其中<equation>C_{ik} = A_{i1}B_{1k} + A_{i2}B_{2k} + \dots + A_{it}B_{tk} = \sum_{j=1}^{i}A_{ij}B_{jk}</equation><equation>(i = 1,\dots,s;k = 1,\dots,r).</equation>


一般地，分块矩阵<equation>A = \left[ \begin{array}{cccc}A_{11} & O & \dots & O\\ O & A_{22} & \dots & O\\ \vdots & \vdots & & \vdots \\ O & O & \dots & A_{s} \end{array} \right],</equation>

简记为<equation>A = \left[ \begin{array}{c c c c} A_{11} & & & \\ & A_{22} & & \\ & & \ddots & \\ & & & A_{ss} \end{array} \right],</equation>其中<equation>A_{ii}</equation>均为小方

阵，则称<equation>A</equation>为对角块矩阵或分块对角形矩阵。若<equation>A, B</equation>均为对角块矩阵，则<equation>A + B, AB</equation>也为对角块矩阵，如：

<equation>\begin{array}{l} \boldsymbol {A} + \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] + \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1} + \boldsymbol {B} _ {1} & & & \\ & \boldsymbol {A} _ {2} + \boldsymbol {B} _ {2} & & \\ & & \ddots & \\ & & & \boldsymbol {A} _ {s} + \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

---


#### 1. 矩阵的初等行（列）变换

其中，<equation>A_{i}, B_{i}</equation>为同阶子矩阵

<equation>\begin{array}{l} \boldsymbol {A} \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {A} _ {2} \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

其中，<equation>A_{i}, B_{i}</equation>为同阶子矩阵

对角块矩阵的逆矩阵公式（设<equation>A_{1}, A_{2}, A_{3}</equation>均可逆）：

<equation>\begin{array}{l} \left[ \begin{array}{c c c} A _ {1} & & \\ & A _ {2} & \\ & & A _ {3} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c c} A _ {1} ^ {- 1} & & \\ & A _ {2} ^ {- 1} & \\ & & A _ {3} ^ {- 1} \end{array} \right], \\ \left[ \begin{array}{c c c} & & A _ {1} \\ & A _ {2} & \\ A _ {3} & & \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c c} & & A _ {3} ^ {- 1} \\ & A _ {2} ^ {- 1} & \\ A _ {1} ^ {- 1} & & \end{array} \right]. \\ \end{array}</equation>


矩阵的初等变换指的是对矩阵施行以下三种行（列）变换：

---


#### (1) 初等行交换矩阵

<equation>\textcircled{1}</equation>交换变换：互换矩阵中的某两行（列）；

<equation>\textcircled{2}</equation>倍乘变换：用一个非零常数<equation>k</equation>乘矩阵的某行(列)；

<equation>\textcircled{3}</equation>倍加变换：将矩阵的某行（列）的 k 倍加到另一行（列）上.


形如

<equation>\left[ \begin{array}{l l l} 0 & 1 & 3 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array} \right], \left[ \begin{array}{c c c c c} 1 & 2 & - 1 & 2 & 5 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 4 & 1 \end{array} \right], \left[ \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 2 & 3 \\ 0 & 0 & 3 \end{array} \right]</equation>

的矩阵称为阶梯形矩阵.

阶梯形矩阵有以下特征：

<equation>\textcircled{1}</equation>全零行位于矩阵的最下方.

<equation>\textcircled{2}</equation>每个非零行的第一个非零元素<equation>c_{ij}</equation>（亦称主元）的列标<equation>j</equation>随着行标<equation>i</equation>的递增而严格增大.

<equation>\textcircled{3}</equation>任一个矩阵经过若干次初等行（列）变换都可以化成阶梯形矩阵.


将单位矩阵作了一次初等行（列）变换的矩阵称作初等矩阵.

三种初等行（列）变换矩阵：


将单位矩阵的第<equation>i</equation>行、第<equation>j</equation>行交换后所得到的矩阵，记作

---


#### （3）初等行倍加矩阵

<equation>\boldsymbol {P} ((i) \leftrightarrow (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ \ddots & & & & \\ & 0 & \dots & 1 & \\ & \vdots & & \vdots & \\ & 1 & \dots & 0 & \\ & & & \ddots & \\ & & & & 1 \end{array} \right] \leftarrow i \text {行} \quad \leftarrow j \text {行}</equation>

作用：将初等行交换矩阵左乘 A，即若

<equation>P ((i) \leftrightarrow (j)) A = A _ {1},</equation>

则<equation>A_{1}</equation>就是将<equation>A</equation>的第<equation>i</equation>行、第<equation>j</equation>行交换后的结果.


将单位矩阵的第 i 行乘以不为零的常数 k后所得到的矩阵，记作

<equation>\boldsymbol {P} ((k (i)) = \left[ \begin{array}{c c c c} 1 & & & \\ & \ddots & & \\ & & k & \\ & & & \ddots \\ & & & 1 \end{array} \right] \leftarrow i \text {行}.</equation>

作用：若<equation>P(k(i))A = A_{2}</equation>，则<equation>A_{2}</equation>就是将<equation>A</equation>的第<equation>i</equation>行乘上<equation>k</equation>倍后的结果.


将单位矩阵第<equation>i</equation>行的<equation>k</equation>倍加到第<equation>j</equation>行后所得到的矩阵，记作

---


#### （4）初等列交换矩阵

<equation>\boldsymbol {P} (k (i) + (j)) = \left[ \begin{array}{c c c c c c} 1 & & & & & \\ & \ddots & & & & \\ & & 1 & & & \\ & & \vdots & \ddots & & \\ & & k & \dots & 1 & \\ & & & & \ddots & \\ & & & & & 1 \end{array} \right] \leftarrow i \text {行} \leftarrow j \text {行}</equation>

作用：若<equation>\mathbf{P}(k(i) + (j))\mathbf{A} = \mathbf{A}_3</equation>，则<equation>\mathbf{A}_3</equation>就是将<equation>\mathbf{A}</equation>的第<equation>i</equation>行的<equation>k</equation>倍加到第<equation>j</equation>行上的结果.


将单位矩阵第 i列与第 j列交换后所得到的矩阵，记作

<equation>Q ((i) \leftrightarrow (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ \ddots & & & & \\ & 0 \quad \dots & 1 & & \\ & \vdots & & \vdots & \\ & 1 \quad \dots & 0 & & \\ & & & \ddots & \\ & & & & 1 \end{array} \right]</equation>

作用：将初等列交换矩阵右乘<equation>A</equation>，即若<equation>AQ((i)\leftrightarrow(j)) = A_{4}</equation>，则<equation>A_{4}</equation>就是将<equation>A</equation>的第<equation>i</equation>列与第<equation>j</equation>列交换后的结果.

---


#### （6）初等列倍加矩阵

将单位矩阵的第<equation>i</equation>列乘以一个不等于零的常数<equation>k</equation>后得到的矩阵，记作

<equation>Q (k (i)) = \left[ \begin{array}{c c c c} 1 & & & \\ & \ddots & & \\ & & k & \\ & & & \ddots \\ & & & 1 \end{array} \right].</equation>

作用：若<equation>AQ(k(i)) = A_{5}</equation>，则<equation>A_{5}</equation>就是将<equation>\mathbf{A}</equation>的第<equation>i</equation>列乘上<equation>k</equation>倍后的结果.


将单位矩阵第<equation>i</equation>列的<equation>k</equation>倍加到第<equation>j</equation>列后所得到的矩阵，记作

<equation>Q (k (i) + (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ & \ddots & & \\ & & 1 \dots k & \\ & & \ddots \vdots & \\ & & & 1 \\ & & & \ddots \\ & & & 1 \\ \uparrow_ {i \text {列}} & \uparrow_ {j \text {列}} \end{array} \right].</equation>

---


#### 6. 用初等行(列)变换法求矩阵的秩

作用：若<equation>A Q (k (i) + (j)) = A_{6}</equation>，则<equation>A_{6}</equation>就是将<equation>A</equation>的第<equation>i</equation>列的<equation>k</equation>倍加到第<equation>j</equation>列上的结果.


<equation>\textcircled{1} P ((i) \leftrightarrow (j)) = Q ((i) \leftrightarrow (j)) = Q ^ {\mathrm {T}} ((i) \leftrightarrow (j));</equation>

<equation>\textcircled{2} \boldsymbol {P} (k (i)) = \boldsymbol {Q} (k (i)) = \boldsymbol {Q} ^ {\mathrm {T}} (k (i));</equation>

<equation>\textcircled{3} \boldsymbol {P} (k (i) + (j)) = \boldsymbol {Q} ^ {\mathrm {T}} (k (i) + (j)).</equation>

即：初等行变换矩阵与同类型的初等列变换矩阵之间为转置关系（事实上前两类是相等的对称矩阵）。


<equation>\textcircled{1}</equation>初等矩阵都是可逆矩阵.

<equation>\textcircled{2}</equation>初等矩阵的逆矩阵也是初等矩阵.

<equation>\textcircled{3}</equation>任一个可逆矩阵经过有限次的初等行变换都可化成单位矩阵.

<equation>\textcircled{4}</equation>一个可逆矩阵可分解为一系列初等矩阵的乘积.


初等行（列）变换不改变矩阵的秩.

矩阵的初等行（列）变换前后，矩阵的秩是相等的，而阶梯形矩阵的秩等于阶梯形矩阵中非零行的个数，由任一个矩阵都可经过若干次初等行（列）变换化成阶梯形矩阵，因此任一个矩阵的秩都可通过初等行（列）变换化成阶梯形矩阵后方便地求得.

---


#### (1)等价

<equation>\textcircled{1}</equation>定义

若矩阵<equation>A</equation>可经过一系列初等行变换和列变换后化成矩阵<equation>B</equation>，则称矩阵<equation>A</equation>与<equation>B</equation>是等价的，记作<equation>A\cong B</equation>

<equation>\textcircled{2}</equation>性质

(a)<equation>A\cong A</equation>;

(b)<equation>A\cong B</equation>，则<equation>B\cong A</equation>;

(c)<equation>A\cong B, B\cong C</equation>，则<equation>A\cong C;</equation>

(d)同型矩阵<equation>\mathbf{A}</equation>与<equation>\mathbf{B}</equation>等价<equation>\Leftrightarrow r(\mathbf{A})=r(\mathbf{B}).</equation>

(2) 相似

<equation>\textcircled{1}</equation>定义

对于同阶方阵<equation>A, B</equation>，若存在<equation>|P| \neq 0</equation>，使<equation>P^{-1}AP = B</equation>，则称<equation>A</equation>与<equation>B</equation>相似，记作<equation>A \sim B</equation>.

<equation>\textcircled{2}</equation>性质

(a)<equation>A\sim A</equation>;

(b)<equation>A\sim B</equation>，则<equation>B\sim A</equation>

(c)<equation>A\sim B, B\sim C</equation>，则<equation>A\sim C;</equation>

(d)若<equation>\mathbf{A}\sim\mathbf{B}</equation>，则<equation>\mathbf{A}^{\mathrm{T}}\sim\mathbf{B}^{\mathrm{T}}</equation>

(e) 若<equation>A, B</equation>可逆且<equation>A\sim B</equation>，则<equation>A^{-1}\sim B^{-1}</equation>；

(f)<equation>A\sim B\Rightarrow A^{n}\sim B^{n}, n</equation>为正整数；

(g)相似矩阵有相同的特征值；

（h）相似矩阵的行列式、秩相等；

---


#### (2)性质

（i）同阶实对称矩阵相似的充要条件是它们有相同的特征值（包括重数）.


对于同阶方阵<equation>A, B</equation>，若存在<equation>|P| \neq 0</equation>，使<equation>P^{\mathrm{T}} A P = B</equation>，则称<equation>A</equation>与<equation>B</equation>合同，记为<equation>A \cong B</equation>.


(a)<equation>A\cong A</equation>;

(b) 若<equation>A\cong B</equation>，则<equation>B\cong A;</equation>

(c) 若<equation>A\cong B, B\cong C</equation>，则<equation>A\cong C;</equation>

（d）同阶实对称矩阵合同的充要条件是秩相等且正惯性指数相等.


<equation>\textcircled{1}</equation>相似<equation>\Rightarrow</equation>等价；

<equation>\textcircled{2}</equation>合同<equation>\Rightarrow</equation>等价；

<equation>\textcircled{3}</equation>若<equation>A</equation>与<equation>B</equation>都是实对称矩阵，则<equation>A</equation>与<equation>B</equation>相似<equation>\Leftrightarrow A</equation>与<equation>B</equation>合同


若存在非零向量<equation>\alpha</equation>，使<equation>A\alpha = \lambda \alpha</equation>，则称<equation>\lambda</equation>为方阵<equation>A</equation>的特征值，<equation>\alpha</equation>是<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量.


<equation>\textcircled{1}</equation>若<equation>\lambda</equation>是<equation>A</equation>的特征值，则<equation>\lambda^{k}</equation>是<equation>A^{k}</equation>的特征值.

---


#### 11. 矩阵等价的充要条件

<equation>\textcircled{2}</equation>若<equation>\lambda \neq 0</equation>是<equation>A</equation>的特征值，则<equation>\lambda^{-1}</equation>是<equation>A^{-1}</equation>的特征值.

<equation>\textcircled{3}</equation>若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>是<equation>A</equation>的特征值，则

<equation>\lambda_{1} + \lambda_{2} + \dots +\lambda_{n} = a_{11} + a_{22} + \dots +a_{m}</equation>（A的迹），<equation>\lambda_{1}\lambda_{2}\dots \lambda_{n} = |\mathbf{A}|.</equation>

<equation>\textcircled{4}</equation><equation>\mathbf{A}</equation>与<equation>\mathbf{A}^{\mathrm{T}}</equation>有相同的特征值.

<equation>\textcircled{5}</equation>矩阵 A属于不同特征值的特征向量必线性无关.

<equation>\textcircled{6}</equation>实对称矩阵属于不同特征值的特征向量必正交.


A可逆<equation>\Leftrightarrow</equation><equation>|A| \neq 0 \Leftrightarrow A=P_{1} P_{2}\dots P_{i}</equation>，其中<equation>P_{i}</equation>（<equation>i=1</equation>2，...，l）为初等矩阵

<equation>\Leftrightarrow A\cong E</equation>（<equation>E</equation>为<equation>n</equation>阶单位矩阵）.


<equation>A\cong B\Leftrightarrow</equation>存在可逆矩阵<equation>P, Q</equation>使<equation>PAQ = B</equation>

<equation>\Leftrightarrow r (\mathbf {A}) = r (\mathbf {B}).</equation>

---


### 第三章 向量


#### 2. 线性组合与线性表出

n个数<equation>a_{1}, a_{2}, \dots , a_{n}</equation>组成一个有次序的数组，称为一个n维向量，用<equation>\alpha = (a_{1}, a_{2}, \dots , a_{n})</equation>（称为行向量）或<equation>\alpha = (a_{1}, a_{2}, \dots , a_{n})^{\mathrm{T}}</equation>（称为列向量）来表示.称<equation>a_{i}</equation>为第<equation>i</equation>个分量.若干个同维列向量（或同维行向量）组成的集合称为向量组.

(2) 向量的加法

<equation>\begin{array}{l} \boldsymbol {\alpha} + \boldsymbol {\beta} = \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) + \left(b _ {1}, b _ {2}, \dots , b _ {n}\right) \\ = \left(a _ {1} + b _ {1}, a _ {2} + b _ {2}, \dots , a _ {n} + b _ {n}\right). \\ \end{array}</equation>

(3) 数乘向量

<equation>k \alpha = k \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) = \left(k a _ {1}, k a _ {2}, \dots , k a _ {n}\right).</equation>


(1) 向量组的线性组合

有一组向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>及一组数<equation>k_{1},k_{2},\dots ,k_{s}</equation>，称

<equation>k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s}</equation>

---


#### 3. 向量组的等价

为向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>的一个线性组合.


若向量<equation>\beta</equation>可表示为向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>的一个线性组合，即有<equation>k_{1},k_{2},\dots ,k_{s}</equation>存在，使

<equation>\boldsymbol {\beta} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s}</equation>

成立，则称向量<equation>\beta</equation>可由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出（或线性表示）。否则称<equation>\beta</equation>不能由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出.

<equation>\textcircled{1}</equation>一个向量<equation>\beta</equation>能否由一个向量组<equation>\alpha_{1}, \alpha_{2}, \dots, \alpha_{s}</equation>线性表出，等价于以<equation>k_{1}, k_{2}, \dots, k_{s}</equation>为未知量的线性方程组<equation>\beta = k_{1}\alpha_{1} + k_{2}\alpha_{2} + \dots + k_{s}\alpha_{s}</equation>是有解还是无解.

<equation>\textcircled{2}</equation>若<equation>\boldsymbol{\beta}</equation>可由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出，其表现形式（即表出系数）是唯一的还是无穷多种形式，等价于线性方程组<equation>k_{1}\alpha_{1}+k_{2}\alpha_{2}+\dots +k_{s}\alpha_{s}=\boldsymbol{\beta}</equation>在有解时只有唯一解还是无穷多组解.


若向量组（I）<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>中每一个向量<equation>\alpha_{j}(j = 1,2,\dots ,s)</equation>均可由向量组（Ⅱ）<equation>\beta_{1},\beta_{2},\dots ,\beta_{i}</equation>线性表出，则称向量组（I）可由向量组（Ⅱ）线性表出.

若向量组（I）可由向量组（Ⅱ）线性表出，向量组（Ⅱ）也可由向量组（I）线性表出，则称向量组（I）与向量组（Ⅱ）为等价向量组，记作：（I）<equation>\cong</equation>（Ⅱ）.

---


#### 1. 线性相关性的定义

向量组的等价有以下性质：


任一个向量组（I）与自身必等价，即（I）<equation>\cong</equation>（I）。


若向量组（I）<equation>\cong</equation>（Ⅱ），则（Ⅱ）<equation>\cong</equation>（I）.


若向量组（I）<equation>\cong</equation>（Ⅱ），向量组（Ⅱ）<equation>\cong</equation>（Ⅲ），则（I）<equation>\cong</equation>（Ⅲ）.


<equation>\textcircled{1}</equation>现有 s个n维向量<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>，若存在着一组不全为零的数组<equation>k_{1},k_{2},\dots ,k_{s}</equation>，使

<equation>k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s} = \mathbf {0}</equation>

成立，则称向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r}</equation>是线性相关的向量组.

<equation>\textcircled{2}</equation>现有 s个n维向量<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>

<equation>k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s} = \mathbf {0}</equation>

若使

成立，只有

<equation>k _ {1} = 0, k _ {2} = 0, \dots , k _ {s} = 0,</equation>

则称向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>是线性无关的向量组.

---


#### 3. 一些重要的定理与结论

<equation>\textcircled{1}</equation>（判定定理1）<equation>s</equation>个<equation>n</equation>维向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性相关（或线性无关）的充要条件是对应的齐次线性方程组<equation>k_{1}\alpha_{1} + k_{2}\alpha_{2} + \dots +k_{s}\alpha_{s} = 0</equation>有非零解（或只有零解).

推论 n个n维向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关（或线性无关）的充要条件是行列式<equation>|A| = |\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>（或<equation>\neq 0</equation>）.

<equation>\textcircled{2}</equation>（判定定理2）向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{j}</equation>线性相关（或线性无关）的充要条件是其中至少有一个向量可由其余向量线性表出（或没有一个向量可由其余向量线性表出).


<equation>\textcircled{1}</equation>包含零向量的向量组必定线性相关.

<equation>\textcircled{2}</equation>包含两个相等向量的向量组必定线性相关.

<equation>\textcircled{3}</equation>若一个向量组线性相关，则加上任意多个向量后，新加向量组仍线性相关。（部分相关，全体必相关）

<equation>\textcircled{4}</equation>一个向量组线性无关，取出其中任何一部分也必线性无关.（全体无关，部分必无关）

<equation>\textcircled{5}</equation>任意 n+1个 n维向量必线性相关.（个数大于维数的向量组必线性相关）

<equation>\textcircled{6}</equation>一个向量组线性无关，则在相同位置处增加一个分量后得到的新向量组（可称为加长组）仍线性无关.

---


#### 2. 极大无关组的性质

<equation>\textcircled{7}</equation>一个向量组线性相关，则在相同位置处去掉一个分量后得到的新向量组（可称为缩短组）仍线性相关.

<equation>\textcircled{8}</equation>若<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性无关，而<equation>\beta ,\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性相关，则<equation>\beta</equation>必可由<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>唯一地线性表出.

<equation>\textcircled{9}</equation>设有向量组（I）<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>，向量组（Ⅱ）<equation>\beta_{1}</equation>，<equation>\beta_{2},\dots ,\beta_{r}</equation>中每个向量都可由向量组（I）线性表出，且<equation>t > s</equation>，则向量组（Ⅱ）必线性相关.

<equation>\textcircled{10}</equation>若<equation>\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \dots, \boldsymbol{\beta}_t</equation>可由<equation>\alpha_1, \alpha_2, \dots \alpha_s</equation>线性表出，且<equation>\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \dots, \boldsymbol{\beta}_t</equation>线性无关，则<equation>t \leqslant s</equation>。


若向量组（I）<equation>\alpha_{1},\alpha_{2},\dots,\alpha_{k}</equation>是向量组（Ⅱ）<equation>\alpha_{1},\alpha_{2},\dots,\alpha_{k}</equation>的一个部分组，且向量组（I）满足以下两个条件：<equation>\textcircled{1}</equation>向量组（I）是线性无关的；<equation>\textcircled{2}</equation>从向量组（Ⅱ）中任取一个向量加到向量组（I）中都线性相关，则称向量组（I）是向量组（Ⅱ）的一个极大线性无关组，简称为极大无关组.


<equation>\textcircled{1}</equation>一个向量组与它的任一个极大无关组之间可以互相线性表出（即等价）.

---


#### 1. 向量的内积

<equation>\textcircled{2}</equation>一个向量组的任两个极大无关组之间也等价.

<equation>\textcircled{3}</equation><equation>\textcircled{3}</equation>一个向量组的任两个极大无关组所包含向量的个数必相等.

<equation>\textcircled{4}</equation>设向量组<equation>\beta_{1},\beta_{2},\dots ,\beta_{r}</equation>可由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出，则<equation>r(\beta_{1},\beta_{2},\dots ,\beta_{r})\leqslant r(\alpha_{1},\alpha_{2},\dots ,\alpha_{s})</equation>

<equation>\textcircled{5}</equation>两个等价（即可以互相线性表出）的向量组，其秩必相等.


（三秩相等定理）矩阵<equation>\mathbf{A}</equation>的秩<equation>r(\mathbf{A})= \mathbf{A}</equation>的列秩<equation>= \mathbf{A}</equation>的行秩.


(1) 内积的定义

已知 n维实向量

<equation>\boldsymbol {\alpha} = \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) ^ {\mathrm {T}}, \boldsymbol {\beta} = \left(b _ {1}, b _ {2}, \dots , b _ {n}\right) ^ {\mathrm {T}},</equation>

称

<equation>(\boldsymbol {\alpha}, \boldsymbol {\beta}) = a _ {1} b _ {1} + a _ {2} b _ {2} + \dots + a _ {n} b _ {n} = \sum_ {i = 1} ^ {n} a _ {i} b _ {i} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta}</equation>

为向量<equation>\alpha, \beta</equation>的内积.

内积具有以下的性质：

<equation>\textcircled{1}</equation>对称性

<equation>(\alpha , \beta) = (\beta , \alpha).</equation>

---


#### (1)定义

<equation>\textcircled{2}</equation>线性性

<equation>\begin{array}{l} (\alpha + \beta , \gamma) = (\alpha , \gamma) + (\beta , \gamma), \\ (k \alpha , \beta) = k (\alpha , \beta). \\ \end{array}</equation>


对任意<equation>\alpha\in \mathbf{R}^{n}</equation>，均有（<equation>\alpha,\alpha) \geqslant 0</equation>，且

<equation>(\boldsymbol {\alpha}, \boldsymbol {\alpha}) = 0 \Leftrightarrow \boldsymbol {\alpha} = \mathbf {0}.</equation>


实数<equation>|\alpha| = \sqrt{(\alpha, \alpha)} = \sqrt{\sum_{i=1}^{n} a_i^2}</equation>称为向量<equation>\alpha</equation>的长度（或模）。若<equation>|\alpha| = 1</equation>，则称<equation>\alpha</equation>为单位向量。若<equation>\alpha</equation>不是单位向量，则<equation>\alpha</equation>方向上的单位向量<equation>\alpha_0 = \frac{1}{|\alpha|}\alpha</equation>。


非零向量<equation>\alpha</equation>与<equation>\beta</equation>的夹角的余弦为

<equation>\cos (\alpha , \beta) = \frac {(\alpha , \beta)}{| \alpha | \cdot | \beta |}.</equation>

若<equation>(\alpha ,\beta) = 0</equation>（即<equation>\cos (\alpha ,\beta) = 0</equation>或<equation>(\alpha ,\beta) = \frac{\pi}{2}</equation>），则称<equation>\alpha</equation>与<equation>\beta</equation>正交，记作<equation>\alpha \bot \beta</equation>


有<equation>s</equation>个<equation>n</equation>维向量：<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}(s\leqslant n)</equation>.若每一个向量都是非零向量，且每两个向量都正交，则称向量组

---


#### (2) 施密特正交化方法

<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>为一个正交向量组

正交向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots \boldsymbol{\alpha}_{s}</equation>用内积表示为：

<equation>(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = 0 (i, j = 1, 2, \dots s; i \neq j)</equation>且<equation>(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) \neq 0 (i = 1, 2, \dots , s)</equation>.


每个向量都是单位向量的正交向量组称为标准正交向量组（或规范正交向量组），即

<equation>\left(\boldsymbol {\alpha} _ {i}, \boldsymbol {\alpha} _ {j}\right) = \left\{ \begin{array}{l l} 0, & \text {当} i \neq j \text {时}, \\ 1, & \text {当} i = j \text {时} \end{array} \right. (i, j = 1, 2, \dots , s).</equation>


用施密特正交化方法可将任意一组线性无关的向量组改造成为标准正交向量组（先正交化再单位化）。若<equation>\alpha_{1}, \alpha_{2}, \dots, \alpha_{n}</equation>是一组线性无关的向量组，令

<equation>\begin{array}{l} \boldsymbol {\beta} _ {1} = \boldsymbol {\alpha} _ {1}, \\ \boldsymbol {\beta} _ {2} = - \frac {\left(\boldsymbol {\alpha} _ {2} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} + \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} = - \frac {\left(\boldsymbol {\alpha} _ {3} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\alpha} _ {3} , \boldsymbol {\beta} _ {2}\right)}{\left(\boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {2}\right)} \boldsymbol {\beta} _ {2} + \boldsymbol {\alpha} _ {3}, \dots , \\ \boldsymbol {\beta} _ {n} = \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {2}\right)}{\left(\boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {2}\right)} \boldsymbol {\beta} _ {2} - \dots - \\ \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {n - 1}\right)}{\left(\boldsymbol {\beta} _ {n - 1}, \boldsymbol {\beta} _ {n - 1}\right)} \boldsymbol {\beta} _ {n - 1} + \boldsymbol {\alpha} _ {n}, \\ \end{array}</equation>

则<equation>\beta_{1},\beta_{2},\dots ,\beta_{n}</equation>是一组两两正交的向量组.

---


#### (2) 子空间

再令

<equation>\gamma_{i} = \frac{\boldsymbol{\beta}_{i}}{|\boldsymbol{\beta}_{i}|}(i = 1,2,\dots,n)</equation>，其中<equation>|\boldsymbol{\beta}_{i}| = \sqrt{(\boldsymbol{\beta}_{i},\boldsymbol{\beta}_{i})}</equation>，则<equation>\gamma_{1},\gamma_{2},\dots,\gamma_{n}</equation>就是一组由<equation>\alpha_{1},\alpha_{2},\dots,\alpha_{n}</equation>改造成的标准正交向量组.


若<equation>n</equation>阶实矩阵<equation>A</equation>满足<equation>A A^{\mathrm{T}} = A^{\mathrm{T}} A = E</equation>，则称<equation>A</equation>为正交矩阵（即<equation>A^{\mathrm{T}} = A^{-1}</equation>）.

n阶矩阵<equation>A</equation>是正交矩阵的充要条件是：<equation>A</equation>的<equation>n</equation>个列（行）向量两两正交，且每个列（行）向量都是单位向量（即<equation>A</equation>的列（行）向量组为<equation>\mathbf{R}^n</equation>中的一组标准正交向量组).

正交矩阵的行列式不是1就是一1.两个正交矩阵的乘积仍是正交矩阵.


设<equation>V</equation>是<equation>n</equation>维向量的非空集合，且<equation>V</equation>对向量的加法与数乘这两种运算都封闭，则称<equation>V</equation>为向量空间.


设<equation>W</equation>是向量空间<equation>V</equation>的一个非空子集，且<equation>W</equation>中的向量对向量加法与数乘这两种运算也封闭，则称<equation>W</equation>为

---


#### （1）基变换与两组基间的过渡矩阵

V的一个子向量空间，简称为子空间


设<equation>V</equation>是向量空间，若<equation>V</equation>中有一组线性无关的向量组<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>，且<equation>V</equation>中任一个向量都可由<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>线性表出，则称<equation>V</equation>为<equation>n</equation>维的向量空间，记作<equation>V^{n}</equation>，又称<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>为<equation>V^{n}</equation>中的一组基.


设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>是<equation>V^{n}</equation>中的一组基，则对于任意<equation>\alpha \in V^{n},\alpha</equation>均可由基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>唯一地线性表出；

<equation>\boldsymbol {\alpha} = x _ {1} \boldsymbol {\varepsilon} _ {1} + x _ {2} \boldsymbol {\varepsilon} _ {2} + \dots + x _ {n} \boldsymbol {\varepsilon} _ {n},</equation>

称其表出系数<equation>x_{1}, x_{2}, \dots x_{n}</equation>是向量<equation>\alpha</equation>在基<equation>\varepsilon_{1}, \varepsilon_{2}, \dots, \varepsilon_{n}</equation>下的坐标. 坐标往往用列向量来表示：

<equation>\boldsymbol {X} = \left(x _ {1}, x _ {2}, \dots x _ {n}\right) ^ {\mathrm {T}},</equation>

则<equation>\pmb{\alpha} = (\pmb{\varepsilon}_1,\pmb{\varepsilon}_2,\dots ,\pmb{\varepsilon}_n)X.</equation>


设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>与<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>是<equation>n</equation>维向量空间<equation>\mathbf{R}^n</equation>中的两组基，且

<equation>\left\{ \begin{array}{l} \boldsymbol {\eta} _ {1} = a _ {1 1} \boldsymbol {\varepsilon} _ {1} + a _ {2 1} \boldsymbol {\varepsilon} _ {2} + \dots + a _ {n 1} \boldsymbol {\varepsilon} _ {n}, \\ \boldsymbol {\eta} _ {2} = a _ {1 2} \boldsymbol {\varepsilon} _ {1} + a _ {2 2} \boldsymbol {\varepsilon} _ {2} + \dots + a _ {n 2} \boldsymbol {\varepsilon} _ {n}, \\ \dots \\ \boldsymbol {\eta} _ {n} = a _ {1 n} \boldsymbol {\varepsilon} _ {1} + a _ {2 n} \boldsymbol {\varepsilon} _ {2} + \dots + a _ {m n} \boldsymbol {\varepsilon} _ {n}, \end{array} \right.</equation>

---


#### (2)坐标变换

此式称为由基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的基变换公式，称矩阵

<equation>A = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right]</equation>

为由旧基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到新基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的过渡矩阵.

过渡矩阵必是可逆矩阵，上面的基变换公式用矩阵及向量符号可表示为

<equation>\left(\eta_ {1}, \eta_ {2}, \dots , \eta_ {n}\right) = \left(\varepsilon_ {1}, \varepsilon_ {2}, \dots , \varepsilon_ {n}\right) A,</equation>

其中过渡矩阵<equation>A</equation>的第<equation>j</equation>列是<equation>\eta_{j}</equation>在基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>下的坐标列向量.


设<equation>\alpha</equation>是<equation>\mathbf{R}^n</equation>中的任一个向量，<equation>\alpha</equation>在基<equation>\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n</equation>下的坐标为<equation>X = (x_{1}, x_{2}, \dots, x_{n})^{\mathrm{T}}</equation>，在基<equation>\eta_1, \eta_2, \dots, \eta_n</equation>下的坐标为<equation>Y = (y_{1}, y_{2}, \dots, y_{n})^{\mathrm{T}}</equation>，则有

<equation>X = A Y \text {或} Y = A ^ {- 1} X.</equation>

此式即为坐标变换公式，式中的<equation>A</equation>即为基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的过渡矩阵.

---

(3) 两组标准正交基之间的过渡矩阵是正交矩阵

设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>是<equation>V^{n}</equation>中的一组基，且<equation>(\varepsilon_{i},\varepsilon_{i}) = 1</equation><equation>(\varepsilon_{i},\varepsilon_{j}) = 0(i,j = 1,2,\dots ,n;i\neq j)</equation>，则称<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>为<equation>V^{n}</equation>中的一组标准正交基（或规范正交基）。

设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>及<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>都是<equation>\mathbf{R}^n</equation>的标准正交基，且有<equation>(\eta_{1},\eta_{2},\dots ,\eta_{n}) = (\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n})A</equation>，则<equation>A</equation>必是一个正交矩阵.

---


### 第四章 线性方程组


#### 1. 一般表示式

(1) 非齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = b _ {1}, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = b _ {2}, \\ \dots \\ a _ {m 1} x _ {1} + a _ {m 2} x _ {2} + \dots + a _ {m n} x _ {n} = b _ {m}. \end{array} \right.</equation>

(2) 齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = 0, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = 0, \\ \dots \\ a _ {m 1} x _ {1} + a _ {m 2} x _ {2} + \dots + a _ {m n} x _ {n} = 0. \end{array} \right.</equation>

2.<equation>\sum</equation>记号表示式

(1) 非齐次线性方程组

<equation>\sum_ {j = 1} ^ {n} a _ {i j} x _ {j} = b _ {i} \quad (i = 1, 2, \dots , m).</equation>

(2) 齐次线性方程组

---


#### 1. 克拉默法则

<equation>\sum_ {j = 1} ^ {n} a _ {i j} x _ {j} = 0 \quad (i = 1, 2, \dots , m).</equation>


(1) 非齐次线性方程组

<equation>A X = b,</equation>

式中<equation>\mathbf{A}=(a_{ij})_{m\times n},\mathbf{X}=(x_{1},x_{2},\dots,x_{n})^{\mathrm{T}},\mathbf{b}=(b_{1},b_{2},\dots,</equation><equation>b_{m})^{\mathrm{T}}.</equation>

(2) 齐次线性方程组

<equation>A X = 0,</equation>

式中<equation>A, X</equation>同上，<equation>0 = (0,\dots ,0)^{\mathrm{T}}.</equation>


(1) 非齐次线性方程组

<equation>x _ {1} \boldsymbol {\alpha} _ {1} + x _ {2} \boldsymbol {\alpha} _ {2} + \dots + x _ {n} \boldsymbol {\alpha} _ {n} = \boldsymbol {b},</equation>

式中<equation>\boldsymbol{a}_{j} = (a_{1j}, a_{2j}, \dots , a_{mj})^{\mathrm{T}}</equation>（<equation>j=1,2,\dots,n )</equation>,<equation>\boldsymbol{b} = (b_{1},</equation><equation>b_{2},\dots,b_{m})^{\mathrm{T}}.</equation>


<equation>x _ {1} \boldsymbol {\alpha} _ {1} + x _ {2} \boldsymbol {\alpha} _ {2} + \dots + x _ {n} \boldsymbol {\alpha} _ {n} = 0,</equation>

式中<equation>\pmb{\alpha}_{j}</equation>同上，<equation>0 = (0,\dots ,0)^{\mathrm{T}}</equation>是一个<equation>m</equation>维的零向量.


<equation>\textcircled{1}</equation>若非齐次线性方程组

---

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = b _ {1}, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = b _ {2}, \\ \dots \\ a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {n n} x _ {n} = b _ {n} \end{array} \right.</equation>

的系数行列式<equation>D = |A| = \left| \begin{array}{c c c c} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n} \end{array} \right| \neq 0,</equation>

则方程组有唯一解：<equation>x_{j} = \frac{D_{j}}{D} = (j = 1,2,\dots ,n)</equation>，其中<equation>D_{j}</equation>是把<equation>D</equation>中第<equation>j</equation>列元素<equation>(a_{1j},a_{2j},\dots ,a_{m})^{\mathrm{T}}</equation>换成常数项<equation>(b_{1},</equation><equation>b_{2},\dots ,b_{n})^{\mathrm{T}}</equation>而得到的新行列式.

<equation>\textcircled{2}</equation>若已知齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = 0, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = 0, \\ \dots \\ a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {m} x _ {n} = 0 \end{array} \right.</equation>

的系数行列式<equation>D = |A| = \left| \begin{array}{c c c c} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{array} \right| \neq 0,</equation>

则该齐次线性方程组只有零解：<equation>x_{j} = 0(j = 1,2,\dots,n).</equation>

---


#### 2. 齐次线性方程组 $ AX=0 $的基础解系

推论 若已知上述齐次线性方程组有非零解，则其系数行列式<equation>D = 0.</equation>


对于<equation>AX = b</equation>（其中<equation>A</equation>为<equation>m \times n</equation>型矩阵）有解的充要条件是：增广矩阵<equation>\widetilde{A} = (A, b)</equation>的秩与系数矩阵<equation>A</equation>的秩相等，即<equation>r(A, b) = r(A)</equation>，且

<equation>\textcircled{1}</equation>当<equation>r (\widetilde{A})=r (A,b)=r (A)=n</equation>（未知量的个数）时，方程组有唯一解.

<equation>\textcircled{2}</equation>当<equation>r(\widetilde{A})=r(A,b)=r(A)<n</equation>（未知量的个数）时，方程组有无穷多个解.


对于<equation>AX = 0</equation>（其中<equation>A</equation>为<equation>m \times n</equation>矩阵），当<equation>r(A) = n</equation>（未知量的个数）时，方程组只有零解：<equation>X = 0</equation>；当<equation>r(A) < n</equation>时，方程组必有非零解（即有无穷多个解）。


<equation>\textcircled{1}</equation>若<equation>X_{1}, X_{2}</equation>都是<equation>AX = 0</equation>的解，则<equation>X_{1} + X_{2}</equation>也是<equation>AX = 0</equation>的解.

<equation>\textcircled{2}</equation>对于任意<equation>k \in \mathbf{R}</equation>，若<equation>X_{1}</equation>是<equation>AX = 0</equation>的解，则<equation>kX_{1}</equation>也都是<equation>AX = 0</equation>的解.


若<equation>\eta_{1}, \eta_{2}, \dots, \eta_{n}</equation>是齐次线性方程组<equation>AX = 0</equation>的一组

---


#### 2. 非齐次线性方程组 $AX = b$ 的解的结构

解（A为<equation>m\times n</equation>矩阵，<equation>r(A) < n )</equation>，且

<equation>\textcircled{1}</equation><equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\dots ,\boldsymbol{\eta}_{k}</equation>线性无关；

<equation>\textcircled{2}</equation><equation>AX = 0</equation>的任一个解都可由它线性表出，则称<equation>\eta_1</equation>，<equation>\eta_2</equation>，…，<equation>\eta_{i}</equation>为齐次线性方程组<equation>AX = 0</equation>的一个基础解系.


若<equation>A</equation>为<equation>m \times n</equation>矩阵，且<equation>r(A) < n</equation>，则其通解（即全部解）为：<equation>k_{1}\eta_{1} + k_{2}\eta_{2} + \dots + k_{n - r(A)}\eta_{n - r(A)}</equation>，其中<equation>\eta_{1},\eta_{2},\dots ,\eta_{n - r(A)}</equation>是<equation>AX = 0</equation>的一个基础解系，<equation>k_{1},k_{2},\dots ,k_{n - r(A)}</equation>为任意常数.


<equation>\textcircled{1}</equation>若<equation>X_{1}, X_{2}</equation>为非齐次线性方程组<equation>AX = b</equation>的两个解，则其差<equation>X_{1} - X_{2}</equation>必是导出组<equation>AX = 0</equation>的解.

<equation>\textcircled{2}</equation>若<equation>\eta_{1}</equation>是<equation>AX = b</equation>的任一个解，<equation>\eta_{1}</equation>是其导出组<equation>AX = 0</equation>的解，则<equation>\eta_{0} + \eta_{1}</equation>也是非齐次线性方程组<equation>AX = b</equation>的解.


当<equation>r(\mathbf{A},\mathbf{b}) = r(\mathbf{A}_{m\times n}) < n</equation>时，其通解（即全部解）为

<equation>\boldsymbol {\eta} _ {0} + k _ {1} \boldsymbol {\eta} _ {1} + k _ {2} \boldsymbol {\eta} _ {2} + \dots + k _ {n - r (A)} \boldsymbol {\eta} _ {n - r (A)},</equation>

其中<equation>\eta_0</equation>为<equation>AX = b</equation>的任一个特解，<equation>\eta_{1},\eta_{2},\dots ,\eta_{n - r(A)}</equation>为导出组<equation>AX = 0</equation>的基础解系，<equation>k_{1},k_{2},\dots ,k_{n - r(A)}</equation>为任意常数.

---


### 第五章 矩阵的特征值和特征向量


#### 2. 特征值与特征向量的性质

对<equation>n</equation>阶矩阵<equation>A</equation>，若存在一个数<equation>\lambda</equation>与一个非零的<equation>n</equation>维向量<equation>X</equation>，使<equation>AX = \lambda X</equation>成立，则称<equation>\lambda</equation>是<equation>A</equation>的一个特征值，称<equation>X</equation>为<equation>A</equation>的属于<equation>\lambda</equation>的特征向量.

称行列式

<equation>f _ {A} (\lambda) = | \lambda E - A |</equation>

为<equation>A</equation>的特征多项式，称

<equation>f _ {A} (\lambda) = | \lambda E - A | = 0</equation>

为<equation>A</equation>的特征方程，称<equation>\lambda E - A</equation>为<equation>A</equation>的特征矩阵.


设<equation>\lambda_{i}(i = 1,2,\dots ,n)</equation>为<equation>n</equation>阶矩阵<equation>A = (a_{ij})_{n\times n}</equation>的特征值，则有

<equation>\textcircled{1}</equation><equation>\sum_{i=1}^{n}\lambda_{i} = \sum_{i=1}^{n}a_{ii} (\sum_{i=1}^{n}a_{ii}</equation>称为 A 的迹，记为<equation>\operatorname{tr}(\mathbf{A}))</equation>,<equation>\prod_{i=1}^{n}\lambda_{i} = |\mathbf{A}|</equation>.

---


#### 3. 可以进一步延伸的公式

<equation>\textcircled{2}A</equation>的不同特征值的特征向量必线性无关，这个性质包含两层内容：

(a)若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>是A的两两不等的特征值，<equation>X_{1}</equation><equation>X_{2},\dots ,X_{s}</equation>是A的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>的特征向量，则向量组<equation>X_{1},X_{2},\dots ,X_{s}</equation>必线性无关.

(b)若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>是A的两两不等的特征值，<equation>X_{11},X_{12},\dots ,X_{1m_1};X_{21},X_{22},\dots ,X_{2m_2};\dots ;X_{s1},X_{s2},\dots ,</equation><equation>X_{s m}</equation>是A的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>的且各自线性无关的特征向量，则向量组：<equation>X_{11},X_{12},\dots ,X_{1m_1},X_{21},X_{22},\dots ,</equation><equation>X_{2m_2},\dots ,X_{s1},X_{s2},\dots ,X_{s m}</equation>必线性无关.


设<equation>X_{0}</equation>是<equation>A</equation>的属于特征值<equation>\lambda_{0}</equation>的特征向量，即<equation>AX_{0} = \lambda_{0}X_{0}</equation>，则以下公式也都成立：

<equation>\textcircled{1}</equation><equation>(k\mathbf{A} + t\mathbf{E})\mathbf{X}_0 = (k\lambda_0 + t)\mathbf{X}_0, k, t</equation>为常数.

<equation>\textcircled{2} A^{k} X_{0}=\lambda_{0}^{k} X_{0}.</equation>

<equation>\textcircled{3}</equation><equation>f(\mathbf{A})\mathbf{X}_0 = f(\lambda_0)\mathbf{X}_0</equation>，式中<equation>f(\mathbf{A})</equation>是<equation>\mathbf{A}</equation>的矩阵多项式，<equation>f(\lambda_0)</equation>是<equation>\lambda_0</equation>的同一多项式.

<equation>\textcircled{4}</equation>若<equation>\mathbf{A}</equation>可逆，则有<equation>\mathbf{A}^{-1}\mathbf{X}_0 = \frac{1}{\lambda_0}\mathbf{X}_0</equation>

<equation>\textcircled{5}</equation><equation>A^{*} X_{0} = \frac{|A|}{\lambda_{0}} X_{0}</equation>.

<equation>\textcircled{6}</equation><equation>(\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P})(\boldsymbol{P}^{-1}\boldsymbol{X}_0) = \lambda_0(\boldsymbol{P}^{-1}\boldsymbol{X}_0).</equation>

---


#### 2. 矩阵可对角化的有关定理

<equation>\textcircled{7}</equation><equation>\mathbf{A}^{\mathrm{T}}</equation>与 A有相同的特征值.

若<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>满足<equation>f(\mathbf{A}) = \mathbf{O}</equation>，则有<equation>f(\lambda) = 0.</equation>


对于<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>，若存在一个<equation>n</equation>阶可逆矩阵<equation>\mathbf{P}</equation>，使

<equation>P ^ {- 1} A P = \Lambda (\Lambda \text {为 对 角 矩 阵})</equation>

成立，则称<equation>A</equation>可相似对角化，简称<equation>A</equation>可对角化，否则就称<equation>A</equation>不可对角化.

若<equation>n</equation>阶矩阵<equation>A</equation>可以对角化，则对角矩阵<equation>A</equation>的<equation>n</equation>个主对角线元素必是<equation>A</equation>的<equation>n</equation>个特征值：<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>（包括重根），其相似变换矩阵<equation>P</equation>的<equation>n</equation>个列向量<equation>X_{1},X_{2},\dots</equation><equation>X_{n}</equation>是<equation>A</equation>的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>的特征向量，且<equation>X_{1},X_{2}</equation><equation>\dots ,X_{n}</equation>线性无关. 即有

<equation>P ^ {- 1} A P = A,</equation>

其中<equation>A = \left[ \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \ddots & \\ & & & \lambda_ {n} \end{array} \right], P = \left(X_{1}, X_{2}, \dots , X_{n}\right)</equation>为可逆

矩阵，且<equation>A X_{j}=\lambda_{j} X_{j} (j=1,2,\dots,n).</equation>


<equation>\textcircled{1}</equation><equation>n</equation>阶矩阵<equation>A</equation>可以对角化的充要条件是<equation>A</equation>有<equation>n</equation>个

---

线性无关的特征向量.

<equation>\textcircled{2}</equation>若<equation>n</equation>阶矩阵<equation>A</equation>有<equation>n</equation>个两两不等的特征值，则<equation>A</equation>必可对角化.

<equation>\textcircled{3}</equation>设<equation>\lambda_{i}</equation>是矩阵<equation>A</equation>的任一个特征值，其代数重数为<equation>n_{i}</equation>（即<equation>\lambda_{i}</equation>是<equation>n_{i}</equation>重特征值），其几何重数为<equation>m_{i}</equation>（即属于<equation>\lambda_{i}</equation>的线性无关的特征向量的最大个数，也是齐次线性方程组<equation>(\lambda_{i}E - A)X = 0</equation>的基础解系中的向量个数，<equation>m_{i} = n - r(\lambda_{i}E - A))</equation>，则恒有<equation>m_{i} \leqslant n_{i}</equation>.

<equation>\textcircled{4}</equation>设<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>的两两不等的特征值为<equation>\lambda_{1}, \lambda_{2}, \dots, \lambda_{s}(1 \leqslant s \leqslant n)</equation>，则矩阵<equation>\mathbf{A}</equation>可对角化的充要条件是对<equation>\mathbf{A}</equation>的每一个特征值<equation>\lambda_{i}</equation>，都有<equation>m_{i} = n_{i}(i = 1, 2, \dots, s)</equation>.

---


### 第六章 二次型


#### 1. 二次型的定义

<equation>n</equation>个变量<equation>x_{1}, x_{2}, \dots, x_{n}</equation>的一个二次齐次多项式

<equation>\begin{array}{l} f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \\ = a _ {1 1} x _ {1} ^ {2} + 2 a _ {1 2} x _ {1} x _ {2} + 2 a _ {1 3} x _ {1} x _ {3} + \dots + 2 a _ {1 n} x _ {1} x _ {n} \\ + a _ {2 2} x _ {2} ^ {2} + 2 a _ {2 3} x _ {2} x _ {3} + \dots + 2 a _ {2 n} x _ {2} x _ {n} \\ + a _ {3 3} x _ {3} ^ {2} + \dots + 2 a _ {3 n} x _ {3} x _ {n} \\ + \dots \\ + a _ {m} x _ {n} ^ {2} \\ \end{array}</equation>

称为一个关于<equation>x_{1}, x_{2}, \dots , x_{n}</equation>的二次型

2. 二次型的矩阵表示式

<equation>\text {设} \boldsymbol {X} = \left(x _ {1}, x _ {2}, \dots , x _ {n}\right), \boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right],</equation>

则

<equation>f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) = \boldsymbol {X} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {X},</equation>

---


#### 4. 惯性定理

称 A为二次型对应的矩阵.


(1) 实二次型的标准形

若

<equation>\begin{array}{l} f (X) = X ^ {\mathrm {T}} A X \xlongequal {X = C Y} Y ^ {\mathrm {T}} \left(C ^ {\mathrm {T}} A C\right) Y \\ = d _ {1} y _ {1} ^ {2} + d _ {2} y _ {2} ^ {2} + \dots + d _ {n} y _ {n} ^ {2} \\ = Y ^ {\mathrm {T}} \cdot \operatorname {d i a g} \left(d _ {1}, d _ {2}, \dots , d _ {n}\right) \cdot Y, \\ \end{array}</equation>

则称平方和

<equation>d _ {1} y _ {1} ^ {2} + d _ {2} y _ {2} ^ {2} + \dots + d _ {n} y _ {n} ^ {2}</equation>

为二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>的一个标准形.

任一个实二次型<equation>f ( X ) = X^{\mathrm{T}} A X</equation>经过适当的可逆线性替换<equation>X=C Y</equation>总可化成标准形（即平方和），即实对称矩阵总可与一个对角矩阵合同：

<equation>\mathbf {C} ^ {\mathrm {T}} \mathbf {A C} = \mathbf {B} = \operatorname {d i a g} \left(d _ {1}, d _ {2}, \dots , d _ {n}\right).</equation>

(2) 实二次型的规范形

形如

<equation>\begin{array}{l} f (X) = X ^ {\mathrm {T}} A X \xlongequal {X = D Z} z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {p} ^ {2} - z _ {p + 1} ^ {2} \\ - \dots - z _ {p + q} ^ {2} + 0 \cdot z _ {p + q + 1} ^ {2} + \dots + 0 \cdot z _ {n} ^ {2} \\ \end{array}</equation>

的标准形称为<equation>f(X)</equation>的规范形，其中<equation>p</equation>称为正惯性指数，<equation>q</equation>称为负惯性指数.


任意一个实系数的二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>总可经过一个适当的可逆线性替换化成规范形，其规范形是

---


#### 1. 正定二次型

唯一的，与所选的坐标变换无关，即正平方项个数<equation>p</equation>负平方项个数<equation>q</equation>由原二次型<equation>f(X) = X^{\mathrm{T}}AX</equation>唯一确定.用矩阵的语言来讲：实对称矩阵总可与对角阵

<equation>\operatorname {d i a g} (1, \dots , 1, - 1, \dots , - 1, 0, \dots , 0)</equation>

合同，且<equation>p + q = r(A)</equation>，其中<equation>p, q</equation>是不变的量.


任一个实二次型总可用配方的方法通过一个适当的可逆线性替换化为标准形.


设<equation>f ( X )=X^{\mathrm{T}} A X</equation>，因为A为实对称矩阵，由实对称矩阵必可通过正交变换化为对角阵A，其主对角线元素必为A的全部特征值，而正交变换（<equation>Q^{\mathrm{T}} A Q=Q^{-1} A Q=A</equation>）中包含了合同变换，因此当作变换<equation>X=Q Y</equation>后，二次型<equation>f ( X )</equation>即变为

<equation>\begin{array}{l} g (\mathbf {Y}) = \mathbf {Y} ^ {\mathrm {T}} \left(\mathbf {Q} ^ {\mathrm {T}} \mathbf {A} \mathbf {Q}\right) \mathbf {Y} = \mathbf {Y} ^ {\mathrm {T}} \mathbf {A} \mathbf {Y} \\ = \lambda_ {1} y _ {1} ^ {2} + \lambda_ {2} y _ {2} ^ {2} + \dots + \lambda_ {n} y _ {n} ^ {2}. \\ \end{array}</equation>

任一个实二次型<equation>f(X) = X^{\mathrm{T}}AX</equation>总可通过变量间的正交替换<equation>X = QY</equation>化为标准形（平方和），其平方项前的系数必是<equation>A</equation>的全部特征值.


设<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>是一个实二次型，若对于任意

---


#### 2. 二次型正定的判定

<equation>X_{0}\neq 0</equation>，<equation>f(\mathbf{X}_0) = \mathbf{X}_0^{\mathrm{T}}\mathbf{A}\mathbf{X}_0 > 0</equation>恒成立，则称

<equation>f (\boldsymbol {X}) = \boldsymbol {X} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {X}</equation>

为正定二次型，称对应矩阵<equation>A</equation>为正定矩阵.


(1) 判定正定性的充分必要条件

<equation>\textcircled{1}</equation>实二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>正定<equation>\Leftrightarrow</equation>正惯性指数<equation>p = n.</equation>

<equation>\textcircled{2}</equation>实二次型<equation>f ( X )=X^{\mathrm{T}} A X</equation>正定<equation>\Leftrightarrow A</equation>与单位矩阵合同，即存在可逆矩阵P，使<equation>P^{\mathrm{T}} A P=E</equation>成立.

<equation>\textcircled{3}</equation>实二次型<equation>f(X) = X^{\mathrm{T}}AX</equation>正定<equation>\Leftrightarrow</equation>存在可逆矩阵<equation>C</equation>，使<equation>A = C^{\mathrm{T}}C</equation>.

<equation>\textcircled{4}</equation>实二次型<equation>f ( \boldsymbol{X} )=\boldsymbol{X}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{X}</equation>正定<equation>\Leftrightarrow \boldsymbol{A}</equation>的特征值全大于0.

<equation>\textcircled{5}</equation>实二次型<equation>f ( \boldsymbol{X} )=\boldsymbol{X}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{X}</equation>正定<equation>\Leftrightarrow A</equation>的各阶顺序主子式全部大于0，即

<equation>\left| a _ {1 1} \right| > 0,</equation>

<equation>\left| \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| > 0,</equation>

<equation>\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| > 0,</equation>

---

<equation>\left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| > 0.</equation>

<equation>\textcircled{6}</equation>实二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>正定<equation>\Leftrightarrow \mathbf{A}</equation>与一个正定矩阵合同.

(2) 实对称矩阵 A正定的必要条件

实对称矩阵<equation>\mathbf{A}</equation>正定<equation>\Rightarrow |\mathbf{A}| > 0; a_{n} > 0</equation>（<equation>i=1,</equation>2,…,n).

---


#### 概率论与数理统计

第三部分

---


### 第一章 随机事件和概率


#### (4)相互独立

<equation>\textcircled{1}</equation>包含：若 B发生必然导致 A发生，称为 A包含 B，记作 A<equation>\supset</equation>B.

<equation>\textcircled{2}</equation>相等：若<equation>A\supset B</equation>且<equation>B\supset A</equation>，则称<equation>A=B.</equation>


若<equation>AB=\varnothing</equation>，则称A与B互不相容.


若<equation>AB = \varnothing</equation>且<equation>A\cup B = \varOmega</equation>，则称 A与B为对立事件，记为<equation>B = \overline{A}</equation>


<equation>\textcircled{1}</equation>若<equation>P(AB) = P(A)P(B)</equation>，则称 A与B相互独立.

<equation>\textcircled{2}</equation>若<equation>\left\{ \begin{array}{l} P (A B) = P (A) P (B), \\ P (B C) = P (B) P (C), \\ P (A C) = P (A) P (C), \\ P (A B C) = P (A) P (B) P (C) \end{array} \right\}</equation>称<equation>A, B, C</equation>相

---


#### 3. 事件运算的规律

互独立.

<equation>\textcircled{3}</equation>性质：<equation>A,B;\overline{A},B;A,\overline{B};\overline{A},\overline{B}</equation>中任一对相互独立，则其余各对相互独立.


(1) 和事件

A发生或者B发生，记为<equation>A\bigcup B.</equation>

(2) 积事件

A发生且B发生，记为AB.

(3) 差事件

A发生且B不发生，记为<equation>A - B = A\overline{B}.</equation>


(1) 交换律

<equation>A \bigcup B = B \bigcup A;</equation>

<equation>A B = B A.</equation>

(2) 结合律

<equation>(A \cup B) \cup C = A \cup (B \cup C);</equation>

<equation>(A B) C = A (B C).</equation>

(3) 分配律

<equation>(A \bigcup B) C = (A C) \bigcup (B C);</equation>

<equation>(A B) \cup C = (A \cup C) (B \cup C).</equation>

(4) 对偶律

<equation>\overline {{A \bigcup B}} = \overline {{A}} \overline {{B}};</equation>

<equation>\overline {{A B}} = \overline {{A}} \cup \overline {{B}}, \overline {{A}} = A.</equation>

---


#### (1)规范性

样本空间<equation>\varOmega</equation>在每次试验中都会发生，故称其为必然事件.


空集（<equation>\varnothing</equation>）在每次试验中都不会发生，故称其为不可能事件.


由单个样本点构成的单点集<equation>\{w\}</equation>称之为基本事件.


若<equation>AB = \varnothing</equation>，则称事件<equation>A</equation>与<equation>B</equation>为互不相容事件.


若<equation>A B=\varnothing</equation>，<equation>A \cup B=\Omega</equation>，则称事件 A与B为对立事件.


概率是从所有事件构成的集合到实数集的一个映射 P，它必须满足下列条件：


<equation>P (\Omega) = 1.</equation>

---


#### 2. 概率的基本性质

(2) 非负性

对任意事件 A，都有

<equation>P (A) \geqslant 0.</equation>

(3) 可列可加性

设<equation>A_{k}, k = 1,2, \dots</equation>为互不相容事件，则映射<equation>P</equation>满足

<equation>P \left(\bigcup_ {k = 1} ^ {\infty} A _ {k}\right) = \sum_ {k = 1} ^ {\infty} P \left(A _ {k}\right).</equation>


(1)<equation>P(\varnothing)=0.</equation>

(2) 有限可加性

设<equation>A_{k}, k = 1, 2, \dots , n</equation>为互不相容事件，则

<equation>P \left(\bigcup_ {k = 1} ^ {n} A _ {k}\right) = \sum_ {k = 1} ^ {n} P \left(A _ {k}\right).</equation>

(3) 对立事件的概率

<equation>P (\bar {A}) = 1 - P (A).</equation>

若事件<equation>A\subset B</equation>，则

(4) 单调性

<equation>P (A) \leqslant P (B).</equation>

(5) 加法公式

<equation>P (A \cup B) = P (A) + P (B) - P (A B).</equation>

(6) 减法公式

<equation>P (A - B) = P (A) - P (A B).</equation>

---


#### 4. 完备事件组

古典概型中，<equation>\varOmega</equation>包含样本点的个数有限，且每个基本事件的概率相等。即设<equation>\Omega = \{w_{1}, w_{2}, \dots, w_{n}\}</equation>，则有

<equation>P \left\{w _ {i} \right\} = P \left\{w _ {j} \right\} \quad (\text {任 意} i, j).</equation>

若<equation>A = \{w_{i1}, w_{i2}, \dots, w_{k}\}</equation>，则

<equation>P (A) = \frac {k}{n}.</equation>


设<equation>\Omega</equation>为一区域，其中的分布是均匀的，则

<equation>P (A) = \frac {m (A)}{m (\Omega)},</equation>

其中<equation>m(\cdot)</equation>为该区域的测度，如长度、面积、体积等.


设<equation>P ( A ) > 0</equation>，定义条件概率为

<equation>P (B | A) = \frac {P (A B)}{P (A)}.</equation>


设<equation>A_{k}, k=1,2,\dots</equation>为互不相容事件，且<equation>\bigcup_{k=1}^{A_{k}}A_{k}=\Omega</equation>，则称<equation>A_{k}, k=1,2,\dots</equation>为完备事件组（也可称之为样本空间的一个可列分割.若其中的事件个数为有限个，则此时分割称为有限分割).

---


#### 7. n重伯努利试验

设<equation>A_{k}, k=1,2,\dots</equation>为样本空间的一个完备事件组，则

<equation>P (B) = \sum_ {k = 1} ^ {\infty} P \left(A _ {k}\right) P \left(B \mid A _ {k}\right).</equation>


设<equation>A_{k}, k = 1,2,\dots</equation>为样本空间的一个完备事件组，则

<equation>P \left(A _ {i} \mid B\right) = \frac {P \left(A _ {i}\right) P \left(B \mid A _ {i}\right)}{\sum_ {k = 1} ^ {\infty} P \left(A _ {k}\right) P \left(B \mid A _ {k}\right)}</equation>


每次试验中只有事件<equation>A</equation>或<equation>\overline{A}</equation>发生，并对此试验独立地重复n次，则称此试验为n重伯努利试验.在n次独立试验中A恰好发生k次的概率

<equation>P _ {n} (k) = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} (k = 0, 1, 2, \dots , n).</equation>

---


### 第二章 一维随机变量及其分布


#### 1. 定义

设 X 为一随机变量，令

<equation>F (x) = P (X \leqslant x), x \in \mathbf {R},</equation>

称此函数为随机变量<equation>X</equation>的分布函数.


<equation>\textcircled{1}</equation>单调不减.

<equation>\textcircled{2}</equation>值域：<equation>[0,1],\lim F(x) = 1,\lim F(x) = 0.</equation>

<equation>\textcircled{3}</equation>在任意点右连续.

<equation>\textcircled{4}</equation>对任意 a<equation>\in</equation>R，有

<equation>P (X = a) = F (a) - F (a - 0),</equation>

其中<equation>F ( a - 0 )</equation>为<equation>F ( x )</equation>在a点的左极限


若随机变量<equation>X</equation>取有限个或可列多个不同的值，则称<equation>X</equation>为离散型随机变量.

---


#### 2. 概率密度的性质

(1) 分布律的定义

<equation>P \{X = x _ {k} \} = p _ {k}, k = 1, 2, \dots .</equation>

(2) 分布律的性质

<equation>p _ {k} \geqslant 0, k = 1, 2, \dots ; \sum_ {k = 1} ^ {\infty} p _ {k} = 1.</equation>


<equation>F (x) = \sum_ {x _ {i} \leqslant x} P \left\{x = x _ {k} \right\}.</equation>


如果对于随机变量<equation>X</equation>的分布函数<equation>F(x)</equation>，存在非负可积函数<equation>f(x)</equation>，使对任意<equation>x</equation>，有

<equation>F (x) = \int_ {- \infty} ^ {x} f (t) \mathrm {d} t,</equation>

则称<equation>X</equation>为连续型随机变量，其中函数<equation>f(x)</equation>称为<equation>X</equation>的概率密度函数，简称概率密度.


<equation>\textcircled{1} f ( x ) \geqslant 0;</equation>

<equation>\textcircled{2}</equation><equation>\int_{- \infty}^{+ \infty} f ( x ) \mathrm{d} x=1;</equation>

---


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