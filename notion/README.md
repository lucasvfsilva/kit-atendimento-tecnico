# 📘 Notion: resumo do atendimento

Uma página organizada com o **resumo executivo**, a **situação das máquinas**, a **planilha incorporada** e os **próximos passos**. É o que eu enviaria para o cliente e para o time interno depois do diagnóstico.

---

## Passo a passo

**1.** Acesse **notion.so** → **+ Nova página** → título: **Clínica Vida – Resumo do Atendimento**. Adicione um ícone, como 🏥.

**2.** Monte a página com os blocos abaixo. Digite **`/`** para inserir cada tipo de bloco:

```
## 📋 Resumo executivo                        (/heading 2)
Diagnóstico de 3 computadores em 03/11/2026.
1 de 3 máquinas atende aos requisitos. Recomendado upgrade antes da implantação.

## 🖥️ Situação das máquinas                    (/tabela)
| Máquina       | Status       | Problema              |
| Recepção      | ❌ Não apto   | RAM 4 GB, 2 núcleos    |
| Consultório 1 | ✅ Apto       | —                     |
| Consultório 2 | ❌ Não apto   | Só 12 GB livres        |

## 📊 Planilha completa                         (/embed → cole o link do Google Sheets)

## ✅ Próximos passos                           (/todo)
☐ Enviar orçamento de upgrade de RAM — até 07/11
☐ Orientar limpeza de disco no Consultório 2
☐ Agendar implantação após os ajustes
```

### Sobre o `/embed`

Ele faz a planilha do Google Sheets **aparecer dentro do Notion**, mostrando que as ferramentas se conversam.
Para funcionar, a planilha precisa estar compartilhada como **"Qualquer pessoa com o link → Leitor"** (veja [google-sheets](../google-sheets/)).

---

## Publicar

**Compartilhar → Publicar → Publicar** → copie o link e coloque no README principal.

---

## Por que essa estrutura

| Bloco | Para quem | Responde |
|---|---|---|
| Resumo executivo | Gestor / cliente | "Qual é a situação?" em 2 linhas |
| Situação das máquinas | Cliente / técnico | "O que exatamente está errado?" |
| Planilha incorporada | Time interno | "Onde estão os números?" |
| Próximos passos | Todos | "O que acontece agora e quando?" |
