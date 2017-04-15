/**
 * Created by Luffy on 2017/3/18.
 */

public class q11_FindKthFromTail {
	public ListNode find(ListNode head, int k){
		if (head == null || k <= 0){
			return null;
		}
		ListNode pre = head;
		ListNode last = head;
		for (int i = 1; i < k; i++){
			if (pre.next != null){
				pre = pre.next;
			}else
				return null;
		}
		while (pre.next != null){
			pre = pre.next;
			last = last.next;
		}
		return last;
	}
}
