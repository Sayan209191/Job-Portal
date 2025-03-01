function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function applyRandomColors() {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.background = getRandomColor();
    });
}

function changeColorOnApply() {
    const card = document.querySelector('.card');
    card.style.background = getRandomColor();
}

// Apply random colors when the page loads
window.onload = applyRandomColors;
