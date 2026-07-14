# Annexe C — Matrices décisionnelles
## Référentiel documentaire canonique
---

# C.1 Objet

La présente annexe formalise les matrices décisionnelles utilisées par le Référentiel documentaire canonique

Elle vise à :

* uniformiser les décisions documentaires ;
* réduire les incohérences d'évaluation ;
* améliorer la reproductibilité ;
* faciliter l'implémentation dans un système IA.

---

# C.2 Principes généraux

## C.2.1 Évaluation multidimensionnelle

Une évaluation documentaire ne doit jamais reposer sur un seul critère.

Les dimensions doivent être évaluées séparément :

* Niveau de preuve ;
* Niveau de confiance ;
* Niveau de complétude documentaire.

---

## C.2.2 Indépendance des dimensions

Les dimensions suivantes sont indépendantes :

```text

Preuve

Confiance

Complétude
```

Aucune dimension ne doit être déduite automatiquement d'une autre.

---

## C.2.3 Transparence

Toute évaluation doit être justifiable.

---

# C.3 Matrice de niveau de preuve

## C.3.1 Niveau Élevé

Conditions typiques :

* source primaire disponible ;
* provenance vérifiable ;
* documentation cohérente ;
* faible nombre de contradictions.

Exemples :

* archive primaire ;
* ouvrage original ;
* rapport officiel ;
* article scientifique original.

---

## C.3.2 Niveau Modéré

Conditions typiques :

* documentation partielle ;
* sources secondaires solides ;
* certaines limitations documentées.

Exemples :

* synthèse académique ;
* revue documentaire ;
* ouvrage spécialisé.

---

## C.3.3 Niveau Faible

Conditions typiques :

* documentation limitée ;
* provenance incomplète ;
* contradictions importantes ;
* source primaire absente.

Exemples :

* citation isolée ;
* source non vérifiable ;
* documentation indirecte.

---

# C.4 Matrice de niveau de confiance

## C.4.1 Très élevé

```text

★★★★★ Très élevé
```

Conditions typiques :

* preuve élevée ;
* cohérence documentaire forte ;
* faible niveau d'incertitude.

---

## C.4.2 Élevé

```text

★★★★☆ Élevé
```

Conditions typiques :

* preuve généralement robuste ;
* limitations mineures.

---

## C.4.3 Modéré

```text

★★★☆☆ Modéré
```

Conditions typiques :

* documentation suffisante ;
* plusieurs zones d'incertitude.

---

## C.4.4 Faible

```text

★★☆☆☆ Faible
```

Conditions typiques :

* documentation limitée ;
* validation partielle.

---

## C.4.5 Très faible

```text

★☆☆☆☆ Très faible
```

Conditions typiques :

* documentation insuffisante ;
* forte incertitude ;
* impossibilité d'attribution robuste.

---

# C.5 Matrice de complétude documentaire

## C.5.1 Complet

Conditions :

* tous les champs obligatoires sont présents ;
* les références sont disponibles ;
* les métadonnées sont complètes.

---

## C.5.2 Partiellement complet

Conditions :

* majorité des champs obligatoires présents ;
* certaines informations manquantes ;
* documentation exploitable mais incomplète.

---

## C.5.3 Incomplet

Conditions :

* informations essentielles absentes ;
* documentation insuffisante ;
* validation limitée.

---

# C.6 Matrice croisée
# Preuve × Confiance

| Niveau de preuve | Confiance recommandée |
|------------------|----------------------|
| Élevé | ★★★★☆ à ★★★★★ |
| Modéré | ★★★☆☆ à ★★★★☆ |
| Faible | ★☆☆☆☆ à ★★★☆☆ |

---

## Règle

Une confiance très élevée ne doit normalement pas être attribuée à une preuve faible.

---

# C.7 Matrice croisée
# Confiance × Complétude

| Confiance | Complétude possible |
|------------|--------------------|
| Très élevée | Complet ou Partiellement complet |
| Élevée | Complet ou Partiellement complet |
| Modérée | Complet, Partiellement complet ou Incomplet |
| Faible | Partiellement complet ou Incomplet |
| Très faible | Généralement Incomplet |

---

## Exemple

Cas valide :

```text

Attribution : Authentifiée

Confiance : Très élevée

Complétude : Partiellement complet
```

La validation peut être robuste malgré certaines lacunes documentaires.

---

# C.8 Matrice d'attribution

## Authentifiée

Conditions typiques :

* attribution documentée ;
* sources concordantes ;
* documentation robuste.

---

## Probable

Conditions typiques :

* documentation cohérente ;
* certaines lacunes subsistent.

---

## Contestée

Conditions typiques :

* plusieurs attributions concurrentes ;
* désaccord documentaire persistant.

---

## Non attribuable

Conditions typiques :

* informations insuffisantes ;
* documentation absente ou contradictoire.

---

# C.9 Matrice de classification documentaire

## Niveau A

Critères :

* attribution fortement documentée ;
* documentation robuste.

---

## Niveau B

Critères :

* attribution plausible ;
* documentation incomplète.

---

## Niveau C

Critères :

* attribution contestée ;
* documentation faible ou insuffisante.

---

# C.10 Matrice de qualité des sources

| Type de source | Priorité |
|---------------|-----------|
| Source primaire | 1 |
| Source secondaire spécialisée | 2 |
| Source secondaire générale | 3 |
| Source tertiaire | 4 |

---

## Règle

À qualité documentaire comparable :

la source de priorité la plus élevée prévaut.

---

# C.11 Matrice d'arbitrage des conflits documentaires

Ordre d'arbitrage :

```text

1. Source primaire

2. Qualité méthodologique

3. Consensus documentaire

4. Ancienneté documentaire

5. Stabilité documentaire
```

---

## Absence d'arbitrage

Lorsque les éléments demeurent équivalents :

```text

Consensus documentaire absent.
```

doit être utilisé.

---

# C.12 Matrice de gestion des limites opérationnelles

Ordre de réduction recommandé :

```text

1. Nombre d'unités

2. Périmètre de l'analyse

3. Variantes

4. Détails secondaires
```

Avant de réduire :

```text

Références

Confiance

Traçabilité

Qualité documentaire
```

---

# C.13 Matrice de conformité documentaire

## Conforme

Conditions :

* directives applicables exécutées ;
* format approprié utilisé ;
* références documentées ;
* limitations identifiées.

---

## Partiellement conforme

Conditions :

* certaines exigences satisfaites ;
* écarts documentés.

---

## Non conforme

Conditions :

* directives obligatoires absentes ;
* documentation insuffisante ;
* traçabilité inadéquate.

---

# C.14 Matrice de synthèse de corpus

Le niveau global doit tenir compte :

```text

Qualité moyenne

+
Qualité minimale

+
Volume des incertitudes

+
Cohérence documentaire
```

---

## Principe

Une seule unité très faible peut réduire l'évaluation globale d'un corpus.

---

# C.15 Utilisation par les systèmes IA

Les matrices de la présente annexe doivent être utilisées pour :

* guider les décisions documentaires ;
* harmoniser les évaluations ;
* produire des résultats reproductibles ;
* améliorer la cohérence inter-réponses.

---

# C.16 Autorité des matrices

Les matrices définies dans la présente annexe constituent les mécanismes décisionnels de référence du Référentiel documentaire canonique

Toute extension future doit demeurer compatible avec ces matrices.

---

# Fin de l'Annexe C

