#### 偏导数的概念与计算

**2024年第12题 | 填空题 | 5分**
12. 设函数 f(u,v)具有2阶连续偏导数，且<equation>\mathrm{d} f|_{(1,1)}=3 \mathrm{d} u+4 \mathrm{d} v</equation>. 令 y=f（<equation>\cos x,1+x^{2}</equation>），则<equation>\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}=</equation>___.
**答案: **```latex
5
```

**解析:**解 由全微分的定义以及<equation>\mathrm{d}f|_{(1,1)}=3\mathrm{d}u+4\mathrm{d}v</equation>可知，<equation>f_{1}^{\prime}(1,1)=3,f_{2}^{\prime}(1,1)=4.</equation>根据链式法则，<equation>\begin{aligned} \frac {\mathrm {d} y}{\mathrm {d} x} &= f _ {1} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot (- \sin x) + f _ {2} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot 2 x, \\ \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} &= f _ {1 1} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot (- \sin x) ^ {2} + f _ {1 2} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot 2 x \cdot (- \sin x) \\ + f _ {1} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot (- \cos x) + f _ {2 1} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot 2 x \cdot (- \sin x) + f _ {2 2} ^ {\prime \prime} (\cos x, 1 + x ^ {2}) \cdot (2 x) ^ {2} \\ + f _ {2} ^ {\prime} (\cos x, 1 + x ^ {2}) \cdot 2. \end{aligned}</equation>将<equation>x=0</equation>代入<equation>\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}</equation>的表达式可得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = - f _ {1} ^ {\prime} (1, 1) + 2 f _ {2} ^ {\prime} (1, 1) = - 3 + 2 \times 4 = 5.</equation>

---

**2022年第2题 | 选择题 | 5分 | 答案: B**

2. 设函数<equation>z=xyf\left(\frac{y}{x}\right)</equation>，其中 f(u)可导，若<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=y^{2}(\ln y-\ln x)</equation>，则（    )

A.<equation>f(1)=\frac{1}{2},f^{\prime}(1)=0</equation>B.<equation>f(1)=0,f^{\prime}(1)=\frac{1}{2}</equation>C.<equation>f(1)=\frac{1}{2},f^{\prime}(1)=1</equation>D.<equation>f(1)=0,f^{\prime}(1)=1</equation>

答案: B

**解析:**解分别求<equation>\frac{\partial z}{\partial x}</equation>和<equation>\frac{\partial z}{\partial y}</equation>利用链式法则，<equation>\frac {\partial z}{\partial x} = y f \left(\frac {y}{x}\right) + x y f ^ {\prime} \left(\frac {y}{x}\right) \cdot \left(- \frac {y}{x ^ {2}}\right) = y f \left(\frac {y}{x}\right) - \frac {y ^ {2}}{x} f ^ {\prime} \left(\frac {y}{x}\right),</equation><equation>\frac {\partial z}{\partial y} = x f \left(\frac {y}{x}\right) + x y f ^ {\prime} \left(\frac {y}{x}\right) \cdot \frac {1}{x} = x f \left(\frac {y}{x}\right) + y f ^ {\prime} \left(\frac {y}{x}\right).</equation>于是，<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=2xyf\left(\frac{y}{x}\right).</equation>与<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=y^{2}(\ln y-\ln x)=y^{2}\ln \frac{y}{x}</equation>比较可得，<equation>f\left(\frac{y}{x}\right)=\frac{y}{2x}\ln \frac{y}{x}.</equation>从而，<equation>f(u)=\frac{1}{2} u \ln u,</equation><equation>f^{\prime}(u)=\frac{1}{2}(\ln u+1).</equation>因此，<equation>f ( 1 ) = 0</equation><equation>f^{\prime}(1)=\frac{1}{2}</equation>应选B.

---

**2020年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x,y)=\int_{0}^{xy}\mathrm{e}^{xt^{2}}\mathrm{d}t</equation>，则<equation>\left.\frac{\partial^{2}f}{\partial x\partial y}\right|_{(1,1)}=</equation>___

**答案:**## 4e.

**解析:**解（法一）注意到 f(x,y)的二阶偏导数连续，故可以交换求导次序.先对 y求偏导，再对 x求偏导.

根据变限积分求导公式，<equation>\frac {\partial f}{\partial y} = \mathrm {e} ^ {x (x y) ^ {2}} \cdot x = x \mathrm {e} ^ {x ^ {3} y ^ {2}},</equation><equation>\frac {\partial^ {2} f}{\partial y \partial x} = \mathrm {e} ^ {x ^ {3} y ^ {2}} + x \cdot \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot 3 x ^ {2} y ^ {2} = \left(3 x ^ {3} y ^ {2} + 1\right) \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation>代入<equation>x = 1,y = 1</equation>，可得<equation>\frac{\partial^2f}{\partial x\partial y}\bigg|_{(1,1)} = \frac{\partial^2f}{\partial y\partial x}\bigg|_{(1,1)} = 4\mathrm{e}.</equation>（法二）若直接对<equation>x</equation>求偏导，则需先对变限积分换元，将<equation>x</equation>移出积分号.令<equation>\sqrt{x} t = u</equation>，则<equation>\mathrm{d}t = \frac{\mathrm{d}u}{\sqrt{x}}.</equation><equation>\int_ {0} ^ {x y} \mathrm {e} ^ {x t ^ {2}} \mathrm {d} t \xlongequal {\sqrt {x} t = u} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \frac {\mathrm {e} ^ {u ^ {2}}}{\sqrt {x}} \mathrm {d} u = \frac {1}{\sqrt {x}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t.</equation>依次计算<equation>\frac{\partial f}{\partial x}, \frac{\partial^2 f}{\partial x \partial y}</equation>.<equation>\frac {\partial f}{\partial x} = - \frac {1}{2} x ^ {- \frac {3}{2}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t + \frac {1}{\sqrt {x}} \cdot \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot \frac {3}{2} \sqrt {x} y = - \frac {1}{2} x ^ {- \frac {3}{2}} \int_ {0} ^ {x ^ {\frac {3}{2}} y} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t + \frac {3}{2} y \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation><equation>\frac {\partial^ {2} f}{\partial x \partial y} = - \frac {1}{2} x ^ {- \frac {3}{2}} \mathrm {e} ^ {x ^ {3} y ^ {2}} \cdot x ^ {\frac {3}{2}} + \frac {3}{2} \mathrm {e} ^ {x ^ {3} y ^ {2}} + 3 x ^ {3} y ^ {2} \mathrm {e} ^ {x ^ {3} y ^ {2}} = \left(3 x ^ {3} y ^ {2} + 1\right) \mathrm {e} ^ {x ^ {3} y ^ {2}}.</equation>代入<equation>x = 1,y = 1</equation>，可得<equation>\frac{\partial^2f}{\partial x\partial y}\bigg|_{(1,1)} = 4\mathrm{e}.</equation>

---

**2019年第9题 | 填空题 | 4分**

9. 设函数 f(u)可导，<equation>z=f(\sin y-\sin x)+xy</equation>，则

**答案:**<equation>\frac {y}{\cos x} + \frac {x}{\cos y}.</equation>

**解析:**解分别计算<equation>\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}.</equation><equation>\frac {\partial z}{\partial x} = f ^ {\prime} (\sin y - \sin x) \cdot (- \cos x) + y, \quad \frac {\partial z}{\partial y} = f ^ {\prime} (\sin y - \sin x) \cdot \cos y + x.</equation>代入<equation>\frac{1}{\cos x}\cdot \frac{\partial z}{\partial x} +\frac{1}{\cos y}\cdot \frac{\partial z}{\partial y}</equation>可得，<equation>\begin{aligned} \frac {1}{\cos x} \cdot \frac {\partial z}{\partial x} + \frac {1}{\cos y} \cdot \frac {\partial z}{\partial y} &= - f ^ {\prime} (\sin y - \sin x) + \frac {y}{\cos x} + f ^ {\prime} (\sin y - \sin x) + \frac {x}{\cos y} \\ &= \frac {y}{\cos x} + \frac {x}{\cos y}. \end{aligned}</equation>

---

**2017年第15题 | 解答题 | 10分**

15. (本题满分10分）

设函数<equation>f ( u,v )</equation>具有2阶连续偏导数，<equation>y=f(\mathrm{e}^{x},\cos x)</equation>，求<equation>\left.\frac{\mathrm{d} y}{\mathrm{d} x}\right|_{x=0},\left.\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\right|_{x=0}.</equation>

**答案:**<equation>\frac{\mathrm{d} y}{\mathrm{d} x}\bigg|_{x=0}=f_{1}^{\prime}(1,1),\frac{\mathrm{d}^{2} y}{\mathrm{d} x^{2}}\bigg|_{x=0}=f_{1}^{\prime}(1,1)+f_{11}^{\prime\prime}(1,1)-f_{2}^{\prime}(1,1).</equation>

**解析:**解分别记 f（u,v）关于第一个变量、第二个变量的偏导数为<equation>f_{1}^{\prime}, f_{2}^{\prime}. f_{1}^{\prime}, f_{2}^{\prime}</equation>具有与f相同的复合结构根据链式法则，<equation>\frac {\mathrm {d} y}{\mathrm {d} x} = f _ {1} ^ {\prime} \frac {\mathrm {d} \left(\mathrm {e} ^ {x}\right)}{\mathrm {d} x} + f _ {2} ^ {\prime} \frac {\mathrm {d} (\cos x)}{\mathrm {d} x} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} - f _ {2} ^ {\prime} \sin x.</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} y}{\mathrm {d} x} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) - 0 = f _ {1} ^ {\prime} (1, 1).</equation>对（1）式两端关于 x求导，得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} = f _ {1} ^ {\prime} \mathrm {e} ^ {x} + \mathrm {e} ^ {x} \left(f _ {1 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {1 2} ^ {\prime \prime} \sin x\right) - f _ {2} ^ {\prime} \cos x - \sin x \left(f _ {2 1} ^ {\prime \prime} \mathrm {e} ^ {x} - f _ {2 2} ^ {\prime \prime} \sin x\right).</equation>代入 x=0，得<equation>\left. \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \right| _ {x = 0} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) - f _ {2} ^ {\prime} (1, 1).</equation>

---

**2011年第11题 | 填空题 | 4分**

11. 设函数 F(x,y)<equation>= \int_{0}^{x y}\frac{\sin t}{1+t^{2}}\mathrm{d}t</equation>，则<equation>\left.\frac{\partial^{2}F}{\partial x^{2}}\right|_{x=0,y=2}</equation> =___

**解析:**因此，<equation>\frac{\partial^{2}F}{\partial x^{2}}\bigg|_{x=0 \atop y=2}=4.</equation>解（法一）令<equation>f ( u )=\int_{0}^{u} \frac{\sin t}{1+t^{2}} \mathrm{d} t</equation>，则<equation>f^{\prime}(u)=\frac{\sin u}{1+u^{2}}</equation>，且<equation>F(x,y)=f(xy)</equation>.于是<equation>\frac{\partial F(x,y)}{\partial x}=f^{\prime}(xy)\cdot \frac{\partial(xy)}{\partial x}=\frac{\sin(xy)}{1+x^{2}y^{2}}\cdot y,</equation><equation>\frac{\partial^{2}F(x,y)}{\partial x^{2}}=y\cdot \frac{y\cos(xy)\cdot(1+x^{2}y^{2})-\sin(xy)\cdot 2xy^{2}}{(1+x^{2}y^{2})^{2}}.</equation>因此，<equation>\left. \frac{\partial^{2}F}{\partial x^{2}} \right|_{x=0, y=2}=4.</equation>（法二）先代值再求导.

由于<equation>F ( x, 2 ) = \int_{0}^{2 x} \frac{\sin t}{1 + t^{2}} \mathrm{d} t</equation>，故<equation>\left. \frac {\partial F}{\partial x} \right| _ {y = 2} = 2 \cdot \frac {\sin (2 x)}{1 + 4 x ^ {2}}, \quad \left. \frac {\partial^ {2} F}{\partial x ^ {2}} \right| _ {y = 2} = 2 \cdot \frac {2 \cos (2 x) \cdot \left(1 + 4 x ^ {2}\right) - \sin (2 x) \cdot 8 x}{\left(1 + 4 x ^ {2}\right) ^ {2}}.</equation>

---

**2011年第16题 | 解答题 | 10分**

16. (本题满分9分)

设函数 z = f(xy, yg(x))，其中函数 f具有二阶连续偏导数，函数 g(x)可导，且在 x=1处取得极值 g(1)=1.

求<equation>\left.\frac{\partial^{2} z}{\partial x \partial y}\right|_{x=1}</equation>y=1.

**解析:**由链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = f _ {1} ^ {\prime} \frac {\partial (x y)}{\partial x} + f _ {2} ^ {\prime} \frac {\partial [ y g (x) ]}{\partial x} = y f _ {1} ^ {\prime} + y g ^ {\prime} (x) f _ {2} ^ {\prime}, \\ \frac {\partial^ {2} z}{\partial x \partial y} = \frac {\partial \left[ y \left(f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime}\right) \right]}{\partial y} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left\{f _ {1 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + f _ {1 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} + g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} \frac {\partial (x y)}{\partial y} + g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \frac {\partial [ y g (x) ]}{\partial y} \right\} \\ = f _ {1} ^ {\prime} + g ^ {\prime} (x) f _ {2} ^ {\prime} + y \left[ x f _ {1 1} ^ {\prime \prime} + g (x) f _ {1 2} ^ {\prime \prime} + x g ^ {\prime} (x) f _ {2 1} ^ {\prime \prime} + g (x) g ^ {\prime} (x) f _ {2 2} ^ {\prime \prime} \right]. \\ \end{array}</equation>由<equation>g ( x )</equation>可导且在<equation>x=1</equation>处取得极值<equation>g ( 1 )=1</equation>知，<equation>g^{\prime}(1)=0.</equation>将<equation>x=1, y=1, g ( 1 )=1,</equation><equation>g^{\prime}(1)=0</equation>代入<equation>\frac{\partial^{2} z}{\partial x \partial y}</equation>，得<equation>\left. \frac {\partial^ {2} z}{\partial x \partial y} \right| _ {x = 1 \atop y = 1} = f _ {1} ^ {\prime} (1, 1) + f _ {1 1} ^ {\prime \prime} (1, 1) + f _ {1 2} ^ {\prime \prime} (1, 1).</equation>

---

**2010年第2题 | 选择题 | 4分 | 答案: B**

2. 设函数 z=z(x,y)由方程<equation>F\left( \frac{y}{x},\frac{z}{x} \right)=0</equation>确定，其中 F为可微函数，且<equation>F_{2}^{\prime}\neq0</equation>，则<equation>x\frac{\partial z}{\partial x}+y\frac{\partial z}{\partial y}=</equation>(    )

A. x B. z C. -x D. -z

答案: B

**解析:**解 对方程<equation>F\left(\frac{y}{x},\frac{z}{x}\right)=0</equation>两端同时关于x，y求偏导数，可得<equation>- \frac {y}{x ^ {2}} F _ {1} ^ {\prime} + \left(- \frac {z}{x ^ {2}} + \frac {1}{x} \cdot \frac {\partial z}{\partial x}\right) F _ {2} ^ {\prime} = 0, \quad \frac {F _ {1} ^ {\prime}}{x} + \frac {F _ {2} ^ {\prime}}{x} \cdot \frac {\partial z}{\partial y} = 0.</equation>由上面两个方程解得，<equation>\frac {\partial z}{\partial x} = \frac {\frac {y}{x} F _ {1} ^ {\prime} + \frac {z}{x} F _ {2} ^ {\prime}}{F _ {2} ^ {\prime}}, \quad \frac {\partial z}{\partial y} = - \frac {F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}}.</equation>因此，<equation>x \frac {\partial z}{\partial x} + y \frac {\partial z}{\partial y} = \frac {y F _ {1} ^ {\prime} + z F _ {2} ^ {\prime} - y F _ {1} ^ {\prime}}{F _ {2} ^ {\prime}} = z.</equation>应选B.

---

**2009年第9题 | 填空题 | 4分**

9. 设函数 f(u,v)具有二阶连续偏导数，z=f(x,xy)，则<equation>\frac{\partial^{2} z}{\partial x \partial y}=</equation>___

**答案:**<equation>x f_{12}^{\prime \prime}+f_{2}^{\prime}+ x y f_{22}^{\prime \prime}.</equation>

**解析:**由二元复合函数求导的链式法则知<equation>\begin{aligned} \frac {\partial z}{\partial x} &= f ^ {\prime} _ {1} (x, x y) + y f ^ {\prime} _ {2} (x, x y), \\ \frac {\partial^ {2} z}{\partial x \partial y} &= x f _ {1 2} ^ {\prime \prime} (x, x y) + f _ {2} ^ {\prime} (x, x y) + x y f _ {2 2} ^ {\prime \prime} (x, x y). \end{aligned}</equation>

---


