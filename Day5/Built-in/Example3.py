from pathlib import Path

p = Path('Even.py')
print(p.exists())
print(p.parent)
d = Path('test_dir')
d.mkdir(exist_ok=True)
d.rmdir()