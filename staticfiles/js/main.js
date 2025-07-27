document.addEventListener("DOMContentLoaded", () => {
  // 1. Animación fade-in escalonada
  const cards = document.querySelectorAll(".card");
  cards.forEach((card, index) => {
    setTimeout(() => {
      card.classList.add("visible");
    }, index * 100);
  });

  // 2. Mostrar detalles ocultos al pasar el mouse
  // (CSS lo activa automáticamente con :hover sobre .card y .detalle)

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

  // 6. Carrusel automático en la página de inicio
  const carruselImagenes = document.querySelectorAll(".imagen-carrusel");
  let indexActual = 0;
  const intervalo = 5000; // 4 segundos entre imágenes

  if (carruselImagenes.length > 0) {
    setInterval(() => {
      carruselImagenes[indexActual].classList.remove("active");
      indexActual = (indexActual + 1) % carruselImagenes.length;
      carruselImagenes[indexActual].classList.add("active");
    }, intervalo);
  }
});
