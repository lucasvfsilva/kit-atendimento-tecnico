# Mostra as configurações do PC e se ele atende aos requisitos mínimos.
# Uso: python info_pc.py
import platform
import shutil
from pathlib import Path

import psutil

GB = 1024 ** 3

ram = psutil.virtual_memory().total / GB
disco_livre = shutil.disk_usage(Path.home().anchor).free / GB  # C:\ no Windows, / no Mac e Linux
nucleos = psutil.cpu_count()

print("=== Configurações do PC ===")
print("Computador: ", platform.node())
print("Sistema:    ", platform.system(), platform.release())
print(f"RAM:         {ram:.1f} GB")
print(f"Disco livre: {disco_livre:.1f} GB")
print("Núcleos:    ", nucleos)

print("\n=== Requisitos mínimos ===")
print("RAM 8 GB:         ", "OK" if ram >= 8 else "NÃO ATENDE")
print("Disco livre 20 GB:", "OK" if disco_livre >= 20 else "NÃO ATENDE")
print("4 núcleos:        ", "OK" if nucleos >= 4 else "NÃO ATENDE")
