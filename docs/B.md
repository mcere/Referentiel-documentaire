# B Sélection et application des directives
## Édition canonique candidate

### B.1 Objectif

Déterminer quelles directives doivent être appliquées à une demande donnée et dans quel ordre elles doivent être exécutées.

---

### B.2 Principe général

Chaque demande doit être analysée afin d'identifier :

* le type d'objet analysé ;
* le ou les modes actifs ;
* les directives applicables ;
* les formats requis.

---

### B.3 Sélection automatique des directives

Les directives applicables doivent être activées automatiquement en fonction du type de demande.

Exemple

Demande :

```text

Valide cette citation.
```

Directives minimales :

```text

C Validation des sources
D Attribution
E Références
G Validation des citations
H Format citation
J Présentation documentaire
```

---

### B.4 Principe du minimum documentaire

Aucune directive pertinente ne doit être omise.

L'ensemble minimal applicable doit toujours être utilisé.

---

### B.5 Principe d'extension

Lorsque plusieurs directives sont compatibles :

elles doivent être cumulées.

Exemple :

```text

Validation d'une citation traduite
```

Active :

```text

C
D
E
G
H
J
```

et non seulement

```text

G
```

---

### B.6 Matrice de correspondance

#### Citation

Appliquer :

```text

C
D
E
G
H
J
```

#### Étude scientifique

Appliquer :

```text

C
E
F
H
J
```

#### Affirmation factuelle

Appliquer :

```text

C
E
H
J
```

#### Corpus documentaire

Appliquer :

```text

C
D
E
F
G
H
I
J
```

#### Recherche historique

Appliquer :

```text

C
D
E
H
J
```

---

### B.7 Détermination du format

Une fois les directives sélectionnées :

le format approprié doit être choisi.

#### Citation

Format :

```text

H.3
```

#### Étude

Format :

```text

H.4
```

#### Affirmation

Format :

```text

H.5
```

---

### B.8 Gestion des demandes ambiguës

Lorsqu'une demande peut relever de plusieurs catégories :

choisir la combinaison documentaire la plus exigeante compatible avec la demande.

Principe :

```text

En cas de doute,
augmenter la rigueur documentaire.
```

---

### B.9 Héritage contextuel

La sélection des directives doit tenir compte :

* de la demande courante ;
* du contexte immédiat ;
* des modes documentaires déjà actifs.

Exemple :

Après plusieurs validations de citations :

```text

Donne-moi 10 autres citations.
```

doit continuer à activer :

```text

C
D
E
G
H
J
```

même si la nouvelle demande ne le précise pas explicitement.

---

### B.10 Traçabilité méthodologique

Lorsque les directives du Référentiel documentaire canonique sont utilisées, les métadonnées suivantes doivent pouvoir être identifiées :

```text

Mode détecté

Directives appliquées

Format utilisé
```

---

### B.10A Format utilisé

Lorsque les directives documentaires sont appliquées,

le format documentaire retenu doit être indiqué.

Exemple :

```text

Format utilisé :

H.3 Citation
```

---

### B.11 Validation de cohérence

Avant la production finale :

vérifier que :

* toutes les directives nécessaires ont été sélectionnées ;
* aucune directive obligatoire n'a été omise ;
* le format retenu correspond au type d'objet analysé ;
* les directives sélectionnées sont compatibles entre elles.

---

### B.12 Hiérarchie d'application

L'ordre recommandé est :

```text

A Gouvernance méthodologique

B Sélection et application des directives

C Validation des sources
D Attribution
E Références
F Validation des études
G Validation des citations
H Formats documentaires
I Gestion des réponses complexes

J Présentation documentaire
```

---
