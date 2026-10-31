# 📊 Google Sheets: aba Máquinas

Registro dos computadores do cliente com **status automático** (apto / não apto), **cores** e uma **linha de resumo**.

> ⚠️ Com o Sheets em português, as fórmulas usam nomes em português (`SE`, `CONT.SE`) e **ponto e vírgula `;`** entre os argumentos.

---

## Passo a passo

**1.** Acesse **sheets.google.com** → **Em branco** → dê o nome **Atendimento – Clientes**.

**2.** Renomeie a aba de baixo para **Máquinas** e preencha:

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Cliente** | **Máquina** | **Sistema** | **RAM (GB)** | **Disco livre (GB)** | **Núcleos** | **Status** |
| 2 | Clínica Vida | Recepção | Windows 10 | 4 | 50 | 2 | |
| 3 | Clínica Vida | Consultório 1 | Windows 11 | 16 | 120 | 8 | |
| 4 | Clínica Vida | Consultório 2 | Windows 11 | 8 | 12 | 4 | |

**3.** Em **G2**, cole a fórmula e arraste até **G4**:

```
=SE(E(D2>=8; E2>=20; F2>=4); "✅ Apto"; "❌ Não apto")
```

Ela verifica se a máquina tem RAM de 8 GB ou mais, **e** disco livre de 20 GB ou mais, **e** 4 núcleos ou mais.

**4. Cores automáticas:** selecione a coluna **G** → **Formatar → Formatação condicional**:
- *"O texto contém"* `Não` → fundo **vermelho**
- **Adicionar outra regra** → *"O texto contém"* `Apto` → fundo **verde**

**5. Linha de resumo**, abaixo da tabela:
- **A6:** `Máquinas aptas:`
- **B6:**
  ```
  =CONT.SE(G2:G4; "✅ Apto") & " de " & CONT.VALORES(B2:B4)
  ```
  Resultado: **1 de 3**.

---

## Resultado esperado

| Máquina | Status | Por quê |
|---|---|---|
| Recepção | ❌ Não apto | RAM 4 GB e só 2 núcleos |
| Consultório 1 | ✅ Apto | — |
| Consultório 2 | ❌ Não apto | Só 12 GB livres em disco |

---

## Compartilhar

**Compartilhar → Acesso geral → Qualquer pessoa com o link → Leitor** → copiar o link.
Esse link vai no README principal e na página do [Notion](../notion/).

**Próximo passo:** a aba **Clientes**, que funciona como [CRM](../crm/).
