2/2 # 结果为float型
2//2 # 结果为int型
bin(10) # 将数字转2进制
oct(10) # 转8进制
hex(10) # 转16进制
ord('w') # 获取字符ASCII码

bool('') # 空字符串，空列表，空字典，0，None等返回False

r'c:\n123' # 会输出原始字符转，不会解释转义字符
aa = 'test'
aa = u'test'  # 轉爲unicode類型

# tuple不可變，存取時tuple和字典都快於列表

#set是无序的，无法用下标取值
{1,2,3} - {2,3} # 取集合差值
{1,2,3} & {2,3} # 取交集
{1,2,3} | {2,3,4} # 取并集

# is比较两个变量内存地址是否相同
# isinstance(a, int)判断变量类型
# isinstance可以多个类型筛选 e.g. isinstance(a, (int, str, float))

# 將列表轉換位迭代器
iter([1, 2, 3]) # 此時該對象就可以通過next方法調用

# 生成器
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o) # 1
next(o) # 3
next(o) # 5
next(o) # 報錯

# 列表解析
aa = [1, 2, 3]
[ item + 2 for item in aa ] # [3, 4, 5]

# 生成器表達式
( item + 2 for item in aa ) # 返回一個生成器，可以通過next調用

# lambda定義匿名函數
a = lambda x, y: x + y
a(20, 40)

# Regex
# {N}                  匹配前面出现的正则表达式N次    [0-9]{3}
# {M,N}                匹配重复出现M次到N次正则表达式 [0-9]{5,9}
# re1|re2              匹配正则表达式re1或re2 
# \bthe                任何以"the"开始的字符串
# \bthe\b              仅匹配单词"the"
# \Bthe                任意包含"the"但不以"the"开头的单词
# b[aeiu]t             bat, bet, bit, but
# [cr][23][dp][o2]     一个包含 4 个字符的字符串: 第一个字符是“r”或“c”,后面是“2”或 “3”,再接下来是 “d” 或 “p”,最后是 “o” 或 “2“ ,例 如:c2do, r3p2, r2d2, c3po, 等等。 
# [r-u][env-y][us]     “r”“s,”“t” 或 “u” 中的任意一个字符,后面跟的是 “e,” “n,” “v,” “w,” “x,” 或 “y”中的任意一个字符,再后面 是字符“u” 或 “s”. 
# [^aeiou]             一个非元音字符 
# [^\t\n]              除 TAB 制表符和换行符以外的任意一个字符 
# \w+@\w+\.com         简单的 XXX@YYY.com 格式的电子邮件地址 
# \d+(\.\d*)?          浮点数 匹配：0.004,”“2.”“75.”

import re
# from re import search as ss  導入模塊的某個方法並取別名
re.search("a.c", "123abcyul")
r = re.match("(a.c)", "123abcyul") # match會從頭開始匹配,只要前面不匹配就會返回空
r.groups() # 返回匹配的內容, 是一個元組
r.group(0) # 返回原字符串
r.group(1) # 返回第一個匹配

# 裝飾器
def use_logging(func):
    def wrapper(*args, **kwargs):
        print("%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()
