$(document).ready(function(){
    
    $(".toggle-show-button").click(function() {
        $(this).next(".toggle-description").toggleClass("toggle-description-show");
    });

    $('.toggle-hide-icon').click(function(){
        $(this).next(".toggle-description-show").hide();
    });

});