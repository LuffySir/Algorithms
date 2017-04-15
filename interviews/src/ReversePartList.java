/**
 * Created by Luffy on 2017/3/19.
 */

public class ReversePartList {

	public static ListNode reverse_part(ListNode head, int len){
		if (head == null)
			return null;
		ListNode pre = null, next = null, newhead = head;
//		��ת����
		int i = 0;
//		��ת
		while ((i < len) && (head != null)){
			next = head.next;
			head.next = pre;
			pre = head;
			head = next;
			i ++;
		}
//		�������ת�ĸ��������������len�������Ѿ���ת�����һ���ڵ�
		if (head == null)
			return pre;
//		�ݹ�����ÿһ���Ѿ���ת������
		newhead.next = reverse_part(head, len);
//		�����ѷ�ת��ͷ���
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
