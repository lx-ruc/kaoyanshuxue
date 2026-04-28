#### 函数的单调性、极值与最值

**2019年第2题 | 选择题 | 4分 | 答案: B**

2. 设函数 f(x) =<equation>\left\{\begin{array}{l l}{x|x|,}&{x\leqslant0,}\\ {x\ln x,}&{x>0,}\end{array} \right.</equation>则 x=0是 f(x)的（    ）

A. 可导点，极值点 B. 不可导点，极值点 C. 可导点，非极值点 D. 不可导点，非极值点

答案: B

**解析:**解 由于 x≤0时，<equation>|x|=-x</equation>，故<equation>f(x)=\left\{\begin{array}{ll}-x^{2},&x\leqslant 0,\\ x\ln x,&x>0.\end{array} \right.</equation>由 f(x）的定义可知，<equation>f(0)=0.</equation>分别计算 f(x)在 x=0处的左、右导数.<equation>f _ {-} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {-}} \frac {- x ^ {2} - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {-}} (- x) = 0,</equation><equation>f _ {+} ^ {\prime} (0) = \lim _ {x \rightarrow 0 ^ {+}} \frac {x \ln x - 0}{x - 0} = \lim _ {x \rightarrow 0 ^ {+}} \ln x = - \infty .</equation>于是，<equation>f ( x )</equation>在<equation>x=0</equation>处的右导数不存在，从而<equation>x=0</equation>是<equation>f ( x )</equation>的不可导点.

由于当<equation>x\leqslant 0</equation>时，<equation>f(x) = -x^{2}</equation>，故在0的任意左侧去心邻域内，<equation>f(x) < 0</equation>.又因为当<equation>0 < x < 1</equation>时，<equation>\ln x < 0</equation>，所以在（0,1）内，<equation>f(x) < 0</equation>.于是，存在<equation>x = 0</equation>的一个去心邻域<equation>(-1,0)\cup (0,1)</equation>，使得在该邻域内<equation>f(x) < f(0) = 0</equation>.根据极值点的定义，<equation>x = 0</equation>是<equation>f(x)</equation>的极大值点.

因此，应选B.

---

**2017年第2题 | 选择题 | 4分 | 答案: C**

2. 设函数 f(x)可导，且 f(x)f'(x)>0，则（    ）

A. f(1)>f(-1) B. f(1)<f(-1) C.<equation>|f(1)|>|f(-1)|</equation>D.<equation>|f(1)|<|f(-1)|</equation>

答案: C

**解析:**解（法一）令<equation>F ( x )=f^{2} ( x ).</equation>由题设知，<equation>F^{\prime}(x)=2 f(x) f^{\prime}(x)>0</equation>，故<equation>f^{2}(x)</equation>单调增加，于是<equation>f^{2}(1)>f^{2}(-1)</equation>即<equation>|f(1)|>|f(-1)|</equation>应选C.

（法二）由于<equation>f ( x ) f^{\prime} ( x ) > 0</equation>，即恒大于零，故<equation>f ( x )</equation>恒大于零或<equation>f ( x )</equation>恒小于零（否则由<equation>f ( x )</equation>的连续性可知<equation>f ( x )</equation>存在零点，从而<equation>f ( x ) f^{\prime} ( x )</equation>不恒大于零).

若<equation>f ( x ) > 0</equation>，则<equation>f^{\prime}(x) > 0</equation>，故<equation>f ( x )</equation>单调增加. 因此<equation>f ( 1 ) > f (- 1 ) > 0.</equation>若<equation>f(x) < 0</equation>，则<equation>f^{\prime}(x) < 0</equation>，故<equation>f(x)</equation>单调减少．因此<equation>f(1) < f(-1) < 0</equation>综上所述，<equation>|f(1)| > |f(-1)|</equation>应选C.

（法三）排除法.

取<equation>f(x) = \mathrm{e}^{x}</equation>，则<equation>f(x)</equation>满足<equation>f(x)f^{\prime}(x) = \mathrm{e}^{x}\cdot \mathrm{e}^{x} > 0</equation>，且<equation>f (1) > f (- 1) > 0, \quad | f (1) | > | f (- 1) |,</equation>故可以排除选项B、D.

取<equation>f ( x )=-\mathrm{e}^{x}</equation>，则<equation>f ( x )</equation>满足<equation>f ( x ) f^{\prime} ( x )=(-\mathrm{e}^{x})\cdot(-\mathrm{e}^{x})>0</equation>，且<equation>f ( 1 ) < f ( - 1 ) < 0</equation>，故可以排除选项A.

因此，应选C.

---

**2017年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数 y(x)由方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>确定，求 y(x）的极值.

**答案:**## 极大值为<equation>y ( 1 ) = 1</equation>，极小值为<equation>y (- 1 ) = 0.</equation>

**解析:**解 对方程两端关于 x求导，得<equation>3 x ^ {2} + 3 y ^ {2} y ^ {\prime} - 3 + 3 y ^ {\prime} = 0.</equation>整理得<equation>\left(y ^ {2} + 1\right) y ^ {\prime} = 1 - x ^ {2}.</equation>由于<equation>y^{2} + 1 > 0</equation>，故<equation>y(x)</equation>的全部驻点为<equation>x = 1</equation>和<equation>x = -1</equation>将 x=1代入方程<equation>x^{3}+y^{3}-3 x+3 y-2=0</equation>，得<equation>y^{3}+3 y-4=0</equation>. 通过观察发现 y=1是该方程的一个根.由于<equation>\frac{\mathrm{d}\left(y^{3}+3 y-4\right)}{\mathrm{d} y}=3 y^{2}+3>0</equation>，故<equation>y^{3}+3 y-4</equation>关于 y单调增加. y=1是<equation>y^{3}+3 y-4=0</equation>的唯

将 x=-1代入方程<equation>x^{3}+y^{3}-3x+3y-2=0</equation>，得<equation>y^{3}+3y=0</equation>，即<equation>y(y^{2}+3)=0. y=0</equation>是该方程的唯一实根，<equation>y(-1)=0.</equation>下面用两种方法来判断驻点的极值点类型.

（法一）对（1）式两端关于<equation>x</equation>求导，得<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} + 2 y \left(y ^ {\prime}\right) ^ {2} = - 2 x.</equation>利用（2）式计算驻点<equation>x = \pm 1</equation>处的二阶导数.

由于在驻点处<equation>y^{\prime} = 0</equation>，故当<equation>x = \pm 1</equation>时，<equation>\left(y ^ {2} + 1\right) y ^ {\prime \prime} = - 2 x.</equation>当 x=1时，(3)式化为<equation>2 y^{\prime \prime}(1)=-2,y^{\prime \prime}(1)=-1<0</equation>；当 x=-1时，(3)式化为<equation>y^{\prime \prime}(-1)=2>0.</equation>因此，<equation>y(1)=1</equation>为极大值，<equation>y(-1)=0</equation>为极小值.

（法二）由（1）式可得<equation>y^{\prime} = \frac{1 - x^{2}}{y^{2} + 1}</equation>.注意到<equation>y^{2} + 1</equation>恒大于零，故<equation>y^{\prime}(x)</equation>与<equation>y(x)</equation>的性质如下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>y&#x27;(x)</td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td></tr><tr><td>y(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td></tr></table>

因此，<equation>y ( 1 ) = 1</equation>为极大值，<equation>y (- 1 ) = 0</equation>为极小值.

---

**2014年第16题 | 解答题 | 10分**

16. (本题满分10分）

设函数<equation>y=f(x)</equation>由方程<equation>y^{3}+xy^{2}+x^{2}y+6=0</equation>确定，求 f(x)的极值.

**答案:**16) 极小值为 f（1）=-2.

**解析:**方程<equation>y^{3}+xy^{2}+x^{2}y+6=0</equation>两端关于 x求导，得<equation>3 y ^ {2} y ^ {\prime} + y ^ {2} + 2 x y y ^ {\prime} + 2 x y + x ^ {2} y ^ {\prime} = 0.</equation>令<equation>y^{\prime}=0</equation>，则有<equation>y^{2}+2 x y=0</equation>，从而<equation>y=0</equation>或<equation>y=-2 x</equation>.将<equation>y=0</equation>代入原方程得到6=0，矛盾，故<equation>y\neq</equation>0，从而<equation>y=-2 x</equation>.将其代入到原方程得到<equation>6 x^{3}=6</equation>，解得<equation>x=1, y=-2</equation>，于是<equation>f(1)=-2, f^{\prime}(1)=0.</equation>对（1）式两端关于 x求导，整理得到<equation>6 y \left(y ^ {\prime}\right) ^ {2} + 3 y ^ {2} y ^ {\prime \prime} + 4 y y ^ {\prime} + 2 x \left(y ^ {\prime}\right) ^ {2} + 2 x y y ^ {\prime \prime} + 2 y + 4 x y ^ {\prime} + x ^ {2} y ^ {\prime \prime} = 0.</equation>将 x=1，f（1）=-2及<equation>f^{\prime} ( 1 )=0</equation>代入上式，得到<equation>f^{\prime\prime} ( 1 )=\frac{4}{9}>0.</equation>因此 x=1是 f(x)的极小值点，极小值为 f（1）=-2.

---

**2010年第16题 | 解答题 | 10分**

16. (本题满分10分)

求函数<equation>f ( x )=\int_{1}^{x^{2}}(x^{2}-t)\mathrm{e}^{-t^{2}}\mathrm{d} t</equation>的单调区间与极值.

**答案:**(16)<equation>f ( x )</equation>的单调增加区间为<equation>(-1,0)</equation>和<equation>( 1,+\infty)</equation>；<equation>f ( x )</equation>的单调减少区间为<equation>(-\infty,-1)</equation>和(0,1)；<equation>f ( x )</equation>的极小值为<equation>f (\pm1)=0</equation>，极大值为<equation>f ( 0 )=\frac{1}{2}\left( 1-\frac{1} {\mathrm{e}} \right).</equation>

**解析:**解 先求<equation>f^{\prime}(x).</equation>由于在变限积分<equation>\int_{1}^{x^{2}}(x^{2}-t)\mathrm{e}^{-t^{2}}\mathrm{d}t</equation>中，x不是积分变量，故可以把它提到积分号外.<equation>f (x) = \int_ {1} ^ {x ^ {2}} \left(x ^ {2} - t\right) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = x ^ {2} \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - \int_ {1} ^ {x ^ {2}} t \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation>根据变限积分函数的求导公式以及求导的乘法法则，<equation>f ^ {\prime} (x) = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t + 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} - 2 x ^ {3} \mathrm {e} ^ {- x ^ {4}} = 2 x \int_ {1} ^ {x ^ {2}} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t.</equation><equation>f^{\prime}(x) = 0</equation>当且仅当<equation>x = 0</equation>或<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故当且仅当<equation>x^{2} = 1</equation>，即<equation>x = \pm 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t = 0.</equation>因此，<equation>x = 0,\pm 1</equation>为<equation>f(x)</equation>的驻点.

对<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t</equation>来说，当<equation>x^{2} < 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t < 0</equation>；当<equation>x^{2} > 1</equation>时，<equation>\int_{1}^{x^{2}}\mathrm{e}^{-t^{2}}\mathrm{d}t > 0</equation>因此有下表.

<table border="1"><tr><td>x</td><td>(-∞,-1)</td><td>-1</td><td>(-1,0)</td><td>0</td><td>(0,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td><equation>f^{\prime}(x)</equation></td><td>-</td><td>0</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td></tr><tr><td>f(x)</td><td>单调减少</td><td>极小值</td><td>单调增加</td><td>极大值</td><td>单调减少</td><td>极小值</td><td>单调增加</td></tr></table>

由此可知，<equation>f ( x )</equation>的单调增加区间为<equation>(-1,0)</equation>和<equation>( 1,+\infty)</equation>；<equation>f ( x )</equation>的单调减少区间为<equation>(-\infty,-1)</equation>和(0，1)；<equation>f (-1)</equation>和f(1)为<equation>f ( x )</equation>的极小值，<equation>f (- 1) = f (1) = \int_ {1} ^ {1} (1 - t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = 0;</equation>f（0）为f（x）的极大值，<equation>f (0) = \int_ {1} ^ {0} (- t) \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t = \frac {1}{2} \left(1 - \frac {1}{\mathrm {e}}\right).</equation>

---


