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


