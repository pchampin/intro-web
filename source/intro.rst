:tocdepth: 2

============================
 Historique et présentation
============================

.. ifslides::

   .. include:: credits.rst.inc

Internet
========

Qu'est-ce qu'Internet?
----------------------

Un ensemble de réseaux informatiques locaux utilisant les mêmes protocoles de bas niveau standards (TCP/IP) et formant un réseau global.

.. figure:: _static/InternetMonde.*
    :height: 15ex
           
    Image © portices.fr__

__ http://www.portices.fr/formation/Res/Internet/Res/InternetMonde.gif


Applications d'Internet
-----------------------

* courrier électronique
* partage de fichiers pair-à-pair (P2P)
* *chat*
* ...
* le World Wide Web


Le World Wide Web (WWW)
------------------------

Un espace d'information global et décentralisé,
basé sur la navigation par hypertexte_.

.. _hypertexte: http://en.wikipedia.org/wiki/Hypertext

.. note::

   Beaucoup d'applications d'Internet utilisent aujourd'hui le Web
   comme interface utilisateur,
   ce qui rend plus floue la différence entre le Web et Internet.




Histoire du Web
===============

partielle et subjective...


Vannevar Bush (1880-1974)
-------------------------

.. figure:: _static/bush.jpg
   :height: 20ex

   Source image `Wikimedia commons`__

   Memex, `As We May Think`__ (1945)

__ http://commons.wikimedia.org/wiki/File:Vannevar_Bush_portrait.jpg
__ http://www.ps.uni-saarland.de/~duchier/pub/vbush/vbush-all.shtml


After the Memex
---------------

.. figure:: _static/first_mouse.jpg
   :height: 20ex

   Source image `Wikipedia`__

   Devinez-vous ce que c'est ?

__ http://en.wikipedia.org/wiki/File:Firstmouseunderside.jpg


Douglas Engelbart (1925-2013)
-----------------------------

.. figure:: _static/engelbart.jpg
   :height: 20ex

   Source image `Wikimedia commons`__

   La souris, les interfaces graphiques

__ http://commons.wikimedia.org/wiki/File:Douglas_Engelbart_in_2008.jpg

.. TODO link 'les interfaces graphiques' to mother of all demos

Ted Nelson (1937-)
------------------

.. figure:: _static/nelson.jpg
   :height: 20ex

   Source image `Wikipedia`__

   Projet Xanadu, « Hypertexte »

__ http://en.wikipedia.org/wiki/File:Ted_Nelson_cropped.jpg



Tim Berners-Lee (1955-)
-----------------------

.. figure:: _static/bernerslee.jpg
   :height: 20ex

   Source image `Mayem @ Flickr`__

   Le World Wide Web, le W3C

__ http://www.flickr.com/photos/mayhem/3353514936


The WWW Consortium (W3C)
------------------------

.. figure:: _static/logo-w3c.png
   :alt: logo W3C
 
   http://www.w3.org/

   “Lead the web to its full potential”

* consortium d'entreprises, d'universités...
  (dont l'`Université de Lyon`_)

* standardisant des technologies ouvertes et libres de droits

.. _Université de Lyon: http://www.universite-lyon.fr/


Steve Jobs (1955-2011)
-----------------------

.. figure:: _static/jobs.jpg
   :height: 20ex

   Source image `Wikimedia commons`__

   Smartphones, Web mobile

__ http://commons.wikimedia.org/wiki/File:Steve_Jobs_Headshot_2010-CROP.jpg


Autres chronologies
-------------------

* `Evolution of Web Design`_
* `The Evolution of the Web`_
* `The History of HTML5`_

.. _Evolution of Web Design: http://blog.kissmetrics.com/evolution-of-web-design/
.. _The Evolution of the Web: http://evolutionofweb.appspot.com/
.. _The History of HTML5: http://www.wix.com/blog/2012/07/the-authentic-infographic-history-of-html5/




Composants du Web
=================

* HTTP
* URLs
* HTML

(à vos souhaits !)



.. index:: HTTP

HTTP
----

* HyperText Transfer Protocol (`RFC 2616`_).

* Décrit comment les données du Web sont échangées entre machines.

* Vous l'étudierez plus en détail l'an prochain...

  * ... mais il faut en savoir un minimum.

.. _RFC 2616: http://datatracker.ietf.org/doc/rfc2616/


HTTP (terminologie)
-------------------

.. rst-class:: small

* **Ressource** :
  toute unité d'information (document, image, vidéo...) accessible sur le Web.

* **Serveur** :
  un ordinateur « contenant » des ressources, toujours connecté à Internet.

* **Client** :
  un ordinateur/smartphone/tablette... utilisé pour afficher des ressources.

.. figure:: _static/client-server.png
   :height: 8ex  

   Source image http://commons.wikimedia.org/wiki/File:Client-server-model.svg



.. index:: URL

URLs
----

* Uniform Resource Locator (`STD 66`_)
* Structure :

.. figure:: _static/url-structure.*
   :width: 80%

   ..

* N'importe qui peut lier à n'importe quoi

.. _STD 66: http://datatracker.ietf.org/doc/rfc3986/

.. rst-class:: small

  NB : les URLs sont parfois appelés URIs ou IRIs → même chose


HTML
----

.. image:: _static/logo-html5.*
   :class: float-right
   :width: 3em

* HyperText Markup Language (HTML5_)
* Décrit comment les données peuvent être intéreprétées par le client

.. note::

  HTML est le langage *principal* du Web, mais ce n'est pas le seul : CSS, Javascript, XML...

  Cette année nous verrons essentiellement HTML et CSS

HTML (suite)
------------

.. rst-class:: small 

* HTML Tags (1991)
* HTML+ (1993) : tables, formulaires
* HTML 2.0 (1995) : :RFC:`1866`
* HTML 3.2 (1997) : recommandation W3C
* HTML 4.0 (1998) : séparation fond-forme (CSS)
* XHTML (2000) : syntaxe plus (trop?) stricte
* HTML5 (2004→) : applications web

Large compatibilité entre les versions.


.. _HTML5: http://www.w3.org/TR/html5/



À quoi bon ?
============

Pourquoi ...
------------

\... apprendre le HTML alors que presque personne aujourd'hui n'écrit du HTML directement ?

Les gens utilisent des traitements de texte |WYSIWYG| et des générateurs.


Parce que...
------------

.. rst-class:: compact

* les générateurs HTML ne permettent pas de tout faire
* le HTML généré a souvent besoin d'être retouché à la main
* vous pouvez être amenés à *écrire* des générateurs
* vous pouvez être amenés à écrire des programmes qui *consomment* du HTML (pour le traiter ou l'afficher)



Et que...
---------

Le WYSIWYG n'est pas idéal pour HTML :

* HTML n'est pas (plus) un langage de présentation :

  * HTML décrit la *structure logique* des pages,
  * c'est CSS qui doit être utilisé pour décrire leur *présentation*.


Et enfin...
-----------

* Cette séparation entre fond et forme permet d'adapter l'affichage à de multiplies clients :

  * écran d'ordinateur de bureau
  * ordinateur portable
  * tablette
  * smartphone
  * smart TV
  * ...

  → `responsive design`__

__ http://en.wikipedia.org/wiki/Responsive_design



.. |WYSIWYG| raw:: html

   <abbr title="What You See Is What You Get">WYSIWYG</abbr>



Vos outils
++++++++++

* un éditeur de texte (e.g. Notepad++) pour éditer vos fichiers HTML,
* un navigateur moderne pour les visualiser.



.. slide:: Fin de la `seance1`:ref:
   :level: 2
   :class: nav-seance

   Vers la `seance2`:ref:.
