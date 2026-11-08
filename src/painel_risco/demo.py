"""Dados totalmente sintéticos, determinísticos e não representativos."""
from __future__ import annotations
import argparse
from pathlib import Path
import random
import pandas as pd

def generate_demo(n: int = 160, seed: int = 42) -> pd.DataFrame:
    if n < 1:
        raise ValueError("n deve ser positivo")
    rng = random.Random(seed)
    base = pd.Timestamp("2024-01-01")
    rows = []
    for i in range(n):
        date = base + pd.Timedelta(days=rng.randint(0, 364))
        rows.append({
            "id": f"DEMO-{i + 1:05d}",
            "data": date.strftime("%Y-%m-%d"),
            "tipo_veiculo": rng.choice(["Automóvel", "Motocicleta", "Bicicleta", "Ônibus"]),
            "gravidade": rng.choices(["Sem vítimas", "Com vítimas", "Fatal"], weights=[75, 23, 2])[0],
            "latitude": round(-22.217 + rng.uniform(-0.025, 0.025), 6),
            "longitude": round(-49.950 + rng.uniform(-0.025, 0.025), 6),
        })
    return pd.DataFrame(rows)

def main() -> None:
    parser = argparse.ArgumentParser(description="Gera dados fictícios para demonstração")
    parser.add_argument("--output", default="data/demo_sintetico.csv")
    parser.add_argument("--rows", type=int, default=160)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    generate_demo(args.rows, args.seed).to_csv(target, index=False)
    print(f"Criado: {target} ({args.rows} registros sintéticos; seed={args.seed})")

if __name__ == "__main__":
    main()
