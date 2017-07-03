Title: dmenu
Date: 2017-06-19 21:33
Category: About
Tags: dmenu, debian

Hay mucha gente que prefiere tener lanzadores a un click de distancia, pero para muchos (como yo) alejarse del teclado al mouse implica un esfuerzo extra. Así que a la hora de lanzar una aplicación lo que prefiero es usar **dmenu**.

dmenu es rapido, dinamic


o y ligero para entornos X, originalmente diseñado para [dwm](http://dwm.suckless.org/) (un manejador de ventanas que espero pronto escribir sobre el, es especial porque he probado dwmX y me entusiasma mucho).  

## Instalación
En la familia de debian dmenu esta incluido en los paquetes suckless-tools

```
# apt-get install suckless-tools
```

## Configuración
Una vez instalado es recomendable configurar teclas de acceso rápido a dmenu. Esto puede hacerlo vía las configuraciones de su entorno gráfico (Gnome, KDE, XFCE, Openbox, etc). En mi caso como uso Openbox la configuración la hago en el archivo ** ~.config/openbox/rc.xml**
Mas precisamente de esta manera:

```
<keybind key="A-F3">
      <action name="Execute">
        <startupnotify>
          <enabled>false</enabled>
          <name>dmenu-bind</name>
        </startupnotify>
        <command>~/.config/dmenu/dmenu-bind.sh</command>
      </action>
    </keybind>

```
Como ven, el comando que ejecuta apunta a ** ~/.config/dmenu/dmenu-bind.sh**, este es un script donde he configurado las opciones de como se lanzara mi dmenu. Entre algunas de las opciones que pueden configurar son: Color de letra, color de fondo, tipo de letra, color de selección, posición, etc.
Ahora les muestro mi configuración:

```
#!/bin/bash
#
# written for nigromancer @nigrobyte based on Bunsenlabs
#
# -nb    normal background colour
# -nf    normal foreground colour
# -sb    selected background colour
# -sf    selected foreground colour
#
# -b    place menu at bottom (otherwise top)
#
# See 'man dmenu' for more information.

USAGE="\n  To start dmenu at the top or bottom of the screen,\n\
  add or remove -b in the dmenu_run command in dmenu-bind.sh.\n\
  -b     locate at bottom\n\n\
  To change colours, edit the options:\n\n\
  -nb    normal background colour\n\
  -nf    normal foreground colour\n\
  -sb    selected background colour\n\
  -sf    selected foreground colour\n\n\
  Get all configuration options with 'man dmenu'.\n"

if [[ $# = 1 ]]; then
    case $1 in
        -h|--help   ) echo -e "$USAGE"
        exit 0;;
        *           ) echo -e "\n  Invalid command argument\n"
        exit 1;;
    esac
fi

dmenu_run -b -i -nb '#151617' -nf '#FF9C00' -sb '#FF9C00' -sf '#151617' -fn 'monofur for Powerline Regular-10'

```
Se ve de la siguiente manera:

<img src="http://i.imgur.com/Vcfn1uG.png"  class="responsive-image"/>

Por si no lo notan, es el lanzador que se ve en la parte de abajo del escritorio. XD

> Saludos, y espero vayan dejando de lado el mouse y ganando velocidad al lanzar sus aplicaciones.

<img src="https://upload.wikimedia.org/wikipedia/en/0/0c/The_Mouth_of_Sauron.jpg" class="responsive-image">

