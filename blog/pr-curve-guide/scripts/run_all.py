"""Regenerate every figure: python scripts/run_all.py"""
import runpy, sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
for f in sorted(here.glob("fig*.py")):
    print(f"--- {f.name}")
    runpy.run_path(str(f), run_name="__main__")
