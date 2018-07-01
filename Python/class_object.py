# 派生內置不可變類型並修改其實例化行爲
# 在創建對象是__init__之前其實會先讓類調用類方法__new__生成一個對象
# 接着再將該對象作爲__init__的第一個參數self傳入__init__
class A:
    def __new__(cls, *args):
        return object.__new__(cls)
    
    def __init__(self, *args):
        pass
# 例如像tuple類型，想要派生修改就需要在__new__中進行
# 因爲tuple初始化實在__new__中實現的



# 如何爲創建大量實例節省內存
# 對象中有一個__dict__屬性，用來支持對象的動態屬性設置
# 這個__dict__在一開始是沒有的，只有當我們開始復制對象屬性時才會產生
# p1.x = 100 等於 p1.__dict__['x'] = 100
# p1.__dict__.pop(x) 刪除屬性
# 這個字典就會佔用比較多的內存
# sys.getsizeof(p1.__dict__) 獲取內存佔用大小
# 如果要節省內存的話，可以通過__slots__
# 在類定義中使用__slots__ = ['uid', 'name', 'level']
# 這樣就會預先分配好屬性，並且之後不可以在動態添加

# 跟蹤內存使用
import tracemalloc
tracemalloc.start()
# start
# 跟蹤代碼
# end
snapshot = tracemalloc.take_snapshot()
# 按行數統計，也可以傳入filename，就是按文件統計
top_stats = snapshot.statistics('lineno')



# 如何讓對象支持上下文管理
