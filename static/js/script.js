// Rainbow wave effect for download buttons
const buttons = document.querySelectorAll('.btn-primary');

buttons.forEach(button => {
  button.addEventListener('animationiteration', () => {
    button.classList.remove('rainbow');
    void button.offsetWidth; // Trigger reflow for smooth animation restart
    button.classList.add('rainbow');
  });
});

// Add star-shaped sparkle effect to the cards
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  for (let i = 0; i < 5; i++) {
    const sparkle = document.createElement('span');
    sparkle.classList.add('star-sparkle');
    sparkle.style.top = `${getRandomPosition(card.offsetHeight)}px`;
    sparkle.style.left = `${getRandomPosition(card.offsetWidth)}px`;
    sparkle.style.animationDelay = `${getRandomDelay()}s`;
    card.appendChild(sparkle);
  }
});

// Flowing rainbow effect for card titles
const cardTitles = document.querySelectorAll('.card-title');

cardTitles.forEach(title => {
  const letters = title.textContent.split('');
  const spannedLetters = letters.map(letter => `<span>${letter}</span>`);
  title.innerHTML = spannedLetters.join('');
  const spanElements = title.querySelectorAll('span');

  spanElements.forEach((span, index) => {
    span.style.animationDelay = `${index * 0.1}s`;
    span.classList.add('rainbow-text');
  });
});

function getRandomPosition(max) {
  return Math.floor(Math.random() * max);
}

function getRandomDelay() {
  return Math.random() * 0.5 + 0.2; // Random delay between 0.2s and 0.7s
}

function createStarSparkle() {
  const sparkle = document.createElement('span');
  sparkle.classList.add('star-sparkle');
  sparkle.style.top = `${getRandomPosition(window.innerHeight)}px`;
  sparkle.style.left = `${getRandomPosition(window.innerWidth)}px`;
  sparkle.style.animationDelay = `${getRandomDelay()}s`;
  document.body.appendChild(sparkle);

  setTimeout(() => {
    sparkle.remove();
  }, 3000);
}

setInterval(createStarSparkle, 1000);
