# rendezvous-churn-ledger

## Français

Mesurer les déplacements de clés lors d’un changement de placement distribué.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m rendezvous_churn_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Compare les placements top-r d’un hachage rendezvous classique avant/après changement de nœuds. Les clés et IDs utilisent un encodage à longueurs préfixées et SHA-256, indépendant du hash Python.

### Limites

Nœuds non pondérés et placement déterministe hors ligne ; ne mesure ni charge réelle, latence, rééquilibrage distribué ou disponibilité. Ordre des réplicas et ensemble de réplicas distingués.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Measure key movement when distributed placement changes.

Synthetic data; no network access or secret required.

```sh
python -m rendezvous_churn_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compares top-r placements of classical rendezvous hashing before/after node changes. Keys and IDs use length-prefixed SHA-256, independent of Python hash randomization.

### Limits

Unweighted nodes and offline deterministic placement; no actual load, latency, distributed rebalance or availability measurement. Replica order and replica membership are distinguished.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Medir movimiento de claves al cambiar la ubicación distribuida.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m rendezvous_churn_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Compara ubicaciones top-r de hashing rendezvous clásico antes/después de cambios de nodos. Claves e IDs usan SHA-256 con longitudes prefijadas, independiente del hash Python.

### Límites

Nodos sin pesos y ubicación determinista fuera de línea; no mide carga, latencia, reequilibrio distribuido o disponibilidad reales. Distingue orden y pertenencia de réplicas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.eecs.umich.edu/techreports/cse/96/CSE-TR-316-96.pdf
