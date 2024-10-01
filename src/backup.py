import shutil
from datetime import datetime
from pathlib import Path

backup_dir = Path("meu_sistema_livraria/backups")
db_path = Path("meu_sistema_livraria/data/livraria.db")
backup_dir.mkdir(parents=True, exist_ok=True)

def criar_backup():
    backup_filename = f"backup_livraria_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.db"
    backup_path = backup_dir / backup_filename
    shutil.copy(db_path, backup_path)
    print(f"Backup criado: {backup_path}")

def limpar_backups_antigos():
    backups = sorted(backup_dir.glob("*.db"), key=lambda x: x.stat().st_mtime)
    if len(backups) > 5:
        for backup in backups[:-5]:
            backup.unlink()
            print(f"Backup removido: {backup}")
