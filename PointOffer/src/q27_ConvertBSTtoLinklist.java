/**
 * Created by Luffy on 2017/3/23.
 */
public class q27_ConvertBSTtoLinklist {
	public TreeNode Convert(TreeNode root){
		if (root == null)
			return null;
		if (root.left == null && root.right == null)
			return root;
//		1、将左子树构造成双链表，并返回链表头结点
		TreeNode left = Convert(root.left);
		TreeNode p = left;
//		2、定位至左子树双链表最后一个节点
		while (p != null && p.right != null){
			p = p.right;
		}
//		3、如果左子树链表不为空，将当前root追加至左子树的后面
		if (left != null){
			p.right = root;
			root.left = p;
		}
//		4、将右子树构造成双链表，并返回链表头结点
		TreeNode right = Convert(root.right);
//		5、如果右子树链表不为空，将该链表追加到root节点之后
		if (right != null){
			right.left = root;
			root.right = right;
		}
		return left != null ? left:root;
	}
}
