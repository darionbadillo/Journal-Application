// This page activates/deactivates dark mode for the website

const darkModeToggle = document.getElementById('darkModeToggle');

//Stores the user choice throughout the sessions
// NOTE: This is a temporary implementation. In the future, I will use a database to store user preferences
let darkMode = localStorage.getItem('darkMode') === 'enabled';

// Constantly ensures that dark mode is enabled/disabled
if (darkMode) {
    document.body.classList.add('bg-dark', 'text-light');
}

// Toggle the darkMode flag
darkModeToggle.addEventListener('click', function() {
    const body = document.body;

    if (darkMode) {
        body.classList.remove('bg-dark', 'text-light');
        localStorage.setItem('darkMode', 'disabled');
    } else {
        body.classList.add('bg-dark', 'text-light');
        localStorage.setItem('darkMode', 'enabled');
    }

    // Toggle the darkMode flag
    darkMode = !darkMode;
})