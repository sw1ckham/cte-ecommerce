$(document).ready(function(){
    $('.toggle-description').hide();

    $(".toggle-button").click(function() {
    $(this).next(".toggle-description").slideToggle("show");
    });

    var t = document.getElementById("myModal"),
    c = ($(".myImg"), $("#img01"));
    $(".myImg").click(function () {
        t.style.display = "block";
        var e = this.src;
        c.attr("MEDIA_URL", e);
    }),
    (document.getElementsByClassName("close")[0].click = function () {
        t.style.display = "none";
    });


    // var onResize = function() {
// apply dynamic padding at the top of the body according to the fixed navbar height
    // $("body").css("padding-top", $(".navbar-fixed-top").height());
    // };
// attach the function to the window resize event
    // $(window).resize(onResize);
// call it also when the page is ready after load or reload
    // $(function() {
    //     onResize();
    // });

    // $(window).resize(function () { 
    // $('body').css('padding-top', parseInt($('#main-navbar').css("height"))+10);
    // });

    // $(window).load(function () { 
    // $('body').css('padding-top', parseInt($('#main-navbar').css("height"))+10);         
    // }); 


})