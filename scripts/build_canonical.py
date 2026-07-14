from pathlib import Path
import re

ROOT = Path(".")
COMPILED = ROOT / "compiled"
COMPILED.mkdir(exist_ok=True)

VERSION = (
    ROOT / "VERSION.md"
).read_text(
    encoding="utf-8"
).strip()

MANIFEST_CONTENT = (
    ROOT / "MANIFEST.md"
).read_text(
    encoding="utf-8"
)

OUTPUT_FILE = (
    COMPILED /
    f"Referentiel-documentaire-canonique-{VERSION}.md"
)

LATEST_FILE = (
    COMPILED /
    "Referentiel-documentaire-canonique-latest.md"
)

lines = []

# En-tête

lines.append("# Référentiel documentaire compilé\n\n")
lines.append(f"Version : {VERSION}\n\n")

# Contenu du manifeste

lines.append("## MANIFESTE\n\n")
lines.append(MANIFEST_CONTENT)
lines.append("\n\n")

# Recherche automatique de tous les fichiers .md
# référencés dans le manifeste

files = re.findall(
    r"((?:docs|annexes)/[^\n]+\.md)",
    MANIFEST_CONTENT
)

# Suppression des doublons tout en conservant l'ordre

seen = set()
ordered_files = []

for file_path in files:
    if file_path not in seen:
        seen.add(file_path)
        ordered_files.append(file_path)

lines.append("## DOCUMENTS DU RÉFÉRENTIEL\n\n")

# Compilation

for file_path in ordered_files:

    p = ROOT / file_path

    if not p.exists():
        lines.append(
            f"\n\n## DOCUMENT MANQUANT : {file_path}\n\n"
        )
        continue

    lines.append(
        f"\n\n## Source : {file_path}\n\n"
    )

    lines.append(
        p.read_text(
            encoding="utf-8"
        )
    )

    lines.append("\n\n")

# Version numérotée

compiled_content = "".join(lines)

OUTPUT_FILE.write_text(
    compiled_content,
    encoding="utf-8"
)

# Version latest

LATEST_FILE.write_text(
    compiled_content,
    encoding="utf-8"
)

print(f"Generated: {OUTPUT_FILE}")
print(f"Generated: {LATEST_FILE}")
