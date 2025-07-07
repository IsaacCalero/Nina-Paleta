document.addEventListener("DOMContentLoaded", () => {
  // 1. Animación fade-in escalonada
  const cards = document.querySelectorAll(".card");
  cards.forEach((card, index) => {
    setTimeout(() => {
      card.classList.add("visible");
    }, index * 100);
  });

  // 2. Mostrar detalles ocultos al pasar el mouse (CSS lo activa)
  // Solo requiere que tengas <p class="detalle">...</p> en cada .card

  // 3. Botón para filtrar productos especiales
  const filtroBtn = document.getElementById("filtrar-especiales");
  if (filtroBtn) {
    filtroBtn.addEventListener("click", () => {
      cards.forEach(card => {
        const esEspecial = card.querySelector(".etiqueta-especial");
        card.style.display = esEspecial ? "block" : "none";
      });
    });
  }

  // 4. Contador de productos disponibles
  const contador = document.getElementById("contador-disponibles");
  if (contador) {
    let disponibles = 0;
    cards.forEach(card => {
      if (!card.classList.contains("no-disponible")) {
        disponibles++;
      }
    });
    contador.textContent = `🍭 Hay ${disponibles} productos disponibles`;
  }

  // 5. Alertas para productos de mascota
  const mascotaCards = document.querySelectorAll(".mascopaletas .card");
  mascotaCards.forEach(card => {
    card.addEventListener("click", () => {
      alert("¿Segur@ que tu perrito aprueba este sabor? 🐶💖");
    });
  });
});
