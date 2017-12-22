:orphan:

===========
Projet 2017
===========

L'objectif de votre projet est de produire, en binôme,
une maquette de site marchand.
Ce sera une *maquette* dans le sens où les fonctionnalités coté serveur
(recherche, passage de commande) seront simulées.

Voici la liste des pages que votre maquette devra, au minimum, comporter :

* une page de garde, affichant un message de bienvenue et les promotions en cours,
  et offrant un champs de recherche ;
* une page simulant un résultat de recherche, affichant une liste d'articles ;
* une page détaillée d'article, incluant une description,
  la possibilité de laisser un commentaire, et d'ajouter l'article à son panier ;
* une page de validation de commande, permettant de saisir les coordonnées de livraison ;
* une page "Qui sommes-nous ?" présentant le site.

Votre site doit être **responsive**:
il doit s'adapter à la largeur de l'écran,
afin de présenter une ergonomie *différente* (et appropriée)
sur un écran d'ordinateur et sur un smartphone.

Vous fournirez (selon les modalités définies par votre enseignant⋅e) :

* l'URL à laquelle son projet est accessible
  (par exemple dans votre `public_html <iut>`:doc:),
* l'URL d'un dépôt GIT (par exemple sur github_, gitlab_ ou bitbucket_)
  contenant les fichiers du projet (et démontrant un minimum d'utilisation), et
* une archive contenant tous les fichiers du projet,

avant le **29/12/2017 23:59**.
tout retard entraînera un malus sur la note.

.. _github: https://github.com
.. _gitlab: https://gitlab.com/
.. _bitbucket: https://bitbucket.org

Quelques indications
++++++++++++++++++++

* Votre maquette utilisera exclusivement du HTML et du CSS
  (pas de Javascript ou de PHP).

* Vous pouvez utiliser des extraits de HTML ou de CSS trouvés sur le Web,
  à condition de *citer vous sources* (URL d'origine en commentaire).

* Pensez-bien à utiliser les valideurs du W3C pour le code `HTML`_ et `CSS`_\ ;
  un site ne passant pas le valideur (sans erreur *ni warning*) recevra une note **en dessous de la moyenne** !

* Comme tout site marchand, votre projet devra avoir un aspect uniforme d'une
  page à l'autre.

* Les pages que vous créez doivent être liées les unes aux autres de manière
  à simuler de manière cohérente la navigation à l'intérieur du site.
  Notez que, même si certaines pages (page de garde, résultat de recherche)
  contiennent des liens vers des articles différents, tous ces liens peuvent
  pointer vers l'unique page détaillée d'article que l'on vous demande
  d'écrire.

* L'organisation des fichiers de votre site doit respecter les bonnes pratiques
  vues en cours.

* Pour simuler un formulaire, il suffit d'utiliser l'adresse de la
  page résultat comme attribut ``action`` de la balise ``<form>``.

* Si vous travaillez seul⋅e,
  vous êtes dispensé⋅e de réaliser la page "résultat de recherche"
  et la page "qui sommes-nous ?".

.. _HTML: http://validator.w3.org/
.. _CSS: http://jigsaw.w3.org/css-validator/
