# 数学二

## 高等数学

### 多元函数微积分学

#### 偏导数的概念与计算

**2025年第1题 | 选择题 | 5分 | 答案: A**

1. 设函数<equation>z=z(x,y)</equation>由<equation>z+\ln z-\int_{y}^{x}\mathrm{e}^{-t^{2}}\mathrm{d}t=0</equation>确定，则<equation>\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}=</equation>(    )

A.<equation>\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}-\mathrm{e}^{-y^{2}} \right)</equation>B.<equation>\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}+\mathrm{e}^{-y^{2}} \right)</equation>C.<equation>-\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}-\mathrm{e}^{-y^{2}} \right)</equation>D.<equation>-\frac{z}{z+1} \left( \mathrm{e}^{-x^{2}}+\mathrm{e}^{-y^{2}} \right)</equation>

答案: A

**解析:**解 对已知方程两端关于 x求偏导数可得<equation>\frac {\partial z}{\partial x} + \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \mathrm {e} ^ {- x ^ {2}} = 0.</equation>整理可得<equation>\frac{z + 1}{z}\frac{\partial z}{\partial x} = \mathrm{e}^{-x^2}</equation>，解得<equation>\frac{\partial z}{\partial x} = \frac{z}{z + 1}\mathrm{e}^{-x^2}</equation>.

同理，对已知方程两端关于 y 求偏导数可得<equation>\frac {\partial z}{\partial y} + \frac {1}{z} \cdot \frac {\partial z}{\partial y} + \mathrm {e} ^ {- \gamma^ {2}} = 0.</equation>整理可得<equation>\frac{z + 1}{z}\frac{\partial z}{\partial y} = -\mathrm{e}^{-y^2}</equation>，解得<equation>\frac{\partial z}{\partial y} = -\frac{z}{z + 1}\mathrm{e}^{-y^2}</equation>.

因此，<equation>\frac {\partial z}{\partial x} + \frac {\partial z}{\partial y} = \frac {z}{z + 1} \left(\mathrm {e} ^ {- x ^ {2}} - \mathrm {e} ^ {- y ^ {2}}\right).</equation>应选A.

---

**2024年第5题 | 选择题 | 5分 | 答案: C**

5. 已知函数<equation>f ( x,y)=\left\{\begin{array}{ll} \left(x^{2}+y^{2}\right)\sin \frac{1}{xy},& xy\neq 0\\ 0,& xy=0 \end{array} \right.</equation>则在点（0，0）处（    ）

A.<equation>\frac{\partial f(x,y)}{\partial x}</equation>连续，f(x,y)可微 B.<equation>\frac{\partial f(x,y)}{\partial x}</equation>连续，f(x,y)不可微

C.<equation>\frac{\partial f(x,y)}{\partial x}</equation>不连续，f(x,y)可微 D.<equation>\frac{\partial f(x,y)}{\partial x}</equation>不连续，f(x,y)不可微

答案: C

**解析:**解 当<equation>y = 0</equation>时，根据偏导数的定义，<equation>\frac{\partial f(x,y)}{\partial x}\bigg|_{(x,0)} = \lim_{\Delta x\to 0}\frac{f(x + \Delta x,0) - f(x,0)}{\Delta x} = \lim_{\Delta x\to 0}\frac{0 - 0}{\Delta x} = 0,</equation>即<equation>f_x^{\prime}(x,0) = 0.</equation>同理可得<equation>\frac{\partial f(x,y)}{\partial y}\bigg|_{(0,y)} = 0,</equation>即<equation>f_y^{\prime}(0,y) = 0.</equation>特别地，<equation>f_x^{\prime}(0,0) = f_y^{\prime}(0,0) = 0.</equation><equation>- 0 -</equation>当 xy≠0时，由链式法则可得<equation>\frac {\partial f (x , y)}{\partial x} = 2 x \sin \frac {1}{x y} + \left(x ^ {2} + y ^ {2}\right) \cdot \cos \frac {1}{x y} \cdot \left(- \frac {1}{x ^ {2} y}\right) = 2 x \sin \frac {1}{x y} - \frac {x ^ {2} + y ^ {2}}{x ^ {2} y} \cos \frac {1}{x y}.</equation>取<equation>x_{n} = y_{n} = \frac{1}{\sqrt{2n\pi}}</equation>，则<equation>\lim_{n\to \infty}x_n = \lim_{n\to \infty}y_n = 0,\sin \frac{1}{x_n y_n}\equiv 0,\cos \frac{1}{x_n y_n}\equiv 1</equation>，而<equation>\frac {x _ {n} ^ {2} + y _ {n} ^ {2}}{x _ {n} ^ {2} y _ {n}} = \frac {\frac {1}{2 n \pi} + \frac {1}{2 n \pi}}{\frac {1}{2 n \pi \sqrt {2 n \pi}}} = 2 \sqrt {2 n \pi},</equation>从而<equation>\lim _ {n \rightarrow \infty} \left(2 x _ {n} \sin \frac {1}{x _ {n} y _ {n}} - \frac {x _ {n} ^ {2} + y _ {n} ^ {2}}{x _ {n} ^ {2} y _ {n}} \cos \frac {1}{x _ {n} y _ {n}}\right) = - \infty .</equation>由此可得，<equation>\lim_{(x,y)\to(0,0)} \left( 2x\sin \frac{1}{xy}-\frac{x^{2}+y^{2}}{x^{2}y}\cos \frac{1}{xy}\right)</equation>不存在.进一步可得<equation>\frac{\partial f(x,y)}{\partial x}</equation>在点（0,0）处不连续另一方面，<equation>\begin{aligned} \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f (0 , 0) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - 0 - 0 \cdot x - 0 \cdot y}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y)}{\sqrt {x ^ {2} + y ^ {2}}}. \end{aligned}</equation>当 xy≠0时，<equation>\left|\sin \frac{1}{xy}\right|\leqslant 1</equation>，故<equation>0 \leqslant \frac {\left| f (x , y) \right|}{\sqrt {x ^ {2} + y ^ {2}}} = \left| \sqrt {x ^ {2} + y ^ {2}} \sin \frac {1}{x y} \right| \leqslant \sqrt {x ^ {2} + y ^ {2}},</equation>当<equation>xy = 0</equation>时，<equation>\frac{|f(x,y)|}{\sqrt{x^2 + y^2}} = 0\leqslant \sqrt{x^2 + y^2}.</equation>进一步由<equation>\lim_{(x,y)\to(0,0)}\sqrt{x^2 + y^2} = 0</equation>以及夹逼准则可得<equation>\lim_{(x,y)\to(0,0)}\frac{|f(x,y)|}{\sqrt{x^2 + y^2}} = 0</equation>，从而<equation>\lim_{(x,y)\to(0,0)}\frac{f(x,y)}{\sqrt{x^2 + y^2}} = 0.</equation>于是，由可微的定义可知，<equation>f(x,y)</equation>在点(0,0)处可微.

综上所述，应选C.

---

**2024年第20题 | 解答题 | 12分**

20. (本题满分12分)

已知函数 f(u,v)具有二阶连续偏导数，且函数 g(x,y)=f(2x+y,3x-y)满足<equation>\frac{\partial^{2} g}{\partial x^{2}}+\frac{\partial^{2} g}{\partial x \partial y}-6 \frac{\partial^{2} g}{\partial y^{2}}=1.</equation>I. 求<equation>\frac{\partial^{2} f}{\partial u \partial v}</equation>；

II. 若<equation>\frac{\partial f(u,0)}{\partial u}=u e^{-u}</equation>，且 f(0,v)<equation>= \frac{1}{50} v^{2}-1</equation>，求 f(u,v)的表达式.

**答案:**(1)<equation>\frac {\partial^ {2} f}{\partial v \partial v} = \frac {1}{2 5}</equation>(2)<equation>f (u, v) = - (u + 1) e ^ {- u} + \frac {1}{2 5} u v + \frac {1}{5 0} v ^ {2}</equation>

**解析:**解（I）根据链式法则，并结合<equation>f(u,v)</equation>具有2阶连续偏导数，从而<equation>\frac{\partial^{2} f}{\partial u \partial v}=\frac{\partial^{2} f}{\partial v \partial u}</equation>可得<equation>\frac {\partial g}{\partial x} = 2 \frac {\partial f}{\partial u} + 3 \frac {\partial f}{\partial v},</equation><equation>\frac {\partial g}{\partial y} = \frac {\partial f}{\partial u} - \frac {\partial f}{\partial v},</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} = 2 \left(2 \frac {\partial^ {2} f}{\partial u ^ {2}} + 3 \frac {\partial^ {2} f}{\partial u \partial v}\right) + 3 \left(2 \frac {\partial^ {2} f}{\partial v \partial u} + 3 \frac {\partial^ {2} f}{\partial v ^ {2}}\right) = 4 \frac {\partial^ {2} f}{\partial u ^ {2}} + 1 2 \frac {\partial^ {2} f}{\partial u \partial v} + 9 \frac {\partial^ {2} f}{\partial v ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial x \partial y} = 2 \left(\frac {\partial^ {2} f}{\partial u ^ {2}} - \frac {\partial^ {2} f}{\partial u \partial v}\right) + 3 \left(\frac {\partial^ {2} f}{\partial v \partial u} - \frac {\partial^ {2} f}{\partial v ^ {2}}\right) = 2 \frac {\partial^ {2} f}{\partial u ^ {2}} + \frac {\partial^ {2} f}{\partial u \partial v} - 3 \frac {\partial^ {2} f}{\partial v ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial y ^ {2}} = \frac {\partial^ {2} f}{\partial u ^ {2}} - \frac {\partial^ {2} f}{\partial u \partial v} - \left(\frac {\partial^ {2} f}{\partial v \partial u} - \frac {\partial^ {2} f}{\partial v ^ {2}}\right) = \frac {\partial^ {2} f}{\partial u ^ {2}} - 2 \frac {\partial^ {2} f}{\partial u \partial v} + \frac {\partial^ {2} f}{\partial v ^ {2}}.</equation>将上述结果代入<equation>\frac{\partial^{2}g}{\partial x^{2}}+\frac{\partial^{2}g}{\partial x\partial y}-6\frac{\partial^{2}g}{\partial y^{2}}=1</equation>可得<equation>4 \frac {\partial^ {2} f}{\partial u ^ {2}} + 1 2 \frac {\partial^ {2} f}{\partial u \partial v} + 9 \frac {\partial^ {2} f}{\partial v ^ {2}} + 2 \frac {\partial^ {2} f}{\partial u ^ {2}} + \frac {\partial^ {2} f}{\partial u \partial v} - 3 \frac {\partial^ {2} f}{\partial v ^ {2}} - 6 \frac {\partial^ {2} f}{\partial u ^ {2}} + 1 2 \frac {\partial^ {2} f}{\partial u \partial v} - 6 \frac {\partial^ {2} f}{\partial v ^ {2}} = 1.</equation>整理可得<equation>25\frac{\partial^{2}f}{\partial u\partial v} = 1</equation>，即<equation>\frac{\partial^{2}f}{\partial u\partial v} = \frac{1}{25}</equation>（Ⅱ）对<equation>\frac{\partial^{2} f}{\partial u \partial v}</equation>关于<equation>v</equation>积分可得，<equation>\frac {\partial f}{\partial u} = \int \frac {\partial^ {2} f}{\partial u \partial v} \mathrm {d} v = \int \frac {1}{2 5} \mathrm {d} v = \frac {v}{2 5} + C _ {1} (u),</equation>其中<equation>C_{1}(u)</equation>是关于<equation>u</equation>的一元函数.

由于<equation>\frac{\partial f(u,0)}{\partial u}=u\mathrm{e}^{-u}</equation>，故在<equation>\frac{\partial f}{\partial u}=\frac{v}{25}+C_{1}(u)</equation>中令<equation>v=0</equation>可得<equation>C_{1}(u)=u\mathrm{e}^{-u}.</equation>于是，<equation>\frac{\partial f}{\partial u}=\frac{v}{25}+</equation><equation>u\mathrm{e}^{-u}.</equation>对<equation>\frac{\partial f}{\partial u}</equation>关于 u积分可得，<equation>\begin{aligned} f (u, v) &= \int \frac {\partial f}{\partial u} \mathrm {d} u = \int \left(\frac {v}{2 5} + u \mathrm {e} ^ {- u}\right) \mathrm {d} u = \frac {u v}{2 5} - \int u \mathrm {d} \left(\mathrm {e} ^ {- u}\right) \\ &= \frac {u v}{2 5} - \left(u \mathrm {e} ^ {- u} - \int \mathrm {e} ^ {- u} \mathrm {d} u\right) = \frac {u v}{2 5} - u \mathrm {e} ^ {- u} - \mathrm {e} ^ {- u} + C _ {2} (v), \end{aligned}</equation>其中<equation>C_{2}(v)</equation>是关于<equation>v</equation>的一元函数.

由于<equation>f(0,v) = \frac{1}{50} v^{2} - 1</equation>，故在<equation>f(u,v) = \frac{uv}{25} - u\mathrm{e}^{-u} - \mathrm{e}^{-u} + C_{2}(v)</equation>中令<equation>u = 0</equation>可得，<equation>\frac{v^2}{50} - 1 = -1</equation><equation>+C_{2}(v)</equation>，即<equation>C_{2}(v) = \frac{v^{2}}{50}</equation>.

因此，<equation>f ( u,v) = \frac{u v}{2 5} +\frac{v^{2}}{5 0} -(u + 1) \mathrm{e}^{-u}.</equation>

---

**2023年第13题 | 填空题 | 5分**

13. 设函数<equation>z=z(x,y)</equation>由<equation>\mathrm{e}^{z}+xz=2x-y</equation>确定，则<equation>\left.\frac{\partial^{2} z}{\partial x^{2}}\right|_{(1,1)}=</equation>___

**答案:**# 3 2

**解析:**解 将 x=1，y=1 代入已知方程，可得<equation>\mathrm{e}^{z}+z=1.</equation>考虑<equation>f ( z )=\mathrm{e}^{z}+z-1.</equation>由于<equation>f^{\prime}(z)=\mathrm{e}^{z}+1>0,f(0)=0</equation>，故 f(z)单调增加，z=0是f(z)的唯一零点.于是，<equation>z ( 1,1 )=0.</equation>对方程<equation>\mathrm{e}^{z}+xz=2x-y</equation>两端关于 x求偏导数，可得<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial x} + z + x \frac {\partial z}{\partial x} = 2.</equation>将<equation>x=1,y=1,z=0</equation>代入（1）式可得<equation>2\frac{\partial z}{\partial x}=2.</equation>因此，<equation>\left.\frac{\partial z}{\partial x}\right|_{(1,1)}=1.</equation>对（1）式两端继续关于 x求偏导数，可得<equation>\mathrm {e} ^ {z} \left(\frac {\partial z}{\partial x}\right) ^ {2} + \mathrm {e} ^ {z} \frac {\partial^ {2} z}{\partial x ^ {2}} + \frac {\partial z}{\partial x} + \frac {\partial z}{\partial x} + x \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>整理可得<equation>\mathrm {e} ^ {z} \left(\frac {\partial z}{\partial x}\right) ^ {2} + 2 \frac {\partial z}{\partial x} + \left(\mathrm {e} ^ {z} + x\right) \frac {\partial^ {2} z}{\partial x ^ {2}} = 0.</equation>将<equation>x = 1,y = 1,z = 0,\frac{\partial z}{\partial x}\bigg|_{(1,1)} = 1</equation>代入（2）式可得<equation>3 + 2\frac{\partial^{2}z}{\partial x^{2}} = 0.</equation>因此，<equation>\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(1,1)} = -\frac{3}{2}.</equation>

---

**2022年第4题 | 选择题 | 5分 | 答案: C**

4. 已知 f(t) 连续，令<equation>F ( x,y)=\int_{0}^{x-y} ( x-y-t ) f ( t ) \mathrm{d} t</equation>，则（    ）<equation>\begin{aligned} \mathrm {A.} \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \\ \mathrm {C.} \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation><equation>\begin{aligned} B. \frac {\partial F}{\partial x} &= \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \\ D. \frac {\partial F}{\partial x} &= - \frac {\partial F}{\partial y}, \frac {\partial^ {2} F}{\partial x ^ {2}} = - \frac {\partial^ {2} F}{\partial y ^ {2}} \end{aligned}</equation>

答案: C

**解析:**解 整理 F(x,y）的表达式.<equation>F (x, y) = \int_ {0} ^ {x - y} (x - y - t) f (t) \mathrm {d} t = (x - y) \int_ {0} ^ {x - y} f (t) \mathrm {d} t - \int_ {0} ^ {x - y} t f (t) \mathrm {d} t.</equation>分别计算<equation>\frac{\partial F}{\partial x},\frac{\partial^{2}F}{\partial x^{2}},\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial y^{2}}.</equation><equation>\frac {\partial F}{\partial x} = (x - y) f (x - y) + \int_ {0} ^ {x - y} f (t) \mathrm {d} t - (x - y) f (x - y) = \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial x ^ {2}} = \frac {\partial \left[ \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial x} = f (x - y),</equation><equation>\frac {\partial F}{\partial y} = - (x - y) f (x - y) - \int_ {0} ^ {x - y} f (t) \mathrm {d} t + (x - y) f (x - y) = - \int_ {0} ^ {x - y} f (t) \mathrm {d} t,</equation><equation>\frac {\partial^ {2} F}{\partial y ^ {2}} = \frac {\partial \left[ - \int_ {0} ^ {x - y} f (t) \mathrm {d} t \right]}{\partial y} = f (x - y).</equation>因此，<equation>\frac{\partial F}{\partial x}=-\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial x^{2}}=\frac{\partial^{2}F}{\partial y^{2}}.</equation>应选C.

---

**2021年第13题 | 填空题 | 5分**

13. 设函数<equation>z=z(x,y)</equation>由方程<equation>( x+1 ) z+y \ln z-\arctan ( 2 x y )=1</equation>确定，则<equation>\left. \frac{\partial z}{\partial x}\right|_{(0,2)}=</equation>___

**答案:**```latex

1.
```
**解析: **解 对方程两端关于 x求偏导，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} + y \cdot \frac {1}{z} \cdot \frac {\partial z}{\partial x} - \frac {2 y}{1 + 4 x ^ {2} y ^ {2}} = 0.</equation>解得<equation>\left(x + 1 + \frac {y}{z}\right) \frac {\partial z}{\partial x} = \frac {2 y}{1 + 4 x ^ {2} y ^ {2}} - z.</equation>将 x=0,y=2代入方程（x+1）z+y<equation>\ln z-\arctan(2 x y)=1</equation>可得 z+2<equation>\ln z=1</equation>.观察可得 z=1 是该方程的一个实根.计算函数 f（z）=z+2<equation>\ln z-1</equation>的导数可得<equation>f^{\prime}(z)=1+\frac{2}{z}>0.</equation>于是，函数<equation>f(z)=z+2\ln z-1</equation>单调增加，z=1是该方程的唯一实根.

将 x=0,y=2,z=1代入（1）式可得<equation>3\frac{\partial z}{\partial x}\bigg|_{(0,2)}=3.</equation>解得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,2)}=1.</equation>

---

**2020年第5题 | 选择题 | 4分 | 答案: B**
5. 关于函数<equation>f ( x, y )=\left\{\begin{array}{l l}x y,&x y\neq 0\\ x,&y=0\\ y,&x=0\end{array} \right.</equation>给出以下结论：<equation>\textcircled{1} \left. \frac{\partial f}{\partial x} \right|_{(0,0)}=1;</equation><equation>\textcircled{2} \left. \frac{\partial^{2} f}{\partial x \partial y} \right|_{(0,0)}=1;</equation><equation>\textcircled{3} \lim_{(x,y)\to(0,0)}f(x,y)=0;</equation><equation>\textcircled{4} \lim_{y\to0}\lim_{x\to0}f(x,y)=0</equation>其中正确的个数是（    ）

A.4 B.3 C.2 D.1
答案: B
**解析: **解 根据偏导数的定义，<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 0)} = \lim _ {x \rightarrow 0} \frac {f (x , 0) - f (0 , 0)}{x - 0} = \lim _ {x \rightarrow 0} \frac {x - 0}{x} = 1.</equation><equation>\textcircled{1}</equation>正确.

根据偏导数的定义，<equation>\left. \frac {\partial^ {2} f}{\partial x \partial y} \right| _ {(0, 0)} = \lim _ {y \rightarrow 0} \frac {\left. \frac {\partial f (x , y)}{\partial x} \right| _ {x = 0} - \left. \frac {\partial f (x , y)}{\partial x} \right| _ {x = 0}}{y - 0}.</equation>但是根据定义，当 y≠0时，<equation>\left. \frac {\partial f (x , y)}{\partial x} \right| _ {x = 0 \atop y \neq 0} = \lim _ {x \rightarrow 0} \frac {f (x , y) - f (0 , y)}{x - 0} = \lim _ {x \rightarrow 0} \frac {x y - y}{x} = \infty .</equation><equation>\frac{\partial f(x,y)}{\partial x}\bigg|_{x=0}</equation>不存在，<equation>\frac{\partial^{2}f}{\partial x\partial y}\bigg|_{(0,0)}</equation>当然也不存在.<equation>\textcircled{2}</equation>不正确.

根据 f(x,y）的定义，

- 当 xy≠0时，<equation>0\leqslant|f(x,y)-0|=|xy|\leqslant\frac{x^{2}+y^{2}}{2}<x^{2}+y^{2}</equation>，当 0 < x²+y² < 1时，<equation>x^{2}+y^{2}<\sqrt{x^{2}+y^{2}};</equation>- 当<equation>x = 0</equation>时，<equation>0\leqslant |f(x,y) - 0| = |y| \leqslant \sqrt{x^2 + y^2};</equation>- 当<equation>y = 0</equation>时，<equation>0\leqslant |f(x,y) - 0| = |x|\leqslant \sqrt{x^2 + y^2}.</equation>而<equation>\lim_{(x,y)\to (0,0)}\sqrt{x^2 + y^2} = 0</equation>，故<equation>\lim_{(x,y)\to (0,0)}f(x,y) = 0.</equation><equation>\textcircled{3}</equation>正确.

按照累次极限的顺序，先计算<equation>\lim_{x\to 0}f(x,y)</equation>，再计算<equation>\lim_{y\to 0}\lim_{x\to 0}f(x,y).</equation>根据累次极限的定义，只需考虑 x≠0，y≠0的情况.<equation>\lim _ {x \rightarrow 0} f (x, y) = \lim _ {x \rightarrow 0} x y = 0, \quad \lim _ {y \rightarrow 0} \lim _ {x \rightarrow 0} f (x, y) = \lim _ {y \rightarrow 0} 0 = 0.</equation><equation>\textcircled{4}</equation>正确.

因此，共有3个结论正确，应选B.

---

**2019年第11题 | 填空题 | 4分**
11. 设函数 f(u)可导，<equation>z=y f\left(\frac{y^{2}}{x}\right)</equation>，则<equation>2 x \frac{\partial z}{\partial x}+y \frac{\partial z}{\partial y}=</equation>___
**解析: **分别计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = y f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) \cdot \left(- \frac {y ^ {2}}{x ^ {2}}\right) = - \frac {y ^ {3}}{x ^ {2}} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right).</equation><equation>\frac {\partial z}{\partial y} = f \left(\frac {y ^ {2}}{x}\right) + y \cdot f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) \cdot \frac {2 y}{x} = f \left(\frac {y ^ {2}}{x}\right) + \frac {2 y ^ {2}}{x} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right).</equation>代入<equation>2 x \frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}</equation>可得，<equation>2 x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = - \frac {2 y ^ {3}}{x} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) + \frac {2 y ^ {3}}{x} f ^ {\prime} \left(\frac {y ^ {2}}{x}\right) + y f \left(\frac {y ^ {2}}{x}\right) = y f \left(\frac {y ^ {2}}{x}\right).</equation>

---

**2019年第20题 | 解答题 | 11分**
20. （本题满分11分）

已知函数 u(x,y)满足<equation>2\frac{\partial^{2} u}{\partial x^{2}}-2\frac{\partial^{2} u}{\partial y^{2}}+3\frac{\partial u}{\partial x}+3\frac{\partial u}{\partial y}=0</equation>，求 a,b的值，使得在变换<equation>u(x,y)=v(x,y)\mathrm{e}^{ax+by}</equation>下，上述等式可化为 v(x,y)不含一阶偏导数的等式.
**答案: **<equation>a = - \frac {3}{4}, b = \frac {3}{4}.</equation>
**解析: **由<equation>u ( x,y)=v ( x,y)\mathrm{e}^{a x+b y}</equation>可得，<equation>\frac {\partial u}{\partial x} = \frac {\partial v}{\partial x} \cdot \mathrm {e} ^ {a x + b y} + \mathrm {e} ^ {a x + b y} \cdot a v = \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial x} + a v\right).</equation><equation>\frac {\partial u}{\partial y} = \frac {\partial v}{\partial y} \cdot \mathrm {e} ^ {a x + b y} + \mathrm {e} ^ {a x + b y} \cdot b v = \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial y} + b v\right).</equation><equation>\frac {\partial^ {2} u}{\partial x ^ {2}} = a \cdot \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial x} + a v\right) + \mathrm {e} ^ {a x + b y} \left(\frac {\partial^ {2} v}{\partial x ^ {2}} + a \frac {\partial v}{\partial x}\right) = \mathrm {e} ^ {a x + b y} \left(2 a \frac {\partial v}{\partial x} + a ^ {2} v + \frac {\partial^ {2} v}{\partial x ^ {2}}\right).</equation><equation>\frac {\partial^ {2} u}{\partial y ^ {2}} = b \cdot \mathrm {e} ^ {a x + b y} \left(\frac {\partial v}{\partial y} + b v\right) + \mathrm {e} ^ {a x + b y} \left(\frac {\partial^ {2} v}{\partial y ^ {2}} + b \frac {\partial v}{\partial y}\right) = \mathrm {e} ^ {a x + b y} \left(2 b \frac {\partial v}{\partial y} + b ^ {2} v + \frac {\partial^ {2} v}{\partial y ^ {2}}\right).</equation>代入已知等式可得，<equation>\mathrm {e} ^ {a x + b y} \left[ 2 \left(2 a \frac {\partial v}{\partial x} + a ^ {2} v + \frac {\partial^ {2} v}{\partial x ^ {2}}\right) - 2 \left(2 b \frac {\partial v}{\partial y} + b ^ {2} v + \frac {\partial^ {2} v}{\partial y ^ {2}}\right) + 3 \left(\frac {\partial v}{\partial x} + a v\right) + 3 \left(\frac {\partial v}{\partial y} + b v\right) \right] = 0.</equation>整理上式，可得<equation>2 \frac {\partial^ {2} v}{\partial x ^ {2}} - 2 \frac {\partial^ {2} v}{\partial y ^ {2}} + (4 a + 3) \frac {\partial v}{\partial x} + (- 4 b + 3) \frac {\partial v}{\partial y} + \left(2 a ^ {2} v - 2 b ^ {2} v + 3 a v + 3 b v\right) = 0.</equation>要使得（1）式中不含有 v(x,y) 的一阶偏导数，需使<equation>4 a+3=0,-4 b+3=0</equation>.解得 a=-<equation>\frac{3}{4},</equation><equation>b=\frac{3}{4}.</equation>因此，<equation>a=-\frac{3}{4}, b=\frac{3}{4}.</equation>

---

**2018年第13题 | 填空题 | 4分**
13. 设函数<equation>z=z(x,y)</equation>由方程<equation>\ln z+\mathrm{e}^{z-1}=xy</equation>确定，则<equation>\left.\frac{\partial z}{\partial x}\right|_{(2,\frac{1}{2})}=</equation>___
**答案: **## 1 4.
**解析: **解（法一）对已知方程两端关于 x求导，可得<equation>\frac {1}{z} \cdot \frac {\partial z}{\partial x} + \mathrm {e} ^ {z - 1} \cdot \frac {\partial z}{\partial x} = y.</equation>将 x=2，<equation>y=\frac{1}{2}</equation>代入已知方程可得，<equation>\ln z+\mathrm{e}^{z-1}=1.</equation>解得 z=1.

将<equation>x = 2, y = \frac{1}{2}, z = 1</equation>代入（1）式可得，<equation>2\frac{\partial z}{\partial x}\bigg|_{(2,\frac{1}{2})} = \frac{1}{2}</equation>，即<equation>\frac{\partial z}{\partial x}\bigg|_{(2,\frac{1}{2})} = \frac{1}{4}</equation>.

（法二）记<equation>F ( x,y,z)=\ln z+\mathrm{e}^{z-1}-x y</equation>，则<equation>F_{x}^{\prime}(x,y,z)=-y,F_{z}^{\prime}(x,y,z)=\frac{1}{z}+\mathrm{e}^{z-1}.</equation>将 x=2，y<equation>=\frac{1}{2}</equation>代入已知方程可得，<equation>\ln z+\mathrm{e}^{z-1}=1.</equation>解得 z=1.

根据隐函数存在定理，<equation>\left. \frac {\partial z}{\partial x} \right| _ {\left(2, \frac {1}{2}\right)} = - \frac {F _ {x} ^ {\prime} \left(2 , \frac {1}{2} , 1\right)}{F _ {z} ^ {\prime} \left(2 , \frac {1}{2} , 1\right)} = - \frac {- \frac {1}{2}}{2} = \frac {1}{4}.</equation>

---

**2017年第5题 | 选择题 | 4分 | 答案: D**
5. 设 f(x,y)具有一阶偏导数，且对任意的(x,y)，都有<equation>\frac{\partial f(x,y)}{\partial x}>0,\frac{\partial f(x,y)}{\partial y}<0</equation>，则（    ）

A. f(0,0)>f(1,1) B. f(0,0)<f(1,1) C. f(0,1)>f(1,0) D. f(0,1)<f(1,0)
答案: D
**解析: **解固定变量 y=0，则 f(x,0)是关于 x的一元函数.由于<equation>\frac{\partial f(x,y)}{\partial x}>0</equation>，故 f(x,0)是关于 x的单调增加函数.于是，<equation>f (1, 0) - f (0, 0) > 0.</equation>固定变量 x=0，则 f（0,y）是关于 y的一元函数.由于<equation>\frac{\partial f(x,y)}{\partial y}<0</equation>，故 f（0,y）是关于 y的单调减少函数.于是，<equation>f (0, 1) - f (0, 0) < 0.</equation>因此，<equation>f ( 1, 0 ) > f ( 0, 0 ) > f ( 0, 1 )</equation>.应选D.

---

**2017年第16题 | 解答题 | 10分**
16. (本题满分10分）设函数<equation>f(u,v)</equation>具有2阶连续偏导数，<equation>y=f(\mathrm{e}^{x},\cos x)</equation>，求<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=0},\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}.</equation>
**答案: **<equation>\frac{\mathrm{d} y}{\mathrm{d} x}\bigg|_{x=0}=f_{1}^{\prime}(1,1),\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\bigg|_{x=0}=f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)-f_{2}^{\prime}(1,1).</equation>
**解析: **解分别记 f（u,v）关于第一个变量、第二个变量的偏导数为<equation>f_{1}^{\prime}, f_{2}^{\prime}. f_{1}^{\prime}, f_{2}^{\prime}</equation>具有与 f相同的复合结构.根据链式法则，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f _ {1} ^ {\prime} \frac {\mathrm {d} \left(\mathrm {e} ^ {x}\right)}{\mathrm {d} x} + f _ {2} ^ {\prime} \frac {\mathrm {d} (\cos x)}{\mathrm {d} x} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} - f _ {2} ^ {\prime} \sin x.</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) - 0 = f _ {1} ^ {\prime} (1, 1).</equation>对（1）式两端关于 x求导，得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} + \mathrm {e} ^ {x} \left(f _ {1 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {1 2} ^ {\prime \prime} \sin x\right) - f _ {2} ^ {\prime} \cos x - \sin x \left(f _ {2 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {2 2} ^ {\prime \prime} \sin x\right).</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) - f _ {2} ^ {\prime} (1, 1).</equation>

---

**2016年第6题 | 选择题 | 4分 | 答案: D**
6. 已知函数<equation>f(x,y)=\frac{\mathrm{e}^{x}}{x-y}</equation>，则（    ）

A.<equation>f_{x}^{\prime}-f_{y}^{\prime}=0</equation>B.<equation>f_{x}^{\prime}+f_{y}^{\prime}=0</equation>C.<equation>f_{x}^{\prime}-f_{y}^{\prime}=f</equation>D.<equation>f_{x}^{\prime}+f_{y}^{\prime}=f</equation>
答案: D
**解析: **分别计算<equation>f_{x}^{\prime}, f_{y}^{\prime}</equation>得<equation>f _ {x} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y) - \mathrm {e} ^ {x}}{(x - y) ^ {2}}, \quad f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x}}{(x - y) ^ {2}}.</equation>因此，<equation>f _ {x} ^ {\prime} + f _ {y} ^ {\prime} = \frac {\mathrm {e} ^ {x} (x - y)}{(x - y) ^ {2}} = \frac {\mathrm {e} ^ {x}}{x - y} = f.</equation>应选 D.

---

**2015年第5题 | 选择题 | 4分 | 答案: D**
5. 设函数 f（u,v）满足<equation>f \left( x+y, \frac{y}{x} \right)=x^{2}-y^{2}</equation>，则<equation>\left. \frac{\partial f}{\partial u} \right|_{u=1},\left. \frac{\partial f}{\partial v} \right|_{u=1}</equation>依次是（    )

A.<equation>\frac{1}{2},0</equation>B. 0,<equation>\frac{1}{2}</equation>C.<equation>-\frac{1}{2},0</equation>D. 0,<equation>-\frac{1}{2}</equation>
答案: D
**解析: **解（法一）由<equation>u=x+y,v=\frac{y}{x}</equation>解出x，y关于u，v的表达式，从而将<equation>f\left(x+y,\frac{y}{x}\right)</equation>写成关于 u,v的表达式，进而求得<equation>\frac{\partial f}{\partial u}\bigg|_{u=1}\,,\frac{\partial f}{\partial v}\bigg|_{u=1}.</equation>由<equation>\left\{\begin{array}{l l}u=x+y,\\ v=\frac{y}{x},\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}x=\frac{u}{1+v},\\ y=\frac{uv}{1+v},\end{array}\right.</equation>故<equation>f (u, v) = \left(\frac {u}{1 + v}\right) ^ {2} - \left(\frac {u v}{1 + v}\right) ^ {2} = \frac {u ^ {2} \left(1 - v ^ {2}\right)}{\left(1 + v\right) ^ {2}} = u ^ {2} \left(\frac {1 - v}{1 + v}\right) = u ^ {2} \left(\frac {2}{1 + v} - 1\right).</equation>因此，<equation>\left. \frac {\partial f}{\partial u} \right| _ {u = 1 \atop v = 1} = 2 u \left(\frac {2}{1 + v} - 1\right) \Bigg | _ {u = 1 \atop v = 1} = 0, \quad \left. \frac {\partial f}{\partial v} \right| _ {u = 1 \atop v = 1} = u ^ {2} \cdot \frac {- 2}{(1 + v) ^ {2}} \Bigg | _ {u = 1 \atop v = 1} = - \frac {1}{2}.</equation>应选 D.

（法二）一方面，<equation>\mathrm {d} f \left(x + y, \frac {y}{x}\right) = \frac {\partial \left(x ^ {2} - y ^ {2}\right)}{\partial x} \mathrm {d} x + \frac {\partial \left(x ^ {2} - y ^ {2}\right)}{\partial y} \mathrm {d} y = 2 x \mathrm {d} x - 2 y \mathrm {d} y;</equation>另一方面，<equation>\begin{aligned} \mathrm {d} f \left(x + y, \frac {y}{x}\right) \frac {u = x + y}{v = \frac {y}{x}} \frac {\partial f}{\partial u} \mathrm {d} u + \frac {\partial f}{\partial v} \mathrm {d} v &= \frac {\partial f}{\partial u} (\mathrm {d} x + \mathrm {d} y) + \frac {\partial f}{\partial v} \left(- \frac {y}{x ^ {2}} \mathrm {d} x + \frac {1}{x} \mathrm {d} y\right) \\ &= \left(\frac {\partial f}{\partial u} - \frac {y}{x ^ {2}} \frac {\partial f}{\partial v}\right) \mathrm {d} x + \left(\frac {\partial f}{\partial u} + \frac {1}{x} \frac {\partial f}{\partial v}\right) \mathrm {d} y. \end{aligned}</equation>比较 dx，dy的系数可得<equation>\left\{ \begin{array}{l} \frac {\partial f}{\partial u} - \frac {y}{x ^ {2}} \frac {\partial f}{\partial v} = 2 x, \\ \frac {\partial f}{\partial u} + \frac {1}{x} \frac {\partial f}{\partial v} = - 2 y. \end{array} \right.</equation>当 u=1，v=1时，由<equation>\left\{\begin{array}{l l}x+y=u,\\ \frac{y}{x}=v\end{array}\right.</equation>解得 x =<equation>\frac{1}{2}</equation>, y =<equation>\frac{1}{2}</equation>. 代入上面的方程组，可得<equation>\frac{\partial f}{\partial u}\bigg|_{u=1} = 0,</equation><equation>\frac{\partial f}{\partial v}\bigg|_{u=1} = -\frac{1}{2}</equation>. 应选D.

---

**2013年第5题 | 选择题 | 4分 | 答案: A**
5. 设<equation>z=\frac{y}{x} f(xy)</equation>，其中函数 f可微，则<equation>\frac{x}{y}\frac{\partial z}{\partial x}+\frac{\partial z}{\partial y}=(\quad)</equation>A.<equation>2 y f^{\prime}( x y )</equation>B.<equation>- 2 y f^{\prime}( x y )</equation>C.<equation>\frac{2}{x} f(x y)</equation>D.<equation>- \frac{2}{x} f(x y)</equation>
答案: A
**解析: **解（法一）用链式法则分别求<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}</equation><equation>\frac {\partial z}{\partial x} = - \frac {y}{x ^ {2}} f (x y) + \frac {y}{x} f ^ {\prime} (x y) \cdot y = - \frac {y}{x ^ {2}} f (x y) + \frac {y ^ {2}}{x} f ^ {\prime} (x y),</equation><equation>\frac {\partial z}{\partial y} = \frac {1}{x} f (x y) + \frac {y}{x} f ^ {\prime} (x y) \cdot x = \frac {1}{x} f (x y) + y f ^ {\prime} (x y).</equation>因此，<equation>\frac {x}{y} \frac {\partial z}{\partial x} + \frac {\partial z}{\partial y} = - \frac {1}{x} f (x y) + y f ^ {\prime} (x y) + \frac {1}{x} f (x y) + y f ^ {\prime} (x y) = 2 y f ^ {\prime} (x y).</equation>应选A.

（法二）利用全微分形式的不变性.<equation>\begin{aligned} \mathrm {d} z &= f (x y) \mathrm {d} \left(\frac {y}{x}\right) + \frac {y}{x} \mathrm {d} [ f (x y) ] \\ &= - \frac {y}{x ^ {2}} f (x y) \mathrm {d} x + \frac {1}{x} f (x y) \mathrm {d} y + \frac {y}{x} f ^ {\prime} (x y) \cdot y \mathrm {d} x + \frac {y}{x} f ^ {\prime} (x y) \cdot x \mathrm {d} y \\ &= \left[ \frac {y ^ {2}}{x} f ^ {\prime} (x y) - \frac {y}{x ^ {2}} f (x y) \right] \mathrm {d} x + \left[ y f ^ {\prime} (x y) + \frac {1}{x} f (x y) \right] \mathrm {d} y. \end{aligned}</equation>因此，<equation>\frac {\partial z}{\partial x} = - \frac {y}{x ^ {2}} f (x y) + \frac {y ^ {2}}{x} f ^ {\prime} (x y), \quad \frac {\partial z}{\partial y} = \frac {1}{x} f (x y) + y f ^ {\prime} (x y).</equation>其余同法一.

---

**2012年第5题 | 选择题 | 4分 | 答案: D**
5. 设函数 f(x,y)可微，且对任意的 x,y都有<equation>\frac{\partial f(x,y)}{\partial x}>0,\frac{\partial f(x,y)}{\partial y}<0</equation>，则使不等式<equation>f(x_{1},y_{1})<f(x_{2},y_{2})</equation>成立的一个充分条件是（    ）

A.<equation>x_{1}>x_{2},y_{1}<y_{2}</equation>B.<equation>x_{1}>x_{2},y_{1}>y_{2}</equation>C.<equation>x_{1}<x_{2},y_{1}<y_{2}</equation>D.<equation>x_{1}<x_{2},y_{1}>y_{2}</equation>
答案: D
**解析: **解 将<equation>f \left(x_{2}, y_{2}\right)-f \left(x_{1}, y_{1}\right)</equation>看作两部分的和，即<equation>f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) = f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {2}\right) + f \left(x _ {1}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right).</equation><equation>f ( x, y_{2} )</equation>为关于<equation>x</equation>的一元函数.由于<equation>\frac{\partial f(x,y)}{\partial x} > 0</equation>，故当<equation>x_{2} > x_{1}</equation>时，<equation>f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {2}\right) > 0.</equation><equation>f ( x_{1}, y )</equation>为关于y的一元函数.由于<equation>\frac{\partial f ( x,y)}{\partial y} < 0</equation>，故当<equation>y_{2} < y_{1}</equation>时，<equation>f \left(x _ {1}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) > 0.</equation>因此，当<equation>x_{1} < x_{2}, y_{1} > y_{2}</equation>时，<equation>f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) = f \left(x _ {2}, y _ {2}\right) - f \left(x _ {1}, y _ {2}\right) + f \left(x _ {1}, y _ {2}\right) - f \left(x _ {1}, y _ {1}\right) > 0.</equation>应选 D.

---

**2012年第11题 | 填空题 | 4分**
11. 设<equation>z=f\left(\ln x+\frac{1}{y}\right)</equation>，其中函数 f(u)可微，则<equation>x\frac{\partial z}{\partial x}+y^{2}\frac{\partial z}{\partial y}=</equation>___
**解析: **利用链式法则，<equation>\frac {\partial z}{\partial x} = f ^ {\prime} \left(\ln x + \frac {1}{y}\right) \cdot \frac {1}{x}, \quad \frac {\partial z}{\partial y} = f ^ {\prime} \left(\ln x + \frac {1}{y}\right) \cdot \left(- \frac {1}{y ^ {2}}\right).</equation>因此，<equation>x \frac {\partial z}{\partial x} + y ^ {2} \frac {\partial z}{\partial y} = f ^ {\prime} \left(\ln x + \frac {1}{y}\right) - f ^ {\prime} \left(\ln x + \frac {1}{y}\right) = 0.</equation>

---

**2011年第17题 | 解答题 | 10分**
17. (本题满分9分)

设函数 z = f(xy, yg(x))，其中函数 f具有二阶连续偏导数，函数 g(x)可导且在 x=1处取得极值 g(1)=1，求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{x=1}</equation>y=1.
**答案: **(17)<equation>f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)+f_{12}^{\prime\prime}(1,1).</equation>
**解析: **由链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial [ y g (x) ]}{\partial x} = y f _ {1} ^ {\prime} + y g ^ {\prime} (x) f _ {2} ^ {\prime}, \\ \frac {\partial^ {2} z}{\partial x \partial y} = \frac {\partial \left[ y \left(f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime}\right) \right]}{\partial y} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left\{f _ {1 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} + g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} \right\} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left[ x f _ {1 1} ^ {\prime \prime} + g (x) f _ {1 2} ^ {\prime \prime} + x g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} + g (x) g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \right]. \\ \end{array}</equation>由<equation>g ( x )</equation>可导且在<equation>x=1</equation>处取得极值<equation>g ( 1 )=1</equation>知，<equation>g^{\prime}(1)=0.</equation>将<equation>x=1, y=1, g ( 1 )=1,</equation><equation>g^{\prime}(1)=0</equation>代入<equation>\frac{\partial^{2} z}{\partial x \partial y}</equation>，得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {x = 1 \atop y = 1} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) + f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2010年第5题 | 选择题 | 4分 | 答案: B**
5. 设函数 z=z(x,y)由方程<equation>F\left( \frac{y}{x},\frac{z}{x} \right)=0</equation>确定，其中 F为可微函数，且<equation>F_{2}^{\prime}\neq0</equation>，则<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=</equation>(    )

A. x B. z C. -x D. -z
答案: B
**解析: **解对方程<equation>F\left(\frac{y}{x},\frac{z}{x}\right)=0</equation>两端同时关于 x，y求偏导数，可得<equation>- \frac {y}{x ^ {2}} F _ {1} ^ {\prime} + \left(- \frac {z}{x ^ {2}} + \frac {1}{x} \cdot \frac {\partial z}{\partial x}\right) F _ {2} ^ {\prime} = 0, \quad \frac {F _ {1} ^ {\prime}}{x} + \frac {F _ {2} ^ {\prime}}{x} \cdot \frac {\partial z}{\partial y} = 0.</equation>由上面两个方程解得，<equation>\frac {\partial z}{\partial x} = \frac {\frac {y}{x} F _ {1} ^ {\prime} + \frac {z}{x} F _ {2} ^ {\prime}}{F _ {2} ^ {\prime}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}}.</equation>因此，<equation>x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = \frac {y F _ {1} ^ {\prime} + z F _ {2} ^ {\prime} - y F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}} = z.</equation>应选B.

---

**2010年第19题 | 解答题 | 10分**
19. (本题满分11分)

设函数 u=f(x,y)具有二阶连续偏导数，且满足等式<equation>4\frac{\partial^{2} u}{\partial x^{2}}+1 2 \frac{\partial^{2} u}{\partial x \partial y}+5 \frac{\partial^{2} u}{\partial y^{2}}=0</equation>. 确定 a,b的值，使等式在变换<equation>\xi=x+a y,\eta=x+b y</equation>下简化为<equation>\frac{\partial^{2} u}{\partial\xi\partial\eta}=0.</equation>
**答案: **(19)<equation>\left\{ \begin{array}{l l} a = - 2, \\ b = - \frac {2}{5}, \end{array} \right. \text {或} \left\{ \begin{array}{l l} a = - \frac {2}{5}, \\ b = - 2. \end{array} \right.</equation>
**解析: **解 由<equation>\left\{\begin{array}{l l} {\xi=x+ay,} \\ {\eta=x+by,} \end{array} \right.</equation>得<equation>\left\{\begin{array}{l l} {x=\frac{a\eta-b\xi}{a-b},} \\ {y=\frac{\xi-\eta}{a-b}.} \end{array} \right.</equation>注意到<equation>u=f(x,y)</equation>具有二阶连续偏导数.由链式法则，当 a≠b时，<equation>u=f(x(\xi,\eta),y(\xi,\eta))</equation>仍具有关于<equation>\xi,\eta</equation>的二阶连续偏导数，从而<equation>\frac{\partial^{2} u}{\partial\xi\partial\eta}=\frac{\partial^{2} u}{\partial\eta\partial\xi}.</equation>由链式法则可得，<equation>\frac {\partial u}{\partial x} = \frac {\partial u}{\partial \xi} \frac {\partial \xi}{\partial x} + \frac {\partial u}{\partial \eta} \frac {\partial \eta}{\partial x} = \frac {\partial u}{\partial \xi} + \frac {\partial u}{\partial \eta},</equation><equation>\frac {\partial u}{\partial y} = \frac {\partial u}{\partial \xi} \frac {\partial \xi}{\partial y} + \frac {\partial u}{\partial \eta} \frac {\partial \eta}{\partial y} = a \frac {\partial u}{\partial \xi} + b \frac {\partial u}{\partial \eta},</equation><equation>\begin{aligned} \frac {\partial^ {2} u}{\partial x ^ {2}} &= \frac {\partial \left(\frac {\partial u}{\partial \xi} + \frac {\partial u}{\partial \eta}\right)}{\partial x} = \frac {\partial^ {2} u}{\partial \xi^ {2}} \frac {\partial \xi}{\partial x} + \frac {\partial^ {2} u}{\partial \xi \partial \eta} \frac {\partial \eta}{\partial x} + \frac {\partial^ {2} u}{\partial \eta \partial \xi} \frac {\partial \xi}{\partial x} + \frac {\partial^ {2} u}{\partial \eta^ {2}} \frac {\partial \eta}{\partial x} \\ &= \frac {\partial^ {2} u}{\partial \xi^ {2}} + 2 \frac {\partial^ {2} u}{\partial \xi \partial \eta} + \frac {\partial^ {2} u}{\partial \eta^ {2}}, \end{aligned}</equation><equation>\begin{aligned} \frac {\partial^ {2} u}{\partial x \partial y} &= \frac {\partial \left(\frac {\partial u}{\partial \xi} + \frac {\partial u}{\partial \eta}\right)}{\partial y} = \frac {\partial^ {2} u}{\partial \xi^ {2}} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \xi \partial \eta} \frac {\partial \eta}{\partial y} + \frac {\partial^ {2} u}{\partial \eta \partial \xi} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \eta^ {2}} \frac {\partial \eta}{\partial y} \\ &= a \frac {\partial^ {2} u}{\partial \xi^ {2}} + (a + b) \frac {\partial^ {2} u}{\partial \xi \partial \eta} + b \frac {\partial^ {2} u}{\partial \eta^ {2}}, \end{aligned}</equation><equation>\begin{aligned} \frac {\partial^ {2} u}{\partial y ^ {2}} &= \frac {\partial \left(a \frac {\partial u}{\partial \xi} + b \frac {\partial u}{\partial \eta}\right)}{\partial y} = a \left(\frac {\partial^ {2} u}{\partial \xi^ {2}} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \xi \partial \eta} \frac {\partial \eta}{\partial y}\right) + b \left(\frac {\partial^ {2} u}{\partial \eta \partial \xi} \frac {\partial \xi}{\partial y} + \frac {\partial^ {2} u}{\partial \eta^ {2}} \frac {\partial \eta}{\partial y}\right) \\ &= a ^ {2} \frac {\partial^ {2} u}{\partial \xi^ {2}} + 2 a b \frac {\partial^ {2} u}{\partial \xi \partial \eta} + b ^ {2} \frac {\partial^ {2} u}{\partial \eta^ {2}}. \end{aligned}</equation>代入<equation>4\frac{\partial^{2} u}{\partial x^{2}}+1 2\frac{\partial^{2} u}{\partial x \partial y}+5\frac{\partial^{2} u}{\partial y^{2}}=0</equation>，整理得<equation>\left(5 a ^ {2} + 1 2 a + 4\right) \frac {\partial^ {2} u}{\partial \xi^ {2}} + \left(5 b ^ {2} + 1 2 b + 4\right) \frac {\partial^ {2} u}{\partial \eta^ {2}} + \left[ 8 + 1 2 (a + b) + 1 0 a b \right] \frac {\partial^ {2} u}{\partial \xi \partial \eta} = 0.</equation>由上可得，<equation>\left\{ \begin{array}{l} 5 a ^ {2} + 1 2 a + 4 = 0, \\ 5 b ^ {2} + 1 2 b + 4 = 0, \\ 8 + 1 2 (a + b) + 1 0 a b \neq 0. \end{array} \right.</equation>解得<equation>\left\{ \begin{array}{l l} a = - 2, \\ b = - \frac {2}{5}, \end{array} \right. \quad \text {或} \quad \left\{ \begin{array}{l l} a = - \frac {2}{5}, \\ b = - 2. \end{array} \right.</equation>

---

**2009年第17题 | 解答题 | 10分**
17. (本题满分10分)

设<equation>z= f ( x+y, x-y, x y )</equation>，其中f具有二阶连续偏导数，求<equation>\mathrm{d} z</equation>与<equation>\frac{\partial^{2} z}{\partial x \partial y}.</equation>
**答案: **7)<equation>\mathrm{d} z=\left(f_{1}^{\prime}+f_{2}^{\prime}+y f_{3}^{\prime}\right) \mathrm{d} x+\left(f_{1}^{\prime}-f_{2}^{\prime}+x f_{3}^{\prime}\right) \mathrm{d} y,</equation><equation>\frac{\partial^{2} z}{\partial x \partial y}=f_{3}^{\prime}+f_{11}^{\prime \prime}+(x+y) f_{13}^{\prime \prime}-f_{22}^{\prime \prime}+(x-y) f_{23}^{\prime \prime}+xy f_{33}^{\prime \prime}.</equation>
**解析: **解 下面的<equation>f_{i}^{\prime}, f_{ij}^{\prime \prime}(i,j = 1,2,3)</equation>分别表示<equation>f_{i}^{\prime}(x + y,x - y,xy),f_{ij}^{\prime \prime}(x + y,x - y,</equation>（法一）将中间变量<equation>x + y,x - y,xy</equation>依次记为1，2，3号.利用链式法则，计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y},\frac{\partial^{2}z}{\partial x\partial y}</equation><equation>\frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x + y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial (x - y)}{\partial x} + f _ {3} ^ {\prime} \frac {\partial (x y)}{\partial x} = f _ {1} ^ {\prime} + f _ {2} ^ {\prime} + y f _ {3} ^ {\prime},</equation><equation>\frac {\partial z}{\partial y} = f _ {1} ^ {\prime} \frac {\partial (x + y)}{\partial y} + f _ {2} ^ {\prime} \frac {\partial (x - y)}{\partial y} + f _ {3} ^ {\prime} \frac {\partial (x y)}{\partial y} = f _ {1} ^ {\prime} - f _ {2} ^ {\prime} + x f _ {3} ^ {\prime}.</equation>因为<equation>\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y</equation>，所以<equation>\mathrm {d} z = \left(f _ {1} ^ {\prime} + f _ {2} ^ {\prime} + y f _ {3} ^ {\prime}\right) \mathrm {d} x + \left(f _ {1} ^ {\prime} - f _ {2} ^ {\prime} + x f _ {3} ^ {\prime}\right) \mathrm {d} y.</equation><equation>\begin{aligned} \frac {\partial^ {2} z}{\partial x \partial y} &= \frac {\partial \left(\frac {\partial z}{\partial x}\right)}{\partial y} = \frac {\partial f _ {1} ^ {\prime}}{\partial y} + \frac {\partial f _ {2} ^ {\prime}}{\partial y} + \frac {\partial \left(y f _ {3} ^ {\prime}\right)}{\partial y} \\ &= f _ {1 1} ^ {\prime \prime} \frac {\partial (x + y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial (x - y)}{\partial y} + f _ {1 3} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} \\ + f _ {2 1} ^ {\prime \prime} \frac {\partial (x + y)}{\partial y} + f _ {2 2} ^ {\prime \prime} \frac {\partial (x - y)}{\partial y} + f _ {2 3} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} \\ + y f _ {3 1} ^ {\prime \prime} \frac {\partial (x + y)}{\partial y} + y f _ {3 2} ^ {\prime \prime} \frac {\partial (x - y)}{\partial y} + y f _ {3 3} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {3} ^ {\prime} \\ &= f _ {1 1} ^ {\prime \prime} - f _ {1 2} ^ {\prime \prime} + x f _ {1 3} ^ {\prime \prime} + f _ {2 1} ^ {\prime \prime} - f _ {2 2} ^ {\prime \prime} + x f _ {2 3} ^ {\prime \prime} + y f _ {3 1} ^ {\prime \prime} - y f _ {3 2} ^ {\prime \prime} + x y f _ {3 3} ^ {\prime \prime} + f _ {3} ^ {\prime} \end{aligned}</equation>由于<equation>f</equation>的二阶偏导数连续，故<equation>f_{12}^{\prime \prime} = f_{21}^{\prime \prime}, f_{13}^{\prime \prime} = f_{31}^{\prime \prime}, f_{23}^{\prime \prime} = f_{32}^{\prime \prime}</equation>. 因此，<equation>\frac {\partial^ {2} z}{\partial x \partial y} = f _ {3} ^ {\prime} + f _ {1 1} ^ {\prime \prime} + (x + y) f _ {1 3} ^ {\prime \prime} - f _ {2 2} ^ {\prime \prime} + (x - y) f _ {2 3} ^ {\prime \prime} + x y f _ {3 3} ^ {\prime \prime}.</equation>（法二）利用全微分形式的不变性.

由于<equation>f</equation>具有二阶连续偏导数，故<equation>z,\frac{\partial z}{\partial x}</equation>均可微.<equation>\begin{aligned} \mathrm {d} z &= f _ {1} ^ {\prime} \mathrm {d} (x + y) + f _ {2} ^ {\prime} \mathrm {d} (x - y) + f _ {3} ^ {\prime} \mathrm {d} (x y) = f _ {1} ^ {\prime} \mathrm {d} x + f _ {1} ^ {\prime} \mathrm {d} y + f _ {2} ^ {\prime} \mathrm {d} x - f _ {2} ^ {\prime} \mathrm {d} y + y f _ {3} ^ {\prime} \mathrm {d} x + x f _ {3} ^ {\prime} \mathrm {d} y \\ &= \left(f _ {1} ^ {\prime} + f _ {2} ^ {\prime} + y f _ {3} ^ {\prime}\right) \mathrm {d} x + \left(f _ {1} ^ {\prime} - f _ {2} ^ {\prime} + x f _ {3} ^ {\prime}\right) \mathrm {d} y. \end{aligned}</equation>因此，<equation>\frac{\partial z}{\partial x} = f_1^{\prime} + f_2^{\prime} + yf_3^{\prime}</equation>.

继续对<equation>\frac{\partial z}{\partial x}</equation>微分，得<equation>\begin{aligned} \mathrm {d} \left(\frac {\partial z}{\partial x}\right) &= \mathrm {d} f _ {1} ^ {\prime} + \mathrm {d} f _ {2} ^ {\prime} + y \mathrm {d} f _ {3} ^ {\prime} + f _ {3} ^ {\prime} \mathrm {d} y \\ &= f _ {1 1} ^ {\prime \prime} \mathrm {d} (x + y) + f _ {1 2} ^ {\prime \prime} \mathrm {d} (x - y) + f _ {1 3} ^ {\prime \prime} \mathrm {d} (x y) \\ + f _ {2 1} ^ {\prime \prime} \mathrm {d} (x + y) + f _ {2 2} ^ {\prime \prime} \mathrm {d} (x - y) + f _ {2 3} ^ {\prime \prime} \mathrm {d} (x y) \\ + y f _ {3 1} ^ {\prime \prime} \mathrm {d} (x + y) + y f _ {3 2} ^ {\prime \prime} \mathrm {d} (x - y) + y f _ {3 3} ^ {\prime \prime} \mathrm {d} (x y) + f _ {3} ^ {\prime} \mathrm {d} y. \end{aligned}</equation>其中，<equation>\mathrm {d} y \text {的系 数} ^ {\prime} = f _ {1 1} ^ {\prime \prime} - f _ {1 2} ^ {\prime \prime} + x f _ {1 3} ^ {\prime \prime} + f _ {2 1} ^ {\prime \prime} - f _ {2 2} ^ {\prime \prime} + x f _ {2 3} ^ {\prime \prime} + y f _ {3 1} ^ {\prime \prime} - y f _ {3 2} ^ {\prime \prime} + x y f _ {3 3} ^ {\prime \prime} + f _ {3} ^ {\prime}.</equation>其余同法一.

---


#### 二次积分与变换积分次序

**2025年第5题 | 选择题 | 5分 | 答案: A**

5. 设函数 f(x,y) 连续，则<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y=</equation>(    )

A.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>B.<equation>\int_{0}^{4}\left[\int_{-2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>C.<equation>\int_{0}^{4}\left[\int_{-2}^{-\sqrt{4-y}}f(x,y)\mathrm{d}x+\int_{2}^{\sqrt{4-y}}f(x,y)\mathrm{d}x\right]\mathrm{d}y</equation>D.<equation>2\int_{0}^{4}\mathrm{d}y\int_{\sqrt{4-y}}^{2}f(x,y)\mathrm{d}x</equation>

答案: A

**解析:**解如图所示，二次积分<equation>\int_{-2}^{2}\mathrm{d}x\int_{4-x^{2}}^{4}f(x,y)\mathrm{d}y</equation>对应的二重积分的积分区域 D为图中灰色区域.<equation>D = \left\{(x, y) \mid 4 - x ^ {2} \leqslant y \leqslant 4, - 2 \leqslant x \leqslant 2 \right\}.</equation>当 x < 0时，解<equation>y=4-x^{2}</equation>可得<equation>x=-\sqrt{4-y}</equation>当 x > 0时，解<equation>y=4-x^{2}</equation>可得<equation>x=\sqrt{4-y}</equation>于是，将D写成Y型区域需要将其分块，<equation>D = \left\{(x, y) \mid - 2 \leqslant x \leqslant - \sqrt {4 - y}, 0 \leqslant y \leqslant 4 \right\} \cup \left\{(x, y) \mid \sqrt {4 - y} \leqslant x \leqslant 2, 0 \leqslant y \leqslant 4 \right\}.</equation>从而，<equation>\int_ {- 2} ^ {2} \mathrm {d} x \int_ {4 - x ^ {2}} ^ {4} f (x, y) \mathrm {d} y = \iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {4} \left[ \int_ {- 2} ^ {- \sqrt {4 - y}} f (x, y) \mathrm {d} x + \int_ {\sqrt {4 - y}} ^ {2} f (x, y) \mathrm {d} x \right] \mathrm {d} y.</equation>选项A正确，选项B、C不正确.

对选项D，该选项正确意味着<equation>\iint \limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y=2\iint \limits_{D_{1}} f(x,y)\mathrm{d}x\mathrm{d}y</equation>，其中<equation>D_{1}</equation>为D位于y轴右边的部分，而该式成立需要<equation>f(x,y)</equation>是关于x的偶函数，但题干条件中并没有这一信息，故该选项不正确。例如，取<equation>f(x,y)=x</equation>，则<equation>\iint \limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y=0</equation>，而<equation>\iint \limits_{D_{1}} f(x,y)\mathrm{d}x\mathrm{d}y>0.</equation>因此，应选A.

---

**2024年第6题 | 选择题 | 5分 | 答案: A**

6. 设 f(x,y)是连续函数，则<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y=</equation>(    )

A.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>B.<equation>\int_{\frac{1}{2}}^{1} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>C.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\frac{\pi}{6}}^{\arcsin y} f(x,y) \mathrm{d} x</equation>D.<equation>\int_{0}^{\frac{1}{2}} \mathrm{d} y \int_{\arcsin y}^{\frac{\pi}{2}} f(x,y) \mathrm{d} x</equation>

答案: A

**解析:**解二次积分<equation>\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \mathrm{d} x \int_{\sin x}^{1} f(x,y) \mathrm{d} y</equation>对应的二重积分的积分区域为<equation>D=\left\{(x,y)\mid \sin x\leqslant y\leqslant 1,\frac{\pi}{6}\leqslant x\leqslant \frac{\pi}{2}\right\}</equation>由于<equation>\arcsin y</equation>的值域为<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，而<equation>\left[\frac{\pi}{6},\frac{\pi}{2}\right]\subset\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>，故曲线<equation>y=\sin x\left(x\in\left[\frac{\pi}{6},\frac{\pi}{2}\right]\right)</equation>上的点（x,y）可写为（<equation>\arcsin y,y).</equation>由此可将 D改写成Y型区域，<equation>D = \left\{(x, y) \mid \frac {\pi}{6} \leqslant x \leqslant \arcsin y, \frac {1}{2} \leqslant y \leqslant 1 \right\}.</equation>因此，<equation>\int_ {\frac {\pi}{6}} ^ {\frac {\pi}{2}} \mathrm {d} x \int_ {\sin x} ^ {1} f (x, y) \mathrm {d} y = \int_ {\frac {1}{2}} ^ {1} \mathrm {d} y \int_ {\frac {\pi}{6}} ^ {\arcsin y} f (x, y) \mathrm {d} x.</equation>应选A.

---

**2022年第2题 | 选择题 | 5分 | 答案: D**

2.<equation>\int_{0}^{2}\mathrm{d}y\int_{y}^{2}\frac{y}{\sqrt{1+x^{3}}}\mathrm{d}x=</equation>(    )

A.<equation>\frac{\sqrt{2}}{6}</equation>B.<equation>\frac{1}{3}</equation>C.<equation>\frac{\sqrt{2}}{3}</equation>D.<equation>\frac{2}{3}</equation>

答案: D

**解析:**解如图（a）所示，二次积分对应的积分区域 D是由直线 y=x,x=2以及 x轴所围成的三角形区域. 原二次积分采用的是先 x，后 y的积分次序，改写成先 y，后 x的积分次序，即将 D写成 X型区域，如图（b）所示.<equation>D = \{(x, y) \mid 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 2 \}.</equation>(a)

(b)

因此，<equation>\begin{aligned} \text {原 积 分} &= \iint_ {D} \frac {y}{\sqrt {1 + x ^ {3}}} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \frac {1}{\sqrt {1 + x ^ {3}}} \mathrm {d} x \int_ {0} ^ {x} y \mathrm {d} y = \frac {1}{2} \int_ {0} ^ {2} \frac {x ^ {2}}{\sqrt {1 + x ^ {3}}} \mathrm {d} x \\ &= \frac {1}{6} \int_ {0} ^ {2} \frac {\mathrm {d} \left(1 + x ^ {3}\right)}{\sqrt {1 + x ^ {3}}} = \frac {1}{6} \cdot 2 \sqrt {1 + x ^ {3}} \Bigg | _ {0} ^ {2} = \frac {1}{3} \times (3 - 1) = \frac {2}{3}. \end{aligned}</equation>应选 D.

---

**2021年第14题 | 填空题 | 5分**

14. 已知函数<equation>f ( t )=\int_{1}^{t^{2}} \mathrm{d} x \int_{\sqrt{x}}^{t} \sin \frac{x}{y} \mathrm{d} y</equation>，则<equation>f^{\prime}\left(\frac{\pi}{2}\right)=</equation>___

**答案:**##<equation>\frac{\pi}{2} \cos \frac{2}{\pi}.</equation>

**解析:**解 根据二次积分的积分限，可得积分<equation>\int_{1}^{t^{2}}\mathrm{d}x\int_{\sqrt{x}}^{t}\sin \frac{x}{y}\mathrm{d}y</equation>对应的积分区域的边界为<equation>y=\sqrt{x},</equation><equation>y = t, x = 1, x = t ^ {2}.</equation>二次积分对应的积分区域 D为图中阴影部分，写成X型区域为<equation>D = \left\{(x, y) \mid \sqrt {x} \leqslant y \leqslant t, 1 \leqslant x \leqslant t ^ {2} \right\}.</equation>交换积分次序，将 D写成 Y型区域，可得<equation>D = \left\{(x, y) \mid 1 \leqslant x \leqslant y ^ {2}, 1 \leqslant y \leqslant t \right\}.</equation>因此，<equation>\begin{aligned} f (t) &= \int_ {1} ^ {t ^ {2}} \mathrm {d} x \int_ {\sqrt {x}} ^ {t} \sin \frac {x}{y} \mathrm {d} y = \int_ {1} ^ {t} \mathrm {d} y \int_ {1} ^ {y ^ {2}} \sin \frac {x}{y} \mathrm {d} x = \int_ {1} ^ {t} y \cdot \left(- \cos \frac {x}{y}\right) \Bigg | _ {1} ^ {y ^ {2}} \mathrm {d} y \\ &= \int_ {1} ^ {t} \left(- y \cos y + y \cos \frac {1}{y}\right) \mathrm {d} y. \end{aligned}</equation>根据变限积分的求导公式，<equation>f ^ {\prime} (t) = \left[ \int_ {1} ^ {t} \left(- y \cos y + y \cos \frac {1}{y}\right) \mathrm {d} y \right] ^ {\prime} = - t \cos t + t \cos \frac {1}{t}.</equation>代入<equation>t = \frac{\pi}{2}</equation>，可得<equation>f^{\prime}\left(\frac{\pi}{2}\right) = \frac{\pi}{2}\cos \frac{2}{\pi}</equation>

---

**2020年第10题 | 填空题 | 4分**

<equation>1 0. \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {y}} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\frac {2}{9} (2 \sqrt {2} - 1).</equation>

**解析:**解 由二次积分的积分限，可写出其对应的二重积分的积分区域的边界曲线：<equation>x=\sqrt{y}, x=1,</equation><equation>y=0, y=1.</equation>由这四条边界围成的区域 D如图（a）所示.<equation>D = \left\{(x, y) \mid \sqrt {y} \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1 \right\}.</equation>如图（b）所示，将 D写成 X型区域的形式，可得<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x ^ {2}, 0 \leqslant x \leqslant 1 \right\}.</equation>(a)

(b)

由此可得，<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {\sqrt {y}} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} x &= \int_ {0} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} x \int_ {0} ^ {x ^ {2}} \mathrm {d} y = \frac {1}{3} \int_ {0} ^ {1} \sqrt {x ^ {3} + 1} \mathrm {d} \left(x ^ {3} + 1\right) \\ &= \frac {1}{3} \cdot \frac {2}{3} \left(x ^ {3} + 1\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {2}{9} \left(2 \sqrt {2} - 1\right). \end{aligned}</equation>

---

**2018年第6题 | 选择题 | 4分 | 答案: C**

6.<equation>\int_{-1}^{0}\mathrm{d}x\int_{-x}^{2-x^{2}}(1-xy)\mathrm{d}y+\int_{0}^{1}\mathrm{d}x\int_{x}^{2-x^{2}}(1-xy)\mathrm{d}y=</equation>(    )

A.<equation>\frac{5}{3}</equation>B.<equation>\frac{5}{6}</equation>C.<equation>\frac{7}{3}</equation>D.<equation>\frac{7}{6}</equation>

答案: C

**解析:**解 记<equation>D _ {1} = \left\{(x, y) \mid - x \leqslant y \leqslant 2 - x ^ {2}, - 1 \leqslant x \leqslant 0 \right\},</equation><equation>D _ {2} = \left\{(x, y) \mid x \leqslant y \leqslant 2 - x ^ {2}, 0 \leqslant x \leqslant 1 \right\},</equation>则<equation>\int_ {- 1} ^ {0} \mathrm {d} x \int_ {- x} ^ {2 - x ^ {2}} (1 - x y) \mathrm {d} y = \iint_ {D _ {1}} (1 - x y) \mathrm {d} x \mathrm {d} y, \quad \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {2 - x ^ {2}} (1 - x y) \mathrm {d} y = \iint_ {D _ {2}} (1 - x y) \mathrm {d} x \mathrm {d} y.</equation>记<equation>D=D_{1}\cup D_{2}</equation>.如图所示，D为由抛物线<equation>y=2-x^{2}</equation>，直线 y=x以及直线 y=-x所围成的阴影区域.所求积分<equation>=\iint_{D}(1-xy)\mathrm{d}x\mathrm{d}y.</equation>由于区域 D关于 y轴对称，而 xy为关于 x的奇函数，1为关于 x的偶函数，故<equation>\begin{aligned} \iint_ {D} (1 - x y) \mathrm {d} x \mathrm {d} y \xlongequal {\iint_ {D} x y \mathrm {d} x \mathrm {d} y = 0} 2 \iint_ {D _ {2}} \mathrm {d} x \mathrm {d} y &= 2 \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {2 - x ^ {2}} \mathrm {d} y = 2 \int_ {0} ^ {1} \left(2 - x ^ {2} - x\right) \mathrm {d} x \\ &= 2 \cdot \left(2 x - \frac {x ^ {3}}{3} - \frac {x ^ {2}}{2}\right) \Big | _ {0} ^ {1} = 2 \times \frac {7}{6} = \frac {7}{3}. \end{aligned}</equation>因此，应选C.

---

**2017年第13题 | 填空题 | 4分**

<equation>\int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\tan x}{x} \mathrm {d} x = \underline {{}}</equation>

**解析:**原二次积分对应的二重积分的积分区域 D为 Y型区域，<equation>D = \left\{(x, y) \mid y \leqslant x \leqslant 1, 0 \leqslant y \leqslant 1 \right\}.</equation>如图所示，将区域 D写成 X型区域，可得<equation>D = \left\{(x, y) \mid 0 \leqslant y \leqslant x, 0 \leqslant x \leqslant 1 \right\}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {1} \mathrm {d} y \int_ {y} ^ {1} \frac {\tan x}{x} \mathrm {d} x &= \int_ {0} ^ {1} \mathrm {d} x \int_ {0} ^ {x} \frac {\tan x}{x} \mathrm {d} y = \int_ {0} ^ {1} \tan x \mathrm {d} x = \int_ {0} ^ {1} \frac {\sin x}{\cos x} \mathrm {d} x = \int_ {0} ^ {1} \frac {- \mathrm {d} (\cos x)}{\cos x} \\ &= - \ln (\cos x) \Bigg | _ {0} ^ {1} = - \ln (\cos 1). \end{aligned}</equation>

---

**2015年第6题 | 选择题 | 4分 | 答案: B**

6. 设 D是第一象限中由曲线<equation>2 x y=1, 4 x y=1</equation>与直线<equation>y=x,y=\sqrt{3} x</equation>围成的平面区域，函数 f(x,y)在 D上连续，则<equation>\iint\limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y=</equation>(    )

A.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{2\sin 2\theta}}^{\frac{1}{\sin 2\theta}} f(r\cos \theta,r\sin \theta) r\mathrm{d}r</equation>B.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{\sqrt{2}\sin 2\theta}}^{\frac{1}{\sqrt{\sin 2\theta}}} f(r\cos \theta,r\sin \theta) r\mathrm{d}r</equation>C.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{2\sin 2\theta}}^{\frac{1}{\sin 2\theta}} f(r\cos \theta,r\sin \theta) \mathrm{d}r</equation>D.<equation>\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \mathrm{d}\theta \int_{\frac{1}{\sqrt{2}\sin 2\theta}}^{\frac{1}{\sqrt{\sin 2\theta}}} f(r\cos \theta,r\sin \theta) \mathrm{d}r</equation>

答案: B

**解析:**将曲线 2xy=1，4xy=1，直线 y=x，<equation>y=\sqrt{3}x</equation>改写为极坐标形式. 积分区域如图所示.<equation>2 x y = 1 \Rightarrow r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {\sin 2 \theta}},</equation><equation>4 x y = 1 \Rightarrow 2 r ^ {2} \sin 2 \theta = 1 \Rightarrow r = \frac {1}{\sqrt {2 \sin 2 \theta}},</equation><equation>y = x \Rightarrow \theta = \frac {\pi}{4},</equation><equation>y = \sqrt {3} x \Rightarrow \theta = \frac {\pi}{3},</equation><equation>\mathrm {d} x \mathrm {d} y = r \mathrm {d} r \mathrm {d} \theta .</equation>于是，积分区域<equation>D</equation>在极坐标系下表示为<equation>D = \left\{(r, \theta) \mid \frac {1}{\sqrt {2 \sin 2 \theta}} \leqslant r \leqslant \frac {1}{\sqrt {\sin 2 \theta}}, \frac {\pi}{4} \leqslant \theta \leqslant \frac {\pi}{3} \right\}.</equation>因此，<equation>\iint_ {D} f (x, y) \mathrm {d} x \mathrm {d} y = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{3}} \mathrm {d} \theta \int_ {\frac {1}{\sqrt {2 \sin 2 \theta}}} ^ {\frac {1}{\sqrt {\sin 2 \theta}}} f (r \cos \theta , r \sin \theta) r \mathrm {d} r.</equation>应选B.

---

**2009年第4题 | 选择题 | 4分 | 答案: C**

4. 设函数 f(x,y) 连续，则<equation>\int_{1}^{2}\mathrm{d}x\int_{x}^{2}f(x,y)\mathrm{d}y+\int_{1}^{2}\mathrm{d}y\int_{y}^{4-y}f(x,y)\mathrm{d}x=</equation>(    )

A.<equation>\int_{1}^{2}\mathrm{d}x\int_{1}^{4-x}f(x,y)\mathrm{d}y</equation>B.<equation>\int_{1}^{2}\mathrm{d}x\int_{x}^{4-x}f(x,y)\mathrm{d}y</equation>C.<equation>\int_{1}^{2}\mathrm{d}y\int_{1}^{4-y}f(x,y)\mathrm{d}x</equation>D.<equation>\int_{1}^{2}\mathrm{d}y\int_{y}^{2}f(x,y)\mathrm{d}x</equation>

答案: C

**解析:**解<equation>\int_{1}^{2}\mathrm{d}x\int_{x}^{2}f(x,y)\mathrm{d}y</equation>对应的积分区域为<equation>D _ {1} = \left\{(x, y) \mid x \leqslant y \leqslant 2, 1 \leqslant x \leqslant 2 \right\}</equation>如图所示，<equation>D_{1}</equation>为由直线<equation>x = 1, y = 2</equation>以及<equation>x = y</equation>围成的三角形.<equation>\int_{1}^{2}\mathrm{d}y\int_{y}^{4-y}f(x,y)\mathrm{d}x</equation>对应的积分区域为<equation>D _ {2} = \left\{(x, y) \mid y \leqslant x \leqslant 4 - y, 1 \leqslant y \leqslant 2 \right\}</equation>如图所示，<equation>D_{2}</equation>为由直线<equation>y=x,x+y=4</equation>以及<equation>y=1</equation>围成的三角形

由图可知，<equation>D _ {1} \cup D _ {2} = D = \left\{(x, y) \mid 1 \leqslant x \leqslant 4 - y, 1 \leqslant y \leqslant 2 \right\}</equation>因此，原积分可写为<equation>\int_{1}^{2}\mathrm{d}y\int_{1}^{4-y}f(x,y)\mathrm{d}x.</equation>应选C.

---

