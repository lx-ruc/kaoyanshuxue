# 数学一

## 高等数学

### 多元函数积分学

#### 旋度的定义

**2018年第11题 | 填空题 | 4分**

11. 设<equation>F(x,y,z)= xy i-yz j+z x k</equation>, 则<equation>\mathbf{rot} F(1,1,0)=</equation>___

**答案:**i-k.

**解析:**根据旋度的定义，<equation>\operatorname {r o t} F (x, y, z) = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ x y & - y z & z x \end{array} \right| = y i - z j - x k.</equation>代入<equation>(x,y,z) = (1,1,0)</equation>，可得<equation>\mathbf{rot} F(1,1,0) = i - k.</equation>

---

**2016年第10题 | 填空题 | 4分**

10. 向量场<equation>A(x,y,z) = (x+y+z)i+xyj+zk</equation>的旋度<equation>\mathbf{rot}A =</equation>___

**答案:**j + (y-1) k.

**解析:**令<equation>P= x+y+z, Q= x y, R=z</equation>，由旋度的定义知<equation>\mathbf{r o t} A=\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\right) i+\left(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\right) j+\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) k=j+(y-1) k.</equation>

---


#### 第一类曲线积分

**2018年第12题 | 填空题 | 4分**

12. 设 L为球面<equation>x^{2}+y^{2}+z^{2}=1</equation>与平面<equation>x+y+z=0</equation>的交线，则<equation>\oint_{L} xy\mathrm{d}s=</equation>___

**解析:**本题中，曲线<equation>L</equation>具有轮换对称性，故应利用轮换对称性来简化计算.

解 曲线 L如图所示.

由曲线<equation>L</equation>的方程可知，该曲线对变量<equation>x, y, z</equation>具有轮换对称性.于是，<equation>\oint_ {L} x y \mathrm {d} s = \oint_ {L} y z \mathrm {d} s = \oint_ {L} z x \mathrm {d} s = \frac {1}{3} \oint_ {L} (x y + y z + z x) \mathrm {d} s.</equation>又因为<equation>x y+y z+z x=\frac{1}{2} \left[ \left(x+y+z\right)^{2}-\left(x^{2}+y^{2}+z^{2}\right) \right]</equation>，所以<equation>\begin{aligned} \oint_ {L} x y \mathrm {d} s &= \frac {1}{3} \oint_ {L} \left(x y + y z + z x\right) \mathrm {d} s = \frac {1}{6} \oint_ {L} \left[ \left(x + y + z\right) ^ {2} - \left(x ^ {2} + y ^ {2} + z ^ {2}\right) \right] \mathrm {d} s \\ \frac {x + y + z = 0}{x ^ {2} + y ^ {2} + z ^ {2} = 1} \frac {1}{6} \oint_ {L} (0 - 1) \mathrm {d} s &= - \frac {1}{6} \oint_ {L} \mathrm {d} s. \end{aligned}</equation>由于 L为单位球面上的一个大圆，即以球心为圆心，且半径等于球半径的一个圆，故<equation>\oint_{L}\mathrm{d}s=L</equation>的周长<equation>= 2\pi.</equation>因此，原积分<equation>= -\frac{1}{6}\times 2\pi = -\frac{\pi}{3}.</equation>

---

**2009年第11题 | 填空题 | 4分**

11. 已知曲线<equation>L: y=x^{2}(0\leqslant x\leqslant\sqrt{2})</equation>，则<equation>\int_{L}x\mathrm{d}s=</equation>___

**答案:**# 13 6.

**解析:**由题设知，<equation>\begin{aligned} \int_ {L} x \mathrm {d} s &= \int_ {0} ^ {\sqrt {2}} x \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {0} ^ {\sqrt {2}} x \sqrt {1 + 4 x ^ {2}} \mathrm {d} x \\ &= \frac {1}{8} \int_ {0} ^ {\sqrt {2}} \sqrt {1 + 4 x ^ {2}} \mathrm {d} \left(4 x ^ {2} + 1\right) = \frac {1}{8} \cdot \frac {2}{3} \left(1 + 4 x ^ {2}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {\sqrt {2}} = \frac {1 3}{6}. \end{aligned}</equation>

---


#### 第一类曲面积分

**2017年第19题 | 解答题 | 10分**

19. (本题满分10分)

设薄片型物体 S是圆雉面<equation>z=\sqrt{x^{2}+y^{2}}</equation>被柱面<equation>z^{2}=2 x</equation>割下的有限部分，其上任一点的密度为<equation>\mu(x,y,z)=</equation><equation>9 \sqrt{x^{2}+y^{2}+z^{2}}.</equation>记圆雉面与柱面的交线为 C.

I. 求 C在 xOy平面上的投影曲线的方程；

II. 求 S的质量 M.

**答案:**<equation>\begin{array}{l} (\mathrm {I}) \left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 x, \\ z = 0; \end{array} \right. \\ (\mathrm {I I}) 6 4. \\ \end{array}</equation>

**解析:**解（I）由题设知，圆锥面与柱面的交线 C的方程为<equation>\left\{\begin{array}{l l}z=\sqrt{x^{2}+y^{2}},\\ z^{2}=2 x, \end{array} \right.</equation>消去 z得到<equation>x^{2}+y^{2}= 2 x</equation>，于是 C在 xOy平面上的投影曲线的方程为<equation>\left\{ \begin{array}{l} x ^ {2} + y ^ {2} = 2 x, \\ z = 0. \end{array} \right.</equation>（Ⅱ）设<equation>D_{xy}=\{(x,y)|x^{2}+y^{2}\leqslant 2x\}</equation>，则曲面 S的方程为<equation>z=\sqrt{x^{2}+y^{2}},(x,y)\in D_{xy}</equation>，从而 S的质量为<equation>\begin{aligned} M &= \iint_ {S} \mu (x, y, z) \mathrm {d} S = \iint_ {S} 9 \sqrt {x ^ {2} + y ^ {2} + z ^ {2}} \mathrm {d} S \xlongequal {z = \sqrt {x ^ {2} + y ^ {2}}} \iint_ {S} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \mathrm {d} S \\ &= \iint_ {D _ {x y}} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \cdot \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} 9 \sqrt {2 \left(x ^ {2} + y ^ {2}\right)} \cdot \sqrt {1 + \left(\frac {x}{\sqrt {x ^ {2} + y ^ {2}}}\right) ^ {2} + \left(\frac {y}{\sqrt {x ^ {2} + y ^ {2}}}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= 1 8 \iint_ {D _ {x y}} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y. \end{aligned}</equation>令<equation>x = r\cos \theta ,y = r\sin \theta</equation>，由<equation>x^{2} + y^{2}\leqslant 2x</equation>知，<equation>r^{2}\leqslant 2r\cos \theta</equation>，即<equation>r\leqslant 2\cos \theta</equation>.如下图，<equation>D_{xy}</equation>在极坐标

变换下对应区域<equation>D = \left\{(r,\theta)\mid 0\leqslant r\leqslant 2\cos \theta , - \frac{\pi}{2}\leqslant \theta \leqslant \frac{\pi}{2}\right\}</equation>，从而<equation>\begin{aligned} M &= 1 8 \iint_ {D _ {x y}} \sqrt {x ^ {2} + y ^ {2}} \mathrm {d} x \mathrm {d} y = 1 8 \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} \theta \int_ {0} ^ {2 \cos \theta} r \cdot r \mathrm {d} r \\ &= 4 8 \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta = 9 6 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {3} \theta \mathrm {d} \theta \\ &= 9 6 \times \frac {2}{3} = 6 4. \end{aligned}</equation>

---

**2012年第12题 | 填空题 | 4分**

12. 设<equation>\Sigma=\{(x,y,z)\mid x+y+z=1,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>，则<equation>\iint\limits_{\Sigma}y^{2}\mathrm{d}S=</equation>___

**答案:**#<equation>\frac{\sqrt{3}}{12}</equation>

**解析:**分析 本题主要考查第一类曲面积分的计算. 一般将其化为重积分后再计算.

若曲面<equation>\Sigma</equation>的方程为<equation>z = z(x,y),(x,y)\in D_{xy}</equation>，且<equation>z(x,y)</equation>在<equation>D_{xy}</equation>上有连续偏导数，<equation>f(x,y,z)</equation>在<equation>\Sigma</equation>上连续，则<equation>\iint_ {\Sigma} f (x, y, z) \mathrm {d} S = \iint_ {D _ {x y}} f (x, y, z (x, y)) \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y.</equation>解 曲面<equation>\varSigma=\{(x,y,z)\mid z=1-x-y,x\geqslant0,y\geqslant0,z\geqslant0\}</equation>在 xOy平面上的投影区域为<equation>D_{xy}=\{(x,y)\mid 0\leqslant y\leqslant1,0\leqslant x\leqslant1-y\}</equation>，于是<equation>\begin{aligned} \iint_ {\Sigma} y ^ {2} \mathrm {d} S &= \iint_ {D _ {x y}} y ^ {2} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} y ^ {2} \sqrt {1 + 1 + 1} \mathrm {d} x \mathrm {d} y = \sqrt {3} \iint_ {D _ {x y}} y ^ {2} \mathrm {d} x \mathrm {d} y \\ &= \sqrt {3} \int_ {0} ^ {1} y ^ {2} \mathrm {d} y \int_ {0} ^ {1 - y} \mathrm {d} x = \sqrt {3} \int_ {0} ^ {1} y ^ {2} (1 - y) \mathrm {d} y = \frac {\sqrt {3}}{1 2}. \end{aligned}</equation>

---

**2010年第19题 | 解答题 | 10分**

19. (本题满分10分)

设 P为椭球面 S：<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>上的动点，若 S在点 P处的切平面与 xOy面垂直，求点 P的轨迹 C，并计算曲面积分 I =<equation>\iint\limits_{\Sigma}\frac{(x+\sqrt{3})|y-2z|}{\sqrt{4+y^{2}+z^{2}-4yz}} \mathrm{d} S</equation>，其中<equation>\varSigma</equation>是椭球面 S位于曲线 C上方的部分.

**答案:**(19) 点P的轨迹C为<equation>\left\{\begin{array}{l l}x^{2}+y^{2}+z^{2}-yz=1\\ y=2z,\end{array}\right.</equation>或者<equation>\left\{\begin{array}{l l}x^{2}+\frac{3}{4} y^{2}=1\\ y=2z,\end{array}\right.</equation>曲面积分为<equation>I=2\pi.</equation>

**解析:**解设点 P的坐标为（x,y,z），则椭球面 S在点 P处的法向量为（2x，2y-z，2z-y）.又 xOy面的法向量可取为（0,0,1），故由 S在点 P处的切平面与 xOy面垂直知，<equation>(2 x, 2 y - z, 2 z - y) \cdot (0, 0, 1) = 0,</equation>即有<equation>y = 2z</equation>. 由于点<equation>P</equation>在椭球面<equation>S</equation>上，故点<equation>P</equation>的轨迹<equation>C</equation>为<equation>\left\{ \begin{array}{l l} x ^ {2} + y ^ {2} + z ^ {2} - y z = 1, \\ y = 2 z, \end{array} \right. \text {或 者} \left\{ \begin{array}{l l} x ^ {2} + \frac {3}{4} y ^ {2} = 1, \\ y = 2 z. \end{array} \right.</equation>下面用两种方法求曲面积分 I.

（法一）<equation>\varSigma</equation>在xOy面上的投影区域为<equation>D_{xy}=\left\{(x,y)\mid x^{2}+\frac{3}{4} y^{2}\leqslant 1\right\}</equation>，其面积为<equation>\pi \cdot 1\cdot \frac{2}{\sqrt{3}}=\frac{2}{\sqrt{3}}\pi.</equation>对方程<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>两边关于x,y分别求偏导数，得<equation>2 x + 2 z \frac {\partial z}{\partial x} - y \frac {\partial z}{\partial x} = 0, \quad 2 y + 2 z \frac {\partial z}{\partial y} - z - y \frac {\partial z}{\partial y} = 0,</equation>解得<equation>\frac{\partial z}{\partial x} = \frac{2x}{y - 2z},\frac{\partial z}{\partial y} = \frac{2y - z}{y - 2z}</equation>. 在<equation>\varSigma</equation>上，<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>，故<equation>\begin{aligned} \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} &= \frac {\sqrt {4 x ^ {2} + 5 y ^ {2} + 5 z ^ {2} - 8 y z}}{| y - 2 z |} = \frac {\sqrt {4 \left(x ^ {2} + y ^ {2} + z ^ {2} - y z\right) + y ^ {2} + z ^ {2} - 4 y z}}{| y - 2 z |} \\ &= \frac {\sqrt {4 + y ^ {2} + z ^ {2} - 4 y z}}{| y - 2 z |}. \end{aligned}</equation>从而<equation>\begin{aligned} I &= \iint_ {\Sigma} \frac {\left(x + \sqrt {3}\right) \mid y - 2 z \mid}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \mathrm {d} S = \iint_ {D _ {x y}} \frac {\left(x + \sqrt {3}\right) \mid y - 2 z \mid}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \cdot \sqrt {1 + \left(\frac {\partial z}{\partial x}\right) ^ {2} + \left(\frac {\partial z}{\partial y}\right) ^ {2}} \mathrm {d} x \mathrm {d} y \\ &= \iint_ {D _ {x y}} \left(x + \sqrt {3}\right) \mathrm {d} x \mathrm {d} y \stackrel {\text {对 称 性}} {=} 0 + \iint_ {D _ {x y}} \sqrt {3} \mathrm {d} x \mathrm {d} y = \sqrt {3} \cdot \frac {2}{\sqrt {3}} \pi = 2 \pi . \end{aligned}</equation>（法二）<equation>\varSigma</equation>在 xOy面上的投影区域为<equation>D_{xy}=\left\{(x,y)\left|x^{2}+\frac{3}{4} y^{2}\leqslant 1\right.\right\}</equation>，其面积为<equation>\pi\cdot1\cdot\frac{2}{\sqrt{3}}=\frac{2}{\sqrt{3}}\pi.</equation><equation>\varSigma</equation>上任一点的法向量为（2x，2y-z，2z-y），其方向余弦<equation>\cos \gamma</equation>满足<equation>| \cos \gamma | = \frac {\left| 2 z - y \right|}{\sqrt {\left(2 x\right) ^ {2} + \left(2 y - z\right) ^ {2} + \left(2 z - y\right) ^ {2}}} = \frac {\left| 2 z - y \right|}{\sqrt {4 x ^ {2} + 5 y ^ {2} + 5 z ^ {2} - 8 y z}}.</equation>又<equation>\Sigma</equation>上的点满足<equation>x^{2}+y^{2}+z^{2}-yz=1</equation>，故有<equation>|\cos \gamma |=\frac{|2z-y|}{\sqrt{4+y^{2}+z^{2}-4yz}}</equation>，从而<equation>\begin{aligned} I &= \iint_ {\Sigma} \frac {(x + \sqrt {3}) | y - 2 z |}{\sqrt {4 + y ^ {2} + z ^ {2}} - 4 y z} \mathrm {d} S = \iint_ {\Sigma} (x + \sqrt {3}) | \cos \gamma | \mathrm {d} S \\ &= \iint_ {D _ {x y}} (x + \sqrt {3}) \mathrm {d} x \mathrm {d} y \xlongequal {\text {对称性}} 0 + \iint_ {D _ {x y}} \sqrt {3} \mathrm {d} x \mathrm {d} y \\ &= \sqrt {3} \cdot \frac {2}{\sqrt {3}} \pi = 2 \pi . \end{aligned}</equation>

---


#### 重积分的概念与性质

**2010年第4题 | 选择题 | 4分 | 答案: D**

4.<equation>\lim_{n\rightarrow \infty}\sum_{i=1}^{n}\sum_{j=1}^{n}\frac{n}{(n+i)(n^{2}+j^{2})}=</equation>(    )

A.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>B.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>C.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y)}\mathrm{d}y</equation>D.<equation>\int_{0}^{1}\mathrm{d}x\int_{0}^{1}\frac{1}{(1+x)(1+y^{2})}\mathrm{d}y</equation>

答案: D

**解析:**解 （法一）考虑将原极限写成二重积分.

令<equation>\Delta \sigma_{ij} = \left[\frac{i - 1}{n},\frac{i}{n}\right]\times \left[\frac{j - 1}{n},\frac{j}{n}\right](i,j = 1,2,\dots ,n)</equation>，则<equation>\{\Delta \sigma_{ij}\}_{1\leqslant i,j\leqslant n}</equation>为<equation>D = [0,1]\times [0,1]</equation>上的一个划分，<equation>\Delta \sigma_{ij}</equation>的面积为<equation>\frac{1}{n^2}</equation>.取<equation>\Delta \sigma_{ij}</equation>上的一点<equation>\left(\frac{i}{n},\frac{j}{n}\right)</equation>.

由于<equation>\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right) \left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \cdot \frac {1}{n ^ {2}},</equation>故<equation>\begin{aligned} \text {原 极 限} &= \lim _ {n \rightarrow \infty} \left[ \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {1}{\left(1 + \frac {i}{n}\right)\left(1 + \frac {j ^ {2}}{n ^ {2}}\right)} \right] = \iint_ {D} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} \sigma \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

（法二）由于所求极限的表达式中 i，j无关，故可以考虑将原极限写成定积分的乘积.由于<equation>\begin{aligned} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \frac {n}{(n + i) \left(n ^ {2} + j ^ {2}\right)} &= \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) \\ \underline {{i , j \text {无关}}} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right), \end{aligned}</equation>故<equation>\begin{aligned} &= \lim _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \left(\frac {1}{1 + \frac {i}{n}} \cdot \frac {1}{n}\right) \cdot \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} \left(\frac {1}{1 + \frac {j ^ {2}}{n ^ {2}}} \cdot \frac {1}{n}\right) = \left(\int_ {0} ^ {1} \frac {1}{1 + x} \mathrm {d} x\right)\left(\int_ {0} ^ {1} \frac {1}{1 + y ^ {2}} \mathrm {d} y\right) \\ &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {1} \frac {1}{(1 + x) \left(1 + y ^ {2}\right)} \mathrm {d} y. \end{aligned}</equation>应选 D.

---

**2009年第2题 | 选择题 | 4分 | 答案: A**

2. 如图，正方形<equation>\{(x,y)\mid|x|\leqslant1,|y|\leqslant1\}</equation>被其对角线划分为四个区域<equation>D_{k}(k=1,2,3,4),I_{k}=\iint_{D_{k}}y\cos x\mathrm{d}x\mathrm{d}y</equation>则<equation>\max_{1\leqslant k\leqslant4}\{I_{k}\}=</equation>（    ）

A.<equation>I_{1}</equation>B.<equation>I_{2}</equation>C.<equation>I_{3}</equation>D.<equation>I_{4}</equation>

答案: A

**解析:**解 令<equation>f ( x,y)=y \cos x</equation>，由于<equation>D_{4}</equation>关于x轴对称，且<equation>f ( x,y)=-f ( x,-y)</equation>，故<equation>I_{4}=0</equation>.同理得到<equation>I_{2}=0</equation>.又<equation>f ( x,y)</equation>在<equation>D_{1}</equation>内部恒大于0，在<equation>D_{3}</equation>内部恒小于0，故由重积分的保号性知，<equation>I_{1}>0, I_{3}<0.</equation>综上所述，<equation>\max_{1\leq k\leq 4}\left\{I_{k}\right\}=I_{1}</equation>应选A.

---


### 函数、极限、连续
#### 函数极限的计算

**2025年第11题 | 填空题 | 5分**

<equation>1 1. \lim _ {x \rightarrow 0 ^ {+}} \frac {x ^ {x} - 1}{\ln x \cdot \ln (1 - x)} = \underline {{}}</equation>

**解析:**解 由于<equation>x^{x}=\mathrm{e}^{x\ln x}</equation>，且当<equation>x\to0</equation>时，<equation>\mathrm{e}^{x}-1\sim x</equation>，故<equation>\lim_{x\to0^{+}}\frac{x^{x}-1}{\ln x\cdot\ln(1-x)}=\lim_{x\to0^{+}}\frac{\mathrm{e}^{x\ln x}-1}{\ln x\cdot\ln(1-x)} \frac{\mathrm{e}^{x\ln x}-1\sim x\ln x}{\ln(1-x)\sim-x} \lim_{x\to0^{+}}\frac{x\ln x}{\ln x\cdot(-x)}=-1.</equation>

---

**2021年第17题 | 解答题 | 10分**

17. (本题满分10分)

求极限 lim<equation>\left(\frac {1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{\mathrm {e} ^ {x} - 1} - \frac {1}{\sin x}\right)</equation>

**解析:**解 （法一）先整理原极限再计算.<equation>\begin{array}{l} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t}{x} + \lim _ {x \rightarrow 0} \frac {\sin x - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \frac {\text {洛必达}}{} \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {x ^ {2}}}{1} + \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {3}}{6} - 1 - x - \frac {x ^ {2}}{2} + 1 + o \left(x ^ {2}\right)}{x ^ {2}} \\ = 1 + \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)}{x ^ {2}} = 1 - \frac {1}{2} = \frac {1}{2}. \\ \end{array}</equation>因此，原极限<equation>= \frac{1}{2}</equation>（法二）将原极限通分整理，化为<equation>\frac{0}{0}</equation>型未定式后再应用洛必达法则.<equation>\begin{aligned} \mathrm {原 极 限} &= \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \sin x} \\ \frac {\mathrm {e} ^ {x} - 1 \sim x}{\sin x \sim x} \lim _ {x \rightarrow 0} \frac {\sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {\cos x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2 x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \sin x \left(1 + \int_ {0} ^ {x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t\right) + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + \cos x \cdot \mathrm {e} ^ {x ^ {2}} + 2 x \cdot \sin x \cdot \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {x}}{2} &= \frac {1}{2}. \\ \mathrm {因 此 , 原 极 限} &= \frac {1}{2}. \end{aligned}</equation>

---

**2020年第9题 | 填空题 | 4分**

9. lim

**答案:**```latex

-1.
```
**解析: **解 通分整理原极限.<equation>\lim _ {x \rightarrow 0} \left[ \frac {1}{\mathrm {e} ^ {x} - 1} - \frac {1}{\ln (1 + x)} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{\left(\mathrm {e} ^ {x} - 1\right) \ln (1 + x)} \frac {\mathrm {e} ^ {x} - 1 \sim x}{\ln (1 + x) \sim x} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}}.</equation>下面用两种方法计算<equation>\lim_{x\to 0}\frac{\ln(1 + x) - \mathrm{e}^{x} + 1}{x^{2}}.</equation>（法一）利用泰勒公式.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} &= \lim _ {x \rightarrow 0} \frac {x - \frac {x ^ {2}}{2} + o \left(x ^ {2}\right) - \left[ 1 + x + \frac {x ^ {2}}{2} + o \left(x ^ {2}\right)\right] + 1}{x ^ {2}} \\ &= \lim _ {x \rightarrow 0} \frac {- x ^ {2} + o \left(x ^ {2}\right)}{x ^ {2}} = - 1. \end{aligned}</equation>（法二）利用洛必达法则.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - \mathrm {e} ^ {x} + 1}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - \mathrm {e} ^ {x}}{2 x} &= \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} (1 + x)}{2 x (1 + x)} = \frac {1}{2} \lim _ {x \rightarrow 0} \frac {1 - \mathrm {e} ^ {x} - x \mathrm {e} ^ {x}}{x} \\ &= \frac {1}{2} \lim _ {x \rightarrow 0} \left(\frac {1 - \mathrm {e} ^ {x}}{x} - \mathrm {e} ^ {x}\right) \xlongequal {\text {洛必达}} \frac {1 - \mathrm {e} ^ {x} \sim - x}{2} \frac {1}{2} \times (- 1 - 1) = - 1. \end{aligned}</equation>

---

**2016年第9题 | 填空题 | 4分**
9. lim
**答案: **# 1 2.
**解析: **解 当<equation>x\to0</equation>时，<equation>1-\cos x^{2}\sim\frac{1}{2} x^{4},\ln(1+x\sin x)\sim x\sin x</equation>从而<equation>\lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{1 - \cos x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\int_ {0} ^ {x} t \ln (1 + t \sin t) \mathrm {d} t}{\frac {1}{2} x ^ {4}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {x \ln (1 + x \sin x)}{2 x ^ {3}} = \lim _ {x \rightarrow 0} \frac {x \cdot x \sin x}{2 x ^ {3}} = \frac {1}{2}.</equation>

---

**2015年第9题 | 填空题 | 4分**
（无内容）
**解析: **解 （法一）利用洛必达法则.<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{\cos x} \cdot (- \sin x)}{2 x} = \lim _ {x \rightarrow 0} \left(- \frac {\sin x}{2 x}\right) = - \frac {1}{2}.</equation>（法二）利用等价无穷小替换.

当<equation>x\to 0</equation>时，<equation>\cos x - 1\to 0,\ln (1 + \cos x - 1)\sim \cos x - 1</equation>，于是<equation>\lim _ {x \rightarrow 0} \frac {\ln (\cos x)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\ln (1 + \cos x - 1)}{x ^ {2}} = \lim _ {x \rightarrow 0} \frac {\cos x - 1}{x ^ {2}} \frac {1 - \cos x - \frac {1}{2} x ^ {2}}{\overline {{=}}} \lim _ {x \rightarrow 0} \frac {- \frac {1}{2} x ^ {2}}{x ^ {2}} = - \frac {1}{2}.</equation>

---

**2014年第15题 | 解答题 | 10分**
15. (本题满分10分)

求极限<equation>\lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right)-t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)}.</equation>
**答案: **<equation>(1 5) \frac {1}{2}.</equation>
**解析: **解 由于<equation>\mathrm{e}^{x}</equation>在 x=0处的带拉格朗日余项的2阶泰勒公式为<equation>\mathrm{e}^{x}=1+x+\frac{x^{2}}{2}+\frac{\mathrm{e}^{\theta x}}{3!} x^{3}</equation>其中<equation>0 < \theta < 1</equation>，故当 x > 0时，<equation>\mathrm{e}^{x}>1+x+\frac{x^{2}}{2}.</equation>于是，<equation>\mathrm{e}^{\frac{1}{t}}-1 > \frac{1}{t}+\frac{1}{2t^{2}}(t > 0),</equation><equation>t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t > t ^ {2} \left(\frac {1}{t} + \frac {1}{2 t ^ {2}}\right) - t = \frac {1}{2}.</equation>从而<equation>\int_{1}^{+\infty}\left[ t^{2}\left(\mathrm{e}^{\frac{1}{t}} - 1\right) - t\right]\mathrm{d}t\to +\infty .</equation>另一方面，<equation>\lim _ {x \rightarrow + \infty} \left[ x ^ {2} \ln \left(1 + \frac {1}{x}\right)\right] \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} x = + \infty .</equation>因此，原极限为<equation>\frac{\infty}{\infty}</equation>型未定式.

当<equation>x\to +\infty</equation>时，<equation>\ln \left(1 + \frac{1}{x}\right)\sim \frac{1}{x}</equation>，故<equation>\begin{aligned} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x ^ {2} \ln \left(1 + \frac {1}{x}\right)} \xlongequal {\ln \left(1 + \frac {1}{x}\right) \sim \frac {1}{x}} \lim _ {x \rightarrow + \infty} \frac {\int_ {1} ^ {x} \left[ t ^ {2} \left(\mathrm {e} ^ {\frac {1}{t}} - 1\right) - t \right] \mathrm {d} t}{x} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow + \infty} \frac {x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x}{1} &= \lim _ {x \rightarrow + \infty} \frac {\mathrm {e} ^ {\frac {1}{x}} - 1 - \frac {1}{x}}{\frac {1}{x ^ {2}}} \\ \xlongequal {u = \frac {1}{x}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - u - 1}{u ^ {2}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {\mathrm {e} ^ {u} - 1}{2 u} \\ \xlongequal {\mathrm {e} ^ {u} - 1 \sim u} \lim _ {u \rightarrow 0 ^ {+}} \frac {u}{2 u} &= \frac {1}{2}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{2}.</equation>将原极限化简为<equation>\lim_{x\to +\infty}[x^{2}(\mathrm{e}^{\frac{1}{x}} -1) - x]</equation>后，也可以用泰勒公式来求该极限.

当<equation>x\to +\infty</equation>时，<equation>\frac{1}{x}\rightarrow 0^{+}</equation>.由<equation>\mathrm{e}^{u}</equation>在<equation>u = 0</equation>处的泰勒公式得，<equation>\mathrm {e} ^ {\frac {1}{x}} = 1 + \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right).</equation>从而，<equation>\begin{array}{l} \lim _ {x \rightarrow + \infty} \left[ x ^ {2} \left(\mathrm {e} ^ {\frac {1}{x}} - 1\right) - x \right] = \lim _ {x \rightarrow + \infty} \left\{x ^ {2} \left[ \frac {1}{x} + \frac {1}{2 !} \cdot \frac {1}{x ^ {2}} + o \left(\frac {1}{x ^ {2}}\right)\right] - x \right\} \\ = \lim _ {x \rightarrow + \infty} \left[ \frac {1}{2} + x ^ {2} \cdot o \left(\frac {1}{x ^ {2}}\right)\right] = \frac {1}{2}. \\ \end{array}</equation>

---

**2011年第15题 | 解答题 | 10分**
15. (本题满分10分)
**解析: **解（法一）由于当<equation>x\to 0</equation>时，<equation>\frac{\ln(1+x)}{x}>0</equation>，故可以对函数<equation>\left[\frac{\ln(1+x)}{x}\right]^{\frac{1}{e^{x}-1}}</equation>取对数.又<equation>\begin{array}{l} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} \xlongequal {\mathrm {e} ^ {x} - 1 \sim x} \lim _ {x \rightarrow 0} \frac {\ln \left[ 1 + \frac {\ln (1 + x) - x}{x} \right]}{x} \\ \xlongequal {\ln (1 + t) - t} \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \\ = \lim _ {x \rightarrow 0} \frac {x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) - x}{x ^ {2}} = - \frac {1}{2}, \\ \end{array}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>(法二)<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \lim_{x\to 0}\left[1 + \frac{\ln(1 + x) - x}{x}\right]^{\frac{x}{\ln(1 + x) - x} \cdot \frac{\ln(1 + x) - x}{x} \cdot \frac{1}{e^x - 1}}.</equation>由于<equation>\lim _ {x \rightarrow 0} \left[ \frac {\ln (1 + x) - x}{x} \cdot \frac {1}{\mathrm {e} ^ {x} - 1} \right] = \lim _ {x \rightarrow 0} \frac {\ln (1 + x) - x}{x ^ {2}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {\frac {1}{1 + x} - 1}{2 x} = \lim _ {x \rightarrow 0} \frac {- 1}{2 (1 + x)} = - \frac {1}{2},</equation><equation>= \mathrm {e} ^ {- \frac {1}{2}}</equation>（法三）由于

注意该技巧！添加绝对值后不用分情况讨论.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \frac {1}{\mathrm {e} ^ {x} - 1} \ln \frac {\ln (1 + x)}{x} &= \lim _ {x \rightarrow 0} \frac {\ln \left| \frac {\ln (1 + x)}{x} \right|}{\mathrm {e} ^ {x} - 1} = \lim _ {x \rightarrow 0} \frac {\ln | \ln (1 + x) | - \ln | x |}{x} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \left[ \frac {\frac {1}{1 + x}}{\ln (1 + x)} - \frac {1}{x} \right] &= \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x (1 + x) \ln (1 + x)} \\ \underline {{\frac {\ln (1 + x) - x}{\lim _ {x \rightarrow 0} (1 + x) = 1}}} \lim _ {x \rightarrow 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2}} \\ \underline {{\text {洛必达}}} \lim _ {x \rightarrow 0} \frac {- \ln (1 + x)}{2 x} &= - \frac {1}{2}, \end{aligned}</equation>故<equation>\lim_{x\to 0}\left[\frac{\ln(1 + x)}{x}\right]^{\frac{1}{e^x - 1}} = \mathrm{e}^{-\frac{1}{2}}.</equation>

---

**2010年第1题 | 选择题 | 4分 | 答案: C**
1. 极限<equation>\lim_{x\to \infty}\left[\frac{x^{2}}{(x-a)(x+b)}\right]^{x}=(\quad)</equation>A. 1 B. e C.<equation>e^{a-b}</equation>D.<equation>e^{b-a}</equation>
答案: C
**解析: **解（法一）若 a,b 不同时为0，则<equation>( a-b) x+a b\neq0</equation>由<equation>\lim_{x\to\infty}\frac{(a-b)x+ab}{(x-a)(x+b)}=0</equation>以及重要极限<equation>\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=e</equation>的复合形式可知，<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {x} \\ &= \lim _ {x \rightarrow \infty} \left[ \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] ^ {\frac {(x - a) (x + b)}{(a - b) x + a b}} \right] ^ {\left[ \frac {(a - b) x + a b}{(x - a) (x + b)} \cdot x \right]} \\ &= \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{x ^ {2} - (a - b) x - a b}} = \mathrm {e} ^ {\lim _ {x \rightarrow \infty} \frac {(a - b) + \frac {a b}{x}}{- \frac {a - b}{x} - \frac {a b}{x ^ {2}}}} = \mathrm {e} ^ {a - b}. \end{aligned}</equation>若<equation>a = b = 0</equation>，则原式<equation>= \lim_{x\to \infty}1^{x} = 1 = \mathrm{e}^{a - b}</equation>.

综上所述，应选C.

（法二）当<equation>x\to \infty</equation>时（无论是<equation>+\infty</equation>还是<equation>-\infty</equation>），<equation>\frac{x^{2}}{(x-a)(x+b)}>0</equation>，故可以对<equation>\left[ \frac{x^{2}}{(x-a)(x+b)} \right]^{x}</equation>取对数.又<equation>\begin{aligned} \lim _ {x \rightarrow \infty} \ln \left[ \frac {x ^ {2}}{(x - a) (x + b)} \right] ^ {x} &= \lim _ {x \rightarrow \infty} x \ln \frac {x ^ {2}}{(x - a) (x + b)} = \lim _ {x \rightarrow \infty} x \ln \left[ 1 + \frac {(a - b) x + a b}{(x - a) (x + b)} \right] \\ &= \lim _ {x \rightarrow \infty} \left[ x \cdot \frac {(a - b) x + a b}{(x - a) (x + b)} \right] = \lim _ {x \rightarrow \infty} \frac {(a - b) x ^ {2} + a b x}{(x - a) (x + b)} = a - b, \end{aligned}</equation>故原式<equation>= \mathrm{e}^{a - b}.</equation>应选C.

---


#### 确定极限中的参数

**2024年第11题 | 填空题 | 5分**
<equation>. \mathrm {若} \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = 6, \mathrm {则} a = \underline {{}}</equation>
**答案: **## a=6.
**解析: **<equation>\begin{aligned} 6 &= \lim _ {x \rightarrow 0} \frac {\left(1 + a x ^ {2}\right) ^ {\sin x} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\mathrm {e} ^ {\sin x \ln \left(1 + a x ^ {2}\right)} - 1}{x ^ {3}} = \lim _ {x \rightarrow 0} \frac {\sin x \ln \left(1 + a x ^ {2}\right)}{x ^ {3}} \\ &= \lim _ {x \rightarrow 0} \frac {x \cdot a x ^ {2}}{x ^ {3}} = a. \end{aligned}</equation>因此，<equation>a=6.</equation>

---

**2023年第11题 | 填空题 | 5分**
11. 当<equation>x \to0</equation>时，函数<equation>f(x)=ax+bx^{2}+\ln(1+x)</equation>与<equation>g(x)=\mathrm{e}^{x^{2}}-\cos x</equation>是等价无穷小，则 ab=___
**答案: **<equation>- 2.</equation>
**解析: **解分别写出<equation>f ( x )</equation>与<equation>g ( x )</equation>在<equation>x=0</equation>处的二阶泰勒公式.当<equation>x\to0</equation>时，<equation>f (x) = a x + b x ^ {2} + x - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) = (a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right),</equation><equation>g (x) = 1 + x ^ {2} + o \left(x ^ {2}\right) - \left[ 1 - \frac {1}{2} x ^ {2} + o \left(x ^ {2}\right) \right] = \frac {3}{2} x ^ {2} + o \left(x ^ {2}\right).</equation>由于<equation>f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小，故<equation>1 = \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {(a + 1) x + \left(b - \frac {1}{2}\right) x ^ {2} + o \left(x ^ {2}\right)}{\frac {3}{2} x ^ {2} + o \left(x ^ {2}\right)}.</equation>由（1）式成立可得<equation>a+1=0,b-\frac{1}{2}=\frac{3}{2}.</equation>解得<equation>a=-1,b=2.</equation>因此，<equation>ab=-2.</equation>

---

**2019年第1题 | 选择题 | 4分 | 答案: C**
1. 当 x→0时，若 x-tanx与<equation>x^{k}</equation>是同阶无穷小，则 k=（    ）

A.1 B.2 C.3 D.4
答案: C
**解析: **解 首先，由于当<equation>x\to0</equation>时，<equation>x-\tan x\to0</equation>，而<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}</equation>为非零常数，故 k > 0.下面用两种方法讨论<equation>\lim_{x\to0}\frac{x-\tan x}{x^{k}}.</equation>（法一）由于<equation>\tan x=x+\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，故<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {- \frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小，k=3.

因此，应选C.

（法二）利用洛必达法则讨论<equation>\lim_{x\to 0}\frac{x - \tan x}{x^k}</equation>.<equation>\lim _ {x \rightarrow 0} \frac {x - \tan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \sec^ {2} x}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \frac {- \tan^ {2} x}{k x ^ {k - 1}} \xlongequal {\tan x \sim x} \lim _ {x \rightarrow 0} \frac {- x ^ {2}}{k x ^ {k - 1}}.</equation>当 k > 3时，该极限为<equation>\infty</equation>；当0 < k < 3时，该极限为0；当 k=3时，该极限为<equation>-\frac{1}{3}.</equation>于是，<equation>x-\tan x</equation>与<equation>x^{3}</equation>是同阶无穷小， k=3.

因此，应选C.

---

**2018年第9题 | 填空题 | 4分**
9. 若<equation>\lim_{x\rightarrow 0}\left(\frac{1-\tan x}{1+\tan x}\right)^{\frac{1}{\sin k x}}=\mathrm{e}</equation>，则 k= ___
**解析: **解（法一）对原极限进行恒等变形，再凑重要极限.<equation>\lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} = \lim _ {x \rightarrow 0} \left(1 - \frac {2 \tan x}{1 + \tan x}\right) ^ {\frac {1 + \tan x}{- 2 \tan x} \cdot \frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}}.</equation>因为<equation>\lim _ {x \rightarrow 0} \left(\frac {- 2 \tan x}{1 + \tan x} \cdot \frac {1}{\sin k x}\right) = \lim _ {x \rightarrow 0} \frac {- 2 \tan x}{\sin k x} \frac {\tan x \sim x}{\sin k x \sim k x} \lim _ {x \rightarrow 0} \frac {- 2 x}{k x} = - \frac {2}{k},</equation>所以原极限<equation>= \mathrm{e}^{-\frac{2}{k}} = \mathrm{e}.</equation>因此，<equation>-\frac{2}{k} = 1,k = -2.</equation>（法二）取对数，再求极限.<equation>\begin{aligned} \lim _ {x \rightarrow 0} \left(\frac {1 - \tan x}{1 + \tan x}\right) ^ {\frac {1}{\sin k x}} &= \lim _ {x \rightarrow 0} \mathrm {e} ^ {\frac {1}{\sin k x} \cdot \ln \left(\frac {1 - \tan x}{1 + \tan x}\right)} = \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {1}{\sin k x} \cdot \ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right)} \\ \frac {\ln \left(1 - \frac {2 \tan x}{1 + \tan x}\right) \sim \frac {- 2 \tan x}{1 + \tan x}}{\frac {\tan x \sim x}{\sin k x \sim k x}} \mathrm {e} ^ {\lim _ {x \rightarrow 0} \frac {- 2 x}{k x}} &= \mathrm {e} ^ {- \frac {2}{k}}. \end{aligned}</equation>由于原极限<equation>= \mathrm{e}</equation>，故<equation>-\frac{2}{k} = 1</equation>，即<equation>k = -2.</equation>

---

**2015年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数<equation>f(x)=x+a\ln(1+x)+bx\sin x,g(x)=kx^{3}.</equation>若 f(x)与 g(x)在<equation>x\rightarrow0</equation>时是等价无穷小，求 a,b,k的值.
**解析: **由于 g(x）中 x的次数为3，故可考虑写出 f(x)在 x=0处的3阶泰勒公式.

由<equation>\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + o \left(x ^ {3}\right), \quad \sin x = x - \frac {x ^ {3}}{3 !} + o \left(x ^ {3}\right),</equation>可得<equation>f (x) = x + a x - \frac {a x ^ {2}}{2} + \frac {a x ^ {3}}{3} + b x ^ {2} + o \left(x ^ {3}\right) = (a + 1) x + \left(b - \frac {a}{2}\right) x ^ {2} + \frac {a}{3} x ^ {3} + o \left(x ^ {3}\right).</equation>记<equation>I=\lim_{x\to 0}\frac{f(x)}{g(x)}=\lim_{x\to 0}\frac{(a+1)x+\left(b-\frac{a}{2}\right)x^{2}+\frac{a}{3}x^{3}+o\left(x^{3}\right)}{kx^{3}}.</equation>由等价无穷小量的定义知<equation>I=1.</equation>首先，<equation>k\neq 0</equation>当 k≠0时，若 I存在，则必有<equation>\left\{\begin{array}{l l}a+1=0,\\ b-\frac{a}{2}=0,\end{array}\right.</equation>否则<equation>I=\infty.</equation>解得 a=-1，b=-<equation>\frac{1}{2}.</equation>又因为 I=1，所以<equation>\frac{a}{3}=k,k=-\frac{1}{3}.</equation>综上所述，<equation>a = -1</equation>，<equation>b = -\frac{1}{2}</equation>，<equation>k = -\frac{1}{3}</equation>

---

**2013年第1题 | 选择题 | 4分 | 答案: D**
1. 已知极限<equation>\lim_{x\rightarrow 0}\frac{x-\arctan x}{x^{k}}=c</equation>，其中 k,c为常数，且<equation>c\neq 0</equation>，则（    )

A. k=2, c=-<equation>\frac{1}{2}</equation>B. k=2, c=<equation>\frac{1}{2}</equation>C. k=3, c=-<equation>\frac{1}{3}</equation>D. k=3, c=<equation>\frac{1}{3}</equation>
答案: D
**解析: **解（法一）当<equation>x\to0</equation>时，<equation>\arctan x=x-\frac{x^{3}}{3}+o\left(x^{3}\right)</equation>，于是<equation>0 \neq c = \lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} = \lim _ {x \rightarrow 0} \frac {\frac {x ^ {3}}{3} + o \left(x ^ {3}\right)}{x ^ {k}}.</equation>当<equation>k > 3</equation>时，<equation>\lim_{x\to 0}\frac{\frac{x^3}{3} + o(x^3)}{x^k} = \lim_{x\to 0}\frac{\frac{1}{3} + \frac{o(x^3)}{x^3}}{x^{k - 3}} = \lim_{x\to 0}\frac{\frac{1}{3}}{x^{k - 3}} = \infty .</equation>当 k < 3时，<equation>\lim_{x\to 0}\frac{\frac{x^{3}}{3}+o\left(x^{3}\right)}{x^{k}}=\lim_{x\to 0}\left[\frac{x^{3-k}}{3}+\frac{o\left(x^{3}\right)}{x^{3}}\cdot x^{3-k}\right]=\lim_{x\to 0}\frac{x^{3-k}}{3}=0.</equation>因此，k=3，此时<equation>c=\frac{1}{3}</equation>应选D.

（法二）由于<equation>c\neq 0</equation>且<equation>\lim_{x\to 0} \left(x-\arctan x\right)=0</equation>，故<equation>\lim_{x\to 0} x^{k}=0</equation>，从而 k>0，于是题设中极限为<equation>\frac{0}{0}</equation>型.根据洛必达法则，<equation>\lim _ {x \rightarrow 0} \frac {x - \arctan x}{x ^ {k}} \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - \frac {1}{1 + x ^ {2}}}{k x ^ {k - 1}} = \lim _ {x \rightarrow 0} \left(\frac {1}{1 + x ^ {2}} \cdot \frac {x ^ {2}}{k x ^ {k - 1}}\right) = \lim _ {x \rightarrow 0} \frac {1}{k x ^ {k - 3}} = c.</equation>又<equation>c\neq 0</equation>，故<equation>k=3</equation>，从而<equation>c=\frac{1}{3}</equation>应选D.

---

**2009年第1题 | 选择题 | 4分 | 答案: A**
1. 当<equation>x\to0</equation>时，<equation>f(x)=x-\sin ax</equation>与<equation>g(x)=x^{2}\ln(1-bx)</equation>是等价无穷小量，则（    )

A. a=1,b=-<equation>\frac{1}{6}</equation>B. a=1,b=<equation>\frac{1}{6}</equation>C. a=-1,b=-<equation>\frac{1}{6}</equation>D. a=-1,b=<equation>\frac{1}{6}</equation>
答案: A
**解析: **由于<equation>x\to0</equation>时，<equation>f(x)</equation>与<equation>g(x)</equation>是等价无穷小量，故<equation>\begin{aligned} 1 &= \lim _ {x \rightarrow 0} \frac {f (x)}{g (x)} = \lim _ {x \rightarrow 0} \frac {x - \sin a x}{x ^ {2} \ln (1 - b x)} \xlongequal {\ln (1 - b x) \sim (- b x)} \lim _ {x \rightarrow 0} \frac {x - \sin a x}{- b x ^ {3}} \\ \xlongequal {\text {洛必达}} \lim _ {x \rightarrow 0} \frac {1 - a \cos a x}{- 3 b x ^ {2}} &= I _ {1}. \end{aligned}</equation>由于<equation>\lim_{x\to 0}(-3bx^2) = 0</equation>，故若<equation>I_{1}</equation>存在，则<equation>\lim_{x\to 0}(1 - a\cos ax) = 0</equation>，从而<equation>a = 1.</equation>代人 a=1，得<equation>I _ {1} = \lim _ {x \rightarrow 0} \frac {1 - \cos x}{- 3 b x ^ {2}} \xlongequal {1 - \cos x \sim \frac {x ^ {2}}{2}} \lim _ {x \rightarrow 0} \frac {\frac {x ^ {2}}{2}}{- 3 b x ^ {2}} = - \frac {1}{6 b}.</equation>当<equation>b = -\frac{1}{6}</equation>时，<equation>I_{1}</equation>存在且等于1.

因此，当<equation>a = 1,b = -\frac{1}{6}</equation>时，<equation>\lim_{x\to 0}\frac{f(x)}{g(x)} = 1,f(x)</equation>与<equation>g(x)</equation>是<equation>x\to 0</equation>时的等价无穷小量.应选A.

---


#### 数列敛散性的判定

**2022年第3题 | 选择题 | 5分 | 答案: D**

3. 已知数列<equation>\{x_{n}\}</equation>满足<equation>-\frac{\pi}{2}\leqslant x_{n}\leqslant \frac{\pi}{2}</equation>，则（    )

A. 若<equation>\lim_{n\to\infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\to\infty}x_{n}</equation>存在

B. 若<equation>\lim_{n\to\infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\to\infty}x_{n}</equation>存在

C. 若<equation>\lim_{n\to\infty}\cos(\sin x_{n})</equation>存在，则<equation>\lim_{n\to\infty}\sin x_{n}</equation>存在，但<equation>\lim_{n\to\infty}x_{n}</equation>不一定存在

D. 若<equation>\lim_{n\to\infty}\sin(\cos x_{n})</equation>存在，则<equation>\lim_{n\to\infty}\cos x_{n}</equation>存在，但<equation>\lim_{n\to\infty}x_{n}</equation>不一定存在

答案: D

**解析:**解 若<equation>\lim_{n\rightarrow \infty}\sin(\cos x_{n})</equation>存在，则将其记为 a.由于<equation>\sin x</equation>在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上存在反函数<equation>\arcsin x</equation>，故<equation>\lim_{n\rightarrow \infty}\cos x_{n}=\lim_{n\rightarrow \infty}\arcsin(\sin(\cos x_{n}))=\arcsin(\lim_{n\rightarrow \infty}\sin(\cos x_{n}))=\arcsin a.</equation>但是<equation>\lim_{n\rightarrow \infty}\cos x_{n}</equation>存在并不能保证<equation>\lim_{n\rightarrow \infty}x_{n}</equation>存在.例如取<equation>x_{n}=(-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\rightarrow \infty}\cos x_{n}=0</equation>，但<equation>\lim_{n\rightarrow \infty}x_{n}</equation>不存在.选项B错误，选项D正确.应选D.

由于<equation>\cos x</equation>在<equation>\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]</equation>上并不单调，故由<equation>\lim_{n\to \infty}\cos (\sin x_n)</equation>存在并不能保证<equation>\lim_{n\to \infty}\sin x_n</equation>存在。同样取<equation>x_{n} = (-1)^{n}\frac{\pi}{2}</equation>，则<equation>\lim_{n\to \infty}\cos (\sin x_n) = \cos 1</equation>，但<equation>\lim_{n\to \infty}\sin x_n</equation>和<equation>\lim_{n\to \infty}x_n</equation>均不存在。选项A、C不正确。

---

**2019年第18题 | 解答题 | 10分**

18. (本题满分10分)

设<equation>a_{n}=\int_{0}^{1} x^{n}\sqrt{1-x^{2}}\mathrm{d}x(n=0,1,2,\dots).</equation>I. 证明数列<equation>\{a_{n}\}</equation>单调递减，且<equation>a_{n}=\frac{n-1}{n+2} a_{n-2}(n=2,3,\cdots)</equation>；

II. 求<equation>\lim_{n\to\infty}\frac{a_{n}}{a_{n-1}}.</equation>

**答案:**（I）证明略；（Ⅱ）<equation>\lim_{n\to \infty}\frac{a_{n}}{a}=1.</equation>

**解析:**解（I）考虑<equation>a_{n+1}-a_{n}</equation>由于在（0，1）内，<equation>x^{n+1}-x^{n}<0,\sqrt{1-x^{2}}>0</equation>故由定积分的保号性可知，<equation>a _ {n + 1} - a _ {n} = \int_ {0} ^ {1} \left(x ^ {n + 1} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x < 0.</equation>因此，<equation>\{a_{n}\}</equation>单调递减.

下面用两种方法证明<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>.

（法一）先三角换元，再分部分分.

令<equation>x=\sin t</equation>，则<equation>\mathrm{d}x=\cos t\mathrm{d}t.</equation><equation>\begin{aligned} a _ {n} &= \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x \xlongequal {x = \sin t} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos t \cdot \cos t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \left(\sin^ {n} t - \sin^ {n + 2} t\right) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n + 1} t \mathrm {d} (\cos t) \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t + \sin^ {n + 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n + 1) \sin^ {n} t \cdot \cos t \mathrm {d} t \right. \\ &= \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \cos^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t - (n + 1) a _ {n}. \end{aligned}</equation>由上可得，<equation>(n + 2)a_{n} = \int_{0}^{\frac{\pi}{2}}\sin^{n}t\mathrm{d}t.</equation>另一方面，<equation>\begin{aligned} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} t \mathrm {d} t &= - \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 1} t \mathrm {d} (\cos t) = - \left[ \sin^ {n - 1} t \cos t \left| _ {0} ^ {\frac {\pi}{2}} - \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot (n - 1) \sin^ {n - 2} t \cdot \cos t \mathrm {d} t \right] \right. \\ &= (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 2} t \cos^ {2} t \mathrm {d} t = (n - 1) a _ {n - 2}. \end{aligned}</equation>因此，<equation>(n + 2)a_{n} = (n - 1)a_{n - 2}</equation>，即<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>.

（法二）直接分部积分.注意到<equation>[ ( 1 - x^{2} )^{\frac{3}{2}} ]^{\prime} = - 3 x \sqrt{1 - x^{2}}</equation>，故<equation>\begin{array}{l} a _ {n} = \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x = - \frac {1}{3} \int_ {0} ^ {1} x ^ {n - 1} \mathrm {d} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \\ = - \frac {1}{3} \left\{\left[ x ^ {n - 1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \right] \Bigg | _ {0} ^ {1} - \int_ {0} ^ {1} \left(1 - x ^ {2}\right) ^ {\frac {3}{2}} \cdot (n - 1) x ^ {n - 2} \mathrm {d} x \right\} \\ = \frac {n - 1}{3} \int_ {0} ^ {1} \left(1 - x ^ {2}\right) \sqrt {1 - x ^ {2}} x ^ {n - 2} \mathrm {d} x = \frac {n - 1}{3} \int_ {0} ^ {1} \left(x ^ {n - 2} - x ^ {n}\right) \sqrt {1 - x ^ {2}} \mathrm {d} x \\ = \frac {n - 1}{3} \left(\int_ {0} ^ {1} x ^ {n - 2} \sqrt {1 - x ^ {2}} \mathrm {d} x - \int_ {0} ^ {1} x ^ {n} \sqrt {1 - x ^ {2}} \mathrm {d} x\right) \\ = \frac {n - 1}{3} \left(a _ {n - 2} - a _ {n}\right). \\ \end{array}</equation>因此，<equation>a_{n} = \frac{n - 1}{n + 2} a_{n - 2}(n = 2,3,\dots)</equation>（Ⅱ）由第（I）问可知<equation>\{a_{n}\}</equation>单调递减，故<equation>a_{n} < a_{n-1} < a_{n-2}</equation>又由<equation>a_{n}</equation>的表达式可知<equation>a_{n} > 0 (n= 0,1,\dots)</equation>，故<equation>\frac {n - 1}{n + 2} = \frac {a _ {n}}{a _ {n - 2}} < \frac {a _ {n}}{a _ {n - 1}} < \frac {a _ {n}}{a _ {n}} = 1.</equation>对（1）式中各项同时取极限，令<equation>n\to \infty</equation>，可得<equation>1 = \lim _ {n \rightarrow \infty} \frac {n - 1}{n + 2} \leqslant \lim _ {n \rightarrow \infty} \frac {a _ {n}}{a _ {n - 1}} \leqslant 1.</equation>由夹逼准则可知，<equation>\lim_{n\to \infty}\frac{a_n}{a_{n-1}} = 1.</equation>

---

**2018年第19题 | 解答题 | 10分**

19. (本题满分10分）

设数列<equation>\{x_{n}\}</equation>满足：<equation>x_{1}>0,x_{n}\mathrm{e}^{x_{n+1}}=\mathrm{e}^{x_{n}}-1(n=1,2,\cdots).</equation>证明数列<equation>\{x_{n}\}</equation>收敛，并求<equation>\lim_{n\rightarrow \infty}x_{n}.</equation>

**答案:**证明略，<equation>\lim x_{n}=0.</equation>n->infty

**解析:**解 由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1(n = 1,2,\dots)</equation>可得，<equation>x _ {n + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right).</equation>先用数学归纳法证明对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>首先，<equation>x_{1} > 0.</equation>假设当<equation>n = k</equation>时，<equation>x_{k} > 0.</equation>注意到当<equation>x > 0</equation>时，<equation>\mathrm{e}^{x} - 1 > x</equation>，从而<equation>\frac{\mathrm{e}^{x} - 1}{x} > 1.</equation>于是，<equation>x _ {k + 1} = \ln \left(\frac {\mathrm {e} ^ {x _ {k}} - 1}{x _ {k}}\right) > \ln 1 = 0.</equation>由数学归纳法可知，对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>因此，数列<equation>\{x_{n}\}</equation>有下界.

下面用两种方法证明数列<equation>\{x_{n}\}</equation>单调减少，即<equation>x_{n + 1} < x_n(n = 1,2,\dots)</equation>.

（法一）由<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1</equation>可知，<equation>\mathrm {e} ^ {x _ {n + 1}} = \frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}} = \frac {\mathrm {e} ^ {x _ {n}} - \mathrm {e} ^ {0}}{x _ {n} - 0} \frac {\text {拉 格 朗 日}}{\text {中 值 定 理}} \mathrm {e} ^ {\xi_ {n}},</equation>其中<equation>\xi_{n}\in (0,x_{n})</equation>由于<equation>\mathrm{e}^x</equation>单调增加，故由<equation>\mathrm{e}^{x_{n+1}} = \mathrm{e}^{\xi_n} < \mathrm{e}^{x_n}</equation>可得<equation>x_{n+1} < x_n</equation>，即数列<equation>\{x_n\}</equation>单调减少.

（法二）<equation>x _ {n + 1} - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n}}\right) - x _ {n} = \ln \left(\frac {\mathrm {e} ^ {x _ {n}} - 1}{x _ {n} \mathrm {e} ^ {x _ {n}}}\right).</equation>记<equation>f(x) = \mathrm{e}^{x} - 1 - x\mathrm{e}^{x}</equation>，则<equation>f^{\prime}(x) = \mathrm{e}^{x} - \mathrm{e}^{x} - x\mathrm{e}^{x} = -x\mathrm{e}^{x}</equation>.

当<equation>x > 0</equation>时，<equation>f^{\prime}(x) < 0,f(x)</equation>在<equation>[0, + \infty)</equation>上单调减少，于是，<equation>f(x) < f(0) = 0.</equation>从而，当<equation>x > 0</equation>时，<equation>\frac {\mathrm {e} ^ {x} - 1}{x \mathrm {e} ^ {x}} - 1 = \frac {\mathrm {e} ^ {x} - 1 - x \mathrm {e} ^ {x}}{x \mathrm {e} ^ {x}} < 0,</equation>即<equation>\frac{\mathrm{e}^x - 1}{x\mathrm{e}^x} < 1.</equation>又因为对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，所以<equation>\ln \left(\frac{\mathrm{e}^{x_n} - 1}{x_n\mathrm{e}^{x_n}}\right) < \ln 1 = 0</equation>，即<equation>x_{n + 1} - x_n < 0.</equation>因此，数列<equation>\{x_{n}\}</equation>单调减少.

由单调有界准则可知，数列<equation>\{x_{n}\}</equation>收敛.由于对所有的正整数<equation>n</equation>，都有<equation>x_{n} > 0</equation>，故<equation>\lim_{n\to \infty}x_n = a\geqslant 0.</equation>对<equation>x_{n}\mathrm{e}^{x_{n + 1}} = \mathrm{e}^{x_{n}} - 1</equation>两端同时令<equation>n\to \infty</equation>，可得<equation>a\mathrm{e}^{a} = \mathrm{e}^{a} - 1.</equation>由前面的结果可知，<equation>x=0</equation>是<equation>f(x)=\mathrm{e}^{x}-1-x\mathrm{e}^{x}</equation>在<equation>[0,+\infty)</equation>上的唯一零点.因此，<equation>a=0</equation>即<equation>\lim_{n\to \infty}x_{n}=0.</equation>

---

**2011年第18题 | 解答题 | 10分**

18. (本题满分10分)

I. 证明：对任意的正整数 n, 都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立；

II. 设<equation>a_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}-\ln n</equation>（<equation>n=1,2,\cdots</equation>），证明数列<equation>\left\{a_{n}\right\}</equation>收敛.

**解析:**证（I）（法一）考虑函数<equation>f ( x )=\ln x</equation>，则<equation>f^{\prime}(x)=\frac{1}{x}</equation>由拉格朗日中值定理，对任意的正整数n，都存在<equation>\xi_{n}\in(n,n+1)</equation>，使得<equation>\ln \left(1 + \frac {1}{n}\right) = f (n + 1) - f (n) = f ^ {\prime} \left(\xi_ {n}\right) = \frac {1}{\xi_ {n}}.</equation>又因为<equation>\xi_{n}\in (n,n + 1)</equation>，所以<equation>\frac{1}{n + 1} < \frac{1}{\xi_n} < \frac{1}{n}</equation>因此，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法二）分别证明<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)</equation>和<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\ln \left(1 + \frac{1}{n}\right) < \frac{1}{n}</equation>，可考虑函数<equation>f(x) = \ln (1 + x) - x.</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-1</equation>当 x > 0时，<equation>f^{\prime}(x)<0</equation>，故 f(x)在<equation>[0,+\infty)</equation>上单调减少.又由于 f(0) = 0，故对任意的正整数 n，<equation>f\left(\frac{1}{n}\right)<f(0)=0</equation>即<equation>\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}.</equation>为证明<equation>\frac{1}{n+1} < \ln \left( 1+\frac{1}{n} \right)</equation>，可考虑函数<equation>g(x)=\ln(1+x)-\frac{x}{1+x}.</equation><equation>g ^ {\prime} (x) = \frac {1}{1 + x} - \frac {(1 + x) - x}{(1 + x) ^ {2}} = \frac {x}{(1 + x) ^ {2}}.</equation>当 x > 0时，<equation>g^{\prime}(x) > 0</equation>，故 g(x)在<equation>[0,+\infty)</equation>上单调增加.又由于<equation>g(0)=0</equation>，故对任意的正整数n，<equation>g\left(\frac{1}{n}\right) > g(0) = 0</equation>，即<equation>\frac{1}{n+1} < \ln \left(1+\frac{1}{n}\right).</equation>综上所述，对任意的正整数 n，都有<equation>\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}</equation>成立.

（法三）注意到<equation>\ln \left( 1+\frac{1}{n} \right)=\int_{n}^{n+1} \frac{1}{x} \mathrm{d} x.</equation>由于<equation>\int_ {n} ^ {n + 1} \frac {1}{n + 1} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{x} \mathrm {d} x < \int_ {n} ^ {n + 1} \frac {1}{n} \mathrm {d} x,</equation>故<equation>\frac {1}{n + 1} < \ln \left(1 + \frac {1}{n}\right) < \frac {1}{n}.</equation>（Ⅱ）若能证明数列<equation>\{a_{n}\}</equation>单调且有界，则由单调有界准则知其收敛.

先证<equation>\left\{a_{n}\right\}</equation>单调.

对任意的正整数<equation>n = 1,2,3,\dots</equation><equation>a _ {n + 1} - a _ {n} = \frac {1}{n + 1} + \ln \frac {n}{n + 1} = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n}\right).</equation>由第（I）问知，<equation>a_{n+1}-a_{n}<0</equation>，故<equation>\left\{a_{n}\right\}</equation>单调减少.

下面证明<equation>\left\{a_{n}\right\}</equation>有下界.

由第（Ⅰ）问知，<equation>\ln 2 - \ln 1 < 1,</equation><equation>\ln 3 - \ln 2 < \frac {1}{2},</equation><equation>\ln (n + 1) - \ln n < \frac {1}{n}.</equation>将上述不等式左端和右端分别相加，得<equation>\ln (n + 1) - \ln 1 < 1 + \frac {1}{2} + \dots + \frac {1}{n}.</equation>同时减去<equation>\ln n</equation>，得<equation>a _ {n} > \ln (n + 1) - \ln n > 0.</equation>因此，<equation>\{a_{n}\}</equation>有下界.

综上所述，数列<equation>\left\{a_{n}\right\}</equation>收敛.

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

