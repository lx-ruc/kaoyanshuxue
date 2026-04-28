#### 五、二阶常系数非齐次线性微分方程

此种方程的一般形式为

<equation>y ^ {(n)} + p _ {1} y ^ {(n - 1)} + p _ {2} y ^ {(n - 2)} + \dots + p _ {n} y = 0,</equation>

其中<equation>p_{i}(i = 1,2,\dots ,n)</equation>为常数，相应的特征方程为

<equation>\lambda^ {n} + p _ {1} \lambda^ {n - 1} + \dots + p _ {n - 1} \lambda + p _ {n} = 0.</equation>

特征方程的根与通解的关系为：

<equation>\textcircled{1}</equation>若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>是<equation>n</equation>个互异实根，则方程的通解为

<equation>y (x) = C _ {1} \mathrm {e} ^ {\lambda_ {1} x} + C _ {2} \mathrm {e} ^ {\lambda_ {2} x} + \dots + C _ {n} \mathrm {e} ^ {\lambda_ {n} x}.</equation>

<equation>\textcircled{2}</equation>若<equation>\lambda = \lambda_0</equation>为特征方程的<equation>k(k\leqslant n)</equation>重实根，则方程的通解中含有

<equation>\left(C _ {1} + C _ {2} x + \dots + C _ {k} x ^ {k - 1}\right) \mathrm {e} ^ {\lambda x}.</equation>

<equation>\textcircled{3}</equation>若<equation>\alpha \pm \beta</equation>为特征方程的<equation>k</equation>重共轭复根，则方程的通解中含有

<equation>\begin{array}{l} \mathrm {e} ^ {\alpha x} \left[ \left(C _ {1} + C _ {2} x + \dots + C _ {k} x ^ {k - 1}\right) \cos \beta x + \right. \\ \left(D _ {1} + D _ {2} x + \dots + D _ {k} x ^ {k - 1}\right) \sin \beta x ]. \\ \end{array}</equation>


二阶常系数非齐次线性微分方程的一般形式为

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x),</equation>

其中 p, q是常数.

求特解<equation>y^{*}</equation>的待定系数法：

---

<equation>\textcircled{1}</equation>若

<equation>f (x) = P _ {m} (x) \mathrm {e} ^ {a x},</equation>

其中<equation>P_{m}(x)</equation>为<equation>x</equation>的<equation>m</equation>次多项式，则待定特解<equation>y^{*}</equation>的形式为

<equation>y ^ {*} = x ^ {k} Q _ {m} (x) \mathrm {e} ^ {a x},</equation>

其中<equation>Q_{m}(x)</equation>是与<equation>P_{m}(x)</equation>同次的多项式，调节系数

<equation>k = \left\{ \begin{array}{ll}0, & \alpha \text{不是特征方程的特征根，} \\ 1, & \alpha \text{是特征方程的单特征根，} \\ 2, & \alpha \text{是特征方程的二重特征根。} \end{array} \right.</equation>

将<equation>y^{*} = x^{k}Q_{m}(x)\mathrm{e}^{ax}</equation>代入方程

<equation>y ^ {\prime \prime} + p y ^ {\prime} + q y = f (x),</equation>

就可以求出<equation>Q_{m}(x).</equation>

<equation>\textcircled{2}</equation>若

<equation>f (x) = \mathrm {e} ^ {\alpha x} \left[ P _ {n} (x) \cos \beta x + Q _ {m} (x) \sin \beta x \right],</equation>

其中<equation>P_{n}(x), Q_{m}(x)</equation>分别为<equation>x</equation>的<equation>n</equation>次，<equation>m</equation>次多项式，则待定特解<equation>y^{*}</equation>的形式为

<equation>y ^ {*} = x ^ {k} \mathrm {e} ^ {\mathrm {a} x} \left[ M _ {i} (x) \cos \beta x + N _ {i} (x) \sin \beta x \right],</equation>

其中<equation>l = \max \{m,n\}</equation>，<equation>M_{l}(x)</equation>，<equation>N_{l}(x)</equation>是两个待定的<equation>l</equation>次多项式，调节系数

<equation>k = \left\{ \begin{array}{l l} 0, & \alpha + \beta \mathrm {i} \text {不 是 特 征 方 程 的 特 征 根}, \\ 1, & \alpha + \beta \mathrm {i} \text {是 特 征 方 程 的 特 征 根}. \end{array} \right.</equation>

---


