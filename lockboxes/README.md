# Lockboxes
Ce projet vérifie si toutes les boîtes peuvent être ouvertes.
## Principe
On commence avec la boîte `0`.
Chaque boîte contient des clés.
Une clé permet d'accéder à la boîte portant son numéro.
## Fonctionnement
- `n` : nombre total de boîtes.
- `unlocked` : boîtes déjà découvertes.
- `keys` : clés à examiner.
- `pop()` : prend une clé.
- `add()` : ajoute une boîte.
- `extend()` : ajoute les nouvelles clés.
Le programme répète ces étapes tant qu'il reste des clés.
À la fin, il vérifie si toutes les boîtes ont été découvertes.
```python
return len(unlocked) == n
```
`True` = toutes les boîtes sont accessibles.
`False` = au moins une boîte reste inaccessible.
## Exemple
```python
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))
# True
```
**À retenir :** clé → boîte → nouvelles clés → nouvelles boîtes.
