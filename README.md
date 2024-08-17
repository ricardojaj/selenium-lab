# Selenium Lab

Este projeto foi desenvolvido para aplicar conhecimentos adquiridos no curso **Automação de Testes Web com Selenium Webdriver e Python**. O foco é a criação de testes automatizados para um e-commerce, simulando ações reais dos usuários.

Você pode acessar o curso através do link abaixo:

[Automação de Testes Web com Selenium Webdriver e Python](https://www.udemy.com/share/10by2r3@E6GP7v5xJ68Nv_EvaWpmDTVcXUhwm3VxXw3Lzxb_2yG0fiSNI-diwZkXsP5PJ1y2/)

## Descrição do Projeto

O site testado é um e-commerce onde os usuários podem adicionar produtos ao carrinho, finalizar compras e acessar várias outras funcionalidades. O projeto inclui testes para:

- Acesso à página principal;
- Adição de produtos ao carrinho;
- Processo de finalização de compra;
- Testes de funcionalidades inválidas.

Os testes utilizam o padrão **Page Objects** para organizar o código de forma limpa e eficiente.

---

## Principais Comandos Utilizados

- **find_element:** Localiza elementos na página usando identificadores como ID, nome, classe, e XPath.
- **XPath:** Linguagem usada para navegar pelos elementos em um documento XML, utilizada aqui para localizar elementos na página web.
- **assert:** Verifica se uma condição é verdadeira. Se não for, o teste falha.
- **send_keys:** Simula a digitação de texto em campos de entrada.
- **click:** Simula um clique em elementos da página, como botões e links.

---

## Padrão Page Object

O projeto utiliza o padrão **Page Objects**, uma abordagem que ajuda a manter os testes organizados e fáceis de manter. Nesse padrão, cada página do site é representada por uma classe, e essa classe contém métodos que interagem com os elementos da página. Assim, se algo na interface mudar, você só precisa atualizar a classe correspondente, sem necessidade de modificar todos os testes.

---

## Uso de Classes e Funções

Além do padrão Page Objects, o projeto faz uso extensivo de **classes** e **funções** para estruturar o código de forma modular e reutilizável:

- **Classes:** Cada classe encapsula a lógica relacionada a uma página específica ou a uma funcionalidade do e-commerce. Isso facilita a manutenção e a leitura do código.
- **Funções:** As funções são usadas para realizar operações específicas, como interagir com elementos da UI, verificar resultados e definir fluxos de testes. Isso permite que o código seja mais organizado e que partes repetitivas possam ser reutilizadas.

Essas práticas ajudam a criar um código mais limpo, modular e fácil de expandir conforme o projeto cresce.
