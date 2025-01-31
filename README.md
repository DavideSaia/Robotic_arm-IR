# Progetto di Implementazione di un Braccio Robotico in ROS

## Descrizione del Progetto

Questo progetto ha l'obiettivo di implementare un braccio robotico in un ambiente ROS (Robot Operating System), con particolare attenzione alla visualizzazione della trasformata tra il link "world" e l'"end effector". La trasformata rappresenta la relazione spaziale tra il sistema di riferimento globale ("world") e il punto finale del braccio robotico ("end effector"), che è cruciale per il controllo e la pianificazione del movimento del robot.

## Struttura del Progetto

Il progetto è organizzato come segue:<br>
├── CMakeLists.txt <br>
├── launch <br>
│ └── arm.launch <br>
├── package.xml <br>
├── rviz <br>
│ └── arm_description.rviz <br>
├── src <br>
│ └── tf_ef.py <br> 
└── urdf <br>
└── robot_description.urdf.xacro <br>


### File Principali

- **CMakeLists.txt**: File di configurazione per la compilazione del pacchetto ROS.
- **package.xml**: File di metadati che descrive il pacchetto ROS, incluse le dipendenze.
- **launch/arm.launch**: File di lancio ROS che avvia tutti i nodi e le configurazioni necessarie per il progetto.
- **rviz/arm_description.rviz**: File di configurazione per RViz, che permette la visualizzazione del braccio robotico e delle trasformate.
- **src/tf_ef.py**: Script Python che calcola e pubblica la trasformata tra il link "world" e l'"end effector".
- **urdf/robot_description.urdf.xacro**: File URDF (Unified Robot Description Format) che descrive la struttura del braccio robotico, inclusi i link e le giunzioni.

## Installazione e Utilizzo

### Prerequisiti

- ROS (Robot Operating System) installato e configurato.
- Pacchetti ROS necessari, come `tf`, `urdf`, `rviz`, e `xacro`.

### Installazione

1. Clona il repository del progetto nella tua workspace di ROS:
   ```bash
   cd ~/catkin_ws/src
   git clone <repository_url>
2. Compila il pacchetto:
   ```bash 
   cd ~/catkin_ws
   catkin_make
3. Aggiungi il pacchetto al tuo ambiente ROS:
   ```bash
   source devel/setup.bash

### Esecuzione


1. Avvia il file di lancio: 
   ```bash
   roslaunch <nome_pacchetto> arm.launch
2. Apri RViz per visualizzare il braccio robotico e la trasformata:
   ```bash
   rosrun rviz rviz -d $(rospack find <nome_pacchetto>)/rviz/arm_description.rviz
3. Lo script tf_ef.py pubblicherà la trasformata tra "world" e "end effector", che può essere visualizzata in RViz.


## Visualizzazione della Trasformata

La trasformata tra il link "world" e l'"end effector" è visualizzata in RViz utilizzando il plugin TF. Questo permette di vedere la posizione e l'orientamento dell'"end effector" rispetto al sistema di riferimento globale.