// fold-post.js
$(document).ready(function() {
    $('.fold-button').click(function() {
        const post = $(this).closest('.one-post');
        post.toggleClass('folded');

        // Меняем текст кнопки
        if (post.hasClass('folded')) {
            $(this).text('развернуть');
        } else {
            $(this).text('свернуть');
        }
    });
});