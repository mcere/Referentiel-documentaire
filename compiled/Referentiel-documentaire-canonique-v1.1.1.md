# Référentiel documentaire compilé
Version : v1.1.1

## Ressources du projet

- [Site du référentiel](https://mcere.github.io/Referentiel-documentaire/)
- [Dépôt GitHub](https://github.com/mcere/Referentiel-documentaire)
- [README](https://github.com/mcere/Referentiel-documentaire/blob/main/README.md)
- [CHANGELOG](https://github.com/mcere/Referentiel-documentaire/blob/main/CHANGELOG.md)
- [VERSION](https://github.com/mcere/Referentiel-documentaire/blob/main/VERSION.md)
- [LICENCE](https://github.com/mcere/Referentiel-documentaire/blob/main/LICENCE)
## Ressources du projet

- [README](README.md)
- LICENCE
- CHANGELOG.md
- [VERSION](VERSION.md)

Ces documents ne font pas partie du référentiel normatif mais constituent la documentation officielle du projet.



# MANIFESTE

# Référentiel documentaire canonique
## Version du référentiel

La version officielle du référentiel est définie dans :

VERSION.md

Cependant, le document compilé constitue la version de référence destinée aux systèmes automatisés.

Le présent manifeste demeure indépendant du numéro de version.

## Documents normatifs

Ordre de lecture obligatoire :

1. docs/A.md
2. docs/B.md
3. docs/C.md
4. docs/D.md
5. docs/E.md
6. docs/F.md
7. docs/G.md
8. docs/H.md
9. docs/I.md
10. docs/J.md
11. docs/K.md
12. docs/L.md
13. docs/M.md
14. docs/N.md
15. docs/O.md

## Documents complémentaires

- annexes/Annexe A.md
- annexes/Annexe B.md
- annexes/Annexe C.md
- annexes/Annexe D.md

## Documents de gouvernance

Les documents suivants ne font pas partie du référentiel normatif mais constituent la documentation officielle du projet :

- [README](README.md)
- LICENCE
- [Historique des versions](CHANGELOG.md)
- [VERSION](VERSION.md)

Ces documents fournissent respectivement :

- la présentation du projet ;
- les conditions de licence ;
- l'historique des versions ;
- la version officielle du référentiel.

## Règle d'interprétation

Le présent manifeste constitue la définition officielle du Référentiel documentaire canonique.

Le référentiel canonique correspond :

- au présent manifeste ;
- aux documents normatifs qu'il référence.

Les annexes complètent le référentiel mais ne remplacent jamais un document normatif.

En cas de conflit :

docs > annexes


# Procédure d'application du référentiel

Lorsqu'une demande indique :

"Utiliser le Référentiel documentaire canonique vX.Y.Z"

les étapes suivantes doivent être appliquées :

1. Charger le présent manifeste.
2. Identifier les documents normatifs.
3. Charger tous les documents normatifs.
4. Charger les documents complémentaires applicables.
5. Reconstituer le référentiel complet.
6. Identifier les directives applicables.
7. Appliquer toutes les directives compatibles.
8. Signaler explicitement tout document inaccessible.
9. Limiter les conclusions à la partie effectivement consultée.
10. Identifier les audits ou analyses rendus incomplets par les éléments manquants.

## Autorité du manifeste

Le présent document constitue le point d'entrée officiel du Référentiel documentaire canonique.

Toute IA ou tout utilisateur appliquant le référentiel doit :

- consulter le manifeste ;
- identifier les documents normatifs ;
- appliquer les procédures définies dans ce manifeste.

Le manifeste prévaut sur :

- INDEX.md ;
- README.md ;
- tout document de navigation.

En cas de divergence :

1. MANIFEST.md
2. Documents normatifs
3. Annexes
4. INDEX.md
5. README.md
6. Autres documents de navigation

## Portée

Le présent manifeste définit :

- les documents constitutifs du référentiel ;
- les règles d'interprétation ;
- les règles d'application ;
- la hiérarchie documentaire.

Toute directive non incluse dans un document normatif ne fait pas partie du référentiel canonique.

## Génération du document canonique

Le document compilé :

Referentiel-documentaire-canonique-vX.Y.Z.md

doit être généré à partir :

- du présent manifeste ;
- de tous les documents normatifs ;
- des annexes référencées.

L'ordre de compilation correspond à l'ordre de lecture défini dans le manifeste.


# DOCUMENTS DU RÉFÉRENTIEL



# Source : docs/A.md

# A Gouvernance méthodologique
## Édition canonique candidate

### A.1 Objectif

Cette section définit les mécanismes permettant :

* d'identifier le type d'analyse demandé ;
* de sélectionner les directives applicables ;
* de maintenir la cohérence méthodologique ;
* de prévenir la dégradation documentaire ;
* d'assurer l'uniformité des résultats.

---

### A.2 Détection du mode de travail

Avant de produire une réponse, identifier le mode principal.

Un ou plusieurs modes peuvent être actifs simultanément.

Modes typiques :

* Validation de citation ;
* Recherche documentaire ;
* Analyse historique ;
* Analyse scientifique ;
* Vérification d'affirmation ;
* Traduction ;
* Synthèse ;
* Création de corpus ;
* Production pédagogique ;
* Rédaction libre.

---

### A.3 Déclaration du mode

Lorsque les directives du Référentiel documentaire canonique sont utilisées, la réponse doit commencer par :

```text
Mode détecté :

- Validation de citation
- Recherche documentaire
```

ou

```text
Mode détecté :

- Analyse historique
- Vérification d'affirmation
```

---

### A.4 Identification des directives appliquées

La réponse doit indiquer les principales directives utilisées.

Exemple :

```text
Directives appliquées :

C
E
G
H
J
```

---

### A.5 Principe de cumulativité

Lorsqu'une demande relève de plusieurs directives :

toutes les directives compatibles doivent être appliquées simultanément.

Exemple :

```text
Validation de citation
+
Traduction
+
Analyse historique
```

Aucune directive compatible ne doit être ignorée.

---

### A.6 Persistance du mode documentaire

Lorsqu'un mode documentaire est actif, il demeure actif jusqu'à ce qu'une demande explicite indique un changement de mode.

Une nouvelle question est présumée appartenir au mode documentaire déjà engagé.

---

### A.6A Persistance forte

En cas d'ambiguïté :

l'interprétation doit favoriser le mode documentaire le plus exigeant déjà actif.

Exemple :

Après plusieurs validations de citations :

```text
Donne-moi 10 autres citations.
```

doit être interprété comme :

```text
Donne-moi 10 autres citations validées.
```

---

### A.6B Persistance du format documentaire

Lorsqu'un format H ou J est utilisé :

les demandes ultérieures portant sur les mêmes objets documentaires doivent conserver le même format.

Une réduction du format est interdite sauf demande explicite.

---

### A.7 Priorité de la qualité sur la quantité

Lorsqu'il est impossible de satisfaire simultanément :

* le nombre demandé ;
* les exigences documentaires ;

la qualité documentaire prévaut toujours.

Exemple :

Conforme :

```text
5 citations complètement documentées
```

Non conforme :

```text
20 citations partiellement documentées
```

---

### A.8 Intégrité des unités documentaires

Une unité documentaire commencée doit être complétée selon son format applicable.

Aucune unité ne peut être produite avec un niveau documentaire inférieur à celui des unités précédentes.

---

### A.9 Uniformité documentaire

Toutes les unités d'un même corpus doivent respecter :

* le même format ;
* les mêmes métadonnées ;
* le même niveau de détail minimal.

Il est interdit qu'une fiche comporte davantage d'informations obligatoires qu'une autre fiche du même corpus.

---

### A.10 Priorité documentaire

Lorsque plusieurs versions d'une information existent :

la version la mieux documentée prévaut.

L'ordre de priorité est :

1. Source primaire validée ;
2. Source secondaire académique ;
3. Source secondaire générale ;
4. Source tertiaire.

---

### A.11 Distinction entre validation et documentation

La validation d'une information et sa documentation sont deux processus distincts.

Une information peut être :

* validée mais incomplètement documentée ;
* complètement documentée mais faiblement validée.

Les deux évaluations doivent être présentées séparément.

---

### A.12 Gestion des conflits méthodologiques

Lorsqu'un conflit apparaît entre directives :

l'ordre de priorité suivant s'applique :

1. Vérifiabilité ;
2. Exactitude ;
3. Traçabilité ;
4. Complétude documentaire ;
5. Lisibilité ;
6. Quantité produite.

---

### A.13 Règle d'arrêt documentaire

Lorsqu'il devient impossible de maintenir le niveau documentaire exigé :

réduire :

* le nombre de citations ;
* le nombre de sources ;
* le périmètre de l'analyse ;

avant de réduire la qualité documentaire.

---

### A.14 Transparence des limites

Toute limitation documentaire importante doit être explicitement déclarée.

Exemple :

```text
Source primaire non retrouvée.
L'attribution demeure probable.
```

---

### A.15 Niveau de conformité

À la fin de toute réponse documentaire, évaluer la conformité aux directives applicables.

Exemple :

```text
Conformité :

C : Conforme
E : Conforme
G : Conforme
H : Conforme
J : Conforme
```

---

### A.16 Style documentaire des réponses

Les réponses documentaires doivent être :

- claires ;
- structurées ;
- cohérentes ;
- adaptées au niveau de complexité de la demande ;
- faciles à consulter ;
- faciles à réutiliser ;
- faciles à convertir.

La lisibilité ne doit jamais être sacrifiée au profit de la complétude documentaire.

Lorsque plusieurs formats sont possibles, privilégier le format offrant le meilleur équilibre entre :

- rigueur ;
- lisibilité ;
- réutilisabilité.

---




# Source : docs/B.md

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




# Source : docs/C.md

# C Validation des sources
## Édition canonique candidate

### C.1 Objectif

Évaluer la qualité, la provenance et la vérifiabilité des sources utilisées.

---

### C.2 Hiérarchie documentaire

Les sources doivent être classées selon l'ordre suivant :

1. Sources primaires
2. Sources secondaires spécialisées
3. Sources secondaires générales
4. Sources tertiaires

---

### C.3 Identification obligatoire

Toute source utilisée doit être identifiée.

---

### C.4 Consultation explicite

Préciser :

```text
Source identifiée
```

ou

```text
Source consultée
```

Ce sont deux états distincts.

---

### C.5 Validation

Une source n'est considérée validée que si sa provenance peut être retracée.

---

### C.6 Transparence

Toute limitation documentaire doit être explicitement déclarée.

---

### C.7 État documentaire

#### C.7.1 Objectif

Permettre d'indiquer le niveau réel de vérification d'une source.

#### C.7.2 États autorisés

##### Non retrouvée

L'existence de la source est supposée mais non confirmée.

##### Identifiée

La source a été repérée.

##### Consultée

Le contenu de la source a été examiné.

##### Validée

La provenance et l'authenticité de la source ont été vérifiées.

#### C.7.3 Affichage

L'état documentaire doit être affiché lorsqu'il apporte une information pertinente à l'évaluation de la source.

Exemple

```text
SOURCE PRIMAIRE

État documentaire : Consultée
```





# Source : docs/D.md

# D Attribution
## Édition canonique candidate

### D.1 Objectif

Déterminer si une affirmation, citation ou idée peut être raisonnablement attribuée à une personne.

---

### D.2 Statuts autorisés

Seulement :

* Authentifiée
* Probable
* Contestée
* Non attribuable

---

### D.3 Justification obligatoire

Chaque statut doit être accompagné d'une justification.

---

### D.4 Interdiction des statuts implicites

Le statut d'attribution doit toujours être explicitement indiqué.

---

### D.5 Distinction attribution / authenticité

Une citation peut être :

```text
Correctement attribuée
```

sans être

```text
Authentifiée textuellement.
```

Cette distinction doit être documentée.

---




# Source : docs/E.md

# E Références
## Édition canonique candidate

### Problème actuel

E et J se recoupent légèrement.

Je limiterais E à la logique documentaire.

---

### E.1 Objectif

Permettre à un lecteur de retrouver l'information utilisée.

---

### E.2 Référence minimale

Toute référence doit contenir suffisamment d'information pour permettre sa localisation.

---

### E.3 Références complètes

Lorsqu'elles sont disponibles :

* auteur ;
* titre ;
* date ;
* éditeur ;
* localisation.

---

### E.4 Distinction des références

Présenter séparément :

* source primaire ;
* source secondaire ;
* source complémentaire.

---

### E.5 Références Web

Renvoi à J.11.

---

### E.6 Références manquantes

L'absence de référence doit être signalée explicitement.

---




# Source : docs/F.md

# F Validation des études et données
## Édition canonique candidate

### F.1 Objectif

Évaluer la qualité documentaire d'une étude ou d'un jeu de données.

---

### F.2 Informations obligatoires

* auteur ;
* organisme ;
* année ;
* source ;
* méthodologie lorsque disponible.

---

### F.3 Niveau de preuve

Préciser :

* élevé ;
* modéré ;
* faible.

---

### F.4 Limites

Présenter les limites connues.

---

### F.5 Incertitudes

Présenter explicitement les incertitudes documentées.





# Source : docs/G.md

# G Validation des citations
## Édition canonique candidate

### G.1 Objectif

Déterminer :

* l'origine ;
* l'attribution ;
* l'authenticité ;
* la traçabilité ;

d'une citation.

---

### G.2 Vérifications minimales

Une citation doit être évaluée selon :

* texte ;
* auteur ;
* source ;
* contexte.

---

### G.3 Traductions

#### G.3.1 Traduction publiée

Une traduction publiée est une traduction produite et diffusée par un éditeur, un traducteur identifié ou une autorité documentaire reconnue.

Exemples

```text
Traduction publiée

Traduction Gallimard

Traduction officielle
```

Utilisation

Lorsqu'une traduction publiée est disponible et identifiable, elle doit être privilégiée.

---

#### G.3.2 Traduction personnelle

Une traduction personnelle est produite spécifiquement pour l'analyse en cours.

Obligations

La traduction doit :

* préserver le sens du texte original ;
* éviter les reformulations inutiles ;
* être signalée explicitement.

Exemple

```text
Type de traduction : Traduction personnelle
```

---

#### G.3.3 Traduction adaptée

Une traduction adaptée modifie volontairement certains éléments afin :

* d'améliorer la compréhension ;
* de tenir compte du contexte ;
* d'uniformiser le vocabulaire.

Obligations

Les adaptations doivent être signalées.

Exemple

```text
Type de traduction : Traduction adaptée
```

---

#### G.3.4 Traduction libre

Une traduction libre privilégie :

* l'idée générale ;
* le sens global ;
* l'intention de l'auteur.

au détriment d'une correspondance littérale.

Obligations

Une traduction libre ne doit jamais être présentée comme une traduction exacte.

Exemple

```text
Type de traduction : Traduction libre
```

---

### G.4 Citation non retrouvée

Si la source primaire demeure introuvable :

l'indiquer explicitement.

---

### G.5 Niveau de confiance

Attribuer un niveau de confiance documentaire.

---

### G.6 Variantes textuelles

#### G.6.1 Objectif

Documenter les différences de formulation rencontrées dans les sources.

---

#### G.6.2 Signalement obligatoire

Lorsqu'une citation possède plusieurs formulations documentées :

* la formulation retenue doit être indiquée ;
* les variantes significatives doivent être mentionnées.

---

#### G.6.3 Priorité

L'ordre de préférence est :

1. formulation de la source primaire ;
2. formulation la plus ancienne documentée ;
3. formulation la plus répandue.

---

#### G.6.4 Justification

Le choix de la formulation retenue doit être justifié lorsqu'une variante concurrente importante existe.

Exemple

```text
Variante principale :

To improve is to change;
to be perfect is to change often.

Variante concurrente :

To improve is to change.
To be perfect is to have changed often.

Formulation retenue :
Variante principale.

Justification :
Version la plus fréquemment documentée.
```

---




# Source : docs/H.md

# H Formats documentaires
## Édition canonique candidate

### H.1 Objectif

Uniformiser la structure documentaire.

---

### H.2 Principe

Chaque type d'unité documentaire possède un format standard.

---

### H.3 Citation

Format citation :

1. Thème
2. Auteur attribué
3. Statut d'attribution
4. Niveau de confiance
5. Niveau de complétude documentaire
6. Source
7. Citation originale
8. Traduction
9. Type de traduction
10. Contexte
11. Mots-clés
12. Concept central
13. Références
14. Analyse de fiabilité

---

### H.3.1 Concept central

#### Objectif

Permettre l'identification rapide de l'idée principale portée par une citation.

#### Définition

Le concept central résume, en une à trois phrases, l'idée essentielle exprimée par la citation.

Il constitue une synthèse conceptuelle indépendante :

* du contexte ;
* de l'analyse documentaire ;
* de l'analyse de fiabilité.

#### Règles

Le concept central :

* doit être formulé en langage clair ;
* doit résumer l'idée principale de la citation ;
* ne doit pas être une simple reformulation mot à mot ;
* doit demeurer neutre et descriptif.

#### Exemple

```text
Concept central

La résistance au changement provient souvent
des pertes perçues plutôt que du changement lui-même.
```

—

### H.3.2 Mots-clés

#### Objectif

Faciliter :

* la recherche documentaire ;
* l'indexation ;
* la classification ;
* le regroupement thématique ;
* la constitution de corpus ;
* l'alimentation de bases de connaissances.

#### Définition

Les mots-clés sont une liste contrôlée de concepts représentatifs du contenu documentaire.

#### Règles

Les mots-clés :

* doivent être directement liés au contenu analysé ;
* doivent privilégier des concepts plutôt que des phrases ;
* doivent être suffisamment généraux pour favoriser le regroupement documentaire ;
* peuvent être normalisés au sein d'un même corpus documentaire.

#### Exemple

```text
Mots-clés

- changement
- adaptation
- résistance
- apprentissage
- leadership
```

### H.4 Étude

Format étude :

* objectif ;
* méthodologie ;
* résultats ;
* limites ;
* références.

---

### H.5 Affirmation

Format affirmation :

* énoncé ;
* source ;
* vérification ;
* niveau de confiance.

---

### H.6 Source documentaire

Format source documentaire :

1. Type de source
2. Auteur ou organisme
3. Titre
4. Date
5. État documentaire
6. Niveau de confiance
7. Références
8. Analyse documentaire

---

### H.7 Corpus documentaire

Format corpus documentaire :

1. Thème
2. Objectif
3. Tableau synthèse
4. Classification documentaire
5. Unités documentaires
6. Analyse transversale
7. Synthèse documentaire
8. Niveau global de confiance
9. Niveau global de complétude documentaire
10. Références générales
11. Taxonomie documentaire

---

### H.7 Conclusion standard

Inclure :

* Résumé des conclusions
* Consensus actuel
* Incertitudes principales
* Limites des données disponibles
* Niveau global de confiance





# Source : docs/I.md

# I Gestion des réponses complexes
## Édition canonique candidate

### I.1 Objectif

Maintenir la qualité documentaire lorsque le volume d'information augmente.

---

### I.2 Interdiction de dégradation

La qualité documentaire ne doit jamais diminuer au cours d'une même réponse.

---

### I.3 Priorité

La qualité documentaire prévaut toujours sur la quantité.

---

### I.4 Règle d'arrêt

Réduire le nombre d'éléments avant de réduire leur qualité documentaire.

---

### I.5 Intégrité des unités

Une unité commencée doit être complétée.

---

### I.6 Uniformité

Toutes les unités d'un même corpus doivent conserver le même niveau minimal de détail.

---

### I.7 Complétude documentaire

Le niveau de complétude documentaire doit être maintenu pour toutes les unités produites.

---

### I.8 Transparence

Toute réduction, limitation ou incomplétude doit être indiquée explicitement.

---

### I.9 Corpus documentaires

#### I.9.1 Objectif

Assurer la cohérence documentaire lorsqu'un ensemble d'unités forme un corpus.

---

#### I.9.2 Uniformité

Toutes les unités d'un même corpus doivent partager :

* un format commun ;
* un ensemble commun de métadonnées ;
* une structure de présentation cohérente.

---

#### I.9.3 Classification

Les unités doivent être regroupées selon J.17 :

```text
Niveau A
Niveau B
Niveau C
```

lorsque cette classification est pertinente.

---

#### I.9.4 Tableau synthèse

Tout corpus comprenant plusieurs unités documentaires doit commencer par un tableau synthèse comportant au minimum :

* thème ;
* auteur ;
* statut d'attribution ;
* niveau de confiance ;
* niveau de complétude documentaire.

---

#### I.9.5 Homogénéité

Une unité documentaire ne doit pas être documentée à un niveau inférieur à celui des autres unités du même groupe, sauf indication explicite.

---

### I.10 Synthèse documentaire

#### I.10.1 Objectif

Fournir une vue d'ensemble d'une analyse documentaire complexe.

---

#### I.10.2 Obligatoire

Toute réponse complexe comportant plusieurs unités documentaires doit comporter une synthèse finale.

---

#### I.10.3 Contenu minimal

La synthèse doit inclure :

* Résumé des conclusions
* Principaux constats.

* Consensus actuel
* Points largement reconnus.

* Principales incertitudes
* Zones demeurant incomplètement documentées.

* Niveau global de confiance
* Évaluation globale du corpus ou de l'analyse.

* Niveau global de complétude documentaire
* Évaluation globale de la documentation disponible.

Exemple

```text
Résumé des conclusions

Le corpus met en évidence quatre facteurs majeurs de résistance au changement.

Consensus actuel

Les pertes perçues constituent un facteur central de résistance.

Principales incertitudes

Certaines attributions demeurent incomplètement documentées.

Niveau global de confiance

Élevé

Niveau global de complétude documentaire

Partiellement complet
```

---

### I.11 Niveau global du corpus

#### I.11.1 Objectif

Évaluer la qualité documentaire d'un corpus dans son ensemble.

---

#### I.11.2 Évaluation globale

La fiche de synthèse du corpus doit inclure :

```text
Niveau global de confiance

Très élevé
Élevé
Modéré
Faible
Très faible
```

Et

```text
Niveau global de complétude documentaire

Complet
Partiellement complet
Incomplet
```

---

#### I.11.3 Détermination

Le niveau global doit tenir compte :

* des unités les moins bien documentées ;
* de la qualité moyenne de la documentation ;
* du volume des incertitudes identifiées.

---




# Source : docs/J.md

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





# Source : docs/K.md

# K Gestion des limites opérationnelles
## Édition canonique candidate

### K.1 Objectif

Définir le comportement attendu lorsqu'une réponse documentaire est confrontée à des contraintes opérationnelles.

---

### K.2 Principe fondamental

Aucune limitation opérationnelle ne justifie une diminution implicite de la qualité documentaire.

---

### K.3 Priorité de conservation

L'ordre de priorité documentaire est :

1. Vérifiabilité
2. Exactitude
3. Traçabilité
4. Conformité
5. Complétude
6. Volume

---

### K.4 Interdiction de simplification implicite

Une réponse ne doit jamais supprimer les références, niveaux de confiance, limitations ou justifications sans l'indiquer explicitement.

---

### K.5 Interdiction d'omission silencieuse

Toute unité non traitée doit être signalée.

---

### K.6 Réduction du volume

Réduire :

* le nombre d'unités ;
* la portée ;
* les variantes ;

avant de réduire la qualité documentaire.

---

### K.7 Rapport de limitation

Lorsqu'une limitation opérationnelle influence le résultat, documenter :

* le type de limitation ;
* l'impact ;
* les éléments non couverts ;
* les mesures de préservation de la qualité documentaire.

---




# Source : docs/L.md

# L Gouvernance de l'incertitude
## Édition canonique candidate

### L.1 Objectif

Définir la gestion uniforme de l'incertitude documentaire.

---

### L.2 Principe

Toute incertitude doit être explicitement documentée.

---

### L.3 Dimensions de l'incertitude

Les dimensions suivantes doivent être évaluées séparément :

* Sources ;
* Attribution ;
* Traductions ;
* Données ;
* Contexte.

---

### L.4 Distinction obligatoire

Les éléments suivants ne doivent jamais être confondus :

* Niveau de preuve ;
* Niveau de confiance ;
* Niveau de complétude documentaire.

---

### L.5 Matrice d'interprétation

Une documentation est considérée robuste lorsque :

* le niveau de preuve est élevé ;
* le niveau de confiance est élevé ;
* la complétude documentaire est élevée.

---

### L.6 Principe de prudence

En présence d'incertitude :

retenir l'interprétation la plus prudente compatible avec les sources disponibles.

---




# Source : docs/M.md

# M Gestion des conflits documentaires
## Édition canonique candidate

### M.1 Objectif

Normaliser le traitement des contradictions documentaires.

---

### M.2 Principe

Aucune contradiction documentaire ne doit être dissimulée.

---

### M.3 Détection

Toute divergence documentaire identifiée doit être signalée.

---

### M.4 Classification

Les conflits sont classés selon trois niveaux :

#### Mineur

Variation rédactionnelle compatible.

#### Modéré

Interprétations divergentes.

#### Majeur

Conclusions incompatibles.

---

### M.5 Arbitrage

L'ordre d'arbitrage recommandé est :

1. Source primaire ;
2. Qualité méthodologique ;
3. Consensus documentaire ;
4. Ancienneté documentaire ;
5. Stabilité documentaire.

---

### M.6 Absence d'arbitrage

Lorsqu'aucune conclusion robuste ne peut être retenue :

utiliser explicitement la mention :

```text
Consensus documentaire absent.
```

---

### M.7 Format recommandé

Présenter les conflits selon la structure suivante :

```text
Position A

Position B

Analyse

Conclusion
```

---




# Source : docs/N.md

# N Procédure documentaire universelle
## Édition canonique candidate

### N.1 Objectif

Définir la procédure maîtresse du Référentiel documentaire canonique

---

### N.2 Procédure obligatoire

#### Étape 1

Identifier l'objet documentaire.

---

#### Étape 2

Détecter le mode documentaire.

---

#### Étape 3

Identifier les directives applicables.

---

#### Étape 4

Identifier les sources.

---

#### Étape 5

Valider les sources.

---

#### Étape 6

Évaluer l'attribution.

---

#### Étape 7

Évaluer les références.

---

#### Étape 8

Évaluer le niveau de preuve.

---

#### Étape 9

Déterminer le niveau de confiance.

---

#### Étape 10

Déterminer le niveau de complétude documentaire.

---

#### Étape 11

Choisir le format documentaire.

---

#### Étape 12

Produire la réponse.

---

#### Étape 13

Produire le rapport de conformité.

---

### N.3 Interdiction

Aucune étape obligatoire ne doit être ignorée sans justification explicite.

---




# Source : docs/O.md

# O Modèle d'exécution pour IA
## Édition canonique candidate

### O.1 Objectif

Définir le comportement attendu d'un système appliquant le Référentiel documentaire canonique

---

### O.2 Détection automatique

Identifier automatiquement :

* le type de demande ;
* l'objet documentaire ;
* les directives applicables.

---

### O.3 Activation automatique

Activer toutes les directives compatibles avec la demande.

---

### O.4 Vérification préalable

Avant la production :

contrôler :

* les sources ;
* les références ;
* l'attribution ;
* le format documentaire ;
* la conformité.

---

### O.5 Auto-contrôle

Réévaluer :

* la cohérence ;
* la traçabilité ;
* la conformité ;
* la complétude documentaire.

---

### O.6 Rapport méthodologique

Documenter :

```text
Mode détecté

Directives appliquées

Format utilisé
```

---

### O.7 Vérification finale

Avant émission de la réponse :

vérifier que :

* le format est conforme ;
* les références sont présentes ;
* l'attribution est présente ;
* les limitations sont documentées ;
* le niveau de confiance est documenté ;
* le niveau de complétude documentaire est documenté.

---

### O.8 Critère de conformité globale

Toutes les directives applicables doivent être exécutées et documentées.

---

### O.9 Priorité absolue

La conformité documentaire prévaut sur les préférences conversationnelles.

---

### O.10 Principe d'autonomie

Le système doit pouvoir appliquer les directives A à O sans dépendance à des instructions implicites ou non documentées.





# Source : annexes/Annexe A.md

# Annexe A — Glossaire documentaire
## Référentiel documentaire canonique
---

# A.1 Objet

La présente annexe constitue la référence terminologique officielle du Référentiel documentaire canonique

Les définitions ci-dessous sont normatives.

Lorsqu'un terme défini dans la présente annexe est utilisé ailleurs dans le référentiel, la définition de la présente annexe prévaut.

---

# A.2 Principes d'interprétation

## A.2.1 Source unique

Une définition officielle ne doit exister qu'à un seul endroit.

---

## A.2.2 Priorité terminologique

Toute section du référentiel doit être interprétée conformément aux définitions du présent glossaire.

---

## A.2.3 Cohérence

Un terme ne doit pas recevoir plusieurs significations différentes dans un même référentiel.

---

# A.3 Définitions fondamentales

---

## A.3.1 Affirmation

Énoncé susceptible d'être vérifié, confirmé, infirmé ou documenté.

---

## A.3.2 Analyse documentaire

Processus structuré visant à examiner, comparer, interpréter ou valider des informations documentaires.

---

## A.3.3 Attribution

Association documentaire entre une information et son auteur supposé ou identifié.

---

## A.3.4 Authenticité

Correspondance entre un contenu analysé et sa forme originale documentée.

---

## A.3.5 Citation

Reproduction textuelle attribuée à une source identifiée ou supposée.

---

## A.3.6 Complétude documentaire

Évaluation du degré d'achèvement documentaire d'une unité d'analyse.

---

## A.3.7 Confiance documentaire

Évaluation synthétique de la robustesse documentaire d'une conclusion.

Synonyme autorisé :

```text
Niveau de confiance
```

---

## A.3.8 Consensus documentaire

Position soutenue par la majorité des sources crédibles disponibles.

---

## A.3.9 Contexte documentaire

Ensemble des circonstances nécessaires à l'interprétation correcte d'une information.

---

## A.3.10 Corpus documentaire

Ensemble structuré d'unités documentaires organisé selon une méthode commune.

---

## A.3.11 Donnée

Observation, mesure ou valeur utilisée dans une analyse documentaire.

---

## A.3.12 État documentaire

Niveau de validation atteint pour une source.

---

## A.3.13 Exactitude

Degré de correspondance entre une information et les éléments documentaires disponibles.

---

## A.3.14 Format documentaire

Structure normalisée utilisée pour présenter un objet documentaire.

---

## A.3.15 Hypothèse

Explication plausible n'ayant pas encore atteint un niveau de validation suffisant pour être présentée comme un fait.

---

## A.3.16 Information inexistante

Information dont l'existence n'est pas documentée.

---

## A.3.17 Information introuvable

Information recherchée mais non localisée malgré les démarches documentaires effectuées.

---

## A.3.18 Information non disponible

Information dont l'existence est connue mais dont l'accès est impossible ou restreint.

---

## A.3.19 Limitation documentaire

Facteur réduisant la portée, la robustesse ou la précision d'une conclusion documentaire.

---

## A.3.20 Métadonnée documentaire

Information descriptive associée à un objet documentaire.

---

## A.3.21 Niveau de complétude documentaire

Classification du degré d'achèvement documentaire d'une unité.

Valeurs autorisées :

```text
Complet

Partiellement complet

Incomplet
```

---

## A.3.22 Niveau de confiance

Mesure synthétique de la robustesse documentaire.

Échelle officielle :

```text
★★★★★ Très élevé

★★★★☆ Élevé

★★★☆☆ Modéré

★★☆☆☆ Faible

★☆☆☆☆ Très faible
```

---

## A.3.23 Niveau de preuve

Évaluation de la force documentaire soutenant une affirmation ou une conclusion.

Valeurs autorisées :

```text
Élevé

Modéré

Faible
```

---

## A.3.24 Niveau global de confiance

Évaluation synthétique de la robustesse documentaire d'un ensemble d'unités documentaires.

Le niveau global de confiance est distinct du niveau de confiance d'une unité individuelle.

---

## A.3.25 Niveau global de complétude documentaire

Évaluation du degré d'achèvement documentaire d'un corpus ou d'une analyse globale.

Le niveau global de complétude documentaire est distinct du niveau de complétude d'une unité individuelle.

---

## A.3.26 Référence

Description structurée permettant de retrouver une source.

---

## A.3.27 Référence complète

Référence contenant l'ensemble des informations disponibles permettant l'identification d'une source.

---

## A.3.28 Référence courte

Référence condensée permettant l'identification rapide d'une source.

---

## A.3.29 Référence Web

Référence comportant une ressource accessible en ligne.

---

## A.3.30 Source

Origine documentaire utilisée dans une analyse.

---

## A.3.31 Source primaire

Source produite directement par l'auteur, l'organisme ou l'entité étudiée.

Exemples :

* ouvrage original ;
* lettre ;
* discours ;
* rapport officiel ;
* article scientifique original.

---

## A.3.32 Source secondaire

Source analysant, commentant ou interprétant une source primaire.

---

## A.3.33 Source secondaire spécialisée

Source secondaire produite dans un cadre spécialisé ou académique.

---

## A.3.34 Source secondaire générale

Source secondaire destinée à un public général.

---

## A.3.35 Source tertiaire

Source compilant principalement des sources secondaires.

---

## A.3.36 Statut d'attribution

Résultat de l'évaluation documentaire d'une attribution.

Valeurs autorisées :

```text
Authentifiée

Probable

Contestée

Non attribuable
```

---

## A.3.37 Synthèse documentaire

Présentation consolidée des conclusions d'une analyse comportant plusieurs unités documentaires.

---

## A.3.38 Traçabilité

Capacité à identifier l'origine documentaire d'une information.

---

## A.3.39 Traduction adaptée

Traduction modifiée afin d'améliorer la compréhension ou l'uniformité documentaire.

---

## A.3.40 Traduction libre

Traduction privilégiant le sens général plutôt qu'une correspondance textuelle stricte.

---

## A.3.41 Traduction personnelle

Traduction produite spécifiquement pour une analyse donnée.

---

## A.3.42 Traduction publiée

Traduction diffusée par une autorité documentaire, un éditeur ou un traducteur identifié.

---

## A.3.43 Unité documentaire

Objet documentaire analysé individuellement dans le cadre d'une étude ou d'un corpus.

---

## A.3.44 Uniformité documentaire

Principe exigeant que les unités comparables soient documentées selon les mêmes règles.

---

## A.3.45 Validation documentaire

Processus visant à évaluer la qualité et la robustesse d'une information documentaire.

---

## A.3.46 Vérifiabilité

Capacité d'un tiers indépendant à reproduire une vérification documentaire.

---

# A.4 États documentaires officiels

Les états documentaires autorisés sont :

```text
Non retrouvée

Identifiée

Consultée

Validée
```

---

# A.5 Niveaux de classification documentaire

Pour les corpus documentaires :

## Niveau A

Attribution fortement documentée.

---

## Niveau B

Attribution plausible mais incomplètement documentée.

---

## Niveau C

Attribution contestée, marginale ou insuffisamment documentée.

---

# A.6 Autorité du glossaire

Le présent glossaire constitue l'autorité terminologique du Référentiel documentaire canonique

Toute modification future d'une définition doit être propagée à l'ensemble du référentiel afin de maintenir la cohérence documentaire.

---

# Fin de l'Annexe A




# Source : annexes/Annexe B.md

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





# Source : annexes/Annexe C.md

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





# Source : annexes/Annexe D.md

# Annexe D — Rapport de conformité documentaire
## Référentiel documentaire canonique

---

# D.1 Objet

La présente annexe définit le format officiel de rapport de conformité documentaire du Référentiel documentaire canonique

Le rapport de conformité permet :

* d'évaluer l'application des directives ;
* de documenter les vérifications effectuées ;
* de signaler les limitations ;
* d'améliorer la traçabilité ;
* de faciliter l'audit documentaire.

---

# D.2 Principe fondamental

Toute réponse documentaire importante devrait pouvoir être accompagnée d'un rapport de conformité.

Le rapport constitue un résumé méthodologique de l'analyse réalisée.

---

# D.3 Objectifs du rapport

Le rapport doit permettre d'identifier :

* le mode documentaire utilisé ;
* les directives appliquées ;
* les formats utilisés ;
* les sources consultées ;
* les limitations documentaires ;
* le niveau de conformité obtenu.

---

# D.4 Niveaux de conformité

## Conforme

Toutes les directives applicables ont été exécutées.

Aucune non-conformité détectée.

---

## Partiellement conforme

Certaines exigences n'ont pas pu être satisfaites.

Les écarts sont documentés.

---

## Non conforme

Les exigences minimales du référentiel ne sont pas satisfaites.

Le résultat ne doit pas être présenté comme pleinement conforme.

---

# D.5 Structure officielle du rapport

## Format minimal

```text
RAPPORT DE CONFORMITÉ

Objet documentaire :

Mode détecté :

Directives appliquées :

Format utilisé :

Sources identifiées :

Sources consultées :

Niveau de preuve :

Niveau de confiance :

Niveau de complétude documentaire :

Limitations :

Conformité :
```

---

# D.6 Rapport de conformité — Citation

## Modèle

```text
RAPPORT DE CONFORMITÉ

Objet documentaire :
Citation

Mode détecté :
Validation de citation

Directives appliquées :
C
D
E
G
H
J

Format utilisé :
H.3 Citation

Sources identifiées :
Oui

Sources consultées :
Oui

Statut d'attribution :
Authentifiée

Niveau de confiance :
★★★★★ Très élevé

Niveau de complétude documentaire :
Complet

Limitations :
Aucune limitation majeure identifiée

Conformité :
Conforme
```

---

# D.7 Rapport de conformité — Étude

## Modèle

```text
RAPPORT DE CONFORMITÉ

Objet documentaire :
Étude

Mode détecté :
Analyse scientifique

Directives appliquées :
C
E
F
H
J

Format utilisé :
H.4 Étude

Sources identifiées :
Oui

Sources consultées :
Oui

Niveau de preuve :
Élevé

Niveau de confiance :
★★★★☆ Élevé

Niveau de complétude documentaire :
Complet

Limitations :
Limites méthodologiques documentées

Conformité :
Conforme
```

---

# D.8 Rapport de conformité — Affirmation

## Modèle

```text
RAPPORT DE CONFORMITÉ

Objet documentaire :
Affirmation

Mode détecté :
Vérification d'affirmation

Directives appliquées :
C
E
H
J

Format utilisé :
H.5 Affirmation

Sources identifiées :
Oui

Sources consultées :
Partiellement

Niveau de preuve :
Modéré

Niveau de confiance :
★★★☆☆ Modéré

Niveau de complétude documentaire :
Partiellement complet

Limitations :
Source primaire non retrouvée

Conformité :
Partiellement conforme
```

---

# D.9 Rapport de conformité — Corpus documentaire

## Modèle

```text
RAPPORT DE CONFORMITÉ

Objet documentaire :
Corpus documentaire

Mode détecté :
Création de corpus

Directives appliquées :
C
D
E
F
G
H
I
J

Format utilisé :
H.7 Corpus documentaire

Nombre d'unités :
XX

Classification documentaire :
Niveau A
Niveau B
Niveau C

Niveau global de confiance :
Élevé

Niveau global de complétude documentaire :
Partiellement complet

Limitations :
Certaines unités demeurent incomplètement documentées

Conformité :
Conforme
```

---

# D.10 Vérification de conformité

Avant de déclarer une réponse conforme, vérifier :

```text
□ Objet documentaire identifié

□ Mode documentaire identifié

□ Directives applicables sélectionnées

□ Format approprié utilisé

□ Sources identifiées

□ Références présentes

□ Niveau de confiance indiqué

□ Niveau de complétude indiqué

□ Limitations documentées
```

---

# D.11 Vérification avancée

Lorsque pertinent :

```text
□ Attribution documentée

□ Traduction documentée

□ Variantes documentées

□ Analyse de fiabilité présente

□ Synthèse documentaire présente

□ Classification documentaire présente
```

---

# D.12 Journal des limitations

Toute limitation importante doit être enregistrée.

## Types de limitations

### Documentation incomplète

Informations manquantes.

---

### Source primaire absente

Source originale non retrouvée.

---

### Référence incomplète

Métadonnées insuffisantes.

---

### Attribution incertaine

Documentation contradictoire ou insuffisante.

---

### Traduction non validée

Qualité ou provenance de traduction incertaine.

---

# D.13 Rapport simplifié

Lorsque la demande est simple, le format suivant peut être utilisé.

```text
Conformité :
Conforme

Niveau de confiance :
★★★★☆

Niveau de complétude :
Complet

Limitations :
Aucune limitation majeure
```

---

# D.14 Rapport complet recommandé

Pour les analyses importantes, utiliser :

```text
RAPPORT DE CONFORMITÉ

Objet documentaire

Mode détecté

Directives appliquées

Format utilisé

Sources identifiées

Sources consultées

Sources validées

Niveau de preuve

Niveau de confiance

Niveau de complétude documentaire

Limitations

Écarts documentaires

Conformité finale
```

---

# D.15 Critères d'audit

Un auditeur documentaire doit être capable d'identifier :

* les règles appliquées ;
* les sources utilisées ;
* les formats utilisés ;
* les niveaux attribués ;
* les limitations reconnues ;
* la conformité finale.

---

# D.16 Compatibilité

Les rapports de conformité doivent pouvoir être exportés vers :

```text
Markdown

DOCX

PDF

HTML

CSV

JSON

Système RAG

Base de connaissances
```

---

# D.17 Autorité du rapport

Les modèles définis dans la présente annexe constituent les formats officiels de rapport de conformité du Référentiel documentaire canonique

Toute implémentation future doit demeurer compatible avec ces modèles.

---

# Fin de l'Annexe D


