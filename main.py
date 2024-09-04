import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime
import argparse
import logging
import pandas as pd
import json

enable_venv = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'.venv\Scripts\activate_this.py')
exec(open(enable_venv).read(), {'__file__': enable_venv})

# Se modificar esses escopos, delete o arquivo token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def load_config(json_path):
    """Carrega as configurações do arquivo JSON."""
    with open(json_path, 'r') as file:
        config = json.load(file)
    return config

def download_sheet(spreadsheet_id, range_name, output_path, file_prefix, service):
    """Baixa e salva uma planilha como CSV."""
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()
        values = result.get('values', [])
        
        if not values:
            logging.warning(f"Não foram encontrados dados na planilha com ID {spreadsheet_id}.")
            return

        # Define o caminho completo do arquivo CSV
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        file_name = file_prefix +'_'+ datetime.now().strftime("%Y%m%d") + '.csv'
        caminho_completo = os.path.join(output_path, file_name)

        df = pd.DataFrame(values[1:], columns=values[0])  # Assume que a primeira linha é o cabeçalho
        df.to_csv(caminho_completo, index=False, encoding='utf-8-sig')
        logging.info(f'Arquivo CSV salvo como "{caminho_completo}".')
    except Exception as e:
        logging.error(f"Erro ao baixar a planilha: {e}")

def main(json_path):
    """Função principal para execução do script."""
    config = load_config(json_path)

    output_path = config.get("output_path", ".")
    
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    
    for sheet_config in config.get("sheets", []):
            file_prefix = sheet_config.get("file_prefix", "")
            download_sheet(sheet_config["spreadsheet_id"],
                           sheet_config["range_name"],
                           output_path,
                           file_prefix,
                           service)

if __name__ == "__main__":
    json_path = 'config/config.json'  # Altere para o caminho do seu arquivo JSON
    main(json_path)
