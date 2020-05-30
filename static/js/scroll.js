// Code taken from https://developpaper.com/django-builds-personal-blogs-back-to-the-top-floating-buttons-vector-icons-footer-sinks-and-sticky-sidebars/

$(document).ready(function(){
   
        $(window).scroll(function () {
            if ($(this).scrollTop() > 200) {
                $('#BackTop').css('display', 'block')
            } else {
                $('#BackTop').css('display', 'none')
            }
        });


        // mybutton = document.getElementById("BackTop");

        // // When the user scrolls down 20px from the top of the document, show the button
        // window.onscroll = function() {scrollFunction()};

        // function scrollFunction() {
        // if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        //     mybutton.style.display = "block";
        // } else {
        //     mybutton.style.display = "none";
        // }
        // }
        
            $('#BackTop').click(function () {
            $('html,body').animate({scrollTop: 0}, 500);
            return false;
        });

});