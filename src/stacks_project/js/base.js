$(document).ready(function () {

    $('.nav-button-tog').click(function () {
        $('.nav-button-tog').toggleClass('change')
    });

    // $(window).scroll(function () {
    //     let position = $(this).scrollTop();
    //     console.log(position)
    // });

    //Toggling between login and register forms
    let loginDiv = $('.log');
    let registerDiv = $('.reg');
    registerDiv.hide();
    $('.toggler-button').on('click', function () {
        $( loginDiv, registerDiv ).toggle();
    });
    // End Of toggling

});