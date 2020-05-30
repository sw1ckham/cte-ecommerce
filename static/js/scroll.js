// Code taken from https://developpaper.com/django-builds-personal-blogs-back-to-the-top-floating-buttons-vector-icons-footer-sinks-and-sticky-sidebars/

$(document).ready(function(){
   
        $(window).scroll(function () {
            if ($(this).scrollTop() > 200) {
                $('#BackTop').css('display', 'block');
            } else {
                $('#BackTop').css('display', 'none');
            }
        });
        
            $('#BackTop').click(function () {
            $('html,body').animate({scrollTop: 0}, 500);
            return false;
        });

});