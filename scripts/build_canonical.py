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
lines.append(
    "## Ressources du projet\n\n"
    "- [Site du référentiel](https://mcere.github.io/Referentiel-documentaire/)\n"
    "- [Dépôt GitHub](https://github.com/mcere/Referentiel-documentaire)\n"
    "- [README](https://github.com/mcere/Referentiel-documentaire/blob/main/README.md)\n"
    "- [CHANGELOG](https://github.com/mcere/Referentiel-documentaire/blob/main/CHANGELOG.md)\n"
    "- [VERSION](https://github.com/mcere/Referentiel-documentaire/blob/main/VERSION.md)\n"
    "- [LICENCE](https://github.com/mcere/Referentiel-documentaire/blob/main/LICENCE)\n"
)

lines.append(
    "Ces documents ne font pas partie du référentiel normatif "
    "mais constituent la documentation officielle du projet.\n\n"
)

lines.append("\n\n# MANIFESTE\n\n")

lines.append(
    (ROOT / "MANIFEST.md").read_text(
        encoding="utf-8"
    )
)

lines.append("\n\n# DOCUMENTS DU RÉFÉRENTIEL\n\n")

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

latest_file = (
    COMPILED /
    "Referentiel-documentaire-canonique-latest.md"
)

latest_file.write_text(
    "".join(lines),
    encoding="utf-8"
)

print(f"Generated: {output_file}")
print(f"Generated: {latest_file}")
