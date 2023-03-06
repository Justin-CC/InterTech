<template>
  <div class="container">
      <!-- 菜品图片
      <div class="meal-pic"></div> -->
      <!-- 菜品信息
      <div class="meal-info">
          name:"Lobster Bisque",
          price: "$5.95",
          disc:"Lorem, deren, trataro, filede, nerada",
      </div> -->
      <!-- 展示已有评论
      <div class="meal-comment-area"></div> -->
      <div class="meal-comment">
        <textarea maxlength="300" name="" id="" placeholder="Please input your comment for this dishes" v-model="comment"></textarea>
        <span class="tip">{{ comment.length }}/300</span>
      </div>
      <div class="submit-btn">
        <!-- <button style="width: 200px;">Submit</button> -->
        <button disabled="isSubmit" style="width: 200px;" @click.prevent="commentSubmit">{{isSubmit?"Submitting":"Submit"}}</button>
        <!-- <button @click="userRegister">Submit</button> -->
      </div>

    </div>
  <!-- <h2>meal detail,{{mealId}}</h2> -->
</template>

<script>
export default {
  data() {
    return {
     mealId : this.$route.query.MealId,
     comment:"",
    // 表示是否正在提交中
     isSubmit:false,
    }
  },
  methods:{
    async commentSubmit(){
      try {
        const { comment } = this;
        comment && (await this.$store.dispatch('commentSubmit', { comment }));
        this.$router.push("/MenuDetail");
      } catch (error) {
        alert(error.message);
      }
    }
  }
}
</script>

<style>

/* comment submit */
.meal-comment textarea{
  margin-top: 200px;
  width: 800px;
  height: 200px;

}
.meal-comment .tip{
  padding: 0 0 0 10px;
}

.submit-btn button {
  background-color: orange;
  padding: 6px;
  border-radius: 0;
  font-size: 16px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  word-spacing: 4px;
  border: 1px solid orange;
  color: #fff;
  width: 100%;
  height: 36px;
  margin-top: 15px;
  outline: none;
}


</style>