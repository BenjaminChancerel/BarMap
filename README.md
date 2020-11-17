# BarMap 

## Contexte :

Dans le cadre de notre première année en école d’informatique, nous devons réaliser un projet en développement algorithmique. Pour être plus précis, nous devons concevoir une application. Nous avons voulu nous démarquer de la possibilité de faire un jeu pour une application qui est plus utile qu’un jeu. Ainsi, nous avon pratique pour les étudiants du 21ème siècle que nous sommes. 
Effectivement aujourd’hui une grande majorité des personnes utilises Google Maps. Application devenue très performantes pour se déplacer et voir les activités aux alentours. De plus la vie d’étudiants est associée aux sorties entre ami(e)s notamment dans les bars. Nous avons eu donc l’idée de créer une application similaire à Google Maps pour consulter les bars aux alentours et dans Bordeaux.
Nous avons donc l’honneur de vous présenter BarMaps eu l’idée de concevoir une application 

## Sommaire 

*   [Description de l'application]
    *   [Comment s'en servir]   
*   [Organisation dans la réalisation]
    *   [Rôles]
    *   [Action mise en oeuvre]
*   [Techonologies]
*   [Structure algorihmique]

## Description de l’application : 

### Comment se servir de BarMap ?

BarMap est avant tout un outil pour localiser les différents bars de Bordeaux.
L’application se divise en plusieurs parti. Tout d’abord il y a la fenêtre d’accueil. Celle-ci consiste à vous présenter brièvement qui nous sommes et ce que nous avons fait pour vous. La page comporte 7 boutons. 

*	Le bouton « quitter » en bas à droite : vous permet de fermer l’application tout simplement 


*	Nous avons ensuite les boutons pour afficher la carte de Bordeaux : 
    *   Le bouton « Tous les bars » va vous afficher la carte de Bordeaux avec tous les bars que nous avons sélectionnés.
    *   Les boutons « Bars ☆ ☆ ☆ », « Bars ☆ ☆ ☆ ☆ », « Bars ☆ ☆ ☆ ☆ ☆ » vous montreront les bars en fonction de leur note
    *   Les boutons « Bar des quais », « Bar du centre » vous montreront les bars en fonction de leur localisation

Une fois la carte générée vous aurez la possibilité de vous déplacer sur celle-ci de cliquer sur les marqueurs.
Chaque marqueur possède des infos sur le bar en question, notamment son nom, son adresse, sa note sur Google Maps (note sur 5). De plus si vous survolez un bar avec votre souris le nombre d’étoiles s’affichera. 

## Organisation dans la réalisation :

### Rôles : 

Pour la réalisation de ce projet nous nous sommes réparti le travail. M. Dupuis a pris en charge l’algorithmie et la création de la carte tandis que M. Chancerel a pris en charge la fenêtre graphique et la rédaction de la base de données.
Ce projet nous a demandés beaucoup de coordination. Nous avons mis en place un contrôle du travail de l’autre pour éviter les égarements (chaque week-end et à chaque cours avec John). Ainsi nous avons pu avancer ensemble en restant coordonner dans la réalisation de ce projet.

### Action mise en œuvre :

Malgré la coordination et la répartition du travail nous avons dû respecter certaines étapes importantes pour mener à bien notre projet.
Nous sommes d’abord passées par une longue phase de recherche pour déterminer la procédure et les outils nécessaire dans la réalisation de ce projet. Une fois la procédure et les outils acquis nous avons commencé la conception. Comme nous vous l’avons dit M. Dupuis c’est chargé de l’algorithmie tandis que M. Chancerel a pris en charge la fenêtre graphique et la base de données. Nous avons ensuite mis en place la version finale de notre application après avoir corriger les bugs découverts lors de la phase de test.

## Technologies :

Pour la création de ce projet nous avons fait appels à différentes technologies notamment différents langages. Des langages telles que Le python (la majeure partie de l’application), le json qui nous a permis de créer la base de données, l’HTML et le javascript qui nous ont permis de créer la carte.
Nous nous sommes servis de folium et de webbrowser pour la carte. La fenêtre graphique est faite grâce à tkinter. De plus la bibliothèque PIL nous as permit d’alimenter le design de la fenêtre avec une image.

## Structure algorithmique :

La clé de notre application est avant tout notre document python. En effet chaque bouton appelle une fonction. Et chaque fonction récupère les informations d’un fichier json pour modifier le document html et ainsi modifier la carte en fonction du bouton sur lequel vous avez cliqué.

