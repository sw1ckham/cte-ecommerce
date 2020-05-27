// Code taken from https://developpaper.com/django-builds-personal-blogs-back-to-the-top-floating-buttons-vector-icons-footer-sinks-and-sticky-sidebars/

$(document).ready(function(){
    $(function () {
        $('#BackTop').click(function () {
            $('html,body').animate({scrollTop: 0}, 500);
        });
        // $(window).scroll(function () {
        //     if ($(this).scrollTop() > 300) {
        //         $('#BackTop').fadeIn(300);
        //     } else {
        //         $('#BackTop').stop().fadeOut(300);
        //     }
        // }).scroll();
    });
})