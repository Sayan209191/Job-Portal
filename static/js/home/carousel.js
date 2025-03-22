let slideIndex = 0;
function moveSlide(direction) {
    const container = document.querySelector(".internship-container");
    const cards = document.querySelectorAll(".internship-card");
    const cardWidth = cards[0].offsetWidth + 20;
    slideIndex += direction;
    if (slideIndex < 0) slideIndex = 0;
    if (slideIndex > cards.length - 2) slideIndex = cards.length - 2;
    container.style.transform = `translateX(-${slideIndex * cardWidth}px)`;
}


let slideIndex2 = 0;
function moveSlideJob(direction) {
    const container = document.querySelector(".job-container"); // Corrected selector
    const cards = document.querySelectorAll(".job-card");
    const cardWidth = cards[0].offsetWidth + 20;
    slideIndex2 += direction;
    if (slideIndex2 < 0) slideIndex2 = 0;
    if (slideIndex2 > cards.length - 2) slideIndex2 = cards.length - 2;
    container.style.transform = `translateX(-${slideIndex2 * cardWidth}px)`;
}
