##Binary Tree（二元樹）是一種樹狀數據結構，其中每個節點最多只能有兩個子節點，通常稱為：

左子節點（Left Child）
右子節點（Right Child）
Binary Tree 的特性
階層結構：類似樹狀層級，每個節點可以有最多兩個子節點。
遞迴定義：每個子節點本身也是一個 Binary Tree（或為空）。
深度（Depth）與高度（Height）：
深度（Depth）：從樹的根（Root）到該節點的邊數。
高度（Height）：從該節點到其最遠葉節點的邊數。
Binary Tree 的類型
Full Binary Tree（滿二元樹）：

每個節點要麼有兩個子節點，要麼是葉節點（沒有子節點）。
Complete Binary Tree（完全二元樹）：

除了最後一層，其他層的節點必須全部填滿。
最後一層的節點需從左至右填充，但不一定要滿。
Perfect Binary Tree（完美二元樹）：

每個節點都有兩個子節點，且所有葉節點都在相同深度。
Balanced Binary Tree（平衡二元樹）：

左右子樹的高度差最多為 1。
Degenerate (or Skewed) Binary Tree（退化二元樹）：

每個節點只有一個子節點（形成類似鏈表的結構）。

##Binary Search Tree（BST，二元搜尋樹） 定義
Binary Search Tree（BST，二元搜尋樹） 是一種 特殊類型的 Binary Tree，滿足以下特性：

左子樹（Left Subtree） 的所有節點值都 小於 根節點值。
右子樹（Right Subtree） 的所有節點值都 大於 根節點值。
每個子樹本身也是一個 BST（遞迴定義）。
