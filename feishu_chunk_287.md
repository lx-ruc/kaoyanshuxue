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


