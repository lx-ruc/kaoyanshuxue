#### 2. 行列式按一行（列）展开

在<equation>n</equation>阶行列式<equation>D = |a_{ij}|</equation>中，划掉元素<equation>a_{ij}</equation>所在第<equation>i</equation>行和第<equation>j</equation>列的所有元素后，余下<equation>(n - 1)^{2}</equation>个元素按照原有次序构成一个<equation>(n - 1)</equation>阶行列式，称之为元素<equation>a_{ij}</equation>在<equation>D</equation>中的余子式，记作<equation>M_{ij}</equation>，即

<equation>M _ {j} = \left| \begin{array}{c c c c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 (j - 1)} & a _ {1 (j + 1)} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 (j - 1)} & a _ {2 (j + 1)} & \dots & a _ {2 n} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {(i - 1) 1} & a _ {(i - 1) 2} & \dots & a _ {(i - 1) (j - 1)} & a _ {(i - 1) (j + 1)} & \dots & a _ {(i - 1) n} \\ a _ {(i + 1) 1} & a _ {(i + 1) 2} & \dots & a _ {(i + 1) (j - 1)} & a _ {(i + 1) (j + 1)} & \dots & a _ {(i + 1) n} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n (j - 1)} & a _ {n (j + 1)} & \dots & a _ {m} \end{array} \right|</equation>

记<equation>A_{ij} = (-1)^{i+j}M_{ij}</equation>，称作元素<equation>a_{ij}</equation>的代数余子式.


n阶行列式<equation>D</equation>等于其任一行(列)各元素与其代数余子式乘积之和，即

<equation>\begin{array}{l} D = a _ {i 1} A _ {i 1} + a _ {i 2} A _ {i 2} + \dots + a _ {i n} A _ {i n} \\ = \sum_ {j = 1} ^ {n} a _ {i j} A _ {i j} \quad (i = 1, 2, \dots , n) \quad (\text {按 第} i \text {行 展 开}) \\ = a _ {1 j} A _ {1 j} + a _ {2 j} A _ {2 j} + \dots + a _ {n j} A _ {n j} \\ \end{array}</equation>

---


