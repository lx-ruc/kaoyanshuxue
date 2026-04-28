#### 傅里叶级数

**2025年第12题 | 填空题 | 5分**
12. 已知函数 f(x)<equation>\left\{\begin{array}{l l}0,&0 \leqslant x < \frac{1}{2}\\ x^{2},&\frac{1}{2} \leqslant x \leqslant 1\end{array} \right.</equation>，的傅里叶级数为<equation>\sum_{n=1}^{\infty} b_{n} \sin n \pi x</equation>，S(x)为<equation>\sum_{n=1}^{\infty} b_{n} \sin n \pi x</equation>的和函数，则<equation>S\left(-\frac{7}{2}\right)=</equation>
**解析: **解 由 S(x)为正弦级数的和函数可知，<equation>S ( x )</equation>为[0,1]上的 f(x)作奇延拓后再作周期为2的周期延拓所得函数的傅里叶级数.

由于 S（x）是周期为2的奇函数，故<equation>S \left(- \frac {7}{2}\right) = S \left(- 4 + \frac {1}{2}\right) = S \left(\frac {1}{2}\right).</equation>又因为<equation>x=\frac{1}{2}</equation>是<equation>f(x)</equation>的间断点，所以由狄利克雷收敛定理可得<equation>S \left(\frac {1}{2}\right) = \frac {1}{2} \left[ \lim _ {x \rightarrow \frac {1}{2} ^ {-}} f (x) + \lim _ {x \rightarrow \frac {1}{2} ^ {+}} f (x) \right] = \frac {1}{2} \left(0 + \frac {1}{4}\right) = \frac {1}{8}.</equation>因此，<equation>S\left(-\frac{7}{2}\right)=\frac{1}{8}.</equation>

---

**2024年第13题 | 填空题 | 5分**
13. 已知函数 f(x)=x+1，若 f(x)<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} a_{n} \cos n x,x \in[0,\pi]</equation>，则<equation>\lim_{n \to \infty} n^{2} \sin a_{2n-1}=</equation>___.
**答案: **\[ -\frac{1}{\pi} \]
**解析: **解 由于 f(x)的傅里叶级数展开式为余弦级数，故 f(x)为偶函数.由余弦级数的系数公式可知，当 n≥1时，<equation>\begin{aligned} a _ {n} &= \frac {2}{\pi} \int_ {0} ^ {\pi} (x + 1) \cos n x d x = \frac {2}{\pi} \left(\int_ {0} ^ {\pi} \cos n x d x + \int_ {0} ^ {\pi} x \cos n x d x\right) \\ &= \frac {2}{\pi} \left[ \frac {1}{n} \sin n x \Big | _ {0} ^ {\pi} + \frac {1}{n} \int_ {0} ^ {\pi} x d (\sin n x) \right] = \frac {2}{n \pi} \int_ {0} ^ {\pi} x d (\sin n x) \\ &= \frac {2}{n \pi} \left(x \sin n x \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \sin n x d x\right) = - \frac {2}{n \pi} \int_ {0} ^ {\pi} \sin n x d x \\ &= \frac {2}{n \pi} \cdot \frac {\cos n x}{n} \Big | _ {0} ^ {\pi} = \frac {2}{n ^ {2} \pi} (\cos n \pi - 1) = \frac {2}{n ^ {2} \pi} [ (- 1) ^ {n} - 1 ]. \end{aligned}</equation>于是，<equation>a _ {2 n - 1} = \frac {2}{(2 n - 1) ^ {2} \pi} [ (- 1) ^ {2 n - 1} - 1 ] = \frac {2}{(2 n - 1) ^ {2} \pi} (- 1 - 1) = \frac {- 4}{(2 n - 1) ^ {2} \pi}.</equation>因此，<equation>\lim _ {n \rightarrow \infty} n ^ {2} \sin a _ {2 n - 1} = \lim _ {n \rightarrow \infty} n ^ {2} \sin \frac {- 4}{(2 n - 1) ^ {2} \pi} = \lim _ {n \rightarrow \infty} \frac {- 4 n ^ {2}}{(2 n - 1) ^ {2} \pi} = - \frac {1}{\pi}.</equation>

---

**2023年第13题 | 填空题 | 5分**
13. 设 f(x)为周期为2的周期函数，且 f(x)=1-x,x∈[0,1]，若 f(x)<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} a_{n} \cos n \pi x</equation>，则<equation>\sum_{n=1}^{\infty} a_{2n}=</equation>___.
**解析: **解 由于 f(x) 的傅里叶级数展开式为余弦级数，故 f(x)为偶函数.由余弦级数的系数计算公式可知，当 n≥1时，<equation>\begin{aligned} a _ {n} &= 2 \int_ {0} ^ {1} (1 - x) \cos n \pi x \mathrm {d} x = 2 \left(\int_ {0} ^ {1} \cos n \pi x \mathrm {d} x - \int_ {0} ^ {1} x \cos n \pi x \mathrm {d} x\right) \\ &= 2 \left[ \frac {1}{n \pi} \sin n \pi x \Big | _ {0} ^ {1} - \frac {1}{n \pi} \int_ {0} ^ {1} x \mathrm {d} (\sin n \pi x) \right] = - \frac {2}{n \pi} \int_ {0} ^ {1} x \mathrm {d} (\sin n \pi x) \\ &= - \frac {2}{n \pi} \left(x \sin n \pi x \Big | _ {0} ^ {1} - \int_ {0} ^ {1} \sin n \pi x \mathrm {d} x\right) = \frac {2}{n \pi} \int_ {0} ^ {1} \sin n \pi x \mathrm {d} x \\ &= \frac {2}{n \pi} \cdot \left(- \frac {\cos n \pi x}{n \pi}\right) \Big | _ {0} ^ {1} = \frac {- 2}{n ^ {2} \pi^ {2}} (\cos n \pi - 1). \end{aligned}</equation>于是，<equation>a _ {2 n} = \frac {- 2}{(2 n) ^ {2} \pi^ {2}} \left(\cos 2 n \pi - 1\right) = \frac {- 1}{2 n ^ {2} \pi^ {2}} (1 - 1) = 0.</equation>因此，<equation>\sum_{n=1}^{\infty} a_{2n}=0.</equation>

---

**2013年第3题 | 选择题 | 4分 | 答案: C**
3. 设<equation>f(x)=\left| x-\frac{1}{2}\right|, b_{n}=2\int_{0}^{1} f(x)\sin(n\pi x)\mathrm{d}x(n=1,2,\cdots).</equation>令<equation>S(x)=\sum_{n=1}^{\infty}b_{n}\sin(n\pi x),</equation>则<equation>S\left(-\frac{9}{4}\right)=</equation>(    )

A.<equation>\frac{3}{4}</equation>B.<equation>\frac{1}{4}</equation>C.<equation>-\frac{1}{4}</equation>D.<equation>-\frac{3}{4}</equation>
答案: C
**解析: **解设<equation>F ( x )</equation>是以2为周期的奇函数，且当<equation>- 1 \leqslant x \leqslant 1</equation>时，<equation>F (x) = \left\{ \begin{array}{l l} f (x), & 0 < x < 1, \\ - f (- x), & - 1 < x < 0, \\ 0, & x = 0, \pm 1. \end{array} \right.</equation>如右图所示，<equation>F ( x )</equation>的傅里叶系数为<equation>\widetilde {a} _ {n} = \int_ {- 1} ^ {1} F (x) \cos n \pi x \mathrm {d} x = 0, n = 0, 1, 2, \dots ,</equation>

---


