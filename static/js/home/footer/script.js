document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");

    const reveal = () => {
        sections.forEach((section) => {
            const sectionTop = section.getBoundingClientRect().top;
            const triggerBottom = window.innerHeight * 0.85;

            if (sectionTop < triggerBottom) {
                section.classList.add("fade-in");
                section.classList.remove("hidden");
            } else {
                section.classList.remove("fade-in");
                section.classList.add("hidden");
            }
        });
    };

    window.addEventListener("scroll", reveal);

    // Initial check
    reveal();
});
ransform: translateY(0);

