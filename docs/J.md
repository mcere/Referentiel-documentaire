# J Présentation et lisibilité des résultats
## Édition canonique candidate

### J.1 Objectif

Les réponses conformes aux directives du Référentiel documentaire canonique doivent non seulement être documentées et vérifiables, mais également :

* faciles à consulter ;
* faciles à comparer ;
* faciles à citer ;
* faciles à réutiliser ;
* faciles à convertir vers d'autres formats.

---

### J.2 Séparation entre contenu et présentation

Les informations doivent être structurées de manière à permettre leur conversion automatique vers :

* PDF ;
* DOCX ;
* HTML ;
* Markdown ;
* Tableau ;
* Base de données ;
* Fiche documentaire ;
* Base de connaissances.

La structure logique doit demeurer indépendante du format visuel utilisé.

---

### J.3 Format privilégié

Sauf indication contraire, privilégier un format de type fiche documentaire Markdown.

Exemple :

```text

# Citation

## Thème

Gestion du changement

## Auteur attribué

Léon Tolstoï

## Statut d'attribution

Authentifiée

## Niveau de confiance

★★★★★ Très élevé

## Niveau de complétude documentaire

Complet

## Citation originale

...

## Traduction française

...

## Contexte

...
```

---

### J.4 Ordre d'affichage recommandé

Lorsqu'une citation est analysée, l'ordre suivant est privilégié :

1. Thème
2. Niveau de confiance
3. Niveau de complétude documentaire
4. Auteur attribué
5. Statut d'attribution
6. Source principale
7. Citation originale
8. Traduction française
9. Type de traduction
10. Contexte
11. Mots-clés
12. Concept central
13. Analyse documentaire
14. Références


Cette règle place immédiatement les informations les plus utiles en tête.

---

### J.5 Présentation tabulaire

Lorsqu'une demande comporte plusieurs citations, sources ou affirmations :

fournir d'abord un tableau synthèse.

Exemple :

```text

Thème Auteur Confiance Complétude Statut

Gestion du changement Tolstoï Très élevé Complet Authentifiée

Résistance au changement Heifetz Très élevé Complet Authentifiée
```

Puis seulement après :

* les fiches détaillées.

---

### J.6 Métadonnées obligatoires

Chaque fiche documentaire doit inclure :

```text

thème ;
auteur attribué ;
statut d'attribution ;
niveau de confiance ;
niveau de complétude documentaire.
```

avant le contenu principal.

---

### J.7 Évaluation visuelle du niveau de confiance

Le niveau de confiance doit être présenté selon deux formes :

#### Forme textuelle

```text

Très élevé
Élevé
Modéré
Faible
Très faible
```

#### Forme visuelle

```text

★★★★★ Très élevé
★★★★☆ Élevé
★★★☆☆ Modéré
★★☆☆☆ Faible
★☆☆☆☆ Très faible
```

---

### J.8 Regroupement thématique

Lorsque plusieurs unités d'analyse sont présentées simultanément :

les regrouper par thème.

Lorsque disponible, utiliser également les mots-clés normalisés comme second niveau de regroupement.

Exemple :

```text

Résistance au changement

Perte

- citation 18
- citation 27

Autonomie

- citation 26

Biais cognitifs

Biais de confirmation

- citation 28

Leadership du changement

Participation

- citation 29
```
---

### J.9 Références simplifiées et complètes

Trois niveaux de références doivent être disponibles.

#### Référence courte

```text

Tolstoï, Three Methods of Reform (1900)
```

#### Référence complète

```text

Tolstoy, Leo.

Three Methods of Reform.

Dans Pamphlets.

Londres :
Free Age Press,
1900.
```

#### Référence Web complète

```text

Books on the Wall.

Leo Tolstoy's Infamous Quote:
Everyone Thinks of Changing the World,
but No One Thinks of Changing Himself.

Books on the Wall.

https://booksonthewall.com/blog/leo-tolstoy-quote/

Consulté le 11 juillet 2026.
```

---

### J.10 Format maître recommandé

Pour les corpus documentaires, utiliser prioritairement :

```text

# THÈME

## AUTEUR ATTRIBUÉ

## STATUT D'ATTRIBUTION

## NIVEAU DE CONFIANCE

## NIVEAU DE COMPLÉTUDE DOCUMENTAIRE

## SOURCE

## CITATION ORIGINALE

## TRADUCTION FRANÇAISE

## TYPE DE TRADUCTION

## CONTEXTE

## MOTS-CLÉS

## CONCEPT CENTRAL

## RÉFÉRENCES PRINCIPALES

### SOURCE PRIMAIRE IDENTIFIÉE

### SOURCE PRIMAIRE CONSULTÉE

### SOURCE SECONDAIRE LA PLUS ANCIENNE IDENTIFIÉE

### RÉFÉRENCES WEB

## ANALYSE DE FIABILITÉ

### VÉRIFIABILITÉ

### FORCE DE L'ATTRIBUTION

### LIMITE DE L'ATTRIBUTION

### JUSTIFICATION
```

Tous les autres formats doivent pouvoir être dérivés de cette structure.

---
### J.10.1 Carte documentaire

#### Objectif

Offrir une représentation synthétique et facilement consultable d'une unité documentaire.

#### Principe

La carte documentaire constitue une vue condensée dérivée du format maître documentaire.

Elle ne remplace pas la fiche documentaire complète.

#### Contenu minimal

La carte documentaire doit inclure :

* thème ;
* auteur attribué ;
* citation ;
* source ;
* mots-clés ;
* concept central ;
* statut d'attribution ;
* niveau de confiance.

#### Utilisations recommandées

La carte documentaire est particulièrement adaptée :

* aux bases de connaissances ;
* aux banques de citations ;
* aux fiches de lecture ;
* aux répertoires documentaires ;
* aux systèmes de recherche documentaire.

#### Exemple

```text

┌────────────────────────────────────┐
│ Citation                           │
├────────────────────────────────────┤
│ Auteur : Ronald A. Heifetz         │
│ Source : The Practice of           │
│ Adaptive Leadership (2009)         │
├────────────────────────────────────┤
│ « Ce à quoi les gens résistent,    │
│ ce n'est pas le changement en soi, │
│ mais la perte. »                   │
├────────────────────────────────────┤
│ Mots-clés                          │
│ changement                         │
│ perte                              │
│ résistance                         │
├────────────────────────────────────┤
│ Concept central                    │
│ Les résistances sont souvent       │
│ liées aux pertes perçues.          │
├────────────────────────────────────┤
│ Attribution : Authentifiée         │
│ Confiance : ★★★★★                  │
└────────────────────────────────────┘
```
### J.11 Références Web

Lorsqu'une référence Web est utilisée :

#### Obligatoire

* auteur ou organisme ;
* titre de la page ;
* nom du site ;
* URL complète ;
* date de consultation.

#### Interdit

```text

booksonthewall.com
```

ou

```text

Wikipedia
```

sans autre précision.

#### Format recommandé

```text

Books on the Wall.

Leo Tolstoy's Infamous Quote:
Everyone Thinks of Changing the World,
but No One Thinks of Changing Himself.

Books on the Wall.

https://booksonthewall.com/blog/leo-tolstoy-quote/

Consulté le 11 juillet 2026.
```

---

### J.12 Références multiples

Lorsqu'une affirmation est soutenue par plusieurs références :

présenter séparément :

* Source primaire
* Source secondaire
* Sources complémentaires

Ne jamais fusionner plusieurs références dans une même entrée.

---

### J.13 Références réutilisables

Chaque référence doit être suffisamment complète pour permettre :

* la recherche manuelle ;
* le copier-coller ;
* l'ouverture directe du lien ;
* l'importation dans un logiciel bibliographique ;
* la conversion vers un autre format de citation.

---

### J.14 Compatibilité bibliographique

Les références doivent pouvoir être converties sans perte majeure vers :

* APA ;
* Chicago ;
* MLA ;
* BibTeX ;
* CSL-JSON.

---

### J.15 Niveau de complétude documentaire

#### Objectif

Permettre d'évaluer rapidement le degré d'achèvement documentaire d'une unité d'analyse.

Chaque citation, source, affirmation ou étude documentée doit indiquer explicitement son niveau de complétude documentaire.

#### Niveaux autorisés

##### Complet

Tous les champs obligatoires exigés par les directives applicables sont remplis.

##### Partiellement complet

La majorité des champs obligatoires sont remplis, mais certaines informations documentaires demeurent incomplètes ou introuvables.

##### Incomplet

La vérification documentaire est insuffisante pour satisfaire aux exigences minimales des directives applicables.

#### Affichage obligatoire

Le niveau de complétude documentaire doit apparaître dans les métadonnées principales de la fiche.

---

### J.15.1 Restrictions d'utilisation

Les niveaux de complétude documentaire déterminent les usages permis d'une unité documentaire.

#### Complet

Peut être utilisé comme :

* référence documentaire ;
* référence pédagogique ;
* référence académique ;
* corpus documentaire validé ;
* source de citation secondaire.

#### Partiellement complet

Peut être utilisé comme :

* référence exploratoire ;
* support pédagogique ;
* piste de recherche ;
* corpus documentaire préliminaire.

Ne doit pas être présenté comme entièrement validé ou exhaustif.

#### Incomplet

Peut être utilisé uniquement comme :

* élément à vérifier ;
* piste documentaire ;
* information provisoire.

Ne doit pas être présenté comme une référence documentaire validée.

---

### J.16 Distinction entre validité et complétude

La validité documentaire et la complétude documentaire sont deux critères indépendants.

Une citation peut être :

* fortement validée mais partiellement documentée ;
* complètement documentée mais faiblement validée ;
* fortement validée et complètement documentée ;
* faiblement validée et incomplètement documentée.

Les deux évaluations doivent être présentées séparément.

Exemple :

```text

Statut d'attribution : Authentifiée

Niveau de confiance : Très élevé

Niveau de complétude documentaire : Partiellement complet
```

---

### J.17 Classification documentaire des corpus

Lorsqu'un corpus comporte plusieurs unités documentaires, celles-ci doivent être regroupées selon leur qualité documentaire.

#### Niveau A

Attribution fortement documentée.

#### Niveau B

Attribution plausible mais incomplètement documentée.

#### Niveau C

Attribution contestée, marginale ou insuffisamment documentée.

La classification du corpus est indépendante du niveau de complétude documentaire.

#### Règle

La classification documentaire du corpus est indépendante :

* du niveau de confiance ;
* du niveau de complétude documentaire.

Une unité de Niveau A peut être :

* Partiellement complète

et une unité de Niveau B peut être :

* Complète

si sa documentation est exhaustive mais son attribution demeure incertaine.

