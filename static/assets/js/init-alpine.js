(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem("dashboard-theme");
  if (saved === "dark") root.classList.add("dark");

  document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("themeButton");
    if (!button) return;
    button.addEventListener("click", function () {
      root.classList.toggle("dark");
      localStorage.setItem(
        "dashboard-theme",
        root.classList.contains("dark") ? "dark" : "light"
      );
    });
  });
})();
