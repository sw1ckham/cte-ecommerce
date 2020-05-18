$(document).ready(function(){
    $('.toggle-description').hide();

    $(".toggle-button").click(function() {
    $(".toggle-description").toggle("show");
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


})