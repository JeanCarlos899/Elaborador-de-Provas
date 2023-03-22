const decreaseButton = document.querySelector('.decrease-font-size');
const increaseButton = document.querySelector('.increase-font-size');
const fontSizeNumber = document.querySelector('.font-size-number');

decreaseButton.addEventListener('click', function () {
    saveMoment();
    let currentSize = fontSizeNumber.value;
    fontSizeNumber.value = currentSize - 1;
    document.querySelectorAll("p").forEach(function (p) {
        p.style.fontSize = fontSizeNumber.value + "px";
    });
});

increaseButton.addEventListener('click', function () {
    saveMoment();
    let currentSize = fontSizeNumber.value;
    fontSizeNumber.value = parseInt(currentSize) + 1;
    document.querySelectorAll("p").forEach(function (p) {
        p.style.fontSize = fontSizeNumber.value + "px";
    });
});

fontSizeNumber.addEventListener('change', function () {
    document.querySelectorAll("p").forEach(function (p) {
        p.style.fontSize = fontSizeNumber.value + "px";
    });
});

const decreaseImageEnunciado = document.querySelector('.decrease-image-enunciado-size');
const increaseImageEnunciado = document.querySelector('.increase-image-enunciado-size');
const imageEnunciadoNumber = document.querySelector('.image-enunciado-number');

decreaseImageEnunciado.addEventListener('click', function () {
    saveMoment();
    let currentQuestion = imageEnunciadoNumber.value;
    let currentHeight = document.getElementById(`imagem-enunciado-${currentQuestion}`).style.height;
    let imagens = document.querySelectorAll(`#imagem-enunciado-${currentQuestion}`);
    imagens.forEach(function (imagem) {
        imagem.style.height = (parseInt(currentHeight) - 5) + "px";
    });
});

increaseImageEnunciado.addEventListener('click', function () {
    saveMoment();
    let currentQuestion = imageEnunciadoNumber.value;
    console.log(currentQuestion);
    let currentHeight = document.getElementById(`imagem-enunciado-${currentQuestion}`).style.height;
    let imagens = document.querySelectorAll(`#imagem-enunciado-${currentQuestion}`);
    imagens.forEach(function (imagem) {
        imagem.style.height = (parseInt(currentHeight) + 5) + "px";
    });
});

const decreaseImageResposta = document.querySelector('.decrease-image-resposta-size');
const increaseImageResposta = document.querySelector('.increase-image-resposta-size');
const imageRespostaNumber = document.querySelector('.image-resposta-number');

decreaseImageResposta.addEventListener('click', function () {
    saveMoment();
    let currentQuestion = imageRespostaNumber.value;
    let currentHeight = document.getElementById(`imagem-alternativa-${currentQuestion}`).style.height;
    let imagens = document.querySelectorAll(`#imagem-alternativa-${currentQuestion}`);
    imagens.forEach(function (imagem) {
        imagem.style.height = (parseInt(currentHeight) - 5) + "px";
    });
});

increaseImageResposta.addEventListener('click', function () {
    saveMoment();
    let currentQuestion = imageRespostaNumber.value;
    let currentHeight = document.getElementById(`imagem-alternativa-${currentQuestion}`).style.height;
    let imagens = document.querySelectorAll(`#imagem-alternativa-${currentQuestion}`);
    imagens.forEach(function (imagem) {
        imagem.style.height = (parseInt(currentHeight) + 3) + "px";
    });
});

function removeMarginLeft () {
    saveMoment();
    let currentQuestion = imageEnunciadoNumber.value;
    let currentMargin = document.getElementById(`imagem-enunciado-${currentQuestion}`).style.marginLeft;
    if (currentMargin === "") {
        currentMargin = 0;
    }
    let imagens = document.querySelectorAll(`#imagem-enunciado-${currentQuestion}`);
    imagens.forEach(function (imagem) {
        imagem.style.marginLeft = (parseInt(currentMargin) - 5) + "px";
    });
}

function removeImageEnunciado() {
    saveMoment();
    let currentQuestion = imageEnunciadoNumber.value;
    let imagens = document.querySelectorAll(`#imagem-enunciado-${currentQuestion}`);
    imagens.forEach(function (imagem) {
        // remover o elemento
        imagem.remove();
    });
};

var ultimoClick = '';

function attImageEnunciado(id) {
    ultimoClick = "imagem-enunciado";
    document.querySelector(".image-enunciado-number").value = id;
    document.querySelector(".image-enunciado-number").classList.add("atualizando");
    setTimeout(function() {
        document.querySelector(".image-enunciado-number").classList.remove("atualizando");
    }, 100);
}

function attImageResposta(id) {
    ultimoClick = "imagem-resposta";
    document.querySelector(".image-resposta-number").value = id;
    document.querySelector(".image-resposta-number").classList.add("atualizando");
    setTimeout(function() {
        document.querySelector(".image-resposta-number").classList.remove("atualizando");
    }, 100);
}

const alignCenter = () => {
  saveMoment();
  let currentQuestion = imageEnunciadoNumber.value;
  let divImagem = document.getElementById(
    `imagem-enunciado-${currentQuestion}`
  ).parentElement;
  divImagem.style.justifyContent = "center";
  console.log("center");
};

const alignLeft = () => {
  saveMoment();
  let currentQuestion = imageEnunciadoNumber.value;
  let divImagem = document.getElementById(
    `imagem-enunciado-${currentQuestion}`
  ).parentElement;
  divImagem.style.justifyContent = "left";
  console.log("left");
};

const alignRight = () => {
  saveMoment();
  let currentQuestion = imageEnunciadoNumber.value;
  let divImagem = document.getElementById(
    `imagem-enunciado-${currentQuestion}`
  ).parentElement;
  divImagem.style.justifyContent = "right";
  console.log("right");
};


document.addEventListener('keydown', function (event) {
    if (event.key === 'q') {
        if (ultimoClick === "imagem-enunciado") {
            decreaseImageEnunciado.click();
        } else if (ultimoClick === "imagem-resposta") {
            decreaseImageResposta.click();
        }
    }
    if (event.key === 'e') { 
        if (ultimoClick === "imagem-enunciado") {
            increaseImageEnunciado.click();
        } else if (ultimoClick === "imagem-resposta") {
            increaseImageResposta.click();
        }
    }
    if (event.key === 'Delete') {
        if (ultimoClick === "imagem-enunciado") {
            removeImageEnunciado();
        } 
    }
    if (event.key === 'w') {
        if (ultimoClick === "imagem-enunciado") {
            alignCenter();
        }
    }
    if (event.key === 'a') {
        if (ultimoClick === "imagem-enunciado") {
            alignLeft();
        }
    }
    if (event.key === 'd') {
        if (ultimoClick === "imagem-enunciado") {
            alignRight();
        }
    }
});