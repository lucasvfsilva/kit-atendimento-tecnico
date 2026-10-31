# 📘 Notion: documentação e relacionamento com o cliente

No Notion ficam os **textos**: o guia que o cliente lê, a página de cada cliente com o diagnóstico explicado, as atas de reunião e os tutoriais. Os números (inventário e funil) ficam no [Google Sheets](../google-sheets/).

---

## 🗂️ Estrutura do workspace

```
🏢 Portal de Atendimento                    (interno 🔒)
├── 📇 Clientes                             banco de dados — uma página por cliente
│     └── Clínica Vida Saudável
│           ├── Resultado do diagnóstico    (requisitos dos PCs dela)
│           └── Atas de reunião
├── 📋 Reuniões e Atas                      banco de dados ligado a Clientes
├── 📚 Tutoriais                            banco de dados
│     └── 📘 Guia de Diagnóstico Técnico   ← única página publicada 🌐
└── 📄 Modelos (ata, diagnóstico)
```

O cliente **só vê o Guia**. Atas e dados de outros clientes ficam na área interna.

---

## 1. Banco de dados **Clientes**

Dica: importe o arquivo [`clientes.csv`](clientes.csv) em **Importar → CSV** para criar o banco já preenchido.

| Coluna | Tipo | Exemplo |
|---|---|---|
| Nome | Título | Clínica Vida Saudável |
| Segmento | Seleção | Clínica / Varejo / Indústria |
| Situação técnica | Status | Em diagnóstico / Apto / Precisa de upgrade |
| Contato | Texto | Dra. Ana — (84) 9 9999-0000 |
| Responsável | Pessoa | Você |
| Reuniões | Relação → Reuniões e Atas | |

### Dentro da página de cada cliente: o diagnóstico

Cole este modelo e preencha com o resultado do `info_pc.py`:

```
## 🖥️ Diagnóstico dos computadores
Data: 03/11/2026 · Requisitos: RAM 8 GB · Disco livre 20 GB · 4 núcleos

| Máquina        | RAM   | Disco livre | Núcleos | Resultado        |
|----------------|-------|-------------|---------|------------------|
| Recepção-01    | 4 GB  | 50 GB       | 2       | ❌ RAM e núcleos |
| Consultório-02 | 16 GB | 120 GB      | 8       | ✅ Apto          |

## 📌 Recomendação
Recepção-01 precisa de upgrade de RAM (mínimo 8 GB) antes da implantação.
```

---

## 2. Banco de dados **Reuniões e Atas**

| Coluna | Tipo |
|---|---|
| Nome | Título — ex.: "Diagnóstico inicial" |
| Data | Data |
| Tipo | Seleção — Diagnóstico / Apresentação / Suporte / Evento |
| Cliente | Relação → Clientes (ativar "mostrar em Clientes") |

### Modelo de ata (criar em **Novo → + Novo modelo**)

```
## 🎯 Objetivo da reunião

## 🖥️ Ecossistema do cliente
| Item                | Situação atual | Atende? |
|---------------------|----------------|---------|
| Computadores        |                |         |
| Sistema operacional |                |         |
| Rede / Internet     |                |         |
| Equipamentos        |                |         |

## 😣 Dores relatadas pelo cliente
-

## 🔧 Requisitos para o time interno
- [ ]

## ✅ Próximos passos
- [ ] Ação — Responsável — Prazo
```

Esse modelo cobre três tarefas de uma vez: **mapear o ecossistema**, **ouvir as dores** e **traduzir em requisitos** para o time de desenvolvimento.

---

## 3. 🌐 Guia de Diagnóstico Técnico (página pública para o cliente)

Texto pronto para colar no Notion:

> ### 👋 Por que fazer o diagnóstico?
> Antes de instalar o sistema, verificamos se seus computadores têm o mínimo necessário. Isso evita lentidão e problemas depois da implantação.
>
> ### 🖥️ Requisitos mínimos
> | Item | Mínimo |
> |---|---|
> | Memória RAM | 8 GB |
> | Espaço livre em disco | 20 GB |
> | Processador | 4 núcleos |
>
> ### ▶️ Como fazer
> 1. Abra o programa de diagnóstico que enviamos.
> 2. Veja o resultado na tela: cada item aparece como **OK** ou **NÃO ATENDE**.
> 3. Tire um print da tela e envie para o seu consultor.
>
> ### 🔒 Seus dados estão seguros
> O programa **não envia nada pela internet**. Ele só lê informações técnicas (memória, disco e processador) e mostra na sua tela. Você decide o que compartilhar.
>
> ### ❓ Perguntas frequentes
> **Meu computador deu "NÃO ATENDE". E agora?**
> Não se preocupe: na maioria dos casos dá para resolver com um ajuste simples, como liberar espaço ou aumentar a memória. Vamos te orientar.
>
> **Como liberar espaço em disco?**
> Abra **Configurações → Sistema → Armazenamento** e use a **Limpeza recomendada**. Também ajuda esvaziar a Lixeira e a pasta Downloads.
>
> **Preciso fazer em todos os computadores?**
> Sim, em todos que vão usar o sistema.
>
> ### 📞 Dúvidas?
> Fale com seu consultor: *seu nome — e-mail — telefone*

**Para publicar:** Compartilhar → **Publicar** → ative **Permitir duplicar como modelo** → copie o link.

---

## 4. 🗣️ Como explicar o resultado para o cliente

Roteiro para a conversa depois do diagnóstico:

**Se está tudo apto ✅**
> "Boa notícia: todos os computadores atendem aos requisitos. Podemos seguir para a implantação. O próximo passo é agendar a instalação. Qual dia funciona melhor para vocês?"

**Se alguma máquina não atende ❌**
1. **Comece pelo positivo:** "Das 5 máquinas, 4 já estão prontas."
2. **Explique sem termo técnico:** "A máquina da recepção tem pouca memória. É como uma mesa pequena demais para trabalhar com várias pastas abertas: o sistema ficaria lento."
3. **Mostre o caminho:** "Dá para resolver com um aumento de memória, que é uma peça simples de trocar."
4. **Combine o próximo passo:** "Posso te enviar um orçamento até sexta?"
5. **Registre:** ata no Notion + próxima ação no [CRM](../crm/).

---

## ✅ Checklist para o portfólio

- [ ] Prints: banco Clientes, página de um cliente com diagnóstico, uma ata preenchida
- [ ] GIF criando uma ata pelo modelo
- [ ] Link público do Guia no README principal
