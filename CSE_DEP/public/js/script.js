const buttons = document.querySelectorAll(".accordion-btn");

buttons.forEach(btn => {
    btn.addEventListener("click", function() {
        const content = this.nextElementSibling;
        content.style.display =
            content.style.display === "block" ? "none" : "block";
    });
});

const programItems = document.querySelectorAll(".program-item");

programItems.forEach(item => {
    const header = item.querySelector(".program-header");

    header.addEventListener("click", () => {

        programItems.forEach(otherItem => {
            if (otherItem !== item) {
                otherItem.classList.remove("active");
            }
        });

        item.classList.toggle("active");
    });
});