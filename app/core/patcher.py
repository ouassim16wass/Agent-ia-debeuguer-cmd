from pathlib import Path
from typing import List, Dict, Any

def apply_patches(file_path, patches: List[Dict[str, Any]]):
    """
    Applique une liste de patchs sur un fichier source.
    Chaque patch :
      - start_line (int, 1-based)
      - end_line (int, 1-based, inclus)
      - replacement (liste de lignes de code SANS \n)
    """
    file = Path(file_path)
    lines = file.read_text(encoding="utf-8").splitlines()

    # Appliquer du bas vers le haut pour éviter les décalages d'indice
    patches_sorted = sorted(patches, key=lambda p: p["start_line"], reverse=True)

    for patch in patches_sorted:
        start = patch["start_line"] - 1
        end = patch["end_line"]
        replacement = patch["replacement"]

        lines[start:end] = replacement

    file.write_text("\n".join(lines), encoding="utf-8")
