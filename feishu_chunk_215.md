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


