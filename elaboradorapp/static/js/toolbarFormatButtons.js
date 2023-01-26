
// Obter o botão
var botaoNegrito = document.querySelector(".bold");
var estadoBotao = false;

// Adicionar event listener
botaoNegrito.addEventListener("click", function () {
    estadoBotao = !estadoBotao;
    if (estadoBotao) {
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
        saveMemento();
        // Criar um novo elemento span
        let novoElemento = document.createElement("span");
        novoElemento.style.fontWeight = "bold";
        // Obter o range da seleção
        let range = selecao.getRangeAt(0);
        // Inserir o novo elemento no range
        range.surroundContents(novoElemento);
    }
}

// Obter o botão
var botaoItalico = document.querySelector(".italic");
var estadoBotao = false;

// Adicionar event listener
botaoItalico.addEventListener("click", function () {
    estadoBotao = !estadoBotao;
    if (estadoBotao) {
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
        saveMemento();
        // Criar um novo elemento span
        let novoElemento = document.createElement("span");
        novoElemento.style.fontStyle = "italic";
        // Obter o range da seleção
        let range = selecao.getRangeAt(0);
        // Inserir o novo elemento no range
        range.surroundContents(novoElemento);
    }
}

// Obter o botão
var botaoSublinhado = document.querySelector(".underline");
var estadoBotao = false;

// Adicionar event listener
botaoSublinhado.addEventListener("click", function () {
    estadoBotao = !estadoBotao;
    if (estadoBotao) {
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
        saveMemento();
        // Criar um novo elemento span
        let novoElemento = document.createElement("span");
        novoElemento.style.textDecoration = "underline";
        // Obter o range da seleção
        let range = selecao.getRangeAt(0);
        // Inserir o novo elemento no range
        range.surroundContents(novoElemento);
    }
}

// Obter o botão
var fontCase = document.querySelector(".font-case");
var estadoBotao = false;

// Adicionar event listener
fontCase.addEventListener("click", function () {
    estadoBotao = !estadoBotao;
    if (estadoBotao) {
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
        saveMemento();
        // Obter o range da seleção
        let range = selecao.getRangeAt(0);
        // Criar um novo texto com o conteúdo em maiúsculas
        let novoTexto = document.createTextNode(selecao.toString().toUpperCase());
        // Remover o conteúdo antigo
        range.deleteContents();
        // Inserir o novo texto no range
        range.insertNode(novoTexto);
    }
}

// Obter o botão
var fontColor = document.querySelector(".color");
var estadoBotao = false;

// Adicionar event listener
fontColor.addEventListener("click", function () {
    estadoBotao = !estadoBotao;
    if (estadoBotao) {
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
        saveMemento();
        let color = document.querySelector(".color-picker-input").value;
        let novoElemento = document.createElement("span");
        novoElemento.style.color = color;
        let range = selecao.getRangeAt(0);
        range.surroundContents(novoElemento);
    }
}

