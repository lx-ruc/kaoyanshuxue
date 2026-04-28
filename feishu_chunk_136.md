#### 定积分的计算

**2025年第17题 | 解答题 | 10分**

17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>

**答案:**#<equation>\frac{3\ln 2+\pi}{10}.</equation>

**解析:**解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得<equation>B=-A</equation>.将<equation>B=-A</equation>代入（2）式可得<equation>C=3A</equation>.将<equation>C=3A</equation>代入（3）式可得<equation>5A=1</equation>，即<equation>A=\frac{1}{5}</equation>.进一步可得<equation>B=-\frac{1}{5},C=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2022年第12题 | 填空题 | 5分**

<equation>\int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\ln 3 - \frac {\sqrt {3}}{3} \pi .</equation>

**解析:**解注意到<equation>( x^{2}+2 x+4)^{\prime}=2 x+2</equation>，<equation>\frac{2 x-4}{x^{2}+2 x+4}=\frac{2 x+2}{x^{2}+2 x+4}</equation><equation>-\frac{6}{x^{2}+2 x+4}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} d x &= \int_ {0} ^ {2} \frac {2 x + 2}{x ^ {2} + 2 x + 4} d x - 6 \int_ {0} ^ {2} \frac {1}{x ^ {2} + 2 x + 4} d x \\ &= \int_ {0} ^ {2} \frac {\mathrm {d} \left(x ^ {2} + 2 x + 4\right)}{x ^ {2} + 2 x + 4} - 2 \int_ {0} ^ {2} \frac {1}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} d x \\ &= \ln \left(x ^ {2} + 2 x + 4\right) \Bigg | _ {0} ^ {2} - 2 \sqrt {3} \int_ {0} ^ {2} \frac {\mathrm {d} \left[ \frac {1}{\sqrt {3}} (x + 1) \right]}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} \\ &= \ln 3 - 2 \sqrt {3} \arctan \frac {1}{\sqrt {3}} (x + 1) \Bigg | _ {0} ^ {2} \\ &= \ln 3 - 2 \sqrt {3} \times \left(\frac {\pi}{3} - \frac {\pi}{6}\right) = \ln 3 - \frac {\sqrt {3}}{3} \pi . \end{aligned}</equation>

---

**2021年第12题 | 填空题 | 5分**

<equation>\int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {\left| x ^ {2} - 9 \right|}} \mathrm {d} x = \underline {{}}</equation>

**解析:**当<equation>\sqrt{5} < x < 3</equation>时，<equation>x^{2}-9<0</equation>；当 3 < x < 5时，<equation>x^{2}-9>0.</equation><equation>\begin{aligned} \int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {| x ^ {2} - 9 |}} \mathrm {d} x &= \int_ {\sqrt {5}} ^ {3} \frac {x}{\sqrt {9 - x ^ {2}}} \mathrm {d} x + \int_ {3} ^ {5} \frac {x}{\sqrt {x ^ {2} - 9}} \mathrm {d} x \\ &= - \frac {1}{2} \int_ {\sqrt {5}} ^ {3} \frac {\mathrm {d} \left(9 - x ^ {2}\right)}{\sqrt {9 - x ^ {2}}} + \frac {1}{2} \int_ {3} ^ {5} \frac {\mathrm {d} \left(x ^ {2} - 9\right)}{\sqrt {x ^ {2} - 9}} \\ &= \left(- \frac {1}{2}\right) \times 2 \times \sqrt {9 - x ^ {2}} \left| _ {\sqrt {5}} ^ {3} + \frac {1}{2} \times 2 \times \sqrt {x ^ {2} - 9} \right| _ {3} ^ {5} \\ &= - (0 - 2) + (4 - 0) = 6. \end{aligned}</equation>

---

**2019年第11题 | 填空题 | 4分**

11. 已知函数<equation>f ( x )=\int_{1}^{x}\sqrt{1+t^{4}}\mathrm{d} t</equation>，则<equation>\int_{0}^{1} x^{2} f ( x ) \mathrm{d} x=</equation>___.

**答案:**<equation>\frac{1-2\sqrt{2}}{18}.</equation>

**解析:**（法一）利用分部积分法.

注意到 f（1）=0.<equation>\begin{aligned} \int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x &= \frac {1}{3} \int_ {0} ^ {1} f (x) \mathrm {d} \left(x ^ {3}\right) = \frac {1}{3} \left[ x ^ {3} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {3} \cdot f ^ {\prime} (x) \mathrm {d} x \right] = - \frac {1}{3} \int_ {0} ^ {1} x ^ {3} \sqrt {1 + x ^ {4}} \mathrm {d} x \right. \\ &= - \frac {1}{1 2} \int_ {0} ^ {1} \sqrt {1 + x ^ {4}} \mathrm {d} \left(x ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + x ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \end{aligned}</equation>（法二）交换积分次序.

将 f(x) 代入所求积分.<equation>\int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \left(\int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t\right) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \mathrm {d} x \int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t.</equation>写出该积分对应的二重积分的积分区域 D. 由二次积分的表达式可知，边界曲线为 t=x，t=1以及 x=0，故<equation>D = \{(x, t) \mid x \leqslant t \leqslant 1, 0 \leqslant x \leqslant 1 \}.</equation>如图所示，交换积分次序可得<equation>D = \{(x, t) \mid 0 \leqslant x \leqslant t, 0 \leqslant t \leqslant 1 \}.</equation>因此，<equation>\begin{array}{l} = - \frac {1}{3} \cdot \frac {1}{4} \int_ {0} ^ {1} \sqrt {1 + t ^ {4}} \mathrm {d} \left(t ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + t ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \\ \end{array}</equation>

---

**2017年第9题 | 填空题 | 4分**

9.<equation>9. \int_ {- \pi} ^ {\pi} \left(\sin^ {3} x + \sqrt {\pi^ {2} - x ^ {2}}\right) \mathrm {d} x = \underline {{}}</equation>

**解析:**由于<equation>[-\pi ,\pi ]</equation>是对称区间，且<equation>\sin^{3}x</equation>是关于x的奇函数，<equation>\sqrt{\pi^{2}-x^{2}}</equation>是关于x的偶函数，故原积分<equation>\frac{\int_{-\pi}^{\pi}\sin^{3}x\mathrm{d}x=0}{\int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x} \int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x</equation><equation>\frac{x=\pi\sin t}{2} 2\int_{0}^{\frac{\pi}{2}}\pi\cos t\cdot \pi\cos t\mathrm{d}t=\pi^{2}\int_{0}^{\frac{\pi}{2}}2\cos^{2}t\mathrm{d}t</equation><equation>= \pi^{2}\int_{0}^{\frac{\pi}{2}}(1+\cos 2t)\mathrm{d}t=\pi^{2}\times \left(\frac{\pi}{2}+0\right)=\frac{\pi^{3}}{2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 设<equation>\int_{0}^{a} x \mathrm{e}^{2 x} \mathrm{d} x=\frac{1}{4}</equation>，则 a=___

**解析:**由于<equation>\frac{1}{4}=\int_{0}^{a}x\mathrm{e}^{2x}\mathrm{d}x=\frac{x\mathrm{e}^{2x}}{2}\bigg|_{0}^{a}-\int_{0}^{a}\frac{\mathrm{e}^{2x}}{2}\mathrm{d}x=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2x}}{4}\bigg|_{0}^{a}=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2a}}{4}+\frac{1}{4},</equation>故<equation>\frac{a}{2}\mathrm{e}^{2a}=\frac{\mathrm{e}^{2a}}{4}</equation>因此，<equation>a=\frac{1}{2}.</equation>

---


