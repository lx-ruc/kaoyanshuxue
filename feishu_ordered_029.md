# 张宇数学公式手册

## 第一部分高等数学

### 第五章 多元函数微分学

#### 二、隐函数求导法

<equation>\frac {\partial z}{\partial x} = \frac {\partial z}{\partial u} \cdot \frac {\partial u}{\partial x} + \frac {\partial z}{\partial v} \cdot \frac {\partial v}{\partial x},</equation>

<equation>\frac {\partial z}{\partial y} = \frac {\partial z}{\partial u} \cdot \frac {\partial u}{\partial y} + \frac {\partial z}{\partial v} \cdot \frac {\partial u}{\partial y}.</equation>


偏导数连续<equation>\Rightarrow</equation>函数可微<equation>\Rightarrow</equation>函数连续<equation>\Rightarrow \lim_{y \to y_0} f(x,y)</equation>存在.偏导数存在.


（二元隐函数存在定理）设函数<equation>F ( x,y,z)</equation>在点<equation>P_{0}(x_{0},y_{0},z_{0})</equation>的某邻域内有连续偏导数，并且

<equation>F \left(x _ {0}, y _ {0}, z _ {0}\right) = 0, F _ {z} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \neq 0,</equation>

则方程<equation>F ( x,y,z)=0</equation>在点<equation>P_{0}\left(x_{0},y_{0},z_{0}\right)</equation>的某一邻域内恒能确定唯一的连续函数<equation>z=f(x,y)</equation>，且满足：

<equation>\textcircled{1}</equation><equation>z_{0} = f(x_{0}, y_{0})</equation>;

<equation>\textcircled{2} F ( x,y,f ( x,y) ) \equiv 0;</equation>

<equation>\textcircled{3} z=f(x,y)</equation>具有连续偏导数，且

<equation>\frac {\partial z}{\partial x} = - \frac {F _ {x} ^ {\prime} (x , y , z)}{F _ {z} ^ {\prime} (x , y , z)},</equation>

<equation>\frac {\partial z}{\partial y} = - \frac {F _ {y} ^ {\prime} (x , y , z)}{F _ {z} ^ {\prime} (x , y , z)}.</equation>

---


#### 四、偏导数在几何中的应用

设函数<equation>z = f(x,y)</equation>在点<equation>P_{0}(x_{0},y_{0})</equation>的某个邻域内有定义，<equation>l = \{m,n\}</equation>是一给定的向量，过<equation>P_{0}</equation>点沿方向1作射线<equation>L</equation>，在射线<equation>L</equation>上<equation>P_{0}</equation>点的邻域内取一点<equation>P(x_{0} + \Delta x,y_{0} + \Delta y)</equation>，当点<equation>P</equation>沿射线<equation>L</equation>趋向<equation>P_{0}</equation>点时，如果极限

<equation>\lim _ {P \rightarrow P _ {n}} \frac {f \left(x _ {0} + \Delta x , y _ {0} + \Delta y\right) - f \left(x _ {0} , y _ {0}\right)}{\left| P P _ {0} \right|}</equation>

存在，则此极限值称为函数<equation>z = f(x,y)</equation>在<equation>P_{0}</equation>点沿方向<equation>l</equation>的方向导数，记为<equation>\left.\frac{\partial f}{\partial l}\right|_{P}</equation>.


设函数<equation>u = F(x,y,z)</equation>在点<equation>M_{0}(x_{0},y_{0},z_{0})</equation>处可微，<equation>l = \{m,n,p\}</equation>是任一给定的向量，则

<equation>\left. \frac {\partial F}{\partial l} \right| _ {M _ {i}} = \operatorname {g r a d} F | _ {M _ {i}} \cdot l ^ {0}.</equation>


(1) 空间曲线<equation>\left\{ \begin{array}{l l} x=\varphi (t), \\ y=\psi (t), \\ z=w (t) \end{array} \right.</equation>在<equation>t=t_{0}</equation>处的切线与法平

---


#### 2. 充分条件

面方程

<equation>\textcircled{1}</equation>切线方程

<equation>\frac {x - x _ {0}}{\varphi^ {\prime} \left(t _ {0}\right)} = \frac {y - y _ {0}}{\psi^ {\prime} \left(t _ {0}\right)} = \frac {z - z _ {0}}{w ^ {\prime} \left(t _ {0}\right)}.</equation>

<equation>\textcircled{2}</equation>法平面方程

<equation>\varphi^ {\prime} \left(t _ {0}\right) \left(x - x _ {0}\right) + \psi^ {\prime} \left(t _ {0}\right) \left(y - y _ {0}\right) + w ^ {\prime} \left(t _ {0}\right) \left(z - z _ {0}\right) = 0.</equation>

(2) 曲面<equation>F ( x,y,z)=0</equation>的切平面与法线方程


<equation>\begin{array}{l} F _ {x} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(x - x _ {0}\right) + F _ {y} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(y - y _ {0}\right) + \\ F _ {z} ^ {\prime} \left(x _ {0}, y _ {0}, z _ {0}\right) \left(z - z _ {0}\right) = 0. \\ \end{array}</equation>

<equation>\textcircled{2}</equation>法线方程

<equation>\frac {x - x _ {0}}{F _ {x} ^ {\prime} \left(x _ {0} , y _ {0} , z _ {0}\right)} = \frac {y - y _ {0}}{F _ {y} ^ {\prime} \left(x _ {0} , y _ {0} , z _ {0}\right)} = \frac {z - z _ {0}}{F _ {z} ^ {\prime} \left(x _ {0} , y _ {0} , z _ {0}\right)}.</equation>


设<equation>z = f(x,y)</equation>在点<equation>(x_0,y_0)</equation>处取得极值，且<equation>f(x,y)</equation>在点<equation>(x_0,y_0)</equation>处存在偏导数，则必有

<equation>f _ {x} ^ {\prime} \left(x _ {0}, y _ {0}\right) = 0, f _ {y} ^ {\prime} \left(x _ {0}, y _ {0}\right) = 0.</equation>


设<equation>z = f(x,y)</equation>在点<equation>(x_0,y_0)</equation>具有连续二阶偏导数，并设<equation>(x_0,y_0)</equation>是<equation>f(x,y)</equation>的驻点，记<equation>A = f_{xx}^{\prime \prime}(x_0,y_0)</equation>，<equation>B = f_{xy}^{\prime \prime}(x_0,y_0)</equation>，<equation>C = f_{xy}^{\prime \prime}(x_0,y_0)</equation>，则

---


#### 3. 条件极值

<equation>\textcircled{1}</equation>当<equation>AC - B^{2} > 0,A > 0</equation>时，<equation>f(x_{0},y_{0})</equation>为极小值；

<equation>\textcircled{2}</equation>当<equation>AC - B^{2} > 0, A < 0</equation>时，<equation>f(x_{0},y_{0})</equation>为极大值；

<equation>\textcircled{3}</equation>当<equation>AC - B^{2} < 0</equation>时，<equation>f(x_{0},y_{0})</equation>不是极值；

<equation>\textcircled{4}</equation>当<equation>AC-B^{2}=0</equation>时，不能确定<equation>f(x_{0},y_{0})</equation>是否为极值.


求<equation>z = f(x,y)</equation>在条件<equation>\varphi (x,y) = 0</equation>下的极值. 一般方法为：

<equation>\textcircled{1}</equation>构造拉格朗日函数

<equation>F (x, y, \lambda) = f (x, y) + \lambda \varphi (x, y).</equation>

<equation>\textcircled{2}</equation>将 F(x,y,<equation>\lambda</equation>)分别对 x,y,<equation>\lambda</equation>求偏导数，构造下列方程组：

<equation>\left\{ \begin{array}{l} F _ {x} ^ {\prime} = f _ {x} ^ {\prime} (x, y) + \lambda \varphi_ {x} ^ {\prime} (x, y) = 0, \\ F _ {y} ^ {\prime} = f _ {y} ^ {\prime} (x, y) + \lambda \varphi_ {y} ^ {\prime} (x, y) = 0, \\ F _ {\lambda} ^ {\prime} = \varphi (x, y) = 0, \end{array} \right.</equation>

解出<equation>(x,y)</equation>，这是可能极值点的坐标.

<equation>\textcircled{3}</equation>判定上述点是否为极值点，如果是，求出该点的函数值 f(x,y).

---


### 第六章 多元函数积分学
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


#### 二、重积分的应用（数学二不作要求）

表示，则

<equation>\begin{array}{l} \iiint_ {\Omega} f (x, y, z) \mathrm {d} v \\ = \iiint_ {\Omega} f (r \cos \theta , r \sin \theta , z) r \mathrm {d} r \mathrm {d} \theta \mathrm {d} z \\ = \int_ {\alpha} ^ {\beta} \mathrm {d} \theta \int_ {r _ {1} (\theta)} ^ {r _ {2} (\theta)} r \mathrm {d} r \int_ {z _ {1} (r, \theta)} ^ {z _ {2} (r, \theta)} f (r \cos \theta , r \sin \theta , z) \mathrm {d} z. \\ \end{array}</equation>

(3) 利用球坐标计算三重积分

<equation>\textcircled{1}</equation>球坐标与直角坐标的关系

<equation>\left\{ \begin{array}{l} x = r \sin \varphi \cos \theta , \\ y = r \sin \varphi \sin \theta , \\ z = r \cos \varphi . \end{array} \right.</equation>

<equation>\textcircled{2}</equation>球坐标系下的体积元素

<equation>\mathrm {d} v = r ^ {2} \sin \varphi \mathrm {d} r \mathrm {d} \theta \mathrm {d} \varphi .</equation>

<equation>\textcircled{3}</equation>球坐标系下三次积分的先后次序一般为<equation>I = \int \mathrm{d}\theta \int \mathrm{d}\varphi \int f(r\sin \varphi \cos \theta ,r\sin \varphi \sin \theta ,r\cos \varphi)r^2\sin \varphi \mathrm{d}r.</equation>

<equation>\textcircled{1}</equation>曲面面积的计算公式


(1) 几何应用

<equation>A = \iint_ {D} \sqrt {1 + \left(f _ {x} ^ {\prime}\right) ^ {2} + \left(f _ {y} ^ {\prime}\right) ^ {2}} \mathrm {d} \sigma .</equation>

---

<equation>\textcircled{2}</equation>体积

<equation>V = \iiint_ {\Omega} \mathrm {d} v = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{3}</equation>平面图形 D的形心<equation>(x,y)</equation>为

<equation>\bar {x} = \frac {\iint_ {D} x \mathrm {d} x \mathrm {d} y}{\iint_ {D} \mathrm {d} x \mathrm {d} y}, \quad \bar {y} = \frac {\iint_ {D} y \mathrm {d} x \mathrm {d} y}{\iint_ {D} \mathrm {d} x \mathrm {d} y}.</equation>

<equation>\textcircled{4}</equation>空间立体<equation>\varOmega</equation>的形心<equation>( \bar{x},\bar{y},\bar{z} )</equation>为

<equation>\bar {x} = \frac {\iiint_ {\Omega} x \mathrm {d} v}{\iiint_ {\Omega} \mathrm {d} v}, \bar {y} = \frac {\iiint_ {\Omega} y \mathrm {d} v}{\iiint_ {\Omega} \mathrm {d} v}, \bar {z} = \frac {\iiint_ {\Omega} z \mathrm {d} v}{\iiint_ {\Omega} \mathrm {d} v}.</equation>

(2) 物理应用

<equation>\textcircled{1}</equation>平面薄片的质心坐标<equation>(\overline{x},\overline{y})</equation>为

<equation>\bar {x} = \frac {\iint_ {D} x \rho (x , y) \mathrm {d} x \mathrm {d} y}{\iint_ {D} \rho (x , y) \mathrm {d} x \mathrm {d} y}, \quad \bar {y} = \frac {\iint_ {D} y \rho (x , y) \mathrm {d} x \mathrm {d} y}{\iint_ {D} \rho (x , y) \mathrm {d} x \mathrm {d} y}</equation>

<equation>\textcircled{2}</equation>立体的质心坐标<equation>( \overline{x},\overline{y},\overline{z} )</equation>为

<equation>\bar {x} = \frac {\iiint_ {\Omega} x \rho (x , y , z) \mathrm {d} v}{\iiint_ {\Omega} \rho (x , y , z) \mathrm {d} v}, \bar {y} = \frac {\iiint_ {\Omega} y \rho (x , y , z) \mathrm {d} v}{\iiint_ {\Omega} \rho (x , y , z) \mathrm {d} v},</equation>

---

<equation>\bar {z} = \frac {\iiint_ {\Omega} z \rho (x , y , z) \mathrm {d} v}{\iiint_ {\Omega} \rho (x , y , z) \mathrm {d} v}</equation>

<equation>\textcircled{3}</equation>平面薄片绕轴的转动惯量

绕<equation>x</equation>轴的转动惯量：<equation>I_{x} = \iint_{D} y^{2}\rho (x,y)\mathrm{d}x\mathrm{d}y.</equation>

绕<equation>y</equation>轴的转动惯量：<equation>I_{y} = \iint_{D} x^{2}\rho (x,y)\mathrm{d}x\mathrm{d}y.</equation>

<equation>\textcircled{4}</equation>立体绕轴的转动惯量

绕<equation>x</equation>轴的转动惯量：<equation>I_{x} = \iint_{D}\left(y^{2} + z^{2}\right)\rho (x,y,z)\mathrm{d}v.</equation>

绕<equation>y</equation>轴的转动惯量：<equation>I_{y} = \iint_{Q}\left(x^{2} + z^{2}\right)\rho (x,y,z)\mathrm{d}v.</equation>

绕<equation>z</equation>轴的转动惯量：<equation>I_{z} = \iint_{D}(x^{2} + y^{2})\rho (x,y,z)\mathrm{d}v.</equation>

<equation>\textcircled{5}</equation>平面薄片对质点的引力<equation>F = \{F_{x}, F_{y}\}</equation>为：

<equation>F _ {x} = \iint_ {D} \frac {G m \rho (x , y) \left(x - x _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} x \mathrm {d} y,</equation>

<equation>F _ {y} = \iint_ {D} \frac {G m \rho (x , y) \left(y - y _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{6}</equation>立体对质点的引力<equation>F = \{F_{x}, F_{y}, F_{z}\}</equation>为

---


#### 1. 曲线积分的计算公式

<equation>F _ {x} = \iiint_ {\Omega} \frac {G m \varphi (x , y , z) \left(x - x _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} v,</equation>

<equation>F _ {y} = \iiint_ {a} \frac {G m \rho (x , y , z) \left(y - y _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} d v,</equation>

<equation>F _ {z} = \iiint_ {\Omega} \frac {G m p (x , y , z) \left(z - z _ {0}\right)}{\left[ \left(x - x _ {0}\right) ^ {2} + \left(y - y _ {0}\right) ^ {2} + \left(z - z _ {0}\right) ^ {2} \right] ^ {\frac {3}{2}}} \mathrm {d} v.</equation>


(1) 化成定积分

<equation>\begin{array}{l} \int_ {\Gamma} f (x, y, z) \mathrm {d} s = \int_ {\alpha} ^ {\beta} f \left[ \varphi (t), \psi (t), w (t) \right]. \\ \sqrt {\varphi^ {\prime 2} (t) + \psi^ {\prime 2} (t) + w ^ {\prime 2} (t)} \mathrm {d} t \quad (\alpha \leqslant \beta), \\ \int_ {\Gamma} P (x, y, z) \mathrm {d} x + Q (x, y, z) \mathrm {d} y + R (x, y, z) \mathrm {d} z \\ = \int_ {\alpha} ^ {\beta} \left\{P \left[ \varphi (t), \psi (t), w (t) \right] \varphi^ {\prime} (t) + Q \left[ \varphi (t), \psi (t), w (t) \right] \right. \\ \psi^ {\prime} (t) + R \left[ \varphi (t), \psi (t), w (t) \right] w ^ {\prime} (t) \} \mathrm {d} t, \\ \end{array}</equation>

其中<equation>\alpha</equation>为<equation>\varGamma</equation>的起点参数<equation>t</equation>的值，<equation>\beta</equation>为<equation>\varGamma</equation>的终点参数<equation>t</equation>的值.

---


#### 2. 全微分求积

(2) 格林公式

<equation>\begin{array}{l} \oint_ {L} P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y \\ = \iint_ {D} \left(\frac {\partial Q}{\partial x} - \frac {\partial P}{\partial y}\right) \mathrm {d} x \mathrm {d} y, \\ \end{array}</equation>

其中 L为正向闭曲线.


<equation>\int_{L} P(x,y)\mathrm{d}x + Q(x,y)\mathrm{d}y</equation>与路径无关的充要条件是<equation>\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}</equation>.

(4) 斯托克斯公式

<equation>\begin{array}{l} \int_ {P} P \mathrm {d} x + Q \mathrm {d} y + R \mathrm {d} z \\ = \iint_ {x} \left| \begin{array}{c c c} \cos \alpha & \cos \beta & \cos \gamma \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right| \mathrm {d} S. \\ \end{array}</equation>

其中<equation>\cos \alpha ,\cos \beta ,\cos \gamma</equation>为<equation>\Sigma</equation>所指定侧法线方向的方向余弦.


<equation>\textcircled{1}</equation>若函数<equation>P ( x,y), Q ( x,y)</equation>在单连通域G内具有一阶连续偏导数，且

<equation>\frac {\partial Q}{\partial x} = \frac {\partial P}{\partial y},</equation>

---

则在<equation>G</equation>内存在二元函数<equation>u(x,y)</equation>，使得

<equation>\mathrm {d} u = P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y.</equation>

<equation>\textcircled{2}</equation>求积公式

<equation>u (x, y) = \int_ {x _ {0}} ^ {x} P \left(x, y _ {0}\right) \mathrm {d} x + \int_ {y _ {0}} ^ {y} Q (x, y) \mathrm {d} y + C.</equation>

3. 曲面积分的计算公式

(1) 化为二重积分

<equation>\textcircled{1}</equation>对面积的曲面积分

<equation>\begin{array}{l} \iint_ {\Sigma} f (x, y, z) \mathrm {d} S \\ = \iint_ {D _ {x y}} f [ x, y, z (x, y) ] \cdot \sqrt {1 + z _ {x} ^ {\prime 2} + z _ {y} ^ {\prime 2}} \mathrm {d} x \mathrm {d} y, \\ \end{array}</equation>

其中<equation>D_{xy}</equation>是曲面<equation>\Sigma</equation>在<equation>xOy</equation>平面上的投影.

<equation>\textcircled{2}</equation>对坐标的曲面积分

<equation>\begin{array}{l} \iint_ {\Sigma} P (x, y, z) \mathrm {d} y \mathrm {d} z \frac {\Sigma \text {为 单 值 函 数} x = x (y , z)}{\Sigma} \\ \pm \iint_ {D _ {y z}} P [ x (y, z), y, z ] \mathrm {d} y \mathrm {d} z, (\text {前} “ + ” \text {后} “ - ”) \\ \iint_ {\Sigma} Q (x, y, z) \mathrm {d} z \mathrm {d} x \frac {\Sigma \text {为 单 值 函 数} y = y (x , z)}{\Sigma} \\ \pm \iint_ {D _ {x z}} Q [ x, y (x, z), z ] \mathrm {d} z \mathrm {d} x, (\text {右} “ + ” \text {左} “ - ”) \\ \end{array}</equation>

---


#### (2) 曲面积分

<equation>\begin{array}{l} \iint_ {\Sigma} R (x, y, z) \mathrm {d} x \mathrm {d} y \frac {\Sigma \text {为 单 值 函数} z = z (x , y)}{} \\ \pm \iint_ {D _ {x y}} R [ x, y, z (x, y) ] \mathrm {d} x \mathrm {d} y. (\text {上} “ + ” \text {下} “ - ”) \\ \end{array}</equation>

(2) 高斯公式

<equation>\begin{array}{l} \oiint_ {\Sigma} P \mathrm {d} y \mathrm {d} z + Q \mathrm {d} z \mathrm {d} x + R \mathrm {d} x \mathrm {d} y \\ = \iiint_ {\Omega} \left(\frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z}\right) \mathrm {d} v, \\ \end{array}</equation>

其中<equation>\Sigma</equation>为闭曲面的外侧，<equation>\Omega</equation>是<equation>\Sigma</equation>所围立体.


(1) 曲线积分

<equation>\int_ {L} P \mathrm {d} x + Q \mathrm {d} y = \int_ {L} \left(P \cos \alpha + Q \cos \beta\right) \mathrm {d} s,</equation>

其中<equation>\alpha (x,y),\beta (x,y)</equation>为有向曲线弧<equation>L</equation>上点<equation>(x,y)</equation>处的切线向量的方向角.

<equation>\begin{array}{l} \int_ {\Gamma} P \mathrm {d} x + Q \mathrm {d} y + R \mathrm {d} z \\ = \int_ {\Gamma} \left(P \cos \alpha + Q \cos \beta + R \cos \gamma\right) \mathrm {d} s, \\ \end{array}</equation>

其中<equation>\alpha (x,y,z),\beta (x,y,z),\gamma (x,y,z)</equation>是有向曲线弧<equation>\varGamma</equation>上点<equation>(x,y,z)</equation>处的切线向量的方向角.

---


#### (2) 散度和旋度

<equation>\begin{array}{l} \iint_ {\Sigma} P \mathrm {d} y \mathrm {d} z + Q \mathrm {d} z \mathrm {d} x + R \mathrm {d} x \mathrm {d} y \\ = \iint_ {\Sigma} \left(P \cos \alpha + Q \cos \beta + R \cos \gamma\right) \mathrm {d} S, \\ \end{array}</equation>

其中<equation>\cos \alpha ,\cos \beta ,\cos \gamma</equation>是有向曲面上点<equation>(x,y,z)</equation>处法向量的方向余弦.


(1) 梯度

<equation>\operatorname {g r a d} f (x, y) = \frac {\partial f}{\partial x} i + \frac {\partial f}{\partial y} j,</equation>

<equation>\operatorname {g r a d} f (x, y, z) = \frac {\partial f}{\partial x} i + \frac {\partial f}{\partial y} j + \frac {\partial f}{\partial z} k.</equation>


若<equation>A=P(x,y,z)i+Q(x,y,z)j+R(x,y,z)k</equation>，则<equation>\textcircled{1}</equation>散度

<equation>\operatorname {d i v} A = \frac {\partial P}{\partial x} + \frac {\partial Q}{\partial y} + \frac {\partial R}{\partial z};</equation>

<equation>\textcircled{2}</equation>旋度

<equation>\operatorname {r o t} A = \left| \begin{array}{c c c} i & j & k \\ \frac {\partial}{\partial x} & \frac {\partial}{\partial y} & \frac {\partial}{\partial z} \\ P & Q & R \end{array} \right|.</equation>

---


### 第七章 级数
#### 1. 数项级数的定义与性质

(1) 定义

<equation>\textcircled{1}</equation><equation>\sum_{n=1}^{\infty} u_{n}=u_{1}+u_{2}+\cdots+u_{n}+\cdots,</equation><equation>S_{n}=\sum_{k=1}^{n} u_{k}</equation>称为级数的部分和.

<equation>\textcircled{2}</equation>若数项级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>的部分和数列<equation>\{S_n\}</equation>有极限，则称级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>收敛，极限值<equation>\lim_{n\to \infty} S_n = A</equation>称为此级数的和，并写作<equation>\sum_{n = 1}^{\infty} u_{n} = A.</equation>当<equation>\lim_{n\to \infty} S_n</equation>不存在时，则称级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>发散.

(2) 级数的基本性质及收敛的必要条件

<equation>\textcircled{1}</equation>设<equation>\sum_{n = 1}^{\infty} u_{n}, \sum_{n = 1}^{\infty} v_{n}</equation>都收敛，其和分别为<equation>A, B</equation>，则

---


#### 2. 正项级数及其敛散性判别法

<equation>\sum_{n = 1}^{\infty}\left(u_{n}\pm v_{n}\right)</equation>必收敛，且<equation>\sum_{n = 1}^{\infty}\left(u_{n}\pm v_{n}\right) = A\pm B</equation>

<equation>\textcircled{2}</equation>设<equation>k</equation>为非零常数，则级数<equation>\sum_{n = 1}^{\infty} u_n</equation>与<equation>\sum_{n = 1}^{\infty} k u_n</equation>有相同的敛散性；

<equation>\textcircled{3}</equation>改变级数的前有限项，不影响级数的敛散性；

<equation>\textcircled{4}</equation>级数收敛的必要条件：若<equation>\sum_{n=1}^{\infty} u_n</equation>收敛，则<equation>\lim_{n\to \infty} u_n = 0</equation>；

<equation>\textcircled{5}</equation>收敛的级数在不改变各项次序的前提下任意加括号得到的新级数仍然收敛，且和不变.


(1) 正项级数收敛的基本定理

设<equation>\{S_n\}</equation>是正项级数<equation>\sum_{n=1}^{\infty} u_n</equation>的部分和数列，则正项级数<equation>\sum_{n=1}^{\infty} u_n</equation>收敛的充要条件是数列<equation>\{S_n\}</equation>有界.

(2) 正项级数的比较判别法

（正项级数比较判别法的非极限形式）设<equation>\sum_{n = 1}^{\infty}u_n</equation><equation>\sum_{n = 1}^{\infty}v_n</equation>都是正项级数，并设<equation>u_{n}\leqslant v_{n}(n\geqslant N_{0})</equation>，则

<equation>\textcircled{1}</equation>若<equation>\sum_{n = 1}^{\infty} v_{n}</equation>收敛，则<equation>\sum_{n = 1}^{\infty} u_{n}</equation>收敛；

---

<equation>\textcircled{2}</equation>若<equation>\sum_{n = 1}^{\infty} u_{n}</equation>发散，则<equation>\sum_{n = 1}^{\infty} v_{n}</equation>发散.

（正项级数比较判别法的极限形式）设<equation>\sum_{n = 1}^{\infty}u_n</equation><equation>\sum_{n = 1}^{\infty}v_n</equation>都是正项级数，并设<equation>\lim_{n\to \infty}\frac{u_n}{v_n} = \rho</equation>或为<equation>+\infty</equation>，则

<equation>\textcircled{1}</equation>当<equation>\rho</equation>为非零常数时，级数<equation>\sum_{n=1}^{\infty} u_{n}</equation><equation>\sum_{n=1}^{\infty} v_{n}</equation>有相同的敛散性；

<equation>\textcircled{2}</equation>当<equation>\rho = 0</equation>时，若<equation>\sum_{n = 1}^{\infty} v_{n}</equation>收敛，则必有<equation>\sum_{n = 1}^{\infty} u_{n}</equation>收敛；

<equation>\textcircled{3}</equation>当<equation>\rho = +\infty</equation>时，若<equation>\sum_{n = 1}^{\infty} v_{n}</equation>发散，则必有<equation>\sum_{n = 1}^{\infty} u_{n}</equation>发散.

(3) 正项级数的比值判别法

设<equation>\sum_{n = 1}^{\infty} u_{n}</equation>是正项级数，若<equation>\lim_{n\to \infty}\frac{u_{n + 1}}{u_n} = \rho</equation>或为<equation>+\infty</equation>，则级数<equation>\sum_{n = 1}^{\infty} u_{n}</equation>有

<equation>\textcircled{1}</equation>当<equation>\rho<1</equation>时，收敛；

<equation>\textcircled{2}</equation>当<equation>\rho >1</equation>或<equation>\infty</equation>时，发散；

<equation>\textcircled{3}</equation>当<equation>\rho=1</equation>时，敛散性不确定.

(4) 正项级数的根值判别法

---


#### （1）条件收敛、绝对收敛

将比值判别法中的<equation>\frac{u_{n + 1}}{u_n}</equation>改成<equation>\sqrt[n]{u_n}</equation>，其他文字叙述、结论均不改动，即为根值判别法.


形如

<equation>\sum_{n=1}^{\infty}(-1)^{n-1} u_{n}(u_{n}>0)</equation>或<equation>\sum_{n=1}^{\infty}(-1)^{n} u_{n}(u_{n}>0)</equation>的级数，称为交错级数.


若交错级数<equation>\sum_{n = 1}^{\infty}(-1)^{n - 1}u_n(u_n > 0)</equation>满足条件；

<equation>\textcircled{1}</equation><equation>u_{n}\geqslant u_{n + 1}(n = 1,2,\dots)</equation>;

<equation>\textcircled{2} \lim_{n \to \infty} u_{n}=0,</equation>

则交错级数<equation>\sum_{n=1}^{\infty} (-1)^{n-1} u_n (u_n > 0)</equation>收敛，其和<equation>S \leqslant u_1</equation>，其余项<equation>S - S_n</equation>满足<equation>|S - S_n| \leqslant u_{n+1}</equation>.


若级数<equation>\sum_{n = 1}^{\infty}|u_n|</equation>收敛，则称级数<equation>\sum_{n = 1}^{\infty}u_n</equation>绝对收敛；

若级数<equation>\sum_{n = 1}^{\infty}|u_n|</equation>发散，但级数<equation>\sum_{n = 1}^{\infty}u_n</equation>收敛，则称级数

---


#### 2. 幂级数的收敛半径

若级数<equation>\sum_{n=1}^{\infty} \mid u_{n} \mid</equation>收敛，则级数<equation>\sum_{n=1}^{\infty} u_{n}</equation>收敛，即绝对收敛的级数一定收敛.


形如<equation>\sum_{n=0}^{\infty} a_{n} ( x-x_{0} )^{n}</equation>的函数项级数称为<equation>x_{0}</equation>处的幂级数.


（阿贝尔定理）对幂级数<equation>\sum_{n=0}^{\infty} a_{n} ( x-x_{0} )^{n}</equation>有如下的结论：

<equation>\textcircled{1}</equation>如果该幂级数在点<equation>x_{1}</equation>收敛，则对满足<equation>|x-x_{0}|<</equation><equation>|x_{1}-x_{0}|</equation>的一切 x所对应的级数<equation>\sum_{n=0}^{\infty} a_{n}(x-x_{0})^{n}</equation>都绝对收敛.

<equation>\textcircled{2}</equation>如果该幂级数在点<equation>x_{2}</equation>发散，则对满足<equation>|x - x_0| > |x_2 - x_0|</equation>的一切<equation>x</equation>所对应的级数<equation>\sum_{n = 0}^{\infty} a_n (x - x_0)^n</equation>都发散.

---


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


#### （1）傅里叶级数的定义

<equation>\frac {1}{1 - x} = \sum_ {n = 0} ^ {\infty} x ^ {n}, x \in (- 1, 1);</equation>

<equation>\frac {1}{1 + x} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {n}, x \in (- 1, 1).</equation>


设函数<equation>f(x)</equation>是周期为<equation>2\pi</equation>的周期函数，且在区间<equation>[-\pi ,\pi ]</equation>上可积，则称

<equation>a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x \mathrm {d} x \quad (n = 1, 2, \dots)</equation>

为<equation>f(x)</equation>的傅里叶系数，称三角级数

<equation>\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right)</equation>

为<equation>f(x)</equation>以<equation>2\pi</equation>为周期的傅里叶级数，记作

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right).</equation>

(2) 傅里叶级数的收敛定理

（狄利克雷收敛定理）设<equation>f(x)</equation>是周期为<equation>2\pi</equation>的周期函数，在区间<equation>[-\pi ,\pi ]</equation>上满足：

---


#### 2. 周期为 21 的傅里叶级数

<equation>\textcircled{1}</equation>只有有限个第一类间断点；

<equation>\textcircled{2}</equation>只有有限个极值点.

则<equation>f ( x )</equation>的以<equation>2 \pi</equation>为周期的傅里叶级数<equation>\frac{a_{0}}{2}+\sum_{n=1}^{\infty} \left(a_{n}\cos nx+b_{n}\sin nx\right)</equation>，其收敛域为<equation>(-\infty , +\infty)</equation>，和函数<equation>S ( x )</equation>是以<equation>2 \pi</equation>为周期的周期函数，且在其一个周期上的表达式为

<equation>S (x) = \left\{ \begin{array}{l l} \frac {f (x - 0) + f (x + 0)}{2}, & x \in (- \pi , \pi), \\ \frac {f (- \pi + 0) + f (\pi - 0)}{2}, & x = \pm \pi . \end{array} \right.</equation>


设函数<equation>f(x)</equation>是周期为<equation>2l</equation>的周期函数，且在区间<equation>[-l, l]</equation>上可积，则称

<equation>a _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {1}{l} \int_ {- l} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots)</equation>

为<equation>f(x)</equation>的傅里叶系数，称三角级数

<equation>\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{l} + b _ {n} \sin \frac {n \pi x}{l}\right)</equation>

为<equation>f(x)</equation>以2l为周期的傅里叶级数.

---

3. 只在<equation>[0, l]</equation>上有定义的函数的傅里叶级数展开

(1) 对称区间上奇、偶函数的傅里叶级数

<equation>\textcircled{1}</equation>若<equation>f(x)</equation>是以<equation>2l</equation>为周期的可积偶函数，则其以<equation>2l</equation>为周期的傅里叶级数为

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l},</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots).</equation>

<equation>\textcircled{2}</equation>若<equation>f(x)</equation>为以<equation>2l</equation>为周期的可积奇函数，则其以<equation>2l</equation>为周期的傅里叶级数为

<equation>f (x) \sim \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l},</equation>

其中

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {1} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

(2) 在<equation>[0, l]</equation>上有定义的函数的傅里叶级数展开

定义在[0，l]上的函数可以有多种方式展开成三角级数，但常用的方式只有三种，即周期奇延拓、周期偶延拓、周期延拓，三种延拓得到的三角级数展开式分别为：

<equation>\textcircled{1}</equation>正弦级数展开：

<equation>f (x) \sim \sum_ {n = 1} ^ {\infty} b _ {n} \sin \frac {n \pi x}{l},</equation>

---

其中

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

<equation>\textcircled{2}</equation>余弦级数展开：

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos \frac {n \pi x}{l},</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots).</equation>

<equation>\textcircled{3}</equation>三角级数展开：

<equation>f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {2 n \pi x}{l} + b _ {n} \sin \frac {2 n \pi x}{l}\right),</equation>

其中

<equation>a _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \cos \frac {2 n \pi x}{l} \mathrm {d} x \quad (n = 0, 1, 2, \dots),</equation>

<equation>b _ {n} = \frac {2}{l} \int_ {0} ^ {l} f (x) \sin \frac {2 n \pi x}{l} \mathrm {d} x \quad (n = 1, 2, \dots).</equation>

---


### 第八章 常微分方程及差分方程
#### 2. 一阶齐次微分方程

形如

<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f (x) g (y)</equation>

或

<equation>M _ {1} (x) N _ {1} (y) \mathrm {d} x + M _ {2} (x) N _ {2} (y) \mathrm {d} y = 0</equation>

的一阶微分方程，称为变量可分离的一阶微分方程.

求通解方法：当<equation>g ( y ) \neq 0</equation>时，

<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f (x) g (y) \Leftrightarrow \frac {\mathrm {d} y}{g (y)} = f (x) \mathrm {d} x,</equation>

<equation>\int \frac {\mathrm {d} y}{g (y)} = \int f (x) \mathrm {d} x,</equation>

则有

将左、右两边的不定积分求出，整理可得方程通解.


形如

<equation>y ^ {\prime} = f \left(\frac {y}{x}\right)</equation>

---


#### 4. 伯努利方程

的一阶微分方程，叫一阶齐次微分方程

求通解方法：设<equation>u = \frac{y}{x}</equation>，将此方程化为关于未知函数<equation>u</equation>的可分离变量的一阶微分方程，求出此一阶微分方程的通解，然后将通解中的<equation>u</equation>用<equation>\frac{y}{x}</equation>替换，即得原微分方程的通解.


形如

<equation>A (x) y ^ {\prime} + B (x) y = C (x)</equation>

的一阶微分方程，叫一阶线性微分方程，其标准形式为

<equation>y ^ {\prime} + p (x) y = q (x).</equation>

当右端的<equation>q(x)</equation>恒为零时，称其为一阶线性齐次微分方程，否则称为一阶线性非齐次微分方程.

求通解方法：通解由公式

<equation>y = \mathrm {e} ^ {- \int p (x) \mathrm {d} x} \left[ \int q (x) \mathrm {e} ^ {\int p (x) \mathrm {d} x} \mathrm {d} x + C \right]</equation>

给出.


形如

<equation>y ^ {\prime} + p (x) y = q (x) y ^ {n} \quad (n \neq 0, 1)</equation>

的方程叫做伯努利方程

求通解方法：令<equation>z = y^{1 - n}</equation>，将此方程化为<equation>z</equation>的一阶

---


#### 二、可降阶的高阶微分方程

线性微分方程，求出此一阶微分方程的通解，然后将通解中的<equation>z</equation>用<equation>y^{1 - n}</equation>替换，即得原微分方程的通解.


如果存在可微函数 u（x，y），使得

<equation>\mathrm {d} u (x, y) = P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y,</equation>

则称一阶微分方程

<equation>P (x, y) \mathrm {d} x + Q (x, y) \mathrm {d} y = 0</equation>

为全微分方程.


1. 形如<equation>y^{(n)}=f(x)</equation>的可降阶方程

这类微分方程只要积分<equation>n</equation>次就得到方程的通解.

2. 不显含函数 y的二阶可降阶的方程<equation>y^{\prime \prime}=f(x,y^{\prime})</equation>这类方程特点是不显含 y，若令<equation>y^{\prime}=p</equation>，则

<equation>y ^ {\prime \prime} = \frac {\mathrm {d} p}{\mathrm {d} x} = p ^ {\prime},</equation>

于是所给方程可降为一阶方程，再按一阶微分方程的方法求解.

3. 不显含自变量 x的二阶可降阶的方程<equation>y^{\prime \prime}=f(y,y^{\prime})</equation>这类方程特点是不显含 x，若令<equation>y^{\prime}=p</equation>，则

<equation>y ^ {\prime \prime} = \frac {\mathrm {d} p}{\mathrm {d} y} \cdot \frac {\mathrm {d} y}{\mathrm {d} x} = p \frac {\mathrm {d} p}{\mathrm {d} y}.</equation>

---


#### 三、线性微分方程解的结构定理

于是所给方程可降为一阶方程，再按一阶微分方程的方法求解.


一手+V：kaoyan33311

<equation>\textcircled{1}</equation>设<equation>y_{1}, y_{2}</equation>是n阶齐次线性微分方程<equation>y^{(n)}+p_{1}(x)y^{(n-1)}+p_{2}(x)y^{(n-2)}+\cdots+p_{n}(x)y=0</equation>的两个解，则

<equation>y = C _ {1} y _ {1} + C _ {2} y _ {2}</equation>

也是该方程的解，其中<equation>C_{1}, C_{2}</equation>是任意常数.

<equation>\textcircled{2}</equation>设<equation>y_{1}, y_{2}, \dots , y_{n}</equation>是n阶齐次线性微分方程<equation>y^{(n)}+p_{1}(x)y^{(n-1)}+p_{2}(x)y^{(n-2)}+\dots +p_{n}(x)y=0</equation>的n个线性无关的解，则

<equation>y = C _ {1} y _ {1} + C _ {2} y _ {2} + \dots + C _ {n} y _ {n}</equation>

是该方程的通解，其中<equation>C_{1}, C_{2}, \dots, C_{n}</equation>是任意常数.

<equation>\textcircled{3}</equation>如果<equation>y_{1}</equation>是方程

<equation>y ^ {(n)} + p _ {1} (x) y ^ {(n - 1)} + p _ {2} (x) y ^ {(n - 2)} + \dots + p _ {n} (x) y = f _ {1} (x)</equation>

的解，<equation>y_{2}</equation>是方程

<equation>y ^ {(n)} + p _ {1} (x) y ^ {(n - 1)} + p _ {2} (x) y ^ {(n - 2)} + \dots + p _ {n} (x) y = f _ {2} (x)</equation>

的解，则<equation>y_{1}+y_{2}</equation>是方程

<equation>y ^ {(n)} + p _ {1} (x) y ^ {(n - 1)} + p _ {2} (x) y ^ {(n - 2)} + \dots + p _ {n} (x) y = f _ {1} (x) + f _ {2} (x)</equation>

的解.

---


#### 1. 二阶常系数齐次线性微分方程

<equation>\textcircled{4}</equation>设<equation>y^{*}</equation>是非齐次线性微分方程

<equation>y^{(n)}+p_{1}(x)y^{(n-1)}+p_{2}(x)y^{(n-2)}+\dots+p_{n}(x)y=f(x)</equation>的一个特解，<equation>C_{1}y_{1}+C_{2}y_{2}+\dots+C_{n}y_{n}</equation>是该非齐次微分方程对应的齐次线性微分方程的通解，则该非齐次线性微分方程的通解为

<equation>y = C _ {1} y _ {1} + C _ {2} y _ {2} + \dots + C _ {n} y _ {n} + y ^ {*}.</equation>


二阶常系数齐次线性微分方程的形式为：

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = 0,</equation>

其中 p，q为常数，其特征方程为

<equation>\lambda^ {2} + p \lambda + q = 0.</equation>

方程的通解为：

<equation>\textcircled{1}</equation>特征方程有两个相异的实根<equation>\lambda_{1},\lambda_{2}</equation>时，通解形式为

<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {1} x}.</equation>

<equation>\textcircled{2}</equation>特征方程有两个相同的实根<equation>\lambda_{1}=\lambda_{2}</equation>时，通解形式为

<equation>y (x) = \left(C _ {1} + C _ {2} x\right) \mathrm {e} ^ {\lambda_ {1} x}.</equation>

<equation>\textcircled{3}</equation>特征方程有一对共轭复根<equation>\alpha \pm \beta \mathrm{i}</equation>时，通解形式为

<equation>y (x) = \mathrm {e} ^ {\alpha x} \left(C _ {1} \cos \beta x + C _ {2} \sin \beta x\right).</equation>

---


#### 五、二阶常系数非齐次线性微分方程

此种方程的一般形式为

<equation>y ^ {(n)} + p _ {1} y ^ {(n - 1)} + p _ {2} y ^ {(n - 2)} + \dots + p _ {n} y = 0,</equation>

其中<equation>p_{i}(i = 1,2,\dots ,n)</equation>为常数，相应的特征方程为

<equation>\lambda^ {n} + p _ {1} \lambda^ {n - 1} + \dots + p _ {n - 1} \lambda + p _ {n} = 0.</equation>

特征方程的根与通解的关系为：

<equation>\textcircled{1}</equation>若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>是<equation>n</equation>个互异实根，则方程的通解为

<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x} + \dots + C _ {n} \mathrm {e} ^ {\lambda_ {n} x}.</equation>

<equation>\textcircled{2}</equation>若<equation>\lambda = \lambda_0</equation>为特征方程的<equation>k(k\leqslant n)</equation>重实根，则方程的通解中含有

<equation>\left(C _ {1} + C _ {2} x + \dots + C _ {k} x ^ {k - 1}\right) \mathrm {e} ^ {\lambda x}.</equation>

<equation>\textcircled{3}</equation>若<equation>\alpha \pm \beta</equation>为特征方程的<equation>k</equation>重共轭复根，则方程的通解中含有

<equation>\begin{array}{l} \mathrm {e} ^ {\alpha x} \left[ \left(C _ {1} + C _ {2} x + \dots + C _ {k} x ^ {k - 1}\right) \cos \beta x + \right. \\ \left(D _ {1} + D _ {2} x + \dots + D _ {k} x ^ {k - 1}\right) \sin \beta x ]. \\ \end{array}</equation>


二阶常系数非齐次线性微分方程的一般形式为

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x),</equation>

其中 p, q是常数.

求特解<equation>y^{*}</equation>的待定系数法：

---

<equation>\textcircled{1}</equation>若

<equation>f (x) = P _ {m} (x) \mathrm {e} ^ {a x},</equation>

其中<equation>P_{m}(x)</equation>为<equation>x</equation>的<equation>m</equation>次多项式，则待定特解<equation>y^{*}</equation>的形式为

<equation>y ^ {*} = x ^ {k} Q _ {m} (x) \mathrm {e} ^ {a x},</equation>

其中<equation>Q_{m}(x)</equation>是与<equation>P_{m}(x)</equation>同次的多项式，调节系数

<equation>k = \left\{ \begin{array}{ll}0, & \alpha \text{不是特征方程的特征根，} \\ 1, & \alpha \text{是特征方程的单特征根，} \\ 2, & \alpha \text{是特征方程的二重特征根。} \end{array} \right.</equation>

将<equation>y^{*} = x^{k}Q_{m}(x)\mathrm{e}^{ax}</equation>代入方程

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x),</equation>

就可以求出<equation>Q_{m}(x).</equation>

<equation>\textcircled{2}</equation>若

<equation>f (x) = \mathrm {e} ^ {\alpha x} \left[ P _ {n} (x) \cos \beta x + Q _ {m} (x) \sin \beta x \right],</equation>

其中<equation>P_{n}(x), Q_{m}(x)</equation>分别为<equation>x</equation>的<equation>n</equation>次，<equation>m</equation>次多项式，则待定特解<equation>y^{*}</equation>的形式为

<equation>y ^ {*} = x ^ {k} \mathrm {e} ^ {\mathrm {a} x} \left[ M _ {i} (x) \cos \beta x + N _ {i} (x) \sin \beta x \right],</equation>

其中<equation>l = \max \{m,n\}</equation>，<equation>M_{l}(x)</equation>，<equation>N_{l}(x)</equation>是两个待定的<equation>l</equation>次多项式，调节系数

<equation>k = \left\{ \begin{array}{l l} 0, & \alpha + \beta \mathrm {i} \text {不 是 特 征 方 程 的 特 征 根}, \\ 1, & \alpha + \beta \mathrm {i} \text {是 特 征 方 程 的 特 征 根}. \end{array} \right.</equation>

---


#### 七、差分方程

形如

<equation>x ^ {n} y ^ {(n)} + p _ {1} x ^ {n - 1} y ^ {(n - 1)} + p _ {2} x ^ {n - 2} y ^ {(n - 2)} + \dots +</equation>

<equation>p _ {n - 1} x y ^ {\prime} + p _ {n} y = f (x)</equation>

的方程称为欧拉方程.

这个方程可以通过变换<equation>x = \mathrm{e}^{t}</equation>化为以<equation>t</equation>为自变量的常系数线性微分方程，求解后代回原来的变量即得欧拉方程的解.


1. 差分的定义

(1) 一阶差分

<equation>\Delta y _ {t} = y _ {t + 1} - y _ {t}.</equation>

(2) 二阶差分

<equation>\Delta^ {2} y _ {t} = y _ {t + 2} - 2 y _ {t + 1} + y _ {t}.</equation>

2. 一阶线性齐次差分方程的解法

(1) 方程形式

<equation>y _ {i + 1} - a y _ {i} = 0.</equation>

(2) 特征方程

<equation>r - a = 0.</equation>

---


#### 3. 一阶线性非齐次差分方程的解法

(3) 通解

<equation>\bar {y} _ {t} = C a ^ {t}.</equation>


(1) 方程形式

<equation>y _ {t + 1} - a y _ {t} = f (t).</equation>

(2) 通解形式

<equation>y _ {t} = \tilde {y} _ {t} + y _ {t} ^ {*}.</equation>

(3) 特解形式

<equation>\textcircled{1}</equation><equation>f(t) = P_{m}(t)</equation>，其中<equation>P_{m}(t)</equation>是 t的 m次多项式<equation>y_{t}^{*} = Q_{m}(t)</equation>，其中<equation>Q_{m}(t)</equation>是特定的 m次多项式.

<equation>\textcircled{2}</equation>若<equation>f(t) = b^{t}P_{m}(t), y_{i}^{*} = t^{k}b^{t}Q_{m}(t).</equation>

当b不是特征方程的根时，取<equation>k = 0</equation>

当b是特征方程的根时，取<equation>k = 1</equation>.

---


## 第二部分线性代数
### 第一章 行列式
#### 2. 行列式的性质

n阶行列式

<equation>\begin{array}{l} D _ {n} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| \\ = \sum_ {\left(j _ {1} j _ {2} \dots j _ {n}\right)} (- 1) ^ {r \left(j _ {1} j _ {2} \dots j _ {n}\right)} a _ {1 j _ {1}} a _ {2 j _ {2}} \dots a _ {m _ {j}}, \\ \end{array}</equation>

式中<equation>\sum_{(j_1,j_2,\dots j_n)}</equation>表示对所有<equation>n</equation>级排列<equation>(j_{1}j_{2}\dots j_{n})</equation>求和.


<equation>\textcircled{1}</equation>行列互换，行列式的值不变，也即<equation>D = D^{\mathrm{T}}</equation>

<equation>\textcircled{2}</equation>任意两行(列)互换位置后，行列式改变符号.

推论1 如果行列式中有两行（列）的对应元素相同，则行列式的值为0.

<equation>\textcircled{3}</equation>将行列式的某一行(列)乘以一个常数<equation>k</equation>后，行列式的值变为原来的<equation>k</equation>倍.

---

推论2 如果行列式的某一行（列）全为0，则行列式的值等于0.

推论3 行列式的某两行（列）元素对应成比例，则行列式的值等于0.

<equation>\textcircled{4}</equation>如果行列式某一行（列）的所有元素都可以写成两个元素的和，则该行列式可以写成两个行列式的和，这两个行列式的这一行（列）分别为对应两个加数，其余行（列）与原行列式相等，即

<equation>\begin{array}{l} \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {i 1} + b _ {i 1} & a _ {i 2} + b _ {i 2} & \dots & a _ {i n} + b _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {i 1} & a _ {i 2} & \dots & a _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| + \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ b _ {i 1} & b _ {i 2} & \dots & b _ {i n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right|. \\ \end{array}</equation>

<equation>\textcircled{5}</equation>将行列式的某行（列）的 k倍加到另一行（列）上，行列式的值不变.

---


#### 2. 行列式按一行（列）展开

在<equation>n</equation>阶行列式<equation>D = |a_{ij}|</equation>中，划掉元素<equation>a_{ij}</equation>所在第<equation>i</equation>行和第<equation>j</equation>列的所有元素后，余下<equation>(n - 1)^{2}</equation>个元素按照原有次序构成一个<equation>(n - 1)</equation>阶行列式，称之为元素<equation>a_{ij}</equation>在<equation>D</equation>中的余子式，记作<equation>M_{ij}</equation>，即

<equation>M _ {j} = \left| \begin{array}{c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 (j - 1)} & a _ {1 (j + 1)} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 (j - 1)} & a _ {2 (j + 1)} & \dots & a _ {2 n} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {(i - 1) 1} & a _ {(i - 1) 2} & \dots & a _ {(i - 1) (j - 1)} & a _ {(i - 1) (j + 1)} & \dots & a _ {(i - 1) n} \\ a _ {(i + 1) 1} & a _ {(i + 1) 2} & \dots & a _ {(i + 1) (j - 1)} & a _ {(i + 1) (j + 1)} & \dots & a _ {(i + 1) n} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n (j - 1)} & a _ {n (j + 1)} & \dots & a _ {m} \end{array} \right|</equation>

记<equation>A_{ij} = (-1)^{i+j}M_{ij}</equation>，称作元素<equation>a_{ij}</equation>的代数余子式.


n阶行列式<equation>D</equation>等于其任一行(列)各元素与其代数余子式乘积之和，即

<equation>\begin{array}{l} D = a _ {i 1} A _ {i 1} + a _ {i 2} A _ {i 2} + \dots + a _ {i n} A _ {i n} \\ = \sum_ {j = 1} ^ {n} a _ {i j} A _ {i j} \quad (i = 1, 2, \dots , n) \quad (\text {按 第} i \text {行 展 开}) \\ = a _ {1 j} A _ {1 j} + a _ {2 j} A _ {2 j} + \dots + a _ {n j} A _ {n j} \\ \end{array}</equation>

---


#### 三、几种特殊的行列式

<equation>= \sum_ {i = 1} ^ {n} a _ {i j} A _ {i j} \quad (j = 1, 2, \dots , n) (\mathrm {按 第} j \mathrm {列 展 开}).</equation>

推论：行列式<equation>D</equation>的某一行（列）各元素与另一行（列）对应元素的代数余子式的乘积之和为零，即

<equation>\begin{array}{l} \sum_ {j = 1} ^ {n} a _ {i j} A _ {k j} = a _ {i 1} A _ {k 1} + a _ {i 2} A _ {k 2} + \dots + a _ {i n} A _ {k n} = 0, \quad (i \neq k) \\ \sum_ {j = 1} ^ {n} a _ {i j} A _ {j k} = a _ {1 i} A _ {1 k} + a _ {2 i} A _ {2 k} + \dots + a _ {n i} A _ {n k} = 0. \quad (i \neq k) \\ \end{array}</equation>


1. 上三角形、下三角形、对角形行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c} a _ {1 1} & 0 & \dots & 0 \\ 0 & a _ {2 2} & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & a _ {m} \end{array} \right| = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ 0 & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & a _ {m} \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & 0 & \dots & 0 \\ a _ {2 1} & a _ {2 2} & \dots & 0 \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {m} \end{array} \right| \\ = a _ {1 1} a _ {2 2} \dots a _ {m}. \\ \end{array}</equation>

---

2. 次对角线行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c} 0 & \dots & 0 & a _ {1 n} \\ 0 & \dots & a _ {2 (n - 1)} & 0 \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & 0 & 0 \end{array} \right| \\ = \left| \begin{array}{c c c c} a _ {1 1} & \dots & a _ {1 (n - 1)} & a _ {1 n} \\ a _ {2 1} & \dots & a _ {2 (n - 1)} & 0 \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & 0 & 0 \end{array} \right| \\ = \left| \begin{array}{c c c c} 0 & \dots & 0 & a _ {1 n} \\ 0 & \dots & a _ {2 (n - 1)} & a _ {2 n} \\ \vdots & & \vdots & \vdots \\ a _ {n 1} & \dots & a _ {n (n - 1)} & a _ {n n} \end{array} \right| \\ = (- 1) ^ {\frac {n (n - 1)}{2}} a _ {1 n} \dots a _ {n 1}. \\ \end{array}</equation>

3. 范德蒙德行列式

<equation>\begin{array}{l} \left| \begin{array}{c c c c c} 1 & 1 & 1 & \dots & 1 \\ a _ {1} & a _ {2} & a _ {3} & \dots & a _ {n} \\ a _ {1} ^ {2} & a _ {2} ^ {2} & a _ {3} ^ {2} & \dots & a _ {n} ^ {2} \\ \vdots & \vdots & \vdots & & \vdots \\ a _ {1} ^ {n - 1} & a _ {2} ^ {n - 1} & a _ {3} ^ {n - 1} & \dots & a _ {n} ^ {n - 1} \end{array} \right| \\ = \prod_ {1 \leq i < j \leq n} \left(a _ {j} - a _ {i}\right). \\ \end{array}</equation>

---


#### 4. 拉普拉斯展开式

<equation>\begin{array}{l} \left| \begin{array}{c c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 k} & & & & \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 k} & \boldsymbol {O} _ {k \times l} & & \\ \vdots & \vdots & & \vdots & & & & \\ a _ {k 1} & a _ {k 2} & \dots & a _ {b k} & & & & \\ c _ {1 1} & c _ {1 2} & \dots & c _ {1 k} & b _ {1 1} & b _ {1 2} & \dots & b _ {1 l} \\ c _ {2 1} & c _ {2 2} & \dots & c _ {2 k} & b _ {2 1} & b _ {2 2} & \dots & b _ {2 l} \\ \vdots & \vdots & & \vdots & \vdots & \vdots & & \vdots \\ c _ {i 1} & c _ {i 2} & \dots & c _ {i k} & b _ {i 1} & b _ {i 2} & \dots & b _ {i l} \end{array} \right| \\ = \left| \begin{array}{c c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 k} & \left| \begin{array}{c c c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 l} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 l} \\ \vdots & \vdots & & \vdots \\ b _ {i 1} & b _ {i 2} & \dots & b _ {i l} \end{array} \right| \\ c _ {1 1} c _ {1 2} \dots c _ {1 k} b _ {1 1} b _ {1 2} \dots b _ {1 l} \\ c _ {2 1} c _ {2 2} \dots c _ {2 k} b _ {2 1} b _ {2 2} \dots b _ {2 l} \\ \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \vdots \\ c _ {i 1} c _ {i 2} \dots c _ {i k} b _ {i 1} b _ {i 2} \dots b _ {i l} \\ a _ {1 1} a _ {1 2} \dots a _ {1 k} \\ a _ {2 1} a _ {2 2} \dots a _ {2 k} \\ \vdots \vdots \vdots \vdots \\ a _ {k 1} a _ {k 2} \dots a _ {b k} \end{array} \right| \\ \end{array}</equation>

---


#### 四、有关行列式的若干个重要公式

<equation>= (- 1) ^ {k} \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 k} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 k} \\ \vdots & \vdots & & \vdots \\ a _ {k 1} & a _ {k 2} & \dots & a _ {k k} \end{array} \right| \left| \begin{array}{c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 l} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 l} \\ \vdots & \vdots & & \vdots \\ b _ {l 1} & b _ {l 2} & \dots & b _ {l l} \end{array} \right|.</equation>


为便于考生综合复习及掌握概念间的联系，现将以后各章所涉及的有关行列式的几个重要公式罗列于下.

设<equation>A, B</equation>均为<equation>n</equation>阶方阵，<equation>k</equation>为常数，<equation>E</equation>为<equation>n</equation>阶单位矩阵，<equation>A^{*}</equation>为<equation>A</equation>的伴随矩阵：

<equation>\textcircled{1}</equation><equation>|k\mathbf{A}| = k^{n} \cdot |\mathbf{A}|</equation>.

<equation>\textcircled{2}</equation>若<equation>A</equation>是可逆矩阵，则有<equation>|A^{-1}| = \frac{1}{|A|}</equation>.

<equation>\textcircled{3}</equation><equation>|\mathbf{A} \cdot \mathbf{B}| = |\mathbf{A}| \cdot |\mathbf{B}|.</equation>

<equation>\textcircled{4}</equation><equation>|\mathbf{A}^{*}|=|\mathbf{A}|^{n-1}.</equation>

<equation>\textcircled{5}</equation><equation>A \cdot A^{*} = A^{*} \cdot A = |A| \cdot E.</equation>

<equation>\textcircled{6} |\mathbf{A}| = \prod_{i=1}^{n} \lambda_{i}</equation>（<equation>\lambda_{1}, \lambda_{2}, \dots, \lambda_{n}</equation>是<equation>\mathbf{A}</equation>的全部特征值).

<equation>\textcircled{7}</equation><equation>|A| \neq 0 \Leftrightarrow A</equation>为可逆矩阵<equation>\Leftrightarrow A</equation>为满秩矩阵，即<equation>r(A)=n.</equation>

---


### 第二章 矩阵
#### 1. 矩阵的定义

由<equation>m \times n</equation>个数<equation>a_{ij}(i = 1,2,\dots,m;j = 1,2,\dots,n)</equation>排列成的<equation>m</equation>行<equation>n</equation>列的数表

<equation>\left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {m 1} & a _ {m 2} & \dots & a _ {m n} \end{array} \right]</equation>

称为<equation>m \times n</equation>矩阵，记为<equation>A = (a_{ij})_{m \times n}</equation>，其中<equation>a_{ij}</equation>称为矩阵<equation>A</equation>的第<equation>i</equation>行第<equation>j</equation>列的元素.

<equation>\textcircled{1}</equation>当<equation>n = m</equation>时，<equation>A</equation>也称为<equation>n</equation>阶方阵，<equation>|A|</equation>称为<equation>A</equation>的行列式.

<equation>\textcircled{2}</equation>两个矩阵<equation>A = (a_{ij})_{m\times n},B = (b_{ij})_{s\times k}</equation>，如果<equation>m = s,n = k</equation>，则称它们为同型矩阵.

<equation>\textcircled{3}</equation>如果两个同型矩阵<equation>A = (a_{ij})_{m\times n},B = (b_{ij})_{m\times n}</equation>对应的元素相等，也即

<equation>a _ {i j} = b _ {i j} (i = 1, \dots , m; j = 1, \dots , n),</equation>

---

则称矩阵 A与矩阵 B相等，记作<equation>A=B.</equation>

常见的特殊矩阵有：

<equation>\textcircled{1}</equation>零矩阵：所有元素均为0的矩阵称之为零矩阵，记为0.

<equation>\textcircled{2}</equation>对角矩阵：主对角线以外的元素均为0的矩阵称之为对角矩阵，记作<equation>\operatorname{diag}\left(a_{1}, a_{2}, \dots, a_{n}\right)</equation>，即

<equation>\mathbf {d i a g} \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) = \left[ \begin{array}{c c c c} a _ {1} & & & \\ & a _ {2} & & \\ & & \ddots & \\ & & & a _ {n} \end{array} \right].</equation>

两个对角矩阵的乘积仍为对角矩阵.

<equation>\textcircled{3}</equation>单位矩阵：主对角线上的元素均为1，其余元素均为0的矩阵称之为单位矩阵，记作E.单位矩阵与任何矩阵相乘都可交换，即

<equation>E A = A E = A.</equation>

<equation>\textcircled{4}</equation>上（下）三角矩阵：主对角线以下的元素全为0的矩阵称之为上三角矩阵；主对角线以上的元素全为0的矩阵称之为下三角矩阵.

<equation>\textcircled{5}</equation>对称矩阵：满足条件<equation>A^{\mathrm{T}}=A</equation>的 n阶矩阵 A称为对称矩阵.即

A为对称矩阵<equation>\Leftrightarrow a_{ij} = a_{ji}</equation>（<equation>i,j=1,2,\dots,n)</equation>

<equation>\textcircled{6}</equation>反对称矩阵：满足条件<equation>A^{\mathrm{T}} = -A</equation>的<equation>n</equation>阶矩阵<equation>A</equation>

---


#### 注 两个相加的矩阵必须是同型的.

称为反对称矩阵。即

<equation>\mathbf{A} = ( a_{ij} )_{n\times n}</equation>为反对称矩阵<equation>\Leftrightarrow a_{ij} = -a_{ji}</equation>（i,j=1,2，…,n)

<equation>\textcircled{7}</equation>正交矩阵：设<equation>A</equation>是<equation>n</equation>阶矩阵，如果<equation>A A^{\mathrm{T}} = A^{\mathrm{T}} A = E</equation>，则称<equation>A</equation>是正交矩阵.


设<equation>A=(a_{ij})</equation><equation>B=(b_{ij})</equation>是两个 m×n矩阵，定义矩阵<equation>C=(c_{ij})=(a_{ij}+b_{ij})</equation>为矩阵 A与矩阵 B的和，记作 C=A +B.


加法的运算性质：

<equation>\textcircled{1}</equation><equation>\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}</equation>（交换律）；

<equation>\textcircled{2}</equation><equation>(\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})</equation>（结合律）；

<equation>\textcircled{3}</equation><equation>\mathbf{A}+\mathbf{O}=\mathbf{A}</equation>（其中<equation>\mathbf{O}=(0)_{m\times n}</equation>）；

<equation>\textcircled{4}</equation><equation>A + (-A) = O</equation>（其中<equation>-A = (-a_{ij})_{m \times n}</equation>）。

(2) 矩阵的数乘

设<equation>A = (a_{ij})</equation>是一个<equation>m\times n</equation>矩阵，<equation>k</equation>为任意实数，则定义

<equation>k\mathbf{A} = (k a_{ij}) \quad (i = 1,2,\dots,m; j = 1,2,\dots,n)</equation>为矩阵的数乘.

数乘的运算性质：

<equation>\textcircled{1} k(l\mathbf{A}) = (kl)\mathbf{A} = l(k\mathbf{A})</equation>（k，l为数）；

---


#### (3)矩阵的乘法

<equation>\textcircled{2} (\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})</equation>;

<equation>\textcircled{3} k(\mathbf{A} + \mathbf{B}) = k\mathbf{A} + k\mathbf{B}</equation>;

<equation>\textcircled{4} ( k+l ) \mathbf{A}=k \mathbf{A}+l \mathbf{A}.</equation>


设<equation>\mathbf{A} = (a_{ij})_{m\times n},\mathbf{B} = (b_{ij})_{n\times k}</equation>（注意<equation>\mathbf{A}</equation>的列数和<equation>\mathbf{B}</equation>的行数相等），定义矩阵

<equation>\mathbf {C} = \left(c _ {i j}\right) _ {m \times k},</equation>

其中

<equation>c _ {i j} = a _ {i 1} b _ {1 j} + a _ {i 2} b _ {2 j} + \dots + a _ {i n} b _ {n j} = \sum_ {k = 1} ^ {n} a _ {i k} b _ {k j},</equation>

称为矩阵<equation>A</equation>与矩阵<equation>B</equation>的乘积，记作<equation>C = AB</equation>

数乘的运算性质：

<equation>\textcircled{1}</equation><equation>\mathbf{(A B) C}=\mathbf{A( B C)}</equation>（结合律）；

<equation>\textcircled{2}</equation><equation>\mathbf{A} (\mathbf{B}+\mathbf{C})=\mathbf{A B}+\mathbf{A C},</equation>

（<equation>\mathbf{B}+\mathbf{C} )\mathbf{A}=\mathbf{B}\mathbf{A}+\mathbf{C}\mathbf{A}</equation>（分配律）；

<equation>\textcircled{3}</equation><equation>( k A ) B=A ( k B )=k ( A B )</equation>（数与乘积的结合律).

注<equation>\textcircled{1}</equation>不是任意两个矩阵<equation>A</equation>与<equation>B</equation>都能相乘的，必须有<equation>A</equation>的列数和<equation>B</equation>的行数相等.

<equation>\textcircled{2}</equation>矩阵乘法一般来说不满足交换律，即一般情况下，<equation>\mathbf{A B}\neq \mathbf{B A}.</equation>

<equation>\textcircled{3}</equation>矩阵的运算也不满足消去律. 即由<equation>AB = AC</equation>且<equation>A \neq O</equation>, 得不出<equation>B = C</equation>.

---


#### （4）方阵的乘幂运算

<equation>\textcircled{4}</equation>零因子定律不成立，即由<equation>AB = O</equation>并不能得到<equation>A = O</equation>或<equation>B = O.</equation>


如果矩阵<equation>A</equation>为方阵，则定义<equation>A^{n} = \underbrace{A \cdot A \cdots A}_{n \text{个} A}</equation>为矩阵<equation>A</equation>的<equation>n</equation>次幂.规定<equation>A^{0} = E</equation>（单位矩阵）.

乘幂的运算性质：

<equation>\textcircled{1}</equation><equation>A^{k} \cdot A^{l} = A^{k+l}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}^{k}\right)^{l}=\mathbf{A}^{k l}.</equation>

注 一般情况下，<equation>(\mathbf{A}\cdot \mathbf{B})^{k}\neq A^{k}\cdot B^{k}.</equation>

(5) 矩阵的转置

设<equation>A_{m\times n} = \left[ \begin{array}{cccc} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{array} \right]_{m\times n}</equation>，定义A的转置

矩阵为

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {2 1} & \dots & a _ {m 1} \\ a _ {1 2} & a _ {2 2} & \dots & a _ {m 2} \\ \vdots & \vdots & & \vdots \\ a _ {1 n} & a _ {2 n} & \dots & a _ {m n} \end{array} \right] _ {n \times m},</equation>

即转置矩阵<equation>A^{\mathrm{T}}</equation>的第<equation>i</equation>行第<equation>j</equation>列元素等于原矩阵<equation>A</equation>的第<equation>j</equation>行第<equation>i</equation>列元素.

转置的运算规则：

---

<equation>\textcircled{1} (\mathbf{A}^{\mathrm{T}})^{\mathrm{T}} = \mathbf{A}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}+\mathbf{B}\right)^{\mathrm{T}}=\mathbf{A}^{\mathrm{T}}+\mathbf{B}^{\mathrm{T}};</equation>

<equation>\textcircled{3}</equation><equation>\mathbf{A B} )^{\mathrm{T}}=\mathbf{B}^{\mathrm{T}} \mathbf{A}^{\mathrm{T}};</equation>

<equation>\textcircled{4} ( k \mathbf{A} )^{\mathrm{T}}=k \cdot \mathbf{A}^{\mathrm{T}}.</equation>

(6) 方阵的行列式

若<equation>\mathbf{A} = (a_{i j})_{n\times n},\mathbf{B} = (b_{i j})_{n\times n}</equation>，则

<equation>| \mathbf {A} | = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right|,</equation>

且<equation>|kA| = k^{n}|A|, |AB| = |A||B|.</equation>

(7) 矩阵的求逆运算

<equation>\textcircled{1}</equation>逆矩阵的定义及定理

若<equation>A, B</equation>均为<equation>n</equation>阶方阵，且满足<equation>AB = BA = E</equation>，则称<equation>A</equation>是可逆矩阵，又称<equation>B</equation>是<equation>A</equation>的逆矩阵，记作<equation>B = A^{-1}</equation>.

(a)若矩阵<equation>A</equation>可逆，则<equation>A</equation>的逆矩阵<equation>A^{-1}</equation>是唯一的.

(b) 矩阵<equation>A</equation>可逆的充分必要条件是<equation>|A| \neq 0</equation>.

(c) 若<equation>|A| \neq 0</equation>，则<equation>A^{-1} = \frac{1}{|A|} A^{*}</equation>，其中

<equation>\boldsymbol {A} ^ {*} = \left[ \begin{array}{c c c c} A _ {1 1} & A _ {2 1} & \dots & A _ {n 1} \\ A _ {1 2} & A _ {2 2} & \dots & A _ {n 2} \\ \vdots & \vdots & & \vdots \\ A _ {1 n} & A _ {2 n} & \dots & A _ {m} \end{array} \right],</equation>

---


#### 3. 矩阵经过运算后秩的变化规律

称为<equation>\mathbf{A}</equation>的伴随矩阵（其中<equation>A_{y}</equation>是元素<equation>a_{y}</equation>的代数余子式）.

由<equation>A^{+}</equation>的构成，可得到以下重要的公式：

<equation>A A ^ {*} = A ^ {*} A = | A | E.</equation>

<equation>\textcircled{2}</equation>求逆运算的运算规则

若<equation>\mathbf{A},\mathbf{B}</equation>均为 n阶可逆矩阵，则

(a)<equation>(\mathbf{A}^{-1})^{-1} = \mathbf{A}</equation>;

(b) 若<equation>k\neq 0</equation>为常数，则<equation>(kA)^{-1} = \frac{1}{k} A^{-1}</equation>；

(c)<equation>(\mathbf{A B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1};</equation>

(d)<equation>A^{\mathrm{T}}</equation>也可逆，且<equation>(A^{\mathrm{T}})^{-1} = (A^{-1})^{\mathrm{T}};</equation>

(e)<equation>|\mathbf{A}^{-1}| = |\mathbf{A}|^{-1}.</equation>


在<equation>A_{m \times n}</equation>中，任取<equation>k</equation>行、<equation>k</equation>列，在这<equation>k</equation>行<equation>k</equation>列的交错处有<equation>k^2</equation>个元素，这<equation>k^2</equation>个元素按原有的次序构成一个<equation>k</equation>阶行列式，称为<equation>A</equation>的一个<equation>k</equation>阶子式。


在<equation>A_{m \times n}</equation>中，至少有一个<equation>r</equation>阶子式不为零，而所有<equation>r + 1</equation>阶子式全为零，则称<equation>A</equation>的秩为<equation>r</equation>，记作<equation>\operatorname{rank}(A) = r</equation>，简记为<equation>r(A) = r</equation>或<equation>R(A) = r</equation>。


<equation>\textcircled{1}</equation><equation>r(\mathbf{A}^{\mathrm{T}}) = r(\mathbf{A})</equation>;

---


#### 1. 分块矩阵的定义

<equation>\textcircled{2} r ( A_{m \times n} ) \leqslant\min \{ m,n \} ;</equation>

<equation>\textcircled{3}</equation><equation>r(\mathbf{A}) = 0 \Leftrightarrow \mathbf{A} = \mathbf{O}</equation>;

<equation>\textcircled{4}</equation><equation>r(k\mathbf{A}) = \left\{ \begin{array}{ll} r(\mathbf{A}), & k \neq 0, \\ 0, & k = 0; \end{array} \right.</equation>

<equation>\textcircled{5} r(\mathbf{A} + \mathbf{B}) \leqslant r(\mathbf{A}) + r(\mathbf{B})</equation>;

<equation>\textcircled{6} r ( \mathbf{A B} ) \leqslant\min \{ r ( \mathbf{A} ) , r ( \mathbf{B} ) \} ;</equation>

<equation>\textcircled{7}</equation>若有矩阵<equation>A_{m\times n}, B_{n\times s}</equation>，且<equation>AB = O</equation>，且<equation>r(A) + r(B) \leqslant n</equation>；

<equation>\textcircled{8}</equation>若<equation>P, Q</equation>为满秩方阵，则

<equation>r (P A) = r (A) = r (A Q) = r (P A Q);</equation>

<equation>\textcircled{9}</equation>初等变换不改变矩阵的秩. 若<equation>B</equation>是阶梯形矩阵，则<equation>r(B)</equation>等于<equation>B</equation>中非零行的个数；

<equation>\textcircled{10}</equation>关于伴随矩阵<equation>A^{*}</equation>的秩：

<equation>r \left(\boldsymbol {A} ^ {*}\right) = \left\{ \begin{array}{l l} n, r (\boldsymbol {A}) = n, \\ 1, r (\boldsymbol {A}) = n - 1, \\ 0, r (\boldsymbol {A}) \leqslant n - 2. \end{array} \right.</equation>


用贯穿矩阵的横线和纵线（称为分划线）把一个矩阵分成若干小块，每一小块称为原矩阵的子块，一般记作<equation>A_{ij}</equation>，分为子块的矩阵叫做分块矩阵。由于不同的需要，同一矩阵可以有不同的分块方法。例如：

---


#### (2) 数乘

$$

\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ \dots \dots

<equation>\boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} & a _ {3 4} \\ a _ {4 1} & a _ {4 2} & a _ {4 3} & a _ {4 4} \end{array} \right] = \left(\boldsymbol {p} _ {1}, \boldsymbol {p} _ {2}, \boldsymbol {p} _ {3}, \boldsymbol {p} _ {4}\right) _ {1 \times 4}.</equation>


<equation>A, B \in M_{m,n}</equation>，且有相同的分块划分方法：<equation>A = \left(A_{ij}\right)_{s \times t}, B = \left(B_{ij}\right)_{s \times t}</equation>，则

<equation>A + B = \left(A_{ij} + B_{ij}\right)_{s\times l}</equation>（每个对应子块可加）.


设<equation>A = \left(A_{ij}\right)_{s\times t}\in M_{m,n}</equation>，则

<equation>k \boldsymbol {A} = \left(k \boldsymbol {A} _ {i j}\right) _ {s \times t}.</equation>

(3) 转置

若

<equation>\boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 t} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \dots & \boldsymbol {A} _ {2 t} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {s 1} & \boldsymbol {A} _ {s 2} & \dots & \boldsymbol {A} _ {x} \end{array} \right] = \left(\boldsymbol {A} _ {i j}\right) _ {s \times t} \in M _ {m, n},</equation>

---


#### (4)乘法

则

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 1} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s 1} ^ {\mathrm {T}} \\ \boldsymbol {A} _ {1 2} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 2} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s 2} ^ {\mathrm {T}} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {1 t} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 t} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s t} ^ {\mathrm {T}} \end{array} \right],</equation>

即分块矩阵先转置后，再将每个子矩阵分别单独转置即为原矩阵的转置矩阵.


设

<equation>\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 t} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \dots & \boldsymbol {A} _ {2 t} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {s 1} & \boldsymbol {A} _ {s 2} & \dots & \boldsymbol {A} _ {s t} \end{array} \right] = \left(\boldsymbol {A} _ {i j}\right) _ {s \times t} \in M _ {m, n}, \\ \boldsymbol {B} = \left[ \begin{array}{c c c c} \boldsymbol {B} _ {1 1} & \boldsymbol {B} _ {1 2} & \dots & \boldsymbol {B} _ {1 r} \\ \boldsymbol {B} _ {2 1} & \boldsymbol {B} _ {2 2} & \dots & \boldsymbol {B} _ {2 r} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {B} _ {t 1} & \boldsymbol {B} _ {t 2} & \dots & \boldsymbol {B} _ {t r} \end{array} \right] = \left(\boldsymbol {B} _ {j k}\right) _ {t \times r} \in M _ {m, n}, \\ \boldsymbol {C} = \boldsymbol {A} \boldsymbol {B} = \left[ \begin{array}{c c c c} \boldsymbol {C} _ {1 1} & \boldsymbol {C} _ {1 2} & \dots & \boldsymbol {C} _ {1 r} \\ \boldsymbol {C} _ {2 1} & \boldsymbol {C} _ {2 2} & \dots & \boldsymbol {C} _ {2 r} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {C} _ {s 1} & \boldsymbol {C} _ {s 2} & \dots & \boldsymbol {C} _ {s r} \end{array} \right], \\ \end{array}</equation>

---


#### 3. 分块对角形（对角块）矩阵

其中<equation>C_{ik} = A_{i1}B_{1k} + A_{i2}B_{2k} + \dots + A_{it}B_{tk} = \sum_{j=1}^{i}A_{ij}B_{jk}</equation><equation>(i = 1,\dots,s;k = 1,\dots,r).</equation>


一般地，分块矩阵<equation>A = \left[ \begin{array}{cccc}A_{11} & O & \dots & O\\ O & A_{22} & \dots & O\\ \vdots & \vdots & & \vdots \\ O & O & \dots & A_{s} \end{array} \right],</equation>

简记为<equation>A = \left[ \begin{array}{c c c c} A_{11} & & & \\ & A_{22} & & \\ & & \ddots & \\ & & & A_{ss} \end{array} \right],</equation>其中<equation>A_{ii}</equation>均为小方

阵，则称<equation>A</equation>为对角块矩阵或分块对角形矩阵。若<equation>A, B</equation>均为对角块矩阵，则<equation>A + B, AB</equation>也为对角块矩阵，如：

<equation>\begin{array}{l} \boldsymbol {A} + \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] + \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1} + \boldsymbol {B} _ {1} & & & \\ & \boldsymbol {A} _ {2} + \boldsymbol {B} _ {2} & & \\ & & \ddots & \\ & & & \boldsymbol {A} _ {s} + \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

---


#### 1. 矩阵的初等行（列）变换

其中，<equation>A_{i}, B_{i}</equation>为同阶子矩阵

<equation>\begin{array}{l} \boldsymbol {A} \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {A} _ {2} \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

其中，<equation>A_{i}, B_{i}</equation>为同阶子矩阵

对角块矩阵的逆矩阵公式（设<equation>A_{1}, A_{2}, A_{3}</equation>均可逆）：

<equation>\begin{array}{l} \left[ \begin{array}{c c c} A _ {1} & & \\ & A _ {2} & \\ & & A _ {3} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c c} A _ {1} ^ {- 1} & & \\ & A _ {2} ^ {- 1} & \\ & & A _ {3} ^ {- 1} \end{array} \right], \\ \left[ \begin{array}{c c c} & & A _ {1} \\ & A _ {2} & \\ A _ {3} & & \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c c} & & A _ {3} ^ {- 1} \\ & A _ {2} ^ {- 1} & \\ A _ {1} ^ {- 1} & & \end{array} \right]. \\ \end{array}</equation>


矩阵的初等变换指的是对矩阵施行以下三种行（列）变换：

---


#### (1) 初等行交换矩阵

<equation>\textcircled{1}</equation>交换变换：互换矩阵中的某两行（列）；

<equation>\textcircled{2}</equation>倍乘变换：用一个非零常数<equation>k</equation>乘矩阵的某行(列)；

<equation>\textcircled{3}</equation>倍加变换：将矩阵的某行（列）的 k 倍加到另一行（列）上.


形如

<equation>\left[ \begin{array}{l l l} 0 & 1 & 3 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array} \right], \left[ \begin{array}{c c c c c} 1 & 2 & - 1 & 2 & 5 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 4 & 1 \end{array} \right], \left[ \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 2 & 3 \\ 0 & 0 & 3 \end{array} \right]</equation>

的矩阵称为阶梯形矩阵.

阶梯形矩阵有以下特征：

<equation>\textcircled{1}</equation>全零行位于矩阵的最下方.

<equation>\textcircled{2}</equation>每个非零行的第一个非零元素<equation>c_{ij}</equation>（亦称主元）的列标<equation>j</equation>随着行标<equation>i</equation>的递增而严格增大.

<equation>\textcircled{3}</equation>任一个矩阵经过若干次初等行（列）变换都可以化成阶梯形矩阵.


将单位矩阵作了一次初等行（列）变换的矩阵称作初等矩阵.

三种初等行（列）变换矩阵：


将单位矩阵的第<equation>i</equation>行、第<equation>j</equation>行交换后所得到的矩阵，记作

---


#### （3）初等行倍加矩阵

<equation>\boldsymbol {P} ((i) \leftrightarrow (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ \ddots & & & & \\ & 0 & \dots & 1 & \\ & \vdots & & \vdots & \\ & 1 & \dots & 0 & \\ & & & \ddots & \\ & & & & 1 \end{array} \right] \leftarrow i \text {行} \quad \leftarrow j \text {行}</equation>

作用：将初等行交换矩阵左乘 A，即若

<equation>P ((i) \leftrightarrow (j)) A = A _ {1},</equation>

则<equation>A_{1}</equation>就是将<equation>A</equation>的第<equation>i</equation>行、第<equation>j</equation>行交换后的结果.


将单位矩阵的第 i 行乘以不为零的常数 k后所得到的矩阵，记作

<equation>\boldsymbol {P} ((k (i)) = \left[ \begin{array}{c c c c} 1 & & & \\ & \ddots & & \\ & & k & \\ & & & \ddots \\ & & & 1 \end{array} \right] \leftarrow i \text {行}.</equation>

作用：若<equation>P(k(i))A = A_{2}</equation>，则<equation>A_{2}</equation>就是将<equation>A</equation>的第<equation>i</equation>行乘上<equation>k</equation>倍后的结果.


将单位矩阵第<equation>i</equation>行的<equation>k</equation>倍加到第<equation>j</equation>行后所得到的矩阵，记作

---


#### （4）初等列交换矩阵

<equation>\boldsymbol {P} (k (i) + (j)) = \left[ \begin{array}{c c c c c c} 1 & & & & & \\ & \ddots & & & & \\ & & 1 & & & \\ & & \vdots & \ddots & & \\ & & k & \dots & 1 & \\ & & & & \ddots & \\ & & & & & 1 \end{array} \right] \leftarrow i \text {行} \leftarrow j \text {行}</equation>

作用：若<equation>\mathbf{P}(k(i) + (j))\mathbf{A} = \mathbf{A}_3</equation>，则<equation>\mathbf{A}_3</equation>就是将<equation>\mathbf{A}</equation>的第<equation>i</equation>行的<equation>k</equation>倍加到第<equation>j</equation>行上的结果.


将单位矩阵第 i列与第 j列交换后所得到的矩阵，记作

<equation>Q ((i) \leftrightarrow (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ \ddots & & & & \\ & 0 \quad \dots & 1 & & \\ & \vdots & & \vdots & \\ & 1 \quad \dots & 0 & & \\ & & & \ddots & \\ & & & & 1 \end{array} \right]</equation>

作用：将初等列交换矩阵右乘<equation>A</equation>，即若<equation>AQ((i)\leftrightarrow(j)) = A_{4}</equation>，则<equation>A_{4}</equation>就是将<equation>A</equation>的第<equation>i</equation>列与第<equation>j</equation>列交换后的结果.

---


#### （6）初等列倍加矩阵

将单位矩阵的第<equation>i</equation>列乘以一个不等于零的常数<equation>k</equation>后得到的矩阵，记作

<equation>Q (k (i)) = \left[ \begin{array}{c c c c} 1 & & & \\ & \ddots & & \\ & & k & \\ & & & \ddots \\ & & & 1 \end{array} \right].</equation>

作用：若<equation>AQ(k(i)) = A_{5}</equation>，则<equation>A_{5}</equation>就是将<equation>\mathbf{A}</equation>的第<equation>i</equation>列乘上<equation>k</equation>倍后的结果.


将单位矩阵第<equation>i</equation>列的<equation>k</equation>倍加到第<equation>j</equation>列后所得到的矩阵，记作

<equation>Q (k (i) + (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ & \ddots & & \\ & & 1 \dots k & \\ & & \ddots \vdots & \\ & & & 1 \\ & & & \ddots \\ & & & 1 \\ \uparrow_ {i \text {列}} & \uparrow_ {j \text {列}} \end{array} \right].</equation>

---


#### 6. 用初等行(列)变换法求矩阵的秩

作用：若<equation>A Q (k (i) + (j)) = A_{6}</equation>，则<equation>A_{6}</equation>就是将<equation>A</equation>的第<equation>i</equation>列的<equation>k</equation>倍加到第<equation>j</equation>列上的结果.


<equation>\textcircled{1} P ((i) \leftrightarrow (j)) = Q ((i) \leftrightarrow (j)) = Q ^ {\mathrm {T}} ((i) \leftrightarrow (j));</equation>

<equation>\textcircled{2} \boldsymbol {P} (k (i)) = \boldsymbol {Q} (k (i)) = \boldsymbol {Q} ^ {\mathrm {T}} (k (i));</equation>

<equation>\textcircled{3} \boldsymbol {P} (k (i) + (j)) = \boldsymbol {Q} ^ {\mathrm {T}} (k (i) + (j)).</equation>

即：初等行变换矩阵与同类型的初等列变换矩阵之间为转置关系（事实上前两类是相等的对称矩阵）。


<equation>\textcircled{1}</equation>初等矩阵都是可逆矩阵.

<equation>\textcircled{2}</equation>初等矩阵的逆矩阵也是初等矩阵.

<equation>\textcircled{3}</equation>任一个可逆矩阵经过有限次的初等行变换都可化成单位矩阵.

<equation>\textcircled{4}</equation>一个可逆矩阵可分解为一系列初等矩阵的乘积.


初等行（列）变换不改变矩阵的秩.

矩阵的初等行（列）变换前后，矩阵的秩是相等的，而阶梯形矩阵的秩等于阶梯形矩阵中非零行的个数，由任一个矩阵都可经过若干次初等行（列）变换化成阶梯形矩阵，因此任一个矩阵的秩都可通过初等行（列）变换化成阶梯形矩阵后方便地求得.

---


#### (1)等价

<equation>\textcircled{1}</equation>定义

若矩阵<equation>A</equation>可经过一系列初等行变换和列变换后化成矩阵<equation>B</equation>，则称矩阵<equation>A</equation>与<equation>B</equation>是等价的，记作<equation>A\cong B</equation>

<equation>\textcircled{2}</equation>性质

(a)<equation>A\cong A</equation>;

(b)<equation>A\cong B</equation>，则<equation>B\cong A</equation>;

(c)<equation>A\cong B, B\cong C</equation>，则<equation>A\cong C;</equation>

(d)同型矩阵<equation>\mathbf{A}</equation>与<equation>\mathbf{B}</equation>等价<equation>\Leftrightarrow r(\mathbf{A})=r(\mathbf{B}).</equation>

(2) 相似

<equation>\textcircled{1}</equation>定义

对于同阶方阵<equation>A, B</equation>，若存在<equation>|P| \neq 0</equation>，使<equation>P^{-1}AP = B</equation>，则称<equation>A</equation>与<equation>B</equation>相似，记作<equation>A \sim B</equation>.

<equation>\textcircled{2}</equation>性质

(a)<equation>A\sim A</equation>;

(b)<equation>A\sim B</equation>，则<equation>B\sim A</equation>

(c)<equation>A\sim B, B\sim C</equation>，则<equation>A\sim C;</equation>

(d)若<equation>\mathbf{A}\sim\mathbf{B}</equation>，则<equation>\mathbf{A}^{\mathrm{T}}\sim\mathbf{B}^{\mathrm{T}}</equation>

(e) 若<equation>A, B</equation>可逆且<equation>A\sim B</equation>，则<equation>A^{-1}\sim B^{-1}</equation>；

(f)<equation>A\sim B\Rightarrow A^{n}\sim B^{n}, n</equation>为正整数；

(g)相似矩阵有相同的特征值；

（h）相似矩阵的行列式、秩相等；

---


#### (2)性质

（i）同阶实对称矩阵相似的充要条件是它们有相同的特征值（包括重数）.


对于同阶方阵<equation>A, B</equation>，若存在<equation>|P| \neq 0</equation>，使<equation>P^{\mathrm{T}} A P = B</equation>，则称<equation>A</equation>与<equation>B</equation>合同，记为<equation>A \cong B</equation>.


(a)<equation>A\cong A</equation>;

(b) 若<equation>A\cong B</equation>，则<equation>B\cong A;</equation>

(c) 若<equation>A\cong B, B\cong C</equation>，则<equation>A\cong C;</equation>

（d）同阶实对称矩阵合同的充要条件是秩相等且正惯性指数相等.


<equation>\textcircled{1}</equation>相似<equation>\Rightarrow</equation>等价；

<equation>\textcircled{2}</equation>合同<equation>\Rightarrow</equation>等价；

<equation>\textcircled{3}</equation>若<equation>A</equation>与<equation>B</equation>都是实对称矩阵，则<equation>A</equation>与<equation>B</equation>相似<equation>\Leftrightarrow A</equation>与<equation>B</equation>合同


若存在非零向量<equation>\alpha</equation>，使<equation>A\alpha = \lambda \alpha</equation>，则称<equation>\lambda</equation>为方阵<equation>A</equation>的特征值，<equation>\alpha</equation>是<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量.


<equation>\textcircled{1}</equation>若<equation>\lambda</equation>是<equation>A</equation>的特征值，则<equation>\lambda^{k}</equation>是<equation>A^{k}</equation>的特征值.

---


#### 11. 矩阵等价的充要条件

<equation>\textcircled{2}</equation>若<equation>\lambda \neq 0</equation>是<equation>A</equation>的特征值，则<equation>\lambda^{-1}</equation>是<equation>A^{-1}</equation>的特征值.

<equation>\textcircled{3}</equation>若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>是<equation>A</equation>的特征值，则

<equation>\lambda_{1} + \lambda_{2} + \dots +\lambda_{n} = a_{11} + a_{22} + \dots +a_{m}</equation>（A的迹），<equation>\lambda_{1}\lambda_{2}\dots \lambda_{n} = |\mathbf{A}|.</equation>

<equation>\textcircled{4}</equation><equation>\mathbf{A}</equation>与<equation>\mathbf{A}^{\mathrm{T}}</equation>有相同的特征值.

<equation>\textcircled{5}</equation>矩阵 A属于不同特征值的特征向量必线性无关.

<equation>\textcircled{6}</equation>实对称矩阵属于不同特征值的特征向量必正交.


A可逆<equation>\Leftrightarrow</equation><equation>|A| \neq 0 \Leftrightarrow A=P_{1} P_{2}\dots P_{i}</equation>，其中<equation>P_{i}</equation>（<equation>i=1</equation>2，...，l）为初等矩阵

<equation>\Leftrightarrow A\cong E</equation>（<equation>E</equation>为<equation>n</equation>阶单位矩阵）.


<equation>A\cong B\Leftrightarrow</equation>存在可逆矩阵<equation>P, Q</equation>使<equation>PAQ = B</equation>

<equation>\Leftrightarrow r (\mathbf {A}) = r (\mathbf {B}).</equation>

---


### 第三章 向量