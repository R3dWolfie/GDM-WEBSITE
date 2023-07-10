document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.classList.add('hover');
    });
    card.addEventListener('mouseleave', () => {
      card.classList.remove('hover');
    });
  });
});
