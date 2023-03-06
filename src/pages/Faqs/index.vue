<template>
    <div class="container" style="margin-top: 130px;">
        <div id="title">
                <h3>FAQs</h3>
        </div>
        <div class="faqsForm">
            <table>
                <tr>
                    <td>Q1.&nbsp;&nbsp;How do I contact your office team?</td>
                </tr>
                <tr>
                    <td>A.&nbsp;&nbsp;&nbsp;Please send us an email at Contact Us.</td>
                </tr>
                <tr>
                    <td>Q2.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q3.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q4.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q5</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q6.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q7.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q8.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q9.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
                <tr>
                    <td>Q10.</td>
                </tr>
                <tr>
                    <td>A.</td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Faqs',
}
</script>

<style scoped lang="less">
.container{
    background-color: orange;
    height: 980px;

    h3{
        color: black;
    }
    .faqsForm{
        width: 1110px;
        margin-top: 10px;
        // margin-left: 20px;
        // text-align: center;
        background-color: wheat;

            table{
                border: 1px solid orange;
                width: 1110px;
                text-align: left;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                color: black;
            }
            table tr{
                border: 1px solid white;
            }
            table td{
                padding: 10px;
                // margin-left: 50px;
            }
        }
    }


</style>
<!-- table,
td,
th {
  text-align: center;
  border: 1px solid #000;
  border-collapse: collapse;
}

table td {
  padding: 10px 30px;
} -->