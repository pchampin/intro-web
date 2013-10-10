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

Structure en arbre
------------------

De la règle d'emboîtement,
il découle que les balises confèrent une structure d'**arbre** au document :

.. rst-class:: big
.. code-block:: html

  <X><Y>Lorem <Z>ipsum</Z></Y> dolor <X>sit.</X></X>

.. rst-class:: big tree
.. code-block:: html

   <X>
   ├ <Y>
   │ ├ "Lorem "
   │ └ <Z>
   │   └ "ipsum"
   ├ " dolor "
   └ <X>
     └ "sit."



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
.. rst-class:: big tree
.. code-block:: html

   ├ <h1> "Thèse"
   ├ <p>  "..."
   ├ <h2> "Argument 1"
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <h2> "Argument 1"
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <h1> "Anti-thèse"
   ├ <h2> "Contre-argument 1"
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <h2> "Contre-argument 2"
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <p>  "..."
   ├ <h1> "Synthèse"
   ├ <p>  "..."
   ├ <p>  "..."
   └ <p>  "..."



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
.. rst-class:: big tree
.. code-block:: html

   ├ <section>
   │ ├ <h1> "Thèse"
   │ ├ <p> "..."
   │ ├ <section>
   │ │ ├ <h2> "Argument 1"
   │ │ ├ <p> "..."
   │ │ ├ <p> "..."
   │ │ └ <p> "..."
   │ └ <section>
   │   ├ <h2> "Argument 2"
   │   ├ <p> "..."
   │   ├ <p> "..."
   │   └ <p> "..."
   ├ <section>
   │ ├ <h1> "Antithèse"
   │ ├ <p> "..."
   │ ├ <section>
   │ │ ├ <h2> "Contre-argument 1"
   │ │ ├ <p> "..."
   │ │ ├ <p> "..."
   │ │ └ <p> "..."
   │ └ <section>
   │   ├ <h2> "Contre-argument 2"
   │   ├ <p> "..."
   │   ├ <p> "..."
   │   └ <p> "..."
   └ <section>
     ├ <h1> "Synthèse"
     ├ <p> "..."
     ├ <p> "..."
     └ <p> "..."

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

  <p class="rendered" lang="fr">
   Selon <cite>Wikipedia</cite>, la <dfn>prose</dfn> est :
   <q>la forme <em>ordinaire</em> de l'expression verbale.</q>
  </p>

.. raw:: html

  <p class="rendered alt" lang="fr">
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
   <img src="_static/monalisa-small.jpg"  alt="Portrait de Mona Lisa" style="max-width: 100%; height: 10em">
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

.. TODO

   Il faudrait ajouter quelques images au document source pour donner
   matière à les placer avec CSS ensuite.



.. slide:: Suite la `seance4`:ref:
   :level: 2
   :class: nav-seance

   * `Positionnement en CSS <position>`:ref:
   * `Personnalisation des boîtes <boite>`:ref:



.. _video:

Vidéo
+++++

TODO



.. _html_avance:

HTML avancé
===========



Entités
+++++++

TODO TRANSLATE & ADAPT

The following characters have special meaning in HTML, so a special code (*entity*) is needed to display them:

===== ============ ============
  <   ``&lt;``     lower than
  >   ``&gt;``     greater than
  "   ``&quote;``  quote
  '   ``&apos;``   apostrophe
``&`` ``&amp;``    ampersand
===== ============ ============

NB: other *entities* exist for many non-ASCII character, for example ``&eacute;`` for é, ``&Agrave;`` for À, ``&ccedil;`` for ç...

However, HTML now supports unicode, so they are not strictly necessary (and they hinder readbility).



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





Méta-données
++++++++++++

TODO TRANSLATE & ADAPT

* ``<meta>`` tags are located in the ``<head>`` of the document.
* They contain *metadata*: data about the document itself (literally: “data about the data”), usable for example by search engines.

.. code-block:: html

  <meta name="description"
        content="learn advanced tricks in HTML">
  <meta name="author"
        content="Pierre-Antoine Champin">
  <meta name="keywords" content="html web iut">

Robot meta tag
--------------

The ``robot`` meta tag can be used to provide instructions to search engines:

* ``index/noindex``: whether they should index the page itself
* ``follow/nofollow``: whether they should follow the links in the page

.. code-block:: html

  <meta name="robot" content="index,nofollow">



Language of metadata
--------------------

Metadata can be provided in different languages, specified with the ``lang`` attribute, with a language code as specified by `BCP47`_.

.. _BCP47: http://www.ietf.org/rfc/bcp/bcp47.txt

.. code-block:: html

  <meta name="description" lang="en"
        content="learn advanced tricks in HTML">
  <meta name="description" lang="fr"
        content="apprenez plus de toursen HTML">

.. note::

  The ``lang`` attribute can be used on *any* HTML tag, including inside the body.



Span et div
+++++++++++

TODO



.. slide:: Fin de la `seance5`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance6`:ref:.



.. _table:

Tableaux
========

TODO TRANSLATE & ADAPT

A table is composed of rows, which are in turn composed of cells.

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

This is described with the following tags:

=========== ===========
table       ``<table>``
row         ``<tr>``
header cell ``<th>``
data cell   ``<td>``
=========== ===========



Example (code)
++++++++++++++

.. code-block:: html

  <table>
    <tr>
      <th>Product</th> <th>Price</th> <th>Available</th>
    </tr>
    <tr>
      <td>Beer</td> <td>3€</td> <td>no</td>
    </tr>
    <tr>
      <td>Wine</td> <td>5€</td> <td>yes</td>
    </tr>
  </table>



Example (rendered)
++++++++++++++++++

.. raw:: html

  <table class="rendered example">
    <tr>
      <th>Product</th> <th>Price</th> <th>Available</th>
    </tr>
    <tr>
      <td>Beer</td> <td>3€</td> <td>no</td>
    </tr>
    <tr>
      <td>Wine</td> <td>5€</td> <td>yes</td>
    </tr>
  </table>



.. _exo_calculette1:

Exercice
++++++++

Reproduisez `ce modèle`__ représentant une calculatrice.

__ _static/exo_calculette/sujet_table.png



.. slide:: Fin de la `seance6`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance7`:ref:.



.. _form:

Formulaires et interactivité
============================

TODO



.. _exo_calculette2:

Exercice
++++++++

Reprenez `votre code représentant une calculatrice <exo_calculette1>`:ref:
et améliorez le pour qu'il soit conforme à `ce modèle`__.

__ _static/exo_calculette/sujet_form.png



.. slide:: Fin de la `seance8`:ref
   :level: 2
   :class: nav-seance

   Vers la `seance9`:ref:.
