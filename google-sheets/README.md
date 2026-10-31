# 📊 Google Sheets: inventário de máquinas e painel

No Google Sheets ficam os **números**: os requisitos, as máquinas de cada cliente com o resultado do diagnóstico e um painel com o resumo. A mesma planilha também guarda o [CRM](../crm/).

---

## 🗂️ Abas da planilha

| Aba | Para que serve |
|---|---|
| **Requisitos** | Os mínimos exigidos pelo sistema |
| **Inventário** | Uma linha por máquina analisada, com ✅/❌ e o motivo |
| **Painel** | Resumo executivo: total, aptas, não aptas e gráfico |
| **Clientes** | O funil de vendas (explicado na pasta [`crm/`](../crm/)) |

Dica: importe o arquivo [`inventario.csv`](inventario.csv) em **Arquivo → Importar → Fazer upload → Inserir nova(s) página(s)** para já começar com dados de exemplo.

> ⚠️ Com o Sheets em português, as fórmulas usam nomes em português (`SE`, `CONT.SE`) e **ponto e vírgula `;`** entre os argumentos.

---

## 1. Aba **Requisitos**

| | A | B |
|---|---|---|
| 1 | **Requisito** | **Mínimo** |
| 2 | RAM (GB) | 8 |
| 3 | Disco livre (GB) | 20 |
| 4 | Núcleos | 4 |

---

## 2. Aba **Inventário**

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| Cliente | Máquina | RAM (GB) | Disco livre (GB) | Núcleos | Status | Motivo | Sistema | Data |

### Status automático (coluna F)

Para linhas digitadas à mão, cole em **F2** e arraste para baixo:

```
=SE(E(C2>=Requisitos!$B$2; D2>=Requisitos!$B$3; E2>=Requisitos!$B$4); "✅ Apto"; "❌ Não apto")
```

- `E(...)` só é verdadeiro se **todas** as condições forem verdadeiras.
- `Requisitos!$B$2` busca o valor na outra aba. O `$` trava a referência ao arrastar.

### Motivo (coluna G)

```
=SE(F2="✅ Apto"; "—"; TEXTJOIN(", "; VERDADEIRO; SE(C2<Requisitos!$B$2; "RAM insuficiente"; ""); SE(D2<Requisitos!$B$3; "Pouco disco"; ""); SE(E2<Requisitos!$B$4; "Poucos núcleos"; "")))
```

Assim a planilha não diz só "não apto": ela diz **por quê**. É isso que o time interno precisa para agir.

### Formatação condicional (destacar problemas em vermelho)

1. Selecione **C2:C**.
2. **Formatar → Formatação condicional → A fórmula personalizada é** → `=C2<Requisitos!$B$2`.
3. Fundo vermelho claro.
4. Repita para **D2:D** (`=D2<Requisitos!$B$3`) e **E2:E** (`=E2<Requisitos!$B$4`).

### Validação de dados (evitar erro de digitação)

Selecione **A2:A** → **Dados → Validação de dados → Menu suspenso (de um intervalo)** → `Clientes!A2:A`.
Assim o nome do cliente é escolhido numa lista, igual ao cadastrado no CRM.

---

## 3. Aba **Painel** (resumo executivo)

| | A | B |
|---|---|---|
| 1 | **Indicador** | **Valor** |
| 2 | Total de máquinas | `=CONT.VALORES(Inventário!B2:B)` |
| 3 | Máquinas aptas | `=CONT.SE(Inventário!F2:F; "✅ Apto")` |
| 4 | Máquinas não aptas | `=CONT.SE(Inventário!F2:F; "❌ Não apto")` |
| 5 | % aptas | `=SE(B2=0; 0; B3/B2)` (formatar como %) |

**Gráfico:** selecione **A3:B4** → **Inserir → Gráfico → Pizza**.

---

## 4. (Avançado) Envio automático a partir do Python

A [`versao-completa/`](../versao-completa/) tem um script que envia os relatórios dos clientes direto para a aba Inventário, usando o **Google Apps Script** ([`Codigo.gs`](../versao-completa/apps_script/Codigo.gs)):

1. Na planilha: **Extensões → Apps Script** → colar o `Codigo.gs` → salvar.
2. **Implantar → Nova implantação → App da Web** (Executar como: *Eu* · Acesso: *Qualquer pessoa*).
3. Copiar o link `/exec` e rodar no terminal:
   ```powershell
   $env:SHEETS_URL = "https://script.google.com/macros/s/SEU_LINK/exec"
   python diagnostico.py --importar recebidos
   ```

O link fica numa variável de ambiente, **fora do código e fora do GitHub**, e o Apps Script só permite **adicionar linhas**.

---

## ✅ Checklist para o portfólio

- [ ] Prints: aba Inventário com cores, aba Painel com gráfico
- [ ] Compartilhar → **Qualquer pessoa com o link → Leitor** → colocar o link no README principal
