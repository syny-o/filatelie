/*-----------------------------------------------------------------------------------

    Template Name:Edgy - classified - car rental, real estate,job find 
    Template URI: https://themes.pixelstrap.net/Edgy
    Description: This is classified Html Template
    Author: Pixelstrap
    Author URL: https://themeforest.net/user/pixelstrap

----------------------------------------------------------------------------------- */

// 01.landing swiper js
// 02.sticky header js
// 03.nav link active header js
// 04.tap to top js
// 05.AOS animation

/*====================
  02.  sticky header js
=======================*/
const header = document.querySelector("header");
const toggleClass = "sticky";

window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 150) {
        header.classList.add(toggleClass);
    } else {
        header.classList.remove(toggleClass);
    }
});

/*====================
  03. nav link active header js
=======================*/
window.addEventListener("scroll", function () {
    const navHeader = document.getElementById("header");
    const sections = document.querySelectorAll("section");

    let current = "";

    sections.forEach((section) => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - sectionHeight / 3) {
            current = section.getAttribute("id");
        }
    });

    const activeLink = document.querySelector(".active-link");
    if (activeLink) {
        activeLink.classList.remove("active-link");
    }
    const newActiveLink = document.querySelector('a[href="#' + current + '"]');
    if (newActiveLink) {
        newActiveLink.classList.add("active-link");
    }
});

/*====================
  04.  tap to top js
=======================*/
const scrollBtn = document.querySelector(".tap-to-tap");
const btnCss = () => {
    if (window.scrollY > 250) {
        scrollBtn.classList.add("show");
    } else {
        scrollBtn.classList.remove("show");
    }
};
document.addEventListener("scroll", () => {
    btnCss();
});
scrollBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth",
    });
});

/*====================
  05. AOS animation js
=======================*/
AOS.init({
    once: true,
});