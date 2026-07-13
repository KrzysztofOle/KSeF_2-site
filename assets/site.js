const root = document.documentElement;
const savedTheme = localStorage.getItem("ksef-theme");
if (savedTheme) root.dataset.theme = savedTheme;

const themeButton = document.querySelector("[data-theme-toggle]");
const setThemeLabel = () => {
  if (!themeButton) return;
  const light = root.dataset.theme === "light";
  themeButton.textContent = light ? "◐" : "☼";
  themeButton.setAttribute("aria-label", light ? "Use dark theme" : "Use light theme");
};
setThemeLabel();

themeButton?.addEventListener("click", () => {
  root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";
  localStorage.setItem("ksef-theme", root.dataset.theme);
  setThemeLabel();
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
document.querySelector("[data-year]").textContent = new Date().getFullYear();
