idatual = 0;

const modal = new bootstrap.Modal(document.getElementById('modalAlterar'));

const modalExcluir = new bootstrap.Modal(document.getElementById('modalExcluir'));

function novo() {
    idatual = -1;
    const txtnomemarca = document.getElementById("txtnomemarca");
    const txtlogo = document.getElementById("txtlogo");
    const txtpais = document.getElementById("txtpais");
    const txttelefone = document.getElementById("txttelefone");

    //limpa os campo
    txtnomemarca.value = "";
    txtlogo.value = "";
    txtpais.value = "";
    txttelefone.value = "";
 
    //abre a dialog
    modal.show();
}
function alterar(id) {
    idatual = id;
    //carregar os dados do id passado por parametro
    fetch("http://127.0.0.1:3333/marca/" + id)
    .then(resp => resp.json())
    .then(dados => {
        //preenche os inputs
        const txtnomemarca = document.getElementById("txtnomemarca");
        const txtlogo = document.getElementById("txtlogo");
        const txtpais = document.getElementById("txtpais");
        const txttelefone = document.getElementById("txttelefone");

        txtnomemarca.value = dados.nomemarca == undefined ? "" : dados.nomemarca;
        txtlogo.value = dados.logo == undefined ? "" : dados.logo;
        txtpais.value = dados.pais_origem == undefined ? "" : dados.pais_origem;
        txttelefone.value = dados.telefone_sac == undefined ? "" : dados.telefone_sac;       

        //mostra a dialog para alterar
        modal.show();
    });
}
function listar() {
    const lista = document.getElementById("lista");
    lista.innerHTML = "<tr><td colspan=5>Carregando...</td></tr>";

    const txtpesquisa = document.getElementById("txtpesquisa");


    fetch("http://127.0.0.1:3333/marca?pesquisa=" + txtpesquisa.value)
    .then(resp => resp.json())
    .then(dados => mostrar(dados));
}
function mostrar(dados) {
    const lista = document.getElementById("lista");
    //limpa a lista
    lista.innerHTML = "";
    //percorre os dados
    for (var i in dados) {
        let id = dados[i].idmarca;
        let nomemarca = dados[i].nomemarca == undefined ? "-" : dados[i].nomemarca;
        let logo = dados[i].logo == undefined ? "-" : dados[i].logo;
        let pais = dados[i].pais_origem == undefined ? "-" : dados[i].pais_origem;
        let telefone = dados[i].telefone_sac == undefined ? "-" : dados[i].telefone_sac;

        lista.innerHTML += "<tr>"
            + "<td class='colunaID'>" + id + "</td>"
            + "<td colspan='2'>" + nomemarca + "</td>"
            + "<td colspan='2' style='text-align: center;'><img src='" + logo + "' width='40' height='40'></td>"
            + "<td colspan='2'>" + pais + "</td>"
            + "<td class='colunaTelefone'>" + telefone + "</td>"
            + "<td class='colunaBotoes'>"
            + "<button type='button' class='btn btn-primary' "
            + " onclick='alterar("+id+")'><img src='https://cdn-icons-png.freepik.com/512/565/565317.png' width='20' height='20' style='filter: invert(1);'></button>"
            + "<button type='button' class='btn btn-danger' style='margin-left: 10px'"
            + " onclick='excluir("+id+")'><img src='https://icons.veryicon.com/png/o/miscellaneous/management-console-icon-update-0318/material-delete.png' width='20' height='20' style='filter: invert(1);'></button>"
            + "</td>"
            + "</tr>";
    }
}
function excluir(id) {
    idatual = id;
    modalExcluir.show();
}
function excluirSim() {
    fetch("http://127.0.0.1:3333/marca/" + idatual,
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
        const txtnomemarca = document.getElementById("txtnomemarca");
        const txtlogo = document.getElementById("txtlogo");
        const txtpais = document.getElementById("txtpais");
        const txttelefone = document.getElementById("txttelefone");

    const dados = {
        nomemarca: txtnomemarca.value,
        logo: txtlogo.value,
        pais_origem: txtpais.value, 
        telefone_sac: txttelefone.value,
    }

    var url;
    var metodo;
    if (idatual<=0) {
        //inserir
        url = "http://127.0.0.1:3333/marca";
        metodo = "POST";
    } else {
        //alterar
        url = "http://127.0.0.1:3333/marca/" + idatual;
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