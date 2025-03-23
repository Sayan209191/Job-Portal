document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded ✅");

    const buttons = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll(".content-section");

    // Ensure only the "about" section is visible initially
    sections.forEach((section) => {
        if (!section.classList.contains("active")) {
            section.style.display = "none";
        }
    });

    buttons.forEach((button) => {
        button.addEventListener("click", function () {
            const sectionId = this.getAttribute("data-section");
            console.log("Clicked:", sectionId);

            // Remove active class from all buttons
            buttons.forEach((btn) => btn.classList.remove("active"));
            this.classList.add("active"); // Highlight clicked button

            // Hide all sections
            sections.forEach((section) => {
                section.style.display = "none";
                section.classList.remove("active");
            });

            // Show the selected section
            const targetSection = document.getElementById(sectionId);
            if (targetSection) {
                targetSection.style.display = "block";
                targetSection.classList.add("active");
                console.log("Now Showing:", sectionId);
            } else {
                console.log("Error: Section not found!");
            }
        });
    });
});
