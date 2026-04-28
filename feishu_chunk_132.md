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


