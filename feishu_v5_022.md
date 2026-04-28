---


#### (3)矩阵的乘法


<equation>\textcircled{2} (\mathbf{A} + \mathbf{B}) + \mathbf{C} = \mathbf{A} + (\mathbf{B} + \mathbf{C})</equation>;

<equation>\textcircled{3} k(\mathbf{A} + \mathbf{B}) = k\mathbf{A} + k\mathbf{B}</equation>;

<equation>\textcircled{4} ( k+l ) \mathbf{A}=k \mathbf{A}+l \mathbf{A}.</equation>


设<equation>\mathbf{A} = (a_{ij})_{m\times n},\mathbf{B} = (b_{ij})_{n\times k}</equation>（注意<equation>\mathbf{A}</equation>的列数和<equation>\mathbf{B}</equation>的行数相等），定义矩阵

<equation>\mathbf {C} = \left(c _ {i j}\right) _ {m \times k},</equation>

其中

<equation>c _ {i j} = a _ {i 1} b _ {1 j} + a _ {i 2} b _ {2 j} + \dots + a _ {i n} b _ {n j} = \sum_ {k = 1} ^ {n} a _ {i k} b _ {k j},</equation>

称为矩阵<equation>A</equation>与矩阵<equation>B</equation>的乘积，记作<equation>C = AB</equation>

数乘的运算性质：

<equation>\textcircled{1}</equation><equation>\mathbf{(A B) C}=\mathbf{A( B C)}</equation>（结合律）；

<equation>\textcircled{2}</equation><equation>\mathbf{A} (\mathbf{B}+\mathbf{C})=\mathbf{A B}+\mathbf{A C},</equation>

（<equation>\mathbf{B}+\mathbf{C} )\mathbf{A}=\mathbf{B}\mathbf{A}+\mathbf{C}\mathbf{A}</equation>（分配律）；

<equation>\textcircled{3}</equation><equation>( k A ) B=A ( k B )=k ( A B )</equation>（数与乘积的结合律).

注<equation>\textcircled{1}</equation>不是任意两个矩阵<equation>A</equation>与<equation>B</equation>都能相乘的，必须有<equation>A</equation>的列数和<equation>B</equation>的行数相等.

<equation>\textcircled{2}</equation>矩阵乘法一般来说不满足交换律，即一般情况下，<equation>\mathbf{A B}\neq \mathbf{B A}.</equation>

<equation>\textcircled{3}</equation>矩阵的运算也不满足消去律. 即由<equation>AB = AC</equation>且<equation>A \neq O</equation>, 得不出<equation>B = C</equation>.

---


#### （4）方阵的乘幂运算


<equation>\textcircled{4}</equation>零因子定律不成立，即由<equation>AB = O</equation>并不能得到<equation>A = O</equation>或<equation>B = O.</equation>


如果矩阵<equation>A</equation>为方阵，则定义<equation>A^{n} = \underbrace{A \cdot A \cdots A}_{n \text{个} A}</equation>为矩阵<equation>A</equation>的<equation>n</equation>次幂.规定<equation>A^{0} = E</equation>（单位矩阵）.

乘幂的运算性质：

<equation>\textcircled{1}</equation><equation>A^{k} \cdot A^{l} = A^{k+l}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}^{k}\right)^{l}=\mathbf{A}^{k l}.</equation>

注 一般情况下，<equation>(\mathbf{A}\cdot \mathbf{B})^{k}\neq A^{k}\cdot B^{k}.</equation>

(5) 矩阵的转置

设<equation>A_{m\times n} = \left[ \begin{array}{cccc} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{array} \right]_{m\times n}</equation>，定义A的转置

矩阵为

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {2 1} & \dots & a _ {m 1} \\ a _ {1 2} & a _ {2 2} & \dots & a _ {m 2} \\ \vdots & \vdots & & \vdots \\ a _ {1 n} & a _ {2 n} & \dots & a _ {m n} \end{array} \right] _ {n \times m},</equation>

即转置矩阵<equation>A^{\mathrm{T}}</equation>的第<equation>i</equation>行第<equation>j</equation>列元素等于原矩阵<equation>A</equation>的第<equation>j</equation>行第<equation>i</equation>列元素.

转置的运算规则：

---

<equation>\textcircled{1} (\mathbf{A}^{\mathrm{T}})^{\mathrm{T}} = \mathbf{A}</equation>;

<equation>\textcircled{2}</equation><equation>\left( \mathbf{A}+\mathbf{B}\right)^{\mathrm{T}}=\mathbf{A}^{\mathrm{T}}+\mathbf{B}^{\mathrm{T}};</equation>

<equation>\textcircled{3}</equation><equation>\mathbf{A B} )^{\mathrm{T}}=\mathbf{B}^{\mathrm{T}} \mathbf{A}^{\mathrm{T}};</equation>

<equation>\textcircled{4} ( k \mathbf{A} )^{\mathrm{T}}=k \cdot \mathbf{A}^{\mathrm{T}}.</equation>

(6) 方阵的行列式

若<equation>\mathbf{A} = (a_{i j})_{n\times n},\mathbf{B} = (b_{i j})_{n\times n}</equation>，则

<equation>| \mathbf {A} | = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right|,</equation>

且<equation>|kA| = k^{n}|A|, |AB| = |A||B|.</equation>

(7) 矩阵的求逆运算

<equation>\textcircled{1}</equation>逆矩阵的定义及定理

若<equation>A, B</equation>均为<equation>n</equation>阶方阵，且满足<equation>AB = BA = E</equation>，则称<equation>A</equation>是可逆矩阵，又称<equation>B</equation>是<equation>A</equation>的逆矩阵，记作<equation>B = A^{-1}</equation>.

(a)若矩阵<equation>A</equation>可逆，则<equation>A</equation>的逆矩阵<equation>A^{-1}</equation>是唯一的.

(b) 矩阵<equation>A</equation>可逆的充分必要条件是<equation>|A| \neq 0</equation>.

(c) 若<equation>|A| \neq 0</equation>，则<equation>A^{-1} = \frac{1}{|A|} A^{*}</equation>，其中

<equation>\boldsymbol {A} ^ {*} = \left[ \begin{array}{c c c c} A _ {1 1} & A _ {2 1} & \dots & A _ {n 1} \\ A _ {1 2} & A _ {2 2} & \dots & A _ {n 2} \\ \vdots & \vdots & & \vdots \\ A _ {1 n} & A _ {2 n} & \dots & A _ {m} \end{array} \right],</equation>

---


#### 3. 矩阵经过运算后秩的变化规律


称为<equation>\mathbf{A}</equation>的伴随矩阵（其中<equation>A_{y}</equation>是元素<equation>a_{y}</equation>的代数余子式）.

由<equation>A^{+}</equation>的构成，可得到以下重要的公式：

<equation>A A ^ {*} = A ^ {*} A = | A | E.</equation>

<equation>\textcircled{2}</equation>求逆运算的运算规则

若<equation>\mathbf{A},\mathbf{B}</equation>均为 n阶可逆矩阵，则

(a)<equation>(\mathbf{A}^{-1})^{-1} = \mathbf{A}</equation>;

(b) 若<equation>k\neq 0</equation>为常数，则<equation>(kA)^{-1} = \frac{1}{k} A^{-1}</equation>；

(c)<equation>(\mathbf{A B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1};</equation>

(d)<equation>A^{\mathrm{T}}</equation>也可逆，且<equation>(A^{\mathrm{T}})^{-1} = (A^{-1})^{\mathrm{T}};</equation>

(e)<equation>|\mathbf{A}^{-1}| = |\mathbf{A}|^{-1}.</equation>


在<equation>A_{m \times n}</equation>中，任取<equation>k</equation>行、<equation>k</equation>列，在这<equation>k</equation>行<equation>k</equation>列的交错处有<equation>k^2</equation>个元素，这<equation>k^2</equation>个元素按原有的次序构成一个<equation>k</equation>阶行列式，称为<equation>A</equation>的一个<equation>k</equation>阶子式。


在<equation>A_{m \times n}</equation>中，至少有一个<equation>r</equation>阶子式不为零，而所有<equation>r + 1</equation>阶子式全为零，则称<equation>A</equation>的秩为<equation>r</equation>，记作<equation>\operatorname{rank}(A) = r</equation>，简记为<equation>r(A) = r</equation>或<equation>R(A) = r</equation>。


<equation>\textcircled{1}</equation><equation>r(\mathbf{A}^{\mathrm{T}}) = r(\mathbf{A})</equation>;

---


#### 1. 分块矩阵的定义


<equation>\textcircled{2} r ( A_{m \times n} ) \leqslant\min \{ m,n \} ;</equation>

<equation>\textcircled{3}</equation><equation>r(\mathbf{A}) = 0 \Leftrightarrow \mathbf{A} = \mathbf{O}</equation>;

<equation>\textcircled{4}</equation><equation>r(k\mathbf{A}) = \left\{ \begin{array}{ll} r(\mathbf{A}), & k \neq 0, \\ 0, & k = 0; \end{array} \right.</equation>

<equation>\textcircled{5} r(\mathbf{A} + \mathbf{B}) \leqslant r(\mathbf{A}) + r(\mathbf{B})</equation>;

<equation>\textcircled{6} r ( \mathbf{A B} ) \leqslant\min \{ r ( \mathbf{A} ) , r ( \mathbf{B} ) \} ;</equation>

<equation>\textcircled{7}</equation>若有矩阵<equation>A_{m\times n}, B_{n\times s}</equation>，且<equation>AB = O</equation>，且<equation>r(A) + r(B) \leqslant n</equation>；

<equation>\textcircled{8}</equation>若<equation>P, Q</equation>为满秩方阵，则

<equation>r (P A) = r (A) = r (A Q) = r (P A Q);</equation>

<equation>\textcircled{9}</equation>初等变换不改变矩阵的秩. 若<equation>B</equation>是阶梯形矩阵，则<equation>r(B)</equation>等于<equation>B</equation>中非零行的个数；

<equation>\textcircled{10}</equation>关于伴随矩阵<equation>A^{*}</equation>的秩：

<equation>r \left(\boldsymbol {A} ^ {*}\right) = \left\{ \begin{array}{l l} n, r (\boldsymbol {A}) = n, \\ 1, r (\boldsymbol {A}) = n - 1, \\ 0, r (\boldsymbol {A}) \leqslant n - 2. \end{array} \right.</equation>


用贯穿矩阵的横线和纵线（称为分划线）把一个矩阵分成若干小块，每一小块称为原矩阵的子块，一般记作<equation>A_{ij}</equation>，分为子块的矩阵叫做分块矩阵。由于不同的需要，同一矩阵可以有不同的分块方法。例如：

---


#### (2) 数乘


$$

\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ \dots \dots

<equation>\boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} & a _ {3 4} \\ a _ {4 1} & a _ {4 2} & a _ {4 3} & a _ {4 4} \end{array} \right] = \left(\boldsymbol {p} _ {1}, \boldsymbol {p} _ {2}, \boldsymbol {p} _ {3}, \boldsymbol {p} _ {4}\right) _ {1 \times 4}.</equation>


<equation>A, B \in M_{m,n}</equation>，且有相同的分块划分方法：<equation>A = \left(A_{ij}\right)_{s \times t}, B = \left(B_{ij}\right)_{s \times t}</equation>，则

<equation>A + B = \left(A_{ij} + B_{ij}\right)_{s\times l}</equation>（每个对应子块可加）.


设<equation>A = \left(A_{ij}\right)_{s\times t}\in M_{m,n}</equation>，则

<equation>k \boldsymbol {A} = \left(k \boldsymbol {A} _ {i j}\right) _ {s \times t}.</equation>

(3) 转置

若

<equation>\boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 t} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \dots & \boldsymbol {A} _ {2 t} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {s 1} & \boldsymbol {A} _ {s 2} & \dots & \boldsymbol {A} _ {x} \end{array} \right] = \left(\boldsymbol {A} _ {i j}\right) _ {s \times t} \in M _ {m, n},</equation>

---


#### (4)乘法


则

<equation>\boldsymbol {A} ^ {\mathrm {T}} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 1} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s 1} ^ {\mathrm {T}} \\ \boldsymbol {A} _ {1 2} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 2} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s 2} ^ {\mathrm {T}} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {1 t} ^ {\mathrm {T}} & \boldsymbol {A} _ {2 t} ^ {\mathrm {T}} & \dots & \boldsymbol {A} _ {s t} ^ {\mathrm {T}} \end{array} \right],</equation>

即分块矩阵先转置后，再将每个子矩阵分别单独转置即为原矩阵的转置矩阵.


设

<equation>\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 t} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} & \dots & \boldsymbol {A} _ {2 t} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {A} _ {s 1} & \boldsymbol {A} _ {s 2} & \dots & \boldsymbol {A} _ {s t} \end{array} \right] = \left(\boldsymbol {A} _ {i j}\right) _ {s \times t} \in M _ {m, n}, \\ \boldsymbol {B} = \left[ \begin{array}{c c c c} \boldsymbol {B} _ {1 1} & \boldsymbol {B} _ {1 2} & \dots & \boldsymbol {B} _ {1 r} \\ \boldsymbol {B} _ {2 1} & \boldsymbol {B} _ {2 2} & \dots & \boldsymbol {B} _ {2 r} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {B} _ {t 1} & \boldsymbol {B} _ {t 2} & \dots & \boldsymbol {B} _ {t r} \end{array} \right] = \left(\boldsymbol {B} _ {j k}\right) _ {t \times r} \in M _ {m, n}, \\ \boldsymbol {C} = \boldsymbol {A} \boldsymbol {B} = \left[ \begin{array}{c c c c} \boldsymbol {C} _ {1 1} & \boldsymbol {C} _ {1 2} & \dots & \boldsymbol {C} _ {1 r} \\ \boldsymbol {C} _ {2 1} & \boldsymbol {C} _ {2 2} & \dots & \boldsymbol {C} _ {2 r} \\ \vdots & \vdots & & \vdots \\ \boldsymbol {C} _ {s 1} & \boldsymbol {C} _ {s 2} & \dots & \boldsymbol {C} _ {s r} \end{array} \right], \\ \end{array}</equation>

---


#### 3. 分块对角形（对角块）矩阵


其中<equation>C_{ik} = A_{i1}B_{1k} + A_{i2}B_{2k} + \dots + A_{it}B_{tk} = \sum_{j=1}^{i}A_{ij}B_{jk}</equation><equation>(i = 1,\dots,s;k = 1,\dots,r).</equation>


一般地，分块矩阵<equation>A = \left[ \begin{array}{cccc}A_{11} & O & \dots & O\\ O & A_{22} & \dots & O\\ \vdots & \vdots & & \vdots \\ O & O & \dots & A_{s} \end{array} \right],</equation>

简记为<equation>A = \left[ \begin{array}{c c c c} A_{11} & & & \\ & A_{22} & & \\ & & \ddots & \\ & & & A_{ss} \end{array} \right],</equation>其中<equation>A_{ii}</equation>均为小方

阵，则称<equation>A</equation>为对角块矩阵或分块对角形矩阵。若<equation>A, B</equation>均为对角块矩阵，则<equation>A + B, AB</equation>也为对角块矩阵，如：

<equation>\begin{array}{l} \boldsymbol {A} + \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] + \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1} + \boldsymbol {B} _ {1} & & & \\ & \boldsymbol {A} _ {2} + \boldsymbol {B} _ {2} & & \\ & & \ddots & \\ & & & \boldsymbol {A} _ {s} + \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

---


#### 1. 矩阵的初等行（列）变换


其中，<equation>A_{i}, B_{i}</equation>为同阶子矩阵

<equation>\begin{array}{l} \boldsymbol {A} \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {A} _ {2} \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

其中，<equation>A_{i}, B_{i}</equation>为同阶子矩阵

对角块矩阵的逆矩阵公式（设<equation>A_{1}, A_{2}, A_{3}</equation>均可逆）：

<equation>\begin{array}{l} \left[ \begin{array}{c c c} A _ {1} & & \\ & A _ {2} & \\ & & A _ {3} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c c} A _ {1} ^ {- 1} & & \\ & A _ {2} ^ {- 1} & \\ & & A _ {3} ^ {- 1} \end{array} \right], \\ \left[ \begin{array}{c c c} & & A _ {1} \\ & A _ {2} & \\ A _ {3} & & \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c c} & & A _ {3} ^ {- 1} \\ & A _ {2} ^ {- 1} & \\ A _ {1} ^ {- 1} & & \end{array} \right]. \\ \end{array}</equation>


矩阵的初等变换指的是对矩阵施行以下三种行（列）变换：

---


#### (1) 初等行交换矩阵


<equation>\textcircled{1}</equation>交换变换：互换矩阵中的某两行（列）；

<equation>\textcircled{2}</equation>倍乘变换：用一个非零常数<equation>k</equation>乘矩阵的某行(列)；

<equation>\textcircled{3}</equation>倍加变换：将矩阵的某行（列）的 k 倍加到另一行（列）上.


形如

<equation>\left[ \begin{array}{l l l} 0 & 1 & 3 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array} \right], \left[ \begin{array}{c c c c c} 1 & 2 & - 1 & 2 & 5 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 4 & 1 \end{array} \right], \left[ \begin{array}{c c c} 1 & 0 & - 1 \\ 0 & 2 & 3 \\ 0 & 0 & 3 \end{array} \right]</equation>

的矩阵称为阶梯形矩阵.

阶梯形矩阵有以下特征：

<equation>\textcircled{1}</equation>全零行位于矩阵的最下方.

<equation>\textcircled{2}</equation>每个非零行的第一个非零元素<equation>c_{ij}</equation>（亦称主元）的列标<equation>j</equation>随着行标<equation>i</equation>的递增而严格增大.

<equation>\textcircled{3}</equation>任一个矩阵经过若干次初等行（列）变换都可以化成阶梯形矩阵.


将单位矩阵作了一次初等行（列）变换的矩阵称作初等矩阵.

三种初等行（列）变换矩阵：


将单位矩阵的第<equation>i</equation>行、第<equation>j</equation>行交换后所得到的矩阵，记作

---


#### （3）初等行倍加矩阵


<equation>\boldsymbol {P} ((i) \leftrightarrow (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ \ddots & & & & \\ & 0 & \dots & 1 & \\ & \vdots & & \vdots & \\ & 1 & \dots & 0 & \\ & & & \ddots & \\ & & & & 1 \end{array} \right] \leftarrow i \text {行} \quad \leftarrow j \text {行}</equation>

作用：将初等行交换矩阵左乘 A，即若

<equation>P ((i) \leftrightarrow (j)) A = A _ {1},</equation>

则<equation>A_{1}</equation>就是将<equation>A</equation>的第<equation>i</equation>行、第<equation>j</equation>行交换后的结果.


将单位矩阵的第 i 行乘以不为零的常数 k后所得到的矩阵，记作

<equation>\boldsymbol {P} ((k (i)) = \left[ \begin{array}{c c c c} 1 & & & \\ & \ddots & & \\ & & k & \\ & & & \ddots \\ & & & 1 \end{array} \right] \leftarrow i \text {行}.</equation>

作用：若<equation>P(k(i))A = A_{2}</equation>，则<equation>A_{2}</equation>就是将<equation>A</equation>的第<equation>i</equation>行乘上<equation>k</equation>倍后的结果.


将单位矩阵第<equation>i</equation>行的<equation>k</equation>倍加到第<equation>j</equation>行后所得到的矩阵，记作

---


#### （4）初等列交换矩阵


<equation>\boldsymbol {P} (k (i) + (j)) = \left[ \begin{array}{c c c c c c} 1 & & & & & \\ & \ddots & & & & \\ & & 1 & & & \\ & & \vdots & \ddots & & \\ & & k & \dots & 1 & \\ & & & & \ddots & \\ & & & & & 1 \end{array} \right] \leftarrow i \text {行} \leftarrow j \text {行}</equation>

作用：若<equation>\mathbf{P}(k(i) + (j))\mathbf{A} = \mathbf{A}_3</equation>，则<equation>\mathbf{A}_3</equation>就是将<equation>\mathbf{A}</equation>的第<equation>i</equation>行的<equation>k</equation>倍加到第<equation>j</equation>行上的结果.


将单位矩阵第 i列与第 j列交换后所得到的矩阵，记作

<equation>Q ((i) \leftrightarrow (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ \ddots & & & & \\ & 0 \quad \dots & 1 & & \\ & \vdots & & \vdots & \\ & 1 \quad \dots & 0 & & \\ & & & \ddots & \\ & & & & 1 \end{array} \right]</equation>

作用：将初等列交换矩阵右乘<equation>A</equation>，即若<equation>AQ((i)\leftrightarrow(j)) = A_{4}</equation>，则<equation>A_{4}</equation>就是将<equation>A</equation>的第<equation>i</equation>列与第<equation>j</equation>列交换后的结果.

---


#### （6）初等列倍加矩阵


将单位矩阵的第<equation>i</equation>列乘以一个不等于零的常数<equation>k</equation>后得到的矩阵，记作

<equation>Q (k (i)) = \left[ \begin{array}{c c c c} 1 & & & \\ & \ddots & & \\ & & k & \\ & & & \ddots \\ & & & 1 \end{array} \right].</equation>

作用：若<equation>AQ(k(i)) = A_{5}</equation>，则<equation>A_{5}</equation>就是将<equation>\mathbf{A}</equation>的第<equation>i</equation>列乘上<equation>k</equation>倍后的结果.


将单位矩阵第<equation>i</equation>列的<equation>k</equation>倍加到第<equation>j</equation>列后所得到的矩阵，记作

<equation>Q (k (i) + (j)) = \left[ \begin{array}{c c c c c} 1 & & & & \\ & \ddots & & \\ & & 1 \dots k & \\ & & \ddots \vdots & \\ & & & 1 \\ & & & \ddots \\ & & & 1 \\ \uparrow_ {i \text {列}} & \uparrow_ {j \text {列}} \end{array} \right].</equation>

---


#### 6. 用初等行(列)变换法求矩阵的秩


作用：若<equation>A Q (k (i) + (j)) = A_{6}</equation>，则<equation>A_{6}</equation>就是将<equation>A</equation>的第<equation>i</equation>列的<equation>k</equation>倍加到第<equation>j</equation>列上的结果.


<equation>\textcircled{1} P ((i) \leftrightarrow (j)) = Q ((i) \leftrightarrow (j)) = Q ^ {\mathrm {T}} ((i) \leftrightarrow (j));</equation>

<equation>\textcircled{2} \boldsymbol {P} (k (i)) = \boldsymbol {Q} (k (i)) = \boldsymbol {Q} ^ {\mathrm {T}} (k (i));</equation>

<equation>\textcircled{3} \boldsymbol {P} (k (i) + (j)) = \boldsymbol {Q} ^ {\mathrm {T}} (k (i) + (j)).</equation>

即：初等行变换矩阵与同类型的初等列变换矩阵之间为转置关系（事实上前两类是相等的对称矩阵）。


<equation>\textcircled{1}</equation>初等矩阵都是可逆矩阵.

<equation>\textcircled{2}</equation>初等矩阵的逆矩阵也是初等矩阵.

<equation>\textcircled{3}</equation>任一个可逆矩阵经过有限次的初等行变换都可化成单位矩阵.

<equation>\textcircled{4}</equation>一个可逆矩阵可分解为一系列初等矩阵的乘积.


初等行（列）变换不改变矩阵的秩.

矩阵的初等行（列）变换前后，矩阵的秩是相等的，而阶梯形矩阵的秩等于阶梯形矩阵中非零行的个数，由任一个矩阵都可经过若干次初等行（列）变换化成阶梯形矩阵，因此任一个矩阵的秩都可通过初等行（列）变换化成阶梯形矩阵后方便地求得.

---


#### (1)等价


<equation>\textcircled{1}</equation>定义

若矩阵<equation>A</equation>可经过一系列初等行变换和列变换后化成矩阵<equation>B</equation>，则称矩阵<equation>A</equation>与<equation>B</equation>是等价的，记作<equation>A\cong B</equation>

<equation>\textcircled{2}</equation>性质

(a)<equation>A\cong A</equation>;

(b)<equation>A\cong B</equation>，则<equation>B\cong A</equation>;

(c)<equation>A\cong B, B\cong C</equation>，则<equation>A\cong C;</equation>

(d)同型矩阵<equation>\mathbf{A}</equation>与<equation>\mathbf{B}</equation>等价<equation>\Leftrightarrow r(\mathbf{A})=r(\mathbf{B}).</equation>

(2) 相似

<equation>\textcircled{1}</equation>定义

对于同阶方阵<equation>A, B</equation>，若存在<equation>|P| \neq 0</equation>，使<equation>P^{-1}AP = B</equation>，则称<equation>A</equation>与<equation>B</equation>相似，记作<equation>A \sim B</equation>.

<equation>\textcircled{2}</equation>性质

(a)<equation>A\sim A</equation>;

(b)<equation>A\sim B</equation>，则<equation>B\sim A</equation>

(c)<equation>A\sim B, B\sim C</equation>，则<equation>A\sim C;</equation>

(d)若<equation>\mathbf{A}\sim\mathbf{B}</equation>，则<equation>\mathbf{A}^{\mathrm{T}}\sim\mathbf{B}^{\mathrm{T}}</equation>

(e) 若<equation>A, B</equation>可逆且<equation>A\sim B</equation>，则<equation>A^{-1}\sim B^{-1}</equation>；

(f)<equation>A\sim B\Rightarrow A^{n}\sim B^{n}, n</equation>为正整数；

(g)相似矩阵有相同的特征值；

（h）相似矩阵的行列式、秩相等；

---


#### (2)性质


（i）同阶实对称矩阵相似的充要条件是它们有相同的特征值（包括重数）.


对于同阶方阵<equation>A, B</equation>，若存在<equation>|P| \neq 0</equation>，使<equation>P^{\mathrm{T}} A P = B</equation>，则称<equation>A</equation>与<equation>B</equation>合同，记为<equation>A \cong B</equation>.


(a)<equation>A\cong A</equation>;

(b) 若<equation>A\cong B</equation>，则<equation>B\cong A;</equation>

(c) 若<equation>A\cong B, B\cong C</equation>，则<equation>A\cong C;</equation>

（d）同阶实对称矩阵合同的充要条件是秩相等且正惯性指数相等.


<equation>\textcircled{1}</equation>相似<equation>\Rightarrow</equation>等价；

<equation>\textcircled{2}</equation>合同<equation>\Rightarrow</equation>等价；

<equation>\textcircled{3}</equation>若<equation>A</equation>与<equation>B</equation>都是实对称矩阵，则<equation>A</equation>与<equation>B</equation>相似<equation>\Leftrightarrow A</equation>与<equation>B</equation>合同


若存在非零向量<equation>\alpha</equation>，使<equation>A\alpha = \lambda \alpha</equation>，则称<equation>\lambda</equation>为方阵<equation>A</equation>的特征值，<equation>\alpha</equation>是<equation>A</equation>的属于特征值<equation>\lambda</equation>的特征向量.


<equation>\textcircled{1}</equation>若<equation>\lambda</equation>是<equation>A</equation>的特征值，则<equation>\lambda^{k}</equation>是<equation>A^{k}</equation>的特征值.

---


#### 11. 矩阵等价的充要条件


<equation>\textcircled{2}</equation>若<equation>\lambda \neq 0</equation>是<equation>A</equation>的特征值，则<equation>\lambda^{-1}</equation>是<equation>A^{-1}</equation>的特征值.

<equation>\textcircled{3}</equation>若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>是<equation>A</equation>的特征值，则

<equation>\lambda_{1} + \lambda_{2} + \dots +\lambda_{n} = a_{11} + a_{22} + \dots +a_{m}</equation>（A的迹），<equation>\lambda_{1}\lambda_{2}\dots \lambda_{n} = |\mathbf{A}|.</equation>

<equation>\textcircled{4}</equation><equation>\mathbf{A}</equation>与<equation>\mathbf{A}^{\mathrm{T}}</equation>有相同的特征值.

<equation>\textcircled{5}</equation>矩阵 A属于不同特征值的特征向量必线性无关.

<equation>\textcircled{6}</equation>实对称矩阵属于不同特征值的特征向量必正交.


A可逆<equation>\Leftrightarrow</equation><equation>|A| \neq 0 \Leftrightarrow A=P_{1} P_{2}\dots P_{i}</equation>，其中<equation>P_{i}</equation>（<equation>i=1</equation>2，...，l）为初等矩阵

<equation>\Leftrightarrow A\cong E</equation>（<equation>E</equation>为<equation>n</equation>阶单位矩阵）.


<equation>A\cong B\Leftrightarrow</equation>存在可逆矩阵<equation>P, Q</equation>使<equation>PAQ = B</equation>

<equation>\Leftrightarrow r (\mathbf {A}) = r (\mathbf {B}).</equation>

---


### 第三章 向量

#### 2. 线性组合与线性表出


n个数<equation>a_{1}, a_{2}, \dots , a_{n}</equation>组成一个有次序的数组，称为一个n维向量，用<equation>\alpha = (a_{1}, a_{2}, \dots , a_{n})</equation>（称为行向量）或<equation>\alpha = (a_{1}, a_{2}, \dots , a_{n})^{\mathrm{T}}</equation>（称为列向量）来表示.称<equation>a_{i}</equation>为第<equation>i</equation>个分量.若干个同维列向量（或同维行向量）组成的集合称为向量组.

(2) 向量的加法

<equation>\begin{array}{l} \boldsymbol {\alpha} + \boldsymbol {\beta} = \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) + \left(b _ {1}, b _ {2}, \dots , b _ {n}\right) \\ = \left(a _ {1} + b _ {1}, a _ {2} + b _ {2}, \dots , a _ {n} + b _ {n}\right). \\ \end{array}</equation>

(3) 数乘向量

<equation>k \alpha = k \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) = \left(k a _ {1}, k a _ {2}, \dots , k a _ {n}\right).</equation>


(1) 向量组的线性组合

有一组向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>及一组数<equation>k_{1},k_{2},\dots ,k_{s}</equation>，称

<equation>k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s}</equation>

---


#### 3. 向量组的等价


为向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>的一个线性组合.


若向量<equation>\beta</equation>可表示为向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>的一个线性组合，即有<equation>k_{1},k_{2},\dots ,k_{s}</equation>存在，使

<equation>\boldsymbol {\beta} = k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s}</equation>

成立，则称向量<equation>\beta</equation>可由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出（或线性表示）。否则称<equation>\beta</equation>不能由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出.

<equation>\textcircled{1}</equation>一个向量<equation>\beta</equation>能否由一个向量组<equation>\alpha_{1}, \alpha_{2}, \dots, \alpha_{s}</equation>线性表出，等价于以<equation>k_{1}, k_{2}, \dots, k_{s}</equation>为未知量的线性方程组<equation>\beta = k_{1}\alpha_{1} + k_{2}\alpha_{2} + \dots + k_{s}\alpha_{s}</equation>是有解还是无解.

<equation>\textcircled{2}</equation>若<equation>\boldsymbol{\beta}</equation>可由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出，其表现形式（即表出系数）是唯一的还是无穷多种形式，等价于线性方程组<equation>k_{1}\alpha_{1}+k_{2}\alpha_{2}+\dots +k_{s}\alpha_{s}=\boldsymbol{\beta}</equation>在有解时只有唯一解还是无穷多组解.


若向量组（I）<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>中每一个向量<equation>\alpha_{j}(j = 1,2,\dots ,s)</equation>均可由向量组（Ⅱ）<equation>\beta_{1},\beta_{2},\dots ,\beta_{i}</equation>线性表出，则称向量组（I）可由向量组（Ⅱ）线性表出.

若向量组（I）可由向量组（Ⅱ）线性表出，向量组（Ⅱ）也可由向量组（I）线性表出，则称向量组（I）与向量组（Ⅱ）为等价向量组，记作：（I）<equation>\cong</equation>（Ⅱ）.

---


#### 1. 线性相关性的定义


向量组的等价有以下性质：


任一个向量组（I）与自身必等价，即（I）<equation>\cong</equation>（I）。


若向量组（I）<equation>\cong</equation>（Ⅱ），则（Ⅱ）<equation>\cong</equation>（I）.


若向量组（I）<equation>\cong</equation>（Ⅱ），向量组（Ⅱ）<equation>\cong</equation>（Ⅲ），则（I）<equation>\cong</equation>（Ⅲ）.


<equation>\textcircled{1}</equation>现有 s个n维向量<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>，若存在着一组不全为零的数组<equation>k_{1},k_{2},\dots ,k_{s}</equation>，使

<equation>k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s} = \mathbf {0}</equation>

成立，则称向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{r}</equation>是线性相关的向量组.

<equation>\textcircled{2}</equation>现有 s个n维向量<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>

<equation>k _ {1} \boldsymbol {\alpha} _ {1} + k _ {2} \boldsymbol {\alpha} _ {2} + \dots + k _ {s} \boldsymbol {\alpha} _ {s} = \mathbf {0}</equation>

若使

成立，只有

<equation>k _ {1} = 0, k _ {2} = 0, \dots , k _ {s} = 0,</equation>

则称向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>是线性无关的向量组.

---


#### 3. 一些重要的定理与结论


<equation>\textcircled{1}</equation>（判定定理1）<equation>s</equation>个<equation>n</equation>维向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性相关（或线性无关）的充要条件是对应的齐次线性方程组<equation>k_{1}\alpha_{1} + k_{2}\alpha_{2} + \dots +k_{s}\alpha_{s} = 0</equation>有非零解（或只有零解).

推论 n个n维向量<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{n}</equation>线性相关（或线性无关）的充要条件是行列式<equation>|A| = |\alpha_{1},\alpha_{2},\dots ,\alpha_{n}| = 0</equation>（或<equation>\neq 0</equation>）.

<equation>\textcircled{2}</equation>（判定定理2）向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{j}</equation>线性相关（或线性无关）的充要条件是其中至少有一个向量可由其余向量线性表出（或没有一个向量可由其余向量线性表出).


<equation>\textcircled{1}</equation>包含零向量的向量组必定线性相关.

<equation>\textcircled{2}</equation>包含两个相等向量的向量组必定线性相关.

<equation>\textcircled{3}</equation>若一个向量组线性相关，则加上任意多个向量后，新加向量组仍线性相关。（部分相关，全体必相关）

<equation>\textcircled{4}</equation>一个向量组线性无关，取出其中任何一部分也必线性无关.（全体无关，部分必无关）

<equation>\textcircled{5}</equation>任意 n+1个 n维向量必线性相关.（个数大于维数的向量组必线性相关）

<equation>\textcircled{6}</equation>一个向量组线性无关，则在相同位置处增加一个分量后得到的新向量组（可称为加长组）仍线性无关.

---


#### 2. 极大无关组的性质


<equation>\textcircled{7}</equation>一个向量组线性相关，则在相同位置处去掉一个分量后得到的新向量组（可称为缩短组）仍线性相关.

<equation>\textcircled{8}</equation>若<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性无关，而<equation>\beta ,\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性相关，则<equation>\beta</equation>必可由<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>唯一地线性表出.

<equation>\textcircled{9}</equation>设有向量组（I）<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>，向量组（Ⅱ）<equation>\beta_{1}</equation>，<equation>\beta_{2},\dots ,\beta_{r}</equation>中每个向量都可由向量组（I）线性表出，且<equation>t > s</equation>，则向量组（Ⅱ）必线性相关.

<equation>\textcircled{10}</equation>若<equation>\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \dots, \boldsymbol{\beta}_t</equation>可由<equation>\alpha_1, \alpha_2, \dots \alpha_s</equation>线性表出，且<equation>\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \dots, \boldsymbol{\beta}_t</equation>线性无关，则<equation>t \leqslant s</equation>。


若向量组（I）<equation>\alpha_{1},\alpha_{2},\dots,\alpha_{k}</equation>是向量组（Ⅱ）<equation>\alpha_{1},\alpha_{2},\dots,\alpha_{k}</equation>的一个部分组，且向量组（I）满足以下两个条件：<equation>\textcircled{1}</equation>向量组（I）是线性无关的；<equation>\textcircled{2}</equation>从向量组（Ⅱ）中任取一个向量加到向量组（I）中都线性相关，则称向量组（I）是向量组（Ⅱ）的一个极大线性无关组，简称为极大无关组.


<equation>\textcircled{1}</equation>一个向量组与它的任一个极大无关组之间可以互相线性表出（即等价）.

---


#### 1. 向量的内积


<equation>\textcircled{2}</equation>一个向量组的任两个极大无关组之间也等价.

<equation>\textcircled{3}</equation><equation>\textcircled{3}</equation>一个向量组的任两个极大无关组所包含向量的个数必相等.

<equation>\textcircled{4}</equation>设向量组<equation>\beta_{1},\beta_{2},\dots ,\beta_{r}</equation>可由向量组<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}</equation>线性表出，则<equation>r(\beta_{1},\beta_{2},\dots ,\beta_{r})\leqslant r(\alpha_{1},\alpha_{2},\dots ,\alpha_{s})</equation>

<equation>\textcircled{5}</equation>两个等价（即可以互相线性表出）的向量组，其秩必相等.


（三秩相等定理）矩阵<equation>\mathbf{A}</equation>的秩<equation>r(\mathbf{A})= \mathbf{A}</equation>的列秩<equation>= \mathbf{A}</equation>的行秩.


(1) 内积的定义

已知 n维实向量

<equation>\boldsymbol {\alpha} = \left(a _ {1}, a _ {2}, \dots , a _ {n}\right) ^ {\mathrm {T}}, \boldsymbol {\beta} = \left(b _ {1}, b _ {2}, \dots , b _ {n}\right) ^ {\mathrm {T}},</equation>

称

<equation>(\boldsymbol {\alpha}, \boldsymbol {\beta}) = a _ {1} b _ {1} + a _ {2} b _ {2} + \dots + a _ {n} b _ {n} = \sum_ {i = 1} ^ {n} a _ {i} b _ {i} = \boldsymbol {\alpha} ^ {\mathrm {T}} \boldsymbol {\beta}</equation>

为向量<equation>\alpha, \beta</equation>的内积.

内积具有以下的性质：

<equation>\textcircled{1}</equation>对称性

<equation>(\alpha , \beta) = (\beta , \alpha).</equation>

---


#### (1)定义


<equation>\textcircled{2}</equation>线性性

<equation>\begin{array}{l} (\alpha + \beta , \gamma) = (\alpha , \gamma) + (\beta , \gamma), \\ (k \alpha , \beta) = k (\alpha , \beta). \\ \end{array}</equation>


对任意<equation>\alpha\in \mathbf{R}^{n}</equation>，均有（<equation>\alpha,\alpha) \geqslant 0</equation>，且

<equation>(\boldsymbol {\alpha}, \boldsymbol {\alpha}) = 0 \Leftrightarrow \boldsymbol {\alpha} = \mathbf {0}.</equation>


实数<equation>|\alpha| = \sqrt{(\alpha, \alpha)} = \sqrt{\sum_{i=1}^{n} a_i^2}</equation>称为向量<equation>\alpha</equation>的长度（或模）。若<equation>|\alpha| = 1</equation>，则称<equation>\alpha</equation>为单位向量。若<equation>\alpha</equation>不是单位向量，则<equation>\alpha</equation>方向上的单位向量<equation>\alpha_0 = \frac{1}{|\alpha|}\alpha</equation>。


非零向量<equation>\alpha</equation>与<equation>\beta</equation>的夹角的余弦为

<equation>\cos (\alpha , \beta) = \frac {(\alpha , \beta)}{| \alpha | \cdot | \beta |}.</equation>

若<equation>(\alpha ,\beta) = 0</equation>（即<equation>\cos (\alpha ,\beta) = 0</equation>或<equation>(\alpha ,\beta) = \frac{\pi}{2}</equation>），则称<equation>\alpha</equation>与<equation>\beta</equation>正交，记作<equation>\alpha \bot \beta</equation>


有<equation>s</equation>个<equation>n</equation>维向量：<equation>\alpha_{1},\alpha_{2},\dots ,\alpha_{s}(s\leqslant n)</equation>.若每一个向量都是非零向量，且每两个向量都正交，则称向量组

---


#### (2) 施密特正交化方法


<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots ,\boldsymbol{\alpha}_{s}</equation>为一个正交向量组

正交向量组<equation>\boldsymbol{\alpha}_{1},\boldsymbol{\alpha}_{2},\dots \boldsymbol{\alpha}_{s}</equation>用内积表示为：

<equation>(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = 0 (i, j = 1, 2, \dots s; i \neq j)</equation>且<equation>(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) \neq 0 (i = 1, 2, \dots , s)</equation>.


每个向量都是单位向量的正交向量组称为标准正交向量组（或规范正交向量组），即

<equation>\left(\boldsymbol {\alpha} _ {i}, \boldsymbol {\alpha} _ {j}\right) = \left\{ \begin{array}{l l} 0, & \text {当} i \neq j \text {时}, \\ 1, & \text {当} i = j \text {时} \end{array} \right. (i, j = 1, 2, \dots , s).</equation>


用施密特正交化方法可将任意一组线性无关的向量组改造成为标准正交向量组（先正交化再单位化）。若<equation>\alpha_{1}, \alpha_{2}, \dots, \alpha_{n}</equation>是一组线性无关的向量组，令

<equation>\begin{array}{l} \boldsymbol {\beta} _ {1} = \boldsymbol {\alpha} _ {1}, \\ \boldsymbol {\beta} _ {2} = - \frac {\left(\boldsymbol {\alpha} _ {2} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1} , \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} + \boldsymbol {\alpha} _ {2}, \\ \boldsymbol {\beta} _ {3} = - \frac {\left(\boldsymbol {\alpha} _ {3} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\alpha} _ {3} , \boldsymbol {\beta} _ {2}\right)}{\left(\boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {2}\right)} \boldsymbol {\beta} _ {2} + \boldsymbol {\alpha} _ {3}, \dots , \\ \boldsymbol {\beta} _ {n} = \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {1}\right)}{\left(\boldsymbol {\beta} _ {1}, \boldsymbol {\beta} _ {1}\right)} \boldsymbol {\beta} _ {1} - \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {2}\right)}{\left(\boldsymbol {\beta} _ {2}, \boldsymbol {\beta} _ {2}\right)} \boldsymbol {\beta} _ {2} - \dots - \\ \frac {\left(\boldsymbol {\alpha} _ {n} , \boldsymbol {\beta} _ {n - 1}\right)}{\left(\boldsymbol {\beta} _ {n - 1}, \boldsymbol {\beta} _ {n - 1}\right)} \boldsymbol {\beta} _ {n - 1} + \boldsymbol {\alpha} _ {n}, \\ \end{array}</equation>

则<equation>\beta_{1},\beta_{2},\dots ,\beta_{n}</equation>是一组两两正交的向量组.

---


#### (2) 子空间


再令

<equation>\gamma_{i} = \frac{\boldsymbol{\beta}_{i}}{|\boldsymbol{\beta}_{i}|}(i = 1,2,\dots,n)</equation>，其中<equation>|\boldsymbol{\beta}_{i}| = \sqrt{(\boldsymbol{\beta}_{i},\boldsymbol{\beta}_{i})}</equation>，则<equation>\gamma_{1},\gamma_{2},\dots,\gamma_{n}</equation>就是一组由<equation>\alpha_{1},\alpha_{2},\dots,\alpha_{n}</equation>改造成的标准正交向量组.


若<equation>n</equation>阶实矩阵<equation>A</equation>满足<equation>A A^{\mathrm{T}} = A^{\mathrm{T}} A = E</equation>，则称<equation>A</equation>为正交矩阵（即<equation>A^{\mathrm{T}} = A^{-1}</equation>）.

n阶矩阵<equation>A</equation>是正交矩阵的充要条件是：<equation>A</equation>的<equation>n</equation>个列（行）向量两两正交，且每个列（行）向量都是单位向量（即<equation>A</equation>的列（行）向量组为<equation>\mathbf{R}^n</equation>中的一组标准正交向量组).

正交矩阵的行列式不是1就是一1.两个正交矩阵的乘积仍是正交矩阵.


设<equation>V</equation>是<equation>n</equation>维向量的非空集合，且<equation>V</equation>对向量的加法与数乘这两种运算都封闭，则称<equation>V</equation>为向量空间.


设<equation>W</equation>是向量空间<equation>V</equation>的一个非空子集，且<equation>W</equation>中的向量对向量加法与数乘这两种运算也封闭，则称<equation>W</equation>为

---


#### （1）基变换与两组基间的过渡矩阵


V的一个子向量空间，简称为子空间


设<equation>V</equation>是向量空间，若<equation>V</equation>中有一组线性无关的向量组<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>，且<equation>V</equation>中任一个向量都可由<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>线性表出，则称<equation>V</equation>为<equation>n</equation>维的向量空间，记作<equation>V^{n}</equation>，又称<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>为<equation>V^{n}</equation>中的一组基.


设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>是<equation>V^{n}</equation>中的一组基，则对于任意<equation>\alpha \in V^{n},\alpha</equation>均可由基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>唯一地线性表出；

<equation>\boldsymbol {\alpha} = x _ {1} \boldsymbol {\varepsilon} _ {1} + x _ {2} \boldsymbol {\varepsilon} _ {2} + \dots + x _ {n} \boldsymbol {\varepsilon} _ {n},</equation>

称其表出系数<equation>x_{1}, x_{2}, \dots x_{n}</equation>是向量<equation>\alpha</equation>在基<equation>\varepsilon_{1}, \varepsilon_{2}, \dots, \varepsilon_{n}</equation>下的坐标. 坐标往往用列向量来表示：

<equation>\boldsymbol {X} = \left(x _ {1}, x _ {2}, \dots x _ {n}\right) ^ {\mathrm {T}},</equation>

则<equation>\pmb{\alpha} = (\pmb{\varepsilon}_1,\pmb{\varepsilon}_2,\dots ,\pmb{\varepsilon}_n)X.</equation>


设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>与<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>是<equation>n</equation>维向量空间<equation>\mathbf{R}^n</equation>中的两组基，且

<equation>\left\{ \begin{array}{l} \boldsymbol {\eta} _ {1} = a _ {1 1} \boldsymbol {\varepsilon} _ {1} + a _ {2 1} \boldsymbol {\varepsilon} _ {2} + \dots + a _ {n 1} \boldsymbol {\varepsilon} _ {n}, \\ \boldsymbol {\eta} _ {2} = a _ {1 2} \boldsymbol {\varepsilon} _ {1} + a _ {2 2} \boldsymbol {\varepsilon} _ {2} + \dots + a _ {n 2} \boldsymbol {\varepsilon} _ {n}, \\ \dots \\ \boldsymbol {\eta} _ {n} = a _ {1 n} \boldsymbol {\varepsilon} _ {1} + a _ {2 n} \boldsymbol {\varepsilon} _ {2} + \dots + a _ {m n} \boldsymbol {\varepsilon} _ {n}, \end{array} \right.</equation>

---


#### (2)坐标变换


此式称为由基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的基变换公式，称矩阵

<equation>A = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right]</equation>

为由旧基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到新基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的过渡矩阵.

过渡矩阵必是可逆矩阵，上面的基变换公式用矩阵及向量符号可表示为

<equation>\left(\eta_ {1}, \eta_ {2}, \dots , \eta_ {n}\right) = \left(\varepsilon_ {1}, \varepsilon_ {2}, \dots , \varepsilon_ {n}\right) A,</equation>

其中过渡矩阵<equation>A</equation>的第<equation>j</equation>列是<equation>\eta_{j}</equation>在基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>下的坐标列向量.


设<equation>\alpha</equation>是<equation>\mathbf{R}^n</equation>中的任一个向量，<equation>\alpha</equation>在基<equation>\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n</equation>下的坐标为<equation>X = (x_{1}, x_{2}, \dots, x_{n})^{\mathrm{T}}</equation>，在基<equation>\eta_1, \eta_2, \dots, \eta_n</equation>下的坐标为<equation>Y = (y_{1}, y_{2}, \dots, y_{n})^{\mathrm{T}}</equation>，则有

<equation>X = A Y \text {或} Y = A ^ {- 1} X.</equation>

此式即为坐标变换公式，式中的<equation>A</equation>即为基<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>到基<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>的过渡矩阵.

---

(3) 两组标准正交基之间的过渡矩阵是正交矩阵

设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>是<equation>V^{n}</equation>中的一组基，且<equation>(\varepsilon_{i},\varepsilon_{i}) = 1</equation><equation>(\varepsilon_{i},\varepsilon_{j}) = 0(i,j = 1,2,\dots ,n;i\neq j)</equation>，则称<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>为<equation>V^{n}</equation>中的一组标准正交基（或规范正交基）。

设<equation>\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n}</equation>及<equation>\eta_{1},\eta_{2},\dots ,\eta_{n}</equation>都是<equation>\mathbf{R}^n</equation>的标准正交基，且有<equation>(\eta_{1},\eta_{2},\dots ,\eta_{n}) = (\varepsilon_{1},\varepsilon_{2},\dots ,\varepsilon_{n})A</equation>，则<equation>A</equation>必是一个正交矩阵.

---


### 第四章 线性方程组

#### 1. 一般表示式


(1) 非齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = b _ {1}, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = b _ {2}, \\ \dots \\ a _ {m 1} x _ {1} + a _ {m 2} x _ {2} + \dots + a _ {m n} x _ {n} = b _ {m}. \end{array} \right.</equation>

(2) 齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = 0, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = 0, \\ \dots \\ a _ {m 1} x _ {1} + a _ {m 2} x _ {2} + \dots + a _ {m n} x _ {n} = 0. \end{array} \right.</equation>

2.<equation>\sum</equation>记号表示式

(1) 非齐次线性方程组

<equation>\sum_ {j = 1} ^ {n} a _ {i j} x _ {j} = b _ {i} \quad (i = 1, 2, \dots , m).</equation>

(2) 齐次线性方程组

---


#### 1. 克拉默法则


<equation>\sum_ {j = 1} ^ {n} a _ {i j} x _ {j} = 0 \quad (i = 1, 2, \dots , m).</equation>


(1) 非齐次线性方程组

<equation>A X = b,</equation>

式中<equation>\mathbf{A}=(a_{ij})_{m\times n},\mathbf{X}=(x_{1},x_{2},\dots,x_{n})^{\mathrm{T}},\mathbf{b}=(b_{1},b_{2},\dots,</equation><equation>b_{m})^{\mathrm{T}}.</equation>

(2) 齐次线性方程组

<equation>A X = 0,</equation>

式中<equation>A, X</equation>同上，<equation>0 = (0,\dots ,0)^{\mathrm{T}}.</equation>


(1) 非齐次线性方程组

<equation>x _ {1} \boldsymbol {\alpha} _ {1} + x _ {2} \boldsymbol {\alpha} _ {2} + \dots + x _ {n} \boldsymbol {\alpha} _ {n} = \boldsymbol {b},</equation>

式中<equation>\boldsymbol{a}_{j} = (a_{1j}, a_{2j}, \dots , a_{mj})^{\mathrm{T}}</equation>（<equation>j=1,2,\dots,n )</equation>,<equation>\boldsymbol{b} = (b_{1},</equation><equation>b_{2},\dots,b_{m})^{\mathrm{T}}.</equation>


<equation>x _ {1} \boldsymbol {\alpha} _ {1} + x _ {2} \boldsymbol {\alpha} _ {2} + \dots + x _ {n} \boldsymbol {\alpha} _ {n} = 0,</equation>

式中<equation>\pmb{\alpha}_{j}</equation>同上，<equation>0 = (0,\dots ,0)^{\mathrm{T}}</equation>是一个<equation>m</equation>维的零向量.


<equation>\textcircled{1}</equation>若非齐次线性方程组

---

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = b _ {1}, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = b _ {2}, \\ \dots \\ a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {n n} x _ {n} = b _ {n} \end{array} \right.</equation>

的系数行列式<equation>D = |A| = \left| \begin{array}{c c c c} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n} \end{array} \right| \neq 0,</equation>

则方程组有唯一解：<equation>x_{j} = \frac{D_{j}}{D} = (j = 1,2,\dots ,n)</equation>，其中<equation>D_{j}</equation>是把<equation>D</equation>中第<equation>j</equation>列元素<equation>(a_{1j},a_{2j},\dots ,a_{m})^{\mathrm{T}}</equation>换成常数项<equation>(b_{1},</equation><equation>b_{2},\dots ,b_{n})^{\mathrm{T}}</equation>而得到的新行列式.

<equation>\textcircled{2}</equation>若已知齐次线性方程组

<equation>\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + \dots + a _ {1 n} x _ {n} = 0, \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + \dots + a _ {2 n} x _ {n} = 0, \\ \dots \\ a _ {n 1} x _ {1} + a _ {n 2} x _ {2} + \dots + a _ {m} x _ {n} = 0 \end{array} \right.</equation>

的系数行列式<equation>D = |A| = \left| \begin{array}{c c c c} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{array} \right| \neq 0,</equation>

则该齐次线性方程组只有零解：<equation>x_{j} = 0(j = 1,2,\dots,n).</equation>

---


#### 2. 齐次线性方程组 $ AX=0 $的基础解系


推论 若已知上述齐次线性方程组有非零解，则其系数行列式<equation>D = 0.</equation>


对于<equation>AX = b</equation>（其中<equation>A</equation>为<equation>m \times n</equation>型矩阵）有解的充要条件是：增广矩阵<equation>\widetilde{A} = (A, b)</equation>的秩与系数矩阵<equation>A</equation>的秩相等，即<equation>r(A, b) = r(A)</equation>，且

<equation>\textcircled{1}</equation>当<equation>r (\widetilde{A})=r (A,b)=r (A)=n</equation>（未知量的个数）时，方程组有唯一解.

<equation>\textcircled{2}</equation>当<equation>r(\widetilde{A})=r(A,b)=r(A)<n</equation>（未知量的个数）时，方程组有无穷多个解.


对于<equation>AX = 0</equation>（其中<equation>A</equation>为<equation>m \times n</equation>矩阵），当<equation>r(A) = n</equation>（未知量的个数）时，方程组只有零解：<equation>X = 0</equation>；当<equation>r(A) < n</equation>时，方程组必有非零解（即有无穷多个解）。


<equation>\textcircled{1}</equation>若<equation>X_{1}, X_{2}</equation>都是<equation>AX = 0</equation>的解，则<equation>X_{1} + X_{2}</equation>也是<equation>AX = 0</equation>的解.

<equation>\textcircled{2}</equation>对于任意<equation>k \in \mathbf{R}</equation>，若<equation>X_{1}</equation>是<equation>AX = 0</equation>的解，则<equation>kX_{1}</equation>也都是<equation>AX = 0</equation>的解.


若<equation>\eta_{1}, \eta_{2}, \dots, \eta_{n}</equation>是齐次线性方程组<equation>AX = 0</equation>的一组

---


#### 2. 非齐次线性方程组 $AX = b$ 的解的结构


解（A为<equation>m\times n</equation>矩阵，<equation>r(A) < n )</equation>，且

<equation>\textcircled{1}</equation><equation>\boldsymbol{\eta}_{1},\boldsymbol{\eta}_{2},\dots ,\boldsymbol{\eta}_{k}</equation>线性无关；

<equation>\textcircled{2}</equation><equation>AX = 0</equation>的任一个解都可由它线性表出，则称<equation>\eta_1</equation>，<equation>\eta_2</equation>，…，<equation>\eta_{i}</equation>为齐次线性方程组<equation>AX = 0</equation>的一个基础解系.


若<equation>A</equation>为<equation>m \times n</equation>矩阵，且<equation>r(A) < n</equation>，则其通解（即全部解）为：<equation>k_{1}\eta_{1} + k_{2}\eta_{2} + \dots + k_{n - r(A)}\eta_{n - r(A)}</equation>，其中<equation>\eta_{1},\eta_{2},\dots ,\eta_{n - r(A)}</equation>是<equation>AX = 0</equation>的一个基础解系，<equation>k_{1},k_{2},\dots ,k_{n - r(A)}</equation>为任意常数.


<equation>\textcircled{1}</equation>若<equation>X_{1}, X_{2}</equation>为非齐次线性方程组<equation>AX = b</equation>的两个解，则其差<equation>X_{1} - X_{2}</equation>必是导出组<equation>AX = 0</equation>的解.

<equation>\textcircled{2}</equation>若<equation>\eta_{1}</equation>是<equation>AX = b</equation>的任一个解，<equation>\eta_{1}</equation>是其导出组<equation>AX = 0</equation>的解，则<equation>\eta_{0} + \eta_{1}</equation>也是非齐次线性方程组<equation>AX = b</equation>的解.


当<equation>r(\mathbf{A},\mathbf{b}) = r(\mathbf{A}_{m\times n}) < n</equation>时，其通解（即全部解）为

<equation>\boldsymbol {\eta} _ {0} + k _ {1} \boldsymbol {\eta} _ {1} + k _ {2} \boldsymbol {\eta} _ {2} + \dots + k _ {n - r (A)} \boldsymbol {\eta} _ {n - r (A)},</equation>

其中<equation>\eta_0</equation>为<equation>AX = b</equation>的任一个特解，<equation>\eta_{1},\eta_{2},\dots ,\eta_{n - r(A)}</equation>为导出组<equation>AX = 0</equation>的基础解系，<equation>k_{1},k_{2},\dots ,k_{n - r(A)}</equation>为任意常数.

---


### 第五章 矩阵的特征值和特征向量

#### 2. 特征值与特征向量的性质


对<equation>n</equation>阶矩阵<equation>A</equation>，若存在一个数<equation>\lambda</equation>与一个非零的<equation>n</equation>维向量<equation>X</equation>，使<equation>AX = \lambda X</equation>成立，则称<equation>\lambda</equation>是<equation>A</equation>的一个特征值，称<equation>X</equation>为<equation>A</equation>的属于<equation>\lambda</equation>的特征向量.

称行列式

<equation>f _ {A} (\lambda) = | \lambda E - A |</equation>

为<equation>A</equation>的特征多项式，称

<equation>f _ {A} (\lambda) = | \lambda E - A | = 0</equation>

为<equation>A</equation>的特征方程，称<equation>\lambda E - A</equation>为<equation>A</equation>的特征矩阵.


设<equation>\lambda_{i}(i = 1,2,\dots ,n)</equation>为<equation>n</equation>阶矩阵<equation>A = (a_{ij})_{n\times n}</equation>的特征值，则有

<equation>\textcircled{1}</equation><equation>\sum_{i=1}^{n}\lambda_{i} = \sum_{i=1}^{n}a_{ii} (\sum_{i=1}^{n}a_{ii}</equation>称为 A 的迹，记为<equation>\operatorname{tr}(\mathbf{A}))</equation>,<equation>\prod_{i=1}^{n}\lambda_{i} = |\mathbf{A}|</equation>.

---


#### 3. 可以进一步延伸的公式


<equation>\textcircled{2}A</equation>的不同特征值的特征向量必线性无关，这个性质包含两层内容：

(a)若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>是A的两两不等的特征值，<equation>X_{1}</equation><equation>X_{2},\dots ,X_{s}</equation>是A的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>的特征向量，则向量组<equation>X_{1},X_{2},\dots ,X_{s}</equation>必线性无关.

(b)若<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>是A的两两不等的特征值，<equation>X_{11},X_{12},\dots ,X_{1m_1};X_{21},X_{22},\dots ,X_{2m_2};\dots ;X_{s1},X_{s2},\dots ,</equation><equation>X_{s m}</equation>是A的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{s}</equation>的且各自线性无关的特征向量，则向量组：<equation>X_{11},X_{12},\dots ,X_{1m_1},X_{21},X_{22},\dots ,</equation><equation>X_{2m_2},\dots ,X_{s1},X_{s2},\dots ,X_{s m}</equation>必线性无关.


设<equation>X_{0}</equation>是<equation>A</equation>的属于特征值<equation>\lambda_{0}</equation>的特征向量，即<equation>AX_{0} = \lambda_{0}X_{0}</equation>，则以下公式也都成立：

<equation>\textcircled{1}</equation><equation>(k\mathbf{A} + t\mathbf{E})\mathbf{X}_0 = (k\lambda_0 + t)\mathbf{X}_0, k, t</equation>为常数.

<equation>\textcircled{2} A^{k} X_{0}=\lambda_{0}^{k} X_{0}.</equation>

<equation>\textcircled{3}</equation><equation>f(\mathbf{A})\mathbf{X}_0 = f(\lambda_0)\mathbf{X}_0</equation>，式中<equation>f(\mathbf{A})</equation>是<equation>\mathbf{A}</equation>的矩阵多项式，<equation>f(\lambda_0)</equation>是<equation>\lambda_0</equation>的同一多项式.

<equation>\textcircled{4}</equation>若<equation>\mathbf{A}</equation>可逆，则有<equation>\mathbf{A}^{-1}\mathbf{X}_0 = \frac{1}{\lambda_0}\mathbf{X}_0</equation>

<equation>\textcircled{5}</equation><equation>A^{*} X_{0} = \frac{|A|}{\lambda_{0}} X_{0}</equation>.

<equation>\textcircled{6}</equation><equation>(\boldsymbol{P}^{-1}\boldsymbol{A}\boldsymbol{P})(\boldsymbol{P}^{-1}\boldsymbol{X}_0) = \lambda_0(\boldsymbol{P}^{-1}\boldsymbol{X}_0).</equation>

---


#### 2. 矩阵可对角化的有关定理


<equation>\textcircled{7}</equation><equation>\mathbf{A}^{\mathrm{T}}</equation>与 A有相同的特征值.

若<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>满足<equation>f(\mathbf{A}) = \mathbf{O}</equation>，则有<equation>f(\lambda) = 0.</equation>


对于<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>，若存在一个<equation>n</equation>阶可逆矩阵<equation>\mathbf{P}</equation>，使

<equation>P ^ {- 1} A P = \Lambda (\Lambda \text {为 对 角 矩 阵})</equation>

成立，则称<equation>A</equation>可相似对角化，简称<equation>A</equation>可对角化，否则就称<equation>A</equation>不可对角化.

若<equation>n</equation>阶矩阵<equation>A</equation>可以对角化，则对角矩阵<equation>A</equation>的<equation>n</equation>个主对角线元素必是<equation>A</equation>的<equation>n</equation>个特征值：<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>（包括重根），其相似变换矩阵<equation>P</equation>的<equation>n</equation>个列向量<equation>X_{1},X_{2},\dots</equation><equation>X_{n}</equation>是<equation>A</equation>的分别属于<equation>\lambda_{1},\lambda_{2},\dots ,\lambda_{n}</equation>的特征向量，且<equation>X_{1},X_{2}</equation><equation>\dots ,X_{n}</equation>线性无关. 即有

<equation>P ^ {- 1} A P = A,</equation>

其中<equation>A = \left[ \begin{array}{c c c c} \lambda_ {1} & & & \\ & \lambda_ {2} & & \\ & & \ddots & \\ & & & \lambda_ {n} \end{array} \right], P = \left(X_{1}, X_{2}, \dots , X_{n}\right)</equation>为可逆

矩阵，且<equation>A X_{j}=\lambda_{j} X_{j} (j=1,2,\dots,n).</equation>


<equation>\textcircled{1}</equation><equation>n</equation>阶矩阵<equation>A</equation>可以对角化的充要条件是<equation>A</equation>有<equation>n</equation>个

---

线性无关的特征向量.

<equation>\textcircled{2}</equation>若<equation>n</equation>阶矩阵<equation>A</equation>有<equation>n</equation>个两两不等的特征值，则<equation>A</equation>必可对角化.

<equation>\textcircled{3}</equation>设<equation>\lambda_{i}</equation>是矩阵<equation>A</equation>的任一个特征值，其代数重数为<equation>n_{i}</equation>（即<equation>\lambda_{i}</equation>是<equation>n_{i}</equation>重特征值），其几何重数为<equation>m_{i}</equation>（即属于<equation>\lambda_{i}</equation>的线性无关的特征向量的最大个数，也是齐次线性方程组<equation>(\lambda_{i}E - A)X = 0</equation>的基础解系中的向量个数，<equation>m_{i} = n - r(\lambda_{i}E - A))</equation>，则恒有<equation>m_{i} \leqslant n_{i}</equation>.

<equation>\textcircled{4}</equation>设<equation>n</equation>阶矩阵<equation>\mathbf{A}</equation>的两两不等的特征值为<equation>\lambda_{1}, \lambda_{2}, \dots, \lambda_{s}(1 \leqslant s \leqslant n)</equation>，则矩阵<equation>\mathbf{A}</equation>可对角化的充要条件是对<equation>\mathbf{A}</equation>的每一个特征值<equation>\lambda_{i}</equation>，都有<equation>m_{i} = n_{i}(i = 1, 2, \dots, s)</equation>.

---


### 第六章 二次型

#### 1. 二次型的定义


<equation>n</equation>个变量<equation>x_{1}, x_{2}, \dots, x_{n}</equation>的一个二次齐次多项式

<equation>\begin{array}{l} f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \\ = a _ {1 1} x _ {1} ^ {2} + 2 a _ {1 2} x _ {1} x _ {2} + 2 a _ {1 3} x _ {1} x _ {3} + \dots + 2 a _ {1 n} x _ {1} x _ {n} \\ + a _ {2 2} x _ {2} ^ {2} + 2 a _ {2 3} x _ {2} x _ {3} + \dots + 2 a _ {2 n} x _ {2} x _ {n} \\ + a _ {3 3} x _ {3} ^ {2} + \dots + 2 a _ {3 n} x _ {3} x _ {n} \\ + \dots \\ + a _ {m} x _ {n} ^ {2} \\ \end{array}</equation>

称为一个关于<equation>x_{1}, x_{2}, \dots , x_{n}</equation>的二次型

2. 二次型的矩阵表示式

<equation>\text {设} \boldsymbol {X} = \left(x _ {1}, x _ {2}, \dots , x _ {n}\right), \boldsymbol {A} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right],</equation>

则

<equation>f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) = \boldsymbol {X} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {X},</equation>

---


#### 4. 惯性定理


称 A为二次型对应的矩阵.


(1) 实二次型的标准形

若

<equation>\begin{array}{l} f (X) = X ^ {\mathrm {T}} A X \xlongequal {X = C Y} Y ^ {\mathrm {T}} \left(C ^ {\mathrm {T}} A C\right) Y \\ = d _ {1} y _ {1} ^ {2} + d _ {2} y _ {2} ^ {2} + \dots + d _ {n} y _ {n} ^ {2} \\ = Y ^ {\mathrm {T}} \cdot \operatorname {d i a g} \left(d _ {1}, d _ {2}, \dots , d _ {n}\right) \cdot Y, \\ \end{array}</equation>

则称平方和

<equation>d _ {1} y _ {1} ^ {2} + d _ {2} y _ {2} ^ {2} + \dots + d _ {n} y _ {n} ^ {2}</equation>

为二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>的一个标准形.

任一个实二次型<equation>f ( X ) = X^{\mathrm{T}} A X</equation>经过适当的可逆线性替换<equation>X=C Y</equation>总可化成标准形（即平方和），即实对称矩阵总可与一个对角矩阵合同：

<equation>\mathbf {C} ^ {\mathrm {T}} \mathbf {A C} = \mathbf {B} = \operatorname {d i a g} \left(d _ {1}, d _ {2}, \dots , d _ {n}\right).</equation>

(2) 实二次型的规范形

形如

<equation>\begin{array}{l} f (X) = X ^ {\mathrm {T}} A X \xlongequal {X = D Z} z _ {1} ^ {2} + z _ {2} ^ {2} + \dots + z _ {p} ^ {2} - z _ {p + 1} ^ {2} \\ - \dots - z _ {p + q} ^ {2} + 0 \cdot z _ {p + q + 1} ^ {2} + \dots + 0 \cdot z _ {n} ^ {2} \\ \end{array}</equation>

的标准形称为<equation>f(X)</equation>的规范形，其中<equation>p</equation>称为正惯性指数，<equation>q</equation>称为负惯性指数.


任意一个实系数的二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>总可经过一个适当的可逆线性替换化成规范形，其规范形是

---


#### 1. 正定二次型


唯一的，与所选的坐标变换无关，即正平方项个数<equation>p</equation>负平方项个数<equation>q</equation>由原二次型<equation>f(X) = X^{\mathrm{T}}AX</equation>唯一确定.用矩阵的语言来讲：实对称矩阵总可与对角阵

<equation>\operatorname {d i a g} (1, \dots , 1, - 1, \dots , - 1, 0, \dots , 0)</equation>

合同，且<equation>p + q = r(A)</equation>，其中<equation>p, q</equation>是不变的量.


任一个实二次型总可用配方的方法通过一个适当的可逆线性替换化为标准形.


设<equation>f ( X )=X^{\mathrm{T}} A X</equation>，因为A为实对称矩阵，由实对称矩阵必可通过正交变换化为对角阵A，其主对角线元素必为A的全部特征值，而正交变换（<equation>Q^{\mathrm{T}} A Q=Q^{-1} A Q=A</equation>）中包含了合同变换，因此当作变换<equation>X=Q Y</equation>后，二次型<equation>f ( X )</equation>即变为

<equation>\begin{array}{l} g (\mathbf {Y}) = \mathbf {Y} ^ {\mathrm {T}} \left(\mathbf {Q} ^ {\mathrm {T}} \mathbf {A} \mathbf {Q}\right) \mathbf {Y} = \mathbf {Y} ^ {\mathrm {T}} \mathbf {A} \mathbf {Y} \\ = \lambda_ {1} y _ {1} ^ {2} + \lambda_ {2} y _ {2} ^ {2} + \dots + \lambda_ {n} y _ {n} ^ {2}. \\ \end{array}</equation>

任一个实二次型<equation>f(X) = X^{\mathrm{T}}AX</equation>总可通过变量间的正交替换<equation>X = QY</equation>化为标准形（平方和），其平方项前的系数必是<equation>A</equation>的全部特征值.


设<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>是一个实二次型，若对于任意

---


#### 2. 二次型正定的判定


<equation>X_{0}\neq 0</equation>，<equation>f(\mathbf{X}_0) = \mathbf{X}_0^{\mathrm{T}}\mathbf{A}\mathbf{X}_0 > 0</equation>恒成立，则称

<equation>f (\boldsymbol {X}) = \boldsymbol {X} ^ {\mathrm {T}} \boldsymbol {A} \boldsymbol {X}</equation>

为正定二次型，称对应矩阵<equation>A</equation>为正定矩阵.


(1) 判定正定性的充分必要条件

<equation>\textcircled{1}</equation>实二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>正定<equation>\Leftrightarrow</equation>正惯性指数<equation>p = n.</equation>

<equation>\textcircled{2}</equation>实二次型<equation>f ( X )=X^{\mathrm{T}} A X</equation>正定<equation>\Leftrightarrow A</equation>与单位矩阵合同，即存在可逆矩阵P，使<equation>P^{\mathrm{T}} A P=E</equation>成立.

<equation>\textcircled{3}</equation>实二次型<equation>f(X) = X^{\mathrm{T}}AX</equation>正定<equation>\Leftrightarrow</equation>存在可逆矩阵<equation>C</equation>，使<equation>A = C^{\mathrm{T}}C</equation>.

<equation>\textcircled{4}</equation>实二次型<equation>f ( \boldsymbol{X} )=\boldsymbol{X}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{X}</equation>正定<equation>\Leftrightarrow \boldsymbol{A}</equation>的特征值全大于0.

<equation>\textcircled{5}</equation>实二次型<equation>f ( \boldsymbol{X} )=\boldsymbol{X}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{X}</equation>正定<equation>\Leftrightarrow A</equation>的各阶顺序主子式全部大于0，即

<equation>\left| a _ {1 1} \right| > 0,</equation>

<equation>\left| \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| > 0,</equation>

<equation>\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| > 0,</equation>

---

<equation>\left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| > 0.</equation>

<equation>\textcircled{6}</equation>实二次型<equation>f(\mathbf{X}) = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}</equation>正定<equation>\Leftrightarrow \mathbf{A}</equation>与一个正定矩阵合同.

(2) 实对称矩阵 A正定的必要条件

实对称矩阵<equation>\mathbf{A}</equation>正定<equation>\Rightarrow |\mathbf{A}| > 0; a_{n} > 0</equation>（<equation>i=1,</equation>2,…,n).

---


#### 概率论与数理统计


第三部分

---


### 第一章 随机事件和概率

#### (4)相互独立


<equation>\textcircled{1}</equation>包含：若 B发生必然导致 A发生，称为 A包含 B，记作 A<equation>\supset</equation>B.

<equation>\textcircled{2}</equation>相等：若<equation>A\supset B</equation>且<equation>B\supset A</equation>，则称<equation>A=B.</equation>


若<equation>AB=\varnothing</equation>，则称A与B互不相容.


若<equation>AB = \varnothing</equation>且<equation>A\cup B = \varOmega</equation>，则称 A与B为对立事件，记为<equation>B = \overline{A}</equation>


<equation>\textcircled{1}</equation>若<equation>P(AB) = P(A)P(B)</equation>，则称 A与B相互独立.

<equation>\textcircled{2}</equation>若<equation>\left\{ \begin{array}{l} P (A B) = P (A) P (B), \\ P (B C) = P (B) P (C), \\ P (A C) = P (A) P (C), \\ P (A B C) = P (A) P (B) P (C) \end{array} \right\}</equation>称<equation>A, B, C</equation>相

---


#### 3. 事件运算的规律


互独立.

<equation>\textcircled{3}</equation>性质：<equation>A,B;\overline{A},B;A,\overline{B};\overline{A},\overline{B}</equation>中任一对相互独立，则其余各对相互独立.


(1) 和事件

A发生或者B发生，记为<equation>A\bigcup B.</equation>

(2) 积事件

A发生且B发生，记为AB.

(3) 差事件

A发生且B不发生，记为<equation>A - B = A\overline{B}.</equation>


(1) 交换律

<equation>A \bigcup B = B \bigcup A;</equation>

<equation>A B = B A.</equation>

(2) 结合律

<equation>(A \cup B) \cup C = A \cup (B \cup C);</equation>

<equation>(A B) C = A (B C).</equation>

(3) 分配律

<equation>(A \bigcup B) C = (A C) \bigcup (B C);</equation>

<equation>(A B) \cup C = (A \cup C) (B \cup C).</equation>

(4) 对偶律

<equation>\overline {{A \bigcup B}} = \overline {{A}} \overline {{B}};</equation>

<equation>\overline {{A B}} = \overline {{A}} \cup \overline {{B}}, \overline {{A}} = A.</equation>

---


#### (1)规范性


样本空间<equation>\varOmega</equation>在每次试验中都会发生，故称其为必然事件.


空集（<equation>\varnothing</equation>）在每次试验中都不会发生，故称其为不可能事件.


由单个样本点构成的单点集<equation>\{w\}</equation>称之为基本事件.


若<equation>AB = \varnothing</equation>，则称事件<equation>A</equation>与<equation>B</equation>为互不相容事件.


若<equation>A B=\varnothing</equation>，<equation>A \cup B=\Omega</equation>，则称事件 A与B为对立事件.


概率是从所有事件构成的集合到实数集的一个映射 P，它必须满足下列条件：


<equation>P (\Omega) = 1.</equation>

---


#### 2. 概率的基本性质


(2) 非负性

对任意事件 A，都有

<equation>P (A) \geqslant 0.</equation>

(3) 可列可加性

设<equation>A_{k}, k = 1,2, \dots</equation>为互不相容事件，则映射<equation>P</equation>满足

<equation>P \left(\bigcup_ {k = 1} ^ {\infty} A _ {k}\right) = \sum_ {k = 1} ^ {\infty} P \left(A _ {k}\right).</equation>


(1)<equation>P(\varnothing)=0.</equation>

(2) 有限可加性

设<equation>A_{k}, k = 1, 2, \dots , n</equation>为互不相容事件，则

<equation>P \left(\bigcup_ {k = 1} ^ {n} A _ {k}\right) = \sum_ {k = 1} ^ {n} P \left(A _ {k}\right).</equation>

(3) 对立事件的概率

<equation>P (\bar {A}) = 1 - P (A).</equation>

若事件<equation>A\subset B</equation>，则

(4) 单调性

<equation>P (A) \leqslant P (B).</equation>

(5) 加法公式

<equation>P (A \cup B) = P (A) + P (B) - P (A B).</equation>

(6) 减法公式

<equation>P (A - B) = P (A) - P (A B).</equation>

---


#### 4. 完备事件组


古典概型中，<equation>\varOmega</equation>包含样本点的个数有限，且每个基本事件的概率相等。即设<equation>\Omega = \{w_{1}, w_{2}, \dots, w_{n}\}</equation>，则有

<equation>P \left\{w _ {i} \right\} = P \left\{w _ {j} \right\} \quad (\text {任 意} i, j).</equation>

若<equation>A = \{w_{i1}, w_{i2}, \dots, w_{k}\}</equation>，则

<equation>P (A) = \frac {k}{n}.</equation>


设<equation>\Omega</equation>为一区域，其中的分布是均匀的，则

<equation>P (A) = \frac {m (A)}{m (\Omega)},</equation>

其中<equation>m(\cdot)</equation>为该区域的测度，如长度、面积、体积等.


设<equation>P ( A ) > 0</equation>，定义条件概率为

<equation>P (B | A) = \frac {P (A B)}{P (A)}.</equation>


设<equation>A_{k}, k=1,2,\dots</equation>为互不相容事件，且<equation>\bigcup_{k=1}^{A_{k}}A_{k}=\Omega</equation>，则称<equation>A_{k}, k=1,2,\dots</equation>为完备事件组（也可称之为样本空间的一个可列分割.若其中的事件个数为有限个，则此时分割称为有限分割).

---


#### 7. n重伯努利试验


设<equation>A_{k}, k=1,2,\dots</equation>为样本空间的一个完备事件组，则

<equation>P (B) = \sum_ {k = 1} ^ {\infty} P \left(A _ {k}\right) P \left(B \mid A _ {k}\right).</equation>


设<equation>A_{k}, k = 1,2,\dots</equation>为样本空间的一个完备事件组，则

<equation>P \left(A _ {i} \mid B\right) = \frac {P \left(A _ {i}\right) P \left(B \mid A _ {i}\right)}{\sum_ {k = 1} ^ {\infty} P \left(A _ {k}\right) P \left(B \mid A _ {k}\right)}</equation>


每次试验中只有事件<equation>A</equation>或<equation>\overline{A}</equation>发生，并对此试验独立地重复n次，则称此试验为n重伯努利试验.在n次独立试验中A恰好发生k次的概率

<equation>P _ {n} (k) = \mathrm {C} _ {n} ^ {k} p ^ {k} (1 - p) ^ {n - k} (k = 0, 1, 2, \dots , n).</equation>

---


### 第二章 一维随机变量及其分布

#### 1. 定义


设 X 为一随机变量，令

<equation>F (x) = P (X \leqslant x), x \in \mathbf {R},</equation>

称此函数为随机变量<equation>X</equation>的分布函数.


<equation>\textcircled{1}</equation>单调不减.

<equation>\textcircled{2}</equation>值域：<equation>[0,1],\lim F(x) = 1,\lim F(x) = 0.</equation>

<equation>\textcircled{3}</equation>在任意点右连续.

<equation>\textcircled{4}</equation>对任意 a<equation>\in</equation>R，有

<equation>P (X = a) = F (a) - F (a - 0),</equation>

其中<equation>F ( a - 0 )</equation>为<equation>F ( x )</equation>在a点的左极限


若随机变量<equation>X</equation>取有限个或可列多个不同的值，则称<equation>X</equation>为离散型随机变量.

---


#### 2. 概率密度的性质


(1) 分布律的定义

<equation>P \{X = x _ {k} \} = p _ {k}, k = 1, 2, \dots .</equation>

(2) 分布律的性质

<equation>p _ {k} \geqslant 0, k = 1, 2, \dots ; \sum_ {k = 1} ^ {\infty} p _ {k} = 1.</equation>


<equation>F (x) = \sum_ {x _ {i} \leqslant x} P \left\{x = x _ {k} \right\}.</equation>


如果对于随机变量<equation>X</equation>的分布函数<equation>F(x)</equation>，存在非负可积函数<equation>f(x)</equation>，使对任意<equation>x</equation>，有

<equation>F (x) = \int_ {- \infty} ^ {x} f (t) \mathrm {d} t,</equation>

则称<equation>X</equation>为连续型随机变量，其中函数<equation>f(x)</equation>称为<equation>X</equation>的概率密度函数，简称概率密度.


<equation>\textcircled{1} f ( x ) \geqslant 0;</equation>

<equation>\textcircled{2}</equation><equation>\int_{- \infty}^{+ \infty} f ( x ) \mathrm{d} x=1;</equation>

---


#### 四、常见随机变量的概率分布


<equation>\textcircled{3}</equation>对于任意实数<equation>x_{1}, x_{2}\left(x_{1}\leqslant x_{2}\right)</equation>

<equation>\begin{array}{l} P \left\{x _ {1} < X \leqslant x _ {2} \right\} = F \left(x _ {2}\right) - F \left(x _ {1}\right) \\ = \int_ {x _ {1}} ^ {x _ {2}} f (x) \mathrm {d} x; \\ \end{array}</equation>

<equation>\textcircled{4}</equation>若<equation>f(x)</equation>在点<equation>x</equation>处连续，则<equation>F^{\prime}(x) = f(x)</equation>.


<table border="1"><tr><td>类型</td><td>定义</td></tr><tr><td>0-1分布</td><td>P(X=1)=p,P(X=0)=1-p(0<p&lt;1)</td></tr><tr><td>二项分布B(n,P)</td><td>P{X=k}=Cnk^{k}(1-p)^{n-k}(0<p&lt;1,k=0,1,2,···,n)</td></tr><tr><td>泊松分布P(λ)</td><td>P{X=k}=\frac{\lambda^{k}}{k!}e^{-\lambda}(\lambda&gt;0,k=0,1,2,···)</td></tr><tr><td>超几何分布</td><td>P{X=m}=\frac{C_{M}^{n}C_{N-M}^{n-m}}{C_{N}^{n}}(N,M,m均为正整数,0≤n≤N,0≤m≤M,0≤n-m≤N-M)</td></tr></table>

---


#### 2. 连续型


<table border="1"><tr><td>类型</td><td>定义</td></tr><tr><td>几何分布</td><td>P{X=k}=p(1-p)^{k-1}(k=1,2, \cdots,0<p&lt;1)</td></tr><tr><td>均匀分布U(a,b)</td><td>f(x)=\begin{cases}\frac{1}{b-a},&amp;a&lt;x<b\\0,&amp;其他\end{cases}$</td></tr><tr><td>指数分布E(λ)</td><td>f(x)=\begin{cases}\lambda e^{-\lambda x},&amp;x&gt;0\\0,&amp;其他\end{cases}(\lambda&gt;0)</td></tr><tr><td>正态分布N(\mu,\delta^{2})</td><td>f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}(\sigma&gt;0,-\infty&lt;x&lt;+\infty)</td></tr></table>


<equation>Y = g (x), P \left\{Y = y _ {j} \right\} = \sum_ {y _ {j} = g \left(x _ {j}\right)} P \left\{X = x _ {i} \right\}.</equation>


<equation>\textcircled{1}</equation><equation>Y = g(X)</equation>为单调可导的函数时，设<equation>X = h(Y)</equation>为其反函数，则

---

<equation>f _ {Y} (y) = \left\{ \begin{array}{l l} f _ {X} [ h (y) ] \left| h ^ {\prime} (y) \right|, & \alpha < y < \beta , \\ 0, & \text {其 他}. \end{array} \right.</equation>

其中<equation>\alpha=\min( g(-\infty), g(+\infty))</equation>

<equation>\beta = \max (g (- \infty), g (+ \infty)).</equation>

<equation>\textcircled{2}</equation>对任意函数<equation>Y=g(X)</equation>

<equation>\begin{array}{l} F _ {Y} (y) = P \{Y \leqslant y \} = P \{g (X) \leqslant y \} \\ = \int_ {g (x) \leqslant y} f _ {X} (x) \mathrm {d} x, \\ \end{array}</equation>

<equation>f _ {Y} (y) = F _ {Y} ^ {\prime} (y).</equation>

---


### 第三章 二维随机变量及其分布

#### (1)定义


<equation>F (x, y) = P \{X \leqslant x, Y \leqslant y \}.</equation>


<equation>\textcircled{1}</equation><equation>F(x,y)</equation>是变量<equation>x</equation>和<equation>y</equation>的单调不减函数；

<equation>\textcircled{2}</equation><equation>0 \leqslant F(x, y) \leqslant 1, F(-\infty, -\infty) = 0, F(+\infty, +\infty) = 1</equation>;

<equation>\textcircled{3} F ( x,y )</equation>关于变量 x和y都右连续；

<equation>\textcircled{4}</equation>对任意<equation>(x_{1}, y_{1}), (x_{2}, y_{2})(x_{1} < x_{2}, y_{1} < y_{2})</equation><equation>F(x_{2}, y_{2}) - F(x_{1}, y_{2}) - F(x_{2}, y_{1}) + F(x_{1}, y_{1}) \geqslant 0.</equation>


若随机变量<equation>(X, Y)</equation>的取值为有限多对或可列无穷多对时，则称<equation>(X, Y)</equation>为二维离散型随机变量.

---


#### 2. 联合概率密度函数的性质


<equation>P _ {i j} = P \left\{X = x _ {i}, Y = y _ {j} \right\}.</equation>

(2) 性质

<equation>0 \leqslant P _ {i j} \leqslant 1; \sum_ {i} \sum_ {j} P _ {i j} = 1.</equation>

(3) 边缘分布律

<equation>P _ {i.} = P \{X = x _ {i} \} = \sum_ {j = 1} ^ {\infty} P _ {i j};</equation>

<equation>P _ {. j} = P \left\{Y = y _ {j} \right\} = \sum_ {i = 1} ^ {\infty} P _ {i j}.</equation>


若存在非负可积函数<equation>f ( x,y)</equation>，使对任意的<equation>x,y</equation>有

<equation>F (x, y) = \int_ {- \infty} ^ {y} \int_ {- \infty} ^ {x} f (u, v) \mathrm {d} u \mathrm {d} v,</equation>

则称<equation>(X, Y)</equation>为二维连续型随机变量，称<equation>f(x,y)</equation>为<equation>(X, Y)</equation>的联合概率密度函数.


<equation>\textcircled{1} f ( x,y ) \geqslant0;</equation>

<equation>\textcircled{2}</equation><equation>\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}x\mathrm{d}y=1;</equation>

<equation>\textcircled{3}</equation>若<equation>f(x,y)</equation>在点<equation>(x,y)</equation>连续，则有

<equation>\frac {\partial^ {2} F}{\partial x \partial y} = f (x, y).</equation>

---


#### 1. 定义


<equation>\textcircled{4} P \{(X, Y) \in G \} = \iint_ {G} f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

3. 边缘密度函数

<equation>f _ {X} (x) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} y,</equation>

<equation>f _ {Y} (y) = \int_ {- \infty} ^ {+ \infty} f (x, y) \mathrm {d} x.</equation>


1. 二维离散型随机变量的条件分布律

<equation>P \left(Y = y _ {j} \mid X = x _ {i}\right) = \frac {p _ {i j}}{p _ {i .}}, j = 1, 2, \dots ;</equation>

<equation>P = \left(X = x _ {i} \mid Y = y _ {j}\right) = \frac {p _ {i j}}{p _ {. j}}, j = 1, 2, \dots .</equation>

2. 二维连续型随机变量的条件密度函数

<equation>f _ {Y | X} (y | x) = \frac {f (x , y)}{f _ {X} (x)}, \quad \left(f _ {X} (x) > 0\right)</equation>

<equation>f _ {X \mid Y} (x \mid y) = \frac {f (x , y)}{f _ {Y} (y)}. \quad \left(f _ {Y} (y) > 0\right)</equation>


设<equation>F(x,y)</equation>及<equation>F_{X}(x),F_{Y}(y)</equation>分别是二维随机变量<equation>(X,Y)</equation>的联合分布函数和边缘分布函数，若对所有<equation>x,y</equation>

---


#### 2. 二维正态分布


有

<equation>P \{X \leqslant x, Y \leqslant y \} = P \{X \leqslant x \} P \{Y \leqslant y \}</equation>

则称随机变量 X和Y相互独立.


(1) 用定义

<equation>F (x, y) = F _ {X} (x) F _ {Y} (y).</equation>

(2) 离散型

<equation>P _ {i j} = P _ {i}. P _ {. j}.</equation>

(3) 连续型

<equation>f (x, y) = f _ {X} (x) f _ {Y} (y).</equation>


若二维随机变量<equation>(X,Y)</equation>的密度函数为

<equation>f (x, y) = \left\{ \begin{array}{c c} \frac {1}{m (D)}, & (x, y) \in D, \\ 0, & \text {其 他}, \end{array} \right.</equation>

其中<equation>m(D)</equation>表示区域<equation>D</equation>的面积，则称<equation>(X, Y)</equation>服从区域<equation>D</equation>上的均匀分布，并记为<equation>X\sim U(D)</equation>.


<equation>\textcircled{1}</equation>若二维随机变量<equation>(X, Y)</equation>的密度函数为

<equation>f (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}} \exp \left\{- \frac {1}{2 \left(1 - \rho^ {2}\right)} \right\}</equation>

---


#### (2)卷积公式


<equation>\left[ \frac {\left(x - \mu_ {1}\right) ^ {2}}{\sigma_ {1} ^ {2}} - 2 \rho \frac {\left(x - \mu_ {1}\right) \left(y - \mu_ {2}\right)}{\sigma_ {1} \sigma_ {2}} + \frac {\left(y - \mu_ {2}\right) ^ {2}}{\sigma_ {2} ^ {2}} \right] \Bigg \}.</equation>

其中参数<equation>\mu_{1}\in \mathbf{R},\mu_{2}\in \mathbf{R},\sigma_{1} > 0,\sigma_{2} > 0,\rho \in [-1,1]</equation>，则称二维随机变量<equation>(X,Y)</equation>服从二维正态分布，并记为<equation>(X,Y)\sim N(\mu_{1},\mu_{2};\sigma_{1}^{2},\sigma_{2}^{2};\rho)</equation>.

<equation>\textcircled{2}</equation>二维正态分布的边缘密度

<equation>f _ {X} (x) = \frac {1}{\sqrt {2 \pi} \delta_ {1}} \mathrm {e} ^ {- \frac {(x - \mu_ {1}) ^ {2}}{2 \delta_ {1} ^ {2}}}, - \infty < x < + \infty .</equation>

<equation>f _ {Y} (x) = \frac {1}{\sqrt {2 \pi} \delta_ {2}} \mathrm {e} ^ {- \frac {(y - \mu_ {2}) ^ {2}}{2 \delta_ {2} ^ {2}}}, - \infty < y < + \infty .</equation>


(1) 一般公式

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f (z - y, y) \mathrm {d} y,</equation>

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f (x, z - x) \mathrm {d} x.</equation>


当<equation>x</equation>和<equation>y</equation>相互独立时，设<equation>(X, Y)</equation>关于<equation>X, Y</equation>的边缘密度分别为<equation>f_{X}(x), f_{Y}(y)</equation>，则

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f _ {X} (z - y) f _ {Y} (y) \mathrm {d} y,</equation>

---

<equation>f _ {Z} (z) = \int_ {- \infty} ^ {+ \infty} f _ {X} (x) f _ {Y} (z - x) \mathrm {d} x.</equation>

2.<equation>M=\max (X, Y)</equation>及<equation>N=\min (X, Y)</equation>的分布

设<equation>X, Y</equation>是两个相互独立的随机变量，它们的分布函数分别为<equation>F_{X}(x)</equation>和<equation>F_{Y}(y)</equation>，则

<equation>\begin{array}{l} F _ {\max } (z) = F _ {X} (z) f _ {Y} (z), \\ F _ {\min } (z) = 1 - \left[ 1 - F _ {X} (z) \right] \left[ 1 - F _ {Y} (z) \right]. \\ \end{array}</equation>

---


### 第四章 随机变量的数字特征

#### 1. 数学期望定义


<equation>\textcircled{1}</equation>若离散型随机变量

<equation>X \sim \left( \begin{array}{c c c c c} x _ {1} & x _ {2} & \dots & x _ {n} & \dots \\ p _ {1} & p _ {2} & \dots & p _ {n} & \dots \end{array} \right),</equation>

且级数<equation>\sum_{k} x_{k} p_{k}</equation>绝对收敛，称随机变量<equation>X</equation>的数学期望存在，并称

<equation>E X = \sum_ {k} x _ {k} p _ {k}</equation>

为其数学期望.

<equation>\textcircled{2}</equation>若连续型随机变量 X的密度函数为 f(x)，且积分<equation>\int_{\mathrm{R}} f ( x ) \mathrm{d} x</equation>绝对收敛，称随机变量 X的数学期望存在，并称

<equation>E X = \int_ {\mathrm {R}} f (x) \mathrm {d} x</equation>

为其数学期望.

---


#### 3. 性质


<equation>\textcircled{1}</equation>若随机变量<equation>X\sim \left( \begin{array}{c c c c c} x_{1} & x_{2} & \dots & x_{n} & \dots \\ p_{1} & p_{2} & \dots & p_{n} & \dots \end{array} \right), Y = g(X)</equation>，则

<equation>E Y = \sum_ {k} g \left(x _ {k}\right) p _ {k}.</equation>

<equation>\textcircled{2}</equation>若随机变量 X的密度函数为<equation>f_{X}(x),Y=g(X)</equation>则

<equation>E Y = \int_ {\mathbf {R}} g (x) f _ {X} (x) \mathrm {d} x.</equation>

<equation>\textcircled{3}</equation>若随机变量<equation>(X, Y) \sim p_{ij}, Z = g(X, Y)</equation>，则

<equation>E Z = \sum_ {i} \sum_ {j} g \left(x _ {i}, y _ {j}\right) p _ {i j}.</equation>

<equation>\textcircled{4}</equation>若随机变量<equation>(X, Y)</equation>的联合密度函数为<equation>f(x, y), Z = g(X, Y)</equation>，则

<equation>E Z = \iint_ {\mathbb {R} ^ {2}} g (x, y) f (x, y) \mathrm {d} x \mathrm {d} y.</equation>

<equation>\textcircled{5}</equation>若随机变量<equation>X\sim \left( \begin{array}{cc}\xi & \eta \\ p & q \end{array} \right)</equation>，则

<equation>E X = p E \xi + q E \eta .</equation>

<equation>\textcircled{1}</equation>线性性：对任意<equation>a,b,c\in \mathbf{R}</equation>及随机变量<equation>X,Y</equation>，若EX，EY存在，则


<equation>E (a X + b Y + c) = a E X + b E Y + c.</equation>

---

<equation>\textcircled{2}</equation>若随机变量 X与 Y相互独立，且 EX，EY存在，则

<equation>E (X Y) = E X \cdot E Y.</equation>


若数学期望<equation>E(X - EX)^{2}</equation>存在，则称其为随机变量<equation>X</equation>的方差，并记为<equation>DX</equation>.同时称<equation>\sqrt{DX}</equation>为随机变量<equation>X</equation>的标准差.


若数学期望<equation>E[(X - EX)(Y - EY)]</equation>存在，则称其为随机变量<equation>X</equation>与<equation>Y</equation>的协方差，并记为<equation>\operatorname{Cov}(X, Y)</equation>.


<equation>\textcircled{1}</equation>对任意随机变量 X，<equation>D X\geqslant0.</equation>

<equation>\textcircled{2}</equation>若 C为固定常数，则<equation>D C=0.</equation>

<equation>\textcircled{3}</equation>常数<equation>a\in\mathbf{R}</equation>，则<equation>D(aX)=a^{2}DX.</equation>

<equation>\textcircled{4} D ( X \pm Y ) = D X + D Y \pm 2 \operatorname{C o v} ( X, Y ).</equation>

<equation>\textcircled{5}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则

<equation>D (X \pm Y) = D X + D Y.</equation>

<equation>\textcircled{6} D X=E X^{2}-(E X)^{2}.</equation>

<equation>\textcircled{7}</equation><equation>\operatorname{C o v} ( X, Y )=\operatorname{C o v} ( Y, X ).</equation>

<equation>\textcircled{8} \operatorname{C o v} ( a X, Y )=a \operatorname{C o v} ( X, Y ).</equation>

---


#### 4. 常见分布的数字特征


<equation>\textcircled{9} \operatorname {C o v} (X + Y, Z) = \operatorname {C o v} (X, Z) + \operatorname {C o v} (Y, Z).</equation>

<equation>\textcircled{10}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则

<equation>\operatorname {C o v} (X, Y) = 0.</equation>

<equation>\begin{array}{l} \textcircled{1 2} \operatorname {C o v} \left(a X + b Y, c \xi + d \eta\right) = a c \operatorname {C o v} \left(X, \xi\right) + \\ a d \operatorname {C o v} (X, \eta) + b c \operatorname {C o v} (Y, \xi) + b d \operatorname {C o v} (Y, \eta). \\ \end{array}</equation>

其中<equation>a, b, c, d</equation>为常数，<equation>X, Y, \xi , \eta</equation>为随机变量.


(1) 0-1分布

若<equation>X\sim \binom{0}{q}\frac{1}{p}</equation>，则

<equation>E X = p, D X = p q.</equation>

(2) 几何分布

若<equation>P(X = n) = pq^{n - 1}(n = 1,2,\dots)</equation>，则

<equation>E X = \frac {1}{p}, D X = \frac {q}{p ^ {2}}.</equation>

(3) 二项分布

若<equation>Y\sim B(n,p)</equation>，则<equation>EY = np,DY = npq.</equation>

(4) 超几何分布

若<equation>P ( Y=k)=\frac{C_{M}^{k} C_{N-M}^{n-k}}{C_{N}^{n}}</equation>，其中<equation>\max \{0,n-N+M\}</equation><equation>\leq k\leq \min \{M,n\}</equation>k为整数，<equation>n-k\leq N-M</equation>记<equation>p=\frac{M}{N}</equation><equation>q=1-p</equation>，则

---


#### 1. 定义


<equation>E Y = n p, D Y = n p q \frac {N - n}{N - 1}.</equation>


若<equation>X\sim P(\lambda)</equation>，则

<equation>E X = \lambda , D X = \lambda .</equation>


<equation>X\sim U(a,b)</equation>，则

<equation>E X = \frac {a + b}{2}, D X = \frac {(b - a) ^ {2}}{1 2}.</equation>


若<equation>X\sim E(\lambda)</equation>，则

<equation>E X = \frac {1}{\lambda}, D X = \frac {1}{\lambda^ {2}}.</equation>

(8) 正态分布

若<equation>X\sim N(\mu ,\sigma^{2})</equation>，则

<equation>E X = \mu , D X = \sigma^ {2}.</equation>


若<equation>DX > 0, DY > 0</equation>，则称<equation>\frac{\operatorname{Cov}(X, Y)}{\sqrt{DX \cdot DY}}</equation>为随机变量<equation>X</equation>与<equation>Y</equation>的相关系数，并记为<equation>\rho_{xy}</equation>. 若<equation>\rho_{xy} = 1</equation>，则称<equation>X</equation>与<equation>Y</equation>正相关；若<equation>\rho_{xy} = -1</equation>，则称<equation>X</equation>与<equation>Y</equation>负相关；若<equation>\rho_{xy} = 0</equation>，则称

---


#### 2. 性质


X与Y不相关.


<equation>\textcircled{1}</equation><equation>|\rho_{x x}| \leqslant 1.</equation>

<equation>\textcircled{2} \operatorname{C o v}^{2} ( X, Y ) \leqslant D X \cdot D Y.</equation>

<equation>\textcircled{3}</equation><equation>| E ( X Y ) | \leqslant \sqrt { E X^{2} \cdot E Y^{2}}.</equation>

<equation>\textcircled{4}</equation>若随机变量<equation>X</equation>与<equation>Y</equation>相互独立，则<equation>\rho_{x y} = 0.</equation>

<equation>\textcircled{5}</equation>若<equation>(X, Y) \sim N(\mu_1, \sigma_1^2; \mu_2, \sigma_2^2; \rho)</equation>，则其中的参数<equation>\rho</equation>为其相关系数，且<equation>X</equation>与<equation>Y</equation>相互独立的充分必要条件为<equation>\rho = 0</equation>。

<equation>\textcircled{6}</equation>若<equation>X\sim \left( \begin{array}{cc}0 & 1\\ q_{1} & p_{1} \end{array} \right), Y\sim \left( \begin{array}{cc}0 & 1\\ q_{2} & p_{2} \end{array} \right), p_{k} + q_{k} = 1(k = 1,2)</equation>，则X与Y相互独立的充分必要条件为<equation>\rho_{xy} = 0.</equation>

---


### 第五章 大数定律和中心极限定理

#### 2. 辛钦大数定律


设随机变量<equation>X</equation>的数学期望与方差存在，则对任意实数<equation>\varepsilon > 0</equation>，下面的不等式成立：

<equation>P \left(\left| X - E X \right| \geqslant \varepsilon\right) \leqslant \frac {D X}{\varepsilon^ {2}}, \text {或}</equation>

<equation>P \left(| X - E X | < \varepsilon\right) \geqslant 1 - \frac {D X}{\varepsilon^ {2}},</equation>

并称之为切比雪夫不等式.


设<equation>X_{1}, X_{2}, \dots, X_{n}, \dots</equation>为相互独立的随机变量序列，其数学期望和方差都存在并且相等，分别记为<equation>\mu</equation>和<equation>\sigma^2</equation>，则对任意<equation>\varepsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \mu \right| < \varepsilon \right\} = 1.</equation>


设<equation>X_{1}, X_{2}, \dots, X_{n}, \dots</equation>为相互独立同分布的随机变

---


#### 2. 棣莫弗一拉普拉斯定理


量序列，且其数学期望存在，记为<equation>\mu</equation>，则对任意<equation>\varepsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \mu \right| < \varepsilon \right\} = 1.</equation>


设随机变量<equation>n_{A}\sim B(n,p)</equation>，则对任意<equation>\varepsilon >0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \frac {n _ {A}}{n} - p \right| < \varepsilon \right\} = 1.</equation>


设<equation>X_{1}, X_{2}, \dots , X_{n}, \dots</equation>为相互独立同分布的随机变量序列，且其数学期望和方差都存在，分别记为<equation>\mu</equation>和<equation>\sigma^2</equation>.则对任意的<equation>x</equation>有

<equation>\lim _ {n \rightarrow \infty} P \left\{\frac {\sum_ {i = 1} ^ {n} X _ {i} - n \mu}{\sqrt {n} \delta} \leqslant x \right\} = \int_ {- \infty} ^ {x} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {i}{2}} \mathrm {d} t.</equation>


设随机变量<equation>\eta_{n}(n = 1,2,\dots)\sim B(n,p)</equation>，则对任意的<equation>x</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\frac {\eta_ {n} - n p}{\sqrt {n p (1 - p)}} \leqslant x \right\} = \int_ {- \infty} ^ {x} \frac {1}{\sqrt {2 \pi}} \mathrm {e} ^ {- \frac {i}{2}} \mathrm {d} t.</equation>

---


#### 二、统计分布与抽样分布定理


1. 样本均值

<equation>\bar {X} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k}.</equation>

2. 样本方差

<equation>S ^ {2} = \frac {1}{n - 1} \sum_ {k = 1} ^ {n} \left(X _ {k} - \bar {X}\right) ^ {2}.</equation>

3. r阶样本原点矩

<equation>A _ {r} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k} ^ {r}.</equation>

4. r阶样本中心矩

<equation>B _ {r} = \frac {1}{n} \sum_ {k = 1} ^ {n} \left(X _ {k} - \bar {X}\right) ^ {r}.</equation>


1.<equation>\chi^{2}</equation>分布

设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>相互独立且均服从<equation>N(0,1)</equation>，令<equation>Y = \sum_{k=1}^{n} X_{k}^{2}</equation>，称随机变量<equation>Y</equation>的分布为自由度为<equation>n</equation>的<equation>\chi^{2}</equation>

---


#### (1)一维正态总体情形


分布，并记为<equation>Y\sim \chi^{2}(n)</equation>. 其数字特征<equation>EY = n, DY = 2n.</equation>


设随机变量<equation>X\sim N(0,1),Y\sim \chi^{2}(n)</equation>且相互独立，令<equation>T = \frac{X}{\sqrt{Y / n}}</equation>，称随机变量<equation>T</equation>的分布为自由度为<equation>n</equation>的<equation>t</equation>分布，并记为<equation>T\sim t(n)</equation>.记随机变量<equation>T</equation>的密度函数为<equation>f_{n}(x)</equation>，则<equation>f_{n}(x)</equation>满足：


<equation>\textcircled{2} \lim_{n \to \infty} f_{n}(x) = \frac{1}{\sqrt{2 \pi}} \mathrm{e}^{-\frac{x^{2}}{2}}.</equation>


设随机变量<equation>X\sim \chi^{2}(m),Y\sim \chi^{2}(n)</equation>且相互独立.令<equation>F = \frac{X / m}{Y / n}</equation>，称其分布为自由度为<equation>(m,n)</equation>的<equation>F</equation>分布，记为<equation>F\sim F(m,n)</equation>，由定义易知<equation>\frac{1}{F}\sim F(n,m)</equation>.


设<equation>X_{1}, X_{2}, \dots, X_{n}</equation>为来自正态总体<equation>X \sim N(\mu, \delta^{2})</equation>的容量为<equation>n</equation>的简单随机样本，<equation>\bar{X}</equation>为样本均值，<equation>S^{2}</equation>为样本方差，则

<equation>\textcircled{1} Z = \frac {\bar {X} - \mu}{\delta / \sqrt {n}} \sim N (0, 1).</equation>

---


#### (2) 二维正态总体情形


<equation>\textcircled{2} Y=\frac{(n-1)S^{2}}{\delta^{2}}\sim\chi^{2}(n-1).</equation>

<equation>\textcircled{3}</equation>随机变量 Y与 Z相互独立，即<equation>\overline{{X}}</equation>与<equation>S^{2}</equation>相互独立<equation>\textcircled{4}</equation><equation>\frac{\overline{{X}} - \mu}{S / \sqrt{n}}\sim t(n-1).</equation>


设<equation>X_{1}, X_{2}, \dots X_{m}</equation>为来自正态总体<equation>X \sim N(\mu_{1}, \delta_{1}^{2})</equation>的容量为<equation>m</equation>的简单随机样本，<equation>\overline{X}</equation>为样本均值，<equation>S_{1}^{2}</equation>为样本方差；<equation>Y_{1}, Y_{2}, \dots, Y_{n}</equation>为来自正态总体<equation>Y \sim N(\mu_{2}, \delta_{2}^{2})</equation>的容量为<equation>n</equation>的简单随机样本，<equation>\overline{Y}</equation>为样本均值，<equation>S_{2}^{2}</equation>为样本方差，且两总体相互独立，则：

<equation>\textcircled{1} Z = \frac {\left(\bar {X} - \bar {Y}\right) - \left(\mu_ {1} - \mu_ {2}\right)}{\sqrt {\frac {\delta_ {1} ^ {2}}{m} + \frac {\delta_ {2} ^ {2}}{n}}} \sim N (0, 1).</equation>

<equation>\textcircled{2} \frac {(m - 1) S _ {1} ^ {2}}{\delta_ {1} ^ {2}} + \frac {(n - 1) S _ {2} ^ {2}}{\delta_ {2} ^ {2}} \sim \chi^ {2} (m + n - 2).</equation>

<equation>\textcircled{4}</equation>当<equation>\delta_1^2 = \delta_2^2 = \delta^2</equation>时，有

<equation>T = \frac {\left(\bar {X} - \bar {Y}\right) - \left(\mu_ {1} - \mu_ {2}\right)}{S _ {w} \sqrt {\frac {1}{m} + \frac {1}{n}}} \sim t (m + n - 2).</equation>

其中<equation>S_{w}^{2}=\frac{(m-1)S_{1}^{2}+(n-1)S_{2}^{2}}{m+n-2}.</equation>

---


### 第七章 答数估计

#### 二、最大似然估计法


估计公式：

<equation>\hat {\mu} _ {k} = A _ {k},</equation>

其中<equation>\mu_{k}</equation>为总体的<equation>k</equation>阶原点矩，<equation>A_{k}</equation>为样本<equation>k</equation>阶原点矩.


1. 样本似然函数

<equation>L (\theta) = L \left(x _ {1}, x _ {2}, \dots , x _ {n}; \theta\right).</equation>

2. 最大似然估计值与最大似然估计量

若<equation>L(x_{1},x_{2},\dots ,x_{n};\hat{\theta}) = \max L\{(x_{1},x_{2},\dots ,x_{n};\theta)\}</equation>，则称<equation>\hat{\theta} (x_{1},x_{2},\dots ,x_{n})</equation>为参数<equation>\theta</equation>的最大似然估计值，而称<equation>\hat{\theta}</equation><equation>(X_{1},X_{2},\dots ,X_{n})</equation>为参数<equation>\theta</equation>的最大似然估计量.

3. 由矩法和最大似然估计法得到的正态总体参数的估计量

<equation>\hat {\mu} = A _ {1} = \bar {X},</equation>

<equation>\hat {\sigma} ^ {2} = A _ {2} - A _ {1} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(X _ {i} - \bar {X}\right) ^ {2}.</equation>

---


#### 三、置信区间


<equation>\textcircled{1}</equation>定义：若<equation>E(\partial) = \theta</equation>，称<equation>\hat{\theta}</equation>是<equation>\theta</equation>的无偏估计量.

<equation>\textcircled{2}</equation>结论：因为<equation>E(\overline{X}) = \mu , E(S^2) = \delta^2</equation>，所以<equation>\overline{X}</equation>是样本均值<equation>\mu</equation>的无偏估计量，样本方差<equation>S^{2}</equation>是总体方差<equation>\sigma^{2}</equation>的无偏估计量.


设<equation>\hat{\theta}_1 = \hat{\theta}_1\left(X_1, X_2, \dots, X_n\right)</equation>与<equation>\hat{\theta}_2 = \hat{\theta}_2\left(X_1, X_2, \dots, X_n\right)</equation>都是<equation>\theta</equation>的无偏估计量，若对任意<equation>\theta \in \Theta</equation>，有<equation>D(\hat{\theta}_1) \leqslant D(\hat{\theta}_2)</equation>，且至少对于某一个<equation>\theta \in \Theta</equation>，上式中不等号成立，则称<equation>\hat{\theta}_1</equation>较<equation>\hat{\theta}_2</equation>有效.


若对于任意<equation>\theta \in \Theta</equation>都满足：对任意<equation>\epsilon > 0</equation>，有

<equation>\lim _ {n \rightarrow \infty} P \left\{\left| \hat {\theta} - \theta \right| < \varepsilon \right\} = 1,</equation>

则称<equation>\hat{\theta}</equation>是<equation>\theta</equation>的一致估计量.


设总体<equation>X</equation>的分布律中含有未知参数<equation>\theta</equation>，来自该总体的几个样本为<equation>X_{1}, X_{2}, \dots, X_{n}, 0 < \alpha < 1.</equation>若存在统计量<equation>\hat{\theta}_{1}</equation>和<equation>\hat{\theta}_{2}</equation>，使得<equation>P(\hat{\theta}_{1} \leqslant \theta \leqslant \hat{\theta}_{2}) = 1 - \alpha</equation>，则称<equation>1 - \alpha</equation>为置信度，<equation>(\hat{\theta}_{1}, \hat{\theta}_{2})</equation>为<equation>\theta</equation>的置信区间.

---

四、常用单个正态总体参数的置信区间表

<table border="1"><tr><td>参数</td><td colspan="2"><equation>\mu</equation></td><td><equation>\delta^{2}</equation></td></tr><tr><td>条件</td><td>已知<equation>\delta^{2}</equation></td><td>未知<equation>\delta^{2}</equation></td><td><equation>\mu</equation>未知</td></tr><tr><td>置信区间</td><td><equation>\left[\bar{X}-\frac{\delta}{\sqrt{n}}z_{\frac{\alpha}{2}}, \bar{X}+\frac{\delta}{\sqrt{n}}z_{\frac{\alpha}{2}}\right]</equation></td><td><equation>\left[\bar{X}-\frac{S}{\sqrt{n}}t_{\frac{\alpha}{2}}(n-1), \bar{X}+\frac{S}{\sqrt{n}}t_{\frac{\alpha}{2}}(n-1)\right]</equation></td><td><equation>\left[\frac{(n-1)S^{2}}{\chi_{\frac{\alpha}{2}}^{2}(n-1)},\frac{(n-1)S^{2}}{\chi_{1-\frac{\alpha}{2}}^{2}(n-1)}\right]</equation></td></tr></table>

---


#### 3. 不等式


<equation>\textcircled{1}</equation><equation>( a \pm b )^{2}=a^{2} \pm 2 a b+b^{2}</equation>

<equation>\textcircled{3} a^{2}-b^{2}=(a-b)(a+b);</equation>

<equation>\textcircled{4}</equation><equation>(a\pm b)^{3}=a^{3}\pm 3a^{2}b+3ab^{2}\pm b^{3};</equation>

<equation>\textcircled{6} a^{n}-b^{n}=(a-b)(a^{n-1}+a^{n-2}b+a^{n-3}b^{2}+\cdots+ a b^{n-2}+b^{n-1})</equation>（n为正整数）.


(1) 一元二次方程<equation>a x^{2}+b x+c=0 ( a \neq0 )</equation>的求根公式

<equation>x _ {1, 2} = \frac {- b \pm \sqrt {b ^ {2} - 4 a c}}{2 a}.</equation>

(2) 根与系数之间的关系

<equation>x _ {1} + x _ {2} = - \frac {b}{a}, x _ {1} x _ {2} = \frac {c}{a}.</equation>

---

<equation>\textcircled{2}</equation><equation>\frac{a+b}{2}\geqslant\sqrt{ab}</equation>（a,b<equation>\in\mathbf{R}^{+}</equation>）;

<equation>\textcircled{4}</equation>柯西不等式<equation>(a^{2} + b^{2})(c^{2} + d^{2}) \geqslant (ac + bd)^{2}</equation>;

<equation>\textcircled{5}</equation><equation>|a| - |b| \leqslant |a + b| \leqslant |a| + |b|</equation>;

<equation>\textcircled{6}</equation><equation>\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}\geqslant\sqrt[n]{a_{1}a_{2}\cdots a_{n}}</equation><equation>(a_{i}>0,i=1,</equation>2,…,n).

4. 指数

<equation>\textcircled{1}</equation><equation>a^{m} \cdot a^{n} = a^{m+n}</equation>;

<equation>\textcircled{2}</equation><equation>a^{m}\div a^{n}=a^{m-n};</equation>

<equation>\textcircled{3}</equation><equation>( a^{m} )^{n}=a^{n m}</equation>

<equation>\textcircled{4} ( a b )^{m}=a^{m} b^{m}</equation>

<equation>\textcircled{5}</equation><equation>\left( \frac{a}{b} \right)^{m}=\frac{a^{m}}{b^{m}};</equation>

<equation>\textcircled{6} a^{-m}=\frac{1}{a^{m}};</equation>

<equation>\textcircled{7} a^{0}=1(a>0).</equation>

5. 对数<equation>(\log_{a} N,a > 0,a\neq 1)</equation>

<equation>\textcircled{1} N=a^{\log N};</equation>

<equation>\textcircled{2} \log_{a}(M N)=\log_{a} M+\log_{a} N;</equation>

<equation>\textcircled{3}</equation><equation>\log_ {a}\left(\frac {M}{N}\right) = \log_ {a} M - \log_ {a} N;</equation>

<equation>\textcircled{4} \log_{a} ( M^{n} )=n \log_{a} M;</equation>

---

<equation>\textcircled{5} \log_{a}\sqrt[n]{M}=\frac{1}{n}\log_{a}M;</equation>

<equation>\textcircled{6}</equation>换底公式：<equation>\log_{a}M = \frac{\log_{b}M}{\log_{b}a}</equation>；

<equation>\textcircled{7} \log_{a} 1=0,\log_{a} a=1.</equation>

6. 数列

(1) 等差数列

<equation>\textcircled{1}</equation>通项公式

<equation>a _ {n} = a _ {1} + (n - 1) d.</equation>

<equation>\textcircled{2}</equation>前 n项的和

<equation>S _ {n} = \frac {n}{2} \left(a _ {1} + a _ {n}\right) = n a _ {1} + \frac {1}{2} n (n - 1) d.</equation>

(2) 等比数列

<equation>\textcircled{1}</equation>通项公式

<equation>a _ {n} = a _ {1} q ^ {n - 1}.</equation>

<equation>\textcircled{2}</equation>前 n项的和

<equation>S _ {n} = \left\{ \begin{array}{l l} n a _ {1}, & q = 1, \\ \frac {a _ {1} - a _ {n} q}{1 - q} = \frac {a _ {1} \left(1 - q ^ {n}\right)}{1 - q}, q \neq 1. \end{array} \right.</equation>

(3) 常用数列前 n项的和

<equation>1 + 2 + \dots + n = \frac {n (n + 1)}{2};</equation>

<equation>1 + 3 + 5 + \dots + (2 n - 1) = n ^ {2};</equation>

---


#### 7. 排列、组合与二项式公式


<equation>1 ^ {2} + 2 ^ {2} + \dots + n ^ {2} = \frac {n (n + 1) (2 n + 1)}{6}.</equation>


(1) 排列数

<equation>\textcircled{1}</equation><equation>A_{n}^{k} = n(n - 1)\dots (n - k + 1)</equation>（元素不可重复的排列）

<equation>\textcircled{2} n^{k}</equation>（元素可以重复的排列）

<equation>\textcircled{3} n! = n ( n - 1 ) \dots 3 \cdot 2 \cdot 1</equation>（全排列）

(2) 组合数

<equation>C _ {n} ^ {k} = \frac {\mathrm {A} _ {n} ^ {k}}{k !} = \frac {n (n - 1) \cdots (n - k + 1)}{k !} = \frac {n !}{(n - k) ! k !}.</equation>

(3) 二项式定理

<equation>(a + b) ^ {n} = \sum_ {k = 0} ^ {n} \mathrm {C} _ {n} ^ {k} \cdot a ^ {n - k} \cdot b ^ {k}, n \in \mathrm {N}.</equation>

---


#### 2. 梯形的面积


<equation>\textcircled{1}</equation><equation>S=\frac{1}{2} a b \sin C</equation>（若<equation>C=\frac{\pi}{2}</equation>，即直角三角形的面积<equation>S=\frac{1}{2} a b</equation>

<equation>\textcircled{2}</equation><equation>S=\sqrt{s(s-a)(s-b)(s-c)},</equation>其中 a,b,c为其三边长，<equation>s=\frac{1}{2} ( a+b+c).</equation>


<equation>S=\frac{1}{2} ( a+b) h</equation>，其中a，b为上下底，高为h.

3. 圆（半径为 r）

<equation>\textcircled{1}</equation>圆周长

<equation>l = 2 \pi r;</equation>

<equation>\textcircled{2}</equation>圆弧长

<equation>l = r \theta ,</equation>

其中<equation>\theta</equation>为圆弧所对的圆心角（单位为弧度）.

<equation>\textcircled{3}</equation>扇形面积

---


#### 4. 旋转体


<equation>S = \frac {1}{2} r ^ {2} \theta ,</equation>

其中<equation>\theta</equation>为圆心角.


(1) 圆柱（底面圆半径为<equation>r</equation>，柱高为<equation>h</equation>）

<equation>\textcircled{1}</equation>侧面积<equation>= 2\pi rh;</equation>

<equation>\textcircled{2}</equation>全面积<equation>= 2\pi r(r + h);</equation>

<equation>\textcircled{3}</equation>体积<equation>= \pi r^{2}h.</equation>

(2) 圆锥（底面圆半径为 r，高为 h，母线长为<equation>l=\sqrt{r^{2}+h^{2}}</equation>）

<equation>\textcircled{1}</equation>侧面积<equation>= \pi r l;</equation>

<equation>\textcircled{2}</equation>全面积<equation>= \pi r(l+r);</equation>

<equation>\textcircled{3}</equation>体积<equation>= \frac{1}{3}\pi r^{2}h.</equation>

(3) 圆台（上、下底面圆半径为<equation>r_{1}, r_{2}</equation>，高为h，母线长为<equation>l=\sqrt{h^{2}+(r_{2}-r_{1})^{2}}</equation>

<equation>\textcircled{1}</equation>侧面积<equation>= \pi (r_{1} + r_{2})l</equation>;

<equation>\textcircled{2}</equation>全面积<equation>= \pi r_{1}(l+r_{1})+\pi r_{2}(l+r_{2}).</equation>

<equation>\textcircled{3}</equation>体积<equation>= \frac{1}{3}\pi h\left(r_{1}^{2}+r_{2}^{2}+r_{1}r_{2}\right).</equation>

(4) 球（半径为 r）

<equation>\textcircled{1}</equation>全面积<equation>= 4\pi r^{2}.</equation>

<equation>\textcircled{2}</equation>体积<equation>= \frac{4}{3}\pi r^{3}.</equation>
