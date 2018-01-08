:orphan:

================
Plan des séances
================

.. ifslides::

   .. include:: credits.rst.inc



.. _seance1:

Séance 1
========

* `intro`:doc:

.. _seance2:

Séance 2
========

* `Bases de HTML <html>`:doc:
  (jusqu'à `l'exemple «Règle du jeu» <exemple_regle_du_jeu>`:ref:)

.. _seance3:

Séance 3
========

* `Balises HTML <balises_html>`:ref: (jusqu'aux listes, incluses)

.. _seance4:

Séance 4
========

* `Bases de CSS <css>`:doc: (jusqu'aux sélecteurs complexes, inclus)

.. _seance5:

Séance 5
========

* `Classes et identifiants <class>`:ref:
* `Liens et images en HTML <liens>`:ref:

.. _seance6:

Séance 6
========

* `Livre dont vous êtes le héros <donjon>`:ref:
* `Organisation des fichiers <orga_fichiers>`:ref:
* `Marge et positionnement <position>`:ref:
* `Positionnement avancé <position2>`:ref:

.. _seance7:

Séance 7
========

* `Personnalisation des boîtes <boite>`:ref:
* `Images de fond <background>`:ref:
* `Modes d'affichage <block>`:ref:
* `Vidéo en HTML <video>`:ref:

.. _seance8:

Séance 8
========

* `HTML avancé <html_avance>`:ref:
* `Tableaux <table>`:ref:

.. _seance9:

Séances 9
=========

* `Pseudo-classes et pseudo-éléments <pseudos>`:ref:

.. _seance10:
.. _seance11:

Séances 10 et 11
================

* `Formulaires et interactivités <form>`:ref:

.. _seance12:

Séance 12
=========

* `Adaptation au media <media>`:ref:


Projet
======

* Deux séances seront consacrées au travail sur le `projet <projet>`:doc:.


.. pour mémoire, le plan que j'avais initialement prévu

    Il y a 14 séances de 2h (+2h sur la typographie).

    Les exercices de « thème » consistent à écrire du code HTML étant donné une image du rendu souhaité. Parfois, le CSS sera fourni, parfois il faudra l'écrire en même temps que le HTML. Si le texte est long, on pourra fournir le contenu textuel sans balise. Sur certains exercices de thème, on pourra aussi fournir le HTML et l'image du rendu, et demander aux étudiants d'écrire simplement le CSS.

    #. Intro et historique + début de la séance suivante
    #. Structure d'un document HTML

       * notion de langage à balise
       * niveaux de titre hn
       * p
       * sections
       * éléments inlines (em, strong, ...)

         * expliquer que b, i, etc... sont banis

       * listes
       * exercices de thème (documents purement textuels)
       * ---
       * structure complète d'un document HTML

         * sans rentrer dans le détail de ce qu'on met dans le head pour l'instant
       * valideur HTML -> les forcer à l'utiliser
       * exercices de thème (dans un modèle fournissant le CSS)

         * et du coup des petits pièges
           (e.g. choisir le bon entre strong, em et def)
       * ---
       * si il y a le temps, parler d'autres balises de structuration :
         nav, header, footer, article, asidde...

       * exercice de thème avec ces balises (par exemple site d'information)

         * avec des styles bien différents pour chaque type de balise,
           afin qu'ils voient s'ils se trompent et comprennent le rôle
           de chaque

         * également, le CSS pourrait faire du positionnement un peu sophistiqué
           (article sur plusieur colonnes, aside en flottant...),
           histoire de bien leur montrer que la présentation est indépendante du
           contenu

    #. CSS :

       * principes de base
       * mise en forme de base (font-*, text-*, padding, margin)
       * sélecteurs, règles de priorité

         * exercices avec des sélecteurs un peu compliqués

           * coloriage magique ?

       * valideur CSS
       * classes et id

         * nécessite d'introduire la notion d'attributs en HTML
         * rôle des classes et des ids en HTML et leur utilisation en CSS
         * exercice TODO trouver une idée


    #. liens et images

       * lien

         * attribut href
         * URL relative, URL absolue
         * bonnes pratiques d'organisation des fichiers
         * liens interne avec id=
         * ---
         * exercice : faire un mini "livre dont vous êtes le héros"

       * image

         * balise dans contenu ("auto-fermante")
         * positionnement des images avec CSS (display inline/block, float)
       *
    #. HTML avancé

       * balise vidéo
         * analogies et différences avec la balise image

       * autr
         * entités
         * commentaires
         * head
         * exercices ?

    #. évaluation intermédiaire ?
    #. tables
       * balises de tables

         * utilisation appropriée des th

       * exercices de thème

         * soit en leur laissant écrire le CSS
         * soit en leur donnant un CSS un peu sophistiqué,
           par exemple avec des :nth-child,
           ce qui fera une transition avec le chapitre suivant

       * tables avancées

         * column group
         * fusion de cellules

    #. pseudo-classes et transitions CSS
       * :hover :visited :target

         * exercices: refaire le livre dont vous êtes le héros en un seul fichier

       * :first-child & co.

         * exercice sur les tables

       * :before et :after, :counters

         * exercices sections

    #. formulaires et interfaces utilisateur
       * balises HTML5 de champs de saisie
       * exemple simple de formulaire (en fournissant le script)

    #. formulaires et interfaces utilisateur (suite)

    #. scripts - 1
       * http://blython.info/
       * explication du principe des scripts
       * exercices sur les contrôles de validité dans le formulaire de la séance précédente...
    #. scripts - 2
       * changement dynamique de classe (et donc de style CSS)

         * combiné avec les transitions CSS

       * création dynamique de contenu

         * utilisation d'AJAX minimal (en fournissant le script?)

    #. DS -> DS commun?
