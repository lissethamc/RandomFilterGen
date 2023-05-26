function showFileName() {
    const fileInput = document.getElementById("image");
    const fileNameLabel = document.querySelector(".custom-file-label");
    const fileNameSpan = document.getElementById("file-name");
  
    if (fileInput.files.length > 0) {
      const fileName = fileInput.files[0].name;
      fileNameLabel.innerHTML = `<img id="loadImg" src="static/loadImg.png" alt="loadImg"><br>Imagen: ${fileName}`;
      fileNameSpan.innerText = fileName;
      fileNameSpan.classList.remove("hide");
      fileNameSpan.classList.add("animated", "show");
    } else {
      fileNameLabel.innerHTML = `<img id="loadImg" src="static/loadImg.png" alt="loadImg"><br>`;
      fileNameSpan.classList.remove("show");
      fileNameSpan.classList.add("animated", "hide");
    }
  }
  