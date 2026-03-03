const buttons = document.querySelectorAll(".accordion-btn");

buttons.forEach(btn => {
    btn.addEventListener("click", function() {
        const content = this.nextElementSibling;
        content.style.display =
            content.style.display === "block" ? "none" : "block";
    });
});