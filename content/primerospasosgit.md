Title: Primeros pasos en Git
Date: 2017-06-30 21:33
Category: About
Tags: git, github

Git es un software de control de versiones diseñado por Linus Torvalds, pensando en la eficiencia y la confiabilidad del mantenimiento de versiones de aplicaciones cuando estas tienen un gran número de archivos de código fuente. 

# Instalación en Debian

Para la instalación solo es necesario el siguiente comando, dado que git se encuentra en repositorios.
```
 # apt-get install git 
```

luego realizar configuraciones globales para el usuario:
```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Agregar tu herrmaineta pare resolver conflictos: Git acepta kdiff3, tkdiff, meld, xxdiff, emerge, vimdiff, gvimdiff, ecmerge, y opendiff
en mi caso:
```
$ git config --global merge.tool kdiff3
```

Si quieres revizar tus configuraciones: 
```
git config --list
```

# Crear tu repositorio local

Creamos un directorio donde se alojara nuestro repositorio
ejemplo "mirepogit" : 
```
$ mkdir mirepogit
```
y nos movemos a ella: 
```
$ cd mirepogit
```
alli inicializamos el repositorio: 
```
$ git init
```

Bien con esto se crean los archivos de configuraciones internos del repositorio local.
Podemos empezar a trabajar en el ejemplo creando unos archivos:  
```
$ touch holamundo
```
Agregamos este archivo al repositorio:
```
$ git add holamundo 
```
podemos agregar recursivamente los archivos de un directorio, si es que se lo indicamos 
ejemplo: 
```
$ git add path_directorio 
```

Una forma de agregar todos los archivos del directorio en el que estamos parados es: 
```
$ git add . 
```

Ahora debemos commitiar el los cambios: 
```
$ git commit -m "este es el mensaje que se le añade al commit"
```

Con esto ya estamos trabajando localmente

# Enlazar mi repositori local con uno externo (ejemplo GitHub)

Bien primero que nada tenemos que crearnos una cuenta en github  (también puede ser en GitLab, Bitbucket o algún otro privado) . Cuando ya tenemos la cuenta creamos el repositorio vamos a obtener varios metodos para clonar este repositorio con nuestro repositorio local. Optamos por hacerlo a través de SSH.
ejemplo:  ```git@github.com:usuario/mirepogit``

> nota: primeramente debemos crear una clave SSH en nuestra computadora y añadir esta clave también a la configuración en github. En nuestra consola hacemos: 
```
$ ssh-keygen
```
De este modo creamos una clave ssh, preferentemente es recomendable ponerle contraseña al momento de crearla. En la configuraciones de cuenta de GitHub agregamos nuestra clave, ejemplo:  
```
$ cat ~/.ssh/id_rsa.pub 
```
y nos devuelve algo similar a esto: 
```
ssh-rsa AAAAB3NzaC1yc2EAAAA345345ABAAABAQCyW40wyyXVboiQCEbBNjhi3iBXAUMEuUHVOGMVA9Sk3ioeeuWG5FoiSne
uifFvKfXRild1fMXj0vCtRDJVSVS9/Cz1EQECf5ju9eHGqF+pMviifpJxfjirFo3rIy4dx7vB8FREsdfazdldQ5Crb9ijbbeaQ
95VrnEcSfJjJwGZWlz4lO+m5En3E509l5Nxax2+HVYjHyIIs7nTLl+bVMFjIRgN9nEyrmDVIVtuCm7ZKWvywwldIqDfTq3LR01
/gl5I9HRyMRAPiiTPZ55AWcNomtMJxFylknT9d8SvlfYmIB81V2XTZ/asdasda43JvVn3jOZoA7ABG90Qx6b00yYD 
usuario@host
```

Bien ahora debemos crear un nuevo repositorio en github, por ejemplo con el mismo nombre "mirepogit", una vez creado podemos obtener en la parte inferior derecha nuestro acceso por SSH; ejemplo "git@github.com:usuario/mirepogit",con este dato procedemos a enlazarlo  con nuestro repositorio local. Para ello nos paramos en la raíz de nuestro proyecto. En este ejemplo es el directorio "mirepogit" que creamos anteriormente y hacemos:
```
$ git remote add origin git@github.com:usuario/mirepogit 
```

Si todo ha salido bien con las claves publicas aquí solo nos pide la clave de nuestra llave SSH
ahora podemos traer las cosas desde nuestro repositorio en gitHub: 
```
 $ git pull origin master
```

Con esto git empieza a trabajar y nos copia las cosas que tengamos en nuestro repositorio en gitHub.

Ahora vamos a hacer lo inverso agregando las cosas desde el repositorio  local al repositorio  en gitHub
```
$ git push origin master
```

Con esto ahora podemos ver en nuestro explorador de repositorio en gitHub que nuestros archivos que fueron adheridos y commitiados localmente ahora están en gitHub.

