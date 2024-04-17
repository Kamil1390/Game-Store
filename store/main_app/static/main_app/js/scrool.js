window.addEventListener('scroll', function() {
  var block = document.querySelector('.fixed-block');
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  var maxTop = 10; // Максимальное смещение блока с верху страницы
  var minTop = 50; // Минимальное смещение блока с верху страницы
  var newTop = scrollTop < minTop ? minTop : (scrollTop > maxTop ? maxTop : scrollTop); // Ограничиваем смещение блока
  block.style.top = newTop + 'px';
});

