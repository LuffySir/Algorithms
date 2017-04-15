/**
 * Created by Luffy on 2017/3/16.
 */
public class q2_ReplaceSpace {
	public String replace_spaces(StringBuffer str){
		int spaces = 0;
		for(int i = 0; i < str.length(); i++){
			if(str.charAt(i) == ' ')
				spaces ++;
		}
		int tail = str.length() - 1;
		int len = str.length() + spaces * 2;
		int end = len - 1;
		str.setLength(end);
		for(;tail >= 0 && tail < len; --tail){
			if (str.charAt(tail) == ' '){
				str.setCharAt(end--, '0');
				str.setCharAt(end--, '2');
				str.setCharAt(end--, '%');
			}else{
				str.setCharAt(end--, str.charAt(tail));
			}
		}
		return str.toString();
	}
}
