import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    strings = []
    len_list = [[] for i in range(50)]
    res = 0
    # 存储字符串
    for i in range(num):
        strings.append(sys.stdin.readline().strip())
    # 字符串长度一样的放到strings列表中相应的位置中
    for s in strings:
        len_list[len(s)].append(s)
    # 在长度一样的字符串中找同类字符串
    for same_len in len_list:
        # 不为空
        if same_len:
            for i in range(len(same_len)):
                a_dict = {}
                for c in same_len[i]:
                    a_dict[c] = a_dict.get(c,0) + 1
                for j in range(i+1, len(same_len)):
                    b_dict = {}
                    for c in same_len[j]:
                        b_dict[c] = b_dict.get(c,0) + 1
                    if a_dict != b_dict:
                        res += 1
                    else:
                        break
            res += 1
    print(res)

