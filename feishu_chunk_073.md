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


