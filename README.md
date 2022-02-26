# Project-Flask

Start making user environment.

<!-- <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="">
        <p>Homepage</p>
        <input type="text" id="nome" name="nome" placeholder="Nome:" autocomplete="on">
        <br>
        <p></p>
        <input type="button" value="Enviar" onclick="teste()">
    </form>
</body>


</html> -->
<!-- <script>
    function teste() {

        var name = document.getElementById("nome").value;

        var mensagem = "";
        if (name == "") {
            mensagem =
                mensagem +
                "\n Para prosseguir preencha todos os campos abaixo: \n Nome \n";
        }

        if (mensagem != "") {
            alert(mensagem);
        } else {
            alert("Cadastrado com Sucesso!!");
            var input = document.getElementById("nome");
            var texto = input.value;

            window.location.href = ('/users/' + texto)
        }


    }
</script> -->

    <!-- ==================== MAIN ====================
    <main class="main">
        <!--==================== PORTFOLIO ====================-->
        <section class="portfolio section" id="portfolio">
            <h2 class="section__title">Portfolio</h2>
            <span class="section__subtitle">Most Recent Work</span>

            <div class="portfolio__container container swiper-container">
                <div class="swiper-wrapper">
                    <!--==================== PORTFOLIO 1====================-->
                    <div class="portfolio__content grid swiper-slide">
                        <img src="{{ url_for('static', filename='img/portfolio1.jpg')}}" alt="" class="portfolio__img">

                        <div class="portfolio__data">
                            <h3 class="portfolio__title">Modern Website</h3>
                            <p class="portfolio__description">Website adaptable to all devices, with ui components and
                                animated interactions.</p>
                            <a href="#" class="button button--flex button--small portfolio__button">
                                Demo
                                <i class="uil uil-arrow-right button__icon"></i>
                            </a>
                        </div>
                    </div>

                    <!--==================== PORTFOLIO 2====================-->
                    <div class="portfolio__content grid swiper-slide">
                        <img src="{{ url_for('static', filename='img/portfolio2.jpg')}}" alt="" class="portfolio__img">

                        <div class="portfolio__data">
                            <h3 class="portfolio__title">Brand Designer</h3>
                            <p class="portfolio__description">Website adaptable to all devices, with ui components and
                                animated interactions.</p>
                            <a href="#" class="button button--flex button--small portfolio__button">
                                Demo
                                <i class="uil uil-arrow-right button__icon"></i>
                            </a>
                        </div>
                    </div>

                    <!--==================== PORTFOLIO 3====================-->
                    <div class="portfolio__content grid swiper-slide">
                        <img src="{{ url_for('static', filename='img/portfolio3.jpg')}}" alt="" class="portfolio__img">

                        <div class="portfolio__data">
                            <h3 class="portfolio__title">Online Store</h3>
                            <p class="portfolio__description">Website adaptable to all devices, with ui components and
                                animated interactions.</p>
                            <a href="#" class="button button--flex button--small portfolio__button">
                                Demo
                                <i class="uil uil-arrow-right button__icon"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Add Arrows -->
                <div class="swiper-button-next">
                    <i class="uil uil-angle-right-b swiper-portfolio-icon"></i>
                </div>

                <div class="swiper-button-prev">
                    <i class="uil uil-angle-left-b swiper-portfolio-icon"></i>
                </div>

                <!-- Add Pagination -->
                <div class="swiper-pagination"></div>
            </div>

            <section class="testimonial section">
                <!--==================== TESTIMONIAL ====================-->
                <h2 class="section__title">Testimonial</h2>
                <span class="section__subtitle">My Client Saying</span>

                <div class="testimonial__container container swiper-container">
                    <div class="swiper-wrapper">
                        <!--==================== TESTIMONIAL 1====================-->
                        <div class="testimonial__content swiper-slide">
                            <div class="testimonial__data">
                                <div class="testimonial__header">
                                    <img src="{{ url_for('static', filename='img/testimonial1.jpg')}}" alt=""
                                        class="testimonial__img">

                                    <div>
                                        <h3 class="testimonial__name">Sara Smith</h3>
                                        <span class="testimonial__client">Client</span>
                                    </div>
                                </div>
                                <div>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                </div>
                            </div>

                            <p class="testimonial__description">I get a good impression, I carry out my project with all
                                the
                                possible quality and attention and support 24 hours a day.</p>
                        </div>

                        <!--==================== TESTIMONIAL 2====================-->
                        <div class="testimonial__content swiper-slide">
                            <div class="testimonial__data">
                                <div class="testimonial__header">
                                    <img src="{{ url_for('static', filename='img/testimonial2.jpg')}}" alt=""
                                        class="testimonial__img">

                                    <div>
                                        <h3 class="testimonial__name">Matt Smith</h3>
                                        <span class="testimonial__client">Client</span>
                                    </div>
                                </div>

                                <div>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                </div>
                            </div>

                            <p class="testimonial__description">I get a good impression, I carry out my project with all
                                the
                                possible quality and attention and support 24 hours a day.</p>
                        </div>

                        <!--==================== TESTIMONIAL 3====================-->
                        <div class="testimonial__content swiper-slide">
                            <div class="testimonial__data">
                                <div class="testimonial__header">
                                    <img src="{{ url_for('static', filename='img/testimonial3.jpg')}}" alt=""
                                        class="testimonial__img">

                                    <div>
                                        <h3 class="testimonial__name">Raul Smith</h3>
                                        <span class="testimonial__client">Client</span>
                                    </div>
                                </div>

                                <div>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                    <i class="uil uil-star testimonial__icon-star"></i>
                                </div>
                            </div>
                            <p class="testimonial__description">I get a good impression, I carry out my project with all
                                the
                                possible quality and attention and support 24 hours a day.</p>
                        </div>
                    </div>

                    <!-- Add Pagination -->
                    <div class="swiper-pagination swiper-pagination-testimonial"></div>
                </div>
            </section>
        </section>
    </main> -->
