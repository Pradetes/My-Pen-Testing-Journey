document.addEventListener('DOMContentLoaded', () => {
    const triggers = document.querySelectorAll('.lightbox-trigger');
    
    // Crear el lightbox en el DOM
    const lightbox = document.createElement('div');
    lightbox.classList.add('lightbox');
    document.body.appendChild(lightbox);

    triggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.preventDefault(); // Evita que el enlace salte
            const imgSrc = trigger.querySelector('img').src; // Obtiene la URL de la imagen
            
            // Crea y muestra el contenido del lightbox
            lightbox.innerHTML = `<img src="${imgSrc}" alt="${trigger.querySelector('img').alt}">`;
            lightbox.style.display = 'flex'; // Muestra el lightbox
        });
    });

    // Cerrar el lightbox al hacer clic en él
    lightbox.addEventListener('click', (e) => {
        if (e.target.tagName !== 'IMG') { // Solo si no se hace clic en la imagen
            lightbox.style.display = 'none'; // Oculta el lightbox
        }
    });

    // Cerrar el lightbox al presionar la tecla "Escape"
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightbox.style.display === 'flex') {
            lightbox.style.display = 'none';
        }
    });
});