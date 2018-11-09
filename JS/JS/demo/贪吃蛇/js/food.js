// 1.定义一个食物构造函数
function Food(options) {
    options = options || {};

    // 食物的位置
    this.x = options.x || 0;
    this.y = options.y || 0;
    
    // 食物宽度和高度
    this.width = options.width || 50;
    this.height = options.height || 50;

    // 食物的颜色
    this.color = options.color || "red";
}

// 2.给食物对象添加一个渲染的方法
Food.prototype.rander = function (map) {

    // 1.动态的创建一个div元素, 作为食物
    var oDiv = document.createElement("div");
    // 2.将创建的div添加到地图中
    map.appendChild(oDiv);

    // 3.设置div的位置和宽高等样式
    // 3.1设置宽高
    oDiv.style.width = this.width + "px";
    oDiv.style.height = this.height + "px";
    // 3.2设置颜色和边框
    oDiv.style.backgroundColor = this.color;
    oDiv.style.borderRadius = "50%";
    // 3.3随机设置食物的位置
    // 3.3.1计算水平和垂直方向可以连续放多少个食物
    var rowNum = map.offsetWidth / this.width;
    var colNum = map.offsetHeight / this.height;
    // 3.3.2生成随机数
    // 注意点:
    // 如果map宽度是800, 每个食物是50, 我们可以放16个食物
    // 如果随机数的最大值是16, 那么将来的位置就是16 * 50, 会超出地图
    // 所以随机数的最大值应该是16 - 1
    this.x = getRandomIntInclusive(0, rowNum - 1);
    this.y = getRandomIntInclusive(0, colNum - 1);
    console.log(this.x, this.y);
    // 3.3.3设置食物的位置
    oDiv.style.position = "absolute";
    oDiv.style.left = this.x * this.width + "px";
    oDiv.style.top = this.y * this.height + "px";
};


// 编写测试代码
// 找到地图元素
var oMap = document.querySelector("#map");
// 创建一个食物对象
var food = new Food();
food.rander(oMap);