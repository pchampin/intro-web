:tocdepth: 2

======
 HTML
======

.. include:: commondefs.rst.inc
.. ifslides::

   .. include:: credits.rst.inc



Un langage à balises
====================



.. index:: balise
   see: tag; balise
   see: markup language; langage à balise

Notion de balise
++++++++++++++++

* HTML est un format textuel,

  * il peut donc être édité dans n'importe quel éditeur de texte.

* Le texte normal sera affiché tel quel.

* Les **balises** sont des codes, qui ne sont pas affichés tels quels,
  mais servent à indiquer le rôle du texte balisé,

  * et donc *indirectement* comment il sera présenté.

.. admonition:: Vocabulaire

  En anglais, les balises sont appelées `tags`:eng:;
  « langage à balise » se traduit par `markup language`:eng:.



Exemple
-------

Si vous écrivez ::

       Qu'est-ce qu'une <em>balise</em>?

.. container:: build

  .. container::

    \... vous verrez :

    .. raw:: html

     <p class="rendered">
       Qu'est-ce qu'une <em>balise</em>?
     </p>

    Le mot « balise » est marqué comme important (em = emphase),
    c'est pourquoi il est affiché en italique.



.. index:: chevron
   see: bracket; chevron
   single: balise; ouvrante
   single: balise; fermante

Structure des balises
+++++++++++++++++++++

.. code-block:: html

   Qu'est-ce qu'une <em>balise</em>?

* Tout texte entre les **chevrons** (en anglais `brackets`:eng:) ``<`` et ``>``
  est considéré une balise.

* ``<em>`` est une balise *ouvrante*,
  ``</em>`` est la balise *fermante* qui lui correspond;
  elles délimitent le texte concerné.

.. tip::

   Les éditeurs de texte reconnaissent les balises,
   et les mettent automatiquement en couleur
   pour faciliter la lecture du code HTML.



.. index:: emboîtement

Emboîtement
-----------

.. image:: _static/matroshka.jpg
   :height: 15ex
   :align: right
   :alt: http://commons.wikimedia.org/wiki/File:Russian-Matroshka2.jpg
   :class: float-right

On peut appliquer plusieurs balises au même texte,
à condition de respecter la règle d'**emboîtement** :

toute balise B ouverte à l'intérieur d'une balise A
doit également être fermée à l'intérieur de A.

Exemples :

.. code-block:: html

   <X>Emboîtement <Y>correct</Y></X>.

.. code-block:: html

  <X>Emboîtement <Y>incorrect</X></Y>.



.. index:: arbre

.. _structure_en_arbre:

Structure en arbre
------------------

De la règle d'emboîtement,
il découle que les balises confèrent une structure d'**arbre** au document :

.. rst-class:: big
.. code-block:: html

  <X><Y>Lorem <Z>ipsum</Z></Y> dolor <X>sit.</X></X>

.. graphviz::

   graph  {

     X -- Y
      Y -- Lorem
      Y -- Z
       Z -- ipsum
     X -- dolor
     X -- X2
       X2 -- "sit."

     X  [ label="<X>", shape=box, style=rounded ]
     Y  [ label="<Y>", shape=box, style=rounded ]
     Z  [ label="<Z>", shape=box, style=rounded ]
     X2 [ label="<X>", shape=box, style=rounded ]

     Lorem  [ shape=elipse, style=filled ]
     ipsum  [ shape=elipse, style=filled ]
     dolor  [ shape=elipse, style=filled ]
     "sit." [ shape=elipse, style=filled ]

   }


.. index:: attribut

Attributs
---------

Certaines balises, en plus du contenu textuel qu'elles délimitent,
ont besoin d'information supplémentaire
(mais qui n'apparaîtra pas dans le document).

Cette information est donnée par des **attributs**,
qui ont la forme ``nom=valeur``
et sont placés *entre les chevrons* de la balise ouvrante,
après son nom.

Par exemple ::

  <a href="http://champin.net/">P-A. Champin</a>

n'affichera que le texte « P-A. Champin ».



.. index:: balise; vide

.. _balisevide:

Balises vides
-------------

Certaines balises particulières n'attendent pas de contenu textuel.
Ces balises **vides** n'ont donc pas de balise fermante correspondante ::

  Cette balise <Y a="v"> n'a pas de contenu.

On peut (mais ce n'est pas une obligation) indiquer explicitement
l'absence de balise fermante en ajoutant la barre oblique
à la fin de la balise ouvrante ::

  Cette balise <Y a="v"/> n'a pas de contenu.



Gestion des espaces
+++++++++++++++++++

Si vous écrivez ::

     Gestion      des
     espaces.

.. container:: build

  .. container::

    \... vous verrez :

    .. raw:: html

     <p class="rendered">
       Gestion      des
       espaces.
     </p>



.. index:: espaces

Explication
-----------

HTML considère tous les caractères d'espacements
(espaces, retours à la ligne...)
comme des séparations entre mots,
et les affiche comme une *simple espace*.

Cela donne de la souplesse dans la mise en page du *code* HTML
(notamment en utilisant l'*indentation*, comme en programmation).

On va voir dans la suite comment faire afficher des retours à la ligne.



.. index:: structure logique, structure phyisique, fond / forme,
           feuille de style

Séparation fond / forme
+++++++++++++++++++++++

Depuis la version 4, HTML vise a décrire la *structure logique* du document,
c'est à dire le **fond** et non la **forme**.

La mise en forme (qu'on appelle parfois *structure physique*) est gérée par
une **feuille de style** qui sera décrite en `css`:doc:.



Structure d'un document
=======================


.. _structure_globale:

Structure globale
+++++++++++++++++

.. code-block:: html
  :linenos:

  <!DOCTYPE html>
  <html>
    <head>
      <title>Titre du document</title>
      <meta charset="utf-8"/>
    </head>
    <body>
      ...
    </body>
  </html>



.. index:: <html>, <head>, <body>, <title>, charset

Explication
-----------

* La 1e ligne indique la version de HTML (ici, HTML5).
* Tout document html (`<html>`:html:) comprend deux parties.

  - La tête (`<head>`:html:) contient les méta-données,
    qui ne sont pas directement affichées :

    * le titre (`<title>`:html:) est obligatoire,
    * l'indication d'encodage (ligne 5) est facultative,
      mais recommandée ;

  - Le corps (`<body>`:html:) contient
    le contenu à proprement parler du document.

.. note::

   On remarque que l'indication d'encodage est un exemple
   de balise sans contenu et possédant un attribut.


Valideur
--------

Le W3C fournit un service de validation en ligne :

  http://validator.w3.org/

Son utilisation vous est *vivement* recommandée.


Titres et paragraphes
+++++++++++++++++++++

Un document typique est une séquence de

* titres (ou en-tête, en anglais `heading`:eng:), et de
* paragraphes.

Les titres ont différents niveaux d'importance,
repérables à leur typographie (et parfois à leur numérotation).

.. container:: build

  .. admonition:: Question

     Identifiez-vous les différents niveaux de titre dans l'exemple suivant ?



Exemple
-------

.. figure:: _static/exo_structure/sujet.png
   :width: 100%
   :class: shadow



.. index:: <p>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>

Titres et paragraphes en HTML
-----------------------------

* Les paragraphes sont délimités par la balise `<p>`:html:
* Les titres sont délimités par les balises `<h1>`:html:, `<h2>`:html:..., `<h6>`:html: ;

  * `<h1>`:html: est le niveau le plus important,
    et `<h6>`:html: le moins important.

Illustration ::

   <h1>Ceci est un titre</h1>
   <p>Ceci est un paragraphe.</p>
   <p>Ceci est un deuxième paragraphe.</p>



Illustration plus élaborée
``````````````````````````
.. rst-class:: big
.. code-block:: html

   <h1>Thèse</h1>
     <p>Paragraphe d'introduction</p>
     <h2>Argument 1</h2>
       <p>...</p> <p>...</p> <p>...</p>
     <h2>Argument 2</h2>
       <p>...</p> <p>...</p> <p>...</p>
   <h1>Antithèse</h1>
     <h2>Contre-argument 1</h2>
       <p>...</p> <p>...</p> <p>...</p>
     <h2>Contre-argument 2</h2>
       <p>...</p> <p>...</p> <p>...</p>
   <h1>Synthèse</h1>
     <p>...</p> <p>...</p> <p>...</p>

Notez l'indentation pour faciliter la lecture.



Cohérence
---------

⚠ L'enchaînement des niveaux de titre doit être cohérent :

* le premier titre devrait toujours être de niveau 1 ;
* un titre ne devrait pas monter de plus d'un niveau par rapport au précédent.

.. warning::

   « Mais si le `<h2>`:html: ne se différencie pas assez du `<h1>`:html:
   visuellement, j'ai le droit de mettre un `<h3>`:html: à la place ? »

   → non; HTML doit être cohérent avec la *structure* du document.
   Pour changer la typographie, on modifiera plutôt le `css`:doc:.

Cohérence (suite)
`````````````````

NB : ces règles de cohérence ne sont pas *normatives*,
leur non-respect n'est *pas* signalé par le valideur,
mais il est tout de même à proscrire.

.. warning::
   C'est donc à vous d'être attentifs à bien les respecter.



.. _exo_catane:

Exercice
````````

#. Téléchargez le `texte`__ correspondant à l'`exemple ci-avant`__
   en utilisant les balises `<p>`:html: et `<hN>`:html:.

   __ _static/exo_structure/texte.txt
   __ _static/exo_structure/sujet.png

   NB : la mise en forme sera différente,
   mais chechez surtout a reproduire la structure *logique* du document.

#. Téléchargez le `modèle HTML`__ correspondant à l'exemple,
   et recopiez votre code à l'intérieur de la balise `<body>`:html: .
   Ce modèle contient un lien vers la feuille de style appropriée.
  
   __ _static/exo_structure/modele.html

Dans les deux cas, ne tenez pas compte pour l'instant
des mots en gras, italique et souligné.



Sections
++++++++

Les titres définissent en fait une structure de plus haut niveau :

* chaque titre indique le début d'une *section*,
* qui se termine au prochain titre de même niveau ;

Une section contient donc

  * un titre,
  * éventuellement des paragraphes,
  * éventuellement une ou plusieurs section(s) de niveau suivant.



.. index:: <section>

Sections en HTML
----------------

* Jusqu'à HTML 4.01, la structuration en sections était laissée implicite.

* Depuis HTML5, on `peut`:del: est encouragé à utiliser
  la balise `<section>`:html:,

  * d'autant que les anciens navigateurs l'ignoreront purement et simplement.



Arbre avec des sections implicites
``````````````````````````````````

.. rst-class:: big
.. graphviz::

   graph {
     node  [ shape=elipse, style=filled ]

     body -- h1_1 -- "Thèse"
     body -- p_1 -- "...1"
     body -- h2_1 -- "Argument 1"
     body -- p_2 -- "...2"
     body -- p_3 -- "...3"
     body -- h2_2 -- "Argument 2"
     body -- p_4 -- "...4"
     body -- p_5 -- "...5"
     body -- h1_2 -- "Anti-thèse"
     body -- h2_3 -- "Contre-argument 1"
     body -- p_6 -- "...6"
     body -- p_7 -- "...7"
     body -- h2_4 -- "Contre-argument 2"
     body -- p_8 -- "...8"
     body -- p_9 -- "...9"
     body -- h1_3 -- "Synthèse"
     body -- p_10 -- "...10"

     body [ label="<body>", shape=box, style=rounded ]
     h1_1 [ label="<h1>", shape=box, style=rounded ]
     h1_2 [ label="<h1>", shape=box, style=rounded ]
     h1_3 [ label="<h1>", shape=box, style=rounded ]
     h2_1 [ label="<h2>", shape=box, style=rounded ]
     h2_2 [ label="<h2>", shape=box, style=rounded ]
     h2_3 [ label="<h2>", shape=box, style=rounded ]
     h2_4 [ label="<h2>", shape=box, style=rounded ]
     p_1 [ label="<p>", shape=box, style=rounded ]
     p_2 [ label="<p>", shape=box, style=rounded ]
     p_3 [ label="<p>", shape=box, style=rounded ]
     p_4 [ label="<p>", shape=box, style=rounded ]
     p_5 [ label="<p>", shape=box, style=rounded ]
     p_6 [ label="<p>", shape=box, style=rounded ]
     p_7 [ label="<p>", shape=box, style=rounded ]
     p_8 [ label="<p>", shape=box, style=rounded ]
     p_9 [ label="<p>", shape=box, style=rounded ]
     p_10 [ label="<p>", shape=box, style=rounded ]

     "...1" [ label="..." ]
     "...2" [ label="..." ]
     "...3" [ label="..." ]
     "...4" [ label="..." ]
     "...5" [ label="..." ]
     "...6" [ label="..." ]
     "...7" [ label="..." ]
     "...8" [ label="..." ]
     "...9" [ label="..." ]
     "...10" [ label="..." ]

   }


Illustration avec sections
``````````````````````````
.. rst-class:: big
.. code-block:: html

   <section>
     <h1>Thèse</h1>
     <p>Paragraphe d'introduction</p>
     <section>
       <h2>Argument 1</h2>
       <p>...</p> <p>...</p> <p>...</p>
     </section><section>
       <h2>Argument 2</h2>
       <p>...</p> <p>...</p> <p>...</p>
     </section>
   </section><section>
     <h1>Antithèse</h1>
     <section>
       <h2>Contre-argument 1</h2>
       <p>...</p> <p>...</p> <p>...</p>
     </section><section>
       <h2>Contre-argument 2</h2>
       <p>...</p> <p>...</p> <p>...</p>
     </section>
   </section><section>
   <h1>Synthèse</h1>
     <p>...</p> <p>...</p> <p>...</p>
   </section>



Arbre avec des sections explicites
``````````````````````````````````
.. rst-class:: big
.. graphviz::

   graph {
     node  [ shape=elipse, style=filled ]

     body -- sec1
     sec1 -- h1_1 -- "Thèse"
     sec1 -- p_1 -- "...1"
     sec1 -- sec2
     sec2 -- h2_1 -- "Argument 1"
     sec2 -- p_2 -- "...2"
     sec2 -- p_3 -- "...3"
     sec1 -- sec3
     sec3 -- h2_2 -- "Argument 2"
     sec3 -- p_4 -- "...4"
     sec3 -- p_5 -- "...5"
     body -- sec4
     sec4 -- h1_2 -- "Anti-thèse"
     sec4 -- sec5
     sec5 -- h2_3 -- "Contre-argument 1"
     sec5 -- p_6 -- "...6"
     sec5 -- p_7 -- "...7"
     sec4 -- sec6
     sec6 -- h2_4 -- "Contre-argument 2"
     sec6 -- p_8 -- "...8"
     sec6 -- p_9 -- "...9"
     body -- sec7
     sec7 -- h1_3 -- "Synthèse"
     sec7 -- p_10 -- "...10"

     body [ label="<body>", shape=box, style=rounded ]
     sec1 [ label="<section>", shape=box, style=rounded ]
     sec2 [ label="<section>", shape=box, style=rounded ]
     sec3 [ label="<section>", shape=box, style=rounded ]
     sec4 [ label="<section>", shape=box, style=rounded ]
     sec5 [ label="<section>", shape=box, style=rounded ]
     sec6 [ label="<section>", shape=box, style=rounded ]
     sec7 [ label="<section>", shape=box, style=rounded ]
     h1_1 [ label="<h1>", shape=box, style=rounded ]
     h1_2 [ label="<h1>", shape=box, style=rounded ]
     h1_3 [ label="<h1>", shape=box, style=rounded ]
     h2_1 [ label="<h2>", shape=box, style=rounded ]
     h2_2 [ label="<h2>", shape=box, style=rounded ]
     h2_3 [ label="<h2>", shape=box, style=rounded ]
     h2_4 [ label="<h2>", shape=box, style=rounded ]
     p_1 [ label="<p>", shape=box, style=rounded ]
     p_2 [ label="<p>", shape=box, style=rounded ]
     p_3 [ label="<p>", shape=box, style=rounded ]
     p_4 [ label="<p>", shape=box, style=rounded ]
     p_5 [ label="<p>", shape=box, style=rounded ]
     p_6 [ label="<p>", shape=box, style=rounded ]
     p_7 [ label="<p>", shape=box, style=rounded ]
     p_8 [ label="<p>", shape=box, style=rounded ]
     p_9 [ label="<p>", shape=box, style=rounded ]
     p_10 [ label="<p>", shape=box, style=rounded ]

     "...1" [ label="..." ]
     "...2" [ label="..." ]
     "...3" [ label="..." ]
     "...4" [ label="..." ]
     "...5" [ label="..." ]
     "...6" [ label="..." ]
     "...7" [ label="..." ]
     "...8" [ label="..." ]
     "...9" [ label="..." ]
     "...10" [ label="..." ]

   }

.. note::

   À ce stade, on pourrait arguer que l'ordinateur *peut* reconstruire
   la structure des sections à partir des niveaux de titre,
   et donc qu'il est superflu d'alourdir le code HTML
   avec cette information redondante.

   Lorsqu'on étudiera `css`:doc: et les `scripts`:doc:,
   on comprendra mieux l'intérêt de rendre cette structure explicite.



.. _exo_catane2:

Exercice
````````
Améliorez votre version de l'`exemple ci-avant`__
en ajoutant les balises `<section>`:html:.

__ _static/exo_structure/sujet.png





Redondance et compatibilité
---------------------------

RMQ: l'emboîtement des sections suffit à déterminer leur niveau,
donc l'information portée par le numéro de titre est *redondante*.

→ en HTML5, on peut n'utiliser que `<h1>`:html: à tous les niveaux,

  * les navigateurs compatibles adapteront la typographie
    en fonction de la « profondeur ».

⚠ cependant, ceci n'est pas compatible avec les anciens navigateurs,
sauf à fournir une feuille de style précise.



Illustration
````````````
.. rst-class:: big
.. code-block:: html

   <section>
     <h1>Thèse</h1>
     <p>Paragraphe d'introduction</p>
     <section>
       <h1>Argument 1</h1>
       <p>...</p> <p>...</p> <p>...</p>
     </section><section>
       <h1>Argument 2</h1>
       <p>...</p> <p>...</p> <p>...</p>
     </section>
   </section><section>
     <h1>Antithèse</h1>
     <section>
       <h1>Contre-argument 1</h1>
       <p>...</p> <p>...</p> <p>...</p>
     </section><section>
       <h1>Contre-argument 2</h1>
       <p>...</p> <p>...</p> <p>...</p>
     </section>
   </section><section>
   <h1>Synthèse</h1>
     <p>...</p> <p>...</p> <p>...</p>
   </section>



.. index:: <article>, <aside>, <header>, <footer>, <nav>

Sections spécialisées
---------------------

Les balises suivantes représentent
des sections avec une sémantique particulière.

================== ===========================================
:html:`<article>`   contenu auto-suffisant
:html:`<aside>`     encart
:html:`<header>`    en-tête de la section parent (ou du doc)
:html:`<footer>`    pied de la section parent (ou du doc)
:html:`<nav>`       section contenant des liens de navigation
================== ===========================================



Exemple
```````
.. rst-class:: big
.. literalinclude:: _static/exemple-sections.html



Quelques balises utiles
+++++++++++++++++++++++

Nous allons maintenant présenter un certain nombre de balises
qui peuvent être utilisées à l'intérieur des balises de paragraphe ou de titre.



.. index:: <em>, <strong>, <dfn>, <cite>, <q>

Balises génériques
------------------

Voici quelques balises utiles, avec leur sémantique,
et leur mise en forme *par défaut*.

================== ====================== ============
 :html:`<em>`       emphase                italique
 :html:`<strong>`   emphase forte          gras
 :html:`<dfn>`      définition             aucun
 :html:`<cite>`     titre d'ouvrage        italique
 :html:`<q>`        citation               guillemets
================== ====================== ============

Exemple
```````
.. code-block:: html

   Selon <cite>Wikipedia</cite>, la <dfn>prose</dfn> est :
   <q>la forme <em>ordinaire</em> de l'expression verbale.</q>

.. raw:: html

  <p class="rendered">
   Selon <cite>Wikipedia</cite>, la <dfn>prose</dfn> est :
   <q>la forme <em>ordinaire</em> de l'expression verbale.</q>
  </p>

.. raw:: html

  <p class="rendered alt">
   Selon <cite>Wikipedia</cite>, la <dfn>prose</dfn> est :
   <q>la forme <em>ordinaire</em> de l'expression verbale.</q>
  </p>



.. index:: <code>, <kbd>, <samp>, <var>

Documentation informatique
--------------------------

Les balises suivantes sont utiles pour écrire
des documentations informatiques (ou scientifiques).

================== ====================== ============
 :html:`<code>`     code informatique      non-prop
 :html:`<kbd>`      entrée clavier         non-prop
 :html:`<samp>`     sortie de programme    non-prop
 :html:`<var>`      variable               italique
================== ====================== ============


Exemple
```````

.. code-block:: html

   La boucle <code>while</code> affiche <samp>1 2 3 4</samp>,
   soient toutes les valeurs prises par <var>i</var>.

.. raw:: html

  <p class="rendered">
   La boucle <code>while</code> affiche <samp>1 2 3 4</samp>,
   soient toutes les valeurs prises par <var>i</var>.
  </p>
   
.. raw:: html

  <p class="rendered alt">
   La boucle <code>while</code> affiche <samp>1 2 3 4</samp>,
   soient toutes les valeurs prises par <var>i</var>.
  </p>



.. index:: <ins>, <del>

Document évolutif
-----------------

Les balises suivantes sont utiles pour faire apparaître
les évolutions d'un document.

================== ====================== ============
 :html:`<ins>`      texte inséré           souligné
 :html:`<del>`      texte supprimé         barré
================== ====================== ============

Exemple
```````

.. code-block:: html

   Je <del>ne</del> connais
   <del>rien à</del><ins>bien</ins> HTML.

.. raw:: html

  <p class="rendered">
   Je <del>ne</del> connais
   <del>rien à</del><ins>bien</ins> HTML.
  </p>
   
.. raw:: html

  <p class="rendered alt">
   Je <del>ne</del> connais
   <del>rien à</del><ins>bien</ins> HTML.
  </p>



.. index:: <b>, <i>, <u>, <br>

Balises historiques
-------------------

Ces balises datent des premières versions de HTML,
où la séparation fond / forme n'était pas encore de rigueur.

============== ===============================
 :html:`<b>`    texte en gras
 :html:`<i>`    texte en italique
 :html:`<u>`    texte souligné
 :html:`<br>`    saut de ligne (sans contenu)
============== ===============================


.. warning::

   Elles sont encore valides en HTML5, (et donc acceptées par le valideur)
   mais la plupart du temps,
   il faut leur préférer une balise avec une sémantique plus précise.



.. _exo_catane3:

Exercice
````````

Reprenez votre code HTML reproduisant l'`exemple ci-avant`__,
et ajoutez les balises manquantes.

__ _static/exo_structure/sujet.png

Le rendu doit maintenant être très proche de celui de l'exemple.



Listes
======

Motivation
++++++++++

Une liste est un paragraphe d'un type particulier,
contenant une énumération d'éléments.

.. index:: <ul>, <li>

Liste non ordonnée
++++++++++++++++++

.. code-block:: html

  <ul>
    <li>sucre</li>
    <li>céréales</li>
    <li>lait</li>
  </ul> 

.. raw:: html

 <section class="rendered">
  <ul>
    <li>sucre</li>
    <li>céréales</li>
    <li>lait</li>
  </ul> 
 </section>



.. index:: <ol>

Liste ordonnée
++++++++++++++

.. code-block:: html

  <ol>
    <li>sucre</li>
    <li>céréales</li>
    <li>lait</li>
  </ol> 

.. raw:: html

 <section class="rendered">
  <ol>
    <li>sucre</li>
    <li>céréales</li>
    <li>lait</li>
  </ol> 
 </section>



Remarque
--------

On note que :

* `<ul>`:html: signifie `unordered list`:eng:
* `<ol>`:html: signifie `ordered list`:eng:
* `<li>`:html: signifie `list item`:eng:

Dans une liste ordonnée, les éléments sont *automatiquement* numérotés
(mais cette numérotation peut être contrôlée avec une feuille de style).



Styles alternatifs pour les listes
----------------------------------

.. raw:: html

 <section class="rendered alt">
  <ul>
    <li>sucre</li>
    <li>céréales</li>
    <li>lait</li>
  </ul> 
 </section>

.. raw:: html

 <section class="rendered alt">
  <ol>
    <li>sucre</li>
    <li>céréales</li>
    <li>lait</li>
  </ol> 
 </section>



Exercice
````````

Dans l'`exemple ci-avant`__ pouvez-vous identifier une liste ?
Reprenez votre code HTML reproduisant cet exemple et
modifiez-le en conséquence.

__ _static/exo_structure/sujet.png

Le rendu doit maintenant être identique à celui de l'exemple.






.. slide:: Fin de la `seance2`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance3`:ref:.



.. _liens:

Liens et contenus embarqués
===========================



.. index::
   single: URL; base
   single: URL; relative

URLs
++++

.. figure:: _static/url-structure.*
   :width: 80%

* Le nom local a une structure hiérarchique
  (similaire à la structure des fichiers).

* Comme pour les fichiers,
  on peut spécifier une URL *relativement* à une autre.
  
.. warning:: 

   Malgré cette similitude,
   les ressources ne correspondent *pas toujours* à des fichiers.


URL relative
------------

======= ================================================
""      l'URL de base
"toto"  la ressource ``toto`` dans le "dossier" courant
"."     le "dossier" courant
".."    le "dossier" parent du "dossier" courant
"/"     le "dossier" racine du serveur
======= ================================================

On peut ensuite combiner ces éléments en les séparant par "/".

Étant données une URL de base et une URL relative,
on peut calculer l'URL absolue correspondante
simplement par un jeu d'écriture.

.. note::

   Plus précisément,
   c'est une manipulation purement *syntaxique*,
   qui est donc indépendante de
   la structure des éventuels fichiers sur le serveur.

   Il est même possible que l'URL relative et le nom de fichier relatif
   donnent des résultats différents, exemple :

   * ``http://example.org/pchampin/`` correspond au répertoire
     ``/home/pchampin/public_html/`` sur le serveur ;

   * l'URL relative ``../jdoe/`` conduit à l'URL ``http://example.org/jdoe/``,
     qui correspond au répertoire ``/home/jdoe/public_html/``,

   * alors que le nom de fichier relatif ``../jdoe/`` conduit au répertoire
     ``/home/pchampin/jdoe/`` qui n'a pas d'URL correspondante
     (et d'ailleurs n'existe probablement pas).

Exercices
---------

Combinez chacune des URLs de base de gauche
avec chacune des URLs relatives de droite.

+------------------------------------+-------------------+
| URLs absolues                      | URLs relatives    |
+====================================+===================+
| * http://example.com/foo/bar/toto  | * .               |
| * http://example.com/foo/bar/tata  | * tata            |
| * http://example.com/foo/bar/titi/ | * ../tata         |
|                                    | * baz/tutu        |
|                                    | * ../../there     |
|                                    | * /somewhere/else |
+------------------------------------+-------------------+
   
Exercices (suite)
`````````````````

Considérant l'URL de base http://example.com/foo/bar/p1.html ,
donnez une URL relative pour :

* http://example.com/foo/bar/p2.html
* http://example.com/foo/assets/style.css
* http://example.com/foo/bar/img/photo.jpg
* http://example.com/global.css

.. index:: <img>, @alt, @src

Image
+++++

* Une image peut être insérée avec la balise `<img>`:html:.

* Cette balise est une `balise vide <balisevide>`:ref:

* Elle a deux attributs obligatoires :

  * `src`:html: : l'URL (absolue ou relative) de l'image,
  * `alt`:html: : une description textuelle de l'image.

.. note::

   La description textuelle est obligatoire pour les situations où l'image
   ne peut pas être affichée :

   * elle n'a pas pu être chargée,
   * elle n'est pas reconnue par le navigateur,
   * le navigateur ne peut pas afficher d'image (*e.g.* lecteur d'écran)...

Exemple
-------

.. code-block:: html

   <img src="_static/monalisa-small.jpg" alt="Portrait de Mona Lisa">

.. raw:: html

 <p class="rendered">
   <img src="_static/monalisa-small.jpg" alt="Portrait de Mona Lisa"
        style="max-width: 100%; height: 10em">
 </p>

Source image Wikipedia__

__ http://en.wikipedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg



Images et droit d'auteur
------------------------

.. warning::

  Le fait qu'une image soit disponible sur le Web ne signifie pas
  que vous avez toute latitude pour la réutiliser sur votre propre site.

Ce qu'il faut faire :

* vérifier les droits associés
  
  - au besoin, en contactant le propriétaire,

* citer les sources.

Images réutilisables
````````````````````

* Domaine publique

* `Creative Commons`__

  * réutilisables sous condition

  * `la recherche avancée de flickr`__ permet de filtre les résultats
    par license (cc)

* voyez aussi `Wikimedia Commons`__

__ http://creativecommons.org/
__ http://www.flickr.com/search/advanced/?
__ http://commons.wikimedia.org/



.. index:: <a>, @href

Liens
+++++

* La balise `<a>`:html: transforme son contenu en lien hypertexte.
* Elle doit contenir un attribut `href`:html:,
  qui contient l'URL (absolue ou relative) vers lequel dirige ce lien.

.. code-block:: html

   Bienvenue à
   <a href="http://iut.univ-lyon1.fr/">l'IUT de Lyon</a>

.. raw:: html

 <p class="rendered">
   Bienvenue à
   <a href="http://iut.univ-lyon1.fr/">
   l'IUT de Lyon
   </a>
 </p>


Contenu de la balise `<a>`:html:
--------------------------------

Rien n'empèche bien sûr la balise `<a>`:html: de contenir d'autres balises.

.. code-block:: html

   Bienvenue à
   <a href="http://iut.univ-lyon1.fr/">
     l'<strong>IUT</strong> de Lyon
     <img src="_static/logo-lyon1.jpg" alt="Logo de Lyon1" />
   </a>

.. raw:: html

 <p class="rendered">
   Bienvenue à
   <a href="http://iut.univ-lyon1.fr/">l'<strong>IUT</strong> de Lyon
   <img src="_static/logo-lyon1.jpg" alt="Logo de Lyon1"/></a>
 </p>



.. index:: fragment, @id

.. _lien_interne:

Lien interne
------------

* Il peut être utile de faire pointer un lien vers un **fragment** particulier
  d'un document plutôt que vers son intégralité.

* En HTML, toute balise délimite une partie du document.
  On peut donner un nom à ce fragment en ajoutant à la balise
  l'attribut `id`:html:.

* L'URL du fragment est constituée en concaténant :

  - l'URL du document,
  - le caractère « # », et
  - l'identifiant du fragment.

* NB : une URL relative commençant par « # » désigne donc un fragment
  du document courant.

.. note::

   Deux éléments du même document ne *peuvent pas* avoir
   la même valeur pour l'attribut `id`:html:
   (ce qui serait contradictoire avec la notion d'identifiant).

   Dans les anciennes versions d'HTML,
   on utilisait une balise vide de la forme::

     <a name="identifier">

   mais cette syntaxe est obsolète.




Exemples
````````

.. code-block:: html

  <a href="#sec1">
    pointe vers le fragment #sec1 du document courant</a>
  <a href="other.html#sec2">
    pointe vers le fragment #sec2 d'un autre document</a>
  <a href="http://en.wikipedia.org/wiki/Lyon#Details">
    pointe vers la section "Détails" d'un article
    Wikipedia</a>

  <section id="sec1">
    La section vers laquelle pointe le 1er lien ci-dessus.
    ...</section>



Organisation des fichiers
-------------------------

Lorsque le nombre de fichiers constituant un site croît,
il devient important de penser leur organisation. Quelques conseils :

* séparer les pages HTML des fichiers « utilitaires »
  (feuilles de styles, images) en plaçant ces derniers dans un sous-répertoire,

* calquer la hiérarchie des répertoires sur la structure logique du site,

* utiliser des fichiers ``index.html`` comme « point d'entrée » de chaque
  répertoire.

Exemple
```````

.. rst-class:: big tree
.. code-block:: text

   
   ├ assets/
   │ ├ style.css
   │ ├ img1.png
   │ └ ...
   ├ index.html 
   ├ page1.html
   ├ page2.html
   │
   ├ sous-site1/
   │ ├ assets/
   │ │ └ ...
   │ ├ index.html
   │ └ page2.html
   └ sous-site2/
     └ ...



.. _donjon:

Exercice : livre dont vous êtes le héros
----------------------------------------

Téléchargez `ce fichier html`__. Il contient un livre dont vous êtes le héros minimaliste.

#. Faites en une version interactive avec des liens internes.
#. Faites en une version interactive ou chaque entrée
   est une page HTML distincte.

__ _static/exo_liens/sujet.html



.. slide:: Suite la `seance4`:ref:
   :level: 2
   :class: nav-seance

   * `Positionnement en CSS <position>`:ref:
   * `Personnalisation des boîtes <boite>`:ref:



.. index:: <video>

.. _video:

Vidéo
+++++

En plus des images, HTML5 permet d'inclure des vidéos,
grâce à la balise `<video>`:html:.

.. code-block:: html

   <video src="_static/Chrome_ImF.webm">
     Ici, une vidéo représentant...
   </video>

.. raw:: html

  <div class="rendered">
   <video src="_static/Chrome_ImF.webm">
     Ici, une vidéo représentant...
   </video>
  </div>

Source vidéo : Google_.

.. _Google: http://google.com/

.. note::

   Le contenu textuel de la balise `<video>`:html:,
   affiché uniquement si le navigateur ne supporte pas cette balise,
   joue le rôle de l'attribut `alt`:html: des images.

.. index:: @autoplay, @controls, @loop, @muted, @poster

Attributs de la balise video
----------------------------

La balise video supporte les attributs suivants :

* `autoplay`:html:\ : lance la lecture automatiquement
* `controls`:html:\ : affiche l'interface de lecture
* `loop`:html:\ : reprend automatiquement la lecture à la fin de la vidéo
* `muted`:html:\ : fixe le volume sonore à 0
* `poster`:html:\ : URL d'une image à afficher avant la lecture

NB : à part `poster`:html:, ces attributs n'ont pas besoin de valeur ;
la simple *présence* de l'attribut active son effet.
Il n'est donc même pas indispensable de leur donner une valeur ;
au lieu de `autoplay=""`:html:, on peut écrire simplement `autoplay`.

Attributs de la balise video (exemple)
``````````````````````````````````````

.. code-block:: html

   <video src="_static/Chrome_ImF.webm"
          autoplay loop muted>
     Ici, une vidéo représentant...
   </video>
   <video src="_static/Chrome_ImF.webm"
          controls poster="_static/sun.png">
     Ici, une vidéo représentant...
   </video>

.. raw:: html

  <div class="rendered">
   <video src="_static/Chrome_ImF.webm"
          autoplay loop muted>
     Ici, une vidéo représentant...
   </video>
   <video src="_static/Chrome_ImF.webm"
          controls poster="_static/sun.png">
     Ici, une vidéo représentant...
   </video>
  </div>

Source vidéo : Google_, image: johnny_automatic_.

.. _johnny_automatic: http://openclipart.org/user-detail/johnny_automatic


.. index:: <source>

Problème de compatibilité
-------------------------

Les navigateurs ne supportent pas tous les même formats vidéo.
Il peut donc être nécessaire de fournir plusieurs sources alternatives
pour la même vidéo.

La balise vidéo peut donc, à la place de l'attribut `src`:html:,
contenir plusieurs balises `<source>`:html: ayant chacune :

  * un attribut `src`:html: avec l'URL d'une version de la vidéo,
  * éventuellement un attribut `type`:html: décrivant son format.

Avec les formats WebM_ et MP4_ (H264+AAC),
on couvre la grande majorité des navigateurs.

.. _WebM: http://fr.wikipedia.org/wiki/WebM
.. _MP4: http://fr.wikipedia.org/wiki/MPEG-4_Part_14

Problème de compatibilité (exemple)
```````````````````````````````````

.. code-block:: html

   <video autoplay loop muted>
     <source src="_static/Chrome_ImF.webm"
             type='video/webm; codecs="vp8, vorbis"'>
     <source src="_static/Chrome_ImF.mp4"
             type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
     Ici, une vidéo représentant...
   </video>

.. raw:: html

  <div class="rendered">
   <video autoplay loop muted>
     <source src="_static/Chrome_ImF.webm"
             type='video/webm; codecs="vp8, vorbis"'>
     <source src="_static/Chrome_ImF.mp4"
             type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
     Ici, une vidéo représentant...
   </video>
  </div>

Source vidéo : Google_.



.. _html_avance:

HTML avancé
===========

.. index:: entité

Entités
+++++++

Les caractères suivants ont une signification spéciale en HTML,
donc il faut utiliser un code spécial (*entité*) pour les afficher :

===== ============ ============
  <   ``&lt;``     lower than
  >   ``&gt;``     greater than
  "   ``&quote;``  quote
  '   ``&apos;``   apostrophe
``&`` ``&amp;``    ampersand
===== ============ ============

Autres entités
--------------

Il existe d'autres entités pour de nombreux caractères non-SCII,
par exemple ``&eacute;`` pour é, ``&Agrave;`` pour À, ``&ccedil;`` pour ç...

Cependant, HTML supporte désormais unicode,
donc ces entités ne sont plus nécessaires.
En revanchent elles nuisent à la lisibilité du code HTML.
Leur utilisation est donc déconseillée.

Commentaires
++++++++++++

En HTML, tout texte commençant par `<!--`:html: 
et se terminant par `-->`:html:
est considéré comme un commentaire.
Tout ce qu'il contient (texte et balises) sera ignoré.

.. code-block:: html

   hello <!-- 
     <strong>wonderful</strong>
   --> world

.. raw:: html

 <p class="rendered">
   hello <!-- 
     <strong>wonderful</strong>
   --> world
 </p>

Utilité
-------

Les commentaires servent à

* documenter la structure d'un document compliqué,
* cacher temporairement une partie d'un document
  (pour le debug, notamment).

Notons que le commentaire ne concerne pas que l'affichage ::

  <link rel="stylesheet" type="text/css" href="style1.css"/>
  <!--
  <link rel="stylesheet" type="text/css" href="style2.css"/>
    inhibe temporairement la 2e feuille de style -->




.. index:: <meta>

Méta-données
++++++++++++

* Les balises `<meta>`:html: sont situées dans l'élément `<head>`:html:
  du document.
* Elles contiennent des *méta-données* : des données sur le document lui-même
  (litéralement, des « données à propos des données »).

.. code-block:: html

  <meta charset="utf-8">
  <meta name="description"
        content="apprenez plus de tours en HTML">
  <meta name="author"
        content="Pierre-Antoine Champin">
  <meta name="keywords" content="html web iut">

.. note::

   On a `déjà <structure_globale>`:ref: rencontré la balise `<meta>`:html:
   pour spécifier l'encodage du document.




Méta-données pour les robots
----------------------------

Avec le nom ``robot``,
la balise `<meta>`:html: peut être utilisée
pour fournir des instrucrions aux moteurs de recherche :

* ``index/noindex``: doivent-ils indexer cette page ou non ?
* ``follow/nofollow``: doivent-ils suivre les liens ou non ?

.. code-block:: html

  <meta name="robot" content="index,nofollow">



.. index:: @lang

Langue des méta-données
-----------------------

Les méta-données peuvent être fournies dans différentes langues,
spécifiées dans l'attribut `lang`:html:
à l'aide d'un code spécifié par `BCP47`_.

.. _BCP47: http://www.ietf.org/rfc/bcp/bcp47.txt

.. code-block:: html

  <meta name="description" lang="en"
        content="learn advanced tricks in HTML">
  <meta name="description" lang="fr"
        content="apprenez plus de tours en HTML">

NB : l'attribut `lang`:html: peut en fait être utilisé
sur *n'importe quelle* balise,
y compris dans le corps (`<body>`:html:) du document.




.. index:: <div>, <span>

Span et div
+++++++++++

HTML fournit deux balises *neutres* (c.à.d. sans sémantique particulière) :

* `<span>`:html: qui s'affiche en mode `inline <inline>`:ref:, et
* `<div>`:html: qui d'affiche en mode `block <block>`:ref:.

Ces éléments sont utiles pour rajouter de la structuration au document,
notamment en portant des `classes <class>`:ref: personnalisées.

.. warning::

   Même lorsqu'on utilise des classes personnalisées,
   il est préférable de les associer, autant que possible,
   à une balise dont la sémantique est proche,
   plutôt qu'à une balise neutre.



.. slide:: Fin de la `seance5`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance6`:ref:.



.. index:: <table>, <tr>, <td>, <th>

.. _table:

Tableaux
========

Structure d'un tableau
++++++++++++++++++++++

Un tableau (ou une table) permet d'organiser des information sur deux dimensions.

Une table (`table`:eng:) est composée de lignes (`rows`:eng:),
elles-mêmes composées de cellules (`cells`:eng:).

On considère deux sortes de cellules :
les cellules d'en-tête (`header cells`:eng:) et
les cellules de données (`data cells`:eng:).

.. raw:: html

  <table class="example">
    <tr>
      <td colspan="3" class="no-border"> the table </td>
    </tr>
    <tr>
      <td colspan="3"> a row </td>
    </tr>
    <tr>
      <th> a header cell </th>
      <td> a data cell </td>
      <td> another data cell </td>
    </tr>
  </table>

Tableau en HTML
---------------

Les différents éléments d'un tableau sont représentés par 

=========== ================
table       `<table>`:html:
row         `<tr>`:html:
header cell `<th>`:html:
data cell   `<td>`:html:
=========== ================



Example
+++++++

.. code-block:: html

  <table>
    <tr>
      <td></td> <th>Medium</th> <th>Large</th>
    </tr>
    <tr>
      <th>Americano</th> <td>1.50€</td> <td>1.90€</td>
    </tr>
    <tr>
      <th>Latte</th> <td>1.90€</td> <td>2.10€</td>
    </tr>
    <tr>
      <th>Cappucino</th> <td>1.90€</td> <td>2.10€</td>
    </tr>
  </table>



Example (résultat)
------------------

.. raw:: html

  <table class="rendered example">
    <tr>
      <td></td> <th>Medium</th> <th>Large</th>
    </tr>
    <tr>
      <th>Americano</th> <td>1.50€</td> <td>1.90€</td>
    </tr>
    <tr>
      <th>Latte</th> <td>1.90€</td> <td>2.10€</td>
    </tr>
    <tr>
      <th>Cappucino</th> <td>1.90€</td> <td>2.10€</td>
    </tr>
  </table>


.. index:: @colspan, @rowspan

Cellules étendues
+++++++++++++++++

Une cellule peut s'étendre
sur plusieurs lignes (vers le bas) et/ou colonnes (vers la droite)
à l'aide des attributs `rowspan`:html: et `colspan`:html:.

.. hint::

   Dans ce cas, le nombre de `<td>`:html: ou `<th>`:html:
   pourra varier d'une `<tr>`:html: à l'autre...

.. raw:: html

  <table class="rendered example" >
    <caption>Exemple</caption>
    <colgroup><col width="25%"><col width="25%"><col width="25%"><col width="25%">
    <tr><td rowspan=2>rowspan=2<td colspan=2>colspan=2<td>.
    <tr><td>.<td colspan=2 rowspan=2>colspan=2 rowspan=2
    <tr><td>.<td>.
  </table>

.. _exo_calculette1:

Exercice
++++++++

Reproduisez le modèle ci-dessous représentant une calculatrice.

.. figure:: _static/exo_calculette/sujet_table.png
   :target: _static/exo_calculette/sujet_table.png
   :alt: calculette
   :width: 50%


.. index:: <caption>, <thead>, <tbody>, <tfoot>

Pour aller plus loin
++++++++++++++++++++

* `<caption>`:html:\ : légende du tableau (premier fils de `<table>`:html:)
* `<thead>`:html:\ : ensemble de lignes (`<row>`:html:) constituant l'en-tête (par ex. intitulés de colonnes)
* `<tbody>`:html:\ : ensemble de lignes (`<row>`:html:) constituant le corps (données à proprement parler)
* `<tfoot>`:html:\ : ensemble de lignes (`<row>`:html:) constituant le pied (par ex. rappel des intitulés de colonnes, ou somme des valeurs par colonne)
* `<colgroup>`:html: et `<col>`:html: permettent d'identifier les colonnes (par exemple pour les besoins du CSS)

Pour plus de détails, voir http://www.w3.org/TR/html5/tabular-data.html#table-model .


Tableaux et mise en pages
-------------------------

Avant que CSS ne s'impose, les tableaux ont souvent été utilisés
pour faciliter la mise en page des sites
(en tête et pied de page, menu latéral, présentation sur plusieurs colonnes).

Aujourd'hui, cette pratique est fortement déconseillée,
car elle est beaucoup moins flexible
que l'utilisation de CSS pour le `positionnement <position>`:ref:.



.. slide:: Fin de la `seance6`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance7`:ref:.



.. _form:

Formulaires et interactivité
============================

.. index:: <input>

Champs de saisie
++++++++++++++++

Certaines pages HTML comportent des **champs**
permettant à l'utilisateur de saisir de l'information.
La balise offrant cette possibilité est la balise `<input>`:html:.

.. code-block:: html

   <input>

.. raw:: html

  <p class="rendered">
   <input>
  </p>


.. index:: @type

Types de champs
---------------

HTML offre un certain nombre de types de champs,
les plus utilisés étant

.. list-table::
  :widths: 70 30

  * - ``<input type="text">``
    - .. raw:: html

         <input type="text">

  * - ``<input type="password">``
    - .. raw:: html

         <input type="password">

  * - ``<input type="checkbox">``
    - .. raw:: html

         <input type="checkbox">

  * - ``<input type="radio">``
    - .. raw:: html

         <input type="radio">

  * - ``<input type="file">``
    - .. raw:: html

         <input type="file">

NB : HTML5 définit beaucoup d'autres `types de champs`__ (par exemple ``date`` ou ``color``),
mais ils ne sont pas encore largement implémentés.

__ http://www.w3.org/TR/html5/forms.html#states-of-the-type-attribute


.. index:: <label>

Libellé
-------

Les champs de saisie sont le plus souvent associés à un libellé.

Ceci est représenté en encapsulant
le libellé (n'importe quel code HTML) *et* la balise `<input>`:html:
dans une balise `<label>`:html:.

.. code-block:: html

   <div><label>Nom : <input></label></div>
   <div><label><input type=checkbox> tarif réduit</div>

.. raw:: html

  <div class="rendered">
   <div><label>Nom : <input></label></div>
   <div><label><input type=checkbox> tarif réduit</div>
  </div>

.. note::

   Une autre méthode consiste à

   * nommer le `<input>`:html: avec l'attribut `@id`:html:, et
   * lui lier le `<label>`:html: avec l'attribut `@for`:html:.

   Par exemple :

   .. code-block:: html

      <table>
        <tr><td><label for="name">Nom :</td>
            <td><input id="name"></td></tr>
        <tr><td><label for="gname">Prénom :</td>
            <td><input id="gname"></td></tr>
      </table>

   .. raw:: html

     <div class="rendered">
      <table>
        <tr><td><label for="name">Nom :</td>
            <td><input id="name"></td></tr>
        <tr><td><label for="gname">Prénom :</td>
            <td><input id="gname"></td></tr>
      </table>
     </div>


.. index:: @placeholder

Alternative au libellé
``````````````````````

Pour les champs de type ``text`` ou ``password``,
une alternative au libellé consiste à utiliser l'attribut `@placeholder`:html:\ :

.. code-block:: html

   <input placeholder="identifiant">
   <input type="password" placeholder="mot de passe">

.. raw:: html

  <div class="rendered">
   <input placeholder="identifiant">
   <input type="password" placeholder="mot de passe">
  </div>



.. index:: <select>, <option>, @multiple

Liste
-----

Un autre type de champ permet de sélectionner (ou ou plusieurs) éléments dans une liste.

.. code-block:: html

   <select>
     <option>Georges</option>
     <option>John</option>
     <option>Paul</option>
     <option>Ringo</option>
   </select>

.. raw:: html

  <div class="rendered">
   <select>
     <option>Georges</option>
     <option>John</option>
     <option>Paul</option>
     <option>Ringo</option>
   </select>
  </div>

L'attribut `@multiple`:html: autorise la sélection de plusieurs éléments.


.. index:: <textarea>

Zone de texte
-------------

Le champ `<input>`:html: ne permet pas la saisie de texte sur plusieurs lignes.
Pour cela, on utilise le champ `<textarea>`:html:.

.. code-block:: html

  <textarea placeholder="type your message">Hello
  world</textarea>

.. raw:: html

  <div class="rendered">
  <textarea placeholder="type your message">Hello
  world</textarea>
  </div>

NB : contrairement à `<input>`:html:,
`<textarea>`:html: attend une balise fermante
(car le texte contenu dans le champ est le contenu de la balise).

.. index:: button

Bouttons
--------

La balise `<button>`:html: permet de créer des boutons.

.. code-block:: html

   <button>Ok</button> <button><em>Annuler</em></button>

.. raw:: html

  <div class="rendered">
   <button>Ok</button> <button><em>Annuler</em></button>
  </div>


.. note::

   Historiquement, les boutons étaient générés par la balise `<input>`:html:
   avec des types spécifiques (``button`` et ``submit`` notamment).


.. index:: <form>, @action

Formulaire
++++++++++

Les champs sont généralement regroupés dans une balise `<form>`:html:,
qu'on appelle un **formulaire**.

Cette balise requiert l'attribut `@action`:html:, qui contient
l'URL de la ressource qui traitera les données du formulaire.


.. index:: @name

Champs d'un formulaire
----------------------

Pour pouvoir être traités,
les champs d'un formulaire doivent tous être identifiés par un nom,
porté par l'attribut `@name`:html:\ :

.. code-block:: html

   <form action="_static/formproc/debug">
     <input name="name" placeholder="identifiant">
     <input name="tel"  placeholder="n° de tel">
     <button>Je m'inscrit</button>
   </form>

.. raw:: html

  <div class="rendered">
   <form action="_static/formproc/debug">
     <input name="name" placeholder="identifiant">
     <input name="tel"  placeholder="n° de tel">
     <button>Je m'inscrit</button>
   </form>
  </div>


.. index:: @value

Cases à cocher et boutons radio
-------------------------------

Les champs ayant le type ``checkbox`` ou ``radio`` vont souvent par groupe.
Tous les membres d'un groupe ont le même nom,
et se différencient par une **valeur** portée par un attribut `@value`:html:.

Pour les cases à cocher, le nom se voir affecter l'ensemble des valeurs sélectionnée.

Pour les boutons radio, une seule valeur peut-être affectée
(l'activation d'un bouton du groupe désactive automatiquement les autres).

Exemple (source)
````````````````

.. code-block:: html

   <form action="_static/formproc/debug">
     <p>Taille :
       <label><input name="size" type="radio" value="s"> Petite</label>
       <label><input name="size" type="radio" value="m"> Moyenne</label>
       <label><input name="size" type="radio" value="l"> Grande</label>
     </p>
     <p>Garniture :
       <label><input name="topping" type="checkbox" value="ch"> Fromage</label>
       <label><input name="topping" type="checkbox" value="ol"> Olives</label>
       <label><input name="topping" type="checkbox" value="mu"> Champignons</label>
     </p>
     <button>Commander</button>
   </form>

Exemple (rendu)
```````````````

.. raw:: html

  <div class="rendered">
   <form action="_static/formproc/debug">
     <p>Taille :
       <label><input name="size" type="radio" value="s"> Petite</label>
       <label><input name="size" type="radio" value="m"> Moyenne</label>
       <label><input name="size" type="radio" value="l"> Grande</label>
     </p>
     <p>Garniture :
       <label><input name="topping" type="checkbox" value="ch"> Fromage</label>
       <label><input name="topping" type="checkbox" value="ol"> Olives</label>
       <label><input name="topping" type="checkbox" value="mu"> Champignons</label>
     </p>
     <button>Commander</button>
   </form>
  </div>

Boutons et formulaires
----------------------

Les boutons ont trois fonctionalités possibles, portées par l'attribut `@type`:html:\ :

* ``submit``\ : envoie les données du formulaire (défaut)
* ``reset``\ : remet tous les champs du formulaire à leur valeur initiale
* ``button``\ : aucun comportement par défaut

Les boutons du dernier type sont utiles en conjonction avec des `scripts`:doc:.


.. index:: @method

Méthode
-------

La balise `<form>`:html: accepte un atttribut `@method`:html:, qui peut prendre deux valeurs :

* ``get``\ : les données sont passée *via* l'URL (défaut)
* ``post``\ : les données sont passées dans la requête HTTP

La méthode ``get`` doit être employée :

* lorsque les données ne sont pas trop volumineuses, et surtout;
* lorsque le traitement des données n'a **pas d'effet de bord**.

Dans tous les autres cas, la méthode ``post`` doit être utilisée.

.. note::

  Bien que les données du formulaire n'apparaissent pas directement avec la méthode ``post``,
  celle-ci n'est pas plus sécurisée que la méthode ``get``\ :
  les données circulent en clair sur le réseau.

  La bonne manière de faire transiter des données de manière sûre sur le Web
  consiste à utiliser le protocole HTTPS au lieu de HTTP.


Envoi de fichier
----------------

L'emploi de `<input type="file">`:html: pour envoyer le contenu d'un fichier
nécessite deux précaution au niveau du `<form>`:html: englobant :

* `method="post"`:html:
* `enctype="multipart/form-data"`:html:

sans quoi c'est le *nom* du fichier, et non son contenu, qui sera envoyé au serveur.



.. _exo_calculette2:

Exercices
+++++++++

Reprenez `votre code représentant une calculatrice <exo_calculette1>`:ref:
et améliorez le pour qu'il soit conforme au modèle ci-dessous.

.. figure:: _static/exo_calculette/sujet_form.png
   :target: _static/exo_calculette/sujet_form.png
   :alt: calculette
   :width: 45%


Exercice
--------

Expérimentez les différents types de champs
avec le processeur fourni à l'adresse suivante  :

  http://champin.net/enseignement/intro-web/_static/formproc/debug

.. slide:: Fin de la `seance8`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance9`:ref:.

.. _exo_form_debug:

