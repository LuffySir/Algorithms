/**
 * Created by Luffy on 2017/3/23.
 */
public class q27_ConvertBSTtoLinklist {
	public TreeNode Convert(TreeNode root){
		if (root == null)
			return null;
		if (root.left == null && root.right == null)
			return root;
//		1���������������˫��������������ͷ���
		TreeNode left = Convert(root.left);
		TreeNode p = left;
//		2����λ��������˫�������һ���ڵ�
		while (p != null && p.right != null){
			p = p.right;
		}
//		3���������������Ϊ�գ�����ǰroot׷�����������ĺ���
		if (left != null){
			p.right = root;
			root.left = p;
		}
//		4���������������˫��������������ͷ���
		TreeNode right = Convert(root.right);
//		5���������������Ϊ�գ���������׷�ӵ�root�ڵ�֮��
		if (right != null){
			right.left = root;
			root.right = right;
		}
		return left != null ? left:root;
	}
}
