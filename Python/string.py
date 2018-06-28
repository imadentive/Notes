# regex拆分字符串
# 1
def my_split(s, seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss: t.extend(ss.split(sep)), res))
        res = t
    return res

# 2
from functools import reduce
my_split2 = lambda s, seps: reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), seps, [s])

# 3 這裏注意處理單個分隔符還是直接使用string自帶的split比較快
import re
re.split('[:,|\t]+', "123|123,456")



# 判斷字符串a是否以字符串b開頭或結尾
# 例子, 將.py或.sh結尾的文件轉爲可執行的
import os
import stat

for fn in os.listdir():
    # endswith或startswith如果需要多個匹配時可以使用元組
    if fn.endswith(('.py', '.sh')):
        fs = os.stat(fn)
        os.chmod(fn, fs.st_mode | stat.S_IXUSR)



# 調整字符串中文本的格式
# 例子, 將yyyy-mm-dd替換成mm/dd/yyyy
import re
# 括號用來表示組，替換時按照字母順序，
# 如果有括號嵌套的情況，前面數字先表示外面的括號
log = "2019-03-04 adsfsdfasfsa"
# 這裏記得替換是加r，代表raw
# 這樣python會直接當成\2輸出，而不會將它轉換成八進制數
# 例如 
# ord('a') 97
# oct(ord('a')) '0o141'
# '\141' a
# 如果不是用r的話那麼就需要使用'\\2'
re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
# 如果組太多想使用別名可以通過
re.sub(r'(?P<d>\d{4})-(?P<m>\d{2})-(?P<y>\d{2})', r'\g<m>/\g<d>/\g<y>', log)



# 拼接字符串
# 正常使用for循環等方法在時間與空間上都有浪費
# 推薦使用join方法
':'.join(['abc', '123', '456'])