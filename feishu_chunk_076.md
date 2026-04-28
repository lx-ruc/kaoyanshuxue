#### 多元函数微分学的几何应用

**2023年第12题 | 填空题 | 5分**

12. 曲面<equation>z=x+2y+\ln(1+x^2+y^2)</equation>在点<equation>(0,0,0)</equation>处的切平面方程为 ___

**答案:**<equation>x + 2 y - z = 0.</equation>

**解析:**解记曲面<equation>z = x + 2y + \ln (1 + x^{2} + y^{2})</equation>为<equation>\varSigma, F(x,y,z) = x + 2y + \ln (1 + x^{2} + y^{2}) - z</equation>，则曲面<equation>\varSigma</equation>的方程为<equation>F(x,y,z) = 0</equation>，其在点（x,y,z）处的一个法向量为<equation>\left(\frac {\partial F}{\partial x}, \frac {\partial F}{\partial y}, \frac {\partial F}{\partial z}\right) = \left(1 + \frac {2 x}{1 + x ^ {2} + y ^ {2}}, 2 + \frac {2 y}{1 + x ^ {2} + y ^ {2}}, - 1\right).</equation>代入点（0，0，0）的坐标可得曲面<equation>\varSigma</equation>在点（0，0，0）处的法向量为（1，2，-1）.因此，曲面<equation>\varSigma</equation>在点 （0，0，0）处的切平面方程为<equation>(x - 0) + 2 (y - 0) - (z - 0) = 0,</equation>即<equation>x+2y-z=0.</equation>

---

**2018年第2题 | 选择题 | 4分 | 答案: B**

2. 过点（1,0,0），（0,1,0），且与曲面<equation>z=x^{2}+y^{2}</equation>相切的平面为（    )

A.<equation>z=0</equation>与<equation>x+y-z=1</equation>B.<equation>z=0</equation>与<equation>2 x+2 y-z=2</equation>C.<equation>x=y</equation>与<equation>x+y-z=1</equation>D.<equation>x=y</equation>与<equation>2 x+2 y-z=2</equation>

答案: B

**解析:**解（法一）记<equation>F ( x,y,z) = z - x^{2} - y^{2}</equation>，则曲面<equation>z = x^{2} + y^{2}</equation>的方程为<equation>F ( x,y,z) = 0.</equation>根据曲面的切平面的定义，曲面<equation>F ( x,y,z) = 0</equation>在点（x,y,z）处的切平面的一个法向量为<equation>(-2x,-2y,1)</equation>（也可以取作（2x,2y，-1）).于是，该点处的切平面的点法式方程为<equation>- 2 x (X - x) - 2 y (Y - y) + (Z - z) = 0.</equation>由于所求切平面过点（1，0，0），（0，1，0），故将这两点的坐标分别代入（1）式可得，<equation>- 2 x (1 - x) + 2 y ^ {2} - z \frac {x ^ {2} + y ^ {2} = z}{- 2 x + z} - 2 x + z = 0,</equation><equation>2 x ^ {2} - 2 y (1 - y) - z \xlongequal {x ^ {2} + y ^ {2} = z} - 2 y + z = 0.</equation>联立<equation>\left\{ \begin{array}{l l} z = 2x, \\ z = 2y, \\ z = x^{2} + y^{2}. \end{array} \right.</equation>由前两个方程可得<equation>x = y</equation>，代入第三个方程可得<equation>2x = 2x^{2}</equation>，解得<equation>x = 0</equation>或<equation>x = 1</equation>. 当<equation>x = 0</equation>时，<equation>y = 0, z = 0</equation>；当<equation>x = 1</equation>时，<equation>y = 1, z = 2</equation>. 从而切点坐标为（0,0,0）或（1,1,2）.

将这两个切点的坐标分别代入（1）式，可得所求切平面的方程分别为 Z=0与<equation>2 X+2 Y-Z=2</equation>因此，应选B.

（法二）排除法.

由于点（1，0，0）和点（0，1，0）均位于所求切平面上，而这两点均不满足方程 x=y，故可排除选项C和选项D.

另一方面，曲面<equation>z=x^{2}+y^{2}</equation>上点（x,y,z）处的切平面的法向量应与（2x，2y，-1）共线.平面<equation>x+y-z=1</equation>的一个法向量为（1，1，-1).若其为切平面，则<equation>\frac{2x}{1}=\frac{2y}{1}=\frac{-1}{-1}</equation>，切点坐标应满足<equation>x=\frac{1}{2}</equation><equation>y=\frac{1}{2}</equation>.代入<equation>z=x^{2}+y^{2}</equation>得<equation>z=\frac{1}{2}</equation>.但是<equation>\left(\frac{1}{2},\frac{1}{2},\frac{1}{2}\right)</equation>并不满足方程<equation>x+y-z=1</equation>.于是，选项A也不正确.

由排除法可知，应选B.

---

**2014年第9题 | 填空题 | 4分**

9. 曲面<equation>z=x^{2}(1-\sin y)+y^{2}(1-\sin x)</equation>在点（1,0,1）处的切平面方程为 ___

**答案:**<equation>2 x - y - z - 1 = 0.</equation>

**解析:**从而切平面的方程为<equation>2 ( x - 1 ) - ( y - 0 ) - ( z - 1 ) = 0</equation>即<equation>2 x - y - z - 1 = 0.</equation>

---

**2013年第2题 | 选择题 | 4分 | 答案: A**

2. 曲面<equation>x^{2}+\cos(xy)+yz+x=0</equation>在点（0，1，-1）处的切平面方程为（    ）

A.<equation>x-y+z=-2</equation>B.<equation>x+y+z=0</equation>C.<equation>x-2y+z=-3</equation>D.<equation>x-y-z=0</equation>

答案: A

**解析:**解 令<equation>F ( x,y,z) = x^{2} + \cos ( x y ) + y z + x</equation>，则曲面在点（0，1，-1）处的法向量为<equation>\left. \left(\frac {\partial F}{\partial x}, \frac {\partial F}{\partial y}, \frac {\partial F}{\partial z}\right) \right| _ {(0, 1, - 1)} = \left(2 x - y \sin (x y) + 1, - x \sin (x y) + z, y\right) \Big | _ {(0, 1, - 1)} = (1, - 1, 1).</equation>从而曲面在点（0,1，-1）处的切平面方程为<equation>x - ( y - 1 ) + ( z + 1 ) = 0</equation>，即<equation>x - y + z = - 2</equation>，选A.

---


