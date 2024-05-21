idatual = 0;

const modal = new bootstrap.Modal(
    document.getElementById('modalAlterar'));

const modalExcluir = new bootstrap.Modal(
    document.getElementById('modalExcluir'));

function novo() {
    idatual = -1;
    const txtnome = document.getElementById("txtnome");
    const txttelefone = document.getElementById("txttelefone");
    const txtemail = document.getElementById("txtemail");
    const txtsenha = document.getElementById("txtsenha");

    //limpa os campo
    txtnome.value = "";
    txttelefone.value = "";
    txtemail.value = "";
    txtsenha.value = "";

    //abre a dialog
    modal.show();
}
function alterar(id) {
    idatual = id;
    //carregar os dados do id passado por parametro
    fetch("http://127.0.0.1:5000/usuario/" + id)
    .then(resp => resp.json())
    .then(dados => {
        //preenche os inputs
        const txtnome = document.getElementById("txtnome");
        const txttelefone = document.getElementById("txttelefone");
        const txtemail = document.getElementById("txtemail");
        const txtsenha = document.getElementById("txtsenha");

        txtnome.value = dados.nome;
        txttelefone.value = dados.telefone;
        txtemail.value = dados.email;
        txtsenha.value = dados.senha;

        //mostra a dialog para alterar
        modal.show();
    });
}
function listar() {
    const lista = document.getElementById("lista");
    lista.innerHTML = "<tr><td colspan=5>Carregando...</td></tr>";

    const txtpesquisa = document.getElementById("txtpesquisa");


    fetch("http://127.0.0.1:5000/usuario?pesquisa=" + txtpesquisa.value)
    .then(resp => resp.json())
    .then(dados => mostrar(dados));
}
function mostrar(dados) {
    const lista = document.getElementById("lista");
    //limpa a lista
    lista.innerHTML = "";
    //percorre os dados
    for (var i in dados) {
        let id = dados[i].idusuario;
        lista.innerHTML += "<tr>"
            + "<td>" + id + "</td>"
            + "<td>" + dados[i].nome + "</td>"
            + "<td>" + dados[i].telefone + "</td>"
            + "<td>" + dados[i].email + "</td>"
            + "<td>"
            + "<button type='button' class='btn btn-primary' "
            + " onclick='alterar("+id+")'>Alterar</button>"
            + "<button type='button' class='btn btn-danger' "
            + " onclick='excluir("+id+")'>Excluir</button>"
            + "</td>"
            + "</tr>";
    }
}
function excluir(id) {
    idatual = id;
    modalExcluir.show();
}
function excluirSim() {
    fetch("http://127.0.0.1:5000/usuario/" + idatual,
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
            method: "DELETE", 
            body: ""
        }
    ).then(() => {
        //fecha a dialog
        modalExcluir.hide();
        //recarrega a lista
        listar();
    })
}
function salvar() {
    const txtnome = document.getElementById("txtnome");
    const txttelefone = document.getElementById("txttelefone");
    const txtemail = document.getElementById("txtemail");
    const txtsenha = document.getElementById("txtsenha");

    const dados = {
        nome: txtnome.value,
        telefone: txttelefone.value,
        email: txtemail.value,
        senha: txtsenha.value 
    }

    var url;
    var metodo;
    if (idatual<=0) {
        //inserir
        url = "http://127.0.0.1:5000/usuario";
        metodo = "POST";
    } else {
        //alterar
        url = "http://127.0.0.1:5000/usuario/" + idatual;
        metodo = "PUT";
    }
    fetch(url,
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
            method: metodo, 
            body: JSON.stringify(dados)
        }
    ).then(() => {
        //abre a dialog
        modal.hide();
        //recarrega a lista
        listar();
    })

}

listar();