var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.parentElement; // родитель .one-post
        post.classList.toggle("folded");   // переключаем класс folded

        // Меняем текст кнопки
        e.target.innerHTML = post.classList.contains("folded") ? "развернуть" : "свернуть";
    });
}