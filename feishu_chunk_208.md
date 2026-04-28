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


