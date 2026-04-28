#### 协方差与相关系数

**2025年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量 X服从正态分布 N(-1,1), Y服从正态分布 N(1,2), 若 X与 X+2Y不相关，则 X与 X-Y的相关系数为（    ）

A.<equation>\frac{1}{3}</equation>B.<equation>\frac{1}{2}</equation>C.<equation>\frac{2}{3}</equation>D.<equation>\frac{3}{4}</equation>

答案: D

**解析:**解 由于 X服从正态分布 N（-1，1），Y服从正态分布 N（1，2），故 D（X）=1，D（Y）=2. 又因为 X与 X+2Y不相关，所以<equation>\operatorname{Cov}(X, X + 2 Y) = \operatorname{Cov}(X, X) + 2 \operatorname{Cov}(X, Y) = D (X) + 2 \operatorname{Cov}(X, Y) = 1 + 2 \operatorname{Cov}(X, Y) = 0.</equation>于是，<equation>\operatorname{Cov}(X, Y) = -\frac{1}{2}.</equation>进一步可得<equation>\operatorname {C o v} (X, X - Y) = \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) = D (X) - \operatorname {C o v} (X, Y) = 1 - \left(- \frac {1}{2}\right) = \frac {3}{2}.</equation><equation>D (X - Y) = D (X) + D (Y) - 2 \operatorname {C o v} (X, Y) = 1 + 2 - 2 \cdot \left(- \frac {1}{2}\right) = 4.</equation>因此，X与X-Y的相关系数<equation>\rho = \frac {\operatorname {C o v} (X , X - Y)}{\sqrt {D (X)} \sqrt {D (X - Y)}} = \frac {\frac {3}{2}}{1 \cdot 2} = \frac {3}{4}.</equation>应选 D.

---

**2023年第16题 | 填空题 | 5分**

16. 设随机变量 X 与 Y 相互独立，且<equation>X \sim B ( 1, p )</equation><equation>Y \sim B ( 2, p )</equation><equation>p \in( 0, 1 )</equation>，则<equation>X+Y</equation>与<equation>X-Y</equation>的相关系数为___.

**答案:**<equation>- \frac {1}{3}.</equation>

**解析:**解 由<equation>X\sim B(1,p)</equation>可知，<equation>D ( X )=p ( 1-p ).</equation>由<equation>Y\sim B ( 2,p)</equation>可知，<equation>D ( Y )=2 p ( 1-p ).</equation><equation>X+Y</equation>与<equation>X-Y</equation>的相关系数<equation>\rho=\frac{\operatorname{Cov}(X+Y,X-Y)}{\sqrt{D(X+Y)}\sqrt{D(X-Y)}}.</equation>由于 X与 Y相互独立，故<equation>D (X + Y) = D (X) + D (Y) = 3 p (1 - p),</equation><equation>D (X - Y) = D (X) + D (Y) = 3 p (1 - p).</equation>由协方差的性质可得，<equation>\begin{aligned} \operatorname {C o v} (X + Y, X - Y) &= \operatorname {C o v} (X, X) - \operatorname {C o v} (X, Y) + \operatorname {C o v} (Y, X) - \operatorname {C o v} (Y, Y) \\ &= D (X) - D (Y) = - p (1 - p). \end{aligned}</equation>因此，<equation>\rho = \frac {- p (1 - p)}{\sqrt {3 p (1 - p)} \sqrt {3 p (1 - p)}} = - \frac {1}{3}.</equation>

---

**2022年第8题 | 选择题 | 5分 | 答案: D**

8. 设随机变量<equation>X\sim N(0,4)</equation>，随机变量<equation>Y\sim B\left(3,\frac{1}{3}\right)</equation>，且 X，Y不相关，则<equation>D(X-3Y+1)=</equation>(    )

A.2 B.4 C.6 D.10

答案: D

**解析:**解 由于 X~ N（0,4），Y~ B<equation>\left( 3, \frac{1}{3} \right)</equation>，故 X的方差 D（X）=4，Y的方差<equation>D (Y) = 3 \times \frac {1}{3} \times \left(1 - \frac {1}{3}\right) = \frac {2}{3}.</equation>又因为<equation>X, Y</equation>不相关，所以<equation>\operatorname{Cov}(X, Y) = 0.</equation>由方差的性质，<equation>\begin{aligned} D (X - 3 Y + 1) &= D (X - 3 Y) = D (X) + D (3 Y) - 2 \operatorname {C o v} (X, 3 Y) \\ &= D (X) + 9 D (Y) - 6 \operatorname {C o v} (X, Y) = 4 + 9 \times \frac {2}{3} - 0 = 1 0. \end{aligned}</equation>因此，应选D.

---

**2022年第10题 | 选择题 | 5分 | 答案: B**

10. 设二维随机变量（X，Y）的概率分布为

<table border="1"><tr><td>X\ Y</td><td>0</td><td>1</td><td>2</td></tr><tr><td>-1</td><td>0.1</td><td>0.1</td><td>b</td></tr><tr><td>1</td><td>a</td><td>0.1</td><td>0.1</td></tr></table>

若事件<equation>\{\max \{X,Y\}=2\}</equation>与事件<equation>\{\min \{X,Y\}=1\}</equation>相互独立，则<equation>\operatorname{Cov}(X,Y)=</equation>(    )

A. -0.6 B. -0.36 C. 0 D. 0.48

答案: B

**解析:**解记事件 A = {<equation>\max \{ X, Y \}=2</equation>} ，事件 B = {<equation>\min \{ X, Y \}=1</equation>} .由于事件 A与B相互独立，故 P（AB）=P(A)P(B).

分别计算 P（A），P（B），P（AB）.<equation>P (A) = P \left\{\max \left\{X, Y \right\} = 2 \right\} = P \left\{Y = 2 \right\} = b + 0. 1.</equation><equation>P (B) = P \left\{\min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 1 \right\} + P \left\{X = 1, Y = 2 \right\} = 0. 1 + 0. 1 = 0. 2.</equation><equation>P (A B) = P \left\{\max \left\{X, Y \right\} = 2, \min \left\{X, Y \right\} = 1 \right\} = P \left\{X = 1, Y = 2 \right\} = 0. 1.</equation>于是，<equation>0. 1 = ( b + 0. 1 ) \times 0. 2</equation>，解得 b=0.4. 进一步，由联合分布律中各概率之和为1，即<equation>0. 1 + 0. 1</equation><equation>+ b + a + 0. 1 + 0. 1 = 1</equation>可得，a=0.2.

XY的可能取值为-2，-1，0，1，2.<equation>P \{X Y = - 2 \} = P \{X = - 1, Y = 2 \} = 0. 4.</equation><equation>P \left\{X Y = - 1 \right\} = P \left\{X = - 1, Y = 1 \right\} = 0. 1.</equation><equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = 0. 1.</equation><equation>P \{X Y = 2 \} = P \{X = 1, Y = 2 \} = 0. 1.</equation><equation>P \{X Y = 0 \} = 1 - 0. 4 - 0. 1 - 0. 1 - 0. 1 = 0. 3.</equation>分别计算 E（X），E（Y），E（XY）.<equation>E (X) = - 1 \times (0. 1 + 0. 1 + 0. 4) + 1 \times (0. 2 + 0. 1 + 0. 1) = - 0. 2.</equation><equation>E (Y) = 0 \times (0. 1 + 0. 2) + 1 \times (0. 1 + 0. 1) + 2 \times (0. 4 + 0. 1) = 1. 2.</equation><equation>E (X Y) = (- 2) \times 0. 4 + (- 1) \times 0. 1 + 0 \times 0. 3 + 1 \times 0. 1 + 2 \times 0. 1 = - 0. 6.</equation>因此，<equation>\operatorname {C o v} (X, Y) = E (X Y) - E (X) E (Y) = - 0. 6 - (- 0. 2) \times 1. 2 = - 0. 3 6.</equation>应选B.

---

**2021年第16题 | 填空题 | 5分**

16. 甲，乙两个盒子中各装有2个红球和2个白球，先从甲盒中任取一球，观察颜色后放入乙盒中，再从乙盒中任取一个球，令 X, Y分别表示从甲盒和乙盒中取到的红球个数，则 X与 Y的相关系数为___

**答案:**# 1 5.

**解析:**解 根据相关系数的计算公式，X与Y的相关系数为<equation>\rho = \frac {\operatorname {C o v} (X , Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}}.</equation>下面分别计算 X, Y的分布律与数字特征.

取球模型为等可能模型.

X的可能取值为0，1.取到白球，则<equation>X=0</equation>，取到红球，则<equation>X=1.</equation><equation>P \{X = 0 \} = \frac {1}{2}, \quad P \{X = 1 \} = \frac {1}{2}.</equation>于是，<equation>E ( X ) = \frac {1}{2}, E \left( X^{2}\right) = \frac {1}{2}, D ( X ) = \frac {1}{2} - \left(\frac {1}{2}\right)^{2} = \frac {1}{4}.</equation>Y的可能取值为0，1. 若从甲盒中取出的是白球，则后来乙盒中共有2个红球和3个白球，取到红球的概率为<equation>\frac{2}{5}</equation>即在 X=0发生的条件下 Y=1发生的概率为<equation>\frac{2}{5}</equation>；若从甲盒中取出的是红球，则后来乙盒中共有3个红球和2个白球，取到红球的概率为<equation>\frac{3}{5}</equation>即在 X=1发生的条件下 Y=1发生的概率为<equation>\frac{3}{5}.</equation><equation>\begin{aligned} P \{Y = 1 \} &= P \{Y = 1 \mid X = 0 \} P \{X = 0 \} + P \{Y = 1 \mid X = 1 \} P \{X = 1 \} \\ &= \frac {2}{5} \times \frac {1}{2} + \frac {3}{5} \times \frac {1}{2} = \frac {1}{2}. \end{aligned}</equation><equation>P \{Y = 0 \} = 1 - P \{Y = 1 \} = 1 - \frac {1}{2} = \frac {1}{2}.</equation>于是，<equation>E ( Y )=\frac{1}{2}, E ( Y^{2} )=\frac{1}{2}, D ( Y )=\frac{1}{2}-\left(\frac{1}{2}\right)^{2}=\frac{1}{4}.</equation>XY的可能取值为0,1.<equation>P \{X Y = 1 \} = P \{X = 1, Y = 1 \} = P \{Y = 1 \mid X = 1 \} P \{X = 1 \} = \frac {3}{5} \times \frac {1}{2} = \frac {3}{1 0}.</equation><equation>P \{X Y = 0 \} = 1 - \frac {3}{1 0} = \frac {7}{1 0}.</equation>于是，<equation>E ( X Y ) = P \{ X Y = 1 \} \times 1 + P \{ X Y = 0 \} \times 0 = \frac {3}{1 0}.</equation>因此，<equation>\rho = \frac {E (X Y) - E (X) E (Y)}{\sqrt {D (X)} \sqrt {D (Y)}} = \frac {\frac {3}{1 0} - \frac {1}{2} \times \frac {1}{2}}{\frac {1}{2} \times \frac {1}{2}} = \frac {\frac {1}{2 0}}{\frac {1}{4}} = \frac {1}{5}.</equation>

---


