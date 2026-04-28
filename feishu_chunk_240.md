#### 3. 分块对角形（对角块）矩阵

其中<equation>C_{ik} = A_{i1}B_{1k} + A_{i2}B_{2k} + \dots + A_{it}B_{tk} = \sum_{j=1}^{i}A_{ij}B_{jk}</equation><equation>(i = 1,\dots,s;k = 1,\dots,r).</equation>


一般地，分块矩阵<equation>A = \left[ \begin{array}{cccc}A_{11} & O & \dots & O\\ O & A_{22} & \dots & O\\ \vdots & \vdots & & \vdots \\ O & O & \dots & A_{s} \end{array} \right],</equation>

简记为<equation>A = \left[ \begin{array}{c c c c} A_{11} & & & \\ & A_{22} & & \\ & & \ddots & \\ & & & A_{ss} \end{array} \right],</equation>其中<equation>A_{ii}</equation>均为小方

阵，则称<equation>A</equation>为对角块矩阵或分块对角形矩阵。若<equation>A, B</equation>均为对角块矩阵，则<equation>A + B, AB</equation>也为对角块矩阵，如：

<equation>\begin{array}{l} \boldsymbol {A} + \boldsymbol {B} = \left[ \begin{array}{c c c} \boldsymbol {A} _ {1} & & \\ & \boldsymbol {A} _ {2} & \\ & & \ddots \\ & & \boldsymbol {A} _ {s} \end{array} \right] + \left[ \begin{array}{c c c} \boldsymbol {B} _ {1} & & \\ & \boldsymbol {B} _ {2} & \\ & & \ddots \\ & & \boldsymbol {B} _ {s} \end{array} \right] \\ = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1} + \boldsymbol {B} _ {1} & & & \\ & \boldsymbol {A} _ {2} + \boldsymbol {B} _ {2} & & \\ & & \ddots & \\ & & & \boldsymbol {A} _ {s} + \boldsymbol {B} _ {s} \end{array} \right], \\ \end{array}</equation>

---


