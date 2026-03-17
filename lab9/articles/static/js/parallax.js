$(document).ready(function() {
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.logo');

    var logoInitialTop = $logo.position().top;
    var initialPositions = [];
    $parallaxElements.each(function() {
        initialPositions.push($(this).position().top);
    });

    $(window).scroll(function() {
        var scrolled = $(window).scrollTop();

        // иконки
        $parallaxElements.each(function(i) {
            var yPosition = initialPositions[i] + scrolled * 0.15 * (i + 1);
            $(this).css({ top: yPosition });
        });

        // логотип
        var logoPosition = logoInitialTop + scrolled * 0.15; // та же скорость, что у первой иконки
        $logo.css({ top: logoPosition });
    });
});