<template>
  <div >
    <!-- 封装组件：1.怎么设计这个组件  2.如何拆分-->
    <zh-carousel
       height="200px"
       :autoplay="true"
       :delay="2000"
       :initial-index="1"
       :loop="true"
       @change="change"
    >
       <zh-carousel-item>
         <div class="content" style="background:red">内容1</div>
       </zh-carousel-item>
       <zh-carousel-item>
         <div class="content" style="background:blue">内容2</div>
       </zh-carousel-item>
       <zh-carousel-item>
         <div class="content" style="background:yellow">内容3</div>
       </zh-carousel-item>
    </zh-carousel>
  </div>
</template>

<script>
export default {
  methods:{
    change(index){
      console.log(index);
    }
  }
}
</script>

<style lang="scss">
.content{
  height:100%;
  width:100%;
}
</style>