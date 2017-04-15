/**
 * Created by Luffy on 2017/3/19.
 */

public class ReversePartList {

	public static ListNode reverse_part(ListNode head, int len){
		if (head == null)
			return null;
		ListNode pre = null, next = null, newhead = head;
//		反转个数
		int i = 0;
//		反转
		while ((i < len) && (head != null)){
			next = head.next;
			head.next = pre;
			pre = head;
			head = next;
			i ++;
		}
//		如果待反转的个数不足给定长度len，返回已经反转的最后一个节点
		if (head == null)
			return pre;
//		递归链接每一段已经反转的链表
		newhead.next = reverse_part(head, len);
//		返回已反转的头结点
		return pre;
	}

	public static void main(String[] args) {
		ListNode p1 = new ListNode(1);
		ListNode p2 = new ListNode(2);
		ListNode p3 = new ListNode(3);
		ListNode p4 = new ListNode(4);
		ListNode p5 = new ListNode(5);
		ListNode p6 = new ListNode(6);
		ListNode p7 = new ListNode(7);
		ListNode p8 = new ListNode(8);
		p1.next = p2;
		p2.next = p3;
		p3.next = p4;
		p4.next = p5;
		p5.next = p6;
		p6.next = p7;
		p7.next = p8;
		ListNode h = reverse_part(p1, 3);
		for (int i = 0; i < 8; i++) {
			System.out.println(h.val);
			h = h.next;
		}
	}
}
