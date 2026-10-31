"""Diagnóstico Técnico: verifica se o computador atende aos requisitos do sistema.

Cliente:  python diagnostico.py
    Abre uma janela com as configurações do PC e mostra se ele é compatível.
    Nada é enviado pela internet: o cliente decide se salva e compartilha o relatório.

Empresa:  python diagnostico.py --importar PASTA_OU_ARQUIVOS
    Envia os relatórios .json recebidos dos clientes para o Google Sheets.
    Precisa da variável de ambiente SHEETS_URL com o link do Apps Script.
"""
import argparse
import json
import os
import platform
import shutil
import socket
import sys
import tkinter as tk
import urllib.request
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import psutil

GB = 1024 ** 3

# Requisitos mínimos do sistema: campo do inventário -> (nome na tela, mínimo)
REQUISITOS = {
    "ram_total_gb": ("Memória RAM (GB)", 8),
    "disco_livre_gb": ("Disco livre (GB)", 20),
    "nucleos_logicos": ("Núcleos do processador", 4),
}


# ---------- Coleta e validação ----------

def coletar():
    disco = shutil.disk_usage(Path.home().anchor)
    return {
        "coletado_em": datetime.now().isoformat(timespec="seconds"),
        "maquina": socket.gethostname(),
        "sistema": f"{platform.system()} {platform.release()}",
        "arquitetura": platform.machine(),
        "processador": platform.processor(),
        "nucleos_logicos": psutil.cpu_count(logical=True),
        "ram_total_gb": round(psutil.virtual_memory().total / GB, 1),
        "disco_total_gb": round(disco.total / GB, 1),
        "disco_livre_gb": round(disco.free / GB, 1),
    }


def validar(inventario):
    itens = []
    for campo, (nome, minimo) in REQUISITOS.items():
        valor = inventario[campo]
        itens.append({"nome": nome, "valor": valor, "minimo": minimo, "ok": valor >= minimo})

    falhas = [f"{i['nome']}: {i['valor']} (mínimo {i['minimo']})" for i in itens if not i["ok"]]
    return {
        "apto": not falhas,
        "status": "✅ Apto" if not falhas else "❌ Não apto",
        "motivo": "; ".join(falhas) or "—",
        "itens": itens,
    }


def salvar_relatorio(pasta, cliente, inventario, resultado):
    """Salva .md (para o cliente ler) e .json (para a empresa importar)."""
    base = Path(pasta) / f"{inventario['coletado_em'][:10]}_{cliente}_{inventario['maquina']}".replace(" ", "-")

    linhas = "\n".join(
        f"| {i['nome']} | {i['valor']} | {i['minimo']} | {'✅' if i['ok'] else '❌'} |"
        for i in resultado["itens"]
    )
    base.with_suffix(".md").write_text(f"""# Diagnóstico técnico: {cliente}

**Máquina:** {inventario['maquina']} · **Sistema:** {inventario['sistema']} · **Data:** {inventario['coletado_em']}

## Resultado: {resultado['status']}

| Requisito | Valor | Mínimo | Atende? |
|---|---|---|---|
{linhas}
""", encoding="utf-8")

    base.with_suffix(".json").write_text(
        json.dumps({"cliente": cliente, "inventario": inventario}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return base


# ---------- Janela do cliente ----------

class Janela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diagnóstico Técnico")
        self.geometry("560x440")
        self.inventario = None
        self.resultado = None

        quadro = ttk.Frame(self, padding=16)
        quadro.pack(fill="both", expand=True)

        ttk.Label(quadro, text="Diagnóstico Técnico", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(
            quadro,
            text="Este programa não envia nenhum dado. Você vê o resultado e decide se compartilha.",
            foreground="gray",
        ).pack(anchor="w", pady=(0, 12))

        linha = ttk.Frame(quadro)
        linha.pack(fill="x")
        ttk.Label(linha, text="Empresa:").pack(side="left")
        self.campo_cliente = ttk.Entry(linha)
        self.campo_cliente.pack(side="left", fill="x", expand=True, padx=8)
        ttk.Button(linha, text="▶ Iniciar diagnóstico", command=self.diagnosticar).pack(side="left")

        self.tabela = ttk.Treeview(quadro, columns=("valor", "situacao"), height=7)
        self.tabela.heading("#0", text="Item")
        self.tabela.heading("valor", text="Valor")
        self.tabela.heading("situacao", text="Situação")
        self.tabela.column("#0", width=170)
        self.tabela.column("valor", width=220)
        self.tabela.column("situacao", width=120)
        self.tabela.pack(fill="both", expand=True, pady=12)

        self.rotulo_resultado = ttk.Label(quadro, font=("Segoe UI", 12, "bold"), wraplength=520)
        self.rotulo_resultado.pack(anchor="w")

        self.botao_salvar = ttk.Button(quadro, text="💾 Salvar relatório", command=self.salvar, state="disabled")
        self.botao_salvar.pack(anchor="e", pady=(12, 0))

    def diagnosticar(self):
        self.inventario = coletar()
        self.resultado = validar(self.inventario)

        self.tabela.delete(*self.tabela.get_children())
        self.tabela.insert("", "end", text="Sistema", values=(self.inventario["sistema"], ""))
        self.tabela.insert("", "end", text="Processador", values=(self.inventario["processador"], ""))
        for item in self.resultado["itens"]:
            situacao = "✅ OK" if item["ok"] else f"❌ mín. {item['minimo']}"
            self.tabela.insert("", "end", text=item["nome"], values=(item["valor"], situacao))

        texto = f"Resultado: {self.resultado['status']}"
        if not self.resultado["apto"]:
            texto += f"\n{self.resultado['motivo']}"
        self.rotulo_resultado.config(text=texto)
        self.botao_salvar.config(state="normal")

    def salvar(self):
        cliente = self.campo_cliente.get().strip()
        if not cliente:
            messagebox.showwarning("Diagnóstico", "Digite o nome da empresa antes de salvar.")
            return
        pasta = filedialog.askdirectory(title="Onde salvar o relatório?", initialdir=Path.home() / "Desktop")
        if not pasta:
            return
        base = salvar_relatorio(pasta, cliente, self.inventario, self.resultado)
        messagebox.showinfo(
            "Relatório salvo",
            f"Arquivos salvos em {pasta}:\n\n{base.name}.md\n{base.name}.json\n\n"
            "Se quiser, envie o arquivo .json para o seu consultor.",
        )


# ---------- Importação (lado da empresa) ----------

def importar(caminhos):
    url = os.environ.get("SHEETS_URL")
    if not url:
        print("Defina a variável de ambiente SHEETS_URL com o link do Apps Script.")
        return 1

    arquivos = [a for c in caminhos for a in (sorted(c.glob("*.json")) if c.is_dir() else [c])]
    for arquivo in arquivos:
        dados = json.loads(arquivo.read_text(encoding="utf-8"))
        inventario = dados["inventario"]
        # Recalcula aqui: usa os requisitos atuais e não depende do que veio no arquivo
        resultado = validar(inventario)
        linha = {**inventario, "cliente": dados["cliente"],
                 "status": resultado["status"], "motivo": resultado["motivo"]}

        requisicao = urllib.request.Request(
            url, data=json.dumps(linha).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST",
        )
        urllib.request.urlopen(requisicao, timeout=30).close()
        print(f"{arquivo.name}: {resultado['status']} → enviado para a planilha")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Diagnóstico técnico do computador")
    parser.add_argument("--importar", nargs="+", type=Path, metavar="CAMINHO",
                        help="(empresa) envia relatórios .json para o Google Sheets")
    args = parser.parse_args()

    if args.importar:
        sys.stdout.reconfigure(encoding="utf-8")  # terminal do Windows não mostra emojis por padrão
        return importar(args.importar)
    Janela().mainloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
