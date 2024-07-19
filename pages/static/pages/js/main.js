document.addEventListener('DOMContentLoaded', function () {
    var dropdownToggle = document.querySelector('.dropdown-toggle');
    var dropdownMenu = document.querySelector('.dropdown-menu');
    var menuToggle = document.querySelector('.menu-toggle');
    var mainMenu = document.querySelector('.main-menu');
    var mainNav = document.querySelector('.main-nav');

    // Mostrar/Ocultar o menu dropdown
    dropdownToggle.addEventListener('click', function (event) {
        event.preventDefault();
        dropdownMenu.classList.toggle('show');
    });

    // Mostrar/Ocultar o menu principal em dispositivos móveis
    menuToggle.addEventListener('click', function () {
        mainNav.classList.toggle('show');
    });

    // Fechar o dropdown se clicar fora
    document.addEventListener('click', function (event) {
        if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove('show');
        }
    });
});
