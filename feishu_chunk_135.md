#### 反常积分的计算

**2025年第12题 | 填空题 | 5分**

12. 设<equation>\int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x = \ln 2, \mathrm {则} a = \underline {{}}</equation>

**解析:**解 由于<equation>\frac{a}{x(2x+a)}=\frac{1}{x}-\frac{2}{2x+a}</equation>，故<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x &= \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {2}{2 x + a}\right) \mathrm {d} x = \left(\ln x - \ln | 2 x + a |\right) \Bigg | _ {1} ^ {+ \infty} = \ln \frac {x}{| 2 x + a |} \Bigg | _ {1} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \ln \frac {x}{| 2 x + a |} - \ln \frac {1}{| 2 + a |} = \ln \frac {| 2 + a |}{2}. \end{aligned}</equation>由<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)} \mathrm{d}x=\ln 2</equation>可得<equation>\ln \frac{\mid 2+a\mid}{2}=\ln 2</equation>结合<equation>\ln x</equation>是单调函数可得<equation>\frac{\mid 2+a\mid}{2}=2</equation>解得 a=2或a=-6.

当 a=-6时，<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)}\mathrm{d}x=\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>，此时 x=3为被积函数的瑕点，且<equation>\lim_{x\to 3^{-}}\frac{x-3}{x(x-3)}=\frac{1}{3}</equation>，由无界函数的反常积分的极限审敛法可得<equation>\int_{1}^{3}\frac{1}{x(x-3)}\mathrm{d}x</equation>发散，从而<equation>\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>发散.于是，应舍去 a=-6.

当<equation>a = 2</equation>时，被积函数在<equation>(1, +\infty)</equation>上没有瑕点.

因此，a=2.

---

**2024年第12题 | 填空题 | 5分**

<equation>\int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\frac {1}{2} \ln 3 - \frac {\pi}{8}</equation>

**解析:**解（法一）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x^{2}-1)</equation>，而<equation>(x^{2}+4)-(x^{2}-1)=5</equation>，故<equation>\frac{5}{x^{4}+3 x^{2}-4}=\frac{5}{(x^{2}+4)(x^{2}-1)}=\frac{1}{x^{2}-1}-\frac{1}{x^{2}+4}=\frac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right)-\frac{1}{x^{2}+4}.</equation>因此，<equation>\begin{aligned} \int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} d x &= \int_ {2} ^ {+ \infty} \left[ \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4} \right] d x \\ &= \frac {1}{2} \ln \left. \frac {x - 1}{x + 1} \right| _ {2} ^ {+ \infty} - \frac {1}{2} \int_ {2} ^ {+ \infty} \frac {1}{1 + \left(\frac {x}{2}\right) ^ {2}} d \left(\frac {x}{2}\right) \\ &= - \frac {1}{2} \ln \frac {1}{3} - \frac {1}{2} \arctan \frac {x}{2} \Big | _ {2} ^ {+ \infty} = \frac {1}{2} \ln 3 - \frac {1}{2} \left(\frac {\pi}{2} - \frac {\pi}{4}\right) \\ &= \frac {1}{2} \ln 3 - \frac {\pi}{8}. \end{aligned}</equation>（法二）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x+1)(x-1)</equation>，故对<equation>\frac{5}{x^{4}+3 x^{2}-4}</equation>进行部分分式分解设<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {A}{x - 1} + \frac {B}{x + 1} + \frac {C x + D}{x ^ {2} + 4}.</equation>通分并整理可得，<equation>\begin{aligned} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} &= \frac {A (x + 1) \left(x ^ {2} + 4\right) + B (x - 1) \left(x ^ {2} + 4\right) + (C x + D) \left(x ^ {2} - 1\right)}{x ^ {4} + 3 x ^ {2} - 4} \\ &= \frac {(A + B + C) x ^ {3} + (A - B + D) x ^ {2} + (4 A + 4 B - C) x + 4 A - 4 B - D}{x ^ {4} + 3 x ^ {2} - 4}. \end{aligned}</equation>比较<equation>x^{3},x^{2},x</equation>的系数以及常数项可得，<equation>[ A + B + C = 0,</equation><equation>A - B + D = 0,</equation><equation>4 A + 4 B - C = 0,</equation><equation>4 A - 4 B - D = 5.</equation>(1) 式与（3）式相加并整理可得<equation>A+B=0</equation>，进一步可得 C=0.将 B=-A代人（2）式与（4）式可得<equation>\left\{\begin{array}{l l}2 A+D=0,\\ 8 A-D=5,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}A=\frac{1}{2},\\ B=-\frac{1}{2},\\ C=0,\\ D=-1. \end{array}\right.</equation>因此，<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4}.</equation>其余同法一.

---

**2013年第11题 | 填空题 | 4分**

<equation>\int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**解析:**<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x &= - \int_ {1} ^ {+ \infty} \ln x \mathrm {d} \left(\frac {1}{1 + x}\right) = - \left[ \frac {\ln x}{1 + x} \Big | _ {1} ^ {+ \infty} - \int_ {1} ^ {+ \infty} \frac {1}{x (1 + x)} \mathrm {d} x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Big | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---


