---


#### 无穷小量的比较


**2020年第1题 | 选择题 | 4分 | 答案: D**

1. 当<equation>x \to 0^{+}</equation>时，下列无穷小量中最高阶的是（    )

A.<equation>\int_{0}^{x} \left( \mathrm{e}^{t^{2}}-1 \right) \mathrm{d} t</equation>B.<equation>\int_{0}^{x} \ln(1+\sqrt{t^{3}}) \mathrm{d} t</equation>C.<equation>\int_{0}^{\sin x} \sin t^{2} \mathrm{d} t</equation>D.<equation>\int_{0}^{1-\cos x} \sqrt{\sin^{3} t} \mathrm{d} t</equation>

答案: D

**解析:**解 由于求一次导，无穷小量的阶数降低1，且选项A、B的积分上、下限相同，故比较这两项的无穷小量的阶的大小，可以转化为比较它们的被积函数的阶。又因为<equation>t\to 0^{+}</equation>时，<equation>\mathrm{e}^{t^{2}}-1\sim t^{2},</equation><equation>\ln(1+\sqrt{t^{3}})\sim t^{\frac{3}{2}}</equation>，所以<equation>\int_{0}^{x}\left(\mathrm{e}^{t^{2}}-1\right)\mathrm{d}t</equation>与<equation>x^{3}</equation>同阶，比<equation>\int_{0}^{x}\ln(1+\sqrt{t^{3}})\mathrm{d}t</equation>高阶.

比较<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {\sin x} \sin t ^ {2} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2} \cdot \cos x}{3 x ^ {2}} &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin (\sin x) ^ {2}}{x ^ {2}} \xlongequal {\text {s i n} u \sim u} \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \frac {(\sin x) ^ {2}}{x ^ {2}} \\ &= \frac {1}{3} \lim _ {x \rightarrow 0 ^ {+}} \left(\frac {\sin x}{x}\right) ^ {2} \xlongequal {\sin x \sim x} \frac {1}{3}. \end{aligned}</equation>于是，<equation>\int_{0}^{\sin x}\sin t^{2}\mathrm{d}t</equation>也与<equation>x^{3}</equation>同阶.

比较<equation>\int_{0}^{1-\cos x}\sqrt{\sin^{3}t}\mathrm{d}t</equation>与<equation>x^{3}</equation>的阶.<equation>\begin{aligned} \lim _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {1 - \cos x} \sqrt {\sin^ {3} t} \mathrm {d} t}{x ^ {3}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sqrt {\sin^ {3} (1 - \cos x)} \sin x}{3 x ^ {2}} \xlongequal {\text {s i n} x \sim x} \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{3 x} \\ &= \lim _ {x \rightarrow 0 ^ {+}} \frac {\sin^ {\frac {3}{2}} (1 - \cos x)}{(1 - \cos x) ^ {\frac {3}{2}}} \cdot \frac {(1 - \cos x) ^ {\frac {3}{2}}}{3 x} \\ \frac {1 - \cos x \sim \frac {x ^ {2}}{2}}{} \lim _ {x \rightarrow 0 ^ {+}} \left[ \frac {\sin (1 - \cos x)}{1 - \cos x} \right] ^ {\frac {3}{2}} \cdot \frac {\left(\frac {x ^ {2}}{2}\right) ^ {\frac {3}{2}}}{3 x} \\ &= 1 \times 0 = 0. \end{aligned}</equation>因此，<equation>\int_0^{1 - \cos x}\sqrt{\sin^3t}\mathrm{d}t</equation>比<equation>x^{3}</equation>高阶，从而比选项A、B、C中的无穷小量均高阶.应选D.

---


#### 函数的连续性


**2017年第1题 | 选择题 | 4分 | 答案: A**

1. 若函数 f(x)<equation>\left\{\begin{array}{l l}{\frac{1-\cos \sqrt{x}}{ax},}&{x>0,}\\ {b,}&{x\leqslant 0}\end{array}\right.</equation>在 x=0处连续，则（    )

A.<equation>a b=\frac{1}{2}</equation>B.<equation>a b=-\frac{1}{2}</equation>C.<equation>a b=0</equation>D.<equation>a b=2</equation>

答案: A

**解析:**解<equation>f(x)</equation>是分段函数. 代入<equation>f(x)</equation>在<equation>(-\infty ,0]</equation>和<equation>(0, + \infty)</equation>上的表达式, 分别计算<equation>\lim_{x\to 0^{-}}f(x)</equation>,<equation>\lim_{x\to 0^{+}}f(x)</equation>.<equation>\lim _ {x \rightarrow 0 ^ {-}} f (x) = f (0) = b,</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} f (x) = \lim _ {x \rightarrow 0 ^ {+}} \frac {1 - \cos \sqrt {x}}{a x} \frac {1 - \cos \sqrt {x} \sim \frac {1}{2} (\sqrt {x}) ^ {2}}{\underline {{=}}} \lim _ {x \rightarrow 0 ^ {+}} \frac {\frac {x}{2}}{a x} = \frac {1}{2 a}.</equation>因此，<equation>b=\frac{1}{2a}</equation>即<equation>ab=\frac{1}{2}</equation>应选A.

---


### 多元函数微分学

#### 方向导数和梯度


**2025年第13题 | 填空题 | 5分**
13. 已知函数<equation>u ( x,y,z)= x y^{2} z^{3}</equation>，向量<equation>\boldsymbol{n}=(2,2,-1)</equation>，则<equation>\left. \frac{\partial u}{\partial \boldsymbol{n}} \right|_{(1,1,1)}=</equation>___
**答案: **1.
**解析: **的方向余弦为<equation>\cos \alpha = \cos \beta = \frac {2}{\sqrt {2 ^ {2} + 2 ^ {2} + (- 1) ^ {2}}} = \frac {2}{3}, \cos \gamma = \frac {- 1}{\sqrt {2 ^ {2} + 2 ^ {2} + (- 1) ^ {2}}} = - \frac {1}{3}.</equation>计算<equation>\frac{\partial u}{\partial x},\frac{\partial u}{\partial y},\frac{\partial u}{\partial z}</equation>得，<equation>\frac {\partial u}{\partial x} = y ^ {2} z ^ {3}, \quad \frac {\partial u}{\partial y} = 2 x y z ^ {3}, \quad \frac {\partial u}{\partial z} = 3 x y ^ {2} z ^ {2}.</equation>因此，在点（1,1,1）处沿方向<equation>n = (2,2, - 1)</equation>的方向导数为<equation>\left. \frac {\partial u}{\partial n} \right| _ {(1, 1, 1)} = 1 \times \frac {2}{3} + 2 \times \frac {2}{3} + 3 \times \left(- \frac {1}{3}\right) = 1.</equation>

---

**2022年第11题 | 填空题 | 5分**
11. 函数<equation>f(x,y)=x^{2}+2y^{2}</equation>在点 (0,1) 处的最大方向导数为 ___
**解析: **解 由于<equation>\mathbf{g r a d} f(x,y)=(2x,4y),</equation>故 f(x,y)在点（0,1）处的梯度为（0,4）.又因为函数在一点处的最大方向导数等于该点处的梯度的模，所以 f(x,y)在点（0,1）处的最大方向导数为4.

---

**2019年第16题 | 解答题 | 10分**
16. (本题满分10分)

设 a,b为实数，函数<equation>z=2+a x^{2}+b y^{2}</equation>在点（3,4）处的方向导数中，沿方向 l=-3i-4j的方向导数最大，最大值为10.

I. 求 a,b;

II. 求曲面<equation>z = 2 + ax^{2} + by^{2}(z\geqslant 0)</equation>的面积.
**答案: **（ I ）<equation>a=-1,b=-1;</equation>（ II ）<equation>\frac{1 3 \pi}{3}.</equation>
**解析: **解（I）计算函数<equation>z=2+ax^{2}+by^{2}</equation>在点（3，4）处的梯度.<equation>\operatorname {g r a d} z (x, y) \mid_ {(3, 4)} = \left(z _ {x} ^ {\prime}, z _ {y} ^ {\prime}\right) \mid_ {(3, 4)} = \left(2 a x, 2 b y\right) \mid_ {(3, 4)} = (6 a, 8 b).</equation>由于函数沿方向<equation>l=-3 i-4 j</equation>的方向导数最大，最大值为10，故<equation>6 a i+8 b j</equation>与<equation>-3 i-4 j</equation>同向，且<equation>\sqrt{(6 a)^{2}+(8 b)^{2}}=10.</equation>由<equation>6 a i+8 b j</equation>与<equation>- 3 i-4 j</equation>同向可得<equation>\frac{6 a}{-3}=\frac{8 b}{-4}>0</equation>，从而<equation>a=b<0</equation>.代入<equation>\sqrt{(6 a)^{2}+(8 b)^{2}}=1 0</equation>可得<equation>a=b=-1.</equation>（Ⅱ）由第（I）问可知曲面<equation>\varSigma</equation>为<equation>z=2-x^{2}-y^{2}(z\geqslant0)</equation>，由第一类曲面积分的几何意义可知其面积等于<equation>\iint\limits_{\Sigma}\mathrm{d}S.</equation><equation>z _ {x} ^ {\prime} = - 2 x, z _ {y} ^ {\prime} = - 2 y, \mathrm {d} S = \sqrt {1 + 4 x ^ {2} + 4 y ^ {2}} \mathrm {d} x \mathrm {d} y.</equation>令<equation>z = 0</equation>，可得<equation>\Sigma</equation>在<equation>xOy</equation>面的投影区域为<equation>D_{xy} = \{(x,y)|x^2 + y^2\leqslant 2\}</equation><equation>\begin{aligned} \iint_ {\Sigma} \mathrm {d} S &= \iint_ {D _ {x y}} \sqrt {1 + \left(z _ {x} ^ {\prime}\right) ^ {2} + \left(z _ {y} ^ {\prime}\right) ^ {2}} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {x y}} \sqrt {1 + 4 x ^ {2} + 4 y ^ {2}} \mathrm {d} x \mathrm {d} y \\ \xlongequal {\text {极 坐 标}} \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 r ^ {2}} \cdot r \mathrm {d} r &= 2 \pi \cdot \frac {1}{8} \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 r ^ {2}} \mathrm {d} \left(1 + 4 r ^ {2}\right) \\ &= \frac {\pi}{4} \cdot \frac {2}{3} \left(1 + 4 r ^ {2}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {\sqrt {2}} = \frac {\pi}{4} \times \frac {2}{3} \times (2 7 - 1) = \frac {1 3 \pi}{3}. \end{aligned}</equation>

---

**2017年第3题 | 选择题 | 4分 | 答案: D**
3. 函数<equation>f(x,y,z)=x^{2} y+z^{2}</equation>在点（1，2，0）处沿向量 n =（1，2，2）的方向导数为（    )

A. 12 B. 6 C. 4 D. 2
答案: D
**解析: **由方向导数的计算公式知，<equation>\begin{aligned} \left. \frac {\partial f}{\partial n} \right| _ {(1, 2, 0)} &= \operatorname {g r a d} f (1, 2, 0) \cdot e _ {n} = \left(\frac {\partial f}{\partial x}, \frac {\partial f}{\partial y}, \frac {\partial f}{\partial z}\right) \Big | _ {(1, 2, 0)} \cdot \frac {n}{\| n \|} \\ &= \left(2 x y, x ^ {2}, 2 z\right) \mid_ {(1, 2, 0)} \cdot \frac {1}{3} n = (4, 1, 0) \cdot \left(\frac {1}{3}, \frac {2}{3}, \frac {2}{3}\right) \\ &= \frac {4}{3} + \frac {2}{3} = 2. \end{aligned}</equation>因此，应选D.

---

**2012年第11题 | 填空题 | 4分**
11. grad<equation>\left(x y+\frac{z}{y}\right)\bigg|_{(2,1,1)}=</equation>___
**答案: **## i+j+k.
**解析: **解 令<equation>f ( x,y,z)= x y+\frac{z}{y}</equation>，则<equation>\left(f_{x}^{\prime},f_{y}^{\prime},f_{z}^{\prime}\right)\big|_{(2,1,1)}=\left(y,x-\frac{z}{y^{2}},\frac{1}{y}\right)\big|_{(2,1,1)}=(1,1,1)</equation>，从而<equation>\operatorname{grad}\left(x y+\frac{z}{y}\right)\big|_{(2,1,1)}=i+j+k.</equation>

---


#### 偏导数的概念与计算


**2024年第12题 | 填空题 | 5分**
12. 设函数 f(u,v)具有2阶连续偏导数，且<equation>\mathrm{d} f|_{(1,1)}=3 \mathrm{d} u+4 \mathrm{d} v</equation>. 令 y=f（<equation>\cos x,1+x^{2}</equation>），则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___.
**答案: **```latex
5
```

**解析:**解 由全微分的定义以及<equation>\mathrm{d}f|_{(1,1)}=3\mathrm{d}u+4\mathrm{d}v</equation>可知，<equation>f_{1}^{\prime}(1,1)=3,f_{2}^{\prime}(1,1)=4.</equation>根据链式法则，<equation>\begin{aligned} \frac {\mathrm {d} y}{\mathrm {d} x} &= f _ {1} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot (- \sin x) + f _ {2} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot 2 x, \\ \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} &= f _ {1 1} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot (- \sin x) ^ {2} + f _ {1 2} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot 2 x \cdot (- \sin x) \\ + f _ {1} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot (- \cos x) + f _ {2 1} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot 2 x \cdot (- \sin x) + f _ {2 2} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot (2 x) ^ {2} \\ + f _ {2} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot 2. \end{aligned}</equation>将<equation>x=0</equation>代入<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}</equation>的表达式可得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = - f _ {1} ^ {\prime} (1, 1) + 2 f _ {2} ^ {\prime} (1, 1) = - 3 + 2 \times 4 = 5.</equation>

---

**2022年第2题 | 选择题 | 5分 | 答案: B**

2. 设函数<equation>z=xyf\left(\frac{y}{x}\right)</equation>，其中 f(u)可导，若<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=y^{2}(\ln y-\ln x)</equation>，则（    )

A.<equation>f(1)=\frac{1}{2},f^{\prime}(1)=0</equation>B.<equation>f(1)=0,f^{\prime}(1)=\frac{1}{2}</equation>C.<equation>f(1)=\frac{1}{2},f^{\prime}(1)=1</equation>D.<equation>f(1)=0,f^{\prime}(1)=1</equation>

答案: B

**解析:**解分别求<equation>\frac{\partial z}{\partial x}</equation>和<equation>\frac{\partial z}{\partial y}</equation>利用链式法则，<equation>\frac {\partial z}{\partial x} = y f \left(\frac {y}{x}\right) + x y f ^ {\prime} \left(\frac {y}{x}\right) \cdot \left(- \frac {y}{x ^ {2}}\right) = y f \left(\frac {y}{x}\right) - \frac {y ^ {2}}{x} f ^ {\prime} \left(\frac {y}{x}\right),</equation><equation>\frac {\partial z}{\partial y} = x f \left(\frac {y}{x}\right) + x y f ^ {\prime} \left(\frac {y}{x}\right) \cdot \frac {1}{x} = x f \left(\frac {y}{x}\right) + y f ^ {\prime} \left(\frac {y}{x}\right).</equation>于是，<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=2xyf\left(\frac{y}{x}\right).</equation>与<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=y^{2}(\ln y-\ln x)=y^{2}\ln \frac{y}{x}</equation>比较可得，<equation>f\left(\frac{y}{x}\right)=\frac{y}{2x}\ln \frac{y}{x}.</equation>从而，<equation>f(u)=\frac{1}{2} u \ln u,</equation><equation>f^{\prime}(u)=\frac{1}{2}(\ln u+1).</equation>因此，<equation>f ( 1 ) = 0</equation><equation>f^{\prime}(1)=\frac{1}{2}</equation>应选B.

---

**2020年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x,y)=\int_{0}^{xy}\mathrm{e}^{xt^{2}}\mathrm{d}t</equation>，则<equation>\left.\frac{\partial^{2}f}{\partial x\partial y}\right|_{(1,1)}=</equation>___

**答案:**## 4e.

**解析:**解（法一）注意到 f(x,y)的二阶偏导数连续，故可以交换求导次序.先对 y求偏导，再对 x求偏导.

根据变限积分求导公式，<equation>\frac {\partial f}{\partial y} = \mathrm {e} ^ {x (x y) ^ {2}} \cdot x = x \mathrm {e} ^ {x ^ {3} y ^ {2}},</equation><equation>\frac {\partial^ {2} f}{\partial y \partial x} = \mathrm {e} ^ {x ^ {3} y ^ {2}} + x \cdot \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot 3 x ^ {2} y ^ {2} = \left(3 x ^ {3} y ^ {2} + 1\right) \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation>代入<equation>x = 1,y = 1</equation>，可得<equation>\frac{\partial^2f}{\partial x\partial y}\bigg|_{(1,1)} = \frac{\partial^2f}{\partial y\partial x}\bigg|_{(1,1)} = 4\mathrm{e}.</equation>（法二）若直接对<equation>x</equation>求偏导，则需先对变限积分换元，将<equation>x</equation>移出积分号.令<equation>\sqrt{x} t = u</equation>，则<equation>\mathrm{d}t = \frac{\mathrm{d}u}{\sqrt{x}}.</equation><equation>\int_ {0} ^ {x y} \mathrm {e} ^ {x t ^ {2}} \mathrm {d} t \xlongequal {\sqrt {x} t = u} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \frac {\mathrm {e} ^ {u ^ {2}}}{\sqrt {x}} \mathrm {d} u = \frac {1}{\sqrt {x}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t.</equation>依次计算<equation>\frac{\partial f}{\partial x}, \frac{\partial^2 f}{\partial x \partial y}</equation>.<equation>\frac {\partial f}{\partial x} = - \frac {1}{2} x ^ {- \frac {3}{2}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t + \frac {1}{\sqrt {x}} \cdot \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot \frac {3}{2} \sqrt {x} y = - \frac {1}{2} x ^ {- \frac {3}{2}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t + \frac {3}{2} y \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation><equation>\frac {\partial^ {2} f}{\partial x \partial y} = - \frac {1}{2} x ^ {- \frac {3}{2}} \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot x ^ {\frac {3}{2}} + \frac {3}{2} \mathrm {e} ^ {x ^ {3} y ^ {2}} + 3 x ^ {3} y ^ {2} \mathrm {e} ^ {x ^ {3} y ^ {2}} = \left(3 x ^ {3} y ^ {2} + 1\right) \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation>代入<equation>x = 1,y = 1</equation>，可得<equation>\frac{\partial^2f}{\partial x\partial y}\bigg|_{(1,1)} = 4\mathrm{e}.</equation>

---

**2019年第9题 | 填空题 | 4分**

9. 设函数 f(u)可导，<equation>z=f(\sin y-\sin x)+xy</equation>，则

**答案:**<equation>\frac {y}{\cos x} + \frac {x}{\cos y}.</equation>

**解析:**解分别计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = f ^ {\prime} (\sin y - \sin x) \cdot (- \cos x) + y, \quad \frac {\partial z}{\partial y} = f ^ {\prime} (\sin y - \sin x) \cdot \cos y + x.</equation>代入<equation>\frac{1}{\cos x}\cdot \frac{\partial z}{\partial x} +\frac{1}{\cos y}\cdot \frac{\partial z}{\partial y}</equation>可得，<equation>\begin{aligned} \frac {1}{\cos x} \cdot \frac {\partial z}{\partial x} + \frac {1}{\cos y} \cdot \frac {\partial z}{\partial y} &= - f ^ {\prime} (\sin y - \sin x) + \frac {y}{\cos x} + f ^ {\prime} (\sin y - \sin x) + \frac {x}{\cos y} \\ &= \frac {y}{\cos x} + \frac {x}{\cos y}. \end{aligned}</equation>

---

**2017年第15题 | 解答题 | 10分**

15. (本题满分10分）

设函数<equation>f ( u,v )</equation>具有2阶连续偏导数，<equation>y=f(\mathrm{e}^{x},\cos x)</equation>，求<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=0},\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}.</equation>

**答案:**<equation>\frac{\mathrm{d} y}{\mathrm{d} x}\bigg|_{x=0}=f_{1}^{\prime}(1,1),\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\bigg|_{x=0}=f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)-f_{2}^{\prime}(1,1).</equation>

**解析:**解分别记 f（u,v）关于第一个变量、第二个变量的偏导数为<equation>f_{1}^{\prime}, f_{2}^{\prime}. f_{1}^{\prime}, f_{2}^{\prime}</equation>具有与f相同的复合结构根据链式法则，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f _ {1} ^ {\prime} \frac {\mathrm {d} \left(\mathrm {e} ^ {x}\right)}{\mathrm {d} x} + f _ {2} ^ {\prime} \frac {\mathrm {d} (\cos x)}{\mathrm {d} x} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} - f _ {2} ^ {\prime} \sin x.</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) - 0 = f _ {1} ^ {\prime} (1, 1).</equation>对（1）式两端关于 x求导，得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} + \mathrm {e} ^ {x} \left(f _ {1 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {1 2} ^ {\prime \prime} \sin x\right) - f _ {2} ^ {\prime} \cos x - \sin x \left(f _ {2 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {2 2} ^ {\prime \prime} \sin x\right).</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) - f _ {2} ^ {\prime} (1, 1).</equation>

---

**2011年第11题 | 填空题 | 4分**

11. 设函数 F(x,y)<equation>= \int_{0}^{x y}\frac{\sin t}{1+t^{2}}\mathrm{d}t</equation>，则<equation>\left.\frac{\partial^{2}F}{\partial x^{2}}\right|_{x=0,y=2}</equation> =___

**解析:**因此，<equation>\frac{\partial^{2}F}{\partial x^{2}}\bigg|_{x=0 \atop y=2}=4.</equation>解（法一）令<equation>f ( u )=\int_{0}^{u} \frac{\sin t}{1+t^{2}} \mathrm{d} t</equation>，则<equation>f^{\prime}(u)=\frac{\sin u}{1+u^{2}}</equation>，且<equation>F(x,y)=f(xy)</equation>.于是<equation>\frac{\partial F(x,y)}{\partial x}=f^{\prime}(xy)\cdot \frac{\partial(xy)}{\partial x}=\frac{\sin(xy)}{1+x^{2}y^{2}}\cdot y,</equation><equation>\frac{\partial^{2}F(x,y)}{\partial x^{2}}=y\cdot \frac{y\cos(xy)\cdot(1+x^{2}y^{2})-\sin(xy)\cdot 2xy^{2}}{(1+x^{2}y^{2})^{2}}.</equation>因此，<equation>\left. \frac{\partial^{2}F}{\partial x^{2}} \right|_{x=0, y=2}=4.</equation>（法二）先代值再求导.

由于<equation>F ( x, 2 ) = \int_{0}^{2 x} \frac{\sin t}{1 + t^{2}} \mathrm{d} t</equation>，故<equation>\left. \frac {\partial F}{\partial x} \right| _ {y = 2} = 2 \cdot \frac {\sin (2 x)}{1 + 4 x ^ {2}}, \quad \left. \frac {\partial^ {2} F}{\partial x ^ {2}} \right| _ {y = 2} = 2 \cdot \frac {2 \cos (2 x) \cdot \left(1 + 4 x ^ {2}\right) - \sin (2 x) \cdot 8 x}{\left(1 + 4 x ^ {2}\right) ^ {2}}.</equation>

---

**2011年第16题 | 解答题 | 10分**

16. (本题满分9分)

设函数 z = f(xy, yg(x))，其中函数 f具有二阶连续偏导数，函数 g(x)可导，且在 x=1处取得极值 g(1)=1.

求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{x=1}</equation>y=1.

**解析:**由链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial [ y g (x) ]}{\partial x} = y f _ {1} ^ {\prime} + y g ^ {\prime} (x) f _ {2} ^ {\prime}, \\ \frac {\partial^ {2} z}{\partial x \partial y} = \frac {\partial \left[ y \left(f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime}\right) \right]}{\partial y} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left\{f _ {1 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} + g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} \right\} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left[ x f _ {1 1} ^ {\prime \prime} + g (x) f _ {1 2} ^ {\prime \prime} + x g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} + g (x) g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \right]. \\ \end{array}</equation>由<equation>g ( x )</equation>可导且在<equation>x=1</equation>处取得极值<equation>g ( 1 )=1</equation>知，<equation>g^{\prime}(1)=0.</equation>将<equation>x=1, y=1, g ( 1 )=1,</equation><equation>g^{\prime}(1)=0</equation>代入<equation>\frac{\partial^{2} z}{\partial x \partial y}</equation>，得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {x = 1 \atop y = 1} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) + f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2010年第2题 | 选择题 | 4分 | 答案: B**

2. 设函数 z=z(x,y)由方程<equation>F\left( \frac{y}{x},\frac{z}{x} \right)=0</equation>确定，其中 F为可微函数，且<equation>F_{2}^{\prime}\neq0</equation>，则<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=</equation>(    )

A. x B. z C. -x D. -z

答案: B

**解析:**解 对方程<equation>F\left(\frac{y}{x},\frac{z}{x}\right)=0</equation>两端同时关于x，y求偏导数，可得<equation>- \frac {y}{x ^ {2}} F _ {1} ^ {\prime} + \left(- \frac {z}{x ^ {2}} + \frac {1}{x} \cdot \frac {\partial z}{\partial x}\right) F _ {2} ^ {\prime} = 0, \quad \frac {F _ {1} ^ {\prime}}{x} + \frac {F _ {2} ^ {\prime}}{x} \cdot \frac {\partial z}{\partial y} = 0.</equation>由上面两个方程解得，<equation>\frac {\partial z}{\partial x} = \frac {\frac {y}{x} F _ {1} ^ {\prime} + \frac {z}{x} F _ {2} ^ {\prime}}{F _ {2} ^ {\prime}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}}.</equation>因此，<equation>x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = \frac {y F _ {1} ^ {\prime} + z F _ {2} ^ {\prime} - y F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}} = z.</equation>应选B.

---

**2009年第9题 | 填空题 | 4分**

9. 设函数 f(u,v)具有二阶连续偏导数，z=f(x,xy)，则<equation>\frac{\partial^{2} z}{\partial x \partial y}=</equation>___

**答案:**<equation>x f_{12}^{\prime \prime}+f_{2}^{\prime}+ x y f_{22}^{\prime \prime}.</equation>

**解析:**由二元复合函数求导的链式法则知<equation>\begin{aligned} \frac {\partial z}{\partial x} &= f ^ {\prime} _ {1} (x, x y) + y f ^ {\prime} _ {2} (x, x y), \\ \frac {\partial^ {2} z}{\partial x \partial y} &= x f _ {1 2} ^ {\prime \prime} (x, x y) + f _ {2} ^ {\prime} (x, x y) + x y f _ {2 2} ^ {\prime \prime} (x, x y). \end{aligned}</equation>

---


#### 多元函数的极值问题


**2024年第18题 | 解答题 | 12分**

8. (本题满分12分)

已知函数<equation>f ( x, y )=x^{3}+y^{3}-( x+y )^{2}+3</equation>，设 T是曲面<equation>z=f(x,y)</equation>在点（1，1，1）处的切平面，D为T与坐标平面所围成的有界区域在 xOy面上的投影.

I. 求 T的方程；

II. 求 f(x,y)在 D上的最大值和最小值.

**答案:**(1)<equation>\varGamma</equation>的方程为<equation>x+y+z=3</equation>(2) 最大值<equation>f(3,0)=f(0,3)=21</equation>，最小值为<equation>f\left(\frac{4}{3},\frac{4}{3}\right)=\frac{17}{27}.</equation>

**解析:**解（I）记<equation>F ( x,y,z) = z - f ( x,y),</equation>，则<equation>F_{x}^{\prime}(x,y,z) = -3x^{2} + 2(x + y),\quad F_{y}^{\prime}(x,y,z) = -3y^{2} + 2(x + y),\quad F_{z}^{\prime}(x,y,z) = 1.</equation>代入<equation>x=1,y=1,z=1</equation>，可得<equation>F_{x}^{\prime}(1,1,1)=1, F_{y}^{\prime}(1,1,1)=1, F_{z}^{\prime}(1,1,1)=1.</equation>于是，曲面<equation>F(x,y,z)</equation><equation>= 0</equation>（即<equation>z = f(x,y)</equation>）在点（1,1,1）处的切平面T的点法式方程为<equation>(x - 1) + (y - 1) + (z - 1) = 0</equation>，即<equation>x + y + z = 3.</equation>（Ⅱ）T与坐标平面所围有界区域在 xOy面上的投影 D = {（x,y）| x+y≤3,x≥0,y≥0} .先求区域 D内部的驻点.

解<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=3x^{2}-2(x+y)=0,\\ f_{y}^{\prime}(x,y)=3y^{2}-2(x+y)=0,\end{array} \right.</equation>两式相减并整理可得<equation>x^{2}-y^{2}=0</equation>，解得 x=y或 x=-y. 由于 x≥0,y≥0，故在区域内部不可能有 x=-y.将 x=y代入<equation>3x^{2}-2(x+y)=0</equation>可得<equation>3x^{2}-4x</equation>=0，解得 x<equation>=\frac{4}{3}</equation>（舍去 x=0）.进一步可得驻点坐标为<equation>\left(\frac{4}{3},\frac{4}{3}\right).</equation>计算可得<equation>f \left(\frac {4}{3}, \frac {4}{3}\right) = 2 \cdot \left(\frac {4}{3}\right) ^ {3} - \left(\frac {8}{3}\right) ^ {2} + 3 = \frac {1 7}{2 7}.</equation>下面求边界上的最值.

（i）在边界<equation>y=0,0\leqslant x\leqslant 3</equation>上，<equation>f(x,y)=x^{3}-x^{2}+3.</equation>记<equation>\varphi(x)=x^{3}-x^{2}+3</equation>，则<equation>\varphi^{\prime}(x)=3x^{2}-2x=x(3x-2),x=\frac{2}{3}</equation>是<equation>\varphi(x)</equation>在（0,3）内的驻点，<equation>\varphi\left(\frac{2}{3}\right)=\left(\frac{2}{3}\right)^{3}-\left(\frac{2}{3}\right)^{2}+3=\frac{77}{27}.</equation>在端点 x=0和x=3处，<equation>\varphi(0)=3, \varphi(3)=21.</equation>（ii）在边界<equation>x=0,0\leqslant y\leqslant 3</equation>上，<equation>f(x,y)=y^{3}-y^{2}+3.</equation>最值情况与（i）相同.

（iii）在边界<equation>x + y = 3,0\leqslant x\leqslant 3</equation>上，<equation>f(x,y) = x^{3} + (3 - x)^{3} - 3^{2} + 3.</equation>记<equation>\psi(x)=x^{3}+(3-x)^{3}-6</equation>，则<equation>\psi^{\prime}(x)=3x^{2}-3(3-x)^{2}=18x-27=9(2x-3),x=\frac{3}{2}</equation>是<equation>\psi(x)</equation>在（0,3）内的驻点，<equation>\psi\left(\frac{3}{2}\right)=2\left(\frac{3}{2}\right)^{3}-6=\frac{3}{4}.</equation>在端点 x=0和x=3处，<equation>\psi(0)=21, \psi(3)=21.</equation>比较可得，<equation>f ( 3, 0 ) = f ( 0, 3 ) = 2 1</equation>是<equation>f ( x, y )</equation>在区域D上的最大值，<equation>f \left( \frac{4}{3}, \frac{4}{3} \right) = \frac{1 7}{2 7}</equation>是<equation>f ( x, y )</equation>在区域D上的最小值.

---

**2023年第18题 | 解答题 | 12分**

18. (本题满分12分)

求函数<equation>f ( x,y)=(y-x^{2})(y-x^{3})</equation>的极值.

**答案:**f(x,y)有极小值，极小值为<equation>f\left(\frac{2}{3},\frac{10}{27}\right)=-\frac{4}{729}.</equation>

**解析:**解<equation>\textcircled{1}</equation>计算 f(x,y)的驻点.<equation>\begin{aligned} f _ {x} ^ {\prime} (x, y) &= - 2 x \left(y - x ^ {3}\right) - 3 x ^ {2} \left(y - x ^ {2}\right) = 2 x ^ {4} - 2 x y + 3 x ^ {4} - 3 x ^ {2} y = 5 x ^ {4} - 3 x ^ {2} y - 2 x y \\ &= x \left(5 x ^ {3} - 3 x y - 2 y\right), \end{aligned}</equation><equation>f _ {y} ^ {\prime} (x, y) = y - x ^ {3} + y - x ^ {2} = 2 y - x ^ {3} - x ^ {2}.</equation>令<equation>\left\{\begin{array}{l l}x(5x^{3}-3xy-2y)=0,\\ 2y-x^{3}-x^{2}=0.\end{array} \right.</equation>由<equation>2y-x^{3}-x^{2}=0</equation>可得<equation>y=\frac{x^{2}(x+1)}{2}</equation>将<equation>y=\frac{x^{2}(x+1)}{2}</equation>代入<equation>x(5x^{3}-3xy-2y)=0</equation>可得<equation>x\left[5x^{3}-\frac{3x^{3}(x+1)}{2}-x^{2}(x+1)\right]=0.</equation>整理可得<equation>x^{3}(3x^{2}-5x+2)=</equation>0，即<equation>x^{3}(x-1)(3x-2)=0.</equation>解得<equation>x=0,x=1</equation>或<equation>x=\frac{2}{3}.</equation>由此可得f(x,y)的全部驻点为（0，0）， (1,1），<equation>\left(\frac{2}{3},\frac{10}{27}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = 5 x ^ {3} - 3 x y - 2 y + x \left(1 5 x ^ {2} - 3 y\right) = 2 0 x ^ {3} - 6 x y - 2 y = 2 \left(1 0 x ^ {3} - 3 x y - y\right),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = x (- 3 x - 2) = - 3 x ^ {2} - 2 x,</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = 2.</equation><equation>\textcircled{3}</equation>计算<equation>AC-B^{2}.</equation>（i）对点（0,0），<equation>A=f_{xx}^{\prime \prime}(0,0)=0,B=f_{xy}^{\prime \prime}(0,0)=0,C=f_{yy}^{\prime \prime}(0,0)=2,AC-B^{2}=0.</equation>我们无法由二元函数极值存在的充分条件判断该点是否为极值点.

由<equation>f ( x,y )</equation>的表达式可知，<equation>f ( 0,0 )=0.</equation>取<equation>y=2 x^{2}</equation>，当x为充分小的正数时，<equation>f (x, y) = \left(2 x ^ {2} - x ^ {2}\right) \left(2 x ^ {2} - x ^ {3}\right) = x ^ {4} (2 - x) > 0.</equation>取<equation>y=2 x^{3}</equation>，当x为充分小的正数时，<equation>f (x, y) = \left(2 x ^ {3} - x ^ {2}\right) \left(2 x ^ {3} - x ^ {3}\right) = x ^ {5} (2 x - 1) < 0.</equation>因此，不论在点（0，0）的多么小的邻域内，均既有<equation>f ( x,y)>0</equation>的点，也有<equation>f ( x,y)<0</equation>的点.根据极值点的定义，点（0，0）不是<equation>f ( x,y)</equation>的极值点.

（ii）对点（1，1），<equation>A=f_{xx}^{\prime \prime}(1,1)=1 2, B=f_{xy}^{\prime \prime}(1,1)=-5, C=f_{yy}^{\prime \prime}(1,1)=2, A C-B^{2}=-1<</equation>0.由二元函数极值存在的充分条件可知，点（1，1）不是<equation>f(x,y)</equation>的极值点.

（iii）对点<equation>\left(\frac{2}{3},\frac{10}{27}\right),A=f_{xx}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=\frac{100}{27},B=f_{xy}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=-\frac{8}{3},C=f_{yy}^{\prime \prime}\left(\frac{2}{3},\frac{10}{27}\right)=2,</equation><equation>AC-B^{2}=\frac{8}{27}>0</equation>，且 A > 0.由二元函数极值存在的充分条件可知，点<equation>\left(\frac{2}{3},\frac{10}{27}\right)</equation>是 f(x,y)的极小值点.极小值为<equation>f \left(\frac {2}{3}, \frac {1 0}{2 7}\right) = \left(\frac {1 0}{2 7} - \frac {4}{9}\right) \times \left(\frac {1 0}{2 7} - \frac {8}{2 7}\right) = - \frac {4}{7 2 9}.</equation>

---

**2022年第13题 | 填空题 | 5分**

13. 当<equation>x \geqslant 0, y \geqslant 0</equation>时，<equation>x^{2}+y^{2} \leqslant k \mathrm{e}^{x+y}</equation>恒成立，则<equation>k</equation>的取值范围是 ___

**答案:**[<equation>4 \mathrm{e}^{-2},+\infty)</equation>.

**解析:**解不等式<equation>x^{2}+y^{2}\leqslant k \mathrm{e}^{x+y}</equation>等价于<equation>\left(x^{2}+y^{2}\right)\mathrm{e}^{-(x+y)}\leqslant k.</equation>记<equation>f(x,y) = (x^{2} + y^{2})\mathrm{e}^{-(x + y)}, D = \{(x,y) \mid x \geqslant 0, y \geqslant 0\}</equation>.

计算 f(x,y)在 D 内的驻点.<equation>f _ {x} ^ {\prime} (x, y) = 2 x \mathrm {e} ^ {- (x + y)} - \left(x ^ {2} + y ^ {2}\right) \mathrm {e} ^ {- (x + y)} = \left(2 x - x ^ {2} - y ^ {2}\right) \mathrm {e} ^ {- (x + y)},</equation><equation>f _ {y} ^ {\prime} (x, y) = 2 y \mathrm {e} ^ {- (x + y)} - \left(x ^ {2} + y ^ {2}\right) \mathrm {e} ^ {- (x + y)} = \left(2 y - x ^ {2} - y ^ {2}\right) \mathrm {e} ^ {- (x + y)}.</equation>解<equation>\left\{ \begin{array}{l} 2x - x^2 - y^2 = 0, \\ 2y - x^2 - y^2 = 0. \end{array} \right.</equation>两式相减得<equation>x = y</equation>，将<equation>x = y</equation>代入<equation>2x - x^2 - y^2 = 0</equation>可得<equation>2x - 2x^2 = 0</equation>，从而<equation>x = 0</equation>或<equation>x = 1.</equation><equation>\left\{ \begin{array}{l} x = 0, \\ y = 0 \end{array} \right.</equation>和<equation>\left\{ \begin{array}{l} x = 1, \\ y = 1 \end{array} \right.</equation>为该方程组的两组解.由于所求为区域D内部的驻点，故舍去点(0,0).点(1,1)为<equation>f(x,y)</equation>在区域D内部的唯一驻点.<equation>f(1,1) = 2\mathrm{e}^{-2}.</equation>下面计算<equation>f(x,y)</equation>在区域<equation>D</equation>的边界<equation>x = 0</equation>与<equation>y = 0</equation>上的最大值.

当<equation>x = 0</equation>时，<equation>f(0,y) = y^{2}\mathrm{e}^{-y}</equation>.记<equation>f_{1}(y) = y^{2}\mathrm{e}^{-y}</equation>，则<equation>f_{1}^{\prime}(y) = (2y - y^{2})\mathrm{e}^{-y}</equation>.解<equation>2y - y^{2} = 0</equation>得<equation>y = 0</equation>或<equation>y = 2</equation>.当<equation>0 < y < 2</equation>时，<equation>f_{1}^{\prime}(y) > 0</equation>，<equation>f_{1}(y)</equation>单调增加，当<equation>y > 2</equation>时，<equation>f_{1}^{\prime}(y) < 0</equation>，<equation>f_{1}(y)</equation>单调减少.于是，<equation>f(0,2) = 4\mathrm{e}^{-2}</equation>为<equation>f(x,y)</equation>在边界<equation>x = 0</equation>上的最大值.

同理可得，<equation>f ( 2, 0 ) = 4 \mathrm{e}^{-2}</equation>为<equation>f ( x,y )</equation>在边界<equation>y=0</equation>上的最大值.

比较<equation>f ( 1,1), f ( 0,2), f ( 2,0)</equation>可得，<equation>f ( 0,2)=f ( 2,0)=4 \mathrm{e}^{-2}</equation>为<equation>f ( x,y)</equation>在区域D上的最大值综上所述，<equation>k</equation>的取值范围为<equation>[ 4 \mathrm{e}^{-2},+\infty).</equation>

---

**2021年第19题 | 解答题 | 12分**

19. (本题满分12分)

已知曲线 C：<equation>\left\{ \begin{array}{l l} x^{2}+2 y^{2}-z=6, \\ 4 x+2 y+z=3 0, \end{array} \right.</equation>求 C上的点到 xOy坐标面距离的最大值.

**答案:**## 最大值为66.

**解析:**解设目标函数为<equation>f ( x,y,z) = z^{2}.</equation>记<equation>\varphi ( x,y,z) = x^{2}+2 y^{2}-z-6,\psi ( x,y,z) = 4 x+2 y+z-3 0</equation>则约束条件为<equation>\varphi ( x,y,z) = 0,\psi ( x,y,z) = 0.</equation>建立拉格朗日函数<equation>L (x, y, z, \lambda , \mu) = z ^ {2} + \lambda \left(x ^ {2} + 2 y ^ {2} - z - 6\right) + \mu \left(4 x + 2 y + z - 3 0\right).</equation>对拉格朗日函数的各个变量分别求偏导，并令其为零，可得如下方程组.<equation>\left[ L _ {x} ^ {\prime} (x, y, z, \lambda , \mu) \right] = 2 \lambda x + 4 \mu = 0,</equation><equation>L _ {y} ^ {\prime} (x, y, z, \lambda , \mu) = 4 \lambda y + 2 \mu = 0,</equation><equation>L _ {z} ^ {\prime} (x, y, z, \lambda , \mu) = 2 z - \lambda + \mu = 0,</equation><equation>L _ {\lambda} ^ {\prime} (x, y, z, \lambda , \mu) = x ^ {2} + 2 y ^ {2} - z - 6 = 0,</equation><equation>L _ {\mu} ^ {\prime} (x, y, z, \lambda , \mu) = 4 x + 2 y + z - 3 0 = 0.</equation>(2) 式<equation>\times2-（1）</equation>式，并整理可得<equation>\lambda(4 y-x)=0.</equation>（i）若<equation>\lambda=0</equation>，则由（1）式，（2）式可得<equation>\mu=0</equation>，再由（3）式可得 z=0.此时，由（4）式，（5）式可得<equation>\left\{\begin{array}{l l}x^{2}+2 y^{2}=6\\2 x+y=1 5.\end{array}\right.</equation>椭圆<equation>x^{2}+2 y^{2}=6</equation>的长轴为x轴，短轴为y轴，长、短半轴长分别为<equation>\sqrt{6},\sqrt{3}</equation>，而直线<equation>2 x+y=1 5</equation>在x轴，y轴上的截距分别为<equation>\frac{1 5}{2}</equation>，15.从而直线<equation>2 x+y=1 5</equation>位于椭圆<equation>x^{2}+2 y^{2}=6</equation>上方，该方程无解.

（ii）若<equation>4 y - x = 0</equation>，则先由（4）式，（5）式消去变量<equation>z</equation>再代入该关系.

(4) 式 +（5）式可得<equation>x^{2}+4 x+2 y^{2}+2 y=3 6</equation>代入<equation>x=4 y</equation>可得，<equation>1 6 y^{2}+1 6 y+2 y^{2}+2 y=3 6</equation>整理可得<equation>y^{2}+y-2=0</equation>解得<equation>y=-2</equation>或<equation>y=1.</equation>当<equation>y = -2, x = -8</equation>时，由（5）式可得<equation>z = 66</equation>；当<equation>y = 1, x = 4</equation>时，由（5）式可得<equation>z = 12</equation>.

比较可得，在曲线 C上，点（-8，-2，66）到<equation>x O y</equation>面的距离最大，最大值为66.

---

**2020年第15题 | 解答题 | 10分**

15. (本题满分10分）

求函数<equation>f ( x,y)=x^{3}+8 y^{3}-x y</equation>的极值.

**答案:**<equation>\text {极 小 值} f \left(\frac {1}{6}, \frac {1}{1 2}\right) = - \frac {1}{2 1 6}.</equation>

**解析:**解<equation>\textcircled{1}</equation>计算 f(x,y)的驻点.

解<equation>\left\{ \begin{array}{l l} f_{x}^{\prime}(x,y)=3x^{2}-y=0, \\ f_{y}^{\prime}(x,y)=24y^{2}-x=0. \end{array} \right.</equation>将 y=3x²代入24y²-x=0可得216x⁴=x，解得x=0或x<equation>=\frac{1}{6}.</equation>于是，<equation>\left\{ \begin{array}{l l} x=0, \\ y=0 \end{array} \right.</equation>或<equation>\left\{ \begin{array}{l l} x=\frac{1}{6}, \\ y=\frac{1}{12}. \end{array} \right.</equation><equation>f(x,y)</equation>有两个驻点(0,0)，<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>\textcircled{2}</equation>计算 f(x,y)的二阶偏导数.<equation>f_{xx}^{\prime\prime}(x,y)=6x,</equation><equation>f_{xy}^{\prime\prime}(x,y)=-1,</equation><equation>f_{yy}^{\prime\prime}(x,y)=48y.</equation><equation>\textcircled{3}</equation>判断驻点是否为极值点以及确定极值点类型.

• 考虑驻点(0,0).<equation>A=f_{xx}^{\prime\prime}(0,0)=0,</equation><equation>B=f_{xy}^{\prime\prime}(0,0)=-1,</equation><equation>C=f_{yy}^{\prime\prime}(0,0)=0.</equation><equation>AC-B^{2}=0-1=-1<0</equation>，故点(0,0)不是极值点.

• 考虑驻点<equation>\left(\frac{1}{6},\frac{1}{12}\right).</equation><equation>A=f_{xx}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=1,</equation><equation>B=f_{xy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=-1,</equation><equation>C=f_{yy}^{\prime\prime}\left(\frac{1}{6},\frac{1}{12}\right)=4.</equation><equation>AC-B^{2}=4-1=3>0</equation>，且 A>0，故点<equation>\left(\frac{1}{6},\frac{1}{12}\right)</equation>为极小值点，极小值为<equation>f\left(\frac{1}{6},\frac{1}{12}\right)=\frac{1}{6^{3}}+\frac{8}{12^{3}}-\frac{1}{6 \times 12}=-\frac{1}{216}.</equation>

---

**2018年第16题 | 解答题 | 10分**

16. (本题满分10分)

将长为 2m的铁丝分成三段，依次围成圆、正方形与正三角形. 三个图形的面积之和是否存在最小值？若存在，求出最小值.

**答案:**三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

**解析:**解设圆、正方形、正三角形的周长分别为 x,y,z，则圆的半径<equation>r=\frac{x}{2\pi}</equation>正方形的边长 a<equation>=\frac{y}{4}</equation>正三角形的边长 b<equation>=\frac{z}{3}</equation>.于是，三个图形的面积之和为<equation>S (x, y, z) = \pi \cdot \left(\frac {x}{2 \pi}\right) ^ {2} + \left(\frac {y}{4}\right) ^ {2} + \frac {1}{2} \cdot \left(\frac {z}{3}\right) ^ {2} \cdot \sin \frac {\pi}{3} = \frac {x ^ {2}}{4 \pi} + \frac {y ^ {2}}{1 6} + \frac {\sqrt {3}}{3 6} z ^ {2}.</equation>由于三段铁丝的周长之和为2，故<equation>x+y+z=2.</equation>建立拉格朗日函数<equation>L(x,y,z,\lambda) = \frac{x^{2}}{4\pi} +\frac{y^{2}}{16} +\frac{\sqrt{3}}{36} z^{2} +\lambda (x + y + z - 2).</equation>令<equation>\left\{ \begin{array}{l} L _ {x} ^ {\prime} = \frac {1}{2 \pi} x + \lambda = 0, \\ L _ {y} ^ {\prime} = \frac {1}{8} y + \lambda = 0, \\ L _ {z} ^ {\prime} = \frac {\sqrt {3}}{1 8} z + \lambda = 0, \\ L _ {\lambda} ^ {\prime} = x + y + z - 2 = \end{array} \right.</equation>由前三个方程可得<equation>x = -2\pi \lambda ,y = -8\lambda ,z = -6\sqrt{3}\lambda .</equation>代入 x+y+z-2=0可得<equation>\lambda = - \frac {2}{2 \pi + 8 + 6 \sqrt {3}} = - \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>于是，<equation>x=\frac{2\pi}{\pi+4+3\sqrt{3}}, y=\frac{8}{\pi+4+3\sqrt{3}}, z=\frac{6\sqrt{3}}{\pi+4+3\sqrt{3}}.</equation>将所得<equation>x,y,z</equation>的值代入<equation>S(x,y,z)</equation>可得<equation>S (x, y, z) = \frac {\pi + 4 + 3 \sqrt {3}}{(\pi + 4 + 3 \sqrt {3}) ^ {2}} = \frac {1}{\pi + 4 + 3 \sqrt {3}}.</equation>为了判定所求得可能的极值点是否为最小值点，我们把问题转化为目标函数<equation>S ( x, y, z )</equation>在有界闭区域<equation>D=\{(x,y,z)\mid x+y+z=2,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>上的最值问题.

由于连续函数在有界闭区域上一定能取到最值，故若我们能分别计算出<equation>S ( x, y, z )</equation>在边界<equation>y + z = 2, z + x = 2, x + y = 2</equation>上的最值，再与<equation>\frac{1}{\pi+4+3\sqrt{3}}</equation>比较，则所得最小值即为区域D上的最小值.

当<equation>x = 0</equation>时，<equation>S(0,y,z)</equation>在<equation>y + z = 2</equation>下的最小值为<equation>S\left(0,\frac{8}{4 + 3\sqrt{3}},\frac{6\sqrt{3}}{4 + 3\sqrt{3}}\right) = \frac{1}{4 + 3\sqrt{3}}.</equation>当<equation>y=0</equation>时，<equation>S ( x, 0, z )</equation>在<equation>x+z=2</equation>下的最小值为<equation>S \left( \frac{2 \pi}{\pi+3 \sqrt{3}}, 0, \frac{6 \sqrt{3}}{\pi+3 \sqrt{3}} \right)=\frac{1}{\pi+3 \sqrt{3}}.</equation>当<equation>z = 0</equation>时，<equation>S(x,y,0)</equation>在<equation>x + y = 2</equation>下的最小值为<equation>S\left(\frac{2\pi}{\pi + 4},\frac{8}{\pi + 4},0\right) = \frac{1}{\pi + 4}</equation>4个值比较可得，<equation>\frac{1}{\pi+4+3\sqrt{3}}</equation>为整个区域D上的最小值，也为<equation>x+y+z=2,x>0,y>0,z>0</equation>时的<equation>S(x,y,z)</equation>的最小值.三个图形的面积之和存在最小值，最小值为<equation>\frac{1}{\pi+4+3\sqrt{3}}.</equation>

---

**2015年第17题 | 解答题 | 10分**

17. (本题满分10分）

已知函数<equation>f ( x,y)=x+y+ x y</equation>，曲线 C：<equation>x^{2}+y^{2}+ x y=3</equation>，求 f(x,y)在曲线 C上的最大方向导数.

**解析:**解 由于函数在一点处的方向导数的最大值等于函数在该点的梯度的模，故求<equation>f ( x,y )</equation>在曲线 C上的最大方向导数等价于求<equation>f ( x,y )</equation>在曲线C上梯度的模的最大值.为了计算方便，考虑梯度模的平方函数.令<equation>g ( x,y ) = f_{x}^{\prime 2}+f_{y}^{\prime 2}=(1+y)^{2}+(1+x)^{2}</equation>，下面求<equation>g ( x,y )</equation>在条件<equation>x^{2}+y^{2}+xy=3</equation>下的最值.作拉格朗日函数<equation>L (x, y, \lambda) = (1 + y) ^ {2} + (1 + x) ^ {2} + \lambda \left(x ^ {2} + y ^ {2} + x y - 3\right).</equation>令<equation>\left[ L _ {x} ^ {\prime} = 2 (1 + x) + \lambda (2 x + y) = 0, \right.</equation><equation>\left\{L _ {y} ^ {\prime} = 2 (1 + y) + \lambda (2 y + x) = 0, \right.</equation><equation>L _ {\lambda} ^ {\prime} = x ^ {2} + y ^ {2} + x y - 3 = 0.</equation>由（1）、(2）消去<equation>\lambda</equation>得到<equation>(x - y)(x + y - 1) = 0</equation>，从而<equation>x = y</equation>或<equation>x + y = 1</equation>若 x = y，代入（3）式，解得 x = y =<equation>\pm 1</equation>；若 x+y=1，代入（3）式，解得 x=2，y=-1或 x=-1， y=2.于是（1，1），（-1，-1），（2，-1），（-1，2）都是可能的最值点.又<equation>g (1, 1) = 8, \quad g (- 1, - 1) = 0, \quad g (2, - 1) = g (- 1, 2) = 9,</equation>故<equation>g ( x,y )</equation>在条件<equation>x^{2}+y^{2}+xy=3</equation>下的最大值为9，从而<equation>f ( x,y )</equation>在曲线C上的最大方向导数为3.

---

**2013年第17题 | 解答题 | 10分**

17. (本题满分10分）

求函数<equation>f ( x,y)=\left(y+\frac{x^{3}}{3}\right)\mathrm{e}^{x+y}</equation>的极值.

**解析:**解 由题设知，<equation>f _ {x} ^ {\prime} (x, y) = x ^ {2} \mathrm {e} ^ {x + y} + \left(y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y} = \left(x ^ {2} + y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {y} ^ {\prime} (x, y) = \mathrm {e} ^ {x + y} + \left(y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y} = \left(1 + y + \frac {x ^ {3}}{3}\right) \mathrm {e} ^ {x + y}.</equation>令<equation>\left\{ \begin{array}{l} f_x^{\prime}(x,y) = 0, \\ f_y^{\prime}(x,y) = 0, \end{array} \right.</equation>即<equation>\left\{ \begin{array}{l} x^{2} + y + \frac{x^{3}}{3} = 0, \\ 1 + y + \frac{x^{3}}{3} = 0, \end{array} \right.</equation>解得驻点为<equation>\left(1, - \frac{4}{3}\right), \left(-1, - \frac{2}{3}\right).</equation>计算 f(x,y)的二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + 2 x ^ {2} + 2 x + y\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {x y} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + x ^ {2} + y + 1\right) \mathrm {e} ^ {x + y},</equation><equation>f _ {y y} ^ {\prime \prime} = \left(\frac {x ^ {3}}{3} + y + 2\right) \mathrm {e} ^ {x + y}.</equation>在驻点<equation>\left( 1,-\frac{4}{3} \right)</equation>处，<equation>A = f _ {x x} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = 3 \mathrm {e} ^ {- \frac {1}{3}}, \quad B = f _ {x y} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = \mathrm {e} ^ {- \frac {1}{3}}, \quad C = f _ {y y} ^ {\prime \prime} \left(1, - \frac {4}{3}\right) = \mathrm {e} ^ {- \frac {1}{3}},</equation>于是<equation>AC - B^{2} = 2\mathrm{e}^{-\frac{2}{3}} > 0,A > 0</equation>，故点<equation>\left(1, - \frac{4}{3}\right)</equation>为<equation>f(x,y)</equation>的极小值点，极小值为<equation>f\left(1, - \frac{4}{3}\right) = -\mathrm{e}^{-\frac{1}{3}}.</equation>在驻点<equation>\left(-1,-\frac{2}{3}\right)</equation>处，<equation>A = f _ {x x} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = - \mathrm {e} ^ {- \frac {5}{3}}, \quad B = f _ {x y} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = \mathrm {e} ^ {- \frac {5}{3}}, \quad C = f _ {y y} ^ {\prime \prime} \left(- 1, - \frac {2}{3}\right) = \mathrm {e} ^ {- \frac {5}{3}},</equation>于是<equation>AC-B^{2}=-2\mathrm{e}^{-\frac{10}{3}}<0</equation>，故点<equation>\left(-1,-\frac{2}{3}\right)</equation>不是极值点.

综上所述，<equation>f ( x,y)</equation>只在点<equation>\left( 1,-\frac{4}{3} \right)</equation>处取得极值<equation>f\left( 1,-\frac{4}{3}\right)=-\mathrm{e}^{-\frac{1}{3}}</equation>，且为极小值.

---

**2012年第16题 | 解答题 | 10分**

16. (本题满分10分）

求函数<equation>f ( x,y)=x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极值.

**答案:**(16) 极大值<equation>f(1,0) = \mathrm{e}^{-\frac{1}{2}}</equation>，极小值<equation>f(-1,0) = -\mathrm{e}^{-\frac{1}{2}}.</equation>

**解析:**解<equation>\textcircled{1}</equation>先找到 f(x,y)的全部驻点.

记<equation>g ( x,y) = \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}.</equation>由于<equation>f _ {x} ^ {\prime} (x, y) = \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = \left(1 - x ^ {2}\right) g (x, y),</equation><equation>f _ {y} ^ {\prime} (x, y) = - x y \mathrm {e} ^ {- \frac {x ^ {2} + y ^ {2}}{2}} = (- x y) g (x, y).</equation>由于 g(x,y) > 0，故满足<equation>\left\{\begin{array}{l l}1-x^{2}=0\\-xy=0\end{array}\right.</equation>的点（x，y）为 f(x，y）的驻点.解该方程组得（x，y）= （<equation>\pm1,0).</equation>因此，点（1，0）和点（-1，0）为<equation>f ( x,y)</equation>的全部驻点.<equation>\textcircled{2}</equation>计算二阶偏导数.<equation>f _ {x x} ^ {\prime \prime} (x, y) = (- 2 x) g (x, y) + \left(1 - x ^ {2}\right) g _ {x} ^ {\prime} (x, y),</equation><equation>f _ {x y} ^ {\prime \prime} (x, y) = \left(1 - x ^ {2}\right) g _ {y} ^ {\prime} (x, y),</equation><equation>f _ {y y} ^ {\prime \prime} (x, y) = (- x) g (x, y) + (- x y) g _ {y} ^ {\prime} (x, y).</equation><equation>\textcircled{3}</equation>计算<equation>A C-B^{2}.</equation>由于<equation>f(x,y)</equation>的驻点<equation>(x_0,y_0)</equation>均满足<equation>1 - x_0^2 = 0, - x_0y_0 = 0</equation>，而<equation>g(x,y)</equation>恒大于零，故在驻点 (1,0) 处，<equation>f_{xx}^{\prime \prime}(1,0) = -2g(1,0) < 0, f_{xy}^{\prime \prime}(1,0) = 0, f_{yy}^{\prime \prime}(1,0) = -g(1,0)</equation>.因此，<equation>f _ {x x} ^ {\prime \prime} (1, 0) f _ {y y} ^ {\prime \prime} (1, 0) - \left[ f _ {x y} ^ {\prime \prime} (1, 0) \right] ^ {2} = 2 g ^ {2} (1, 0) > 0.</equation>由于<equation>f_{xx}^{\prime \prime}(1,0)=-2 g(1,0)<0</equation>，故点（1，0）为<equation>f(x,y)</equation>的极大值点，<equation>f(1,0)=\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极大值.同理可得，点（-1，0）为<equation>f(x,y)</equation>的极小值点，<equation>f(-1,0)=-\mathrm{e}^{-\frac{1}{2}}</equation>为<equation>f(x,y)</equation>的极小值.

因此，函数<equation>f ( x,y) = x \mathrm{e}^{- \frac{x^{2}+y^{2}}{2}}</equation>的极大值为<equation>\mathrm{e}^{- \frac{1}{2}}</equation>，极小值为<equation>- \mathrm{e}^{- \frac{1}{2}}.</equation>

---

**2011年第3题 | 选择题 | 4分 | 答案: A**

3. 设函数 f(x)具有二阶连续导数，且 f(x) > 0，<equation>f^{\prime}(0)=0</equation>，则函数 z=f(x)<equation>\ln f(y)</equation>在点 (0,0)处取得极小值的一个充分条件是（    ）

A.<equation>f(0)>1,f^{\prime\prime}(0)>0</equation>B.<equation>f(0)>1,f^{\prime\prime}(0)<0</equation>C.<equation>f(0)<1,f^{\prime\prime}(0)>0</equation>D.<equation>f(0)<1,f^{\prime\prime}(0)<0</equation>

答案: A

**解析:**由题设知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = f ^ {\prime} (x) \ln f (y) \Big | _ {(0, 0)} = f ^ {\prime} (0) \ln f (0) = 0,</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = \frac {f (x) f ^ {\prime} (y)}{f (y)} \Bigg | _ {(0, 0)} = \frac {f (0) f ^ {\prime} (0)}{f (0)} = 0.</equation>从而点（0，0）为函数<equation>z ( x,y)</equation>的驻点.又<equation>A = \left. \frac {\partial^ {2} z}{\partial x ^ {2}} \right| _ {(0, 0)} = f ^ {\prime \prime} (x) \ln f (y) \Big | _ {(0, 0)} = f ^ {\prime \prime} (0) \ln f (0),</equation><equation>B = \left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(0, 0)} = \left. \frac {f ^ {\prime} (x) f ^ {\prime} (y)}{f (y)} \right| _ {(0, 0)} = \frac {f ^ {\prime} (0) f ^ {\prime} (0)}{f (0)} = 0,</equation><equation>C = \left. \frac {\partial^ {2} z}{\partial y ^ {2}} \right| _ {(0, 0)} = f (x) \cdot \frac {f ^ {\prime \prime} (y) f (y) - \left[ f ^ {\prime} (y) \right] ^ {2}}{f ^ {2} (y)} \Bigg | _ {(0, 0)} = \frac {f ^ {2} (0) f ^ {\prime \prime} (0) - f (0) \left[ f ^ {\prime} (0) \right] ^ {2}}{f ^ {2} (0)} = f ^ {\prime \prime} (0).</equation>令<equation>A=f^{\prime \prime}(0)\ln f(0)>0, A C-B^{2}=[f^{\prime \prime}(0)]^{2}\ln f(0)>0</equation>，解得<equation>f(0)>1,f^{\prime \prime}(0)>0.</equation>因此，<equation>f(0)>1,f^{\prime \prime}(0)>0</equation>为函数<equation>z(x,y)</equation>在点（0,0）处取得极小值的一个充分条件.应选A.

---

**2009年第15题 | 解答题 | 10分**

15. (本题满分9分）

求二元函数<equation>f ( x,y)=x^{2}\left( 2+y^{2}\right)+y\ln y</equation>的极值.

**答案:**(15) 极小值<equation>f\left(0,\frac{1}{\mathrm{e}}\right) = -\frac{1}{\mathrm{e}}.</equation>

**解析:**解 令<equation>\left\{\begin{array}{l l}f_{x}^{\prime}(x,y)=2 x(2+y^{2})=0,\\ f_{y}^{\prime}(x,y)=2 x^{2} y+\ln y+1=0,\end{array} \right.</equation>解得驻点为<equation>\left(0,\frac{1}{e}\right).</equation>f(x,y)的二阶偏导数为<equation>f_{xx}^{\prime \prime}(x,y)=2(2+y^{2}),</equation><equation>f_{xy}^{\prime \prime}(x,y)=4 x y,</equation><equation>f_{yy}^{\prime \prime}(x,y)=2 x^{2}+\frac{1}{y},</equation>于是<equation>A=f_{xx}^{\prime \prime}\left(0,\frac{1}{e}\right)=2\left(2+\frac{1}{e^{2}}\right),</equation><equation>B=f_{xy}^{\prime \prime}\left(0,\frac{1}{e}\right)=0,</equation><equation>C=f_{yy}^{\prime \prime}\left(0,\frac{1}{e}\right)=\mathrm{e}.</equation>由于<equation>AC-B^{2}>0,</equation><equation>A>0</equation>，故f(x,y)在<equation>\left(0,\frac{1}{e}\right)</equation>处取得极小值<equation>f\left(0,\frac{1}{e}\right)=-\frac{1}{e}.</equation>

---


#### 多元函数微分学的几何应用


**2023年第12题 | 填空题 | 5分**

12. 曲面<equation>z=x+2y+\ln(1+x^2+y^2)</equation>在点<equation>(0,0,0)</equation>处的切平面方程为 ___

**答案:**<equation>x + 2 y - z = 0.</equation>

**解析:**解记曲面<equation>z = x + 2y + \ln (1 + x^{2} + y^{2})</equation>为<equation>\varSigma, F(x,y,z) = x + 2y + \ln (1 + x^{2} + y^{2}) - z</equation>，则曲面<equation>\varSigma</equation>的方程为<equation>F(x,y,z) = 0</equation>，其在点（x,y,z）处的一个法向量为<equation>\left(\frac {\partial F}{\partial x}, \frac {\partial F}{\partial y}, \frac {\partial F}{\partial z}\right) = \left(1 + \frac {2 x}{1 + x ^ {2} + y ^ {2}}, 2 + \frac {2 y}{1 + x ^ {2} + y ^ {2}}, - 1\right).</equation>代入点（0，0，0）的坐标可得曲面<equation>\varSigma</equation>在点（0，0，0）处的法向量为（1，2，-1）.因此，曲面<equation>\varSigma</equation>在点 （0，0，0）处的切平面方程为<equation>(x - 0) + 2 (y - 0) - (z - 0) = 0,</equation>即<equation>x+2y-z=0.</equation>

---

**2018年第2题 | 选择题 | 4分 | 答案: B**

2. 过点（1,0,0），（0,1,0），且与曲面<equation>z=x^{2}+y^{2}</equation>相切的平面为（    )

A.<equation>z=0</equation>与<equation>x+y-z=1</equation>B.<equation>z=0</equation>与<equation>2 x+2 y-z=2</equation>C.<equation>x=y</equation>与<equation>x+y-z=1</equation>D.<equation>x=y</equation>与<equation>2 x+2 y-z=2</equation>

答案: B

**解析:**解（法一）记<equation>F ( x,y,z) = z - x^{2} - y^{2}</equation>，则曲面<equation>z = x^{2} + y^{2}</equation>的方程为<equation>F ( x,y,z) = 0.</equation>根据曲面的切平面的定义，曲面<equation>F ( x,y,z) = 0</equation>在点（x,y,z）处的切平面的一个法向量为<equation>(-2x,-2y,1)</equation>（也可以取作（2x,2y，-1）).于是，该点处的切平面的点法式方程为<equation>- 2 x (X - x) - 2 y (Y - y) + (Z - z) = 0.</equation>由于所求切平面过点（1，0，0），（0，1，0），故将这两点的坐标分别代入（1）式可得，<equation>- 2 x (1 - x) + 2 y ^ {2} - z \frac {x ^ {2} + y ^ {2} = z}{- 2 x + z} - 2 x + z = 0,</equation><equation>2 x ^ {2} - 2 y (1 - y) - z \xlongequal {x ^ {2} + y ^ {2} = z} - 2 y + z = 0.</equation>联立<equation>\left\{ \begin{array}{l l} z = 2x, \\ z = 2y, \\ z = x^{2} + y^{2}. \end{array} \right.</equation>由前两个方程可得<equation>x = y</equation>，代入第三个方程可得<equation>2x = 2x^{2}</equation>，解得<equation>x = 0</equation>或<equation>x = 1</equation>. 当<equation>x = 0</equation>时，<equation>y = 0, z = 0</equation>；当<equation>x = 1</equation>时，<equation>y = 1, z = 2</equation>. 从而切点坐标为（0,0,0）或（1,1,2）.

将这两个切点的坐标分别代入（1）式，可得所求切平面的方程分别为 Z=0与<equation>2 X+2 Y-Z=2</equation>因此，应选B.

（法二）排除法.

由于点（1，0，0）和点（0，1，0）均位于所求切平面上，而这两点均不满足方程 x=y，故可排除选项C和选项D.

另一方面，曲面<equation>z=x^{2}+y^{2}</equation>上点（x,y,z）处的切平面的法向量应与（2x，2y，-1）共线.平面<equation>x+y-z=1</equation>的一个法向量为（1，1，-1).若其为切平面，则<equation>\frac{2x}{1}=\frac{2y}{1}=\frac{-1}{-1}</equation>，切点坐标应满足<equation>x=\frac{1}{2}</equation><equation>y=\frac{1}{2}</equation>.代入<equation>z=x^{2}+y^{2}</equation>得<equation>z=\frac{1}{2}</equation>.但是<equation>\left(\frac{1}{2},\frac{1}{2},\frac{1}{2}\right)</equation>并不满足方程<equation>x+y-z=1</equation>.于是，选项A也不正确.

由排除法可知，应选B.

---

**2014年第9题 | 填空题 | 4分**

9. 曲面<equation>z=x^{2}(1-\sin y)+y^{2}(1-\sin x)</equation>在点（1,0,1）处的切平面方程为 ___

**答案:**<equation>2 x - y - z - 1 = 0.</equation>

**解析:**从而切平面的方程为<equation>2 ( x - 1 ) - ( y - 0 ) - ( z - 1 ) = 0</equation>即<equation>2 x - y - z - 1 = 0.</equation>

---

**2013年第2题 | 选择题 | 4分 | 答案: A**

2. 曲面<equation>x^{2}+\cos(xy)+yz+x=0</equation>在点（0，1，-1）处的切平面方程为（    ）

A.<equation>x-y+z=-2</equation>B.<equation>x+y+z=0</equation>C.<equation>x-2y+z=-3</equation>D.<equation>x-y-z=0</equation>

答案: A

**解析:**解 令<equation>F ( x,y,z) = x^{2} + \cos ( x y ) + y z + x</equation>，则曲面在点（0，1，-1）处的法向量为<equation>\left. \left(\frac {\partial F}{\partial x}, \frac {\partial F}{\partial y}, \frac {\partial F}{\partial z}\right) \right| _ {(0, 1, - 1)} = \left(2 x - y \sin (x y) + 1, - x \sin (x y) + z, y\right) \Big | _ {(0, 1, - 1)} = (1, - 1, 1).</equation>从而曲面在点（0,1，-1）处的切平面方程为<equation>x - ( y - 1 ) + ( z + 1 ) = 0</equation>，即<equation>x - y + z = - 2</equation>，选A.

---


#### 全微分的概念与计算


**2021年第2题 | 选择题 | 5分 | 答案: C**

2. 设函数 f(x,y)可微，且<equation>f \left( x+1, \mathrm{e}^{x} \right)=x \left( x+1 \right)^{2}, f \left( x, x^{2} \right)=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f \left( 1, 1 \right)=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>

答案: C

**解析:**根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f(x + 1,\mathrm{e}^{x}) = x(x + 1)^{2},f(x,x^{2}) = 2x^{2}\ln x</equation>两端均关于<equation>x</equation>求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令<equation>x=0</equation>，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令<equation>x=1</equation>，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第3题 | 选择题 | 4分 | 答案: A**

3. 设函数 f(x,y)在点(0,0)处可微，<equation>f(0,0)=0,\boldsymbol{n}=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},-1\right)\bigg|_{(0,0)},</equation>非零向量<equation>\alpha</equation>与n垂直，则（    )

A.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\boldsymbol{n}\cdot(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

B.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\boldsymbol{n}\times(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

C.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\alpha\cdot(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

D.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\alpha\times(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

答案: A

**解析:**由函数<equation>f ( x,y )</equation>在点（0，0）处可微，且<equation>f ( 0,0 )=0</equation>可知，<equation>\begin{aligned} 0 &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f (0 , 0) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} \\ \underline {{f (0 , 0) = 0}} \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= - \lim _ {(x, y) \rightarrow (0, 0)} \frac {f _ {x} ^ {\prime} (0 , 0) x + f _ {y} ^ {\prime} (0 , 0) y - f (x , y)}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= - \lim _ {(x, y) \rightarrow (0, 0)} \frac {\boldsymbol {n} \cdot (x , y , f (x , y))}{\sqrt {x ^ {2} + y ^ {2}}}. \end{aligned}</equation>因此，<equation>\lim_{(x,y)\to (0,0)}\frac{|\boldsymbol{n}\cdot(x,y,f(x,y))|}{\sqrt{x^2 + y^2}} = \lim_{(x,y)\to (0,0)}\frac{\boldsymbol{n}\cdot(x,y,f(x,y))}{\sqrt{x^2 + y^2}} = 0</equation>，应选A.

下面说明其余选项均不正确.<equation>\begin{array}{l} + y k, | n \times (x, y, x) | = \sqrt {4 x ^ {2} + 2 y ^ {2}}. \\ \end{array}</equation><equation>\lim _ {(x, y) \rightarrow (0, 0)} \frac {\left| \boldsymbol {n} \times (x , y , x) \right|}{\sqrt {x ^ {2} + y ^ {2}}} = \lim _ {(x, y) \rightarrow (0, 0)} \frac {\sqrt {4 x ^ {2} + 2 y ^ {2}}}{\sqrt {x ^ {2} + y ^ {2}}} = \lim _ {(x, y) \rightarrow (0, 0)} \sqrt {2 + \frac {2 x ^ {2}}{x ^ {2} + y ^ {2}}}.</equation>取<equation>y=x</equation>与<equation>y=\sqrt{3} x</equation>两条不同路径，可得沿这两条路径所得极限不一样，从而该二重极限不存在.

---

**2016年第11题 | 填空题 | 4分**

11. 设函数 f(u,v) 可微，z=z(x,y) 由方程<equation>( x+1 ) z-y^{2}=x^{2} f ( x-z,y )</equation>确定，则<equation>\mathrm{d} z |_{(0,1)}=</equation>___

**答案:**-<equation>\mathrm{d} x+2 \mathrm{d} y.</equation>

**解析:**解（法一）对已知方程两端分别关于<equation>x,y</equation>求偏导数，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} = 2 x f (x - z, y) + x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(1 - \frac {\partial z}{\partial x}\right) \right].</equation><equation>(x + 1) \frac {\partial z}{\partial y} - 2 y = x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(- \frac {\partial z}{\partial y}\right) + f _ {2} ^ {\prime} (x - z, y) \right].</equation>将<equation>(x,y) = (0,1)</equation>代入已知方程，可得<equation>z - 1 = 0</equation>，从而<equation>z(0,1) = 1.</equation>再将<equation>(x,y,z) = (0,1,1)</equation>代入（1）、（2）两式，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,1)} = -1,\frac{\partial z}{\partial y}\bigg|_{(0,1)} = 2.</equation>因此，<equation>\mathrm {d} z \mid_ {(0, 1)} = - \mathrm {d} x + 2 \mathrm {d} y.</equation>（法二）对已知方程两端微分，可得<equation>\mathrm{d}[ ( x + 1 ) z ] - \mathrm{d} ( y^{2} ) = \mathrm{d}[ x^{2} f ( x - z , y ) ]</equation>.进一步可得，<equation>\begin{aligned} (x + 1) \mathrm {d} z + z \mathrm {d} x - 2 y \mathrm {d} y &= f (x - z, y) \mathrm {d} \left(x ^ {2}\right) + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right] \\ &= 2 x f (x - z, y) \mathrm {d} x + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right]. \end{aligned}</equation>将<equation>(x,y) = (0,1)</equation>代入已知方程，可得<equation>z - 1 = 0</equation>，从而<equation>z(0,1) = 1.</equation>代入上式可得<equation>\mathrm {d} z + \mathrm {d} x - 2 \mathrm {d} y = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,1)} = -\mathrm{d}x + 2\mathrm{d}y.</equation>

---

**2015年第11题 | 填空题 | 4分**

11. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{z} + xyz + x + \cos x = 2</equation>确定，则<equation>\mathrm{d}z|_{(0,1)} =</equation>___

**解析:**<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial y} + x z + x y \frac {\partial z}{\partial y} = 0.</equation>将<equation>( x,y)=(0,1)</equation>代入原方程，得到<equation>z ( 0,1 )=0.</equation>再将<equation>( x,y,z)=(0,1,0)</equation>代入方程（1）、（2），得到<equation>\left. \frac{\partial z}{\partial x}\right|_{(0,1)}=-1,\left. \frac{\partial z}{\partial y}\right|_{(0,1)}=0.</equation>于是<equation>\mathrm {d} z \mid_ {(0, 1)} = \frac {\partial z}{\partial x} \Big | _ {(0, 1)} \mathrm {d} x + \frac {\partial z}{\partial y} \Big | _ {(0, 1)} \mathrm {d} y = - \mathrm {d} x.</equation>（法二）对方程<equation>\mathrm{e}^{z}+xyz+x+\cos x=2</equation>两端微分，得到<equation>\mathrm {e} ^ {z} \mathrm {d} z + x y \mathrm {d} z + x z \mathrm {d} y + y z \mathrm {d} x + \mathrm {d} x - \sin x \mathrm {d} x = 0,</equation>整理得<equation>\left(\mathrm {e} ^ {z} + x y\right) \mathrm {d} z = (\sin x - 1 - y z) \mathrm {d} x - x z \mathrm {d} y.</equation>将<equation>(x,y) = (0,1)</equation>代入原方程，得到<equation>z(0,1) = 0</equation>，再代入上式得到<equation>\mathrm{d}z|_{(0,1)} = -\mathrm{d}x.</equation>## （法三）利用隐函数存在定理.

令<equation>F ( x,y,z) = \mathrm{e}^{z}+ x y z+x+\cos x-2.</equation>将（x,y）=（0,1）代入原方程，得到<equation>z ( 0,1 )=0</equation>从而<equation>F ( 0,1,0 )=0.</equation>又<equation>F _ {x} ^ {\prime} (x, y, z) = y z + 1 - \sin x, \quad F _ {y} ^ {\prime} (x, y, z) = x z, \quad F _ {z} ^ {\prime} (0, 1, 0) = \left(\mathrm {e} ^ {z} + x y\right) | _ {(0, 1, 0)} = 1 \neq 0,</equation>故由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 1)} = - \frac {F _ {x} ^ {\prime} (0 , 1 , 0)}{F _ {z} ^ {\prime} (0 , 1 , 0)} = - 1, \quad \left. \frac {\partial z}{\partial y} \right| _ {(0, 1)} = - \frac {F _ {y} ^ {\prime} (0 , 1 , 0)}{F _ {z} ^ {\prime} (0 , 1 , 0)} = 0,</equation>从而<equation>\mathrm{d}z\mid_{(0,1)} = \frac{\partial z}{\partial x}\bigg|_{(0,1)}\mathrm{d}x + \frac{\partial z}{\partial y}\bigg|_{(0,1)}\mathrm{d}y = -\mathrm{d}x.</equation>解（法一）对方程<equation>\mathrm{e}^{z}+xyz+x+\cos x=2</equation>两端分别关于 x,y求偏导数，得到<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial x} + y z + x y \frac {\partial z}{\partial x} + 1 - \sin x = 0,</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**

3. 如果函数 f(x,y)在点(0,0)处连续，那么下列命题正确的是（    )

A. 若极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{|x|+|y|}</equation>存在，则 f(x,y)在点(0,0)处可微

B. 若极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{x^{2}+y^{2}}</equation>存在，则 f(x,y)在点(0,0)处可微

C. 若 f(x,y)在点(0,0)处可微，则极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{|x|+|y|}</equation>存在

D. 若 f(x,y)在点(0,0)处可微，则极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{x^{2}+y^{2}}</equation>存在

答案: B

**解析:**解 对于选项A，取<equation>f ( x,y)=| x |+| y |</equation>，则<equation>f ( x,y)</equation>在点（0,0）处连续，且<equation>\lim_{x\to 0}\frac{f(x,y)}{|x|+|y|}=1</equation>但<equation>f ( x,y)</equation>在点（0,0）处的偏导数都不存在，故<equation>f ( x,y)</equation>在点（0,0）处不可微，从而选项A不正确.

对于选项C、D，取<equation>f ( x,y)\equiv 1</equation>，可知选项C、D不正确.

由排除法选B.下面证明选项B.

设<equation>\lim_{x\to 0}\frac{f(x,y)}{x^2 + y^2} = a</equation>，由于<equation>f(x,y)</equation>在（0,0）处连续，故<equation>f (0, 0) = \lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 0}} f (x, y) = \lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 0}} \left[ \frac {f (x , y)}{x ^ {2} + y ^ {2}} \cdot \left(x ^ {2} + y ^ {2}\right)\right] = a \cdot 0 = 0,</equation>从而<equation>\lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \frac {f (\Delta x , \Delta y) - f (0 , 0)}{\sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}}} = \lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \left[ \frac {f (\Delta x , \Delta y)}{(\Delta x) ^ {2} + (\Delta y) ^ {2}} \cdot \sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}} \right] = a \lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}} = 0,</equation>即有<equation>f \left(\Delta x, \Delta y\right) - f (0, 0) = 0 \cdot \Delta x + 0 \cdot \Delta y + o \left(\sqrt {\left(\Delta x\right) ^ {2} + \left(\Delta y\right) ^ {2}}\right).</equation>由可微的定义知，<equation>f(x,y)</equation>在点（0,0）处可微.

---


### 一元函数积分学

#### 定积分的计算


**2025年第17题 | 解答题 | 10分**
17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>
**答案: **#<equation>\frac{3\ln 2+\pi}{10}.</equation>
**解析: **解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得 B=-A.将 B=-A 代入（2）式可得 C=3A.将 C=3A 代入（3）式可得 5A=1，即<equation>A=\frac{1}{5}.</equation>进一步可得 B=-<equation>\frac{1}{5},</equation>C<equation>=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 设连续函数 f(x)满足<equation>f(x+2)-f(x)=x,\int_{0}^{2} f(x)\mathrm{d} x=0</equation>，则<equation>\int_{1}^{3} f(x)\mathrm{d} x=</equation>___
**解析: **解注意到<equation>\int_{2}^{3} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x</equation>，故由<equation>f(x+2)-f(x)=x</equation>可得，<equation>\int_{2}^{3} f(x)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} x\mathrm{d}x=\frac{1}{2}.</equation>(1)

又因为<equation>\int_{0}^{1} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\int_{0}^{2} f(x)\mathrm{d}x=0</equation>，所以<equation>-\int_{0}^{1} f(x)\mathrm{d}x=\int_{1}^{2} f(x)\mathrm{d}x.</equation>从而由（1）式可得<equation>\int_{2}^{3} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\frac{1}{2},</equation>即<equation>\int_{1}^{3} f(x)\mathrm{d}x=\frac{1}{2}.</equation>

---

**2022年第12题 | 填空题 | 5分**
<equation>1 2. \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解（法一）利用根式代换.

令<equation>t = \sqrt{x}</equation>，则<equation>x = t^{2}</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {1} ^ {e ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x \xlongequal {t = \sqrt {x}} \int_ {1} ^ {e} \frac {2 \ln t}{t} \cdot 2 t \mathrm {d} t &= 4 \int_ {1} ^ {e} \ln t \mathrm {d} t = 4 \left(t \ln t \Big | _ {1} ^ {e} - \int_ {1} ^ {e} t \cdot \frac {1}{t} \mathrm {d} t\right) \\ &= 4 \left[ \mathrm {e} - (\mathrm {e} - 1) \right] = 4. \end{aligned}</equation>（法二）利用分部积分法.<equation>\begin{aligned} \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {1} ^ {\mathrm {e} ^ {2}} \ln x \mathrm {d} (\sqrt {x}) = 2 \left(\sqrt {x} \ln x \Big | _ {1} ^ {\mathrm {e} ^ {2}} - \int_ {1} ^ {\mathrm {e} ^ {2}} \sqrt {x} \cdot \frac {1}{x} \mathrm {d} x\right) = 2 \left(2 \mathrm {e} - \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {1}{\sqrt {x}} \mathrm {d} x\right) \\ &= 4 \mathrm {e} - 4 \sqrt {x} \Big | _ {1} ^ {\mathrm {e} ^ {2}} = 4 \mathrm {e} - (4 \mathrm {e} - 4) = 4. \end{aligned}</equation>

---

**2015年第10题 | 填空题 | 4分**
10.<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \underline {{}}</equation>
**解析: **由于<equation>\frac{\sin x}{1 + \cos x}</equation>是奇函数，<equation>|x|</equation>是偶函数，故<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x = 0, \quad \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 2 \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} x = \frac {\pi^ {2}}{4}.</equation>因此，<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 0 + \frac {\pi^ {2}}{4} = \frac {\pi^ {2}}{4}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: A**
4. 若<equation>\int_{-\pi}^{\pi} \left(x-a_{1}\cos x-b_{1}\sin x\right)^{2}\mathrm{d}x=\min_{a,b\in\mathbf{R}}\left\{\int_{-\pi}^{\pi}\left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x\right\}</equation>，则<equation>a_{1}\cos x+b_{1}\sin x=</equation>(    )

A. 2sinx B. 2cosx C. 2<equation>\pi\sin x</equation>D. 2<equation>\pi\cos x</equation>
答案: A
**解析: **解（法一）<equation>\begin{aligned} \int_ {- \pi} ^ {\pi} \left(x - a \cos x - b \sin x\right) ^ {2} \mathrm {d} x &= \int_ {- \pi} ^ {\pi} \left(x ^ {2} + a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 a x \cos x - 2 b x \sin x + 2 a b \sin x \cos x\right) \mathrm {d} x \\ \xlongequal {\text {对称性}} 2 \int_ {0} ^ {\pi} x ^ {2} \mathrm {d} x + 2 \int_ {0} ^ {\pi} \left(a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 b x \sin x\right) \mathrm {d} x \\ &= \frac {2}{3} \pi^ {3} + \left(a ^ {2} + b ^ {2} - 4 b\right) \pi . \end{aligned}</equation>当 a=0时，<equation>a^{2}</equation>最小；当 b=2时，<equation>b^{2}-4b</equation>最小，从而当 a=0，b=2时，<equation>\int_{- \pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>最小.因此<equation>a_{1}=0,b_{1}=2</equation>，从而<equation>a_{1}\cos x+b_{1}\sin x=2\sin x</equation>，应选A.

（法二）看作二元函数的最值问题求解.

令<equation>f ( a,b)=\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，则<equation>\frac {\partial f (a , b)}{\partial a} = \int_ {- \pi} ^ {\pi} \left[ - 2 (x - a \cos x - b \sin x) \cos x \right] \mathrm {d} x = 2 a \int_ {- \pi} ^ {\pi} \cos^ {2} x \mathrm {d} x = 2 a \pi ,</equation><equation>\frac {\partial f (a , b)}{\partial b} = \int_ {- \pi} ^ {\pi} \left[ - 2 \left(x - a \cos x - b \sin x\right) \sin x \right] \mathrm {d} x = 2 \int_ {- \pi} ^ {\pi} \left(b \sin^ {2} x - x \sin x\right) \mathrm {d} x = 2 \left(b \pi - 2 \pi\right).</equation>令<equation>\frac{\partial f(a,b)}{\partial a} = 0,\frac{\partial f(a,b)}{\partial b} = 0</equation>，解得<equation>a = 0,b = 2</equation>，从而<equation>a_1 = 0,b_1 = 2</equation>.应选A.

（法三）将选项A、B、C、D的值分别代入<equation>\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，得到<equation>\int_ {- \pi} ^ {\pi} (x - 2 \sin x) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} - 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \sin x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {2} (\pi - 2),</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {3}.</equation>由于<equation>\frac{2}{3}\pi^{3}-4\pi<\frac{2}{3}\pi^{3}+4\pi<\frac{2}{3}\pi^{3}+4\pi^{2}(\pi-2)<\frac{2}{3}\pi^{3}+4\pi^{3}</equation>，故选A.

---

**2014年第10题 | 填空题 | 4分**
10. 设<equation>f(x)</equation>是周期为4的可导奇函数,且<equation>f^{\prime}(x)=2(x-1),x\in[0,2]</equation>,则<equation>f(7)=</equation>___.
**解析: **由于<equation>f ( x )</equation>是周期为4的函数，且<equation>7=2\times4-1</equation>，故<equation>f ( 7 ) = f (-1).</equation>(a)

(b)

（法一）由 f(x)为奇函数可得<equation>f(0)=0</equation>.由当<equation>x\in[0,2]</equation>时，<equation>f^{\prime}(x)=2(x-1)</equation>可得， f(x)在 [0,2]上的表达式为<equation>f (x) = \int_ {0} ^ {x} 2 (t - 1) \mathrm {d} t + f (0) = x ^ {2} - 2 x = (x - 1) ^ {2} - 1.</equation>于是<equation>f(1) = -1.</equation>由<equation>f(x)</equation>为奇函数得，<equation>f(-1) = -f(1) = 1</equation>，即<equation>f(7) = 1.</equation>（法二）由 f(x)为奇函数可知，<equation>f(x)=-f(-x).</equation>在等式两端求导得<equation>f^{\prime}(x)=f^{\prime}(-x),</equation>从而<equation>f^{\prime}(x)</equation>为偶函数，<equation>f^{\prime}(x)</equation>的图像关于y轴对称.在[0，2]上，<equation>f^{\prime}(x)=2(x-1),</equation>为一条过点（0，-2）和点（1，0）的直线。由此可知，在[-2，0]上，<equation>y=f^{\prime}(x)</equation>为过点（0，-2）和点（-1，0）的直线，可求得<equation>f^{\prime}(x)=-2(x+1).</equation>从而，<equation>f(x)</equation>在[-2，0]上为<equation>f (x) = \int_ {0} ^ {x} - 2 (t + 1) \mathrm {d} t + f (0) = - x ^ {2} - 2 x = - (x + 1) ^ {2} + 1.</equation>因此，<equation>f(-1)=1</equation>，即<equation>f(7)=1.</equation>

---

**2013年第15题 | 解答题 | 10分**
15. (本题满分10分)

计算<equation>\int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x, \text {其 中} f (x) = \int_ {1} ^ {x} \frac {\ln (t + 1)}{t} \mathrm {d} t.</equation>
**解析: **解（法一）由题设知，<equation>f^{\prime}(x) = \frac{\ln(x + 1)}{x}, x\in(0,1],</equation>且<equation>f(1)=0</equation>，于是<equation>\begin{aligned} \int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {0} ^ {1} f (x) \mathrm {d} (\sqrt {x}) = 2 \left[ \sqrt {x} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \sqrt {x} f ^ {\prime} (x) \mathrm {d} x \right] \right. \\ &= 0 - 2 \int_ {0} ^ {1} \sqrt {x} \cdot \frac {\ln (x + 1)}{x} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (x + 1)}{\sqrt {x}} \mathrm {d} x \\ &= - 4 \int_ {0} ^ {1} \ln (x + 1) \mathrm {d} (\sqrt {x}) \\ &= - 4 \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ \underline {{= - 4}} \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ &= - 4 \ln 2 + 4 \int_ {0} ^ {1} \frac {t}{t ^ {2} + 1} \cdot 2 t \mathrm {d} t \\ &= - 4 \ln 2 + 8 \int_ {0} ^ {1} \left(1 - \frac {1}{t ^ {2} + 1}\right) \mathrm {d} t \\ &= - 4 \ln 2 + 8 \left(t - \arctan t\right) \Bigg | _ {0} ^ {1} \\ &= - 4 \ln 2 + 8 - 2 \pi . \end{aligned}</equation><equation>\begin{array}{l} \frac {\text {交换 积 分}}{\text {次 序}} - \int_ {0} ^ {1} \mathrm {d} t \int_ {0} ^ {t} \frac {\ln (t + 1)}{t} \cdot \frac {1}{\sqrt {x}} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (t + 1)}{\sqrt {t}} \mathrm {d} t \\ \underline {{\text {同 法 一}}} - 4 \ln 2 + 8 - 2 \pi . \\ \end{array}</equation>

---

**2012年第10题 | 填空题 | 4分**
<equation>1 0. \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解<equation>\sqrt{2 x-x^{2}}=\sqrt{1-(x-1)^{2}}.</equation>令 t=x-1，则有<equation>\begin{aligned} \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x &= \int_ {- 1} ^ {1} (t + 1) \sqrt {1 - t ^ {2}} \mathrm {d} t = \int_ {- 1} ^ {1} t \sqrt {1 - t ^ {2}} \mathrm {d} t + \int_ {- 1} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\text {对称性}}} 0 + 2 \int_ {0} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\underline {{t = \sin \theta}}}} 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{2}} (1 + \cos 2 \theta) \mathrm {d} \theta = \frac {\pi}{2}. \end{aligned}</equation>

---

**2010年第10题 | 填空题 | 4分**
10.
**解析: **<equation>\begin{aligned} \int_ {0} ^ {\pi^ {2}} \sqrt {x} \cos \sqrt {x} \mathrm {d} x \stackrel {t = \sqrt {x}} {=} \int_ {0} ^ {\pi} t \cos t \mathrm {d} \left(t ^ {2}\right) \\ &= \int_ {0} ^ {\pi} 2 t ^ {2} \cos t \mathrm {d} t = \int_ {0} ^ {\pi} 2 t ^ {2} \mathrm {d} (\sin t) \\ \underline {{\mathrm {分 部 积 分}}} (\sin t \cdot 2 t ^ {2}) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 t \sin t \mathrm {d} t &= \int_ {0} ^ {\pi} 4 t \mathrm {d} (\cos t) \right. \\ \underline {{\mathrm {分 部 积 分}}} (\cos t \cdot 4 t) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 \cos t \mathrm {d} t &= - 4 \pi . \right. \end{aligned}</equation>

---


#### 变限积分


**2024年第1题 | 选择题 | 5分 | 答案: C**
1. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{\cos t} \mathrm{d} t,g ( x )=\int_{0}^{\sin x} \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则（    )

A. f(x)是奇函数，g(x)是偶函数 B. f(x)是偶函数，g(x)是奇函数

C. f(x)与 g(x)均为奇函数 D. f(x)与 g(x)均为周期函数
答案: C
**解析: **解 由于<equation>\mathrm{e}^{\cos t}</equation>是偶函数，且<equation>f(0)=0</equation>，故由分析中的结论可得<equation>f(x)=\int_{0}^{x}\mathrm{e}^{\cos t}\mathrm{d}t</equation>是奇函数.同理，<equation>h(x)=\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t</equation>也是奇函数.

注意到<equation>g ( x )=h (\sin x)</equation>，故<equation>g (- x) = h (\sin (- x)) = h (- \sin x) = - h (\sin x) = - g (x).</equation>于是，<equation>g ( x )</equation>也是奇函数.

因此，应选C.

下面说明选项 D 不正确.

由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故<equation>g (x + 2 \pi) = \int_ {0} ^ {\sin (x + 2 \pi)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {\sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = g (x).</equation>于是，<equation>g ( x )</equation>也是周期为<equation>2 \pi</equation>的周期函数.但是，由于<equation>f^{\prime}(x)=\mathrm{e}^{\cos x}>0</equation>，故f(x）单调增加，从而f(x)不可能为周期函数.

也可以直接验证<equation>f(-x)=-f(x), g(-x)=-g(x)</equation>，从而得到它们均为奇函数.<equation>f (- x) = \int_ {0} ^ {- x} \mathrm {e} ^ {\cos t} \mathrm {d} t \underline {{= u = - t}} - \int_ {0} ^ {x} \mathrm {e} ^ {\cos (- u)} \mathrm {d} u = - \int_ {0} ^ {x} \mathrm {e} ^ {\cos u} \mathrm {d} u = - f (x),</equation><equation>g (- x) = \int_ {0} ^ {\sin (- x)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {- \sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \xlongequal {u = - t} - \int_ {0} ^ {\sin x} \mathrm {e} ^ {(- u) ^ {2}} \mathrm {d} u = - \int_ {0} ^ {\sin x} \mathrm {e} ^ {u ^ {2}} \mathrm {d} u = - g (x).</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.
答案: D
**解析: **解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0，2），（2，3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在[-1,0）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（0，1）上，<equation>f ( x ) < 0</equation>，故 F(x)单调减少；在（1，2）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（2，3]上，<equation>f ( x ) = 0</equation>，故 F(x)为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D. 应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1，3]上有界且只有两个间断点，f(x)在[-1，3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 定积分的概念、性质及几何意义


**2022年第4题 | 选择题 | 5分 | 答案: A**

4. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)}\mathrm{d}x,I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x}\mathrm{d}x,I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x}\mathrm{d}x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>

答案: A

**解析:**解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x)>\frac{x}{2},\frac{\ln(1+x)}{1+\cos x}>\frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>.

此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} > x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x}<\frac{x}{1+\cos x}<x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x>\frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2021年第4题 | 选择题 | 5分 | 答案: B**

4. 设函数 f(x)在区间[0,1]上连续，则<equation>\int_{0}^{1} f(x)\mathrm{d}x=</equation>(    )

A.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}</equation>B.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}</equation>C.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}</equation>D.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}</equation>

答案: B

**解析:**解 由于 f(x)连续，故<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在，从而可对区间[0，1]进行划分，将该积分写为 n项和式的极限.

将[0，1]分为n等份，每个小区间为<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation><equation>k=1,2,\dots,n</equation>从<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation>中取点<equation>\frac{2k-1}{2n}</equation>故由<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在以及定积分的定义可得<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} f \left(\frac {2 k - 1}{2 n}\right) \cdot \frac {1}{n}.</equation>因此，应选B.

下面说明选项A、C、D均不正确.

选项A：<equation>\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{2n} = \frac{1}{2}\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{n} = \frac{1}{2}\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项C：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{n} = 2\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{2n} = 2\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项D：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n} = 4\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{1}{2n} = 4\int_{0}^{1}f(x)\mathrm{d}x.</equation>

---

**2018年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x</equation>，<equation>N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x</equation>，<equation>K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A.<equation>M>N>K</equation>B.<equation>M>K>N</equation>C.<equation>K>M>N</equation>D.<equation>K>N>M</equation>

答案: C

**解析:**解分别计算 M,N,K.

由于<equation>\frac{2x}{1 + x^2}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1 + x^2}\mathrm{d}x = 0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \xlongequal {\frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{}} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x} > 1 + x.</equation>于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{\mathrm{e}^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第16题 | 解答题 | 10分**

16. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>

**解析:**解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) &= \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ &= \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\text {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {x ^ {2}}{2 (1 + x)} d x \right. \\ &= \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>I_{k}=\int_{0}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则有（    ）

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{3}<I_{2}<I_{1}</equation>C.<equation>I_{2}<I_{3}<I_{1}</equation>D.<equation>I_{2}<I_{1}<I_{3}</equation>

答案: D

**解析:**解（法一）记<equation>J_{k}=\int_{(k-1)\pi}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则<equation>I _ {1} = J _ {1}, \quad I _ {2} = J _ {1} + J _ {2}, \quad I _ {3} = J _ {1} + J _ {2} + J _ {3}.</equation>由于<equation>\mathrm{e}^{x^{2}} > 0</equation>，且在（0，<equation>\pi</equation>）上，<equation>\sin x > 0</equation>；在（<equation>\pi,2\pi</equation>）上，<equation>\sin x < 0</equation>；在（<equation>2\pi,3\pi</equation>）上，<equation>\sin x > 0</equation>，故<equation>J_{1}>0</equation>，<equation>J_{2}<0</equation>，<equation>J_{3}>0</equation>.由此可得，<equation>I_{1}>I_{2}</equation>，<equation>I_{3}>I_{2}</equation>.

下面比较<equation>I_{1}</equation>和<equation>I_{3}.</equation><equation>I _ {3} - I _ {1} = J _ {2} + J _ {3}.</equation><equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x > \mathrm {e} ^ {(2 \pi) ^ {2}} \int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x,</equation><equation>\left| J _ {2} \right| = \left| \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \right| < \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|, \quad J _ {2} > - \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|.</equation>由定积分的几何意义可知，<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x</equation>和<equation>|\int_{\pi}^{2\pi}\sin x\mathrm{d}x|</equation>分别为<equation>\sin x</equation>在<equation>(2\pi ,3\pi)</equation>上以及在<equation>(\pi ,2\pi)</equation>上的部分与<equation>x</equation>轴围成的图形面积.根据<equation>\sin x</equation>的图形，这两部分面积相等，即<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x = \left|\int_{\pi}^{2\pi}\sin x\mathrm{d}x\right|.</equation>于是，

于是，<equation>J _ {2} + J _ {3} > \mathrm {e} ^ {(2 \pi) ^ {2}} \left(\int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x - \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|\right) = 0,</equation>即<equation>I_{3} > I_{1}.</equation>因此，<equation>I_{2} < I_{1} < I_{3}</equation>应选D.

（法二）在法一中，证明<equation>J_{2} + J_{3} > 0</equation>，也可以使用如下方法.<equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \xlongequal {u = x - \pi} \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin (u + \pi) \mathrm {d} u = - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin u \mathrm {d} u,</equation><equation>J _ {2} + J _ {3} = \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(x + \pi) ^ {2}} \sin x \mathrm {d} x = \int_ {\pi} ^ {2 \pi} \sin x \left[ \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {(x + \pi) ^ {2}} \right] \mathrm {d} x.</equation>当<equation>x\in (\pi ,2\pi)</equation>时，<equation>\sin x < 0,\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2} < 0,\sin x[\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2}] > 0</equation>，从而<equation>J_{2} + J_{3} > 0.</equation>其余同法一.

---

**2011年第4题 | 选择题 | 4分 | 答案: B**

4. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I,J,K的大小关系为（    )

A. I<J<K B. I<K<J C. J<I<K D. K<J<I

答案: B

**解析:**解 当 0 < x <<equation>\frac{\pi}{4}</equation>时，0 < sin x < cos x < 1 < cot x.又 f(t) = ln t在（0，+<equation>\infty</equation>）上单调增加，故当 0 < x <<equation>\frac{\pi}{4}</equation>时，<equation>\ln(\sin x) < \ln(\cos x) < \ln(\cot x)</equation>，从而由积分的保号性可知， I < K < J ，选B.

---

**2010年第17题 | 解答题 | 10分**

17. (本题满分10分)

17. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>

**答案:**(17) （I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>，理由略；（Ⅱ）<equation>\lim_{n\to\infty}u_{n}=0.</equation>

**解析:**解（I）在（0，1]上，<equation>|\ln t|</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑 f（t）=<equation>\ln(1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t \in [0,1]</equation>时，<equation>\ln (1 + t) \leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}(t\ln t) = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \left| _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right)\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


#### 反常积分的计算与敛散性


**2021年第11题 | 填空题 | 5分**

<equation>\int_ {0} ^ {+ \infty} \frac {1}{x ^ {2} + 2 x + 2} \mathrm {d} x = \underline {{}}</equation>

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**将<equation>x^{2}+2 x+2</equation>配方.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{x ^ {2} + 2 x + 2} &= \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{(x + 1) ^ {2} + 1} = \int_ {0} ^ {+ \infty} \frac {\mathrm {d} (x + 1)}{(x + 1) ^ {2} + 1} = \arctan (x + 1) \Big | _ {0} ^ {+ \infty} \\ &= \frac {\pi}{2} - \arctan 1 = \frac {\pi}{2} - \frac {\pi}{4} = \frac {\pi}{4}. \end{aligned}</equation>

---

**2016年第1题 | 选择题 | 4分 | 答案: C**

1. 若反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>收敛，则（    )

A. a < 1且b > 1 B. a > 1且b > 1 C. a < 1且a+b > 1 D. a > 1且a+b > 1

答案: C

**解析:**解 由于被积函数<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>在<equation>[0,+\infty)</equation>上可能的瑕点为<equation>x=0</equation>，故将反常积分分为两部分，即<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x=\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x+\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x.</equation>对于积分<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，若<equation>a\leqslant0</equation>，则该积分为正常的定积分；若<equation>a>0</equation>，则<equation>x=0</equation>为被积函数的瑕点.

由于<equation>\lim_{x\rightarrow 0^{+}}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a}}}=\lim_{x\rightarrow 0^{+}}\frac{1}{(1+x)^{b}}=1</equation>，故当<equation>x\rightarrow 0^{+}</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a}}</equation>等价. 瑕积分<equation>\int_{0}^{1}\frac{1}{x^{a}}\mathrm{d}x</equation>当且仅当<equation>0<a<1</equation>时收敛，加上<equation>a\leqslant0</equation>时的情况，<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a<1</equation>时收敛.

对于反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，由于<equation>\lim_{x\rightarrow+\infty}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a+b}}}=\lim_{x\rightarrow+\infty}\left(\frac{x}{1+x}\right)^{b}=1</equation>，故当<equation>x\rightarrow+\infty</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a+b}}</equation>等价. 反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a+b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛，故<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛.

综上所述，反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}</equation>收敛当且仅当 a,b满足 a < 1 且 a+b > 1，应选 C.

---

**2013年第12题 | 填空题 | 4分**

<equation>2. \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**答案:**## ln 2.

**解析:**<equation>\begin{aligned} { } ^ { + \infty } \frac {\ln x}{( 1 + x ) ^ { 2 } } \mathrm { d } x &= - \int _ { 1 } ^ { + \infty } \ln x \mathrm { d } \left( \frac { 1 } { 1 + x } \right) = - \left[ \left. \frac {\ln x}{1 + x} \right| _ { 1 } ^ { + \infty } - \int _ { 1 } ^ { + \infty } \frac { 1 } { x ( 1 + x ) } \mathrm { d } x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Bigg | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>
