﻿
# Download das bases do Google Sheets
![Python](https://img.shields.io/badge/Python-green)
## 📚Bibliotecas utilizadas
```
pip install --upgrade google-auth-httplib2 google-auth-oauthlib gspread
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install pandas
```
## ⚙Como Configurar
### 1️⃣Configuração no Google Console
- Abra o [Google Console](https://console.cloud.google.com/)
- Aceite os termos e crie um projeto
- Ative a API do Google Drive e do Google Sheets
- Clique no Menu > APIs e Serviços > Tela de permissão OAuth
- Clique em **Externo** > Criar 
- Em **Informações do app** defina o Nome do APP e em **E-mail para suporte do usuário** defina o seu e-mail 
- Em **Dados de contato do desenvolvedor** repita o mesmo e-mail definido no **E-mail para suporte do usuário** > **Salvar e Continuar**
- Clique em **Salvar e Continuar** até chegar na etapa **Usuários de teste**, aqui você adiciona todos os usuários que terão acesso a usar a API, adicione seu e-mail e o e-mail de quem você quer autorizar a utilização clicando em **Add User**, após adicionar os usuários clique em **Salvar e Continuar**
- Clique no Menu > APIs e Serviços > Credenciais
- Clique em **Criar Credenciais** > **ID do cliente OAuth**
- Em **Tipo de aplicativo** selecione **App para computador** e defina um nome para a credencial
- Após criar irá abrir uma janela para você baixar o arquivo .json, salve este arquivo como **credentials.json** na pasta **Credential** da aplicação.

### 2️⃣Configuração na aplicação
Primeiro devemos configurar o arquivo **conf.json** que se encontra na pasta **config** na aplicação:
```
{
    "output_path": "local que vai ser salvo o arquivo",
    "sheets": [
        {
            "spreadsheet_id": "id da planilha",
            "range_name": "nome da sheet",
            "file_prefix": "nome para o arquivo"
        }
    ]
}
```
Nesta aplicação podemos baixar mais do que uma planilha, para adicionar novas planilhas você pode adicionar mais um conjunto dentro de "sheets" conforme exemplo abaixo:
```
{
    "output_path": "local que vai ser salvo o arquivo",
    "sheets": [
        {
            "spreadsheet_id": "id da planilha 1",
            "range_name": "nome da sheet 1",
            "file_prefix": "nome para o arquivo 1"
        },
        {
            "spreadsheet_id": "id da planilha 2",
            "range_name": "nome da sheet 2",
            "file_prefix": "nome para o arquivo 2"
        },
        {
            "spreadsheet_id": "id da planilha 3",
            "range_name": "nome da sheet 3",
            "file_prefix": "nome para o arquivo 3"
        }
    ]
}
```
Lembrando que todos os arquivos serão salvos na mesma pasta que é definida em **output_path**.

Após estas configurações só executar o **main.py**.

### 3️⃣Arquivo token.json

Após executar pela primeira vez a aplicação, irá abrir uma janela para logar na conta do gmail e validar o token, esta configuração só será feita um vez apenas quando houver o primeiro acesso, o e-mail que vai validar pode ser qualquer um que estiver na lista de credenciais definida nas configurações do Google Console, se depois de um tempo as bases pararem de baixar o motivo é que o token expirou, então vá na aplicação, exclua o arquivo token.json e rode a aplicação novamente, assim você terá que permitir novamente, até o momento com testes não foi verificado um prazo de expiração, foi testado durante 15 dias seguidos.

## Conecte-se comigo

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thiago-romualdo-732204244/)


