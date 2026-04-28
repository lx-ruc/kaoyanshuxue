#### 1. 二重积分的计算法

(1) 利用直角坐标系计算二重积分若积分区域 D是 X型域，其不等式表示为<equation>D: \left\{ \begin{array}{l l} a \leqslant x \leqslant b, \\ \varphi_{1}(x) \leqslant y \leqslant \varphi_{2}(x), \end{array} \right.</equation><equation>I = \iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = \int_{a}^{b} \mathrm{d}x \int_{\varphi_{1}(x)}^{\varphi_{1}(x)} f(x,y)\mathrm{d}y.</equation>若积分区域 D是 Y型域，其不等式表示为<equation>D: \left\{ \begin{array}{l l} c \leqslant y \leqslant d, \\ \varphi_{1}(y) \leqslant x \leqslant \varphi_{2}(y), \end{array} \right.</equation><equation>I = \iint_{D} f(x,y)\mathrm{d}x\mathrm{d}y = \int_{c}^{d} \mathrm{d}y \int_{\varphi_{1}(y)}^{\varphi_{1}(y)} f(x,y)\mathrm{d}x.</equation>

则

(2) 利用极坐标计算二重积分

<equation>\textcircled{1}</equation>如果极点<equation>O</equation>在区域<equation>D</equation>内，此时<equation>D</equation>可用不等式

---

$$

\left\{ \begin{array}{l l} 0 \leqslant \theta \leqslant 2 \pi , \\ 0 \leqslant r \leqslant \varphi (\theta) \end{array} \right. \text {表 示 ， 则}

$$

<equation>\begin{array}{l} \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} \theta \mathrm {d} r \\ = \int_ {0} ^ {2 \pi} \mathrm {d} \theta \int_ {0} ^ {\varphi (\theta)} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} r. \\ \end{array}</equation>

<equation>\textcircled{2}</equation>如果极点 O在区域 D的边界上，此时 D可用不等式<equation>\left\{ \begin{array}{l l} \alpha \leqslant \theta \leqslant \beta , \\ 0 \leqslant r \leqslant \varphi (\theta) \end{array} \right.</equation>表示，则

<equation>\begin{array}{l} \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} \theta \mathrm {d} r \\ = \int_ {\alpha} ^ {\beta} \mathrm {d} \theta \int_ {0} ^ {\varphi (\theta)} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} r. \\ \end{array}</equation>

<equation>\textcircled{3}</equation>如果极点<equation>O</equation>在区域<equation>D</equation>外，此时<equation>D</equation>可用不等式<equation>\left\{ \begin{array}{l l} \alpha \leqslant \theta \leqslant \beta , \\ \varphi_{1}(\theta) \leqslant r \leqslant \varphi_{2}(\theta) \end{array} \right.</equation>来表示，则

<equation>\begin{array}{l} \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \iint_ {D} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} \theta \mathrm {d} r \\ = \int_ {a} ^ {\beta} \mathrm {d} \theta \int_ {\varphi_ {1} (\theta)} ^ {\varphi_ {2} (\theta)} f (r \cos \theta , r \sin \theta) \cdot r \mathrm {d} r. \\ \end{array}</equation>

2. 三重积分的计算法

(1) 利用直角坐标系计算三重积分

<equation>\textcircled{1}</equation>“先一后二”，即将三重积分化为：

---

<equation>\iiint_ {\Omega} f (x, y, z) \mathrm {d} v = \left\{ \begin{array}{l l} \iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} y \int_ {z _ {1} (x, y)} ^ {z _ {2} (x, y)} f (x, y, z) \mathrm {d} z, \\ \iint_ {D _ {x y}} \mathrm {d} y \mathrm {d} z \int_ {z _ {1} (y, z)} ^ {z _ {2} (y, z)} f (x, y, z) \mathrm {d} x, \\ \iint_ {D _ {x y}} \mathrm {d} x \mathrm {d} z \int_ {y _ {1} (x, z)} ^ {y _ {2} (x, z)} f (x, y, z) \mathrm {d} y. \end{array} \right.</equation>

<equation>\textcircled{2}</equation>“先二后一”，即将三重积分化为：

<equation>\iiint_ {\Omega} f (x, y, z) \mathrm {d} v = \left\{ \begin{array}{l} \int_ {c} ^ {d} \mathrm {d} z \iint_ {D (z)} f (x, y, z) \mathrm {d} x \mathrm {d} y, \\ \int_ {a} ^ {b} \mathrm {d} x \iint_ {D (x)} f (x, y, z) \mathrm {d} y \mathrm {d} z, \\ \int_ {m} ^ {n} \mathrm {d} y \iint_ {D (x)} f (x, y, z) \mathrm {d} x \mathrm {d} z. \end{array} \right.</equation>

(2) 利用柱坐标计算三重积分

<equation>\mathrm {d} v = r \mathrm {d} r \mathrm {d} \theta \mathrm {d} z.</equation>

<equation>\textcircled{1}</equation>柱坐标系下的体积元素

<equation>\textcircled{2}</equation>柱坐标系下的三次积分的先后次序一般为

<equation>I = \int \mathrm {d} \theta \int r \mathrm {d} r \int f (r \cos \theta , r \sin \theta , z) \mathrm {d} z.</equation>

<equation>\textcircled{3}</equation>若空间区域<equation>\varOmega</equation>可以用不等式

<equation>\left\{ \begin{array}{l} z _ {1} (r, \theta) \leqslant z \leqslant z _ {2} (r, \theta), \\ r _ {1} (\theta) \leqslant r \leqslant r _ {2} (\theta), \\ \alpha \leqslant \theta \leqslant \beta \end{array} \right.</equation>

---


