function showFileName() {
    const fileInput = document.getElementById("image");
    const fileNameLabel = document.querySelector(".custom-file-label");
    const fileNameSpan = document.getElementById("file-name");
  
    if (fileInput.files.length > 0) {
      const fileName = fileInput.files[0].name;
      fileNameLabel.innerHTML = `Imagen: ${fileName}<br><br><img id="loadedIMG" src="/static/uploads/${fileName}" alt="ups, problema al cargar la imagen. Solo continua :)" style=" max-height:170px; max-width: 320px; border: solid #00536e 1px;">`;
      fileNameSpan.innerText = fileName;
      fileNameSpan.classList.remove("hide");
      fileNameSpan.classList.add("animated", "show");
    } else {
      fileNameLabel.innerHTML = `<img id="loadImg" src="/static/loadImg.png" alt="loadImg"><br>`;
      fileNameSpan.classList.remove("show");
      fileNameSpan.classList.add("animated", "hide");
    }
  }
  

  function showSpinner() {
    const spinner = document.getElementById('spinner');
    spinner.classList.remove('hidden');
}

function hideSpinner() {
    const spinner = document.getElementById('spinner');
    spinner.classList.add('hidden');
}

// JavaScript para controlar la visibilidad del spinner y la imagen
window.addEventListener('DOMContentLoaded', (event) => {
    const spinner = document.getElementById('spinner');
    const form = document.querySelector('.upload-form');
    const previewImage = document.getElementById('preview-image');

    // Ocultar el spinner al cargar la página
    hideSpinner();

    // Mostrar el spinner al enviar el formulario
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Evitar el envío del formulario
        showSpinner();

        // Simular un retraso para mostrar el spinner
        setTimeout(() => {
            form.submit(); // Enviar el formulario después de mostrar el spinner
        }, 100);
    });

    // Ocultar el spinner cuando la imagen se cargue
    previewImage.addEventListener('load', () => {
        hideSpinner();
    });
});