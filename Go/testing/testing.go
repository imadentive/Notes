// go test . 测试当前目录下的test
// test所在文件必须以_test.go结尾
// test方法都以Test开头并且会传一个*testing.T

// 获取代码测试覆盖率
// go test -coverprofile=c.out
// go tool cover -html=c.out

// 测试当前目录下的benchmark测试
// go test -bench .

// 运行pprof后会进入一个交互的命令行
// go test -bench . -cpuprofile cpu.out
// go tool pprof cpu.out

// 在pprof中输入web就可以看到cpu使用的分布图
// 由于该图是svg，所以需要安装一个graphviz工具
// 图中方框越大线越粗就代表cpu使用越高

// 执行go doc会显示当前包下的文档
// go doc后面可以跟一些包下面相关的类型，接口，函数等
// godoc -http :6060  开启一个go doc的web服务
// 会包括gopath和goroot下的包

// 在_test.go文件下面可以添加示例代码方法用来在doc中显示
// 示例方法以Example开头后面接函数名 参看queue_test.go
// 函数后面需要加注释表示expect的output信息, e.g.
// Output:
// 1
// 2
// false
// 3
// true
// go test时，Example方法也会被加入test case中