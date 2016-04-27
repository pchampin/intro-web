:orphan:

===========
Projet 2016
===========

L'objectif de votre projet est de produire, en binôme,
une maquette de site marchand.
Ce sera une *maquette* dans le sens où les fonctionnalités coté serveur
(recherche, passage de commande) seront simulées.

Voici la liste des pages que votre maquette devra, au minimum, comporter :

* une page de garde, affichant un message de bienvenue et les promotions en cours,
  et offrant une fonction de recherche ;
* une page de résultat de recherche, affichant une liste d'articles ;
* une page détaillée d'article, incluant une description,
  la possibilité de laisser un commentaire, et d'ajouter l'article à son panier ;
* une page de validation de commande, permettant de saisir les coordonnées de livraison ;
* une page "Qui sommes-nous ?" présentant le site.

IMPORTANT :
la présentation de votre site devra s'adapter à la largeur de l'écran,
afin de présenter une ergonomie différente (et appropriée)
sur un écran d'ordinateur et sur un smartphone.

Pensez-bien à utiliser les valideurs du W3C pour le code `HTML`__ et `CSS`__\ ;
une partie de votre noté dépend d'eux !

__ http://validator.w3.org/
__ http://jigsaw.w3.org/css-validator/


Chaque binôme renseignera sur Tomuss__

* l'URL à laquelle son projet est accessible, et
* l'URL d'un dépôt GIT (par exemple sur github_, gitlab_ ou bitbucket_)
  contenant les fichiers du projet (et démontrant un minimum d'utilisation),

avant le **lundi 13 juin 2016 à 23:59**\ ;
tout retard entraînera un malus sur la note.

__ https://tomuss.univ-lyon1.fr//2016/Printemps/info_6s1-2

.. _github: https://github.com
.. _gitlab: https://gitlab.com/
.. _bitbucket: https://bitbucket.org
        
Quelques indications
++++++++++++++++++++

* Votre maquette utilisera exclusivement du HTML et du CSS
  (pas de Javascript ou de PHP).

* Comme tout site marchand, votre projet devra avoir un aspect uniforme d'une
  page à l'autre.

* Les pages que vous créez doivent être liées les unes aux autres de manière
  à simuler de manière cohérente la navigation à l'intérieur du site.
  Notez que, même si certaines pages (page de garde, résultat de recherche)
  contiennent des liens vers des articles différents, tous ces liens peuvent
  pointer vers l'unique page détaillée d'article que l'on vous demande
  d'écrire.

* Pour simuler un formulaire, il suffit d'utiliser l'adresse de la
  page résultat comme attribut ``action`` de la balise ``<form>``.
  

