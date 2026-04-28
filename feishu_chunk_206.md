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


