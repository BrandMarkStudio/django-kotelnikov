// parallax.js
$(document).ready(function() {
    var scrolled = 0;
    var yPosition;
    
    // все иконки для параллакса
    var $parallaxElements = $('.icons-for-parallax img');
    
    // логотип для параллакса
    var $logo = $('.logo-container');

    // при скролле
    $(window).scroll(function() {
        // сколько пикселей проскроллено
        scrolled = $(window).scrollTop();

        // параллакс для иконок
        for (var i = 0; i < $parallaxElements.length; i++) {
            yPosition = scrolled * 0.15 * (i + 1); // разные скорости
            $parallaxElements.eq(i).css({ top: yPosition });
        }

        // параллакс для логотипа
        // выбрана скорость 0.05, чтобы движение было плавным и небольшим
        var logoPosition = scrolled * 0.5;
        $logo.css({ top: logoPosition });
    });
});