$(document).ready(function(){
    
    
    $(".toggle-show-button").click(function() {
        $(this).next(".toggle-description").toggleClass("toggle-description-show");
    });

    $('.toggle-hide-icon').click(function(){
        $(this).next(".toggle-description-show").hide();
    });

    // $('#myModal').on('shown.bs.modal', function () {
    // $('#myInput').trigger('focus')
    // });

    // console.log('load')
    // var t = document.getElementById("myModal"),
    // c = ($(".myImg"), $("#img01"));
    // $(".myImg").click(function () {
    //     console.log(this);
    //     t.style.display = "block";
    //     var e = this.src;
    //     console.log(this.src);
    //     c.attr("MEDIA_URL", e);
        
    // }),

    // (document.getElementsByClassName("close")[0].click = function () {
    //     t.style.display = "none";
    // });

});