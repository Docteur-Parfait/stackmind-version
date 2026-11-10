# Construit manifest.json pour les données distantes du jeu (dossier de fichiers JSON).
# Usage : python tools/content_manifest.py [dossier] [--min-app 1.6.0]
#   dossier par défaut : data/content (copie intégrée au jeu). Dans le dépôt de contenu : « . ».
# Vérifie que chaque fichier est un JSON valide, calcule son SHA-256 et augmente le numéro de version.
# Le jeu ne télécharge un fichier que si son empreinte a changé, et refuse un fichier qui ne correspond
# pas à l'empreinte du manifeste.
import hashlib, json, os, sys

SCHEMA = 1
FILES = ["economy", "skins", "skies", "fx", "modes", "weekly", "missions", "sky_keys", "ais", "strings"]

args = [a for a in sys.argv[1:] if not a.startswith("--")]
root = os.path.abspath(args[0] if args else os.path.join(os.path.dirname(__file__), "..", "data", "content"))
min_app = "1.6.0"
if "--min-app" in sys.argv:
    min_app = sys.argv[sys.argv.index("--min-app") + 1]

path = os.path.join(root, "manifest.json")
old = {}
if os.path.exists(path):
    with open(path, encoding="utf-8") as f:
        old = json.load(f)

files = {}
for name in FILES:
    p = os.path.join(root, name + ".json")
    with open(p, "rb") as f:
        raw = f.read()
    json.loads(raw.decode("utf-8"))   # erreur claire si le JSON est cassé
    files[name] = hashlib.sha256(raw).hexdigest()

version = int(old.get("version", 0))
if files != old.get("files") or min_app != old.get("min_app"):
    version += 1

manifest = {"schema": SCHEMA, "version": version, "min_app": min_app, "files": files}
with open(path, "w", encoding="utf-8", newline="\n") as f:
    json.dump(manifest, f, indent="\t")
    f.write("\n")
print(f"manifest version {version} ({len(files)} fichiers) -> {path}")
