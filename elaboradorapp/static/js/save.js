
document.querySelector(".save").addEventListener("click", function(){
    const url = location.pathname;
    const parts = url.split('/');
    const idProva = parts[parts.length - 1];
    var divContent = document.querySelector(".avaliacao").innerHTML;
    var nomeProva = document.querySelector("title").innerHTML;
    var nomePersonalizado = document.querySelector(".name-input").value;
    if (nomePersonalizado != "") {
        nomeProva = nomePersonalizado;
    }
    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/salvar-prova/', true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrf_token);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Cria o elemento div com a mensagem de sucesso
            var popup = document.createElement("div");
            popup.innerHTML = "Prova salva com sucesso!";
            popup.classList.add("popup");
            document.body.appendChild(popup);
            
            // Remove o elemento após 3 segundos
            setTimeout(function(){
                popup.remove();
            }, 1000);
        }
    };
    xhr.send("html_prova=" + divContent + "&nome_prova=" + nomeProva + "&id=" + idProva);
});

function confirmDeletion() {
    if (confirm("Tem certeza de que deseja excluir esta prova?")) {
      return true;
    } else {
      return false;
    }
  }
  