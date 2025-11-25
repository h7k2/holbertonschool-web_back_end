📌 Python Async Function – Holberton School

Ce projet introduit la programmation asynchrone en Python avec le module asyncio.
Tu vas apprendre à utiliser les coroutines, les tasks, à exécuter plusieurs fonctions en concurrence, et à mesurer leur temps d’exécution.

🧠 Learning Objectives

À la fin de ce projet, vous serez capable d’expliquer :

La syntaxe async et await

Comment exécuter un programme async avec asyncio

Comment lancer plusieurs coroutines en concurrence

Comment créer des asyncio.Task

Comment utiliser le module random

Comment mesurer un temps d’exécution async

🛠 Requirements

Ubuntu 20.04 LTS

Python 3.9

Tous les fichiers doivent :

être exécutables

respecter pycodestyle 2.5.x

avoir une documentation complète

être annotés avec des type hints

commencer par : #!/usr/bin/env python3

Éditeurs autorisés : vi, vim, emacs

Un fichier README.md est obligatoire à la racine du projet

📂 Files
0-basic_async_syntax.py

Fonction : wait_random(max_delay=10)

Coroutine asynchrone retournant un délai aléatoire entre 0 et max_delay

Utilise random.uniform() et asyncio.sleep()

1-concurrent_coroutines.py

Fonction : wait_n(n, max_delay)

Lance n fois wait_random en concurrence

Retourne la liste des délais en ordre croissant, sans utiliser sort()

Utilise asyncio.as_completed()

2-measure_runtime.py

Fonction : measure_time(n, max_delay)

Mesure le temps total d’exécution de wait_n

Retourne le temps moyen par coroutine (total_time / n)

Utilise le module time

3-tasks.py

Fonction : task_wait_random(max_delay)

Ne doit PAS être async

Retourne une asyncio.Task créée avec :

asyncio.create_task(wait_random(max_delay))

4-tasks.py

Fonction : task_wait_n(n, max_delay)

Version basée sur wait_n mais utilisant task_wait_random

Retourne une liste des délais en ordre croissant grâce à asyncio.as_completed()

▶️ Exemples d'exécution
0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769

1-main.py
[0.9, 1.0, 1.7, 3.6, 4.5]

2-main.py
1.759705400466919

3-main.py
<class '_asyncio.Task'>

4-main.py
[0.22, 1.19, 1.84, 2.14, 4.00]

✔️ Concepts utilisés

Coroutines (async)

Suspension avec await

Concurrence vs parallélisme

asyncio.sleep()

asyncio.create_task()

asyncio.as_completed()

random.uniform()
