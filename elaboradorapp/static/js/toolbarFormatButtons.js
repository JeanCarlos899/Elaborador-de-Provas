
// Obter o botão
var botaoNegrito = document.querySelector(".bold");
var estadoBotaoNegrito = false;

// Adicionar event listener
botaoNegrito.addEventListener("click", function () {
    estadoBotaoNegrito = !estadoBotaoNegrito;
    if (estadoBotaoNegrito) {
        // Ativar formatação de negrito
        botaoNegrito.style.color = "#1a73e8";
        botaoNegrito.style.backgroundColor = "#e0e0e0";
        botaoNegrito.style.borderRadius = "5px";
        document.addEventListener("mouseup", formataNegrito);
    } else {
        // Desativar formatação de negrito
        botaoNegrito.style.color = "";
        botaoNegrito.style.backgroundColor = "";
        botaoNegrito.style.borderRadius = "";
        document.removeEventListener("mouseup", formataNegrito);
    }
});

function formataNegrito() {
    // Obter a seleção de texto
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        saveMoment();
        // Criar um novo elemento span
        try {
            let novoElemento = document.createElement("span");
            novoElemento.style.fontWeight = "bold";
            // Obter o range da seleção
            let range = selecao.getRangeAt(0);
            // Inserir o novo elemento no range
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
}

// Obter o botão
var botaoItalico = document.querySelector(".italic");
var estadoBotaoItalico = false;

// Adicionar event listener
botaoItalico.addEventListener("click", function () {
    estadoBotaoItalico = !estadoBotaoItalico;
    if (estadoBotaoItalico) {
        // Ativar formatação de negrito
        botaoItalico.style.color = "#1a73e8";
        botaoItalico.style.backgroundColor = "#e0e0e0";
        botaoItalico.style.borderRadius = "5px";
        document.addEventListener("mouseup", formataItalico);
    } else {
        // Desativar formatação de negrito
        botaoItalico.style.color = "";
        botaoItalico.style.backgroundColor = "";
        botaoItalico.style.borderRadius = "";
        document.removeEventListener("mouseup", formataItalico);
    }
});

function formataItalico() {
    // Obter a seleção de texto
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        saveMoment();
        // Criar um novo elemento span
        try {
            let novoElemento = document.createElement("span");
            novoElemento.style.fontStyle = "italic";
            // Obter o range da seleção
            let range = selecao.getRangeAt(0);
            // Inserir o novo elemento no range
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
}

// Obter o botão
var botaoSublinhado = document.querySelector(".underline");
var estadoBotaoSublinhado = false;

// Adicionar event listener
botaoSublinhado.addEventListener("click", function () {
    estadoBotaoSublinhado = !estadoBotaoSublinhado;
    if (estadoBotaoSublinhado) {
        // Ativar formatação de negrito
        botaoSublinhado.style.color = "#1a73e8";
        botaoSublinhado.style.backgroundColor = "#e0e0e0";
        botaoSublinhado.style.borderRadius = "5px";
        document.addEventListener("mouseup", formataSublinhado);
    } else {
        // Desativar formatação de negrito
        botaoSublinhado.style.color = "";
        botaoSublinhado.style.backgroundColor = "";
        botaoSublinhado.style.borderRadius = "";
        document.removeEventListener("mouseup", formataSublinhado);
    }
});

function formataSublinhado() {
    // Obter a seleção de texto
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        saveMoment();
        // Criar um novo elemento span
        try {
            let novoElemento = document.createElement("span");
            novoElemento.style.textDecoration = "underline";
            // Obter o range da seleção
            let range = selecao.getRangeAt(0);
            // Inserir o novo elemento no range
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
}

// Obter o botão
var fontCase = document.querySelector(".font-case");
var estadoBotaoFontCase = false;

// Adicionar event listener
fontCase.addEventListener("click", function () {
    estadoBotaoFontCase = !estadoBotaoFontCase;
    if (estadoBotaoFontCase) {
        // Ativar formatação de negrito
        fontCase.style.color = "#1a73e8";
        fontCase.style.backgroundColor = "#e0e0e0";
        fontCase.style.borderRadius = "5px";
        document.addEventListener("mouseup", formataFontCase);
    } else {
        // Desativar formatação de negrito
        fontCase.style.color = "";
        fontCase.style.backgroundColor = "";
        fontCase.style.borderRadius = "";
        document.removeEventListener("mouseup", formataFontCase);
    }
});

function formataFontCase() {
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        saveMoment();
        // Obter o range da seleção
        try {
            let range = selecao.getRangeAt(0);
            // Criar um novo texto com o conteúdo em maiúsculas
            let novoTexto = document.createTextNode(selecao.toString().toUpperCase());
            // Remover o conteúdo antigo
            range.deleteContents();
            // Inserir o novo texto no range
            range.insertNode(novoTexto);
        } catch (e) {
            // ignorar
        }
    }
}

// Obter o botão
var fontColor = document.querySelector(".color");
var estadoBotaoColor = false;

// Adicionar event listener
fontColor.addEventListener("click", function () {
    estadoBotaoColor = !estadoBotaoColor;
    if (estadoBotaoColor) {
        // Ativar formatação de negrito
        fontColor.style.color = "#1a73e8";
        fontColor.style.backgroundColor = "#e0e0e0";
        fontColor.style.borderRadius = "5px";
        document.addEventListener("mouseup", formataFontColor);
    } else {
        // Desativar formatação de negrito
        fontColor.style.color = "";
        fontColor.style.backgroundColor = "";
        fontColor.style.borderRadius = "";
        document.removeEventListener("mouseup", formataFontColor);
    }
});

function formataFontColor() {
    let selecao = window.getSelection();
    if (selecao.toString().length > 0) {
        saveMoment();
        try {
            let color = document.querySelector(".color-picker-input").value;
            let novoElemento = document.createElement("span");
            novoElemento.style.color = color;
            let range = selecao.getRangeAt(0);
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
}