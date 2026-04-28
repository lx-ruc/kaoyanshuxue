# 数学三

## 高等数学

### 多元函数微积分学

#### 全微分的概念与计算

**2023年第12题 | 填空题 | 5分**

12. 已知函数 f(x,y)满足<equation>\mathrm{d} f(x,y)=\frac{x\mathrm{d} y-y\mathrm{d} x}{x^{2}+y^{2}}, f(1,1)=\frac{\pi}{4}</equation>，则 f<equation>(\sqrt{3},3)=</equation>___.

**答案:**##<equation>\frac{\pi}{3}</equation>

**解析:**解 由<equation>\mathrm{d}f(x,y)=\frac{x\mathrm{d}y-y\mathrm{d}x}{x^{2}+y^{2}}</equation>可知，<equation>f_{x}^{\prime}(x,y)=\frac{-y}{x^{2}+y^{2}},f_{y}^{\prime}(x,y)=\frac{x}{x^{2}+y^{2}}.</equation>于是，当<equation>y > 0</equation>时，<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int \frac {- y}{x ^ {2} + y ^ {2}} \mathrm {d} x = - \int \frac {\mathrm {d} \left(\frac {x}{y}\right)}{1 + \left(\frac {x}{y}\right) ^ {2}} = - \arctan \frac {x}{y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.实际上，<equation>\varphi(y)=f(0,y).</equation>对 f(x,y）=-arctan<equation>\frac{x}{y}+\varphi(y)</equation>关于 y求偏导数可得<equation>f _ {y} ^ {\prime} (x, y) = - \frac {- \frac {x}{y ^ {2}}}{1 + \left(\frac {x}{y}\right) ^ {2}} + \varphi^ {\prime} (y) = \frac {x}{x ^ {2} + y ^ {2}} + \varphi^ {\prime} (y).</equation>比较可得<equation>\varphi^{\prime}(y)=0</equation>，从而当 y > 0时，<equation>\varphi(y)=C,f(x,y)=-\arctan \frac{x}{y}+C</equation>，其中 C为待定常数.

由<equation>f(1,1)=\frac{\pi}{4}</equation>可得，<equation>\frac{\pi}{4}=-\frac{\pi}{4}+C</equation>，解得 C<equation>=\frac{\pi}{2}.</equation>因此，<equation>f(x,y)=-\arctan \frac{x}{y}+\frac{\pi}{2}.</equation>进一步可得<equation>f (\sqrt {3}, 3) = - \arctan \frac {1}{\sqrt {3}} + \frac {\pi}{2} = \frac {\pi}{2} - \frac {\pi}{6} = \frac {\pi}{3}.</equation>

---

**2021年第4题 | 选择题 | 5分 | 答案: C**

4. 设函数 f(x,y)可微，且<equation>f ( x+1, \mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x, x^{2} )=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f ( 1, 1 )=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>

答案: C

**解析:**根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f ( x+1,\mathrm{e}^{x} )=x ( x+1 )^{2}, f ( x,x^{2} )=2 x^{2} \ln x</equation>两端均关于 x求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令<equation>x=0</equation>，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令<equation>x=1</equation>，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第9题 | 填空题 | 4分**

9. 设<equation>z=\arctan[xy+\sin(x+y)]</equation>，则<equation>\mathrm{d}z|_{(0,\pi)}=</equation>___.

**答案:**<equation>(\pi - 1) \mathrm {d} x - \mathrm {d} y.</equation>

**解析:**根据链式法则，<equation>\frac{\partial z}{\partial x}=\frac{y+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}},</equation><equation>\frac{\partial z}{\partial y}=\frac{x+\cos(x+y)}{1+\left[ x y+\sin(x+y)\right]^{2}}.</equation>代入<equation>x=0,y=\pi</equation>，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,\pi)}=\pi-1, \frac{\partial z}{\partial y}\bigg|_{(0,\pi)}=-1.</equation>因此，<equation>\mathrm{d}z\bigg|_{(0,\pi)}=(\pi-1)\mathrm{d}x-\mathrm{d}y.</equation>

---

**2017年第12题 | 填空题 | 4分**

12. 设函数<equation>f(x,y)</equation>具有一阶连续偏导数，且<equation>\mathrm{d} f(x,y)=y \mathrm{e}^{y} \mathrm{d} x+x(1+y) \mathrm{e}^{y} \mathrm{d} y,f(0,0)=0</equation>，则<equation>f(x,y)=</equation>___

**答案:**##<equation>x y \mathrm{e}^{y}.</equation>

**解析:**由于<equation>\mathrm {d} f (x, y) = y \mathrm {e} ^ {y} \mathrm {d} x + x (1 + y) \mathrm {e} ^ {y} \mathrm {d} y,</equation>故<equation>f_x^{\prime}(x,y) = y\mathrm{e}^{y}, f_y^{\prime}(x,y) = x(1 + y)\mathrm{e}^{y}.</equation>对<equation>f_{x}^{\prime}(x,y)</equation>关于 x积分，得<equation>f (x, y) = \int f _ {x} ^ {\prime} (x, y) \mathrm {d} x = \int y \mathrm {e} ^ {y} \mathrm {d} x = x y \mathrm {e} ^ {y} + \varphi (y),</equation>其中<equation>\varphi(y)</equation>为关于 y的一元函数.

对<equation>x y \mathrm{e}^{y}+\varphi(y)</equation>关于y求偏导数，得<equation>\frac {\partial \left[ x y \mathrm {e} ^ {y} + \varphi (y) \right]}{\partial y} = x \mathrm {e} ^ {y} + x y \mathrm {e} ^ {y} + \varphi^ {\prime} (y) = x (1 + y) \mathrm {e} ^ {y} + \varphi^ {\prime} (y).</equation>与<equation>f_{y}^{\prime}(x,y)</equation>比较，得<equation>\varphi^{\prime}(y) = 0</equation>，故<equation>\varphi(y)\equiv C</equation>，其中C为常数.

代入<equation>x = 0</equation>，<equation>y = 0</equation>，得<equation>f(0,0) = 0 + C.</equation>于是，<equation>C = 0.</equation>因此，<equation>f ( x,y)= x y \mathrm{e}^{y}.</equation>

---

**2016年第11题 | 填空题 | 4分**

11. 设函数 f(u,v) 可微，z=z(x,y) 由方程<equation>( x+1 ) z-y^{2}=x^{2} f ( x-z,y )</equation>确定，则<equation>\mathrm{d} z |_{(0,1)}=</equation>___

**答案:**## dx + 2dy.

**解析:**（法一）对已知方程两端分别关于 x，y求偏导数，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} = 2 x f (x - z, y) + x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(1 - \frac {\partial z}{\partial x}\right) \right].</equation><equation>(x + 1) \frac {\partial z}{\partial y} - 2 y = x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(- \frac {\partial z}{\partial y}\right) + f _ {2} ^ {\prime} (x - z, y) \right].</equation>将（x,y）=（0,1）代入已知方程，可得 z-1=0，从而 z(0,1)=1.再将（x,y,z）=（0,1,1）代入（1）、（2）两式，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,1)}=-1, \frac{\partial z}{\partial y}\bigg|_{(0,1)}=2.</equation>因此，<equation>\mathrm{d} z \bigg|_{(0,1)}=-\mathrm{d} x+2 \mathrm{d} y</equation><equation>\mathrm {d} z \mid_ {(0, 1)} = - \mathrm {d} x + 2 \mathrm {d} y.</equation>（法二）对已知方程两端微分，可得<equation>\mathrm{d}[(x+1)z]-\mathrm{d}(y^{2})=\mathrm{d}[x^{2}f(x-z,y)]</equation>.进一步可得，<equation>\begin{aligned} (x + 1) \mathrm {d} z + z \mathrm {d} x - 2 y \mathrm {d} y &= f (x - z, y) \mathrm {d} \left(x ^ {2}\right) + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right] \\ &= 2 x f (x - z, y) \mathrm {d} x + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right]. \end{aligned}</equation>将（x,y）=（0,1）代入已知方程，可得 z-1=0，从而 z（0,1）=1.代入上式可得<equation>\mathrm {d} z + \mathrm {d} x - 2 \mathrm {d} y = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,1)} = -\mathrm{d}x + 2\mathrm{d}y.</equation>

---

**2015年第11题 | 填空题 | 4分**

11. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{x+2y+3z} + xyz = 1</equation>确定，则<equation>\mathrm{d}z|_{(0,0)} =</equation>___

**答案:**<equation>- \frac {1}{3} \mathrm {d} x - \frac {2}{3} \mathrm {d} y.</equation>

**解析:**解下面我们分别用上述三种方法解本题.

（法一）对原方程两端分别关于 x,y求偏导数，可得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(1 + 3 \frac {\partial z}{\partial x}\right) + y z + x y \frac {\partial z}{\partial x} = 0.</equation><equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(2 + 3 \frac {\partial z}{\partial y}\right) + x z + x y \frac {\partial z}{\partial y} = 0.</equation>当<equation>x=0,y=0</equation>时，由原方程知<equation>\mathrm{e}^{3 z}=1</equation>，故<equation>z(0,0)=0</equation>代入（1）式得<equation>\frac{\partial z}{\partial x}=-\frac{1}{3}</equation>代入（2）式得<equation>\frac{\partial z}{\partial y}=-\frac{2}{3}.</equation>因此，<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法二）对原方程两端微分，可得<equation>\mathrm{d}\left(\mathrm{e}^{x + 2y + 3z} + xyz\right) = 0</equation>，展开得<equation>\mathrm {e} ^ {x + 2 y + 3 z} \left(\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z\right) + y z \mathrm {d} x + x z \mathrm {d} y + x y \mathrm {d} z = 0.</equation>当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>代入（3）式得<equation>\mathrm {d} x + 2 \mathrm {d} y + 3 \mathrm {d} z = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>（法三）当<equation>x = 0, y = 0</equation>时，由原方程知<equation>\mathrm{e}^{3z} = 1</equation>，故<equation>z(0,0) = 0.</equation>令<equation>F ( x, y, z) = \mathrm{e}^{x+2 y+3 z} + x y z - 1</equation>，则由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 0)} = - \left. \frac {F _ {x} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {\mathrm {e} ^ {x + 2 y + 3 z} + y z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {1}{3},</equation><equation>\left. \frac {\partial z}{\partial y} \right| _ {(0, 0)} = - \left. \frac {F _ {y} ^ {\prime}}{F _ {z} ^ {\prime}} \right| _ {(0, 0, 0)} = - \left. \frac {2 \mathrm {e} ^ {x + 2 y + 3 z} + x z}{3 \mathrm {e} ^ {x + 2 y + 3 z} + x y} \right| _ {(0, 0, 0)} = - \frac {2}{3}.</equation>因此，<equation>\mathrm{d}z\mid_{(0,0)} = -\frac{1}{3}\mathrm{d}x - \frac{2}{3}\mathrm{d}y.</equation>

---

**2012年第11题 | 填空题 | 4分**

11. 设连续函数<equation>z=f(x,y)</equation>满足<equation>\lim_{ \begin{array}{l} x\to 0 \\ y\to 1 \end{array} } \frac{f(x,y)-2x+y-2} {\sqrt{x^{2}+(y-1)^{2}}}=0</equation>，则<equation>\mathrm{d} z|_{(0,1)}=</equation>___

**答案:**## 2dx-dy.

**解析:**解 由于<equation>\lim_{x\to 0}\frac{f(x,y)-2x+y-2}{\sqrt{x^2+(y-1)^2}} = 0</equation>，故<equation>\lim_{y\to 0}\left[f(x,y)-2x+y-2\right] = 0.</equation>又由<equation>f ( x,y )</equation>在点（0,1）处连续可知，<equation>f ( 0,1 )=\lim_{x\to 0}\lim_{y\to 1} f ( x,y)=\lim_{x\to 0}\lim_{y\to 1} ( 2 x-y+2 )=1</equation>，故<equation>f ( 0,1 )=1.</equation>代入题给条件，可得<equation>\lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 1}} \frac {f (x , y) - f (0 , 1) - 2 x + (y - 1)}{\sqrt {x ^ {2} + (y - 1) ^ {2}}} = 0.</equation>因此，由函数<equation>f ( x,y )</equation>可微的定义可知，<equation>f ( x,y )</equation>在点(0,1)处可微且<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)} = 2,\frac{\partial f}{\partial y}\bigg|_{(0,1)} = -1,</equation><equation>\mathrm{d}z\mid_{(0,1)} = 2\mathrm{d}x - \mathrm{d}y.</equation>本题也可以直接计算<equation>\frac{\partial f}{\partial x}\bigg|_{(0,1)}, \frac{\partial f}{\partial y}\bigg|_{(0,1)}</equation>.

在等式<equation>\lim_{x\to 0}\frac{f(x,y)-2x+y-2}{\sqrt{x^2+(y-1)^2}} = 0</equation>中分别令<equation>y = 1</equation>，<equation>x = 0</equation>可得，<equation>\lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{| x |} = 0, \quad \lim _ {y \rightarrow 1} \frac {f (0 , y) + y - 2}{| y - 1 |} = 0.</equation>于是，<equation>\lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{x} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - 2 x - 1}{| x |} \cdot \frac {| x |}{x} = 0.</equation>同理可得<equation>\lim_{y\rightarrow 1}\frac{f(0,y)+y-2}{y-1}=0.</equation>从而<equation>\lim_{x\rightarrow 0}\frac{f(x,1)-1}{x}=2, \lim_{y\rightarrow 1}\frac{f(0,y)-1}{y-1}=-1.</equation>又因为 f(0,1)=1，所以<equation>\left. \frac {\partial f}{\partial x} \right| _ {(0, 1)} = \lim _ {x \rightarrow 0} \frac {f (x , 1) - 1}{x} = 2, \quad \left. \frac {\partial f}{\partial y} \right| _ {(0, 1)} = \lim _ {y \rightarrow 1} \frac {f (0 , y) - 1}{y - 1} = - 1.</equation>

---

**2011年第10题 | 填空题 | 4分**

10. 设函数<equation>z=\left(1+\frac{x}{y}\right)^{\frac{x}{y}}</equation>，则<equation>\mathrm{d}z|_{(1,1)}=</equation>___

**答案:**(1 + 2ln2) (dx - dy).

**解析:**解<equation>z = \mathrm{e}^{\frac{x}{y}\ln(1 + \frac{x}{y})}</equation>.根据链式法则，<equation>\begin{array}{l} \frac {\partial z}{\partial x} = \left(1 + \frac {x}{y}\right) ^ {\frac {x}{y}} \left[ \frac {1}{y} \ln \left(1 + \frac {x}{y}\right) + \frac {x}{y (x + y)} \right], \\ \frac {\partial z}{\partial y} = - \left(1 + \frac {x}{y}\right) ^ {\frac {x}{y}} \left[ \frac {x}{y ^ {2}} \ln \left(1 + \frac {x}{y}\right) + \frac {x ^ {2}}{y ^ {2} (x + y)} \right]. \\ \mathrm {n} 2, \frac {\partial z}{\partial y} \Big | _ {(1, 1)} = - (1 + 2 \ln 2), \mathrm {d} z \Big | _ {(1, 1)} = (1 + 2 \ln 2) \\ \end{array}</equation>因此，<equation>\frac{\partial z}{\partial x}\bigg|_{(1,1)} = 1 + 2\ln 2,\frac{\partial z}{\partial y}\bigg|_{(1,1)} = -(1 + 2\ln 2),\mathrm{d}z\bigg|_{(1,1)} = (1 + 2\ln 2)(\mathrm{d}x - \mathrm{d}y).</equation>

---


#### 二重积分的概念与性质

**2016年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>J_{i}=\iint_{D_{i}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y(i=1,2,3)</equation>，其中<equation>D_{1}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant 1\}</equation><equation>D_{2}=\{(x,y)\mid 0\leqslant x\leqslant 1,0\leqslant y\leqslant \sqrt{x}\}</equation><equation>D_{3}=\{(x,y)\mid 0\leqslant x\leqslant 1,x^{2}\leqslant y\leqslant 1</equation>则（    ）

A.<equation>J_{1}<J_{2}<J_{3}</equation>B.<equation>J_{3}<J_{1}<J_{2}</equation>C.<equation>J_{2}<J_{3}<J_{1}</equation>D.<equation>J_{2}<J_{1}<J_{3}</equation>

答案: B

**解析:**解如图所示，<equation>D_{1}=D_{2}\cup D_{2}^{\prime}=D_{3}\cup D_{3}^{\prime}.</equation>在<equation>D_{2}^{\prime}</equation>上，由于<equation>x-y<0,\sqrt[3]{x-y}<0</equation>，故<equation>\iint_{D_{2}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y<0.</equation>在<equation>D_{3}^{\prime}</equation>上，由于<equation>x-y>0,\sqrt[3]{x-y}>0</equation>，故<equation>\iint_{D_{3}^{\prime}} \sqrt[3]{x-y}\mathrm{d}x\mathrm{d}y>0.</equation>因此，<equation>J _ {1} - J _ {2} = \iint_ {D _ {1} \backslash D _ {2}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {2} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y < 0,</equation><equation>J _ {1} - J _ {3} = \iint_ {D _ {1} \backslash D _ {3}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {3} ^ {\prime}} \sqrt [ 3 ]{x - y} \mathrm {d} x \mathrm {d} y > 0.</equation>综上所述，<equation>J_{1} < J_{2}, J_{1} > J_{3}</equation>，即<equation>J_{3} < J_{1} < J_{2}.</equation>应选B.

---

**2013年第3题 | 选择题 | 4分 | 答案: B**

3. 设<equation>D_{k}</equation>是圆域<equation>D=\{(x,y)\mid x^{2}+y^{2}\leqslant 1\}</equation>位于第 k象限的部分.记<equation>I_{k}=\iint_{D_{k}}(y-x)\mathrm{d}x\mathrm{d}y(k=1,2,3,4)</equation>，则（    )

A.<equation>I_{1}>0</equation>B.<equation>I_{2}>0</equation>C.<equation>I_{3}>0</equation>D.<equation>I_{4}>0</equation>

答案: B

**解析:**解（法一）由于在第一象限内 x > 0，y > 0，第二象限内 x < 0，y > 0，第三象限内 x < 0， y < 0，第四象限内 x > 0，y < 0，故被积函数 y - x在第二象限内恒大于零，从而<equation>\iint_{D_{2}}(y-x)\mathrm{d}x\mathrm{d}y>0.</equation>应选B.

（法二）在极坐标系下计算<equation>I_{k}(k = 1,2,3,4).</equation><equation>\begin{array}{l} I _ {k} \stackrel {\text {极 坐 标}} {=} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \int_ {0} ^ {1} r ^ {2} \mathrm {d} r = \frac {1}{3} \int_ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}} (\sin \theta - \cos \theta) \mathrm {d} \theta \\ = - \frac {\left(\sin \theta + \cos \theta\right)}{3} \Bigg | _ {\frac {(k - 1) \pi}{2}} ^ {\frac {k \pi}{2}}. \\ \end{array}</equation>分别求得<equation>I _ {1} = 0, \quad I _ {2} = \frac {2}{3}, \quad I _ {3} = 0, \quad I _ {4} = - \frac {2}{3}.</equation><equation>I_{2} > 0</equation>应选B.

---


#### 二重积分的综合与应用

**2014年第10题 | 填空题 | 4分**

10. 设 D 是由曲线<equation>xy+1=0</equation>与直线<equation>y+x=0</equation>及<equation>y=2</equation>围成的有界区域，则 D 的面积为 ___.

**答案:**<equation>\frac {3}{2} - \ln 2.</equation>

**解析:**（法一）区域D如图（a）所示.将D写为Y型区域，<equation>D = \left\{(x, y) \mid - y \leqslant x \leqslant - \frac {1}{y}, 1 \leqslant y \leqslant 2 \right\}.</equation>因此，<equation>D</equation>的面积<equation>= \iint_{D} \mathrm{d}x \mathrm{d}y = \int_{1}^{2} \mathrm{d}y \int_{-y}^{-\frac{1}{y}} \mathrm{d}x = \int_{1}^{2} \left(-\frac{1}{y} + y\right) \mathrm{d}y = -\ln y \left|_{1}^{2} + \frac{y^{2}}{2}\right|_{1}^{2} = \frac{3}{2} - \ln 2.</equation>（法二）如图（b）所示，将<equation>D</equation>分为两个X型区域<equation>D_{1}, D_{2}</equation>.<equation>D _ {1} = \left\{(x, y) \mid - x \leqslant y \leqslant 2, - 2 \leqslant x \leqslant - 1 \right\},</equation><equation>D _ {2} = \left\{(x, y) \mid - \frac {1}{x} \leqslant y \leqslant 2, - 1 \leqslant x \leqslant - \frac {1}{2} \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \iint_ {D _ {1}} \mathrm {d} x \mathrm {d} y + \iint_ {D _ {2}} \mathrm {d} x \mathrm {d} y = \int_ {- 2} ^ {- 1} \mathrm {d} x \int_ {- x} ^ {2} \mathrm {d} y + \int_ {- 1} ^ {- \frac {1}{2}} \mathrm {d} x \int_ {- \frac {1}{x}} ^ {2} \mathrm {d} y \\ = \int_ {- 2} ^ {- 1} (2 + x) \mathrm {d} x + \int_ {- 1} ^ {- \frac {1}{2}} \left(2 + \frac {1}{x}\right) \mathrm {d} x = \frac {1}{2} + 1 + \ln \frac {1}{2} = \frac {3}{2} - \ln 2. \\ \end{array}</equation>

---

**2012年第12题 | 填空题 | 4分**

12. 由曲线<equation>y=\frac{4}{x}</equation>和直线<equation>y=x</equation>及<equation>y=4x</equation>在第一象限中围成的平面图形的面积为 ___

**答案:**## 4ln 2.

**解析:**解 D为由曲线<equation>y=\frac{4}{x}</equation>和直线 y=x及 y=4x在第一象限中围成的平面区域.由二重积分的几何意义知，所求面积为<equation>\iint\limits_{D}\mathrm{d}x\mathrm{d}y.</equation>先求出这三条曲线在第一象限中的交点，分别为（1，4），（2，2）.

(a)

(b)

（法一）如图（a）所示，将区域<equation>D</equation>划分为两个X型区域.<equation>D _ {1} = \left\{(x, y) \mid x \leqslant y \leqslant 4 x, 0 \leqslant x \leqslant 1 \right\}, \quad D _ {2} = \left\{(x, y) \mid x \leqslant y \leqslant \frac {4}{x}, 1 \leqslant x \leqslant 2 \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {1} \mathrm {d} x \int_ {x} ^ {4 x} \mathrm {d} y + \int_ {1} ^ {2} \mathrm {d} x \int_ {x} ^ {\frac {4}{x}} \mathrm {d} y = \int_ {0} ^ {1} 3 x \mathrm {d} x + \int_ {1} ^ {2} \left(\frac {4}{x} - x\right) \mathrm {d} x \\ = \frac {3}{2} + 4 \ln 2 - \frac {3}{2} = 4 \ln 2. \\ \end{array}</equation>（法二）如图（b）所示，将区域<equation>D</equation>划分为两个Y型区域.<equation>D _ {1} = \left\{(x, y) \mid \frac {y}{4} \leqslant x \leqslant y, 0 \leqslant y \leqslant 2 \right\}, \quad D _ {2} = \left\{(x, y) \mid \frac {y}{4} \leqslant x \leqslant \frac {4}{y}, 2 \leqslant y \leqslant 4 \right\}.</equation>因此，<equation>\begin{array}{l} D \text {的 面 积} = \iint_ {D} \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {2} \mathrm {d} y \int_ {\frac {y}{4}} ^ {y} \mathrm {d} x + \int_ {2} ^ {4} \mathrm {d} y \int_ {\frac {y}{4}} ^ {\frac {4}{y}} \mathrm {d} x = \int_ {0} ^ {2} \frac {3}{4} y \mathrm {d} y + \int_ {2} ^ {4} \left(\frac {4}{y} - \frac {y}{4}\right) \mathrm {d} y \\ = \frac {3}{2} + 4 \ln 2 - \frac {3}{2} = 4 \ln 2. \\ \end{array}</equation>

---

**2011年第19题 | 解答题 | 10分**

19. (本题满分10分)

设函数<equation>f(x)</equation>在区间[0,1]上具有连续导数，<equation>f(0) = 1</equation>，且满足<equation>\iint_ {D _ {t}} f ^ {\prime} (x + y) \mathrm {d} x \mathrm {d} y = \iint_ {D _ {t}} f (t) \mathrm {d} x \mathrm {d} y, \text {其 中} D _ {t} = \{(x, y) \mid 0 \leqslant y \leqslant t - x, 0 \leqslant x \leqslant t \} (0 < t \leqslant 1).</equation>求 f(x)的表达式.

**答案:**<equation>(1 9) f (x) = \frac {4}{(2 - x) ^ {2}}, 0 \leqslant x \leqslant 1.</equation>

**解析:**解<equation>\begin{array}{l} \iint_ {D _ {t}} f ^ {\prime} (x + y) \mathrm {d} x \mathrm {d} y = \int_ {0} ^ {t} \mathrm {d} x \int_ {0} ^ {t - x} f ^ {\prime} (x + y) \mathrm {d} y \xlongequal {u = x + y} \int_ {0} ^ {t} \mathrm {d} x \int_ {x} ^ {t} f ^ {\prime} (u) \mathrm {d} u \\ = \int_ {0} ^ {t} \left[ f (t) - f (x) \right] \mathrm {d} x = t f (t) - \int_ {0} ^ {t} f (x) \mathrm {d} x. \\ \end{array}</equation>另一方面，由于 f（t）中不包含变量 x,y，从而<equation>\iint_ {D _ {t}} f (t) \mathrm {d} x \mathrm {d} y = f (t) \iint_ {D _ {t}} \mathrm {d} x \mathrm {d} y = \frac {t ^ {2}}{2} f (t),</equation>其中<equation>\frac{t^{2}}{2}</equation>是<equation>D_{t}</equation>的面积，故我们得到一个新的等式，<equation>t f (t) - \int_ {0} ^ {t} f (x) \mathrm {d} x = \frac {t ^ {2}}{2} f (t).</equation>对（1）式两端关于 t求导，得<equation>f ( t )+ t f^{\prime} ( t )-f ( t )= t f ( t )+\frac{t^{2}}{2} f^{\prime} ( t )</equation>，化简得<equation>( 2-t ) f^{\prime} ( t )=2 f ( t ).</equation>这是一个可分离变量的微分方程.解该方程得，<equation>f(t)=\frac{C}{(2-t)^{2}},</equation>0 < t≤1.由 f(x)在[0,1]上连续且<equation>f(0)=1</equation>得，<equation>f (0) = \lim _ {t \rightarrow 0 ^ {+}} \frac {C}{(2 - t) ^ {2}} = \frac {C}{4} = 1.</equation>从而 C=4.

因此，<equation>f ( x ) = \frac { 4 } { ( 2 - x ) ^ { 2 } }</equation><equation>0 \leqslant x \leqslant 1.</equation>

---


### 一元函数积分学
#### 反常积分的计算

**2025年第12题 | 填空题 | 5分**

12. 设<equation>\int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x = \ln 2, \mathrm {则} a = \underline {{}}</equation>

**解析:**解 由于<equation>\frac{a}{x(2x+a)}=\frac{1}{x}-\frac{2}{2x+a}</equation>，故<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {a}{x (2 x + a)} \mathrm {d} x &= \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {2}{2 x + a}\right) \mathrm {d} x = \left(\ln x - \ln | 2 x + a |\right) \Bigg | _ {1} ^ {+ \infty} = \ln \frac {x}{| 2 x + a |} \Bigg | _ {1} ^ {+ \infty} \\ &= \lim _ {x \rightarrow + \infty} \ln \frac {x}{| 2 x + a |} - \ln \frac {1}{| 2 + a |} = \ln \frac {| 2 + a |}{2}. \end{aligned}</equation>由<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)} \mathrm{d}x=\ln 2</equation>可得<equation>\ln \frac{\mid 2+a\mid}{2}=\ln 2</equation>结合<equation>\ln x</equation>是单调函数可得<equation>\frac{\mid 2+a\mid}{2}=2</equation>解得 a=2或a=-6.

当 a=-6时，<equation>\int_{1}^{+\infty}\frac{a}{x(2x+a)}\mathrm{d}x=\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>，此时 x=3为被积函数的瑕点，且<equation>\lim_{x\to 3^{-}}\frac{x-3}{x(x-3)}=\frac{1}{3}</equation>，由无界函数的反常积分的极限审敛法可得<equation>\int_{1}^{3}\frac{1}{x(x-3)}\mathrm{d}x</equation>发散，从而<equation>\int_{1}^{+\infty}\frac{-3}{x(x-3)}\mathrm{d}x</equation>发散.于是，应舍去 a=-6.

当<equation>a = 2</equation>时，被积函数在<equation>(1, +\infty)</equation>上没有瑕点.

因此，a=2.

---

**2024年第12题 | 填空题 | 5分**

<equation>\int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\frac {1}{2} \ln 3 - \frac {\pi}{8}</equation>

**解析:**解（法一）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x^{2}-1)</equation>，而<equation>(x^{2}+4)-(x^{2}-1)=5</equation>，故<equation>\frac{5}{x^{4}+3 x^{2}-4}=\frac{5}{(x^{2}+4)(x^{2}-1)}=\frac{1}{x^{2}-1}-\frac{1}{x^{2}+4}=\frac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right)-\frac{1}{x^{2}+4}.</equation>因此，<equation>\begin{aligned} \int_ {2} ^ {+ \infty} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} d x &= \int_ {2} ^ {+ \infty} \left[ \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4} \right] d x \\ &= \frac {1}{2} \ln \left. \frac {x - 1}{x + 1} \right| _ {2} ^ {+ \infty} - \frac {1}{2} \int_ {2} ^ {+ \infty} \frac {1}{1 + \left(\frac {x}{2}\right) ^ {2}} d \left(\frac {x}{2}\right) \\ &= - \frac {1}{2} \ln \frac {1}{3} - \frac {1}{2} \arctan \frac {x}{2} \Big | _ {2} ^ {+ \infty} = \frac {1}{2} \ln 3 - \frac {1}{2} \left(\frac {\pi}{2} - \frac {\pi}{4}\right) \\ &= \frac {1}{2} \ln 3 - \frac {\pi}{8}. \end{aligned}</equation>（法二）注意到<equation>x^{4}+3 x^{2}-4=(x^{2}+4)(x+1)(x-1)</equation>，故对<equation>\frac{5}{x^{4}+3 x^{2}-4}</equation>进行部分分式分解设<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {A}{x - 1} + \frac {B}{x + 1} + \frac {C x + D}{x ^ {2} + 4}.</equation>通分并整理可得，<equation>\begin{aligned} \frac {5}{x ^ {4} + 3 x ^ {2} - 4} &= \frac {A (x + 1) \left(x ^ {2} + 4\right) + B (x - 1) \left(x ^ {2} + 4\right) + (C x + D) \left(x ^ {2} - 1\right)}{x ^ {4} + 3 x ^ {2} - 4} \\ &= \frac {(A + B + C) x ^ {3} + (A - B + D) x ^ {2} + (4 A + 4 B - C) x + 4 A - 4 B - D}{x ^ {4} + 3 x ^ {2} - 4}. \end{aligned}</equation>比较<equation>x^{3},x^{2},x</equation>的系数以及常数项可得，<equation>[ A + B + C = 0,</equation><equation>A - B + D = 0,</equation><equation>4 A + 4 B - C = 0,</equation><equation>4 A - 4 B - D = 5.</equation>(1) 式与（3）式相加并整理可得<equation>A+B=0</equation>，进一步可得 C=0.将 B=-A代人（2）式与（4）式可得<equation>\left\{\begin{array}{l l}2 A+D=0,\\ 8 A-D=5,\end{array}\right.</equation>解得<equation>\left\{\begin{array}{l l}A=\frac{1}{2},\\ B=-\frac{1}{2},\\ C=0,\\ D=-1. \end{array}\right.</equation>因此，<equation>\frac {5}{x ^ {4} + 3 x ^ {2} - 4} = \frac {1}{2} \left(\frac {1}{x - 1} - \frac {1}{x + 1}\right) - \frac {1}{x ^ {2} + 4}.</equation>其余同法一.

---

**2013年第11题 | 填空题 | 4分**

<equation>\int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**解析:**<equation>\begin{aligned} \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x &= - \int_ {1} ^ {+ \infty} \ln x \mathrm {d} \left(\frac {1}{1 + x}\right) = - \left[ \frac {\ln x}{1 + x} \Big | _ {1} ^ {+ \infty} - \int_ {1} ^ {+ \infty} \frac {1}{x (1 + x)} \mathrm {d} x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Big | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---


#### 定积分的计算

**2025年第17题 | 解答题 | 10分**

17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>

**答案:**#<equation>\frac{3\ln 2+\pi}{10}.</equation>

**解析:**解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得<equation>B=-A</equation>.将<equation>B=-A</equation>代入（2）式可得<equation>C=3A</equation>.将<equation>C=3A</equation>代入（3）式可得<equation>5A=1</equation>，即<equation>A=\frac{1}{5}</equation>.进一步可得<equation>B=-\frac{1}{5},C=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2022年第12题 | 填空题 | 5分**

<equation>\int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} \mathrm {d} x = \underline {{}}</equation>

**答案:**<equation>\ln 3 - \frac {\sqrt {3}}{3} \pi .</equation>

**解析:**解注意到<equation>( x^{2}+2 x+4)^{\prime}=2 x+2</equation>，<equation>\frac{2 x-4}{x^{2}+2 x+4}=\frac{2 x+2}{x^{2}+2 x+4}</equation><equation>-\frac{6}{x^{2}+2 x+4}.</equation>因此，<equation>\begin{aligned} \int_ {0} ^ {2} \frac {2 x - 4}{x ^ {2} + 2 x + 4} d x &= \int_ {0} ^ {2} \frac {2 x + 2}{x ^ {2} + 2 x + 4} d x - 6 \int_ {0} ^ {2} \frac {1}{x ^ {2} + 2 x + 4} d x \\ &= \int_ {0} ^ {2} \frac {\mathrm {d} \left(x ^ {2} + 2 x + 4\right)}{x ^ {2} + 2 x + 4} - 2 \int_ {0} ^ {2} \frac {1}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} d x \\ &= \ln \left(x ^ {2} + 2 x + 4\right) \Bigg | _ {0} ^ {2} - 2 \sqrt {3} \int_ {0} ^ {2} \frac {\mathrm {d} \left[ \frac {1}{\sqrt {3}} (x + 1) \right]}{1 + \left[ \frac {1}{\sqrt {3}} (x + 1) \right] ^ {2}} \\ &= \ln 3 - 2 \sqrt {3} \arctan \frac {1}{\sqrt {3}} (x + 1) \Bigg | _ {0} ^ {2} \\ &= \ln 3 - 2 \sqrt {3} \times \left(\frac {\pi}{3} - \frac {\pi}{6}\right) = \ln 3 - \frac {\sqrt {3}}{3} \pi . \end{aligned}</equation>

---

**2021年第12题 | 填空题 | 5分**

<equation>\int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {\left| x ^ {2} - 9 \right|}} \mathrm {d} x = \underline {{}}</equation>

**解析:**当<equation>\sqrt{5} < x < 3</equation>时，<equation>x^{2}-9<0</equation>；当 3 < x < 5时，<equation>x^{2}-9>0.</equation><equation>\begin{aligned} \int_ {\sqrt {5}} ^ {5} \frac {x}{\sqrt {| x ^ {2} - 9 |}} \mathrm {d} x &= \int_ {\sqrt {5}} ^ {3} \frac {x}{\sqrt {9 - x ^ {2}}} \mathrm {d} x + \int_ {3} ^ {5} \frac {x}{\sqrt {x ^ {2} - 9}} \mathrm {d} x \\ &= - \frac {1}{2} \int_ {\sqrt {5}} ^ {3} \frac {\mathrm {d} \left(9 - x ^ {2}\right)}{\sqrt {9 - x ^ {2}}} + \frac {1}{2} \int_ {3} ^ {5} \frac {\mathrm {d} \left(x ^ {2} - 9\right)}{\sqrt {x ^ {2} - 9}} \\ &= \left(- \frac {1}{2}\right) \times 2 \times \sqrt {9 - x ^ {2}} \left| _ {\sqrt {5}} ^ {3} + \frac {1}{2} \times 2 \times \sqrt {x ^ {2} - 9} \right| _ {3} ^ {5} \\ &= - (0 - 2) + (4 - 0) = 6. \end{aligned}</equation>

---

**2019年第11题 | 填空题 | 4分**

11. 已知函数<equation>f ( x )=\int_{1}^{x}\sqrt{1+t^{4}}\mathrm{d} t</equation>，则<equation>\int_{0}^{1} x^{2} f ( x ) \mathrm{d} x=</equation>___.

**答案:**<equation>\frac{1-2\sqrt{2}}{18}.</equation>

**解析:**（法一）利用分部积分法.

注意到 f（1）=0.<equation>\begin{aligned} \int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x &= \frac {1}{3} \int_ {0} ^ {1} f (x) \mathrm {d} \left(x ^ {3}\right) = \frac {1}{3} \left[ x ^ {3} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} x ^ {3} \cdot f ^ {\prime} (x) \mathrm {d} x \right] = - \frac {1}{3} \int_ {0} ^ {1} x ^ {3} \sqrt {1 + x ^ {4}} \mathrm {d} x \right. \\ &= - \frac {1}{1 2} \int_ {0} ^ {1} \sqrt {1 + x ^ {4}} \mathrm {d} \left(x ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + x ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \end{aligned}</equation>（法二）交换积分次序.

将 f(x) 代入所求积分.<equation>\int_ {0} ^ {1} x ^ {2} f (x) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \left(\int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t\right) \mathrm {d} x = \int_ {0} ^ {1} x ^ {2} \mathrm {d} x \int_ {1} ^ {x} \sqrt {1 + t ^ {4}} \mathrm {d} t.</equation>写出该积分对应的二重积分的积分区域 D. 由二次积分的表达式可知，边界曲线为 t=x，t=1以及 x=0，故<equation>D = \{(x, t) \mid x \leqslant t \leqslant 1, 0 \leqslant x \leqslant 1 \}.</equation>如图所示，交换积分次序可得<equation>D = \{(x, t) \mid 0 \leqslant x \leqslant t, 0 \leqslant t \leqslant 1 \}.</equation>因此，<equation>\begin{array}{l} = - \frac {1}{3} \cdot \frac {1}{4} \int_ {0} ^ {1} \sqrt {1 + t ^ {4}} \mathrm {d} \left(t ^ {4}\right) = - \frac {1}{1 2} \cdot \frac {2}{3} \cdot \left(1 + t ^ {4}\right) ^ {\frac {3}{2}} \Bigg | _ {0} ^ {1} = \frac {1 - 2 \sqrt {2}}{1 8}. \\ \end{array}</equation>

---

**2017年第9题 | 填空题 | 4分**

9.<equation>9. \int_ {- \pi} ^ {\pi} \left(\sin^ {3} x + \sqrt {\pi^ {2} - x ^ {2}}\right) \mathrm {d} x = \underline {{}}</equation>

**解析:**由于<equation>[-\pi ,\pi ]</equation>是对称区间，且<equation>\sin^{3}x</equation>是关于x的奇函数，<equation>\sqrt{\pi^{2}-x^{2}}</equation>是关于x的偶函数，故原积分<equation>\frac{\int_{-\pi}^{\pi}\sin^{3}x\mathrm{d}x=0}{\int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x} \int_{-\pi}^{\pi}\sqrt{\pi^{2}-x^{2}}\mathrm{d}x</equation><equation>\frac{x=\pi\sin t}{2} 2\int_{0}^{\frac{\pi}{2}}\pi\cos t\cdot \pi\cos t\mathrm{d}t=\pi^{2}\int_{0}^{\frac{\pi}{2}}2\cos^{2}t\mathrm{d}t</equation><equation>= \pi^{2}\int_{0}^{\frac{\pi}{2}}(1+\cos 2t)\mathrm{d}t=\pi^{2}\times \left(\frac{\pi}{2}+0\right)=\frac{\pi^{3}}{2}.</equation>

---

**2014年第11题 | 填空题 | 4分**

11. 设<equation>\int_{0}^{a} x \mathrm{e}^{2 x} \mathrm{d} x=\frac{1}{4}</equation>，则 a=___

**解析:**由于<equation>\frac{1}{4}=\int_{0}^{a}x\mathrm{e}^{2x}\mathrm{d}x=\frac{x\mathrm{e}^{2x}}{2}\bigg|_{0}^{a}-\int_{0}^{a}\frac{\mathrm{e}^{2x}}{2}\mathrm{d}x=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2x}}{4}\bigg|_{0}^{a}=\frac{a}{2}\mathrm{e}^{2a}-\frac{\mathrm{e}^{2a}}{4}+\frac{1}{4},</equation>故<equation>\frac{a}{2}\mathrm{e}^{2a}=\frac{\mathrm{e}^{2a}}{4}</equation>因此，<equation>a=\frac{1}{2}.</equation>

---


#### 变限积分

**2024年第2题 | 选择题 | 5分 | 答案: B**

2. 设<equation>I=\int_{a}^{a+k\pi}|\sin x|\mathrm{d}x,k</equation>为整数，则 I的值（    ）

A. 只与 a有关 B. 只与 k有关 C. 与 a,k均有关 D. 与 a,k均无关

答案: B

**解析:**解（法一）由于<equation>|\sin (x + \pi)| = | - \sin x| = |\sin x|</equation>，故<equation>|\sin x|</equation>是周期为<equation>\pi</equation>的周期函数由分析中的结论（2）可知，<equation>I = \int_ {a} ^ {a + k \pi} | \sin x | \mathrm {d} x = k \int_ {0} ^ {\pi} | \sin x | \mathrm {d} x = k \int_ {0} ^ {\pi} \sin x \mathrm {d} x = 2 k.</equation>因此，<equation>I</equation>的值只与k有关，应选B.

（法二）我们先证明：<equation>\int_{a}^{a+k\pi}|\sin x|\mathrm{d}x=\int_{0}^{k\pi}|\sin x|\mathrm{d}x.</equation>记<equation>F ( a )=\int_{a}^{a+k\pi}|\sin x| \mathrm{d} x.</equation>考虑<equation>F^{\prime}(a).</equation><equation>\begin{aligned} F ^ {\prime} (a) &= \left(\int_ {a} ^ {a + k \pi} | \sin x | \mathrm {d} x\right) ^ {\prime} = | \sin (a + k \pi) | - | \sin a | \\ \underline {{\sin (x + k \pi) = (- 1) ^ {k} \sin x}} | (- 1) ^ {k} \sin a | - | \sin a | &= 0. \end{aligned}</equation>于是，<equation>F(a)</equation>是常函数，<equation>F(a)</equation>恒等于<equation>F(0)</equation>，即<equation>\int_{0}^{k\pi}|\sin x|\mathrm{d}x.</equation>由定积分的性质可得，<equation>I = \int_ {0} ^ {k \pi} | \sin x | \mathrm {d} x = \sum_ {i = 0} ^ {k - 1} \int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x.</equation>由于<equation>\int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x \xlongequal {t = x - i \pi} \int_ {0} ^ {\pi} | \sin (t + i \pi) | \mathrm {d} t = \int_ {0} ^ {\pi} \sin t \mathrm {d} t = 2,</equation>故由（1）式可得<equation>I = \sum_ {i = 0} ^ {k - 1} \int_ {i \pi} ^ {(i + 1) \pi} | \sin x | \mathrm {d} x = 2 k.</equation>因此，<equation>I</equation>的值只与k有关，应选B.

---

**2020年第3题 | 选择题 | 4分 | 答案: A**

3. 设奇函数 f(x)在<equation>(-\infty,+\infty)</equation>上具有连续导数，则（    )

A.<equation>\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是奇函数 B.<equation>\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是偶函数

C.<equation>\int_{0}^{x}[\cos f^{\prime}(t)+f(t)]\mathrm{d}t</equation>是奇函数 D.<equation>\int_{0}^{x}[\cos f^{\prime}(t)+f(t)]\mathrm{d}t</equation>是偶函数

答案: A

**解析:**解 由于 f(x)是奇函数，故<equation>\cos f(x)</equation>是偶函数，<equation>f^{\prime}(x)</equation>是偶函数，从而<equation>\cos f(x)+f^{\prime}(x)</equation>也是偶函数.<equation>F(x)=\int_{0}^{x}[\cos f(t)+f^{\prime}(t)]\mathrm{d}t</equation>是<equation>\cos f(x)+f^{\prime}(x)</equation>的一个原函数，且 F(0)=0.因此， F(x)是奇函数.应选A.

下面说明其余选项均不正确.

取<equation>f ( x )=x</equation>，则<equation>\cos f ( x )=\cos x,f^{\prime}(x)=1,\cos f^{\prime}(x)=\cos 1.</equation><equation>\int_{0}^{x}[\cos t+1]\mathrm{d} t=\sin x+x</equation>是奇函数，故选项B不正确.<equation>\int_{0}^{x}[\cos 1+t]\mathrm{d} t=\cos 1\cdot x+\frac{x^{2}}{2}</equation>既不是奇函数，也不是偶函数，故选项C、D不正确.

---

**2016年第18题 | 解答题 | 10分**

18. (本题满分10分）

设函数 f(x)连续，且满足<equation>\int_{0}^{x} f(x-t)\mathrm{d} t=\int_{0}^{x}(x-t)f(t)\mathrm{d} t+\mathrm{e}^{-x}-1</equation>求 f(x).

**答案:**<equation>f (x) = - \frac {\mathrm {e} ^ {- x} + \mathrm {e} ^ {x}}{2}.</equation>

**解析:**令 u=x-t，则<equation>\int_ {0} ^ {x} f (x - t) \mathrm {d} t \xlongequal {u = x - t} - \int_ {x} ^ {0} f (u) \mathrm {d} u = \int_ {0} ^ {x} f (u) \mathrm {d} u.</equation>另一方面，<equation>\int_ {0} ^ {x} (x - t) f (t) \mathrm {d} t = x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t.</equation>于是已知等式化为<equation>\int_ {0} ^ {x} f (u) \mathrm {d} u = x \int_ {0} ^ {x} f (t) \mathrm {d} t - \int_ {0} ^ {x} t f (t) \mathrm {d} t + \mathrm {e} ^ {- x} - 1.</equation>由于 f(x) 连续，故<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>可导.对上式两端关于 x求导，可得<equation>f (x) = \int_ {0} ^ {x} f (t) \mathrm {d} t + x f (x) - x f (x) - \mathrm {e} ^ {- x},</equation>即<equation>f (x) = \int_ {0} ^ {x} f (t) \mathrm {d} t - \mathrm {e} ^ {- x}.</equation>对（1）式两端关于 x求导，可得<equation>f ^ {\prime} (x) = f (x) + \mathrm {e} ^ {- x},</equation>即<equation>f^{\prime}(x) - f(x) = \mathrm{e}^{-x}</equation>.<equation>\begin{aligned} f (x) &= \mathrm {e} ^ {- \int (- 1) \mathrm {d} x} \left[ \int \mathrm {e} ^ {- x} \cdot \mathrm {e} ^ {\int (- 1) \mathrm {d} x} \mathrm {d} x + C \right] = \mathrm {e} ^ {x} \left(\int \mathrm {e} ^ {- x} \cdot \mathrm {e} ^ {- x} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {x} \left(\int \mathrm {e} ^ {- 2 x} \mathrm {d} x + C\right) = \mathrm {e} ^ {x} \left(- \frac {1}{2} \mathrm {e} ^ {- 2 x} + C\right), \end{aligned}</equation>此为一阶非齐次线性微分方程.由求解公式可得，

其中 C为待定常数.

将 x=0代入（1）式可得，<equation>f(0)=-1</equation>.再将 x=0，<equation>f(0)=-1</equation>代入（2）式，可得<equation>-1=-\frac{1}{2}+C</equation>解得 C=-<equation>\frac{1}{2}</equation>.因此，<equation>f (x) = \mathrm {e} ^ {x} \left(- \frac {1}{2} \mathrm {e} ^ {- 2 x} - \frac {1}{2}\right) = - \frac {\mathrm {e} ^ {- x} + \mathrm {e} ^ {x}}{2}.</equation>

---

**2015年第10题 | 填空题 | 4分**

10. 设函数 f(x) 连续，<equation>\varphi(x)=\int_{0}^{x^{2}} x f(t) \mathrm{d} t</equation>. 若<equation>\varphi(1)=1, \varphi^{\prime}(1)=5</equation>，则 f(1) = ___.

**解析:**解 首先，由于在<equation>\int_0^{x^2} xf(t)\mathrm{d}t</equation>中，<equation>x</equation>不是积分变量，故可将<equation>x</equation>作为因子提出放在积分号外，即<equation>\varphi (x) = \int_ {0} ^ {x ^ {2}} x f (t) \mathrm {d} t = x \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t.</equation>由求导的乘法法则和变限积分的求导公式可得<equation>\varphi^ {\prime} (x) = \int_ {0} ^ {x ^ {2}} f (t) \mathrm {d} t + x f \left(x ^ {2}\right) \cdot 2 x.</equation>由<equation>\varphi(1)=1</equation>可得<equation>\varphi(1)=\int_{0}^{1} f(t)\mathrm{d} t=1</equation>；由<equation>\varphi^{\prime}(1)=5</equation>可得<equation>\varphi^{\prime}(1)=\int_{0}^{1} f(t)\mathrm{d} t+2f(1)=5.</equation>因此，<equation>f(1)=\frac{\varphi^{\prime}(1)-\varphi(1)}{2}=2.</equation>

---

**2010年第9题 | 填空题 | 4分**

9. 设可导函数<equation>y=y(x)</equation>由方程<equation>\int_{0}^{x+y}\mathrm{e}^{-t^{2}}\mathrm{d}t=\int_{0}^{x}x\sin t^{2}\mathrm{d}t</equation>确定，则<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=</equation>___.

**解析:**解 对方程<equation>\int_{0}^{x+y}\mathrm{e}^{-t^{2}}\mathrm{d}t=\int_{0}^{x}x\sin t^{2}\mathrm{d}t=x\int_{0}^{x}\sin t^{2}\mathrm{d}t</equation>两端关于 x求导得，<equation>\mathrm{e}^{-(x+y)^{2}}\cdot[1+y^{\prime}(x)]=\int_{0}^{x}\sin t^{2}\mathrm{d}t+x\sin x^{2}.</equation>将 x=0代入原方程得<equation>\int_{0}^{y}\mathrm{e}^{-t^{2}}\mathrm{d}t=0</equation>.由于<equation>\mathrm{e}^{-t^{2}}</equation>恒大于零，故 y=0.再将 x=0，y=0代入（1）式可知，<equation>1+y^{\prime}(0)=0</equation>.因此，<equation>\left.\frac{\mathrm{d}y}{\mathrm{d}x}\right|_{x=0}=y^{\prime}(0)=-1.</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: A**

3. 使不等式<equation>\int_{1}^{x} \frac{\sin t}{t}\mathrm{d}t > \ln x</equation>成立的 x 的范围是（    ）

A. (0,1) B.<equation>\left(1, \frac{\pi}{2}\right)</equation>C.<equation>\left(\frac{\pi}{2}, \pi\right)</equation>D.<equation>(\pi, +\infty)</equation>

答案: A

**解析:**解 令<equation>f ( x )=\int_{1}^{x}\frac{\sin t}{t}\mathrm{d} t-\ln x</equation>，则<equation>f ( 1 )=0. f ( x )</equation>的自然定义域为<equation>x > 0.</equation>计算<equation>f^{\prime}(x)</equation>得，<equation>f ^ {\prime} (x) = \frac {\sin x}{x} - \frac {1}{x} = \frac {\sin x - 1}{x} \leqslant 0,</equation>并且等号仅在<equation>x=2 n \pi+\frac{\pi}{2}</equation>（<equation>n</equation>为正整数）时成立.于是，<equation>f(x)</equation>是（0，<equation>+\infty</equation>）上的单调减少函数.

当 0 < x < 1时，<equation>f ( x ) > f ( 1 ) = 0</equation>；当 x > 1时，<equation>f ( x ) < f ( 1 ) = 0</equation>因此，使得<equation>f ( x ) > 0</equation>即<equation>\int_{1}^{x}\frac{\sin t}{t}\mathrm{d}t-\ln x>0</equation>的 x的范围是(0,1).应选A.

---

**2009年第4题 | 选择题 | 4分 | 答案: D**

4. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.

答案: D

**解析:**解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0,2），（2,3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在<equation>[-1,0)</equation>上，<equation>f ( x ) > 0</equation>，故 F(x) 单调增加；在(0,1)上，<equation>f ( x ) < 0</equation>，故 F(x) 单调减少；在

(1,2)上，<equation>f ( x ) > 0</equation>，故<equation>F ( x )</equation>单调增加；在（2,3]上，<equation>f ( x ) = 0</equation>，故<equation>F ( x )</equation>为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D.应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1,3]上有界且只有两个间断点，f(x)在[-1,3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d} t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 定积分的应用

**2024年第19题 | 解答题 | 12分**

19. (本题满分12分)

设 t>0，平面有界区域 D由曲线<equation>y=x\mathrm{e}^{-2x}</equation>与直线 x=t,x=2t及 x轴围成，D的面积为 S(t)，求 S(t)的最大值.

**答案:**<equation>\frac {1}{1 6} \ln 2 + \frac {3}{6 4}.</equation>

**解析:**解 由于<equation>x\mathrm{e}^{-2x} > 0</equation>，故区域D的面积<equation>S(t) = \int_{t}^{2t}x\mathrm{e}^{-2x}\mathrm{d}x.</equation>由变限积分的求导公式可得，<equation>S ^ {\prime} (t) = \left(\int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) ^ {\prime} = 2 \cdot 2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} = 4 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} = t \mathrm {e} ^ {- 4 t} \left(4 - \mathrm {e} ^ {2 t}\right).</equation>解<equation>4-\mathrm{e}^{2 t}=0</equation>可得<equation>t=\ln 2</equation>.于是，当<equation>0 < t < \ln 2</equation>时，<equation>S^{\prime}(t)>0,S(t)</equation>单调增加，当<equation>t > \ln 2</equation>时，<equation>S^{\prime}(t)<0,S(t)</equation>单调减少.

因此，<equation>S ( t )</equation>的最大值在<equation>t=\ln 2</equation>时取得，最大值为<equation>S (\ln 2).</equation>下面用两种方法计算<equation>S(\ln 2).</equation>（法一）<equation>\begin{array}{l} S (\ln 2) = \int_ {\ln 2} ^ {2 \ln 2} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {1}{2} \int_ {\ln 2} ^ {2 \ln 2} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {1}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2} - \int_ {\ln 2} ^ {2 \ln 2} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ = - \frac {1}{2} \left(2 \ln 2 \cdot \frac {1}{1 6} - \ln 2 \cdot \frac {1}{4} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {\ln 2} ^ {2 \ln 2}\right) = \frac {\ln 2}{1 6} - \frac {1}{4} \left(\frac {1}{1 6} - \frac {1}{4}\right) \\ = \frac {\ln 2}{1 6} + \frac {3}{6 4}. \\ \end{array}</equation>（法二）也可以计算出<equation>S(t)</equation>的表达式再代入<equation>t = \ln 2</equation>.<equation>\begin{array}{l} S (t) = \int_ {t} ^ {2 t} x \mathrm {e} ^ {- 2 x} \mathrm {d} x = - \frac {1}{2} \int_ {t} ^ {2 t} x \mathrm {d} \left(\mathrm {e} ^ {- 2 x}\right) = - \frac {1}{2} \left(x \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t} - \int_ {t} ^ {2 t} \mathrm {e} ^ {- 2 x} \mathrm {d} x\right) \\ = - \frac {1}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 2 x} \Big | _ {t} ^ {2 t}\right) = - \frac {1}{2} \left(2 t \mathrm {e} ^ {- 4 t} - t \mathrm {e} ^ {- 2 t} + \frac {1}{2} \mathrm {e} ^ {- 4 t} - \frac {1}{2} \mathrm {e} ^ {- 2 t}\right) \\ = - \frac {1}{2} \left[ \left(2 t + \frac {1}{2}\right) \mathrm {e} ^ {- 4 t} - \left(t + \frac {1}{2}\right) \mathrm {e} ^ {- 2 t} \right]. \\ \end{array}</equation>因此，<equation>S (\ln 2) = - \frac {1}{2} \left[ \left(2 \ln 2 + \frac {1}{2}\right) \cdot \frac {1}{1 6} - \left(\ln 2 + \frac {1}{2}\right) \cdot \frac {1}{4} \right] = \frac {\ln 2}{1 6} + \frac {3}{6 4}.</equation>

---

**2023年第18题 | 解答题 | 12分**

8. (本题满分12分)

已知平面区域<equation>D=\left\{(x,y)\left|0\leqslant y\leqslant \frac{1}{x\sqrt{1+x^{2}}},x\geqslant 1\right.\right\}</equation>I. 求 D的面积;

II. 求 D绕 x轴旋转所成旋转体的体积.

**答案:**( I )<equation>\ln(\sqrt{2}+1)</equation>;

( II )<equation>\pi\left(1-\frac{\pi}{4}\right).</equation>

**解析:**（I）区域 D是由曲线<equation>y=\frac{1}{x\sqrt{1+x^{2}}}</equation>，直线 x=1以及 x轴围成的无界区域，其面积为<equation>\begin{aligned} S &= \int_ {1} ^ {+ \infty} \frac {1}{x \sqrt {1 + x ^ {2}}} \mathrm {d} x \xlongequal {x = \tan t} \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (\tan t)}{\tan t \sqrt {1 + \tan^ {2} t}} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\sec^ {2} t}{\tan t \sec t} \mathrm {d} t \\ &= \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} t}{\sin t} = \int_ {\frac {\pi}{4}} ^ {\frac {\pi}{2}} \frac {\mathrm {d} (- \cos t)}{1 - \cos^ {2} t} \xlongequal {u = \cos t} \int_ {\frac {\sqrt {2}}{2}} ^ {0} \frac {- \mathrm {d} u}{1 - u ^ {2}} = \frac {1}{2} \int_ {0} ^ {\frac {\sqrt {2}}{2}} \left(\frac {1}{1 - u} + \frac {1}{1 + u}\right) \mathrm {d} u \\ &= \frac {1}{2} \ln \frac {1 + u}{1 - u} \Bigg | _ {0} ^ {\frac {\sqrt {2}}{2}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>（Ⅱ）由旋转体的体积公式可知，区域 D绕 x轴旋转所成旋转体的体积为<equation>\begin{aligned} V &= \int_ {1} ^ {+ \infty} \pi \left(\frac {1}{x \sqrt {1 + x ^ {2}}}\right) ^ {2} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \frac {1}{x ^ {2} \left(1 + x ^ {2}\right)} \mathrm {d} x = \pi \int_ {1} ^ {+ \infty} \left(\frac {1}{x ^ {2}} - \frac {1}{1 + x ^ {2}}\right) \mathrm {d} x \\ &= \pi \left(- \frac {1}{x} - \arctan x\right) \Bigg | _ {1} ^ {+ \infty} = \pi \left(1 - \frac {\pi}{4}\right). \end{aligned}</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 设平面区域 D 由曲线<equation>y=\sqrt{x}\sin\pi x(0\leqslant x\leqslant1)</equation>与 x轴围成，则 D绕 x轴旋转所成的旋转体的体积为 ___.

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**（法一）根据旋转体的体积公式，<equation>\begin{array}{l} V = \pi \int_ {0} ^ {1} (\sqrt {x} \sin \pi x) ^ {2} \mathrm {d} x = \pi \int_ {0} ^ {1} x \sin^ {2} \pi x \mathrm {d} x \xlongequal {\pi x = t} \frac {1}{\pi} \int_ {0} ^ {\pi} t \sin^ {2} t \mathrm {d} t = \frac {1}{\pi} \cdot \frac {\pi}{2} \int_ {0} ^ {\pi} \sin^ {2} t \mathrm {d} t \\ = \frac {1}{2} \cdot 2 \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm {d} t = \frac {\pi}{4}. \\ \end{array}</equation>（法二）下面用另一种方法计算<equation>\int_{0}^{\pi} t\sin^{2}t\mathrm{d}t.</equation><equation>\begin{array}{l} \int_ {0} ^ {\pi} t \sin^ {2} t \mathrm {d} t = \int_ {0} ^ {\pi} t \cdot \frac {1 - \cos 2 t}{2} \mathrm {d} t = \frac {1}{2} \int_ {0} ^ {\pi} (t - t \cos 2 t) \mathrm {d} t = \frac {1}{2} \left(\frac {t ^ {2}}{2} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} t \cos 2 t \mathrm {d} t\right) \\ = \frac {1}{2} \left[ \frac {\pi^ {2}}{2} - \frac {1}{2} \int_ {0} ^ {\pi} t \mathrm {d} (\sin 2 t) \right] = \frac {\pi^ {2}}{4} - \frac {1}{4} \left(t \sin 2 t \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \sin 2 t \mathrm {d} t\right) \\ = \frac {\pi^ {2}}{4} - \frac {1}{4} \left(0 + \frac {\cos 2 t}{2} \Big | _ {0} ^ {\pi}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}</equation>

---

**2020年第12题 | 填空题 | 4分**

12. 设平面区域<equation>D=\left\{(x,y)\left| \frac{x}{2}\leqslant y\leqslant \frac{1}{1+x^{2}},0\leqslant x\leqslant 1\right. \right\}</equation>，则 D绕 y轴旋转所成的旋转体的体积为 ___.

**答案:**<equation>\pi \ln 2 - \frac {\pi}{3}.</equation>

**解析:**解 由已知条件可知，区域 D由曲线<equation>y=\frac{1}{1+x^{2}},y=\frac{x}{2},x=0,x=1</equation>围成，其绕 y轴旋转一周所得旋转体的体积可看作两个旋转体的体积之差.

由旋转体的体积公式可得，所求旋转体的体积<equation>\begin{array}{l} V = 2 \pi \int_ {0} ^ {1} x \left(\frac {1}{1 + x ^ {2}} - \frac {x}{2}\right) \mathrm {d} x = 2 \pi \int_ {0} ^ {1} \left(\frac {x}{1 + x ^ {2}} - \frac {x ^ {2}}{2}\right) \mathrm {d} x \\ = 2 \pi \left[ \frac {1}{2} \ln \left(1 + x ^ {2}\right) - \frac {x ^ {3}}{6} \right] \Bigg | _ {0} ^ {1} = \pi \ln 2 - \frac {\pi}{3}. \\ \end{array}</equation>

---

**2019年第18题 | 解答题 | 10分**

18. (本题满分10分)

求曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与x轴之间图形的面积.

**答案:**<equation>\frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>

**解析:**如图所示，曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与 x轴有无穷多个交点，<equation>x=n\pi</equation>（n为非负整数）均为曲线与 x轴的交点. 因此，该曲线与 x轴围成的平面图形在 x轴上方与 x轴下方均有无穷多部分. 计算面积时，应分别计算该平面图形位于 x轴上方部分的面积与位于 x轴下方部分的面积，再求级数和.

解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于（<equation>k\pi</equation>，<equation>( k+1)\pi</equation>）的部分与 x轴之间的图形面积等于<equation>\int_{k\pi}^{(k+1)\pi} \mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{array}{l} S _ {n} = \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \underline {{= x - k \pi}} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ = \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \\ \end{array}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\mathrm{e}^{-\pi}+1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t=\frac{1}{2}\left(\mathrm{e}^{-\pi}+1\right).</equation><equation>S = \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.当<equation>x\in(2n\pi,(2n+1)\pi)</equation>时，<equation>\sin x > 0</equation>；当<equation>x\in((2n+1)\pi,</equation><equation>(2n+2)\pi)</equation>时，<equation>\sin x < 0</equation>因此，根据定积分的几何意义，曲线位于<equation>(2n\pi, (2n+1)\pi)</equation>的部分与x轴之间的图形面积等于<equation>\int_{2n\pi}^{(2n+1)\pi} \mathrm{e}^{-x}\sin x\mathrm{d}x</equation>；曲线位于<equation>((2n+1)\pi, (2n+2)\pi)</equation>的部分与x轴之间的图形面积等于<equation>-\int_{(2n+1)\pi}^{(2n+2)\pi} \mathrm{e}^{-x}\sin x\mathrm{d}x.</equation>记所求面积为 S，则<equation>S = \sum_ {n = 0} ^ {\infty} \int_ {2 n \pi} ^ {(2 n + 1) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x - \sum_ {n = 0} ^ {\infty} \int_ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x.</equation>下面计算<equation>\int\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2\int \mathrm{e}^{-x}\sin x\mathrm{d}x = -\mathrm{e}^{-x}(\sin x + \cos x) - C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} (\sin x + \cos x) + C \right],</equation>其中 C为任意常数.

因此，<equation>\begin{array}{l} S = \sum_ {n = 0} ^ {\infty} \left[ - \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \left| _ {2 n \pi} ^ {(2 n + 1) \pi} + \sum_ {n = 0} ^ {\infty} \left[ \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \right| _ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \\ = \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 1) \pi} + \mathrm {e} ^ {- 2 n \pi} \right] + \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 2) \pi} + \mathrm {e} ^ {- (2 n + 1) \pi} \right] \\ = \frac {1}{2} \left[ \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} + 2 \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- (2 n + 1) \pi} + \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} \right] \\ = \frac {1}{2} \left(\frac {1}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {2 \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {\mathrm {e} ^ {- 2 \pi}}{1 - \mathrm {e} ^ {- 2 \pi}}\right) = \frac {1}{2} \cdot \frac {\left(1 + \mathrm {e} ^ {- \pi}\right) ^ {2}}{\left(1 + \mathrm {e} ^ {- \pi}\right) \left(1 - \mathrm {e} ^ {- \pi}\right)} \\ = \frac {1}{2} \cdot \frac {1 + \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \\ \end{array}</equation>

---

**2013年第16题 | 解答题 | 10分**

16. (本题满分10分)

设 D是由曲线<equation>y=x^{\frac{1}{3}}</equation>，直线 x=a（a>0）及 x轴所围成的平面图形，<equation>V_{x}</equation>和<equation>V_{y}</equation>分别是 D绕 x轴，y轴旋转一周所得旋转体的体积.若<equation>V_{y}=1 0 V_{x}</equation>，求 a的值.

**答案:**(16)<equation>a=7\sqrt{7}.</equation>

**解析:**解（法一）<equation>D</equation>绕<equation>x</equation>轴旋转所得的旋转体的体积<equation>V_{x}</equation>为<equation>V _ {x} = \pi \int_ {0} ^ {a} \left(x ^ {\frac {1}{3}}\right) ^ {2} \mathrm {d} x = \frac {3 \pi}{5} x ^ {\frac {5}{3}} \Bigg | _ {0} ^ {a} = \frac {3 \pi}{5} a ^ {\frac {5}{3}}.</equation><equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为<equation>V _ {y} = 2 \pi \int_ {0} ^ {a} x \cdot x ^ {\frac {1}{3}} \mathrm {d} x = 2 \pi \cdot \frac {3}{7} a ^ {\frac {7}{3}} = \frac {6 \pi}{7} a ^ {\frac {7}{3}}.</equation>由于<equation>V_{y}=1 0 V_{x}</equation>，故<equation>\frac{6\pi}{7} a^{\frac{7}{3}}=1 0\cdot \frac{3\pi}{5} a^{\frac{5}{3}}.</equation>整理得<equation>a ^ {\frac {5}{3}} \left(6 \pi - \frac {6 \pi}{7} a ^ {\frac {2}{3}}\right) = 0.</equation>因此，<equation>a = 0</equation>或<equation>a^{\frac{2}{3}} = 7.</equation>由题设知，<equation>a > 0</equation>，故<equation>a^{\frac{2}{3}} = 7</equation>，即<equation>a = 7\sqrt{7}.</equation>（法二）<equation>D</equation>绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}</equation>为底面半径为<equation>a</equation>，高为<equation>a^{\frac{1}{3}}</equation>的圆柱体体积减去<equation>D^{\prime}</equation>（如图，由曲线<equation>y = x^{\frac{1}{3}}</equation>，直线<equation>y = a^{\frac{1}{3}}</equation>与<equation>y</equation>轴围成）绕<equation>y</equation>轴旋转所得旋转体的体积<equation>V_{y}^{\prime}</equation>圆柱体的体积<equation>V = \pi a^{2}\cdot a^{\frac{1}{3}} = \pi a^{\frac{7}{3}}.</equation><equation>V _ {y} ^ {\prime} = \pi \int_ {0} ^ {a ^ {\frac {1}{3}}} \left(y ^ {3}\right) ^ {2} \mathrm {d} y = \frac {\pi}{7} y ^ {7} \left| _ {0} ^ {a ^ {\frac {1}{3}}} = \frac {\pi}{7} a ^ {\frac {7}{3}}. \right.</equation>因此，<equation>V_{y} = \pi a^{\frac{7}{3}} - \frac{\pi}{7} a^{\frac{7}{3}} = \frac{6\pi}{7} a^{\frac{7}{3}}.</equation>其余同法一.

---

**2011年第12题 | 填空题 | 4分**

12. 曲线<equation>y=\sqrt{x^{2}-1}</equation>, 直线<equation>x=2</equation>及<equation>x</equation>轴所围的平面图形绕<equation>x</equation>轴旋转所成的旋转体的体积为 ___.

**解析:**解如图所示，联立方程<equation>\left\{\begin{array}{l l}y=\sqrt{x^{2}-1}\\ x=2,\end{array}\right.</equation>可解得曲线<equation>y=\sqrt{x^{2}-1}</equation>与直线<equation>x=2</equation>的交点为（2，<equation>\sqrt{3}</equation>）由旋转体的体积公式知所求体积为<equation>V = \pi \int_ {1} ^ {2} y ^ {2} (x) \mathrm {d} x = \pi \int_ {1} ^ {2} \left(x ^ {2} - 1\right) \mathrm {d} x = \pi \left(\frac {x ^ {3}}{3} - x\right) \Big | _ {1} ^ {2} = \frac {4}{3} \pi .</equation>

---

**2010年第10题 | 填空题 | 4分**

10. 设位于曲线<equation>y=\frac{1}{\sqrt{x(1+\ln^{2}x)}}</equation>（<equation>\mathrm{e}\leqslant x<+\infty</equation>）下方，x轴上方的无界区域为 G，则 G绕 x轴旋转一周所得空间区域的体积为 ___

**答案:**#<equation>\frac{\pi^{2}}{4}.</equation>

**解析:**解 由曲线表达式可知，<equation>y</equation>是关于<equation>x</equation>的单调减少函数且<equation>\lim_{x\to +\infty}y(x) = 0.</equation>由旋转体的体积公式知G绕<equation>x</equation>轴旋转一周所得空间区域的体积<equation>\begin{array}{l} V = \pi \int_ {\mathrm {e}} ^ {+ \infty} \left[ \frac {1}{\sqrt {x \left(1 + \ln^ {2} x\right)}} \right] ^ {2} \mathrm {d} x = \pi \int_ {\mathrm {e}} ^ {+ \infty} \frac {1}{x \left(1 + \ln^ {2} x\right)} \mathrm {d} x \\ = \pi \int_ {\mathrm {e}} ^ {+ \infty} \frac {\mathrm {d} (\ln x)}{1 + \ln^ {2} x} = \pi \arctan (\ln x) \Big | _ {\mathrm {e}} ^ {+ \infty} = \pi \left(\frac {\pi}{2} - \frac {\pi}{4}\right) = \frac {\pi^ {2}}{4}. \\ \end{array}</equation>

---

**2009年第19题 | 解答题 | 10分**

19. (本题满分10分)

设曲线 y=f(x)，其中 f(x)是可导函数，且 f(x)>0.已知曲线 y=f(x)与直线 y=0,x=1及 x=t(t>1)所围成的曲边梯形绕 x轴旋转一周所得的立体体积值是该曲边梯形面积值的<equation>\pi t</equation>倍，求该曲线的方程.

**答案:**(19)<equation>x=\frac{1}{3\sqrt{y}}+\frac{2}{3} y,x\geqslant 1.</equation>

**解析:**解 由旋转体的体积公式知曲边梯形绕 x轴旋转一周所得的立体体积<equation>V=\pi \int_{1}^{t}[f(x)]^{2}\mathrm{d}x.</equation>由定积分的几何意义知曲边梯形的面积<equation>S=\int_{1}^{t}f(x)\mathrm{d}x.</equation>由已知条件知<equation>V=\pi t S</equation>，故对任意的 t > 1，都有<equation>\pi \int_{1}^{t}[f(x)]^{2}\mathrm{d}x=\pi t\int_{1}^{t}f(x)\mathrm{d}x.</equation><equation>\pi \int_ {1} ^ {t} [ f (x) ] ^ {2} \mathrm {d} x = \pi t \int_ {1} ^ {t} f (x) \mathrm {d} x.</equation>上式两端消去<equation>\pi</equation>后并关于<equation>t</equation>求导得，<equation>[ f (t) ] ^ {2} = \int_ {1} ^ {t} f (x) \mathrm {d} x + t f (t).</equation>继续对上式两端关于 t求导得，<equation>2 f (t) f ^ {\prime} (t) = 2 f (t) + t f ^ {\prime} (t).</equation>令<equation>y=f(t)</equation>，得<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {2 y}{2 y - t}.</equation>下面用两种方法解方程<equation>\frac{\mathrm{d}y}{\mathrm{d}t}=\frac{2y}{2y-t}.</equation>（法一）由<equation>\frac{\mathrm{d}y}{\mathrm{d}t} = \frac{2y}{2y - t}</equation>可得<equation>\frac{\mathrm{d}t}{\mathrm{d}y} + \frac{1}{2y} t = 1.</equation>此为一阶非齐次线性微分方程，其通解为<equation>t = \mathrm {e} ^ {- \int \frac {1}{2 y} \mathrm {d} y} \left(\int \mathrm {e} ^ {\int \frac {1}{2 y} \mathrm {d} y} \mathrm {d} y + C\right) = y ^ {- \frac {1}{2}} \left(\frac {2}{3} y ^ {\frac {3}{2}} + C\right) = C y ^ {- \frac {1}{2}} + \frac {2}{3} y.</equation>由（1）式可得<equation>[ f(1)]^{2}=f(1)</equation>，于是<equation>f(1)=1</equation>（舍去<equation>f(1)=0 )</equation>.代入上式解得<equation>C=\frac{1}{3}</equation>，即<equation>t=\frac{1}{3\sqrt{y}}+\frac{2}{3} y</equation>因此，所求曲线方程为<equation>x = \frac {1}{3 \sqrt {y}} + \frac {2}{3} y, \quad x \geqslant 1.</equation>（法二）此为齐次微分方程.令<equation>u=\frac{y}{t}</equation>，则<equation>y=ut,\frac{\mathrm{d}y}{\mathrm{d}t}=u+t\frac{\mathrm{d}u}{\mathrm{d}t}</equation>，从而<equation>u+t\frac{\mathrm{d}u}{\mathrm{d}t}=\frac{\mathrm{d}y}{\mathrm{d}t}=\frac{2y}{2y-t}=\frac{2u}{2u-1}.</equation>整理得<equation>\frac {2 u - 1}{3 u - 2 u ^ {2}} \mathrm {d} u = \frac {\mathrm {d} t}{t}.</equation>对上式两端积分得，<equation>\int \frac {2 u - 1}{3 u - 2 u ^ {2}} \mathrm {d} u = \int \left(- \frac {1}{3 u} + \frac {4}{3} \cdot \frac {1}{3 - 2 u}\right) \mathrm {d} u = \int \frac {\mathrm {d} t}{t}.</equation>由于 y > 0，t > 1，故 u > 0，从而<equation>-\frac{1}{3}\ln u-\frac{2}{3}\ln |3-2u|=\ln t+C_{1}</equation>，其中<equation>C_{1}</equation>为常数，即<equation>[ u (3 - 2 u) ^ {2} ] ^ {- \frac {1}{3}} = C t, \quad C = \mathrm {e} ^ {C _ {1}}.</equation>同法一可得<equation>f ( 1 )=1.</equation>于是<equation>u ( 1 )=\frac{f ( 1 )}{1}=1.</equation>代入（2）式解得<equation>C=1.</equation>将<equation>u=\frac{y}{t}</equation>代入（2）式化简得到<equation>y(3t-2y)^{2}=1</equation>，从而<equation>t=\frac{1}{3}\left(\pm \frac{1}{\sqrt{y}}+2y\right).</equation>由于<equation>y(1)=1</equation>，故<equation>t=\frac{1}{3}\left(\frac{1}{\sqrt{y}}+2y\right)</equation>即所求曲线方程为<equation>x=\frac{1}{3\sqrt{y}}+\frac{2}{3}y,x\geqslant 1.</equation>

---


#### 不定积分的计算

**2023年第2题 | 选择题 | 5分 | 答案: D**

2. 函数 f(x) =<equation>\left\{\begin{array}{l l}{\frac{1}{\sqrt{1+x^{2}}},}&{x\leqslant0,}\\ {(x+1)\cos x,}&{x>0}\end{array} \right.</equation>的一个原函数为（    )

A. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x),}&{x\leqslant0,}\\ {(x+1)\cos x-\sin x,}&{x>0.}\end{array} \right.</equation>B. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}-x)+1,}&{x\leqslant0,}\\ {(x+1)\cos x-\sin x,}&{x>0.}\end{array} \right.</equation>C. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x),}&{x\leqslant0,}\\ {(x+1)\sin x+\cos x,}&{x>0.}\end{array} \right.</equation>D. F(x) =<equation>\left\{\begin{array}{l l}{\ln(\sqrt{1+x^{2}}+x)+1,}&{x\leqslant0,}\\ {(x+1)\sin x+\cos x,}&{x>0.}\end{array} \right.</equation>

答案: D

**解析:**解（法一）首先，由于 F(x）是 f(x)的原函数，故必连续，而四个选项中的 F(x)均为分段函数，于是我们可以分别考察 F(x)在分界点处的连续性.

对选项 A,<equation>\lim_{x\rightarrow 0^{-}}F(x)=0, \lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项B，<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

对选项 C<equation>\lim_{x\rightarrow 0^{-}}F(x)=0,\lim_{x\rightarrow 0^{+}}F(x)=1. F(x)</equation>不连续.

对选项 D<equation>\lim_{x\to 0^{-}}F(x)=\lim_{x\to 0^{+}}F(x)=1=F(0).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.<equation>[ (x + 1) \cos x - \sin x ] ^ {\prime} = \cos x - (x + 1) \sin x - \cos x = - (x + 1) \sin x,</equation><equation>[ (x + 1) \sin x + \cos x ] ^ {\prime} = \sin x + (x + 1) \cos x - \sin x = (x + 1) \cos x.</equation>由上可排除选项B.

因此，应选D.

（法二）当<equation>x\leqslant0</equation>时，<equation>\begin{array}{l} F (x) = \int \frac {\mathrm {d} x}{\sqrt {1 + x ^ {2}}} \xlongequal {x = \tan \theta} \int \frac {\sec^ {2} \theta}{\sec \theta} \mathrm {d} \theta = \int \sec \theta \mathrm {d} \theta = \ln | \sec \theta + \tan \theta | + C _ {1} \\ \underline {{\frac {x = \tan \theta}{2}}} \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1}. \\ \end{array}</equation>当 x > 0时，<equation>\begin{aligned} F (x) &= \int (x + 1) \cos x \mathrm {d} x = \int (x + 1) \mathrm {d} (\sin x) = (x + 1) \sin x - \int \sin x \mathrm {d} x \\ &= (x + 1) \sin x + \cos x + C _ {2}. \end{aligned}</equation>四个选项中，仅有选项C、D符合要求.

由于 F(x）是 f(x)在<equation>(-\infty, +\infty)</equation>上的一个原函数，故 F(x)在 x=0处连续.<equation>\lim _ {x \rightarrow 0 ^ {-}} F (x) = \lim _ {x \rightarrow 0 ^ {-}} \left[ \ln \left(\sqrt {1 + x ^ {2}} + x\right) + C _ {1} \right] = C _ {1},</equation><equation>\lim _ {x \rightarrow 0 ^ {+}} F (x) = \lim _ {x \rightarrow 0 ^ {+}} \left[ (x + 1) \sin x + \cos x + C _ {2} \right] = C _ {2} + 1.</equation>由<equation>\lim_{x\to 0^{-}}F(x) = \lim_{x\to 0^{+}}F(x)</equation>可得<equation>C_1 = C_2 + 1.</equation>选项C中，<equation>C_{1}=C_{2}=0,F(x)</equation>不连续，选项D中，<equation>C_{1}=1,C_{2}=0,F(x)</equation>连续，应选D.

---

**2018年第10题 | 填空题 | 4分**

**答案:**<equation>\mathrm{e}^{x}\arcsin \sqrt{1 - \mathrm{e}^{2x}} -\sqrt{1 - \mathrm{e}^{2x}} +C</equation>，其中C为任意常数.

**解析:**解 （法一）利用分部积分法.<equation>\begin{array}{l} \int \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} x \xlongequal {\text {分 部 积 分}} \int \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \int \mathrm {e} ^ {x} \cdot \frac {1}{\sqrt {1 - 1 + \mathrm {e} ^ {2 x}}} \cdot \frac {- 2 \mathrm {e} ^ {2 x}}{2 \sqrt {1 - \mathrm {e} ^ {2 x}}} \mathrm {d} x \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} + \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {1 - \mathrm {e} ^ {2 x}}} \mathrm {d} x \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \frac {1}{2} \int \frac {\mathrm {d} \left(1 - \mathrm {e} ^ {2 x}\right)}{\sqrt {1 - \mathrm {e} ^ {2 x}}} \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C, \\ \end{array}</equation>其中 C为任意常数.

（法二）利用第二类换元法.

令<equation>\mathrm{e}^{x}=\cos t, t\in\left[0,\frac{\pi}{2}\right)</equation>，则<equation>\sqrt{1-\mathrm{e}^{2x}}=\sin t, t=\arcsin \sqrt{1-\mathrm{e}^{2x}},\mathrm{e}^{x}\mathrm{d}x=-\sin t\mathrm{d}t.</equation>因此，<equation>\begin{array}{l} \int \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} \mathrm {d} x = \int t \cdot (- \sin t) \mathrm {d} t = \int t \mathrm {d} (\cos t) = t \cos t - \int \cos t \mathrm {d} t \\ = t \cos t - \sin t + C = \mathrm {e} ^ {x} \arccos \mathrm {e} ^ {x} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C \\ = \mathrm {e} ^ {x} \arcsin \sqrt {1 - \mathrm {e} ^ {2 x}} - \sqrt {1 - \mathrm {e} ^ {2 x}} + C, \\ \end{array}</equation>其中 C为任意常数.

---

**2011年第17题 | 解答题 | 10分**

17. (本题满分10分)

求不定积分

**答案:**(17)<equation>2 \sqrt{x} \arcsin \sqrt{x}+2 \sqrt{x} \ln x+2 \sqrt{1-x}-4 \sqrt{x}+C</equation>，其中C为任意常数.

**解析:**解 （法一）利用换元法和分部积分法.

令<equation>\sqrt{x} = t</equation>，则<equation>x = t^{2}</equation>，<equation>t > 0</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation>于是，<equation>\begin{array}{l} \int \frac {\arcsin \sqrt {x} + \ln x}{\sqrt {x}} \mathrm {d} x = \int \frac {\arcsin t + \ln t ^ {2}}{t} \cdot 2 t \mathrm {d} t = 2 \int \left(\arcsin t + \ln t ^ {2}\right) \mathrm {d} t \\ \underline {{\mathrm {分 部 积 分}}} = 2 \left[ \left(\arcsin t + \ln t ^ {2}\right) t - \int \left(\frac {1}{\sqrt {1 - t ^ {2}}} + \frac {2 t}{t ^ {2}}\right) t \mathrm {d} t \right] \\ = 2 \left(\arcsin t + \ln t ^ {2}\right) t + \int \frac {\mathrm {d} \left(1 - t ^ {2}\right)}{\sqrt {1 - t ^ {2}}} - \int 4 \mathrm {d} t \\ = 2 \left(\arcsin t + \ln t ^ {2}\right) t + 2 \sqrt {1 - t ^ {2}} - 4 t + C, \\ \end{array}</equation>其中 C为任意常数.

将<equation>t=\sqrt{x}</equation>代回，可得<equation>\text {原 积 分} = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x + 2 \sqrt {1 - x} - 4 \sqrt {x} + C,</equation>其中 C为任意常数.

（法二）分部积分法.<equation>\begin{array}{l} \int \frac {\arcsin \sqrt {x} + \ln x}{\sqrt {x}} \mathrm {d} x = 2 \int (\arcsin \sqrt {x} + \ln x) \mathrm {d} (\sqrt {x}) \\ \underline {{\mathrm {分 部 积 分}}} = 2 \left[ \left(\arcsin \sqrt {x} + \ln x\right) \sqrt {x} - \int \sqrt {x} \left(\frac {\frac {1}{2} x ^ {- \frac {1}{2}}}{\sqrt {1 - x}} + \frac {1}{x}\right) \mathrm {d} x \right] \\ = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x - \int \left(\frac {1}{\sqrt {1 - x}} + \frac {2}{\sqrt {x}}\right) \mathrm {d} x \\ = 2 \sqrt {x} \arcsin \sqrt {x} + 2 \sqrt {x} \ln x + 2 \sqrt {1 - x} - 4 \sqrt {x} + C, \\ \end{array}</equation>其中 C为任意常数.

---

**2009年第16题 | 解答题 | 10分**

16. (本题满分10分)

计算不定积分<equation>\int\ln\left(1+\sqrt{\frac{1+x}{x}}\right)\mathrm{d}x(x>0).</equation>

**答案:**(16)<equation>x \ln \left( 1+\sqrt{\frac{1+x}{x}} \right)+\frac{1}{2} \ln \left( \sqrt{1+x}+\sqrt{x} \right)-\frac{\sqrt{x}}{2\left( \sqrt{1+x}+\sqrt{x} \right)}-C</equation>，其中C为任意常数.

**解析:**解（法一）令<equation>u=\sqrt{\frac{1+x}{x}}</equation>，则<equation>x=\frac{1}{u^{2}-1}.</equation>于是，<equation>\int \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right) \mathrm {d} x = \int \ln (1 + u) \mathrm {d} \left(\frac {1}{u ^ {2} - 1}\right) = \frac {\ln (1 + u)}{u ^ {2} - 1} - \int \frac {1}{\left(u ^ {2} - 1\right) \left(u + 1\right)} \mathrm {d} u.</equation>计算<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \int \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u &= \frac {1}{2} \int \frac {(u + 1) - (u - 1)}{\left(u ^ {2} - 1\right) (u + 1)} \mathrm {d} u = \frac {1}{2} \left[ \int \frac {1}{u ^ {2} - 1} \mathrm {d} u - \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u \right] \\ &= \frac {1}{4} \int \left(\frac {1}{u - 1} - \frac {1}{u + 1}\right) \mathrm {d} u - \frac {1}{2} \int \frac {1}{(u + 1) ^ {2}} \mathrm {d} u = \frac {1}{4} \ln \frac {u - 1}{u + 1} + \frac {1}{2 (u + 1)} + C, \end{aligned}</equation>其中 C为任意常数.这里的<equation>\ln \frac{u-1}{u+1}</equation>没有绝对值符号，是因为<equation>u=\sqrt{\frac{1+x}{x}}>1.</equation>将 u =<equation>\sqrt{\frac{1+x}{x}}</equation>代回原积分，得<equation>\begin{aligned} \mathrm {原 积 分} &= \frac {\ln (1 + u)}{u ^ {2} - 1} + \frac {1}{4} \ln \frac {u + 1}{u - 1} - \frac {1}{2 (u + 1)} - C \\ \frac {u = \sqrt {\frac {1 + x}{x}}}{x \ln \left(1 + \sqrt {\frac {1 + x}{x}}\right)} + \frac {1}{2} \ln \left(\sqrt {1 + x} + \sqrt {x}\right) - \frac {\sqrt {x}}{2 \left(\sqrt {1 + x} + \sqrt {x}\right)} - C, \end{aligned}</equation>其中 C为任意常数.

（法二）使用待定系数法来求<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u.</equation><equation>\begin{aligned} \frac {1}{\left(u ^ {2} - 1\right) (u + 1)} &= \frac {a}{u - 1} + \frac {b}{u + 1} + \frac {c}{(u + 1) ^ {2}} = \frac {a (u + 1) ^ {2} + b (u - 1) (u + 1) + c (u - 1)}{(u - 1) (u + 1) ^ {2}} \\ &= \frac {(a + b) u ^ {2} + (2 a + c) u + a - b - c}{(u - 1) (u + 1) ^ {2}}. \end{aligned}</equation>比较<equation>u^{2}</equation>，<equation>u</equation>的系数以及常数项，可得<equation>\left\{ \begin{array}{l l} a + b = 0, \\ 2a + c = 0, \\ a - b - c = 1, \end{array} \right.</equation>解得<equation>a = \frac{1}{4}, b = -\frac{1}{4}, c = -\frac{1}{2}</equation>.

因此，<equation>\int \frac{1}{(u^{2}-1)(u+1)} \mathrm{d} u=\frac{1}{4} \int \left[ \frac{1}{u-1}-\frac{1}{u+1}-\frac{2}{(u+1)^{2}} \right] \mathrm{d} u=\frac{1}{4} \left( \ln \frac{u-1}{u+1}+\frac{2}{u+1} \right)+C</equation>其中C为任意常数.

其余同法一.

---

