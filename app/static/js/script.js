const textArea = document.getElementById("text");
const fileInput = document.getElementById("file");
const fileName = document.getElementById("file-name");
const removeFileBtn = document.getElementById("remove-file");
const responseBox = document.getElementById("response");

textArea.addEventListener("input", () => {
  fileInput.disabled = textArea.value.trim().length > 0;
});

fileInput.addEventListener("change", () => {
  if (fileInput.files.length > 0) {
    fileName.textContent = fileInput.files[0].name;
    removeFileBtn.style.display = "inline-block";
    textArea.disabled = true; // mantém a lógica de exclusividade
  } else {
    resetFileInput();
  }
});

removeFileBtn.addEventListener("click", () => {
  resetFileInput();
});

function resetFileInput() {
  fileInput.value = "";
  fileName.textContent = "Nenhum arquivo selecionado";
  removeFileBtn.style.display = "none";
  textArea.disabled = false;
}


async function submitData() {
  let formData = new FormData();
  let text = textArea.value.trim();
  let file = fileInput.files[0];

  if (text && file) {
    showError("Escolha apenas TEXTO ou ARQUIVO.");
    return;
  }

  if (text) formData.append("text", text);
  if (file) formData.append("file", file);

  // estado de carregamento
  responseBox.style.display = "block";
  responseBox.innerHTML = `<div class="loader"></div> <span>Analisando email...</span>`;

  try {
    let res = await fetch("/process", {
      method: "POST",
      body: formData
    });

    let data = await res.json();

    if (!res.ok || data.error) {
      const msg = data.error || `Erro ${res.status} no processamento.`;
      return showError(msg);
    }

    let badgeClass = data.label === 1 ? "badge-important" : "badge-not-important";
    let badgeText = data.label === 1 ? "Produtivo" : "Improdutivo";

    responseBox.innerHTML = `
      <div class="card">
        <div class="reply"><strong>Resposta sugerida:</strong><br>${data.reply}</div>
        <div class="badge ${badgeClass}">${badgeText}</div>
      </div>
    `;
  } catch (err) {
    showError("Erro: não foi possível processar a requisição.");
  }
}

function showError(msg) {
  responseBox.style.display = "block";
  responseBox.innerHTML = `
    <div class="card">
      <div class="badge badge-not-important">${msg}</div>
    </div>
  `;
}