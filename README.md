# API_Restaurant Backend_test
Développement d'une Api pour permettre le fonctionnement d'une application web dédier a un restaurant

--Objectifs
   deffinir la logique metier de l'application d'un restaurant

--Listes des routes disponible via l'Api

/api/orders     #route de récuperation des commandes
/api/beverages           #route de récuperation des différentes boissons
/api/dishes             #route de récuperation des differents plats
/api/create/dish        #route de création de d'un plat
/api/create/beverage     #route de création d'une boisson
/api/menu/{date_of}         #route de récuperation du ménu en fonction de la date

--Base de donnnes et ORM

    -ORM
	mappage classe python est fait est faite depuis le module "schemas.py"
	mappage en tuble de communication avec la base faite depuis le module "models.py"
	
    -Definiton d'une connexion avec une base de donneés MySQL depuis le moduule "database.py" et creation creation des session locales

