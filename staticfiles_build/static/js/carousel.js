document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll(".carousel img");
    let currentIndex = 0;

    function showImage(index) {
        images.forEach(img => img.classList.remove("active"));
        images[index].classList.add("active");
    }

    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }

    function prevImage() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        showImage(currentIndex);
    }

    const nextButton = document.querySelector(".next-button");
    nextButton.addEventListener("click", function () {
        nextImage();
    });

    const prevButton = document.querySelector(".prev-button");
    prevButton.addEventListener("click", function () {
        prevImage();
    });

    setInterval(nextImage, 4000); // Change image every 4 seconds

// Get the dark mode toggle element
    const toggleButton = document.querySelector(".toggle-dark-mode");
    toggleButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
    });

    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('contracted');
    } else {
        header.classList.remove('contracted');
    }
    });


});