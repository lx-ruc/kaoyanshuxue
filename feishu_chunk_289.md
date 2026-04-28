#### 3. 性质

<equation>\textcircled{1}</equation>若随机变量<equation>X\sim \left( \begin{array}{c c c c c} x_{1} & x_{2} & \dots & x_{n} & \dots \\ p_{1} & p_{2} & \dots & p_{n} & \dots \end{array} \right), Y = g(X)</equation>，则

<equation>E Y = \sum_ {k} g \left(x _ {k}\right) p _ {k}.</equation>

<equation>\textcircled{2}</equation>若随机变量 X的密度函数为<equation>f_{X}(x),Y=g(X)</equation>则

<equation>E Y = \int_ {\mathbf {R}} g (x) f _ {X} (x) \mathrm {d} x.</equation>

<equation>\textcircled{3}</equation>若随机变量<equation>(X, Y) \sim p_{ij}, Z = g(X, Y)</equation>，则

<equation>E Z = \sum_ {i} \sum_ {j} g \left(x _ {i}, y _ {j}\right) p _ {i j}.</equation>

<equation>\textcircled{4}</equation>若随机变量<equation>(X, Y)</equation>的联合密度函数为<equation>f(x, y), Z = g(X, Y)</equation>，则

<equation>E Z = \iint_ {\mathbb {R} ^ {2}} g (x, y) f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{5}</equation>若随机变量<equation>X\sim \left( \begin{array}{cc}\xi & \eta \\ p & q \end{array} \right)</equation>，则

<equation>E X = p E \xi + q E \eta .</equation>

<equation>\textcircled{1}</equation>线性性：对任意<equation>a,b,c\in \mathbf{R}</equation>及随机变量<equation>X,Y</equation>，若EX，EY存在，则


<equation>E (a X + b Y + c) = a E X + b E Y + c.</equation>

---

<equation>\textcircled{2}</equation>若随机变量 X与 Y相互独立，且 EX，EY存在，则

<equation>E (X Y) = E X \cdot E Y.</equation>


若数学期望<equation>E(X - EX)^{2}</equation>存在，则称其为随机变量<equation>X</equation>的方差，并记为<equation>DX</equation>.同时称<equation>\sqrt{DX}</equation>为随机变量<equation>X</equation>的标准差.


若数学期望<equation>E[(X - EX)(Y - EY)]</equation>存在，则称其为随机变量<equation>X</equation>与<equation>Y</equation>的协方差，并记为<equation>\operatorname{Cov}(X, Y)</equation>.


<equation>\textcircled{1}</equation>对任意随机变量 X，<equation>D X\geqslant0.</equation>

<equation>\textcircled{2}</equation>若 C为固定常数，则<equation>D C=0.</equation>

<equation>\textcircled{3}</equation>常数<equation>a\in\mathbf{R}</equation>，则<equation>D(aX)=a^{2}DX.</equation>

<equation>\textcircled{4} D ( X \pm Y ) = D X + D Y \pm 2 \operatorname{C o v} ( X, Y ).</equation>

<equation>\textcircled{5}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则

<equation>D (X \pm Y) = D X + D Y.</equation>

<equation>\textcircled{6} D X=E X^{2}-(E X)^{2}.</equation>

<equation>\textcircled{7}</equation><equation>\operatorname{C o v} ( X, Y )=\operatorname{C o v} ( Y, X ).</equation>

<equation>\textcircled{8} \operatorname{C o v} ( a X, Y )=a \operatorname{C o v} ( X, Y ).</equation>

---


