import java.util.Stack;

/**
 * Created by Luffy on 2017/3/20.
 */
public class q19_MirrorTree {
	public void Mirror(TreeNode root){
		TreeNode tmp = null;
		if (root != null){
			tmp = root.left;
			root.left = root.right;
			root.right = tmp;
			if (root.left != null)
				Mirror(root.left);
			if (root.right != null)
				Mirror(root.right);
		}
	}

	public void Mirror_no_recursive(TreeNode root){
		if (root == null)
			return;
		Stack<TreeNode> stack = new Stack<TreeNode>();
		stack.push(root);
		while (!stack.isEmpty()){
			TreeNode node = stack.pop();
			if (node.left != null || node.right != null){
				TreeNode tmp = node.left;
				node.left = node.right;
				node.right = tmp;
			}
			if (node.left != null)
				stack.push(node.left);
			if (node.right != null)
				stack.push(node.right);
		}
	}
}
