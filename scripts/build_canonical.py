from pathlib import Path
import re

ROOT = Path(".")
COMPILED = ROOT / "compiled"
COMPILED.mkdir(exist_ok=True)

version = (ROOT / "VERSION.md").read_text(
    encoding="utf-8"
).strip()

manifest = (ROOT / "MANIFEST.md").read_text(
    encoding="utf-8"
)

output_file = (
    COMPILED /
    f"Referentiel-documentaire-canonique-{version}.md"
)

lines = []

lines.append("# Référentiel documentaire compilé\n")
lines.append(f"Version : {version}\n\n")

lines.append("---\n\n")

lines.append(
    (ROOT / "MANIFEST.md").read_text(
        encoding="utf-8"
    )
)

lines.append("\n\n---\n\n")

files = re.findall(
    r"(docs/[A-Z]\.md|annexes/Annexe\s+[A-Z]\.md)",
    manifest
)

for file_path in files:

    p = ROOT / file_path

    if not p.exists():
        lines.append(
            f"\n\n# DOCUMENT MANQUANT : {file_path}\n\n"
        )
        continue

    lines.append(
        f"\n\n# Source : {file_path}\n\n"
    )

    lines.append(
        p.read_text(encoding="utf-8")
    )

    lines.append("\n\n")

output_file.write_text(
    "".join(lines),
    encoding="utf-8"
)

print(f"Generated: {output_file}")
