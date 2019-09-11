===================================================================
 Annexe technique : Héberger des pages Web sur le serveur de l'IUT
===================================================================

Votre répertoire personnel
++++++++++++++++++++++++++

Vous disposez d'un répertoire spécial dans votre répertoire personnel (Z:)
nommé ``public_html``.

Toutes les pages Web qui s'y trouvent sont visibles à l'adresse :

http://iutdoua-web.univ-lyon1.fr/~votrelogin

où ``votrelogin`` correspond à votre identifiant étudiant (pxxxxxxx).

.. important::

    Ce site n'est accessible que depuis le réseau filaire de l'université.

    Pour y accéder depuis Eduroam ou depuis chez vous,
    vous devrez utiliser un VPN.


Accéder à votre répertoire en FTP
+++++++++++++++++++++++++++++++++

Si vous souhaitez modifier les fichiers présents dans votre espace personnel depuis l'extérieur, il est possible de se connecter au serveur de l'IUT en suivant le protocole FTP.

Vous pouvez utiliser un outil comme `FileZilla`__ pour envoyer des fichiers en FTP.

Les paramètres de connexion sont les suivants :

* Hôte : iutdoua-samba.univ-lyon1.fr
* Port : 990
* Protocole : FTP - Protocole de Transfert de Fichiers
* Chiffrement : Connexion FTP explicite sur TLS
* Mode d'auth. : Demander le mot de passe

__ https://filezilla-project.org/

Alternative
+++++++++++

* Créez un projet sur la forge GitLab de l'université : https://forge.univ-lyon1.fr/,
  en sélectionnant *Create from template*,
  et en choisissant le modèle "Pages/Plain HTML".

* Clonez ce projet sur votre machine,
  et ajoutez à vos fichiers (HTML, CSS, images...) dans le répertoire `public`.
  Faite ensuite un *commit* et un *push*.

* Depuis la page de votre projet sur la forge,
  consultez (dans le menu de gauche) ``Setting > Pages``;
  vous devriez voir un message de la forme :

    Congratulations! Your pages are served under:
   
    http://votre_identifiant.pages.univ-lyon1.fr/votre_projet

* Chaque fois que vous ferez un *push* sur la branche ``master``,
  ce site sera automatiquement mis à jour (avec éventuellement un petit délais).

* NB: par défaut, ce site n'est accessible qu'aux personnes authentifiées (avec un compte Lyon1).
  Il est possible de le rendre public en allant dans ``Settings > General > Visibility, project features, permissions``,
  et en changeant la valeur de ``Pages access control`` à ``Everyone``.
  