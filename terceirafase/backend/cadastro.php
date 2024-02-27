<?php

//iniciar sessão php
session_start();

// coomando para iniciar o mysql
$conectar = mysql_connect('localhost','root','');

//selecionar o BD revenda
$banco = mysql_select_db('revenda');

//comandos para verificar as opçoes
// GRAVAR EXCLUIR ALTERAR PESQUISAR

if (isset($_POST['gravar']))// erro aqui!
{
    // capturar as variaveis do html
    $codigo = $_POST['codigo'];
    $nome   = $_POST['nome'];

    $sql = "insert into marca (codigo, nome) values ('$codigo','$nome')";

    // executar o comando BD
    $resultado = mysql_query($sql);

    //verificar resultado
    if ($resultado === TRUE)
    {

        echo "Dados gravados com sucesso.";
    }
    else
    {
        echo "erro ao gravar os dados";
    }
}

if (isset($_POST['excluir']))// erro aqui!
{
    // capturar as variaveis do html
    $codigo = $_POST['codigo'];
    $nome   = $_POST['nome'];

    $sql = "delete from marca WHERE codigo = $codigo";

    // executar o comando BD
    $resultado = mysql_query($sql);

    //verificar resultado
    if ($resultado === TRUE)
    {

        echo "Dados deletados com sucesso.";
    }
    else
    {
        echo "Erro ao deletar os dados";
    }
}

if (isset($_POST['alterar']))// erro aqui!
{
    $codigo = $_POST['codigo'];
    $nome   = $_POST['nome'];

    $sql = "update marca set nome = '$nome'
     where codigo = '$codigo'";

    // executar o comando BD
    $resultado = mysql_query($sql);

    //verificar resultado
    if ($resultado === TRUE)
    {

        echo "Dados gravados com sucesso.";
    }
    else
    {
        echo "Erro ao gravar os dados";
    }
}

if (isset($_POST['pesquisar']))// erro aqui!
{    
    $sql = mysql_query("SELECT * FROM marca");

    echo"<b>Marcas Cadastradas:</b> <br><br>";

    while ($dados = mysql_fetch_object($sql)){
        echo "codigo:".$dados->codigo. "   ";
        echo "nome: ".$dados->nome."<br>";
    }
}