$(document).ready(function() {
    // Эффект затемнения при наведении на заголовок
    $('.post-title').hover(
        function(event) { // Навели курсор
            $(event.currentTarget).closest('.one-post')
                .find('.one-post-shadow').stop().animate({opacity: 0.1}, 300);
        },
        function(event) { // Убрали курсор
            $(event.currentTarget).closest('.one-post')
                .find('.one-post-shadow').stop().animate({opacity: 0}, 300);
        }
    );

    // Существующий hover на весь пост
    $('.one-post').hover(
        function(event) {
            $(event.currentTarget).find('.one-post-shadow').stop().animate({opacity: 0.1}, 300);
        },
        function(event) {
            $(event.currentTarget).find('.one-post-shadow').stop().animate({opacity: 0}, 300);
        }
    );
});