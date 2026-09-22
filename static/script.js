console.log("work js");
const title = document.querySelector(".title");
const themeBlack = document.querySelector(".btn-color_themes.black");
const themeWhite = document.querySelector(".btn-color_themes.white");

const body = document.querySelector("body");

themeBlack.addEventListener("click", () => {
  body.classList.add("black");
});
themeWhite.addEventListener("click", () => {
  body.classList.remove("black");
});

function splitAndAddClass() {
  const text = title.textContent;
  title.innerHTML = text
    .split("")
    .map((letter) => `<span class="letter">${letter}</span>`)
    .join("");

  document.querySelectorAll(".letter").forEach((el, index) => {
    el.setAttribute(
      "style",
      `z-index: -${index}; animation-delay: ${index / text.length + 1}s`,
    );
  });
}

splitAndAddClass();
// --------form
const openFormButton = document.querySelector("#open-form");
const formBox = document.querySelector(".form-box");

openFormButton.addEventListener("click", () => {
  formBox.classList.toggle("active");
});
