// index.js
const express = require('express');
const app = express();

// Middleware: habilita leitura de JSON no corpo das requisições
app.use(express.json());

// Define a porta onde o servidor vai escutar
const PORT = 3000;

// Rota raiz: GET /
app.get('/', (req, res) => {
    res.send('Olá, Mundo! Minha primeira API com Express.');
});


// Dados em memória (array simula o banco de dados por enquanto)
let produtos = [
    { id: 1, nome: 'Notebook', preco: 2500.00 },
    { id: 2, nome: 'Mouse', preco: 89.90 },
    { id: 3, nome: 'Teclado', preco: 149.00 },
];

// GET /produtos — retorna todos os produtos
app.get('/produtos', (req, res) => {
    res.status(200).json(produtos);
});

// GET /produtos/:id — retorna um produto específico
app.get('/produtos/:id', (req, res) => {
    const id = parseInt(req.params.id);             // converte string para int
    const produto = produtos.find(p => p.id=== id);

    if (!produto) {
        return res.status(404).json({ mensagem: 'Produto não encontrado' });
    }

    res.status(200).json(produto);
});


// POST /produtos — cria um novo produto
app.post ('/produtos', (req, res) => {
    const {nome, preco} = req.body;     

    // Validação Básica
    if (!nome || preco === undefined) {
        return res.status(400).json ({ mensagem: 'Nome e e preço são obrigatórios '});
    }

    // Gerar um novo ID
    const novoId = produtos.legth > 0   // Se a quantidade de produtos for maior que 0
        ? Math.max(...produtos.map(p=> p.id)) + 1   //Adicione 1 ao maior id já cadastrado
        : 1;                            // se igual a 0, o ID é 1

    const novoProduto = {id: novoId, nome, preco }; // variável com informações do novo produto
    produtos.push(novoProduto);                     // adiciona o novo produto ao array

    res.status(201).json(novoProduto); // 201 Created

})


// Inicia o servidor
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
