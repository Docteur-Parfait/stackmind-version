# Contenu modifiable de StackMind AI

Ces fichiers JSON décrivent tout ce qui peut changer sans nouvelle version du jeu : boutique, ciels, effets,
modes, défi de la semaine, missions, économie, IA à collectionner et leurs noms. Ce dossier est la copie
intégrée au jeu ; la même arborescence est publiée sur GitHub Pages, et le jeu télécharge la version la
plus récente en arrière-plan (`scripts/content_sync.gd`). Elle s'applique au lancement suivant.

Un fichier ne contient que des **données** : il combine ce qui existe déjà dans le jeu (formes d'emblème,
décors, météos, icônes de mode). Rien n'y est exécuté.

## Publier une mise à jour

1. Modifier les fichiers JSON.
2. `python content_manifest.py .` (dans ce dépôt) : vérifie chaque fichier, recalcule les empreintes
   SHA-256 et augmente `version` dans `manifest.json`.
3. Pousser le dossier sur le dépôt de contenu.

Le jeu refuse une mise à jour si un fichier manque, si une empreinte ne correspond pas, si un champ
indispensable manque ou si `min_app` est plus récent que la version installée. Il garde alors la
version précédente.

## Fichiers

| Fichier | Contenu |
|---|---|
| `manifest.json` | `schema` (1), `version`, `min_app`, empreinte de chaque fichier |
| `economy.json` | pièces par étage et par parfait, prix et durée du « continuer », cadeaux du jour (7 jours), pénalité du contre-la-montre, `gameplay` (vitesses, tolérance…), `rarities` (ordre, couleurs, étage minimal, poids, lueur) |
| `skins.json` | tours : `id`, `price`, `hue`, `step`, `sat`, `val` (+ `sat0`, `val1`, `name`) |
| `skies.json` | ciels : `id`, `price`, `col`, `fixed`, `offset` |
| `fx.json` | effets : `id`, `price`, `col`, `amount`, `ramp` |
| `modes.json` | modes : `id`, `price`, `icon`, `col`, `speed`, `ramp`, `base`, `tol`, `coins` |
| `weekly.json` | réglages du défi de la semaine (un par semaine, en boucle) |
| `missions.json` | missions : `id`, `kind`, `goal`, `reward` |
| `sky_keys.json` | dégradé du ciel selon la hauteur (`h`) |
| `ais.json` | les IA, dans l'ordre : `rarity`, `shape` (forme d'emblème existante) |
| `strings.json` | noms et descriptions en `en` et `fr` (`SKIN_<id>`, `SKY_<id>`, `FX_<id>`, `MODE_<id>`, `MODE_DESC_<id>`, `WEEK_*`, `AI_NAME_xx`, `AI_TAG_xx`, `RARITY_*`) |

Les couleurs s'écrivent `"#rrggbb"`. Le premier élément de `skins`, `fx` et `modes` doit rester
`classique`, et celui de `skies` doit rester `auto` : ce sont les éléments gratuits de départ.
