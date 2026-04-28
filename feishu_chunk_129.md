#### 偏导数的概念与计算

**2025年第14题 | 填空题 | 5分**

14. 已知函数<equation>z=z(x,y)</equation>由<equation>z+\ln z-\int_{y}^{x}x\mathrm{e}^{-t^{2}}\mathrm{d}t=1</equation>确定，则<equation>\left.\frac{\partial^{2} z}{\partial x^{2}}\right|_{(1,1)}=</equation>___

**解析:**解 将<equation>x = 1,y = 1</equation>代入方程<equation>z + \ln z - \int_{y}^{x}x\mathrm{e}^{-t^{2}}\mathrm{d}t = 1</equation>可得，<equation>z(1,1) + \ln z(1,1) = 1.</equation>注意到<equation>z = 1</equation>是方程<equation>z + \ln z = 1</equation>的一个解，且<equation>(z + \ln z)^{\prime} = 1 + \frac{1}{z} > 0</equation>，函数<equation>z + \ln z</equation>单调增加，故1是该方程的唯一解，<equation>z(1,1) = 1.</equation>已知方程可写为<equation>z+\ln z-x\int_{y}^{x}\mathrm{e}^{-t^{2}}\mathrm{d} t=1</equation>，对该方程两端关于 x求偏导数可得<equation>\frac {\partial z}{\partial x} + \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \int_ {y} ^ {x} \mathrm {e} ^ {- t ^ {2}} \mathrm {d} t - x \cdot \mathrm {e} ^ {- x ^ {2}} = 0.</equation>在(1)式中代入<equation>x = 1,y = 1,z = 1</equation>可得<equation>2\frac{\partial z}{\partial x}\bigg|_{(1,1)} = \mathrm{e}^{-1}</equation>，解得<equation>\frac{\partial z}{\partial x}\bigg|_{(1,1)} = \frac{1}{2\mathrm{e}}.</equation>对（1）式两端关于 x求偏导数可得<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {1}{z} \cdot \frac {\partial^ {2} z}{\partial x ^ {2}} - \frac {1}{z ^ {2}} \cdot \left(\frac {\partial z}{\partial x}\right) ^ {2} - \mathrm {e} ^ {- x ^ {2}} - \mathrm {e} ^ {- x ^ {2}} + 2 x ^ {2} \mathrm {e} ^ {- x ^ {2}} = 0.</equation>在（2）式中代入<equation>x=1,y=1,z=1,\frac{\partial z}{\partial x}\bigg|_{(1,1)}=\frac{1}{2\mathrm{e}}</equation>可得<equation>2\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)}-\frac{1}{4\mathrm{e}^{2}}-2\mathrm{e}^{-1}+2\mathrm{e}^{-1}=0</equation>解得<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)}=\frac{1}{8\mathrm{e}^{2}}.</equation>

---

**2024年第18题 | 解答题 | 12分**

18. (本题满分12分）设函数<equation>z=z(x,y)</equation>由方程<equation>z+\mathrm{e}^{x}-y\ln(1+z^{2})=0</equation>确定，求<equation>\left.\left(\frac{\partial^{2} z}{\partial x^{2}}+\frac{\partial^{2} z}{\partial y^{2}}\right)\right|_{(0,0)}</equation>

**解析:**解 将 x=0,y=0代入方程<equation>z+{\mathrm{e}}^{x}-y\ln(1+z^{2})=0</equation>可得，<equation>z(0,0)+1=0</equation>即<equation>z(0,0)=-1.</equation>对方程<equation>z+{\mathrm{e}}^{x}-y\ln(1+z^{2})=0</equation>两端同时关于 x求偏导数可得，<equation>\frac {\partial z}{\partial x} + \mathrm {e} ^ {x} - y \cdot \frac {2 z \frac {\partial z}{\partial x}}{1 + z ^ {2}} = 0, \quad \text {即} \frac {\partial z}{\partial x} + \mathrm {e} ^ {x} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial z}{\partial x} = 0.</equation>将<equation>x = 0,y = 0,z = -1</equation>代人（1）式可得，<equation>\frac{\partial z}{\partial x}\bigg|_{(0,0)} + 1 = 0</equation>，即<equation>\frac{\partial z}{\partial x}\bigg|_{(0,0)} = -1.</equation>对<equation>\frac{\partial z}{\partial x} +\mathrm{e}^{x} -\frac{2yz}{1+z^{2}}\cdot \frac{\partial z}{\partial x} = 0</equation>两端关于<equation>x</equation>求偏导数可得，<equation>\frac {\partial^ {2} z}{\partial x ^ {2}} + \mathrm {e} ^ {x} - 2 y \cdot \frac {1 + z ^ {2} - 2 z ^ {2}}{\left(1 + z ^ {2}\right) ^ {2}} \cdot \left(\frac {\partial z}{\partial x}\right) ^ {2} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>将<equation>x = 0,y = 0,z = -1,\frac{\partial z}{\partial x}\bigg|_{(0,0)} = -1</equation>代人(2）式可得，<equation>\frac{\partial^2z}{\partial x^2}\bigg|_{(0,0)} + 1 = 0</equation>，即<equation>\frac{\partial^2z}{\partial x^2}\bigg|_{(0,0)} = -1.</equation>对方程<equation>z + \mathrm{e}^{x} - y\ln (1 + z^{2}) = 0</equation>两端同时关于 y求偏导数可得，<equation>\frac {\partial z}{\partial y} - \ln \left(1 + z ^ {2}\right) - y \cdot \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} = 0, \quad \text {即} \frac {\partial z}{\partial y} - \ln \left(1 + z ^ {2}\right) - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial z}{\partial y} = 0.</equation>将<equation>x = 0,y = 0,z = -1</equation>代人（3）式可得，<equation>\frac{\partial z}{\partial y}\bigg|_{(0,0)} - \ln 2 = 0</equation>，即<equation>\frac{\partial z}{\partial y}\bigg|_{(0,0)} = \ln 2.</equation>对<equation>\frac{\partial z}{\partial y}-\ln(1+z^{2})-\frac{2yz}{1+z^{2}}\cdot \frac{\partial z}{\partial y}=0</equation>两端关于 y求偏导数可得，<equation>\frac {\partial^ {2} z}{\partial y ^ {2}} - \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} - \frac {2 z \frac {\partial z}{\partial y}}{1 + z ^ {2}} - 2 y \cdot \frac {1 + z ^ {2} - 2 z ^ {2}}{\left(1 + z ^ {2}\right) ^ {2}} \cdot \left(\frac {\partial z}{\partial y}\right) ^ {2} - \frac {2 y z}{1 + z ^ {2}} \cdot \frac {\partial^ {2} z}{\partial y ^ {2}} = 0.</equation>将<equation>x = 0,y = 0,z = -1,\frac{\partial z}{\partial y}\bigg|_{(0,0)} = \ln 2</equation>代入(4)式可得，<equation>\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(0,0)} + 2\ln 2 = 0</equation>，即<equation>\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(0,0)} = -2\ln 2.</equation>因此，<equation>\left(\frac{\partial^{2}z}{\partial x^{2}} + \frac{\partial^{2}z}{\partial y^{2}}\right)\bigg|_{(0,0)} = -1 - 2\ln 2.</equation>

---

**2023年第1题 | 选择题 | 5分 | 答案: A**

1. 已知函数<equation>f ( x,y)=\ln ( y+| x \sin y | )</equation>，则（    ）

A.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)}</equation>不存在，<equation>\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>存在

B.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)}</equation>存在，<equation>\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>不存在

C.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)},\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>均存在

D.<equation>\left. \frac{\partial f}{\partial x}\right|_{(0,1)},\left. \frac{\partial f}{\partial y}\right|_{(0,1)}</equation>均不存在

答案: A

**解析:**由<equation>f ( x,y )</equation>的表达式可知，<equation>f ( 0,1 )=0.</equation>根据偏导数的定义，<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 1)} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - f (0 , 1)}{x - 0} = \lim _ {x \rightarrow 0} \frac {\ln (1 + | x \sin 1 |)}{x} = \lim _ {x \rightarrow 0} \frac {| x | \sin 1}{x}.</equation>由于<equation>\lim_{x\to 0^{-}}\frac{|x|}{x} = -1,</equation><equation>\lim_{x\to 0^{+}}\frac{|x|}{x} = 1,</equation>故<equation>\lim_{x\to 0}\frac{|x|}{x}</equation>不存在，从而<equation>\left.\frac{\partial f}{\partial x}\right|_{(0,1)}</equation>不存在.<equation>\left. \frac {\partial f}{\partial y} \right| _ {(0, 1)} = \lim _ {y \rightarrow 1} \frac {f (0 , y) - f (0 , 1)}{y - 1} = \lim _ {y \rightarrow 1} \frac {\ln y}{y - 1} = \lim _ {y \rightarrow 1} \frac {\ln (1 + y - 1)}{y - 1} = \lim _ {y \rightarrow 1} \frac {y - 1}{y - 1} = 1.</equation>因此，<equation>\frac{\partial f}{\partial y}\bigg|_{(0,1)}=1.</equation>综上所述，<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)}</equation>不存在，<equation>\frac{\partial f}{\partial y}\bigg|_{(0,1)}</equation>存在，应选A.

---

**2022年第3题 | 选择题 | 5分 | 答案: C**

3. 已知 f(t) 连续，令<equation>F ( x,y)=\int_{0}^{x-y} ( x-y-t ) f ( t ) \mathrm{d} t</equation>，则（    ）<equation>\begin{aligned} \mathrm {A}. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \\ \mathrm {C}. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation><equation>\begin{aligned} B. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \\ D. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation>

答案: C

**解析:**解 整理 F(x,y）的表达式.<equation>F (x, y) = \int_ {0} ^ {x - y} (x - y - t) f (t) \mathrm {d} t = (x - y) \int_ {0} ^ {x - y} f (t) \mathrm {d} t - \int_ {0} ^ {x - y} t f (t) \mathrm {d} t.</equation>分别计算<equation>\frac{\partial F}{\partial x},\frac{\partial^{2} F}{\partial x^{2}},\frac{\partial F}{\partial y},\frac{\partial^{2} F}{\partial y^{2}}.</equation><equation>\frac {\partial F}{\partial x} = (x - y) f (x - y) + \int_ {0} ^ {x - y} f (t) \mathrm {d} t - (x - y) f (x - y) = \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial \left[ \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial x} = f (x - y),</equation><equation>\frac {\partial F}{\partial y} = - (x - y) f (x - y) - \int_ {0} ^ {x - y} f (t) \mathrm {d} t + (x - y) f (x - y) = - \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial y ^ {2}} = \frac {\partial \left[ - \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial y} = f (x - y).</equation>因此，<equation>\frac{\partial F}{\partial x}=-\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial x^{2}}=\frac{\partial^{2}F}{\partial y^{2}}.</equation>应选C.

---

**2019年第16题 | 解答题 | 10分**

16. (本题满分10分）

设函数 f(u,v)具有2阶连续偏导数，函数 g(x,y) = xy-f(x+y,x-y).求<equation>\frac{\partial^{2} g}{\partial x^{2}}+\frac{\partial^{2} g}{\partial x \partial y}+\frac{\partial^{2} g}{\partial y^{2}}.</equation>

**答案:**<equation>1 - 3 f_{11}^{\prime \prime} ( x + y, x - y ) - f_{22}^{\prime \prime} ( x + y, x - y ).</equation>

**解析:**<equation>\begin{aligned} \frac {\partial g}{\partial x} &= y - f _ {1} ^ {\prime} (x + y, x - y) - f _ {2} ^ {\prime} (x + y, x - y), \\ \frac {\partial g}{\partial y} &= x - f _ {1} ^ {\prime} (x + y, x - y) + f _ {2} ^ {\prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial x ^ {2}} &= - f _ {1 1} ^ {\prime \prime} (x + y, x - y) - f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} - f _ {1 1} ^ {\prime \prime} (x + y, x - y) - 2 f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial x \partial y} &= 1 - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 1} ^ {\prime \prime} (x + y, x - y) + f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} 1 - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {2 2} ^ {\prime \prime} (x + y, x - y), \\ \frac {\partial^ {2} g}{\partial y ^ {2}} &= - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + f _ {1 2} ^ {\prime \prime} (x + y, x - y) + f _ {2 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y) \\ \frac {f (u , v) \mathrm {具 有} 2 \mathrm {阶 连 续 偏 导 数}}{} - f _ {1 1} ^ {\prime \prime} (x + y, x - y) + 2 f _ {1 2} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y). \\ \mathrm {代 入} \frac {\partial^ {2} g}{\partial x ^ {2}} + \frac {\partial^ {2} g}{\partial x \partial y} + \frac {\partial^ {2} g}{\partial y ^ {2}} \mathrm {可 得}, \\ \frac {\partial^ {2} g}{\partial x} \frac {\partial^ {2} g}{\partial y} \frac {\partial^ {2} g}{\partial y ^ {2}} \end{aligned}</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} + \frac {\partial^ {2} g}{\partial x \partial y} + \frac {\partial^ {2} g}{\partial y ^ {2}} = 1 - 3 f _ {1 1} ^ {\prime \prime} (x + y, x - y) - f _ {2 2} ^ {\prime \prime} (x + y, x - y).</equation>

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x,y)=\frac{\mathrm{e}^{x}}{x-y}</equation>，则（    ）

A.<equation>f_{x}^{\prime}-f_{y}^{\prime}=0</equation>B.<equation>f_{x}^{\prime}+f_{y}^{\prime}=0</equation>C.<equation>f_{x}^{\prime}-f_{y}^{\prime}=f</equation>D.<equation>f_{x}^{\prime}+f_{y}^{\prime}=f</equation>

答案: D

**解析:**分别计算<equation>f_{x}^{\prime}, f_{y}^{\prime}</equation>得

因此，<equation>f _ {x} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y) - \mathrm {e} ^ {x}}{(x - y) ^ {2}}, \quad f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x}}{(x - y) ^ {2}}.</equation><equation>f _ {x} ^ {\prime} + f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y)}{(x - y) ^ {2}} = \frac {\mathrm {e} ^ {x}}{x - y} = f.</equation>应选 D.

---

**2013年第10题 | 填空题 | 4分**

10. 设函数<equation>z=z(x,y)</equation>由方程<equation>( z+y )^{x}= x y</equation>确定，则<equation>\left. \frac{\partial z}{\partial x} \right|_{(1,2)}=</equation>___

**答案:**# 2(1-ln2).

**解析:**解 将方程<equation>( z+y)^{x}=xy</equation>化为<equation>\mathrm{e}^{x\ln(z+y)}=xy</equation>，对所得方程两端关于 x求偏导数，可得<equation>\mathrm {e} ^ {x \ln (z + y)} \left[ \ln (z + y) + \frac {x \cdot \frac {\partial z}{\partial x}}{z + y} \right] = y.</equation>当 x=1，y=2时，由原方程可知 z=0，从而由上式可得<equation>\mathrm{e}^{\ln 2}\left(\ln 2+\frac{\frac{\partial z}{\partial x}\bigg|_{(1,2)}}{2}\right)=2</equation>即<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,2)}= 2(1-\ln 2).</equation>

---

**2011年第16题 | 解答题 | 10分**

16. (本题满分10分）

已知函数 f(u,v)具有二阶连续偏导数，<equation>f(1,1)=2</equation>是 f(u,v)的极值，<equation>z=f(x+y,f(x,y))</equation>.求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{(1,1)}.</equation>

**答案:**<equation>= f_{11}^{\prime \prime}(2,2) + f_{2}^{\prime}(2,2)f_{12}^{\prime \prime}(1,1).</equation>

**解析:**对<equation>z = f(x + y,f(x,y))</equation>两端关于<equation>x</equation>求偏导数得<equation>\frac {\partial z}{\partial x} = f _ {1} ^ {\prime} (x + y, f (x, y)) + f _ {2} ^ {\prime} (x + y, f (x, y)) \cdot f _ {1} ^ {\prime} (x, y).</equation>继续对上式两端关于 y求偏导数得<equation>\begin{array}{l} \frac {\partial^ {2} z}{\partial x \partial y} = f _ {1 1} ^ {\prime \prime} (x + y, f (x, y)) + f _ {1 2} ^ {\prime \prime} (x + y, f (x, y)) f _ {2} ^ {\prime} (x, y) \\ + \left[ f _ {2 1} ^ {\prime \prime} (x + y, f (x, y)) + f _ {2 2} ^ {\prime \prime} (x + y, f (x, y)) f _ {2} ^ {\prime} (x, y) \right] f _ {1} ^ {\prime} (x, y) \\ + f _ {2} ^ {\prime} (x + y, f (x, y)) f _ {1 2} ^ {\prime \prime} (x, y). \\ \end{array}</equation>由极值的必要条件可知<equation>f_1^{\prime}(1,1) = f_2^{\prime}(1,1) = 0.</equation>将<equation>f(1,1) = 2,f_1^{\prime}(1,1) = f_2^{\prime}(1,1) = 0</equation>代入上式可得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {(1, 1)} = f _ {1 1} ^ {\prime \prime} (2, 2) + f _ {2} ^ {\prime} (2, 2) f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2009年第10题 | 填空题 | 4分**

10. 设<equation>z=(x+\mathrm{e}^{y})^{x}</equation>，则<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,0)}=</equation>___

**答案:**## 2ln2+1.

**解析:**（法一）在点（1，0）附近，<equation>x > 0</equation>，从而<equation>x+\mathrm{e}^{y}>0, z>0.</equation>对<equation>z=(x+\mathrm{e}^{y})^{x}</equation>两端取对数得到<equation>\ln z = x \ln \left(x + \mathrm {e} ^ {y}\right).</equation>对上式两端关于 x求导得，<equation>\frac {1}{z} \cdot \frac {\partial z}{\partial x} = \ln \left(x + \mathrm {e} ^ {y}\right) + \frac {x}{x + \mathrm {e} ^ {y}}.</equation>当<equation>x = 1</equation>，<equation>y = 0</equation>时，<equation>z = 2.</equation>因此，<equation>\frac{\partial z}{\partial x}\bigg|_{(1,0)} = 2\left(\ln 2 + \frac{1}{2}\right) = 2\ln 2 + 1.</equation>（法二）将<equation>y = 0</equation>代入<equation>z = (x + \mathrm{e}^{y})^{x}</equation>中得到<equation>z(x,0) = (x + 1)^{x}</equation>.于是，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(1, 0)} = \frac {\mathrm {d} \left[ (x + 1) ^ {x} \right]}{\mathrm {d} x} \Bigg | _ {x = 1} = \left[ \mathrm {e} ^ {x \ln (x + 1)} \right] ^ {\prime} \Bigg | _ {x = 1} = \mathrm {e} ^ {x \ln (x + 1)} \left[ \ln (x + 1) + \frac {x}{x + 1} \right] \Bigg | _ {x = 1} = 2 \ln 2 + 1.</equation>

---


