# 🎵 Lyrics Importer

<div align="center">

**Automação de importação de letras para o ProPresenter 7.8**

Solução completa para importar letras de músicas diretamente no ProPresenter com um único clique.

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Build do Executável](#-build-do-executável)
- [Troubleshooting](#-troubleshooting)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

O **Lyrics Importer** é uma ferramenta desenvolvida para automatizar o processo de importação de letras de músicas no ProPresenter 7.8. O aplicativo roda em segundo plano como um ícone na bandeja do sistema, iniciando um servidor local que recebe requisições de importação.

### Como Funciona

1. 📡 Servidor Flask rodando localmente na porta 3000
2. 🌐 Recebe URL da música via requisição HTTP POST
3. 🔍 Faz scraping da letra do site
4. 📝 Formata a letra adequadamente para projeção
5. 🎬 Automatiza a importação no ProPresenter usando pyautogui

---

## ✨ Funcionalidades

- 🚀 **Servidor em Background**: Executa como ícone na bandeja do sistema
- 🔄 **Importação Automática**: Um clique para importar letras completas
- 📋 **Formatação Inteligente**: Ajusta automaticamente espaçamento e quebras de linha
- 🎯 **Integração com ProPresenter**: Detecta e interage com a janela do ProPresenter
- 🖼️ **Interface Simples**: Menu de contexto para controlar o servidor
- 📊 **Logs Detalhados**: Sistema de logging para debug e monitoramento

---

## 🛠️ Tecnologias

### Backend
- **Python 3.13** - Linguagem principal
- **Flask** - Framework web para API REST
- **Flask-CORS** - Suporte para CORS

### Automação
- **PyAutoGUI** - Automação de GUI e teclado
- **PyGetWindow** - Gerenciamento de janelas
- **Pyperclip** - Manipulação da área de transferência
- **Pystray** - Ícone na bandeja do sistema

### Web Scraping
- **Requests** - Requisições HTTP
- **BeautifulSoup4** - Parse de HTML

### Build
- **PyInstaller** - Criação de executável standalone

---

## 📦 Pré-requisitos

- **Python 3.13+**
- **ProPresenter 7.8** instalado e configurado
- **Windows** (testado no Windows, pode precisar ajustes para outros OS)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/lyrics-importer.git
cd lyrics-importer
```

### 2. Instale as dependências

```bash
pip install flask flask-cors pyautogui pygetwindow pyperclip pystray pillow requests beautifulsoup4 pyinstaller
```

### 3. Execute o aplicativo

```bash
cd src/app
python main.py
```

O ícone aparecerá na bandeja do sistema. Clique com o botão direito para iniciar o servidor.

---

## 💡 Como Usar

### Iniciando o Servidor

1. Execute o aplicativo (aparecerá um ícone na bandeja)
2. Clique com o botão direito no ícone
3. Selecione **"Iniciar"** para iniciar o servidor
4. O servidor estará rodando em `http://localhost:3000`

### Importando uma Letra

Envie uma requisição POST para `http://localhost:3000/import`:

```bash
curl -X POST http://localhost:3000/import \
  -H "Content-Type: application/json" \
  -d '{"url": "https://site-de-letras.com/musica"}'
```

Ou via JavaScript:

```javascript
fetch('http://localhost:3000/import', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ url: 'https://site-de-letras.com/musica' })
})
.then(res => res.json())
.then(data => console.log(data));
```

### Resposta da API

**Sucesso:**
```json
{
  "status": "ok"
}
```

**Erro:**
```json
{
  "status": "error",
  "message": "Descrição do erro"
}
```

---

## 📁 Estrutura do Projeto

```
lyrics-importer/
├── src/
│   └── app/
│       ├── main.py                 # Aplicativo principal (Flask + Tray Icon)
│       ├── logic.py                # Lógica de importação
│       ├── main.spec               # Configuração PyInstaller
│       ├── assets/
│       │   └── icon.ico            # Ícone do aplicativo
│       ├── resources/
│       │   └── importar_btn.png    # Imagem do botão de importação
│       └── utils/
│           ├── fetch.py            # Busca de letras (web scraping)
│           ├── formatter.py        # Formatação de letras
│           └── resource_path.py    # Resolução de caminhos
├── dist/                           # Executável gerado (após build)
├── README.md
└── .gitignore
```

---

## 🔨 Build do Executável

### 1. Instale o PyInstaller

```bash
pip install pyinstaller
```

### 2. Execute o build

```bash
cd src/app
pyinstaller main.spec
```

O executável será gerado em `dist/Lyrics Importer.exe`

### 3. Configurações do Build (main.spec)

- **Icon**: `assets/icon.ico`
- **Console**: Desabilitado (modo windowed)
- **UPX**: Habilitado para compressão
- **Data Files**: Inclui `assets/` e `resources/`

---

## 🐛 Troubleshooting

### ❌ "ProPresenter não está aberto"

**Solução**: Verifique se o ProPresenter está em execução antes de importar uma letra.

### ❌ "Letra não encontrada na página"

**Solução**: Verifique se a URL está correta e se o site usa o seletor `.lyric-original`.

### ❌ "Botão de importação não encontrado"

**Solução**: 
- Certifique-se de que a imagem `importar_btn.png` está atualizada
- Ajuste o parâmetro `confidence` em `logic.py` (linha 73)

### 📝 Verificar Logs

Os logs são salvos em `server_debug.log` no diretório de execução:

```bash
tail -f server_debug.log
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

Desenvolvido com ❤️ para facilitar o trabalho de equipes de louvor e apresentações.

---

## 🌟 Agradecimentos

- ProPresenter pela incrível ferramenta de apresentação
- Comunidade Python pelos excelentes pacotes
- Todos que contribuíram e testaram o aplicativo

---

<div align="center">

**[⬆ Voltar ao topo](#-lyrics-importer)**

</div>
