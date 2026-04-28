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


#### 定积分的计算

**2025年第17题 | 解答题 | 10分**
17. 计算<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x.</equation>
**答案: **#<equation>\frac{3\ln 2+\pi}{10}.</equation>
**解析: **解设<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {A}{x + 1} + \frac {B x + C}{x ^ {2} - 2 x + 2}.</equation>通分并整理可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {(A + B) x ^ {2} + (B + C - 2 A) x + 2 A + C}{(x + 1) \left(x ^ {2} - 2 x + 2\right)}.</equation>比较<equation>x^{2}, x</equation>的系数以及常数项可得，<equation>A + B = 0,</equation><equation>\left\{B + C - 2 A = 0, \right.</equation><equation>2 A + C = 1.</equation>由（1）式可得 B=-A.将 B=-A 代入（2）式可得 C=3A.将 C=3A 代入（3）式可得 5A=1，即<equation>A=\frac{1}{5}.</equation>进一步可得 B=-<equation>\frac{1}{5},</equation>C<equation>=\frac{3}{5}.</equation>由此可得，<equation>\frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} = \frac {1}{5} \left(\frac {1}{x + 1} - \frac {x - 3}{x ^ {2} - 2 x + 2}\right).</equation>下面分别计算<equation>\int_{0}^{1}\frac{1}{x+1}\mathrm{d}x</equation>与<equation>\int_{0}^{1}\frac{x-3}{x^{2}-2x+2}\mathrm{d}x.</equation><equation>\int_ {0} ^ {1} \frac {1}{x + 1} \mathrm {d} x = \ln (x + 1) \Big | _ {0} ^ {1} = \ln 2.</equation><equation>\begin{aligned} \int_ {0} ^ {1} \frac {x - 3}{x ^ {2} - 2 x + 2} \mathrm {d} x &= \int_ {0} ^ {1} \frac {x - 1}{x ^ {2} - 2 x + 2} \mathrm {d} x - \int_ {0} ^ {1} \frac {2}{x ^ {2} - 2 x + 2} \mathrm {d} x \\ &= \frac {1}{2} \int_ {0} ^ {1} \frac {\mathrm {d} \left(x ^ {2} - 2 x + 2\right)}{x ^ {2} - 2 x + 2} - 2 \int_ {0} ^ {1} \frac {1}{1 + (x - 1) ^ {2}} \mathrm {d} x \\ &= \frac {1}{2} \ln \left(x ^ {2} - 2 x + 2\right) \left| _ {0} ^ {1} - 2 \arctan (x - 1) \right| _ {0} ^ {1} \\ &= - \frac {1}{2} \ln 2 - 2 [ 0 - \arctan (- 1) ] = - \frac {1}{2} \ln 2 - \frac {\pi}{2}. \end{aligned}</equation>因此，<equation>\int_ {0} ^ {1} \frac {1}{(x + 1) \left(x ^ {2} - 2 x + 2\right)} \mathrm {d} x = \frac {1}{5} \left[ \ln 2 - \left(- \frac {1}{2} \ln 2 - \frac {\pi}{2}\right) \right] = \frac {3 \ln 2 + \pi}{1 0}.</equation>

---

**2023年第14题 | 填空题 | 5分**
14. 设连续函数 f(x)满足<equation>f(x+2)-f(x)=x,\int_{0}^{2} f(x)\mathrm{d} x=0</equation>，则<equation>\int_{1}^{3} f(x)\mathrm{d} x=</equation>___
**解析: **解注意到<equation>\int_{2}^{3} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x</equation>，故由<equation>f(x+2)-f(x)=x</equation>可得，<equation>\int_{2}^{3} f(x)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} f(x+2)\mathrm{d}x-\int_{0}^{1} f(x)\mathrm{d}x=\int_{0}^{1} x\mathrm{d}x=\frac{1}{2}.</equation>(1)

又因为<equation>\int_{0}^{1} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\int_{0}^{2} f(x)\mathrm{d}x=0</equation>，所以<equation>-\int_{0}^{1} f(x)\mathrm{d}x=\int_{1}^{2} f(x)\mathrm{d}x.</equation>从而由（1）式可得<equation>\int_{2}^{3} f(x)\mathrm{d}x+\int_{1}^{2} f(x)\mathrm{d}x=\frac{1}{2},</equation>即<equation>\int_{1}^{3} f(x)\mathrm{d}x=\frac{1}{2}.</equation>

---

**2022年第12题 | 填空题 | 5分**
<equation>1 2. \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解（法一）利用根式代换.

令<equation>t = \sqrt{x}</equation>，则<equation>x = t^{2}</equation>，<equation>\mathrm{d}x = 2t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {1} ^ {e ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x \xlongequal {t = \sqrt {x}} \int_ {1} ^ {e} \frac {2 \ln t}{t} \cdot 2 t \mathrm {d} t &= 4 \int_ {1} ^ {e} \ln t \mathrm {d} t = 4 \left(t \ln t \Big | _ {1} ^ {e} - \int_ {1} ^ {e} t \cdot \frac {1}{t} \mathrm {d} t\right) \\ &= 4 \left[ \mathrm {e} - (\mathrm {e} - 1) \right] = 4. \end{aligned}</equation>（法二）利用分部积分法.<equation>\begin{aligned} \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {\ln x}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {1} ^ {\mathrm {e} ^ {2}} \ln x \mathrm {d} (\sqrt {x}) = 2 \left(\sqrt {x} \ln x \Big | _ {1} ^ {\mathrm {e} ^ {2}} - \int_ {1} ^ {\mathrm {e} ^ {2}} \sqrt {x} \cdot \frac {1}{x} \mathrm {d} x\right) = 2 \left(2 \mathrm {e} - \int_ {1} ^ {\mathrm {e} ^ {2}} \frac {1}{\sqrt {x}} \mathrm {d} x\right) \\ &= 4 \mathrm {e} - 4 \sqrt {x} \Big | _ {1} ^ {\mathrm {e} ^ {2}} = 4 \mathrm {e} - (4 \mathrm {e} - 4) = 4. \end{aligned}</equation>

---

**2015年第10题 | 填空题 | 4分**
10.<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \underline {{}}</equation>
**解析: **由于<equation>\frac{\sin x}{1 + \cos x}</equation>是奇函数，<equation>|x|</equation>是偶函数，故<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x = 0, \quad \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 2 \int_ {0} ^ {\frac {\pi}{2}} x \mathrm {d} x = \frac {\pi^ {2}}{4}.</equation>因此，<equation>\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(\frac {\sin x}{1 + \cos x} + | x |\right) \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {\sin x}{1 + \cos x} \mathrm {d} x + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} | x | \mathrm {d} x = 0 + \frac {\pi^ {2}}{4} = \frac {\pi^ {2}}{4}.</equation>

---

**2014年第4题 | 选择题 | 4分 | 答案: A**
4. 若<equation>\int_{-\pi}^{\pi} \left(x-a_{1}\cos x-b_{1}\sin x\right)^{2}\mathrm{d}x=\min_{a,b\in\mathbf{R}}\left\{\int_{-\pi}^{\pi}\left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x\right\}</equation>，则<equation>a_{1}\cos x+b_{1}\sin x=</equation>(    )

A. 2sinx B. 2cosx C. 2<equation>\pi\sin x</equation>D. 2<equation>\pi\cos x</equation>
答案: A
**解析: **解（法一）<equation>\begin{aligned} \int_ {- \pi} ^ {\pi} \left(x - a \cos x - b \sin x\right) ^ {2} \mathrm {d} x &= \int_ {- \pi} ^ {\pi} \left(x ^ {2} + a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 a x \cos x - 2 b x \sin x + 2 a b \sin x \cos x\right) \mathrm {d} x \\ \xlongequal {\text {对称性}} 2 \int_ {0} ^ {\pi} x ^ {2} \mathrm {d} x + 2 \int_ {0} ^ {\pi} \left(a ^ {2} \cos^ {2} x + b ^ {2} \sin^ {2} x - 2 b x \sin x\right) \mathrm {d} x \\ &= \frac {2}{3} \pi^ {3} + \left(a ^ {2} + b ^ {2} - 4 b\right) \pi . \end{aligned}</equation>当 a=0时，<equation>a^{2}</equation>最小；当 b=2时，<equation>b^{2}-4b</equation>最小，从而当 a=0，b=2时，<equation>\int_{- \pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>最小.因此<equation>a_{1}=0,b_{1}=2</equation>，从而<equation>a_{1}\cos x+b_{1}\sin x=2\sin x</equation>，应选A.

（法二）看作二元函数的最值问题求解.

令<equation>f ( a,b)=\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，则<equation>\frac {\partial f (a , b)}{\partial a} = \int_ {- \pi} ^ {\pi} \left[ - 2 (x - a \cos x - b \sin x) \cos x \right] \mathrm {d} x = 2 a \int_ {- \pi} ^ {\pi} \cos^ {2} x \mathrm {d} x = 2 a \pi ,</equation><equation>\frac {\partial f (a , b)}{\partial b} = \int_ {- \pi} ^ {\pi} \left[ - 2 \left(x - a \cos x - b \sin x\right) \sin x \right] \mathrm {d} x = 2 \int_ {- \pi} ^ {\pi} \left(b \sin^ {2} x - x \sin x\right) \mathrm {d} x = 2 \left(b \pi - 2 \pi\right).</equation>令<equation>\frac{\partial f(a,b)}{\partial a} = 0,\frac{\partial f(a,b)}{\partial b} = 0</equation>，解得<equation>a = 0,b = 2</equation>，从而<equation>a_1 = 0,b_1 = 2</equation>.应选A.

（法三）将选项A、B、C、D的值分别代入<equation>\int_{-\pi}^{\pi} \left(x-a\cos x-b\sin x\right)^{2}\mathrm{d}x</equation>，得到<equation>\int_ {- \pi} ^ {\pi} (x - 2 \sin x) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} - 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi ,</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \sin x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {2} (\pi - 2),</equation><equation>\int_ {- \pi} ^ {\pi} \left(x - 2 \pi \cos x\right) ^ {2} \mathrm {d} x = \frac {2}{3} \pi^ {3} + 4 \pi^ {3}.</equation>由于<equation>\frac{2}{3}\pi^{3}-4\pi<\frac{2}{3}\pi^{3}+4\pi<\frac{2}{3}\pi^{3}+4\pi^{2}(\pi-2)<\frac{2}{3}\pi^{3}+4\pi^{3}</equation>，故选A.

---

**2014年第10题 | 填空题 | 4分**
10. 设<equation>f(x)</equation>是周期为4的可导奇函数,且<equation>f^{\prime}(x)=2(x-1),x\in[0,2]</equation>,则<equation>f(7)=</equation>___.
**解析: **由于<equation>f ( x )</equation>是周期为4的函数，且<equation>7=2\times4-1</equation>，故<equation>f ( 7 ) = f (-1).</equation>(a)

(b)

（法一）由 f(x)为奇函数可得<equation>f(0)=0</equation>.由当<equation>x\in[0,2]</equation>时，<equation>f^{\prime}(x)=2(x-1)</equation>可得， f(x)在 [0,2]上的表达式为<equation>f (x) = \int_ {0} ^ {x} 2 (t - 1) \mathrm {d} t + f (0) = x ^ {2} - 2 x = (x - 1) ^ {2} - 1.</equation>于是<equation>f(1) = -1.</equation>由<equation>f(x)</equation>为奇函数得，<equation>f(-1) = -f(1) = 1</equation>，即<equation>f(7) = 1.</equation>（法二）由 f(x)为奇函数可知，<equation>f(x)=-f(-x).</equation>在等式两端求导得<equation>f^{\prime}(x)=f^{\prime}(-x),</equation>从而<equation>f^{\prime}(x)</equation>为偶函数，<equation>f^{\prime}(x)</equation>的图像关于y轴对称.在[0，2]上，<equation>f^{\prime}(x)=2(x-1),</equation>为一条过点（0，-2）和点（1，0）的直线。由此可知，在[-2，0]上，<equation>y=f^{\prime}(x)</equation>为过点（0，-2）和点（-1，0）的直线，可求得<equation>f^{\prime}(x)=-2(x+1).</equation>从而，<equation>f(x)</equation>在[-2，0]上为<equation>f (x) = \int_ {0} ^ {x} - 2 (t + 1) \mathrm {d} t + f (0) = - x ^ {2} - 2 x = - (x + 1) ^ {2} + 1.</equation>因此，<equation>f(-1)=1</equation>，即<equation>f(7)=1.</equation>

---

**2013年第15题 | 解答题 | 10分**
15. (本题满分10分)

计算<equation>\int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x, \text {其 中} f (x) = \int_ {1} ^ {x} \frac {\ln (t + 1)}{t} \mathrm {d} t.</equation>
**解析: **解（法一）由题设知，<equation>f^{\prime}(x) = \frac{\ln(x + 1)}{x}, x\in(0,1],</equation>且<equation>f(1)=0</equation>，于是<equation>\begin{aligned} \int_ {0} ^ {1} \frac {f (x)}{\sqrt {x}} \mathrm {d} x &= 2 \int_ {0} ^ {1} f (x) \mathrm {d} (\sqrt {x}) = 2 \left[ \sqrt {x} f (x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \sqrt {x} f ^ {\prime} (x) \mathrm {d} x \right] \right. \\ &= 0 - 2 \int_ {0} ^ {1} \sqrt {x} \cdot \frac {\ln (x + 1)}{x} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (x + 1)}{\sqrt {x}} \mathrm {d} x \\ &= - 4 \int_ {0} ^ {1} \ln (x + 1) \mathrm {d} (\sqrt {x}) \\ &= - 4 \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ \underline {{= - 4}} \left[ \sqrt {x} \ln (x + 1) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {\sqrt {x}}{x + 1} \mathrm {d} x \right] \right. \\ &= - 4 \ln 2 + 4 \int_ {0} ^ {1} \frac {t}{t ^ {2} + 1} \cdot 2 t \mathrm {d} t \\ &= - 4 \ln 2 + 8 \int_ {0} ^ {1} \left(1 - \frac {1}{t ^ {2} + 1}\right) \mathrm {d} t \\ &= - 4 \ln 2 + 8 \left(t - \arctan t\right) \Bigg | _ {0} ^ {1} \\ &= - 4 \ln 2 + 8 - 2 \pi . \end{aligned}</equation><equation>\begin{array}{l} \frac {\text {交换 积 分}}{\text {次 序}} - \int_ {0} ^ {1} \mathrm {d} t \int_ {0} ^ {t} \frac {\ln (t + 1)}{t} \cdot \frac {1}{\sqrt {x}} \mathrm {d} x = - 2 \int_ {0} ^ {1} \frac {\ln (t + 1)}{\sqrt {t}} \mathrm {d} t \\ \underline {{\text {同 法 一}}} - 4 \ln 2 + 8 - 2 \pi . \\ \end{array}</equation>

---

**2012年第10题 | 填空题 | 4分**
<equation>1 0. \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x = \underline {{}}</equation>
**解析: **解<equation>\sqrt{2 x-x^{2}}=\sqrt{1-(x-1)^{2}}.</equation>令 t=x-1，则有<equation>\begin{aligned} \int_ {0} ^ {2} x \sqrt {2 x - x ^ {2}} \mathrm {d} x &= \int_ {- 1} ^ {1} (t + 1) \sqrt {1 - t ^ {2}} \mathrm {d} t = \int_ {- 1} ^ {1} t \sqrt {1 - t ^ {2}} \mathrm {d} t + \int_ {- 1} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\text {对称性}}} 0 + 2 \int_ {0} ^ {1} \sqrt {1 - t ^ {2}} \mathrm {d} t \\ \underline {{\underline {{t = \sin \theta}}}} 2 \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} \theta \mathrm {d} \theta &= \int_ {0} ^ {\frac {\pi}{2}} (1 + \cos 2 \theta) \mathrm {d} \theta = \frac {\pi}{2}. \end{aligned}</equation>

---

**2010年第10题 | 填空题 | 4分**
10.
**解析: **<equation>\begin{aligned} \int_ {0} ^ {\pi^ {2}} \sqrt {x} \cos \sqrt {x} \mathrm {d} x \stackrel {t = \sqrt {x}} {=} \int_ {0} ^ {\pi} t \cos t \mathrm {d} \left(t ^ {2}\right) \\ &= \int_ {0} ^ {\pi} 2 t ^ {2} \cos t \mathrm {d} t = \int_ {0} ^ {\pi} 2 t ^ {2} \mathrm {d} (\sin t) \\ \underline {{\mathrm {分 部 积 分}}} (\sin t \cdot 2 t ^ {2}) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 t \sin t \mathrm {d} t &= \int_ {0} ^ {\pi} 4 t \mathrm {d} (\cos t) \right. \\ \underline {{\mathrm {分 部 积 分}}} (\cos t \cdot 4 t) \left| _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 4 \cos t \mathrm {d} t &= - 4 \pi . \right. \end{aligned}</equation>

---


#### 变限积分

**2024年第1题 | 选择题 | 5分 | 答案: C**
1. 已知函数<equation>f ( x )=\int_{0}^{x} \mathrm{e}^{\cos t} \mathrm{d} t,g ( x )=\int_{0}^{\sin x} \mathrm{e}^{t^{2}} \mathrm{d} t</equation>，则（    )

A. f(x)是奇函数，g(x)是偶函数 B. f(x)是偶函数，g(x)是奇函数

C. f(x)与 g(x)均为奇函数 D. f(x)与 g(x)均为周期函数
答案: C
**解析: **解 由于<equation>\mathrm{e}^{\cos t}</equation>是偶函数，且<equation>f(0)=0</equation>，故由分析中的结论可得<equation>f(x)=\int_{0}^{x}\mathrm{e}^{\cos t}\mathrm{d}t</equation>是奇函数.同理，<equation>h(x)=\int_{0}^{x}\mathrm{e}^{t^{2}}\mathrm{d}t</equation>也是奇函数.

注意到<equation>g ( x )=h (\sin x)</equation>，故<equation>g (- x) = h (\sin (- x)) = h (- \sin x) = - h (\sin x) = - g (x).</equation>于是，<equation>g ( x )</equation>也是奇函数.

因此，应选C.

下面说明选项 D 不正确.

由于<equation>\sin x</equation>是周期为<equation>2\pi</equation>的周期函数，故<equation>g (x + 2 \pi) = \int_ {0} ^ {\sin (x + 2 \pi)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {\sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = g (x).</equation>于是，<equation>g ( x )</equation>也是周期为<equation>2 \pi</equation>的周期函数.但是，由于<equation>f^{\prime}(x)=\mathrm{e}^{\cos x}>0</equation>，故f(x）单调增加，从而f(x)不可能为周期函数.

也可以直接验证<equation>f(-x)=-f(x), g(-x)=-g(x)</equation>，从而得到它们均为奇函数.<equation>f (- x) = \int_ {0} ^ {- x} \mathrm {e} ^ {\cos t} \mathrm {d} t \underline {{= u = - t}} - \int_ {0} ^ {x} \mathrm {e} ^ {\cos (- u)} \mathrm {d} u = - \int_ {0} ^ {x} \mathrm {e} ^ {\cos u} \mathrm {d} u = - f (x),</equation><equation>g (- x) = \int_ {0} ^ {\sin (- x)} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t = \int_ {0} ^ {- \sin x} \mathrm {e} ^ {t ^ {2}} \mathrm {d} t \xlongequal {u = - t} - \int_ {0} ^ {\sin x} \mathrm {e} ^ {(- u) ^ {2}} \mathrm {d} u = - \int_ {0} ^ {\sin x} \mathrm {e} ^ {u ^ {2}} \mathrm {d} u = - g (x).</equation>

---

**2009年第3题 | 选择题 | 4分 | 答案: D**
3. 设函数 y=f(x)在区间[-1,3]上的图形如图所示，则函数<equation>F ( x )=\int_{0}^{x} f ( t ) \mathrm{d} t</equation>的图形为（    ）

A.

B.

C.

D.
答案: D
**解析: **解（法一）我们可以从<equation>f(x)</equation>出发具体分析<equation>F(x)</equation>的性质.

因为<equation>f ( x )</equation>分段连续，所以由变上限积分函数的性质可知，在<equation>[-1,0)</equation>，（0，2），（2，3]上，均有<equation>F^{\prime}(x)=f(x).</equation><equation>\textcircled{1}</equation>由于 f(x)在[-1,3]上有界且只有两个间断点，故 f(x)可积.又因为<equation>F(x)=\int_{0}^{x} f(t)\mathrm{d}t</equation>所以 F(x)连续.<equation>\textcircled{2}</equation>在[-1,0）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（0，1）上，<equation>f ( x ) < 0</equation>，故 F(x)单调减少；在（1，2）上，<equation>f ( x ) > 0</equation>，故 F(x)单调增加；在（2，3]上，<equation>f ( x ) = 0</equation>，故 F(x)为常函数.<equation>\textcircled{3} F ( 0 )=\int_{0}^{0} f ( t ) \mathrm{d} t=0.</equation>在<equation>[-1,1]</equation>上，<equation>F ( x )</equation>均小于等于零.<equation>\textcircled{4}</equation><equation>f(1) = 0, x = 1</equation>为<equation>F(x)</equation>的驻点及极小值点.

同时满足以上要求的图形只有选项D. 应选D.

（法二）通过图形考察<equation>f(x)</equation>在<equation>[-1,0)</equation>上的性质，可知当<equation>x\in[-1,0)</equation>时，<equation>f(x)\equiv 1</equation>，故<equation>F (- 1) = \int_ {0} ^ {- 1} 1 \mathrm {d} x = - 1, \quad F (0) = \int_ {0} ^ {0} 1 \mathrm {d} x = 0,</equation>从而可排除选项A和选项C.

又由于 f(x)在[-1，3]上有界且只有两个间断点，f(x)在[-1，3]上可积，而 F(x) =<equation>\int_{0}^{x} f(t)\mathrm{d}t</equation>，故 F(x)必连续，从而可以排除选项B.

综上所述，应选D.

---


#### 定积分的概念、性质及几何意义

**2022年第4题 | 选择题 | 5分 | 答案: A**

4. 若<equation>I_{1}=\int_{0}^{1}\frac{x}{2(1+\cos x)}\mathrm{d}x,I_{2}=\int_{0}^{1}\frac{\ln(1+x)}{1+\cos x}\mathrm{d}x,I_{3}=\int_{0}^{1}\frac{2x}{1+\sin x}\mathrm{d}x</equation>，则（    )

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{2}<I_{1}<I_{3}</equation>C.<equation>I_{1}<I_{3}<I_{2}</equation>D.<equation>I_{3}<I_{2}<I_{1}</equation>

答案: A

**解析:**解 通过观察可发现，要比较<equation>I_{1}</equation>与<equation>I_{2}</equation>的大小，只需比较<equation>\frac{x}{2}</equation>与<equation>\ln(1+x)</equation>的大小.

令<equation>f(x)=\ln(1+x)-\frac{x}{2}</equation>，则<equation>f(0)=0</equation><equation>f^{\prime}(x)=\frac{1}{1+x}-\frac{1}{2}</equation>当<equation>x\in(0,1)</equation>时，<equation>f^{\prime}(x)>0</equation><equation>f(x)</equation>单调增加，从而<equation>f(x)>f(0)=0</equation>即<equation>\ln(1+x)>\frac{x}{2},\frac{\ln(1+x)}{1+\cos x}>\frac{x}{2(1+\cos x)}</equation>因此，<equation>I_{2}>I_{1}</equation>.

此外，同样的方法不难证明在(0,1)内，<equation>\ln(1+x)<x.</equation>另一方面，由于在(0,1)内，<equation>0<\sin x,\cos x<1,1<1+\sin x<2</equation>故<equation>I_{3}</equation>的被积函数<equation>\frac{2x}{1+\sin x} > x.</equation>结合<equation>\ln(1+x)<x</equation>可得，<equation>\frac{\ln(1+x)}{1+\cos x}<\frac{x}{1+\cos x}<x.</equation>于是，<equation>\frac{2x}{1+\sin x}>x>\frac{\ln(1+x)}{1+\cos x}.</equation>因此，<equation>I_{3}>I_{2}.</equation>综上所述，应选A.

---

**2021年第4题 | 选择题 | 5分 | 答案: B**

4. 设函数 f(x)在区间[0,1]上连续，则<equation>\int_{0}^{1} f(x)\mathrm{d}x=</equation>(    )

A.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{2n}</equation>B.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{n}f\left(\frac{2k-1}{2n}\right)\frac{1}{n}</equation>C.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k-1}{2n}\right)\frac{1}{n}</equation>D.<equation>\lim_{n\rightarrow \infty}\sum_{k=1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n}</equation>

答案: B

**解析:**解 由于 f(x)连续，故<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在，从而可对区间[0，1]进行划分，将该积分写为 n项和式的极限.

将[0，1]分为n等份，每个小区间为<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation><equation>k=1,2,\dots,n</equation>从<equation>\left[ \frac{k-1}{n},\frac{k}{n}\right]</equation>中取点<equation>\frac{2k-1}{2n}</equation>故由<equation>\int_{0}^{1} f(x)\mathrm{d}x</equation>存在以及定积分的定义可得<equation>\int_ {0} ^ {1} f (x) \mathrm {d} x = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} f \left(\frac {2 k - 1}{2 n}\right) \cdot \frac {1}{n}.</equation>因此，应选B.

下面说明选项A、C、D均不正确.

选项A：<equation>\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{2n} = \frac{1}{2}\lim_{n\to \infty}\sum_{k = 1}^{n}f\left(\frac{2k - 1}{2n}\right)\frac{1}{n} = \frac{1}{2}\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项C：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{n} = 2\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k - 1}{2n}\right)\frac{1}{2n} = 2\int_{0}^{1}f(x)\mathrm{d}x.</equation>选项D：<equation>\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{2}{n} = 4\lim_{n\to \infty}\sum_{k = 1}^{2n}f\left(\frac{k}{2n}\right)\frac{1}{2n} = 4\int_{0}^{1}f(x)\mathrm{d}x.</equation>

---

**2018年第4题 | 选择题 | 4分 | 答案: C**

4. 设<equation>M=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{(1+x)^{2}}{1+x^{2}}\mathrm{d}x</equation>，<equation>N=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{1+x}{\mathrm{e}^{x}}\mathrm{d}x</equation>，<equation>K=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}(1+\sqrt{\cos x})\mathrm{d}x</equation>，则（    )

A.<equation>M>N>K</equation>B.<equation>M>K>N</equation>C.<equation>K>M>N</equation>D.<equation>K>N>M</equation>

答案: C

**解析:**解分别计算 M,N,K.

由于<equation>\frac{2x}{1 + x^2}</equation>是奇函数，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{2x}{1 + x^2}\mathrm{d}x = 0.</equation>于是，<equation>M = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {(1 + x) ^ {2}}{1 + x ^ {2}} \mathrm {d} x = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x ^ {2} + 2 x}{1 + x ^ {2}} \mathrm {d} x \xlongequal {\frac {\int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {2 x}{1 + x ^ {2}} \mathrm {d} x = 0}{}} \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>注意到当<equation>x\neq 0</equation>时，<equation>\mathrm{e}^{x} > 1 + x.</equation>于是，在<equation>\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>上，<equation>\frac{1+x}{\mathrm{e}^{x}}\leqslant 1</equation>且等号仅在<equation>x=0</equation>处成立.<equation>N = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \frac {1 + x}{\mathrm {e} ^ {x}} \mathrm {d} x < \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \mathrm {d} x = \pi .</equation>由于<equation>\sqrt{\cos x}</equation>是偶函数，且当 x<equation>\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]</equation>时，<equation>\cos x\geqslant0</equation>且等号仅在端点处成立，故<equation>\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sqrt{\cos x}\mathrm{d}x>0.</equation>于是，<equation>K = \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \left(1 + \sqrt {\cos x}\right) \mathrm {d} x = \pi + \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \sqrt {\cos x} \mathrm {d} x > \pi .</equation>综上所述，<equation>K > M > N</equation>应选C.

---

**2017年第16题 | 解答题 | 10分**

16. (本题满分10分)<equation>\text {求} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right)</equation>

**解析:**解 根据定积分的定义，提出因子<equation>\frac{1}{n}</equation>，可得<equation>\begin{aligned} \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n ^ {2}} \ln \left(1 + \frac {k}{n}\right) &= \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \frac {k}{n} \ln \left(1 + \frac {k}{n}\right) \cdot \frac {1}{n} = \int_ {0} ^ {1} x \ln (1 + x) d x \\ &= \frac {1}{2} \int_ {0} ^ {1} \ln (1 + x) d \left(x ^ {2}\right) \xlongequal {\text {分 部 积 分}} \frac {x ^ {2}}{2} \ln (1 + x) \left| _ {0} ^ {1} - \int_ {0} ^ {1} \frac {x ^ {2}}{2 (1 + x)} d x \right. \\ &= \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \frac {x ^ {2} - 1 + 1}{1 + x} d x = \frac {\ln 2}{2} - \frac {1}{2} \int_ {0} ^ {1} \left(x - 1 + \frac {1}{1 + x}\right) d x \\ &= \frac {\ln 2}{2} - \frac {1}{2} \left[ \frac {x ^ {2}}{2} - x + \ln (1 + x) \right] \Bigg | _ {0} ^ {1} = \frac {1}{4}. \end{aligned}</equation>因此，原极限<equation>= \frac{1}{4}.</equation>

---

**2012年第4题 | 选择题 | 4分 | 答案: D**

4. 设<equation>I_{k}=\int_{0}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则有（    ）

A.<equation>I_{1}<I_{2}<I_{3}</equation>B.<equation>I_{3}<I_{2}<I_{1}</equation>C.<equation>I_{2}<I_{3}<I_{1}</equation>D.<equation>I_{2}<I_{1}<I_{3}</equation>

答案: D

**解析:**解（法一）记<equation>J_{k}=\int_{(k-1)\pi}^{k\pi}\mathrm{e}^{x^{2}}\sin x\mathrm{d}x(k=1,2,3)</equation>，则<equation>I _ {1} = J _ {1}, \quad I _ {2} = J _ {1} + J _ {2}, \quad I _ {3} = J _ {1} + J _ {2} + J _ {3}.</equation>由于<equation>\mathrm{e}^{x^{2}} > 0</equation>，且在（0，<equation>\pi</equation>）上，<equation>\sin x > 0</equation>；在（<equation>\pi,2\pi</equation>）上，<equation>\sin x < 0</equation>；在（<equation>2\pi,3\pi</equation>）上，<equation>\sin x > 0</equation>，故<equation>J_{1}>0</equation>，<equation>J_{2}<0</equation>，<equation>J_{3}>0</equation>.由此可得，<equation>I_{1}>I_{2}</equation>，<equation>I_{3}>I_{2}</equation>.

下面比较<equation>I_{1}</equation>和<equation>I_{3}.</equation><equation>I _ {3} - I _ {1} = J _ {2} + J _ {3}.</equation><equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x > \mathrm {e} ^ {(2 \pi) ^ {2}} \int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x,</equation><equation>\left| J _ {2} \right| = \left| \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \right| < \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|, \quad J _ {2} > - \mathrm {e} ^ {(2 \pi) ^ {2}} \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|.</equation>由定积分的几何意义可知，<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x</equation>和<equation>|\int_{\pi}^{2\pi}\sin x\mathrm{d}x|</equation>分别为<equation>\sin x</equation>在<equation>(2\pi ,3\pi)</equation>上以及在<equation>(\pi ,2\pi)</equation>上的部分与<equation>x</equation>轴围成的图形面积.根据<equation>\sin x</equation>的图形，这两部分面积相等，即<equation>\int_{2\pi}^{3\pi}\sin x\mathrm{d}x = \left|\int_{\pi}^{2\pi}\sin x\mathrm{d}x\right|.</equation>于是，

于是，<equation>J _ {2} + J _ {3} > \mathrm {e} ^ {(2 \pi) ^ {2}} \left(\int_ {2 \pi} ^ {3 \pi} \sin x \mathrm {d} x - \left| \int_ {\pi} ^ {2 \pi} \sin x \mathrm {d} x \right|\right) = 0,</equation>即<equation>I_{3} > I_{1}.</equation>因此，<equation>I_{2} < I_{1} < I_{3}</equation>应选D.

（法二）在法一中，证明<equation>J_{2} + J_{3} > 0</equation>，也可以使用如下方法.<equation>J _ {3} = \int_ {2 \pi} ^ {3 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x \xlongequal {u = x - \pi} \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin (u + \pi) \mathrm {d} u = - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(u + \pi) ^ {2}} \sin u \mathrm {d} u,</equation><equation>J _ {2} + J _ {3} = \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {x ^ {2}} \sin x \mathrm {d} x - \int_ {\pi} ^ {2 \pi} \mathrm {e} ^ {(x + \pi) ^ {2}} \sin x \mathrm {d} x = \int_ {\pi} ^ {2 \pi} \sin x \left[ \mathrm {e} ^ {x ^ {2}} - \mathrm {e} ^ {(x + \pi) ^ {2}} \right] \mathrm {d} x.</equation>当<equation>x\in (\pi ,2\pi)</equation>时，<equation>\sin x < 0,\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2} < 0,\sin x[\mathrm{e}^{x^2} - \mathrm{e}^{(x + \pi)^2}] > 0</equation>，从而<equation>J_{2} + J_{3} > 0.</equation>其余同法一.

---

**2011年第4题 | 选择题 | 4分 | 答案: B**

4. 设<equation>I=\int_{0}^{\frac{\pi}{4}}\ln(\sin x)\mathrm{d}x, J=\int_{0}^{\frac{\pi}{4}}\ln(\cot x)\mathrm{d}x, K=\int_{0}^{\frac{\pi}{4}}\ln(\cos x)\mathrm{d}x</equation>，则 I,J,K的大小关系为（    )

A. I<J<K B. I<K<J C. J<I<K D. K<J<I

答案: B

**解析:**解 当 0 < x <<equation>\frac{\pi}{4}</equation>时，0 < sin x < cos x < 1 < cot x.又 f(t) = ln t在（0，+<equation>\infty</equation>）上单调增加，故当 0 < x <<equation>\frac{\pi}{4}</equation>时，<equation>\ln(\sin x) < \ln(\cos x) < \ln(\cot x)</equation>，从而由积分的保号性可知， I < K < J ，选B.

---

**2010年第17题 | 解答题 | 10分**

17. (本题满分10分)

17. (本题满分10分)

I. 比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>）的大小，说明理由；

II. 记<equation>u_{n}=\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>（ n=1,2，<equation>\cdots</equation>），求极限<equation>\lim_{n\to\infty}u_{n}.</equation>

**答案:**(17) （I）<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t<\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t</equation>，理由略；（Ⅱ）<equation>\lim_{n\to\infty}u_{n}=0.</equation>

**解析:**解（I）在（0，1]上，<equation>|\ln t|</equation><equation>\ln(1+t)</equation>与 t均非负，故比较<equation>\int_{0}^{1}|\ln t|[\ln(1+t)]^{n}\mathrm{d}t</equation>与<equation>\int_{0}^{1}t^{n}|\ln t|\mathrm{d}t(n=1,2,\cdots)</equation>的大小，只需比较<equation>\ln(1+t)</equation>与 t的大小.

考虑 f（t）=<equation>\ln(1+t)-t.</equation><equation>f ^ {\prime} (t) = \frac {1}{1 + t} - 1.</equation>当<equation>t\in (0,1]</equation>时，<equation>f^{\prime}(t) < 0,f(t)\leqslant f(0) = 0.</equation>因此，当<equation>t \in [0,1]</equation>时，<equation>\ln (1 + t) \leqslant t.</equation>由于两被积函数仅在<equation>t = 1</equation>处相等，故<equation>\int_ {0} ^ {1} | \ln t | [ \ln (1 + t) ] ^ {n} \mathrm {d} t < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t (n = 1, 2, \dots).</equation>（Ⅱ）（法一）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {1} t ^ {n} \mid \ln t \mid \mathrm {d} t &= \frac {- 1}{n + 1} \int_ {0} ^ {1} \ln t \mathrm {d} \left(t ^ {n + 1}\right) = \frac {- 1}{n + 1} \left(t ^ {n + 1} \ln t \mid_ {0} ^ {1} - \int_ {0} ^ {1} t ^ {n + 1} \cdot \frac {1}{t} \mathrm {d} t\right) \\ \frac {\lim _ {t \rightarrow 0 ^ {+}} t ^ {n + 1} \ln t = 0}{\overline {{\quad}}} \frac {1}{n + 1} \int_ {0} ^ {1} t ^ {n} \mathrm {d} t &= \frac {1}{(n + 1) ^ {2}}. \end{aligned}</equation>因此，<equation>\lim _ {n \rightarrow \infty} \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t = \lim _ {n \rightarrow \infty} \frac {1}{(n + 1) ^ {2}} = 0.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法二）由第（I）问知，<equation>0 < u_{n} < \int_{0}^{1} t^{n}|\ln t|\mathrm{d}t.</equation>又因为<equation>\lim_{t\to 0^{+}}(t\ln t) = 0</equation>，所以存在<equation>M > 0</equation>，使得对任意的<equation>t\in (0,1]</equation>，有<equation>t|\ln t|\leqslant M</equation>，从而<equation>0 < u _ {n} < \int_ {0} ^ {1} t ^ {n} | \ln t | \mathrm {d} t \leqslant M \int_ {0} ^ {1} t ^ {n - 1} \mathrm {d} t = \frac {M}{n}.</equation>由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>（法三）由于<equation>t\in[0,1]</equation>时，<equation>\ln(1 + t)\leqslant \ln 2 < 1</equation>，故<equation>u_{n}\leqslant (\ln 2)^{n}\int_{0}^{1}|\ln t|\mathrm{d}t.</equation>计算<equation>\int_{0}^{1}|\ln t| \mathrm{d} t</equation>得，<equation>\int_ {0} ^ {1} | \ln t | \mathrm {d} t = - \int_ {0} ^ {1} \ln t \mathrm {d} t = - \left(t \ln t \left| _ {0} ^ {1} - \int_ {0} ^ {1} 1 \mathrm {d} t\right)\right) \xlongequal {\lim _ {t \rightarrow 0 ^ {+}} t \ln t = 0} 1.</equation>从而<equation>0 < u_{n}\leqslant (\ln 2)^{n}</equation>因为<equation>\lim_{n\to \infty}(\ln 2)^n = 0</equation>，所以由夹逼准则知，<equation>\lim_{n\to \infty}u_n = 0.</equation>

---


#### 反常积分的计算与敛散性

**2021年第11题 | 填空题 | 5分**

<equation>\int_ {0} ^ {+ \infty} \frac {1}{x ^ {2} + 2 x + 2} \mathrm {d} x = \underline {{}}</equation>

**答案:**##<equation>\frac{\pi}{4}</equation>

**解析:**将<equation>x^{2}+2 x+2</equation>配方.<equation>\begin{aligned} \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{x ^ {2} + 2 x + 2} &= \int_ {0} ^ {+ \infty} \frac {\mathrm {d} x}{(x + 1) ^ {2} + 1} = \int_ {0} ^ {+ \infty} \frac {\mathrm {d} (x + 1)}{(x + 1) ^ {2} + 1} = \arctan (x + 1) \Big | _ {0} ^ {+ \infty} \\ &= \frac {\pi}{2} - \arctan 1 = \frac {\pi}{2} - \frac {\pi}{4} = \frac {\pi}{4}. \end{aligned}</equation>

---

**2016年第1题 | 选择题 | 4分 | 答案: C**

1. 若反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>收敛，则（    )

A. a < 1且b > 1 B. a > 1且b > 1 C. a < 1且a+b > 1 D. a > 1且a+b > 1

答案: C

**解析:**解 由于被积函数<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>在<equation>[0,+\infty)</equation>上可能的瑕点为<equation>x=0</equation>，故将反常积分分为两部分，即<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x=\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x+\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x.</equation>对于积分<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，若<equation>a\leqslant0</equation>，则该积分为正常的定积分；若<equation>a>0</equation>，则<equation>x=0</equation>为被积函数的瑕点.

由于<equation>\lim_{x\rightarrow 0^{+}}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a}}}=\lim_{x\rightarrow 0^{+}}\frac{1}{(1+x)^{b}}=1</equation>，故当<equation>x\rightarrow 0^{+}</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a}}</equation>等价. 瑕积分<equation>\int_{0}^{1}\frac{1}{x^{a}}\mathrm{d}x</equation>当且仅当<equation>0<a<1</equation>时收敛，加上<equation>a\leqslant0</equation>时的情况，<equation>\int_{0}^{1}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a<1</equation>时收敛.

对于反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>，由于<equation>\lim_{x\rightarrow+\infty}\frac{\frac{1}{x^{a}(1+x)^{b}}}{\frac{1}{x^{a+b}}}=\lim_{x\rightarrow+\infty}\left(\frac{x}{1+x}\right)^{b}=1</equation>，故当<equation>x\rightarrow+\infty</equation>时，<equation>\frac{1}{x^{a}(1+x)^{b}}</equation>与<equation>\frac{1}{x^{a+b}}</equation>等价. 反常积分<equation>\int_{1}^{+\infty}\frac{1}{x^{a+b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛，故<equation>\int_{1}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}\mathrm{d}x</equation>当且仅当<equation>a+b>1</equation>时收敛.

综上所述，反常积分<equation>\int_{0}^{+\infty}\frac{1}{x^{a}(1+x)^{b}}</equation>收敛当且仅当 a,b满足 a < 1 且 a+b > 1，应选 C.

---

**2013年第12题 | 填空题 | 4分**

<equation>2. \int_ {1} ^ {+ \infty} \frac {\ln x}{(1 + x) ^ {2}} \mathrm {d} x = \underline {{}}</equation>

**答案:**## ln 2.

**解析:**<equation>\begin{aligned} { } ^ { + \infty } \frac {\ln x}{( 1 + x ) ^ { 2 } } \mathrm { d } x &= - \int _ { 1 } ^ { + \infty } \ln x \mathrm { d } \left( \frac { 1 } { 1 + x } \right) = - \left[ \left. \frac {\ln x}{1 + x} \right| _ { 1 } ^ { + \infty } - \int _ { 1 } ^ { + \infty } \frac { 1 } { x ( 1 + x ) } \mathrm { d } x \right] \\ &= - \lim _ {x \rightarrow + \infty} \frac {\ln x}{1 + x} + \int_ {1} ^ {+ \infty} \left(\frac {1}{x} - \frac {1}{x + 1}\right) \mathrm {d} x \\ \underline {{\text {洛必达}}} - \lim _ {x \rightarrow + \infty} \frac {1}{x} + \ln \frac {x}{x + 1} \Bigg | _ {1} ^ {+ \infty} \\ &= 0 + \ln 1 - \ln \frac {1}{2} = \ln 2. \end{aligned}</equation>

---

**2010年第3题 | 选择题 | 4分 | 答案: D**

3. 设 m,n均是正整数，则反常积分<equation>\int_{0}^{1}\frac{\sqrt[m]{\ln^{2}(1-x)}}{\sqrt[n]{x}} \mathrm{d} x</equation>的收敛性（    ）

A. 仅与 m的取值有关 B. 仅与 n的取值有关

C. 与 m,n的取值都有关 D. 与 m,n的取值都无关

答案: D

**解析:**由于被积函数有两个可能的瑕点，<equation>x=0</equation>和<equation>x=1</equation>，故将原积分拆成两部分进行考虑.<equation>\int_ {0} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x = \int_ {0} ^ {\frac {1}{2}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x + \int_ {\frac {1}{2}} ^ {1} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \mathrm {d} x.</equation>先讨论<equation>\int_0^{\frac{1}{2}}\frac{[\ln(1 - x)]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性.考虑<equation>\lim_{x\to 0^{+}}\frac{[\ln(1 - x)]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>.<equation>\lim _ {x \rightarrow 0 ^ {+}} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} \xlongequal {\ln (1 - x) \sim (- x)} \lim _ {x \rightarrow 0 ^ {+}} x ^ {\frac {2}{m} - \frac {1}{n}} = \left\{\begin{array}{l l}0,&\frac {2}{m} - \frac {1}{n} > 0,\\1,&\frac {2}{m} - \frac {1}{n} = 0,\\\infty ,&\frac {2}{m} - \frac {1}{n} < 0.\end{array}\right.</equation>当 m，n为正整数时，<equation>\frac{2}{m} -\frac{1}{n}\geqslant \frac{2}{m} -1 > -1.</equation>- 当<equation>\frac{2}{m}-\frac{1}{n}\geqslant0</equation>时，<equation>x=0</equation>是被积函数的可去间断点，<equation>\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}</equation>在<equation>\left[0,\frac{1}{2}\right]</equation>上可积，<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>存在且有限.

- 当<equation>- 1 < \frac{2}{m} - \frac{1}{n} < 0</equation>时，<equation>x=0</equation>是被积函数的瑕点.取<equation>p=\frac{1}{n}-\frac{2}{m}</equation>则<equation>0 < p < 1</equation><equation>\lim_{x\rightarrow 0^{+}}\frac{x^{p}\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}=1.</equation>由极限审敛法可知反常积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>收敛.

因此，不论 m，n 取何正整数，积分<equation>\int_{0}^{\frac{1}{2}}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.

下面讨论<equation>\int_{\frac{1}{2}}^{1}\frac{\left[\ln(1-x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>的收敛性. x=1为被积函数的瑕点.

考虑极限<equation>\lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \frac {\left[ \ln (1 - x) \right] ^ {\frac {2}{m}}}{x ^ {\frac {1}{n}}} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}}.</equation>记<equation>I _ {0} = \lim _ {x \rightarrow 1 ^ {-}} \sqrt {1 - x} \left[ \ln (1 - x) \right] ^ {\frac {2}{m}} \xlongequal {u = 1 - x} \lim _ {u \rightarrow 0 ^ {+}} u ^ {\frac {1}{2}} (\ln u) ^ {\frac {2}{m}}.</equation>若 m=1，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\left(\ln u\right) ^ {2}}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} \frac {- 4 \ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛必达}} \lim _ {u \rightarrow 0 ^ {+}} 8 u ^ {\frac {1}{2}} = 0.</equation>若 m=2，则<equation>I _ {0} = \lim _ {u \rightarrow 0 ^ {+}} \frac {\ln u}{u ^ {- \frac {1}{2}}} \xlongequal {\text {洛 必达}} \lim _ {u \rightarrow 0 ^ {+}} (- 2) u ^ {\frac {1}{2}} = 0.</equation>若<equation>m > 2</equation>，则<equation>0 < \frac{2}{m} < 1</equation>，同理使用洛必达法则可计算得<equation>I_0 = 0.</equation>因此，由极限审敛法知，不论 m，n 取何正整数，积分<equation>\int_{\frac{1}{2}}^{1} \frac{\left[ \ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛综上所述，不论 m，n 取何正整数，积分<equation>\int_{0}^{1} \frac{\left[ \ln(1 - x)\right]^{\frac{2}{m}}}{x^{\frac{1}{n}}}\mathrm{d}x</equation>均收敛.应选D.

---


#### 定积分的应用

**2019年第17题 | 解答题 | 10分**

17. (本题满分10分）

求曲线<equation>y=\mathrm{e}^{-x}\sin x(x\geqslant 0)</equation>与x轴之间图形的面积.

**答案:**<equation>\frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>

**解析:**解（法一）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.根据定积分的几何意义，曲线位于<equation>(k\pi ,(k + 1)\pi)</equation>的部分与<equation>x</equation>轴之间的图形面积等于<equation>\int_{k\pi}^{(k + 1)\pi}\mathrm{e}^{-x}|\sin x|\mathrm{d}x.</equation>计算<equation>S_{n}。</equation><equation>\begin{aligned} S _ {n} &= \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \mathrm {e} ^ {- x} | \sin x | \mathrm {d} x \xlongequal {t = x - k \pi} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \mathrm {e} ^ {- (t + k \pi)} | \sin (t + k \pi) | \mathrm {d} t \\ &= \sum_ {k = 0} ^ {n - 1} \mathrm {e} ^ {- k \pi} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>下面计算<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t.</equation><equation>\begin{aligned} \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t &= - \int_ {0} ^ {\pi} \sin t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) = - \left(\sin t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t\right) \\ &= \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \cos t \mathrm {d} t = - \int_ {0} ^ {\pi} \cos t \mathrm {d} \left(\mathrm {e} ^ {- t}\right) \\ &= - \cos t \mathrm {e} ^ {- t} \Big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t \\ &= \mathrm {e} ^ {- \pi} + 1 - \int_ {0} ^ {\pi} \mathrm {e} ^ {- t} \sin t \mathrm {d} t. \end{aligned}</equation>由上式可得<equation>2\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t = \mathrm{e}^{-\pi} + 1</equation>，于是<equation>\int_{0}^{\pi}\mathrm{e}^{-t}\sin t\mathrm{d}t = \frac{1}{2}\left(\mathrm{e}^{-\pi} + 1\right)</equation>.

因此，<equation>S = \lim _ {n \rightarrow \infty} S _ {n} = \frac {1}{2} \left(\mathrm {e} ^ {- \pi} + 1\right) \lim _ {n \rightarrow \infty} \frac {1 - \mathrm {e} ^ {- n \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} \cdot \frac {\mathrm {e} ^ {- \pi} + 1}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}.</equation>（法二）注意到<equation>\mathrm{e}^{-x}</equation>恒大于零.当<equation>x\in(2n\pi,(2n+1)\pi)</equation>时，<equation>\sin x > 0</equation>；当<equation>x\in((2n+1)\pi,</equation><equation>(2n+2)\pi)</equation>时，<equation>\sin x < 0</equation>因此，根据定积分的几何意义，曲线位于<equation>(2n\pi, (2n+1)\pi)</equation>的部分与x轴之间的图形面积等于<equation>\int_{2n\pi}^{(2n+1)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x</equation>；曲线位于<equation>((2n+1)\pi, (2n+2)\pi)</equation>的部分与x轴之间的图形面积等于<equation>-\int_{(2n+1)\pi}^{(2n+2)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x.</equation>记所求面积为 S，则<equation>S = \sum_ {n = 0} ^ {\infty} \int_ {2 n \pi} ^ {(2 n + 1) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x - \sum_ {n = 0} ^ {\infty} \int_ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \mathrm {e} ^ {- x} \sin x \mathrm {d} x.</equation>下面计算<equation>\int \mathrm{e}^{-x}\sin x\mathrm{d}x.</equation><equation>\begin{aligned} \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x &= - \int \sin x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) = - \left(\sin x \mathrm {e} ^ {- x} - \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x\right) \\ &= - \sin x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \cos x \mathrm {d} x = - \sin x \mathrm {e} ^ {- x} - \int \cos x \mathrm {d} \left(\mathrm {e} ^ {- x}\right) \\ &= - \sin x \mathrm {e} ^ {- x} - \left(\cos x \mathrm {e} ^ {- x} + \int \mathrm {e} ^ {- x} \sin x \mathrm {d} x\right). \end{aligned}</equation>由上式可得<equation>2\int \mathrm{e}^{-x}\sin x\mathrm{d}x = -\mathrm{e}^{-x}(\sin x + \cos x) - C</equation>，于是<equation>\int \mathrm {e} ^ {- x} \sin x \mathrm {d} x = - \frac {1}{2} \left[ \mathrm {e} ^ {- x} \left(\sin x + \cos x\right) + C \right],</equation>其中 C为任意常数.

因此，<equation>\begin{aligned} S &= \sum_ {n = 0} ^ {\infty} \left[ - \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {2 n \pi} ^ {(2 n + 1) \pi} + \sum_ {n = 0} ^ {\infty} \left[ \frac {1}{2} \mathrm {e} ^ {- x} (\sin x + \cos x) \right] \Bigg | _ {(2 n + 1) \pi} ^ {(2 n + 2) \pi} \\ &= \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 1) \pi} + \mathrm {e} ^ {- 2 n \pi} \right] + \frac {1}{2} \sum_ {n = 0} ^ {\infty} \left[ \mathrm {e} ^ {- (2 n + 2) \pi} + \mathrm {e} ^ {- (2 n + 1) \pi} \right] \\ &= \frac {1}{2} \left[ \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} + 2 \sum_ {n = 0} ^ {\infty} \mathrm {e} ^ {- (2 n + 1) \pi} + \sum_ {n = 1} ^ {\infty} \mathrm {e} ^ {- 2 n \pi} \right] \\ &= \frac {1}{2} \left(\frac {1}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {2 \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- 2 \pi}} + \frac {\mathrm {e} ^ {- 2 \pi}}{1 - \mathrm {e} ^ {- 2 \pi}}\right) = \frac {1}{2} \cdot \frac {\left(1 + \mathrm {e} ^ {- \pi}\right) ^ {2}}{\left(1 + \mathrm {e} ^ {- \pi}\right) \left(1 - \mathrm {e} ^ {- \pi}\right)} \\ &= \frac {1}{2} \cdot \frac {1 + \mathrm {e} ^ {- \pi}}{1 - \mathrm {e} ^ {- \pi}} = \frac {1}{2} + \frac {1}{\mathrm {e} ^ {\pi} - 1}. \end{aligned}</equation>

---

**2017年第4题 | 选择题 | 4分 | 答案: C**

4. 甲、乙两人赛跑，计时开始时，甲在乙前方10（单位：m）处，图中，实线表示甲的速度曲线<equation>v=v_{1}(t)</equation>（单位： m/s），虚线表示乙的速度曲线<equation>v=v_{2}(t)</equation>，三块阴影部分面积的数值依次是10，20，3. 计时开始后乙追上甲的时刻记为<equation>t_{0}</equation>（单位：s），则（    ）

A.<equation>t_{0}=1 0</equation>B.<equation>1 5<t_{0}<2 0</equation>C.<equation>t_{0}=2 5</equation>D.<equation>t_{0}>2 5</equation>

答案: C

**解析:**解 根据定积分的物理意义，从0s到10s这段时间内，实线位于虚线之上，于是甲跑过的路程比乙跑过的路程多10m；从10s到25s这段时间内，虚线位于实线之上，于是乙跑过的路程比甲跑过的路程多20m.

---

**2012年第18题 | 解答题 | 10分**

18. (本题满分10分)

已知曲线 L：<equation>\left\{\begin{array}{l l}x=f(t),\\ y=\cos t\end{array}\right.</equation><equation>(0\leqslant t<\frac{\pi}{2})</equation>，其中函数 f(t)具有连续导数，且 f(0)=0，<equation>f^{\prime}(t)>0</equation><equation>(0<t<\frac{\pi}{2})</equation>. 若曲线 L的切线与 x轴的交点到切点的距离恒为1，求函数 f(t)的表达式，并求以曲线 L及 x轴和 y轴为边界的区域的面积.

**答案:**(18)<equation>f ( t )=\ln | \sec t+\tan t |-\sin t, 0\leqslant t < \frac{\pi}{2}</equation>; 面积为<equation>\frac{\pi}{4}</equation>

**解析:**解曲线 L在点（ f(t），cos t）处的切线的斜率为<equation>\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\frac{\mathrm{d} y}{\mathrm{d} t}}{\frac{\mathrm{d} x}{\mathrm{d} t}}=-\frac{\sin t}{f^{\prime}(t)},</equation>从而切线方程为<equation>y - \cos t = \frac {- \sin t}{f ^ {\prime} (t)} [ x - f (t) ],</equation>于是切线与<equation>x</equation>轴的交点为<equation>\left(f(t) + \frac{\cos t}{\sin t} f^{\prime}(t),0\right)</equation>.由已知条件可得<equation>\left[ f (t) + \frac {\cos t}{\sin t} f ^ {\prime} (t) - f (t) \right] ^ {2} + \left(0 - \cos t\right) ^ {2} = 1,</equation>化简得<equation>[f^{\prime}(t)]^{2} = \left(\frac{\sin^{2}t}{\cos t}\right)^{2}</equation>.

由于当<equation>0 < t < \frac{\pi}{2}</equation>时，<equation>f^{\prime}(t) > 0</equation>，故<equation>f^{\prime}(t) = \frac{\sin^{2}t}{\cos t}</equation>. 又<equation>f(0) = 0</equation>，故<equation>\forall 0\leqslant t < \frac{\pi}{2}</equation>，有<equation>f (t) = \int_ {0} ^ {t} \frac {\sin^ {2} x}{\cos x} \mathrm {d} x = \int_ {0} ^ {t} \frac {1 - \cos^ {2} x}{\cos x} \mathrm {d} x = \int_ {0} ^ {t} \sec x \mathrm {d} x - \int_ {0} ^ {t} \cos x \mathrm {d} x = \ln | \sec t + \tan t | - \sin t,</equation>设以曲线<equation>L</equation>及<equation>x</equation>轴和<equation>y</equation>轴为边界的区域的面积为<equation>S</equation>，则<equation>\begin{aligned} S &= \int_ {0} ^ {\frac {\pi}{2}} y (t) \mathrm {d} \left(x (t)\right) = \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot x ^ {\prime} (t) \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot f ^ {\prime} (t) \mathrm {d} t \\ &= \int_ {0} ^ {\frac {\pi}{2}} \cos t \cdot \frac {\sin^ {2} t}{\cos t} \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm {d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {1 - \cos 2 t}{2} \mathrm {d} t = \frac {\pi}{4}. \end{aligned}</equation>

---

**2011年第9题 | 填空题 | 4分**

9. 曲线<equation>y=\int_{0}^{x}\tan t\mathrm{d}t \left( 0\leqslant x\leqslant\frac{\pi}{4} \right)</equation>的弧长 s = ___

**答案:**##<equation>\ln(\sqrt{2}+1).</equation>

**解析:**<equation>\begin{aligned} s &= \int_ {0} ^ {\frac {\pi}{4}} \sqrt {1 + \left[ y ^ {\prime} (x) \right] ^ {2}} \mathrm {d} x = \int_ {0} ^ {\frac {\pi}{4}} \sqrt {1 + \tan^ {2} x} \mathrm {d} x \\ &= \int_ {0} ^ {\frac {\pi}{4}} \sec x \mathrm {d} x = \ln | \sec x + \tan x | \Bigg | _ {0} ^ {\frac {\pi}{4}} = \ln (\sqrt {2} + 1). \end{aligned}</equation>

---

**2009年第17题 | 解答题 | 10分**

17. (本题满分11分)

椭球面<equation>S_{1}</equation>是椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>绕 x轴旋转而成，圆雉面<equation>S_{2}</equation>是由过点(4,0)且与椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>相切的直线绕 x轴旋转而成.

I. 求<equation>S_{1}</equation>及<equation>S_{2}</equation>的方程；

II. 求<equation>S_{1}</equation>与<equation>S_{2}</equation>之间的立体的体积.

**答案:**(17) （I）椭球面<equation>S_{1}</equation>的方程为<equation>\frac{x^{2}}{4}+\frac{y^{2}+z^{2}}{3}=1</equation>，圆锥面<equation>S_{2}</equation>的方程为<equation>y^{2}+z^{2}=\frac{1}{4}(x-4)^{2}</equation>； （Ⅱ）<equation>V=\pi.</equation>

**解析:**解（I）由椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>绕 x轴旋转得到的椭球面<equation>S_{1}</equation>的方程为<equation>\frac {x ^ {2}}{4} + \frac {\left(\pm \sqrt {y ^ {2} + z ^ {2}}\right) ^ {2}}{3} = 1,</equation>即为<equation>\frac{x^2}{4} +\frac{y^2 + z^2}{3} = 1.</equation>设椭圆<equation>\frac{x^{2}}{4}+\frac{y^{2}}{3}=1</equation>上任一点为（<equation>2\cos \theta ,\sqrt{3}\sin \theta )</equation>，则过该点且与椭圆相切的直线的斜率为<equation>\frac{\mathrm{d}y}{\mathrm{d}x}=</equation><equation>\frac{\frac{\mathrm{d}y}{\mathrm{d}\theta}}{\frac{\mathrm{d}x}{\mathrm{d}\theta}}=\frac{(\sqrt{3}\sin \theta)^{\prime}}{(2\cos \theta)^{\prime}}=\frac{\sqrt{3}\cos \theta}{-2\sin \theta}</equation>，从而切线方程为<equation>y = - \frac {\sqrt {3} \cos \theta}{2 \sin \theta} (x - 2 \cos \theta) + \sqrt {3} \sin \theta .</equation>将<equation>( x,y)=(4,0)</equation>代入上式得<equation>\cos \theta=\frac{1}{2},\sin \theta=\pm \frac{\sqrt{3}}{2}</equation>，于是切线方程为<equation>y=\pm \frac{1}{2} ( x-4 )</equation>，切点为<equation>\left( 1,\pm \frac{3}{2} \right).</equation>又圆锥面<equation>S_{2}</equation>是由直线<equation>y=\frac{1}{2} ( x-4 )</equation>绕x轴旋转得到，故<equation>S_{2}</equation>的方程为<equation>\pm \sqrt{y^{2}+z^{2}}=\frac{1}{2} ( x-4 )</equation>即为<equation>y^{2}+z^{2}=\frac{1}{4} ( x-4 )^{2}.</equation>（Ⅱ）记<equation>V_{1}</equation>为椭球面<equation>S_{1}</equation>所围成的椭球体在平面<equation>x=1</equation>与<equation>x=2</equation>之间的部分的体积，则由旋转体体积公式知，<equation>V_{1}=\pi \int_{1}^{2} y^{2}\mathrm{d}x=\pi \int_{1}^{2} 3 \left( 1-\frac{x^{2}}{4} \right) \mathrm{d}x=\frac{5}{4} \pi</equation>；记<equation>V_{2}</equation>为圆锥面<equation>S_{2}</equation>与平面<equation>x=1</equation>所围成的区域的体积，即底面半径为<equation>\frac{3}{2}</equation>，高为3的圆锥体体积，则<equation>V_{2}=\frac{1}{3}\pi r^{2} h=\frac{1}{3}\pi \cdot \left( \frac{3}{2} \right)^{2} \cdot 3=\frac{9}{4}\pi.</equation>因此，<equation>S_{1}</equation>与<equation>S_{2}</equation>之间的立体的体积为<equation>V=V_{2}-V_{1}=\frac{9}{4}\pi -\frac{5}{4}\pi =\pi.</equation>

---


#### 不定积分的计算

**2018年第15题 | 解答题 | 10分**

15. (本题满分10分)

求不定积分

**答案:**<equation>\frac{\mathrm{e}^{2x}\arctan \sqrt{\mathrm{e}^{x} - 1}}{2} -\frac{1}{6}\left(\mathrm{e}^{x} - 1\right)^{\frac{3}{2}} - \frac{1}{2}\sqrt{\mathrm{e}^{x} - 1} + C</equation>，其中C为任意常数.

**解析:**解 利用分部积分法.<equation>\begin{aligned} \int \mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} x \stackrel {\text {分 部 积 分}} {=} \frac {1}{2} \int \arctan \sqrt {\mathrm {e} ^ {x} - 1} \mathrm {d} \left(\mathrm {e} ^ {2 x}\right) \\ &= \frac {\mathrm {e} ^ {2 x}}{2} \cdot \arctan \sqrt {\mathrm {e} ^ {x} - 1} - \frac {1}{2} \int \mathrm {e} ^ {2 x} \cdot \frac {1}{1 + \mathrm {e} ^ {x} - 1} \cdot \frac {\mathrm {e} ^ {x}}{2 \sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x \\ &= \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{4} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x. \end{aligned}</equation>下面用两种方法计算<equation>\int \frac{\mathrm{e}^{2x}}{\sqrt{\mathrm{e}^{x} - 1}}\mathrm{d}x.</equation>（法一）令<equation>u = \sqrt{\mathrm{e}^{x} - 1}</equation>，则<equation>x = \ln (u^{2} + 1)</equation>，<equation>\mathrm{d}x = \frac{2u}{u^{2} + 1}\mathrm{d}u.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\left(u ^ {2} + 1\right) ^ {2}}{u} \cdot \frac {2 u}{u ^ {2} + 1} \mathrm {d} u = 2 \int \left(u ^ {2} + 1\right) \mathrm {d} u = \frac {2}{3} u ^ {3} + 2 u + C _ {1} \\ &= \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

（法二）令<equation>t = \mathrm{e}^{x}</equation>，则<equation>\mathrm{d}t = \mathrm{e}^{x}\mathrm{d}x.</equation><equation>\begin{aligned} \int \frac {\mathrm {e} ^ {2 x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} x &= \int \frac {\mathrm {e} ^ {x}}{\sqrt {\mathrm {e} ^ {x} - 1}} \mathrm {d} \left(\mathrm {e} ^ {x}\right) = \int \frac {t}{\sqrt {t - 1}} \mathrm {d} t = \int \frac {t - 1 + 1}{\sqrt {t - 1}} \mathrm {d} t = \int \left(\sqrt {t - 1} + \frac {1}{\sqrt {t - 1}}\right) \mathrm {d} t \\ &= \frac {2}{3} (t - 1) ^ {\frac {3}{2}} + 2 \sqrt {t - 1} + C _ {1} = \frac {2}{3} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} + 2 \sqrt {\mathrm {e} ^ {x} - 1} + C _ {1}, \end{aligned}</equation>其中<equation>C_{1}</equation>为任意常数.

因此，<equation>\text {原 积 分} = \frac {\mathrm {e} ^ {2 x} \arctan \sqrt {\mathrm {e} ^ {x} - 1}}{2} - \frac {1}{6} \left(\mathrm {e} ^ {x} - 1\right) ^ {\frac {3}{2}} - \frac {1}{2} \sqrt {\mathrm {e} ^ {x} - 1} + C,</equation>其中 C为任意常数.

---

**2016年第2题 | 选择题 | 4分 | 答案: D**

2. 已知函数<equation>f(x)=\left\{\begin{array}{l l}2(x-1),&x<1,\\ \ln x,&x\geqslant 1,\end{array} \right.</equation>则 f(x)的一个原函数是（    ）

A.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1),}&{x\geqslant 1.}\\ \end{array} \right.</equation>B.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)-1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>C.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x+1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>D.<equation>F(x)=\left\{\begin{array}{l l}{(x-1)^{2},}&{x<1,}\\ {x(\ln x-1)+1,}&{x\geqslant 1.}\\ \end{array} \right.</equation>

答案: D

**解析:**解（法一）当 x < 1时，<equation>F (x) = \int 2 (x - 1) \mathrm {d} x = (x - 1) ^ {2} + C _ {1};</equation>当 x≥1时，<equation>F (x) = \int \ln x \mathrm {d} x = x (\ln x - 1) + C _ {2},</equation>其中<equation>C_{1}, C_{2}</equation>均为任意常数.

进一步，由于<equation>F(x)</equation>是<equation>f(x)</equation>在<equation>(-\infty , + \infty)</equation>上的一个原函数，故<equation>F(x)</equation>在<equation>x = 1</equation>处应连续.<equation>\lim _ {x \rightarrow 1 ^ {-}} F (x) = \lim _ {x \rightarrow 1 ^ {-}} \left(x - 1\right) ^ {2} + C _ {1} = C _ {1}, \quad \lim _ {x \rightarrow 1 ^ {+}} F (x) = \lim _ {x \rightarrow 1 ^ {+}} x \left(\ln x - 1\right) + C _ {2} = C _ {2} - 1.</equation>若<equation>F ( x )</equation>连续，则<equation>C_{1}=C_{2}-1.</equation>选项D中，<equation>C_{1}=0, C_{2}=1, F(x)</equation>连续，应选D.

（法二）首先，由于<equation>F ( x )</equation>是<equation>f ( x )</equation>的原函数，故必连续，而四个选项中的<equation>F ( x )</equation>均是分段函数，于是我们可以分别考察<equation>F ( x )</equation>在分界点处的连续性.

选项A：<equation>\lim_{x\to 1^{-}}F(x)=0,\lim_{x\to 1^{+}}F(x)=-1.F(x)</equation>不连续.

选项B：<equation>\lim_{x\to 1^{-}}F(x)=\lim_{x\to 1^{+}}F(x)=0=F(1). F(x)</equation>连续.

选项C：<equation>\lim_{x\to 1^{-}}F(x) = 0</equation>，<equation>\lim_{x\to 1^{+}}F(x) = 2.F(x)</equation>不连续.

选项D：<equation>\lim_{x\to 1^{-}}F(x) = \lim_{x\to 1^{+}}F(x) = 0 = F(1).F(x)</equation>连续.

由上可排除选项A与选项C.

选项B与选项D的差别在于函数表达式.

计算<equation>f(x)</equation>在<equation>[1, +\infty)</equation>上的原函数，得<equation>\int f (x) \mathrm {d} x = \int \ln x \mathrm {d} x = x (\ln x - 1) + C,</equation>其中 C为任意常数.比较（1）式与选项B、选项D，可排除选项B.应选D.

---


### 常微分方程


#### 一阶非齐次线性微分方程

**2025年第18题 | 解答题 | 12分**
18. 已知函数 f(u)在区间 （0，<equation>+ \infty</equation>）内具有2阶导数，记<equation>g ( x,y)=f\left(\frac{x}{y}\right)</equation>，若 g(x,y)满足<equation>x ^ {2} \frac {\partial^ {2} g}{\partial x ^ {2}} + x y \frac {\partial^ {2} g}{\partial x \partial y} + y ^ {2} \frac {\partial^ {2} g}{\partial y ^ {2}} = 1,</equation>且<equation>g ( x,x)=1,\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{2}{x}</equation>，求 f(u).
**答案: **<equation>f ( u ) = \frac { 1 } { 2 } \left( \ln u \right)^{2}+2 \ln u+1.</equation>
**解析: **解 根据链式法则，<equation>\frac {\partial g}{\partial x} = f ^ {\prime} \left(\frac {x}{y}\right) \cdot \frac {1}{y}, \quad \frac {\partial g}{\partial y} = f ^ {\prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right),</equation><equation>\frac {\partial^ {2} g}{\partial x ^ {2}} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \frac {1}{y ^ {2}},</equation><equation>\frac {\partial^ {2} g}{\partial x \partial y} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) \cdot \frac {1}{y} - \frac {1}{y ^ {2}} f ^ {\prime} \left(\frac {x}{y}\right) = - \frac {x}{y ^ {3}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {1}{y ^ {2}} f ^ {\prime} \left(\frac {x}{y}\right),</equation><equation>\frac {\partial^ {2} g}{\partial y ^ {2}} = f ^ {\prime \prime} \left(\frac {x}{y}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) \cdot \left(- \frac {x}{y ^ {2}}\right) + \frac {2 x}{y ^ {3}} f ^ {\prime} \left(\frac {x}{y}\right) = \frac {x ^ {2}}{y ^ {4}} f ^ {\prime \prime} \left(\frac {x}{y}\right) + \frac {2 x}{y ^ {3}} f ^ {\prime} \left(\frac {x}{y}\right).</equation>代入<equation>x^{2}\frac{\partial^{2}g}{\partial x^{2}}+xy\frac{\partial^{2}g}{\partial x\partial y}+y^{2}\frac{\partial^{2}g}{\partial y^{2}}=1</equation>可得<equation>\frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) - \frac {x}{y} f ^ {\prime} \left(\frac {x}{y}\right) + \frac {x ^ {2}}{y ^ {2}} f ^ {\prime \prime} \left(\frac {x}{y}\right) + \frac {2 x}{y} f ^ {\prime} \left(\frac {x}{y}\right) = 1.</equation>整理可得<equation>\frac{x^2}{y^2} f^{\prime \prime}\left(\frac{x}{y}\right) + \frac{x}{y} f^{\prime}\left(\frac{x}{y}\right) = 1.</equation>令<equation>u=\frac{x}{y}</equation>，可得<equation>u^{2}f^{\prime \prime}(u)+u f^{\prime}(u)=1.</equation>下面用两种方法解该方程

（法一）整理<equation>u^{2}f^{\prime \prime}(u)+u f^{\prime}(u)=1</equation>可得<equation>f^{\prime \prime}(u)+\frac{1}{u} f^{\prime}(u)=\frac{1}{u^{2}}.</equation>这是一个可降阶微分方程.令<equation>p=f^{\prime}(u)</equation>，则该方程化为<equation>p^{\prime}+\frac{p}{u}=\frac{1}{u^{2}}.</equation>由一阶非齐次线性微分方程的通解公式可得<equation>p = \mathrm {e} ^ {\int \left(- \frac {1}{u}\right) \mathrm {d} u} \left(\int \frac {1}{u ^ {2}} \cdot \mathrm {e} ^ {\int \frac {1}{u} \mathrm {d} u} \mathrm {d} u + C _ {1}\right) = \frac {1}{u} \left(\int \frac {1}{u} \mathrm {d} u + C _ {1}\right) = \frac {1}{u} \left(\ln u + C _ {1}\right),</equation>其中<equation>C_{1}</equation>为待定常数.

由<equation>\frac{\partial g}{\partial x}=f^{\prime}\left(\frac{x}{y}\right)\cdot \frac{1}{y}</equation>可得<equation>\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{1}{x} f^{\prime}(1),</equation>结合<equation>\frac{\partial g}{\partial x}\bigg|_{(x,x)}=\frac{2}{x}</equation>可得<equation>f^{\prime}(1)=2.</equation>代入<equation>f^{\prime}(u)</equation><equation>= \frac{1}{u} (\ln u + C_1)</equation>可得<equation>C_{1}=2.</equation>于是，<equation>f^{\prime}(u)=\frac{1}{u}(\ln u+2).</equation>进一步积分可得<equation>f (u) = \int \frac {1}{u} (\ln u + 2) \mathrm {d} u = \int \ln u \mathrm {d} (\ln u) + \int \frac {2}{u} \mathrm {d} u = \frac {1}{2} (\ln u) ^ {2} + 2 \ln u + C _ {2},</equation>其中<equation>C_{2}</equation>为待定常数.

由<equation>g(x,x) = 1</equation>可得<equation>f(1) = 1</equation>，代入<equation>f(u) = \frac{1}{2} (\ln u)^{2} + 2\ln u + C_{2}</equation>可得<equation>C_{2} = 1.</equation>因此，<equation>f(u)=\frac{1}{2} (\ln u)^{2}+2\ln u+1.</equation>（法二）注意到<equation>u^{2} f^{\prime \prime}(u) + uf^{\prime}(u) = 1</equation>是欧拉方程

令<equation>u=\mathrm{e}^{\prime}.</equation>于是，<equation>\frac {\mathrm {d} f}{\mathrm {d} t} = \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \frac {\mathrm {d} u}{\mathrm {d} t} = \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} f}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \frac {\mathrm {d} u}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} f}{\mathrm {d} u} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} f}{\mathrm {d} u ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} f}{\mathrm {d} t}.</equation>由此可得<equation>\frac{\mathrm{d}f}{\mathrm{d}u} = \mathrm{e}^{-t}\frac{\mathrm{d}f}{\mathrm{d}t},\frac{\mathrm{d}^2f}{\mathrm{d}u^2} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^2f}{\mathrm{d}t^2} -\frac{\mathrm{d}f}{\mathrm{d}t}\right)</equation>，于是<equation>u^{2}f^{\prime \prime}(u) = \frac{\mathrm{d}^2f}{\mathrm{d}t^2} -\frac{\mathrm{d}f}{\mathrm{d}t},uf^{\prime}(u) = \frac{\mathrm{d}f}{\mathrm{d}t}</equation>代入<equation>u^{2}f^{\prime \prime}(u)</equation><equation>+uf^{\prime}(u) = 1</equation>可得<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1.</equation>这是一个二阶常系数非齐次线性微分方程，其对应的齐次方程的特征方程为<equation>\lambda^2 = 0</equation>，特征根为<equation>\lambda_{1,2} = 0</equation>.于是，该齐次方程的解为<equation>y = C_{1} + C_{2} t</equation>，其中<equation>C_{1}, C_{2}</equation>为待定常数.

由于0是特征方程的二重根，故可设<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>的特解<equation>y^{*} = At^{2}</equation>. 将<equation>y^{*} = At^{2}</equation>代入<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>可得2A<equation>= 1</equation>，即<equation>A = \frac{1}{2}</equation>.由此可得<equation>y^{*} = \frac{1}{2} t^{2}</equation>，进一步可得<equation>\frac{\mathrm{d}^2f}{\mathrm{d}t^2} = 1</equation>的解为<equation>y = C_{1} + C_{2}t + \frac{1}{2} t^{2}</equation>.由<equation>u = \mathrm{e}^{t}</equation>可得<equation>t = \ln u</equation>，从而<equation>f(u) = C_{1} + C_{2}\ln u + \frac{1}{2}(\ln u)^{2}</equation>.计算可得<equation>f^{\prime}(u) = \frac{1}{u}(\ln u + C_{2})</equation>同法一可得<equation>f(1) = 1,f^{\prime}(1) = 2</equation>，代入<equation>f(u),f^{\prime}(u)</equation>的表达式解得<equation>\left\{ \begin{array}{l} C_{1} = 1, \\ C_{2} = 2 \end{array} \right.</equation>因此，<equation>f ( u ) = \frac { 1 } { 2 } \left( \ln u \right)^{2}+2 \ln u+1.</equation>

---

**2022年第17题 | 解答题 | 10分**
17. (本题满分10分）

设函数 y(x)是微分方程<equation>y^{\prime}+\frac{1}{2\sqrt{x}} y=2+\sqrt{x}</equation>的满足条件 y(1)=3的解，求曲线 y=y(x)的渐近线.
**答案: **<equation>y=2 x</equation>为曲线<equation>y=2 x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.
**解析: **解 根据求解公式，<equation>y = \mathrm {e} ^ {- \int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\int \frac {1}{2 \sqrt {x}} \mathrm {d} x} \mathrm {d} x + C _ {0} \right] = \mathrm {e} ^ {- \sqrt {x}} \left[ \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x + C _ {0} \right].</equation>下面计算<equation>\int (2 + \sqrt{x})\mathrm{e}^{\sqrt{x}}\mathrm{d}x.</equation>令<equation>u=\sqrt{x}</equation>，则<equation>x=u^{2}</equation>，<equation>\mathrm{d}x=2u\mathrm{d}u.</equation><equation>\begin{aligned} \int (2 + \sqrt {x}) \mathrm {e} ^ {\sqrt {x}} \mathrm {d} x \xlongequal {u = \sqrt {x}} 2 \int (2 + u) u \mathrm {e} ^ {u} \mathrm {d} u &= 2 \left(\int u ^ {2} \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 \left[ \int u ^ {2} \mathrm {d} \left(\mathrm {e} ^ {u}\right) + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u \right] = 2 \left(u ^ {2} \mathrm {e} ^ {u} - \int 2 u \mathrm {e} ^ {u} \mathrm {d} u + \int 2 u \mathrm {e} ^ {u} \mathrm {d} u\right) \\ &= 2 u ^ {2} \mathrm {e} ^ {u} + C _ {1} = 2 x \mathrm {e} ^ {\sqrt {x}} + C _ {1}. \end{aligned}</equation>将该结果代入（1）式，可得<equation>y = \mathrm {e} ^ {- \sqrt {x}} \left(2 x \mathrm {e} ^ {\sqrt {x}} + C\right) = 2 x + C \mathrm {e} ^ {- \sqrt {x}},</equation>其中<equation>C</equation>为待定常数. 代入<equation>y(1) = 3</equation>，可得<equation>3 = 2 + C \cdot \mathrm{e}^{-1}</equation>，解得<equation>C = \mathrm{e}</equation>.

因此，<equation>y ( x ) = 2 x + \mathrm {e} ^ {1 - \sqrt {x}} , x \in ( 0, + \infty).</equation>由于函数<equation>y(x) = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>在<equation>(0, +\infty)</equation>内连续，且<equation>\lim_{x\to 0^{+}}y(x) = \mathrm{e}</equation>，故曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有铅直渐近线.

又因为<equation>\lim_{x\to +\infty}y(x) = \lim_{x\to +\infty}\left(2x + \mathrm{e}^{1 - \sqrt{x}}\right) = +\infty</equation>，所以曲线<equation>y = 2x + \mathrm{e}^{1 - \sqrt{x}}</equation>没有水平渐近线.

下面计算斜渐近线.<equation>\lim _ {x \rightarrow + \infty} \frac {y (x)}{x} = \lim _ {x \rightarrow + \infty} \frac {2 x + \mathrm {e} ^ {1 - \sqrt {x}}}{x} = 2,</equation><equation>\lim _ {x \rightarrow + \infty} [ y (x) - 2 x ] = \lim _ {x \rightarrow + \infty} \mathrm {e} ^ {1 - \sqrt {x}} = 0.</equation>因此，<equation>y=2x</equation>为曲线<equation>y=2x+\mathrm{e}^{1-\sqrt{x}}</equation>的斜渐近线，也是唯一的渐近线.

---

**2019年第15题 | 解答题 | 10分**
15. (本题满分10分)

设函数 y(x)是微分方程<equation>y^{\prime}+xy=\mathrm{e}^{-\frac{x^{2}}{2}}</equation>满足条件 y(0)=0的特解.

I. 求 y(x) ;

II. 求曲线 y=y(x)的凹凸区间及拐点.
**答案: **（I）<equation>y ( x )=x \mathrm{e}^{- \frac{x^{2}}{2}};</equation>（Ⅱ）凹区间为<equation>(-\sqrt{3},0)</equation>和<equation>(\sqrt{3},+\infty)</equation>，凸区间为<equation>(-\infty,-\sqrt{3})</equation>和<equation>(0,\sqrt{3})</equation>，拐点为<equation>(-\sqrt{3},-\sqrt{3} \mathrm{e}^{- \frac{3}{2}}),(0,0)</equation>和<equation>(\sqrt{3},\sqrt{3} \mathrm{e}^{- \frac{3}{2}}).</equation>
**解析: **（I）由一阶非齐次线性微分方程的求解公式可得，<equation>y = \mathrm {e} ^ {\int (- x) \mathrm {d} x} \left(\int \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot \mathrm {e} ^ {\int x \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \left(\int 1 \mathrm {d} x + C\right) = x \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + C \mathrm {e} ^ {- \frac {x ^ {2}}{2}},</equation>其中 C为待定常数.

代入<equation>x = 0</equation>，<equation>y(0) = 0</equation>可得，<equation>C = 0.</equation>因此，<equation>y = x\mathrm{e}^{-\frac{x^2}{2}}.</equation>（Ⅱ）分别计算<equation>y^{\prime}, y^{\prime\prime}.</equation><equation>y ^ {\prime} = \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + x \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot (- x) = \left(1 - x ^ {2}\right) \mathrm {e} ^ {- \frac {x ^ {2}}{2}},</equation><equation>y ^ {\prime \prime} = (- 2 x) \mathrm {e} ^ {- \frac {x ^ {2}}{2}} + \left(1 - x ^ {2}\right) \cdot \mathrm {e} ^ {- \frac {x ^ {2}}{2}} \cdot (- x) = \left(x ^ {3} - 3 x\right) \mathrm {e} ^ {- \frac {x ^ {2}}{2}}.</equation>令<equation>y^{\prime \prime}=0</equation>，可得<equation>x=0</equation><equation>x=\pm \sqrt{3}</equation>.当<equation>x < -\sqrt{3}</equation>时，<equation>y^{\prime \prime} < 0</equation>；当<equation>-\sqrt{3} < x < 0</equation>时，<equation>y^{\prime \prime} > 0</equation>；当<equation>0 < x < \sqrt{3}</equation>时，<equation>y^{\prime \prime} < 0</equation>；当<equation>x > \sqrt{3}</equation>时，<equation>y^{\prime \prime} > 0.</equation>因此，<equation>y=y(x)</equation>的凹区间为<equation>(-\sqrt{3},0)</equation>和<equation>(\sqrt{3},+\infty)</equation>，凸区间为<equation>(-\infty,-\sqrt{3})</equation>和<equation>(0,\sqrt{3})</equation>。拐点共有3个：<equation>(-\sqrt{3},-\sqrt{3}\mathrm{e}^{-\frac{3}{2}}),(0,0),(\sqrt{3},\sqrt{3}\mathrm{e}^{-\frac{3}{2}}).</equation>

---

**2018年第18题 | 解答题 | 10分**
18. (本题满分10分)

已知微分方程<equation>y^{\prime}+y=f(x)</equation>，其中 f(x)是 R上的连续函数.

I. 若 f(x)=x，求方程的通解;

II. 若 f(x)是周期为 T的函数，证明：方程存在唯一的以 T为周期的解.
**答案: **（I）<equation>y=x-1+C\mathrm{e}^{-x}</equation>，其中C为任意常数； （Ⅱ）证明略.
**解析: **解（I）若<equation>f ( x )=x</equation>，则<equation>y^{\prime}+y=f ( x )</equation>是一阶非齐次线性微分方程根据求解公式，可得已知方程的通解为<equation>\begin{aligned} y &= \mathrm {e} ^ {- \int \mathrm {d} x} \left(\int x \cdot \mathrm {e} ^ {\int \mathrm {d} x} \mathrm {d} x + C\right) = \mathrm {e} ^ {- x} \left(\int x \cdot \mathrm {e} ^ {x} \mathrm {d} x + C\right) \\ &= \mathrm {e} ^ {- x} \left[ (x - 1) \mathrm {e} ^ {x} + C \right] = x - 1 + C \mathrm {e} ^ {- x}, \end{aligned}</equation>其中 C为任意常数.

（Ⅱ）下面证明方程<equation>y^{\prime} + y = f(x)</equation>的以<equation>T</equation>为周期的解存在.

根据求解公式，可得已知方程的通解为<equation>y (x) = \mathrm {e} ^ {- x} \left[ \int f (x) \mathrm {e} ^ {x} \mathrm {d} x + C ^ {\prime} \right] = \mathrm {e} ^ {- x} \left[ \int_ {0} ^ {x} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right],</equation>其中 C为任意常数.

于是，<equation>\begin{aligned} y (x + T) &= \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {x + T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right] = \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {T} ^ {x + T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + C \right] \\ \underline {{= u = t - T}} \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {0} ^ {x} f (u + T) \mathrm {e} ^ {u + T} \mathrm {d} u + C \right] \\ \underline {{= \frac {f (u + T) = f (u)}{2}}} \mathrm {e} ^ {- x - T} \left[ \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \mathrm {e} ^ {T} \int_ {0} ^ {x} f (u) \mathrm {e} ^ {u} \mathrm {d} u + C \right] \\ &= \mathrm {e} ^ {- x} \left[ \mathrm {e} ^ {- T} \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + \int_ {0} ^ {x} f (u) \mathrm {e} ^ {u} \mathrm {d} u + C \mathrm {e} ^ {- T} \right]. \end{aligned}</equation>比较 y(x)与 y(x+T).若<equation>\mathrm{e}^{-x}\left[ \mathrm{e}^{-T}\int_{0}^{T}f(t)\mathrm{e}^{t}\mathrm{d}t+\int_{0}^{x}f(u)\mathrm{e}^{u}\mathrm{d}u+C\mathrm{e}^{-T}\right]=\mathrm{e}^{-x}\left[ \int_{0}^{x}f(t)\mathrm{e}^{t}\mathrm{d}t+C\right]</equation>即<equation>\mathrm {e} ^ {- T} \int_ {0} ^ {T} f (t) \mathrm {e} ^ {t} \mathrm {d} t + G \mathrm {e} ^ {- T} = C,</equation>则<equation>y ( x+T)=y ( x ), y ( x )</equation>是以T为周期的解.解（1）式得<equation>C=\frac{\int_{0}^{T} f ( t ) \mathrm{e}^{t} \mathrm{d} t}{\mathrm{e}^{T}-1}.</equation>由于T为一常数，故C为一确定常数.

因此，若<equation>f(x)</equation>是周期为<equation>T</equation>的函数，则方程<equation>y^{\prime} + y = f(x)</equation>存在以<equation>T</equation>为周期的解.

下面证明方程<equation>y^{\prime} + y = f(x)</equation>的以<equation>T</equation>为周期的解唯一.

假设<equation>y_{1}, y_{2}</equation>是方程<equation>y^{\prime} + y = f(x)</equation>的两个不同的以<equation>T</equation>为周期的解，则<equation>y_{1} - y_{2}</equation>为齐次线性微分方程<equation>y^{\prime} + y = 0</equation>的解，且<equation>y_{1} - y_{2}</equation>也是以<equation>T</equation>为周期的函数. 解<equation>y^{\prime} + y = 0</equation>可得<equation>y = C_{0}\mathrm{e}^{-x}</equation>，其中<equation>C_{0}</equation>为任意常数. 于是，<equation>y_{1} - y_{2} = C_{0}\mathrm{e}^{-x}</equation>，但是该函数不是以<equation>T</equation>为周期的函数. 矛盾.

综上所述，若<equation>f ( x )</equation>是周期为<equation>T</equation>的函数，则方程<equation>y^{\prime}+y=f ( x )</equation>存在唯一的以<equation>T</equation>为周期的解.

---

**2016年第3题 | 选择题 | 4分 | 答案: A**
3. 若<equation>y=(1+x^{2})^{2}-\sqrt{1+x^{2}},</equation><equation>y=(1+x^{2})^{2}+\sqrt{1+x^{2}}</equation>是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的两个解，则 q(x) =（    )

A.<equation>3 x(1+x^{2})</equation>B.<equation>- 3 x(1+x^{2})</equation>C.<equation>\frac{x}{1+x^{2}}</equation>D.<equation>- \frac{x}{1+x^{2}}</equation>
答案: A
**解析: **解 令<equation>y_{1}=(1+x^{2})^{2}-\sqrt{1+x^{2}}, y_{2}=(1+x^{2})^{2}+\sqrt{1+x^{2}}.</equation>由于<equation>y_{1}, y_{2}</equation>均是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的解，故<equation>y_{2}-y_{1}=2\sqrt{1+x^{2}}</equation>是对应的齐次线性方程<equation>y^{\prime}+p(x)y=0</equation>的解.将解代入方程中得到<equation>\frac {2 x}{\sqrt {1 + x ^ {2}}} + 2 p (x) \sqrt {1 + x ^ {2}} = 0,</equation>从而<equation>p ( x ) = - \frac { x } { 1 + x ^ { 2 } } .</equation>由于<equation>y_{1}, y_{2}</equation>是微分方程<equation>y^{\prime}+p(x)y=q(x)</equation>的解，故<equation>\frac{y_{1}+y_{2}}{2}=(1+x^{2})^{2}</equation>也是该微分方程的解.将解代入方程中得到<equation>4 x \left(1 + x ^ {2}\right) - \frac {x}{1 + x ^ {2}} \cdot \left(1 + x ^ {2}\right) ^ {2} = q (x),</equation>即<equation>q ( x ) = 3 x \left( 1+x^{2} \right).</equation>应选A.

---

**2011年第10题 | 填空题 | 4分**
10. 微分方程<equation>y' + y = \mathrm{e}^{-x}\cos x</equation>满足条件<equation>y(0) = 0</equation>的解为<equation>y = \underline{\quad}</equation>
**解析: **利用求解公式可得，<equation>y=\mathrm{e}^{-\int\mathrm{d} x}\left(\int\mathrm{e}^{-x}\cos x\mathrm{e}^{\int\mathrm{d} x}\mathrm{d} x+C\right)=\mathrm{e}^{-x}\left(\int\cos x\mathrm{d} x+C\right)=\mathrm{e}^{-x}(\sin x+C).</equation>将 y(0) = 0 代入上式得到 C = 0，于是所求解为 y =<equation>\mathrm{e}^{-x}\sin x.</equation>

---


#### 其他方程

**2024年第14题 | 填空题 | 5分**

14. 微分方程<equation>y^{\prime}=\frac{1}{(x+y)^{2}}</equation>满足条件 y(1)=0的解为 ___

**答案:**<equation>\arctan (x + y) = y + \frac {\pi}{4}</equation>

**解析:**解 令<equation>u=x+y</equation>，则<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=1+\frac{\mathrm{d}y}{\mathrm{d}x}</equation>，原方程化为<equation>\frac{\mathrm{d}u}{\mathrm{d}x}-1=\frac{1}{u^{2}}</equation>，即<equation>\frac{\mathrm{d}u}{\mathrm{d}x}=\frac{1+u^{2}}{u^{2}}.</equation>这是一个可分离变量的微分方程，分离变量可得<equation>\left(1-\frac{1}{1+u^{2}}\right)\mathrm{d}u=\mathrm{d}x.</equation>方程两端同时积分可得<equation>u-\arctan u=x+C.</equation>由<equation>y(1)=0</equation>可得，<equation>u(1)=1.</equation>代入<equation>u-\arctan u=x+C</equation>可得<equation>1-\frac{\pi}{4}=1+C,</equation>解得<equation>C=-\frac{\pi}{4}.</equation>于是，<equation>u-\arctan u=x-\frac{\pi}{4}.</equation>将<equation>u=x+y</equation>代回<equation>u-\arctan u=x-\frac{\pi}{4}</equation>并整理可得<equation>y-\arctan(x+y)+\frac{\pi}{4}=0.</equation>

---

**2021年第13题 | 填空题 | 5分**

13. 欧拉方程<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>满足条件<equation>y(1)=1, y^{\prime}(1)=2</equation>的解为<equation>y=</equation>___.

**答案:**<equation>x^{2}.</equation>

**解析:**解 由初始条件<equation>y ( 1 ) = 1, y^{\prime} ( 1 ) = 2</equation>可知应在<equation>x > 0</equation>的范围内求解.

令<equation>x = \mathrm{e}^{t}</equation>. 于是，<equation>\frac {\mathrm {d} y}{\mathrm {d} t} = \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}.</equation><equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} = \frac {\mathrm {d} \left(\frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t}\right)}{\mathrm {d} t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \frac {\mathrm {d} x}{\mathrm {d} t} \cdot \mathrm {e} ^ {t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} x} \cdot \mathrm {e} ^ {t} = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} x ^ {2}} \cdot \mathrm {e} ^ {2 t} + \frac {\mathrm {d} y}{\mathrm {d} t}.</equation>从而，<equation>y^{\prime} = \mathrm{e}^{-t}\frac{\mathrm{d}y}{\mathrm{d}t}, y^{\prime \prime} = \mathrm{e}^{-2t}\left(\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}\right).</equation>因此，<equation>xy^{\prime} = \frac{\mathrm{d}y}{\mathrm{d}t}, x^{2}y^{\prime \prime} = \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} - \frac{\mathrm{d}y}{\mathrm{d}t}.</equation>代入<equation>x^{2} y^{\prime \prime}+x y^{\prime}-4 y=0</equation>可得<equation>\frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - \frac {\mathrm {d} y}{\mathrm {d} t} + \frac {\mathrm {d} y}{\mathrm {d} t} - 4 y = \frac {\mathrm {d} ^ {2} y}{\mathrm {d} t ^ {2}} - 4 y = 0.</equation><equation>\frac{\mathrm{d}^2y}{\mathrm{d}t^2} - 4y = 0</equation>是一个二阶常系数齐次线性微分方程，其特征方程为<equation>r^2 - 4 = 0</equation>，特征根为<equation>r_{1,2} = \pm 2.</equation>于是，该方程的解为<equation>y = C_{1}\mathrm{e}^{2t} + C_{2}\mathrm{e}^{-2t} = C_{1}x^{2} + C_{2}x^{-2}</equation>，其中<equation>C_{1},C_{2}</equation>为待定常数. 从而，<equation>y^{\prime} = 2C_{1}x - 2C_{2}x^{-3}.</equation>代入 y（1）=1可得<equation>1=C_{1}+C_{2}</equation>代入<equation>y^{\prime}(1)=2</equation>可得<equation>2=2 C_{1}-2 C_{2}</equation>解得<equation>C_{1}=1,C_{2}=0.</equation>综上所述，原方程的解为<equation>y=x^{2}.</equation>

---


#### 常系数齐次线性微分方程

**2023年第2题 | 选择题 | 5分 | 答案: C**

2. 若微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>的解在<equation>(-\infty,+\infty)</equation>上有界，则（    )

A. a < 0,b > 0 B. a > 0,b > 0 C. a = 0,b > 0 D. a = 0,b < 0

答案: C

**解析:**解 由于二阶常系数齐次线性微分方程必有零解，而零解为有界解，故微分方程<equation>y^{\prime \prime}+ay^{\prime}+by=0</equation>必然存在<equation>(-\infty , +\infty)</equation>上的有界解.本题实际上是要求此方程的所有解都有界.

微分方程<equation>y^{\prime \prime} + a y^{\prime} + b y = 0</equation>的特征方程为<equation>\lambda^{2} + a \lambda + b = 0.</equation>- 若<equation>\Delta=a^{2}-4 b>0</equation>，则特征方程有两个不同实根<equation>\lambda_{1},\lambda_{2}</equation>，从而至少有一个实根非零.此时，微分方程的解为<equation>y=C_{1}\mathrm{e}^{\lambda_{1}x}+C_{2}\mathrm{e}^{\lambda_{2}x}.</equation>取<equation>C_{1} = C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}\left(\mathrm{e}^{\lambda_{1}x} + \mathrm{e}^{\lambda_{2}x}\right) = +\infty</equation>或<equation>\lim_{x\to +\infty}\left(\mathrm{e}^{\lambda_{1}x} + \mathrm{e}^{\lambda_{2}x}\right) = +\infty</equation>. 该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b=0</equation>，则特征方程有两个相同实根<equation>\lambda</equation>.此时，微分方程的解为<equation>y=(C_{1}+ C_{2} x) \mathrm{e}^{\lambda x}.</equation>取<equation>C_{1} = 0, C_{2} = 1</equation>，则<equation>\lim_{x\to -\infty}x\mathrm{e}^{\lambda x} = \infty</equation>或<equation>\lim_{x\to +\infty}x\mathrm{e}^{\lambda x} = \infty</equation>. 该解在<equation>(-\infty , +\infty)</equation>上无界.

- 若<equation>\Delta=a^{2}-4 b<0</equation>，则特征方程有一对共轭复根<equation>\lambda_{1,2}=\alpha\pm\beta\mathrm{i}</equation>.此时，微分方程的解为<equation>y=\mathrm{e}^{\alpha x}\left(C_{1}\cos \beta x+C_{2}\sin \beta x\right).</equation>当<equation>\alpha \neq 0</equation>时，取<equation>C_{1} = 1, C_{2} = 0</equation>，所得解<equation>y = \mathrm{e}^{\alpha x}\cos \beta x</equation>是<equation>(-\infty , + \infty)</equation>上的无界函数.

当<equation>\alpha=0</equation>时，微分方程的解为<equation>y=C_{1}\cos \beta x+C_{2}\sin \beta x</equation>.对任意常数<equation>C_{1},C_{2}</equation>，该解在<equation>(-\infty, +\infty)</equation>上均有界.根据求根公式，<equation>\lambda_{1,2}=-\frac{a}{2}\pm \frac{\sqrt{4b-a^{2}}}{2}\mathrm{i}</equation>，即<equation>\alpha=-\frac{a}{2}.</equation>于是，<equation>a=0.</equation>结合<equation>a^{2}-4b<0</equation>可知，<equation>b>0.</equation>因此，<equation>a=0,b>0.</equation>应选C.

---

**2020年第11题 | 填空题 | 4分**

11. 设函数 f(x)满足<equation>f^{\prime\prime}(x)+af^{\prime}(x)+f(x)=0(a>0)</equation>，且 f(0)=m，<equation>f^{\prime}(0)=n</equation>，则<equation>\int_{0}^{+\infty}f(x)\mathrm{d}x=</equation>___

**答案:**## n+am.
