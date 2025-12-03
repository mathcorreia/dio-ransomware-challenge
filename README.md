# 🔒 Ransomware Simulator (Educational Project)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Educational-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **⚠️ AVISO LEGAL / DISCLAIMER**
> Este software foi desenvolvido estritamente para fins **acadêmicos e educacionais** no âmbito do Bootcamp de Cibersegurança da **Digital Innovation One (DIO)**.
> O uso deste código para criptografar arquivos de terceiros sem consentimento é ilegal e antiético. O autor não se responsabiliza pelo uso indevido desta ferramenta.

---

## 📄 Sobre o Projeto

Este projeto consiste na implementação de um **Ransomware** básico utilizando a linguagem Python. O objetivo principal é desmistificar o funcionamento de malwares que sequestram dados, permitindo compreender na prática os conceitos de criptografia simétrica e manipulação de arquivos.

Ao entender como o ataque funciona, tornamo-nos profissionais de segurança mais capacitados para desenvolver defesas e estratégias de prevenção.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Biblioteca de Criptografia:** `pyaes`
* **Algoritmo:** AES (Advanced Encryption Standard)
* **Modo de Operação:** CTR (Counter Mode)

## ⚙️ Arquitetura da Solução

O projeto é dividido em dois scripts principais que simulam o ciclo de vida de um ataque ransomware:

### 1. O Agente Malicioso (`encrypter.py`)
Responsável por realizar o "sequestro" do arquivo.
1.  Localiza o arquivo alvo (`teste.txt`).
2.  Lê o conteúdo binário do arquivo.
3.  Remove o arquivo original do sistema.
4.  Criptografa os dados utilizando uma chave de 16 bytes.
5.  Salva um novo arquivo com a extensão `.ransomwaretroll`.

### 2. A Ferramenta de Resgate (`decrypter.py`)
Responsável por devolver o acesso aos dados (simulando o pagamento do resgate).
1.  Localiza o arquivo criptografado.
2.  Utiliza a chave de segurança (Key) para reverter a criptografia.
3.  Remove o arquivo malicioso.
4.  Restaura o arquivo original (`teste.txt`) com seu conteúdo legível.

---

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para testar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o Python instalado e instale a dependência necessária:

```
pip install pyaes
```
Passo a Passo

Clone o repositório:


```
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
cd NOME-DO-REPO
```

Crie o arquivo de teste: 

Crie um arquivo chamado teste.txt na raiz do projeto e escreva qualquer frase dentro dele.

Execute a Criptografia:
```
python encrypter.py
```
Resultado: 

O arquivo teste.txt sumirá e aparecerá o arquivo criptografado. 

Tente abri-lo para ver que os dados estão ilegíveis.

Execute a Descriptografia:

```
python decrypter.py
```

Resultado:
O arquivo original é restaurado com sucesso.

🧠 Aprendizados Técnicos

Durante o desenvolvimento deste desafio, foram aplicados os seguintes conceitos:

Manipulação de Arquivos (I/O): 
Leitura e escrita de arquivos em modo binário (rb, wb) para garantir integridade dos dados.

Criptografia AES:
Utilização do padrão AES, que é um algoritmo de chave simétrica (a mesma chave que criptografa é a que descriptografa).

Modo CTR:
O uso do modo Counter transforma o cifrador de bloco em um cifrador de fluxo, permitindo criptografar dados de qualquer tamanho com alta eficiência.

👨‍💻 Autor
Matheus Correia

Projeto desenvolvido como parte do desafio técnico da DIO.
