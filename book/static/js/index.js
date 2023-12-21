document.addEventListener('DOMContentLoaded', function () {
    const bdModeToggle = document.querySelector('.bd-mode-toggle');
    const themeButtons = document.querySelectorAll('.bd-mode-toggle .dropdown-item:not([data-bs-theme-value="auto"])');

    // Function to set the theme
    const setTheme = (theme) => {
        document.documentElement.setAttribute('data-bs-theme', theme);
        localStorage.setItem('theme', theme);
    };

    // Function to handle theme button click
    const handleThemeButtonClick = (button) => {
        themeButtons.forEach((btn) => {
            btn.classList.remove('active');
            btn.setAttribute('aria-pressed', 'false');
            btn.querySelector('.bi-check').style.display = 'none';
        });

        button.classList.add('active');
        button.setAttribute('aria-pressed', 'true');
        button.querySelector('.bi-check').style.display = 'inline-block';

        const selectedTheme = button.getAttribute('data-bs-theme-value');
        setTheme(selectedTheme);
    };

    // Event listeners for theme buttons
    themeButtons.forEach((button) => {
        button.addEventListener('click', () => {
            handleThemeButtonClick(button);
        });
    });

    // Check local storage for theme preference
    const storedTheme = localStorage.getItem('theme');
    if (storedTheme) {
        setTheme(storedTheme);
        const activeButton = document.querySelector(`[data-bs-theme-value="${storedTheme}"]:not([data-bs-theme-value="auto"])`);
        if (activeButton) {
            handleThemeButtonClick(activeButton);
        }
    }
});