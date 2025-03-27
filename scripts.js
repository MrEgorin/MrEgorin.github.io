document.addEventListener('DOMContentLoaded', () => {
    // Burger menu functionality
    const burgerMenu = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');

    burgerMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Highlight the active navigation link
    const currentPage = window.location.pathname.split('/').pop();
    const navLinksItems = document.querySelectorAll('.nav-links a');
    navLinksItems.forEach(link => {
        if (link.getAttribute('data-page') === currentPage) {
            link.classList.add('active');
        }
    });

    // Handle navigation transitions with JavaScript
    const pageLinks = document.querySelectorAll('[data-page]');
    pageLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const page = link.getAttribute('data-page');
            // Add a fade-out effect before navigating
            document.body.style.opacity = '0';
            setTimeout(() => {
                window.location.href = page;
            }, 300); // Match the transition duration in CSS
        });
    });

    // Fade-in effect on page load
    document.body.style.opacity = '1';
});
