#### 全微分的概念与计算

**2021年第2题 | 选择题 | 5分 | 答案: C**

2. 设函数 f(x,y)可微，且<equation>f \left( x+1, \mathrm{e}^{x} \right)=x \left( x+1 \right)^{2}, f \left( x, x^{2} \right)=2 x^{2} \ln x</equation>，则<equation>\mathrm{d} f \left( 1, 1 \right)=</equation>(    )

A.<equation>\mathrm{d} x+\mathrm{d} y</equation>B.<equation>\mathrm{d} x-\mathrm{d} y</equation>C.<equation>\mathrm{d} y</equation>D.<equation>-\mathrm{d} y</equation>

答案: C

**解析:**根据全微分的定义，<equation>\mathrm {d} f (1, 1) = f _ {1} ^ {\prime} (1, 1) \mathrm {d} x + f _ {2} ^ {\prime} (1, 1) \mathrm {d} y.</equation>对<equation>f(x + 1,\mathrm{e}^{x}) = x(x + 1)^{2},f(x,x^{2}) = 2x^{2}\ln x</equation>两端均关于<equation>x</equation>求导，可得<equation>f _ {1} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) + f _ {2} ^ {\prime} \left(x + 1, \mathrm {e} ^ {x}\right) \cdot \mathrm {e} ^ {x} = (x + 1) ^ {2} + x \cdot 2 (x + 1) = (x + 1) (3 x + 1).</equation><equation>f _ {1} ^ {\prime} \left(x, x ^ {2}\right) + f _ {2} ^ {\prime} \left(x, x ^ {2}\right) \cdot 2 x = 4 x \ln x + 2 x ^ {2} \cdot \frac {1}{x} = 2 x \left(2 \ln x + 1\right).</equation>在（1）式中令<equation>x=0</equation>，可得<equation>f_{1}^{\prime}(1,1)+f_{2}^{\prime}(1,1)=1.</equation>在（2）式中令<equation>x=1</equation>，可得<equation>f_{1}^{\prime}(1,1)+ 2 f_{2}^{\prime}(1,1)=2.</equation>联立两式解得<equation>f_{1}^{\prime}(1,1)=0,f_{2}^{\prime}(1,1)=1.</equation>因此，<equation>\mathrm{d}f(1,1)=\mathrm{d}y.</equation>应选C.

---

**2020年第3题 | 选择题 | 4分 | 答案: A**

3. 设函数 f(x,y)在点(0,0)处可微，<equation>f(0,0)=0,\boldsymbol{n}=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},-1\right)\bigg|_{(0,0)},</equation>非零向量<equation>\alpha</equation>与n垂直，则（    )

A.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\boldsymbol{n}\cdot(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

B.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\boldsymbol{n}\times(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

C.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\alpha\cdot(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

D.<equation>\lim_{(x,y)\to(0,0)}\frac{\left|\alpha\times(x,y,f(x,y))\right|}{\sqrt{x^{2}+y^{2}}}</equation>存在

答案: A

**解析:**由函数<equation>f ( x,y )</equation>在点（0，0）处可微，且<equation>f ( 0,0 )=0</equation>可知，<equation>\begin{aligned} 0 &= \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f (0 , 0) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} \\ \underline {{f (0 , 0) = 0}} \lim _ {(x, y) \rightarrow (0, 0)} \frac {f (x , y) - f _ {x} ^ {\prime} (0 , 0) x - f _ {y} ^ {\prime} (0 , 0) y}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= - \lim _ {(x, y) \rightarrow (0, 0)} \frac {f _ {x} ^ {\prime} (0 , 0) x + f _ {y} ^ {\prime} (0 , 0) y - f (x , y)}{\sqrt {x ^ {2} + y ^ {2}}} \\ &= - \lim _ {(x, y) \rightarrow (0, 0)} \frac {\boldsymbol {n} \cdot (x , y , f (x , y))}{\sqrt {x ^ {2} + y ^ {2}}}. \end{aligned}</equation>因此，<equation>\lim_{(x,y)\to (0,0)}\frac{|\boldsymbol{n}\cdot(x,y,f(x,y))|}{\sqrt{x^2 + y^2}} = \lim_{(x,y)\to (0,0)}\frac{\boldsymbol{n}\cdot(x,y,f(x,y))}{\sqrt{x^2 + y^2}} = 0</equation>，应选A.

下面说明其余选项均不正确.<equation>\begin{array}{l} + y k, | n \times (x, y, x) | = \sqrt {4 x ^ {2} + 2 y ^ {2}}. \\ \end{array}</equation><equation>\lim _ {(x, y) \rightarrow (0, 0)} \frac {\left| \boldsymbol {n} \times (x , y , x) \right|}{\sqrt {x ^ {2} + y ^ {2}}} = \lim _ {(x, y) \rightarrow (0, 0)} \frac {\sqrt {4 x ^ {2} + 2 y ^ {2}}}{\sqrt {x ^ {2} + y ^ {2}}} = \lim _ {(x, y) \rightarrow (0, 0)} \sqrt {2 + \frac {2 x ^ {2}}{x ^ {2} + y ^ {2}}}.</equation>取<equation>y=x</equation>与<equation>y=\sqrt{3} x</equation>两条不同路径，可得沿这两条路径所得极限不一样，从而该二重极限不存在.

---

**2016年第11题 | 填空题 | 4分**

11. 设函数 f(u,v) 可微，z=z(x,y) 由方程<equation>( x+1 ) z-y^{2}=x^{2} f ( x-z,y )</equation>确定，则<equation>\mathrm{d} z |_{(0,1)}=</equation>___

**答案:**-<equation>\mathrm{d} x+2 \mathrm{d} y.</equation>

**解析:**解（法一）对已知方程两端分别关于<equation>x,y</equation>求偏导数，可得<equation>z + (x + 1) \frac {\partial z}{\partial x} = 2 x f (x - z, y) + x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(1 - \frac {\partial z}{\partial x}\right) \right].</equation><equation>(x + 1) \frac {\partial z}{\partial y} - 2 y = x ^ {2} \left[ f _ {1} ^ {\prime} (x - z, y) \cdot \left(- \frac {\partial z}{\partial y}\right) + f _ {2} ^ {\prime} (x - z, y) \right].</equation>将<equation>(x,y) = (0,1)</equation>代入已知方程，可得<equation>z - 1 = 0</equation>，从而<equation>z(0,1) = 1.</equation>再将<equation>(x,y,z) = (0,1,1)</equation>代入（1）、（2）两式，可得<equation>\frac{\partial z}{\partial x}\bigg|_{(0,1)} = -1,\frac{\partial z}{\partial y}\bigg|_{(0,1)} = 2.</equation>因此，<equation>\mathrm {d} z \mid_ {(0, 1)} = - \mathrm {d} x + 2 \mathrm {d} y.</equation>（法二）对已知方程两端微分，可得<equation>\mathrm{d}[ ( x + 1 ) z ] - \mathrm{d} ( y^{2} ) = \mathrm{d}[ x^{2} f ( x - z , y ) ]</equation>.进一步可得，<equation>\begin{aligned} (x + 1) \mathrm {d} z + z \mathrm {d} x - 2 y \mathrm {d} y &= f (x - z, y) \mathrm {d} \left(x ^ {2}\right) + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right] \\ &= 2 x f (x - z, y) \mathrm {d} x + x ^ {2} \mathrm {d} \left[ f (x - z, y) \right]. \end{aligned}</equation>将<equation>(x,y) = (0,1)</equation>代入已知方程，可得<equation>z - 1 = 0</equation>，从而<equation>z(0,1) = 1.</equation>代入上式可得<equation>\mathrm {d} z + \mathrm {d} x - 2 \mathrm {d} y = 0,</equation>即<equation>\mathrm{d}z\mid_{(0,1)} = -\mathrm{d}x + 2\mathrm{d}y.</equation>

---

**2015年第11题 | 填空题 | 4分**

11. 若函数<equation>z = z(x,y)</equation>由方程<equation>\mathrm{e}^{z} + xyz + x + \cos x = 2</equation>确定，则<equation>\mathrm{d}z|_{(0,1)} =</equation>___

**解析:**<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial y} + x z + x y \frac {\partial z}{\partial y} = 0.</equation>将<equation>( x,y)=(0,1)</equation>代入原方程，得到<equation>z ( 0,1 )=0.</equation>再将<equation>( x,y,z)=(0,1,0)</equation>代入方程（1）、（2），得到<equation>\left. \frac{\partial z}{\partial x}\right|_{(0,1)}=-1,\left. \frac{\partial z}{\partial y}\right|_{(0,1)}=0.</equation>于是<equation>\mathrm {d} z \mid_ {(0, 1)} = \frac {\partial z}{\partial x} \Big | _ {(0, 1)} \mathrm {d} x + \frac {\partial z}{\partial y} \Big | _ {(0, 1)} \mathrm {d} y = - \mathrm {d} x.</equation>（法二）对方程<equation>\mathrm{e}^{z}+xyz+x+\cos x=2</equation>两端微分，得到<equation>\mathrm {e} ^ {z} \mathrm {d} z + x y \mathrm {d} z + x z \mathrm {d} y + y z \mathrm {d} x + \mathrm {d} x - \sin x \mathrm {d} x = 0,</equation>整理得<equation>\left(\mathrm {e} ^ {z} + x y\right) \mathrm {d} z = (\sin x - 1 - y z) \mathrm {d} x - x z \mathrm {d} y.</equation>将<equation>(x,y) = (0,1)</equation>代入原方程，得到<equation>z(0,1) = 0</equation>，再代入上式得到<equation>\mathrm{d}z|_{(0,1)} = -\mathrm{d}x.</equation>## （法三）利用隐函数存在定理.

令<equation>F ( x,y,z) = \mathrm{e}^{z}+ x y z+x+\cos x-2.</equation>将（x,y）=（0,1）代入原方程，得到<equation>z ( 0,1 )=0</equation>从而<equation>F ( 0,1,0 )=0.</equation>又<equation>F _ {x} ^ {\prime} (x, y, z) = y z + 1 - \sin x, \quad F _ {y} ^ {\prime} (x, y, z) = x z, \quad F _ {z} ^ {\prime} (0, 1, 0) = \left(\mathrm {e} ^ {z} + x y\right) | _ {(0, 1, 0)} = 1 \neq 0,</equation>故由隐函数存在定理知，<equation>\left. \frac {\partial z}{\partial x} \right| _ {(0, 1)} = - \frac {F _ {x} ^ {\prime} (0 , 1 , 0)}{F _ {z} ^ {\prime} (0 , 1 , 0)} = - 1, \quad \left. \frac {\partial z}{\partial y} \right| _ {(0, 1)} = - \frac {F _ {y} ^ {\prime} (0 , 1 , 0)}{F _ {z} ^ {\prime} (0 , 1 , 0)} = 0,</equation>从而<equation>\mathrm{d}z\mid_{(0,1)} = \frac{\partial z}{\partial x}\bigg|_{(0,1)}\mathrm{d}x + \frac{\partial z}{\partial y}\bigg|_{(0,1)}\mathrm{d}y = -\mathrm{d}x.</equation>解（法一）对方程<equation>\mathrm{e}^{z}+xyz+x+\cos x=2</equation>两端分别关于 x,y求偏导数，得到<equation>\mathrm {e} ^ {z} \frac {\partial z}{\partial x} + y z + x y \frac {\partial z}{\partial x} + 1 - \sin x = 0,</equation>

---

**2012年第3题 | 选择题 | 4分 | 答案: B**

3. 如果函数 f(x,y)在点(0,0)处连续，那么下列命题正确的是（    )

A. 若极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{|x|+|y|}</equation>存在，则 f(x,y)在点(0,0)处可微

B. 若极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{x^{2}+y^{2}}</equation>存在，则 f(x,y)在点(0,0)处可微

C. 若 f(x,y)在点(0,0)处可微，则极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{|x|+|y|}</equation>存在

D. 若 f(x,y)在点(0,0)处可微，则极限<equation>\lim_{x\rightarrow 0}\frac{f(x,y)}{x^{2}+y^{2}}</equation>存在

答案: B

**解析:**解 对于选项A，取<equation>f ( x,y)=| x |+| y |</equation>，则<equation>f ( x,y)</equation>在点（0,0）处连续，且<equation>\lim_{x\to 0}\frac{f(x,y)}{|x|+|y|}=1</equation>但<equation>f ( x,y)</equation>在点（0,0）处的偏导数都不存在，故<equation>f ( x,y)</equation>在点（0,0）处不可微，从而选项A不正确.

对于选项C、D，取<equation>f ( x,y)\equiv 1</equation>，可知选项C、D不正确.

由排除法选B.下面证明选项B.

设<equation>\lim_{x\to 0}\frac{f(x,y)}{x^2 + y^2} = a</equation>，由于<equation>f(x,y)</equation>在（0,0）处连续，故<equation>f (0, 0) = \lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 0}} f (x, y) = \lim _ {\substack {x \rightarrow 0 \\ y \rightarrow 0}} \left[ \frac {f (x , y)}{x ^ {2} + y ^ {2}} \cdot \left(x ^ {2} + y ^ {2}\right)\right] = a \cdot 0 = 0,</equation>从而<equation>\lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \frac {f (\Delta x , \Delta y) - f (0 , 0)}{\sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}}} = \lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \left[ \frac {f (\Delta x , \Delta y)}{(\Delta x) ^ {2} + (\Delta y) ^ {2}} \cdot \sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}} \right] = a \lim _ {\Delta x \rightarrow 0 \atop \Delta y \rightarrow 0} \sqrt {(\Delta x) ^ {2} + (\Delta y) ^ {2}} = 0,</equation>即有<equation>f \left(\Delta x, \Delta y\right) - f (0, 0) = 0 \cdot \Delta x + 0 \cdot \Delta y + o \left(\sqrt {\left(\Delta x\right) ^ {2} + \left(\Delta y\right) ^ {2}}\right).</equation>由可微的定义知，<equation>f(x,y)</equation>在点（0,0）处可微.

---


### 一元函数积分学


