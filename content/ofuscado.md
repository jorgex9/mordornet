Title: Hola Mundo! Ofuscado
Date: 2017-07-03 03:40
Category: About
Tags: php, ofuscar, código ofuscado


Cuando estamos en etapa de desarrollo, una de las mejores y buenas practicas es hacer nuestro código lo mas legible posible (buena identación, respetar las formas de nombrar variables, métodos y clases) ademas de acompañar de buenos comentarios. Esto hace que con el paso del tiempo y el cambio de 
desarrolladores, el código sea entendible y mantenible con facilidad.

Pero también podemos pensar en hacer todo lo contrario "Ofuscar nuestro código , es decir, el código ofuscado es aquel tan intrincado, enredado, enrevesado y confuso que resulta prácticamente imposible entenderlo incluso para quien lo escribió  Esto se usa mucho en el desarrollo de software malicioso (malware), generadores de spam y sitios web fraudulentos.

## Veamos un caso practico en C++

Un ejemplo básico es llamar a las variables y funciones con palabras reservadas mas algún símbolo. Entonces definimos en **C++** una variable del tipo int de nombre **int_**
```c++
    int _int;
```

Ahora veamos la forma de escribir una función en C++ de nombre _int que recibe como parámetro un entero y devuelve un valor del tipo long, que siempre va a ser cero.

```c++
    long int _int(int int_){return int_-int_};
```

## Ahora vamos a ver mas de codigo ofuscad opero en PHP :)

el clasico *Hola Mundo!*: 
```php
<?php echo 'Hola Mundo!'; ?>;
```
Ofuscar transformando a caracteres en octal. Se antepone \ para identificar un caracter octal 
```php
<?php echo "\110\157\154\141\40\155\165\156\144\157\41"; ?>;
```
Ofuscar transformando a caracteres hexadecimales. Se antepone \x para identificar un caracter hexadecimal.

```php
<?php echo "\x48\x6f\x6c\x61\x20\x6d\x75\x6e\x64\x6f\x21"; ?>
```

Funciones recomendadas para realizar la transformación

* ```decoct(ord("A"))``` : *decoct* devuelve una cadena que contiene una representación octal del argumento dado y *ord* devuelve el valor ASCII de un caracter
* ```dechex(ord("A"))``` : *dechex* devuelve una cadena que contiene una representación hexadecimal del argumento dado.

Entonces también podemos usar una mezcla 
```php
<?php  echo "\110\x6f\154\x61\40\x6d\165\x6e\144\x6f\41"; ?>
```

un paso mas. Cambiemos echo por la función printf y a esta por una variable
veamos paso a paso...

```php
<?php
printf ("\110\x6f\154\x61\40\x6d\165\x6e\144\x6f\41");
$i8238im432 = "printf";
$i8238im432("\110\x6f\154\x61\40\x6d\165\x6e\144\x6f\41");
?>
```

y aun mas! vamos a comprimir nuestro código y cifrar en base64, para ello usaremos ```gzdeflate``` y ```base64_encode```. Tengan en cuenta que aquí nuestro codigo debe ir sin las tags ```<?php  ?>``` 

```php
<?php printf(base64_encode(gzdeflate('printf("Hola Mundo!");'))); ?>
```

esto nos devolverá nuestro código ofuscado
```
KyjKzCtJ01DyyM9JVPAtzUvJV1TStAYA
```
ahora lo vemos en ejecución
```php
<?php eval (gzinflate(base64_decode('KyjKzCtJ01DyyM9JVPAtzUvJV1TStAYA'))); ?>
```
Un poco mas y si cambiando de nombres las variables base64_decode, gzinflate y obtenemos nuestro Hola Mundo! mas ofuscado?

```php
<?php
$a07f983d5a12b4="\142\x61\163\x65\66\x34\137\x64\145\x63\157\x64\145";
$a92384nasdkj3="\147\172\151\156\146\154\141\164\145";
eval($b92384nasdkj3($a07f983d5a12b4('KyjKzCtJ01DyyM9JVPAtzUvJV1TStAYA')));
?>

```
Esto no termina allí, se puede ofuscar tanto como uno pueda. Existen torneos de ofuscación como el IOCCC (International Obfuscated C Code Contest) que es un torneo internacional de ofuscación en C. [Aquí](http://pastebin.com/sXXyUtEu) pueden ver el código de un simulador de vuelo del torneo 

En la red podemos encontrar software que automatizan esta tarea, ofuscando tanto el código, como programa objeto. También existen lenguajes de programación llamados esotéricos como BrainFuck donde podemos ver obras de artes como esta versión del famoso juego de la vida! (juego del cual derivo el logo de la cultura hacker)
[htp://pastebin.com/pgKmeTeK](http://pastebin.com/sXXyUtEu)

**un Hola Mundo! interesante... no?**

<img src="https://nemeronwriter.com/wp-content/uploads/bfi_thumb/espada92-33kwgf0tnwi1npwu9dds0a.jpg" class="responsive-image">