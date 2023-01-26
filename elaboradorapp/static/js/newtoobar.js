function formataNegrito() {
    // Obter a seleção de texto
    var selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        saveMoment();
        // Obter o range da seleção
        var range = selecao.getRangeAt(0);
        var nos = [];
        recursivelyGetTextNodes(range.commonAncestorContainer, nos);
        for (var i = 0; i < nos.length; i++) {
            var nodeRange = document.createRange();
            nodeRange.selectNode(nos[i]);
            if (range.compareBoundaryPoints(Range.START_TO_START, nodeRange) <= 0 && range.compareBoundaryPoints(Range.END_TO_END, nodeRange) >= 0) {
                var novoElemento = document.createElement("span");
                novoElemento.style.fontWeight = "bold";
                novoElemento.appendChild(nos[i].cloneNode());
                nos[i].parentNode.replaceChild(novoElemento, nos[i]);
            }
        }
    }
}

function recursivelyGetTextNodes(node, nodes) {
    if (node.nodeType === Node.TEXT_NODE) {
        nodes.push(node);
    } else {
        for (var i = 0; i < node.childNodes.length; i++) {
            recursivelyGetTextNodes(node.childNodes[i], nodes);
        }
    }
}






function formataNegrito() {
    // Obter a seleção de texto
    var selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        saveMoment();
        var novoElemento = document.createElement("span");
        novoElemento.style.fontWeight = "bold";
        var range = selecao.getRangeAt(0);
        range.surroundContents(novoElemento);
    }
}