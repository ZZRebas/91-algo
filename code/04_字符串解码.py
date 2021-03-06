'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

思路：
用栈的方式记录左右括号，因为左右括号的读取是先进后出的顺序
解题方法类似于中缀表达式转波兰表达式
'''


def str_decode(s):
    stack=[]
    for i in range(len(s)): #遍历字符串s
        if s[i] != ']':     #如果不为’]‘就添加到栈stack
            stack.append(s[i])
        else:               #为’]‘，就更新栈：从离栈顶最近的'['到栈顶
            end_bracket_index=len(stack)-1-stack[-1::-1].index('[')   #获取离栈顶最近的'['的索引
            end_num=stack[end_bracket_index-1]    #获取离栈顶最近的'['的前面数字的索引
            stack_tail=stack[end_bracket_index+1:]    #获取离栈顶最近的'['到栈顶内的元素
            for n in stack_tail:    #离栈顶最近的'['到栈顶内的元素不能有数字
                if n.isdigit():
                    return '输入错误'
            if not end_num.isdigit():   #左括号前面一定有数字
                return '输入错误'
            stack=stack[:end_bracket_index-1]+(stack_tail*int(end_num))   #更新栈
    return ''.join(x for x in stack)

s1 = "3[a]2[bc]"
s2 = "3[a2[c]]"
s3 = "2[abc]3[cd]ef"
s4 = "abc3[cd]xyz"
print(str_decode(s1))   #aaabcbc
print(str_decode(s2))   #accaccacc
print(str_decode(s3))   #abcabccdcdcdef
print(str_decode(s4))   #abccdcdcdxyz

print(str_decode('2[sf]3[2[e]f]'))
