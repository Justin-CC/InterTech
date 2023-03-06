<template>
    <section id="menu" class="menu">
        <div class="container">

            <div class="section-title">
                <h2 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Check our tasty <span style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Menu</span></h2>
            </div>

            <div class="row">
                <div class="col-lg-12 d-flex justify-content-center">
                    <ul id="menu-flters" style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">
                        <li data-filter="*" class="filter-active">Show All</li>
                        <li data-filter=".filter-starters">Starters</li>
                        <li data-filter=".filter-salads">Salads</li>
                        <li data-filter=".filter-specialty">Specialty</li>
                    </ul>
                </div>
            </div>

            <div class="row menu-container">

                <div class="col-lg-6 menu-item filter-starters" v-for="item in mockMenuList" :key="item.id">
                    <div class="menu-content">
                        <a :href="`#/MenuDetail?MealId=${item.id}`">{{item.name}}</a><span>{{item.price}}</span>
                    </div>
                    <div class="menu-ingredients">
                        {{item.disc}}
                    </div>
                </div>

                <!-- <div class="col-lg-6 menu-item filter-starters">
                    <div class="menu-content">
                        <a href="#">Lobster Bisque</a><span>$5.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Lorem, deren, trataro, filede, nerada
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-specialty">
                    <div class="menu-content">
                        <a href="#">Bread barrel</a><span>$6.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Lorem, deren, trataro, filede, nerada
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-starters">
                    <div class="menu-content">
                        <a href="#">Crab Cake</a><span>$7.95</span>
                    </div>
                    <div class="menu-ingredients">
                        A delicate crab cake served on a toasted roll with lettuce and tartar sauce
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-salads">
                    <div class="menu-content">
                        <a href="#">Caesar Selections</a><span>$8.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Lorem, deren, trataro, filede, nerada
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-specialty">
                    <div class="menu-content">
                        <a href="#">Tuscan Grilled</a><span>$9.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Grilled chicken with provolone, artichoke hearts, and roasted red pesto
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-starters">
                    <div class="menu-content">
                        <a href="#">Mozzarella Stick</a><span>$4.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Lorem, deren, trataro, filede, nerada
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-salads">
                    <div class="menu-content">
                        <a href="#">Greek Salad</a><span>$9.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Fresh spinach, crisp romaine, tomatoes, and Greek olives
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-salads">
                    <div class="menu-content">
                        <a href="#">Spinach Salad</a><span>$9.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Fresh spinach with mushrooms, hard boiled egg, and warm bacon vinaigrette
                    </div>
                </div>

                <div class="col-lg-6 menu-item filter-specialty">
                    <div class="menu-content">
                        <a href="#">Lobster Roll</a><span>$12.95</span>
                    </div>
                    <div class="menu-ingredients">
                        Plump lobster meat, mayo and crisp lettuce on a toasted bulky roll
                    </div>
                </div> -->

            </div>

        </div>
    </section><!-- End Menu Section -->
</template>

<script>
import { mapState } from 'vuex'
export default {
    name: '',
    data() {
      return {
        mockMenuList : [
          {
            id: 1,
            type: 1,
            name:"Lobster Bisque",
            price: "$5.95",
            disc:"Lorem, deren, trataro, filede, nerada",
          },
          {
            id: 2,
            type: 1,
            name:"Bread barrel",
            price: "$6.95",
            disc:"Lorem, deren, trataro, filede, nerada",
          },
          {
            id: 3,
            type: 1,
            name:"Crab Cake",
            price: "$7.95",
            disc:"A delicate crab cake served on a toasted roll with lettuce and tartar sauce",
          },
          {
            id: 4,
            type: 1,
            name:"Lobster Bisque",
            price: "$5.95",
            disc:"Lorem, deren, trataro, filede, nerada",
          },
          {
            id: 5,
            type: 1,
            name:"Bread barrel",
            price: "$6.95",
            disc:"Lorem, deren, trataro, filede, nerada",
          },
          {
            id: 6,
            type: 1,
            name:"Crab Cake",
            price: "$7.95",
            disc:"A delicate crab cake served on a toasted roll with lettuce and tartar sauce",
          },
          {
            id: 7,
            type: 1,
            name:"Lobster Bisque",
            price: "$5.95",
            disc:"Lorem, deren, trataro, filede, nerada",
          },
          {
            id: 8,
            type: 1,
            name:"Bread barrel",
            price: "$6.95",
            disc:"Lorem, deren, trataro, filede, nerada",
          },
          {
            id: 9,
            type: 1,
            name:"Crab Cake",
            price: "$7.95",
            disc:"A delicate crab cake served on a toasted roll with lettuce and tartar sauce",
          },
        ]
      }
    },
    mounted() {
      // getMenuList
      // this.$store.dispatch('menuList');
    },
    computed: {
        ...mapState({
            menuList: state => state.home.menuList
        })
    }
}
</script>

<style scoped></style>
