# Annexe B — Modèles documentaires officiels
## Référentiel documentaire canonique
---

# B.1 Objet

La présente annexe regroupe les modèles documentaires officiels du Référentiel documentaire canonique

Ces modèles constituent la représentation normalisée des objets documentaires définis dans la section H.

Les modèles peuvent être utilisés :

* en Markdown ;
* en DOCX ;
* en PDF ;
* en HTML ;
* en base de données ;
* en système RAG ;
* en base de connaissances.

---

# B.2 Principes généraux

## B.2.1 Uniformité

Toutes les unités documentaires d'un même type doivent utiliser le même modèle.

---

## B.2.2 Intégrité

Une unité documentaire commencée doit être complétée selon son modèle officiel.

---

## B.2.3 Métadonnées obligatoires

Lorsque pertinentes, les métadonnées suivantes doivent apparaître avant le contenu principal :

* Niveau de confiance ;
* Niveau de complétude documentaire ;
* Statut d'attribution.

---

## B.2.4 Réutilisabilité

Les modèles doivent pouvoir être convertis sans perte majeure d'information.

---

# B.3 Modèle officiel — Citation

## Structure

```text
# THÈME

## AUTEUR ATTRIBUÉ

## STATUT D'ATTRIBUTION

## NIVEAU DE CONFIANCE

## NIVEAU DE COMPLÉTUDE DOCUMENTAIRE

## SOURCE

## CITATION ORIGINALE

## TRADUCTION

## TYPE DE TRADUCTION

## CONTEXTE

## RÉFÉRENCES

## ANALYSE DE FIABILITÉ
```

---

## Exemple de gabarit

```text
# THÈME

Gestion du changement

## AUTEUR ATTRIBUÉ

Nom de l'auteur

## STATUT D'ATTRIBUTION

Authentifiée

## NIVEAU DE CONFIANCE

★★★★★ Très élevé

## NIVEAU DE COMPLÉTUDE DOCUMENTAIRE

Complet

## SOURCE

Titre de la source

## CITATION ORIGINALE

Texte original

## TRADUCTION

Texte traduit

## TYPE DE TRADUCTION

Traduction publiée

## CONTEXTE

Contexte documentaire

## RÉFÉRENCES

Références utilisées

## ANALYSE DE FIABILITÉ

Analyse documentaire
```

---

# B.4 Modèle officiel — Étude

## Structure

```text
# ÉTUDE

## AUTEUR

## ORGANISME

## ANNÉE

## OBJECTIF

## MÉTHODOLOGIE

## RÉSULTATS

## LIMITES

## INCERTITUDES

## NIVEAU DE PREUVE

## NIVEAU DE CONFIANCE

## RÉFÉRENCES
```

---

## Exemple de gabarit

```text
# ÉTUDE

## AUTEUR

Nom

## ORGANISME

Organisation

## ANNÉE

2026

## OBJECTIF

Objectif de l'étude

## MÉTHODOLOGIE

Description de la méthodologie

## RÉSULTATS

Résultats principaux

## LIMITES

Limites connues

## INCERTITUDES

Incertitudes documentées

## NIVEAU DE PREUVE

Élevé

## NIVEAU DE CONFIANCE

★★★★☆

## RÉFÉRENCES

Sources utilisées
```

---

# B.5 Modèle officiel — Affirmation

## Structure

```text
# AFFIRMATION

## ÉNONCÉ

## SOURCE

## VÉRIFICATION

## NIVEAU DE PREUVE

## NIVEAU DE CONFIANCE

## NIVEAU DE COMPLÉTUDE DOCUMENTAIRE

## LIMITATIONS

## RÉFÉRENCES
```

---

## Exemple de gabarit

```text
# AFFIRMATION

## ÉNONCÉ

Affirmation analysée

## SOURCE

Source principale

## VÉRIFICATION

Résultat de la vérification

## NIVEAU DE PREUVE

Modéré

## NIVEAU DE CONFIANCE

★★★☆☆

## NIVEAU DE COMPLÉTUDE DOCUMENTAIRE

Partiellement complet

## LIMITATIONS

Description

## RÉFÉRENCES

Références utilisées
```

---

# B.6 Modèle officiel — Source documentaire

## Structure

```text
# SOURCE DOCUMENTAIRE

## TYPE DE SOURCE

## AUTEUR OU ORGANISME

## TITRE

## DATE

## ÉTAT DOCUMENTAIRE

## NIVEAU DE CONFIANCE

## RÉFÉRENCES

## ANALYSE DOCUMENTAIRE
```

---

## Exemple de gabarit

```text
# SOURCE DOCUMENTAIRE

## TYPE DE SOURCE

Source primaire

## AUTEUR OU ORGANISME

Auteur

## TITRE

Titre du document

## DATE

1900

## ÉTAT DOCUMENTAIRE

Consultée

## NIVEAU DE CONFIANCE

★★★★☆

## RÉFÉRENCES

Référence complète

## ANALYSE DOCUMENTAIRE

Description et évaluation de la source
```

---

# B.7 Modèle officiel — Corpus documentaire

## Structure

```text
# THÈME

## OBJECTIF

## TABLEAU SYNTHÈSE

## CLASSIFICATION DOCUMENTAIRE

## UNITÉS DOCUMENTAIRES

## ANALYSE TRANSVERSALE

## SYNTHÈSE DOCUMENTAIRE

## NIVEAU GLOBAL DE CONFIANCE

## NIVEAU GLOBAL DE COMPLÉTUDE DOCUMENTAIRE

## RÉFÉRENCES GÉNÉRALES
```

---

## Tableau synthèse minimal

```text
Thème

Auteur

Statut d'attribution

Niveau de confiance

Niveau de complétude documentaire
```

---

## Exemple de gabarit

```text
# THÈME

Gestion du changement

## OBJECTIF

Constituer un corpus documentaire sur le changement organisationnel

## TABLEAU SYNTHÈSE

Liste synthétique des unités documentaires

## CLASSIFICATION DOCUMENTAIRE

Niveau A
Niveau B
Niveau C

## UNITÉS DOCUMENTAIRES

Fiches détaillées

## ANALYSE TRANSVERSALE

Analyse globale

## SYNTHÈSE DOCUMENTAIRE

Résumé des conclusions

## NIVEAU GLOBAL DE CONFIANCE

Élevé

## NIVEAU GLOBAL DE COMPLÉTUDE DOCUMENTAIRE

Partiellement complet

## RÉFÉRENCES GÉNÉRALES

Liste complète des références
```

---

# B.8 Modèle officiel — Synthèse documentaire

## Structure

```text
# SYNTHÈSE DOCUMENTAIRE

## RÉSUMÉ DES CONCLUSIONS

## CONSENSUS ACTUEL

## PRINCIPALES INCERTITUDES

## NIVEAU GLOBAL DE CONFIANCE

## NIVEAU GLOBAL DE COMPLÉTUDE DOCUMENTAIRE
```

---

## Exemple de gabarit

```text
# SYNTHÈSE DOCUMENTAIRE

## RÉSUMÉ DES CONCLUSIONS

Principaux constats

## CONSENSUS ACTUEL

Points largement reconnus

## PRINCIPALES INCERTITUDES

Documentation incomplète

## NIVEAU GLOBAL DE CONFIANCE

Élevé

## NIVEAU GLOBAL DE COMPLÉTUDE DOCUMENTAIRE

Partiellement complet
```

---

# B.9 Compatibilité documentaire

Tous les modèles définis dans la présente annexe doivent pouvoir être convertis vers :

```text
Markdown

DOCX

PDF

HTML

CSV

JSON

Base de données

Système RAG
```

sans perte majeure de structure documentaire.

---

# B.10 Autorité des modèles

Les modèles définis dans la présente annexe constituent les formats documentaires de référence du Référentiel documentaire canonique

Toute extension future doit demeurer compatible avec ces modèles maîtres.

---

# Fin de l'Annexe B

