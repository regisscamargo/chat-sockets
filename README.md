# Chat de Sistemas Distribuídos

Este repositório contém o código-fonte de um chat desenvolvido como parte de uma atividade da disciplina de Sistemas Distribuídos, ministrada na Universidade do Planalto Catarinense, no curso de Sistemas de Informação.

## Descrição

O chat implementado neste projeto é uma aplicação cliente-servidor que permite a comunicação entre múltiplos usuários em uma rede distribuída. Ele foi desenvolvido como parte de um estudo sobre conceitos fundamentais de sistemas distribuídos, incluindo comunicação entre processos, protocolos de rede e interfaces gráficas de usuário.

## Funcionalidades

- **Login de Usuário:** Os usuários podem fazer login fornecendo um nome de usuário, endereço IP e porta.
- **Chat em Grupo:** Os usuários podem enviar mensagens que serão distribuídas para todos os outros usuários conectados ao servidor.
- **Mensagens Privadas:** Além do chat em grupo, os usuários podem enviar mensagens privadas diretamente para outro usuário, que só será visível para o destinatário.
- **Interface Gráfica:** A aplicação possui uma interface gráfica de usuário que facilita a interação e visualização das mensagens.

## Estrutura do Projeto

O projeto é dividido em duas partes principais:

- **Cliente:** Contém o código-fonte do cliente do chat, incluindo a interface gráfica de usuário e a lógica de comunicação com o servidor.
- **Servidor:** Contém o código-fonte do servidor do chat, que gerencia as conexões dos clientes e distribui as mensagens.

## Tecnologias Utilizadas

- **Python:** A linguagem de programação principal usada para implementar tanto o cliente quanto o servidor.
- **Qt:** Utilizado para criar a interface gráfica de usuário do cliente.
- **Sockets:** Para comunicação entre o cliente e o servidor via TCP/IP.

## Como Executar

1. Clone este repositório em sua máquina local.
2. Execute o servidor fornecendo um endereço IP e uma porta.
3. Execute o cliente e insira as informações de login.
4. Comece a enviar mensagens para o chat em grupo ou diretamente para outros usuários.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Este projeto foi desenvolvido como parte de uma atividade acadêmica por Régis Camargo.
