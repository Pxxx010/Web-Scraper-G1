# Web Scraper G1

Este é um projeto de web scraping que utiliza Selenium para coletar as principais notícias do site G1.

## Descrição

O script automatiza a coleta das 10 principais notícias do portal G1, extraindo:
- Título da notícia
- Link da notícia
- Categoria da notícia

Os dados são salvos em um arquivo `noticias.txt` no formato texto.

## Requisitos

- Python 3.x
- Selenium
- ChromeDriver (gerenciado automaticamente pelo webdriver-manager)

## Instalação

1. Clone este repositório
2. Instale as dependências:

```bash
pip install selenium webdriver-manager
```

## Como usar

1. Execute o script:

```bash
python app.py
```

2. O script irá:
   - Abrir o Chrome em modo headless
   - Acessar o site do G1
   - Coletar as 10 principais notícias
   - Salvar os dados em `noticias.txt`

## Estrutura do projeto

```
.
├── app.py          # Script principal
├── noticias.txt    # Arquivo de saída com as notícias
└── README.md       # Este arquivo
```