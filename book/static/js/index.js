document.addEventListener("DOMContentLoaded", function () {
  const bdModeToggle = document.querySelector(".bd-mode-toggle");
  const themeButtons = document.querySelectorAll(
    '.bd-mode-toggle .dropdown-item:not([data-bs-theme-value="auto"])'
  );

  // Function to set the theme
  const setTheme = (theme) => {
    document.documentElement.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);
  };

  // Function to handle theme button click
  const handleThemeButtonClick = (button) => {
    themeButtons.forEach((btn) => {
      btn.classList.remove("active");
      btn.setAttribute("aria-pressed", "false");
      btn.querySelector(".bi-check").style.display = "none";
    });

    button.classList.add("active");
    button.setAttribute("aria-pressed", "true");
    button.querySelector(".bi-check").style.display = "inline-block";

    const selectedTheme = button.getAttribute("data-bs-theme-value");
    setTheme(selectedTheme);
  };

  // Event listeners for theme buttons
  themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      handleThemeButtonClick(button);
    });
  });

  // Check local storage for theme preference
  const storedTheme = localStorage.getItem("theme");
  if (storedTheme) {
    setTheme(storedTheme);
    const activeButton = document.querySelector(
      `[data-bs-theme-value="${storedTheme}"]:not([data-bs-theme-value="auto"])`
    );
    if (activeButton) {
      handleThemeButtonClick(activeButton);
    }
  }
});

(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach((e) => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Book isotope and filter
   */
  window.addEventListener("load", () => {
    let bookContainer = select(".book-container");
    if (bookContainer) {
      let bookIsotope = new Isotope(bookContainer, {
        itemSelector: ".book-item",
      });

      let bookFilters = select("#book-flters li", true);

      on(
        "click",
        "#book-flters li",
        function (e) {
          e.preventDefault();
          bookFilters.forEach(function (el) {
            el.classList.remove("filter-active");
          });
          this.classList.add("filter-active");

          bookIsotope.arrange({
            filter: this.getAttribute("data-filter"),
          });
          // bookIsotope.on("arrangeComplete", function () {
          //   AOS.refresh();
          // });
        },
        true
      );
    }
  });


  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl, {
                customClass: function (tooltip) {
                    return 'custom-tooltip'; // Add your custom tooltip class
                }
            });
        });
})();
