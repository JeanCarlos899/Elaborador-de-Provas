
const moments = []
const redoStack = []
const divProva = document.querySelector('.prova')

function saveMoment() {
    moments.push(divProva.innerHTML)
}

function undo() {
    if (moments.length > 0) {
        const lastMemento = moments.pop();
        redoStack.push(divProva.innerHTML);
        divProva.innerHTML = lastMemento;
    }
}

function redo() {
    if (redoStack.length > 0) {
        const lastRedo = redoStack.pop();
        moments.push(divProva.innerHTML);
        divProva.innerHTML = lastRedo;
    }
}

document.addEventListener("keydown", function (e) {
    if (e.ctrlKey && e.keyCode == 90) {
        undo();
    }
    if (e.ctrlKey && e.keyCode == 89) {
        redo();
    }
});

const undoButton = document.querySelector('.undo')
const redoButton = document.querySelector('.redo')

undoButton.addEventListener('click', function () {
    undo();
})

redoButton.addEventListener('click', function () {
    redo();
})