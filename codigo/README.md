# 🔍 Como verificar os requisitos no PC do cliente

Três formas, da mais simples para a mais completa. Os requisitos mínimos são: **8 GB de RAM**, **20 GB livres em disco** e **4 núcleos**.

| Arquivo | O que é |
|---|---|
| [`info_pc.py`](info_pc.py) | Script Python que mostra as configurações e compara com os requisitos |
| [`lembrete.gs`](lembrete.gs) | Apps Script que envia e-mail diário com os follow-ups do [CRM](../crm/) |

---

## 🪟 Windows: atalhos do sistema, sem instalar nada

| Atalho | O que mostra |
|---|---|
| **Win + Pause/Break** (ou **Win + X → Sistema**) | Processador, **RAM instalada** e versão do Windows |
| **Ctrl + Shift + Esc** → aba **Desempenho** | **CPU** (núcleos e processadores lógicos), **Memória** e **Disco**, tudo num lugar só ⭐ |
| **Win + E** → **Este Computador** | **Espaço livre** de cada disco |
| **Win + R** → `msinfo32` | Relatório completo do sistema |
| **Win + R** → `winver` | Versão exata do Windows |

## 🪟 Windows: terminal, com um comando só

Abra o PowerShell (**Win + X → Terminal**) e cole:

```powershell
"Sistema: " + (Get-CimInstance Win32_OperatingSystem).Caption; "RAM: {0:N1} GB" -f ((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB); "Disco livre (C:): {0:N1} GB" -f ((Get-PSDrive C).Free/1GB); "Nucleos: " + (Get-CimInstance Win32_Processor).NumberOfLogicalProcessors
```

Exemplo de saída:

```
Sistema: Microsoft Windows 11 Pro
RAM: 15,4 GB
Disco livre (C:): 12,1 GB
Nucleos: 12
```

Alternativa mais curta, mas com informação demais na tela: `systeminfo`

---

## 🍎 Mac

**Sem terminal:** menu  → **Sobre este Mac** mostra o chip/processador, a memória e a versão. Para o espaço livre: **Ajustes do Sistema → Geral → Armazenamento**.

**No Terminal** (Cmd + Espaço → "Terminal"):

```bash
sw_vers -productVersion                                    # versão do macOS
echo "$(( $(sysctl -n hw.memsize) / 1073741824 )) GB RAM"  # memória
sysctl -n hw.ncpu                                          # núcleos
df -h /                                                    # disco (coluna "Avail" = livre)
```

---

## 🐧 Linux

**Sem terminal:** **Configurações → Sobre** (o nome muda um pouco conforme a distribuição).

**No Terminal** (Ctrl + Alt + T):

```bash
grep PRETTY_NAME /etc/os-release   # sistema
free -h                            # memória (linha "Mem", coluna "total")
nproc                              # núcleos
df -h /                            # disco (coluna "Disp." ou "Avail" = livre)
```

---

## 🐍 Qualquer sistema: o script `info_pc.py`

```bash
pip install psutil
python info_pc.py
```

```
=== Configurações do PC ===
Computador:  DESKTOP-FU4L3HL
Sistema:     Windows 11
RAM:         15.4 GB
Disco livre: 12.1 GB
Núcleos:     12

=== Requisitos mínimos ===
RAM 8 GB:          OK
Disco livre 20 GB: NÃO ATENDE
4 núcleos:         OK
```

Funciona em **Windows, Mac e Linux** e **não envia nenhum dado pela internet**.

---

## Quando usar cada um

| Situação | Melhor opção |
|---|---|
| Olhar rápido uma máquina, com o cliente do lado | **Ctrl + Shift + Esc → Desempenho** |
| Copiar os dados para a planilha | **Comando do PowerShell** (já sai formatado) |
| Várias máquinas ou sistemas diferentes | **`info_pc.py`** (mesmo resultado em qualquer sistema) |

Os dados coletados vão para a aba **Máquinas** do [Google Sheets](../google-sheets/).
