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
