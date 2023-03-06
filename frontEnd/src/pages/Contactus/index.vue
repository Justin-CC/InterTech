<template>
    <!-- ======= Contact Section ======= -->
    <section id="contact" class="contact" style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">
        <div class="container">

            <div class="section-title" style="margin-top: 100px;">
                <h2 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;"><span>Contact</span> Us</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam corrupti iure minima repellendus est dolore exercitationem ullam iste fugiat asperiores, a debitis quia voluptate commodi, enim quisquam, amet delectus sint!</p>
                    <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem earum aspernatur assumenda impedit itaque delectus totam architecto mollitia dolore deleniti. Modi qui quod consequuntur, in quo voluptatem. Consectetur, nihil a.</p> -->
            </div>
        </div>

        <div class="map">
            <iframe style="border:0; width: 100%; height: 350px;"
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4476.866970922372!2d-4.294356916003157!3d55.87249485707186!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x488845d20af469b3%3A0xa3f0620b655e4983!2sUniversity%20of%20Glasgow!5e0!3m2!1sen!2suk!4v1676898551466!5m2!1sen!2suk"
                frameborder="0" allowfullscreen></iframe>
        </div>

        <div class="container mt-5">

            <div class="info-wrap">
                <div class="row">
                    <div class="col-lg-3 col-md-6 info">
                        <i class="bi bi-geo-alt"></i>
                        <h4 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Location:</h4>
                        <p>University Ave<br>Glasgow G12 8QQ</p>
                    </div>

                    <div class="col-lg-3 col-md-6 info mt-4 mt-lg-0">
                        <i class="bi bi-clock"></i>
                        <h4 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Open Hours:</h4>
                        <p>Monday-Saturday:<br>11:00 AM - 2300 PM</p>
                    </div>

                    <div class="col-lg-3 col-md-6 info mt-4 mt-lg-0">
                        <i class="bi bi-envelope"></i>
                        <h4 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Email:</h4>
                        <p>info@example.com<br>contact@example.com</p>
                    </div>

                    <div class="col-lg-3 col-md-6 info mt-4 mt-lg-0">
                        <i class="bi bi-phone"></i>
                        <h4 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Call:</h4>
                        <p>+1 5589 55488 51<br>+1 5589 22475 14</p>
                    </div>
                </div>
            </div>

            <form action="forms/contact.php" method="post" role="form" class="php-email-form">
                <div class="row">
                    <div class="col-md-6 form-group">
                        <input type="text" name="name" class="form-control" id="name" placeholder="Your Name" required>
                    </div>
                    <div class="col-md-6 form-group mt-3 mt-md-0">
                        <input type="email" class="form-control" name="email" id="email" placeholder="Your Email" required>
                    </div>
                </div>
                <div class="form-group mt-3">
                    <input type="text" class="form-control" name="subject" id="subject" placeholder="Subject" required>
                </div>
                <div class="form-group mt-3">
                    <textarea class="form-control" name="message" rows="5" placeholder="Message" required></textarea>
                </div>
                <div class="my-3">
                    <div class="loading">Loading</div>
                    <div class="error-message"></div>
                    <div class="sent-message">Your message has been sent. Thank you!</div>
                </div>
                <div class="text-center"><button type="submit">Send Message</button></div>
            </form>

        </div>
    </section><!-- End Contact Section -->
</template>

<script>
export default {
    name: 'Contactus',
}
</script>

<style scoped>
</style>
