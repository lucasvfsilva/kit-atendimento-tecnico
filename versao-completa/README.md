# 🧩 Versão completa: janela gráfica + integração com Google Sheets

Evolução do [`info_pc.py`](../info_pc.py) com dois modos no mesmo arquivo:

| Modo | Comando | O que faz |
|---|---|---|
| **Cliente** | `python diagnostico.py` | Abre uma janela com as configurações do PC e o resultado. Pode salvar o relatório (.md e .json). **Não envia nada pela internet.** |
| **Empresa** | `python diagnostico.py --importar recebidos` | Envia os relatórios .json recebidos dos clientes para a aba Inventário do Google Sheets |

## Como funciona o envio

```
Cliente: abre o programa → vê o resultado → salva o .json → envia ao consultor (se quiser)
Empresa: coloca o .json em "recebidos/" → roda --importar → linha nova na planilha
```

- O link da planilha fica na variável de ambiente `SHEETS_URL`, **nunca no código**.
- O [`apps_script/Codigo.gs`](apps_script/Codigo.gs) fica dentro da planilha e só permite **adicionar linhas**.
- Ao importar, o resultado é **recalculado**: não depende do que veio no arquivo.

Passo a passo da configuração: [google-sheets/README.md](../google-sheets/README.md#4-avançado-envio-automático-a-partir-do-python).

## Requisitos

```bash
pip install psutil
```
