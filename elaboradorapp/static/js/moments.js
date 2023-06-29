
class Moments {
    constructor() {
        this.moments = []
        this.redoStack = []
        this.divProva = document.querySelector('.prova')
        this.undoButton = document.querySelector(".undo");
        this.redoButton = document.querySelector(".redo");
    }

    saveMoment() {
        this.moments.push(this.divProva.innerHTML)
    }

    undo() {
        if (this.moments.length > 0) {
            const lastMemento = this.moments.pop();
            this.redoStack.push(this.divProva.innerHTML);
            this.divProva.innerHTML = lastMemento;
        }
    }

    redo() {
        if (this.redoStack.length > 0) {
            const lastRedo = this.redoStack.pop();
            this.moments.push(this.divProva.innerHTML);
            this.divProva.innerHTML = lastRedo;
        }
    }

    addEventListeners() {
        this.undoButton.addEventListener('click', function () {
            moments.undo();
        })
        this.redoButton.addEventListener('click', function () {
            moments.redo();
        })

        document.addEventListener("keydown", function (e) {
            if (e.ctrlKey && e.key === "z") {
                moments.undo();
            } else if (e.ctrlKey && e.key === "y") {
                moments.redo();
            }
        });
    }

    init() {
        this.addEventListeners();
    }
}

const moments = new Moments();
moments.init();