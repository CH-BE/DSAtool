document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('theme-toggle');
  const root = document.documentElement;
  const current = localStorage.getItem('theme') || 'light';
  root.setAttribute('data-theme', current);

  toggle.addEventListener('click', () => {
    const newTheme = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });
});