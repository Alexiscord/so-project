# Universidad ICESI - Sistemas Operativos - Proyecto Final
 A00232548 - Joan Alexis Córdoba Narváez

Para la realización de esta actividad se ha configurado:
<ul>
	<li>Maquina Virtual con Ubuntu Server 16.04 </li>
	<li>Memoria RAM: 2GB</li>
	<li>Disco Duro: 20GB</li>
	<li>Dos núcleos</li>
	<li>Interfaces de red: NAT, Bridge y Host</li>
</ul>

Para la configuración de las interdaces de red, se edita el archivo "interfaces" que se encuentra en /etc/network/ y se activa dchp para cada una de ellas como aparece en el archivo interfaces ubicado en este repositorio.
Luego, se reinician los servicios de red "service networking restart"

Usamos sudo ufw allow xxxx para abrir un puerto requerido, donde xxxx es el número del puerto.

Se instalan algunas dependencias requeridas por ubuntu para Python
sudo apt-get install build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Se instala SQLite:

sudo apt-get install SQLite

Al igual que en Centos, hemos de instalar Python 2.7

wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz<br>
tar xzf Python-2.7.13.tgz<br>
cd Python-2.7.13<br>
sudo ./configure<br>
sudo make install<br>

Se procede a la instalación de PIP, VirtualEnv y Flask<br>

a. Instalar virtualenv <br>
sudo apt-get install virtualenv<br>
cd ~/ <br>
mkdir envs<br>
cd envs<br>
virtualenv flask_env<br>
Activar el ambiente<br>
flask_env/bin/actívate<br>

Luego se copia los Scripts de Python creados antes en el anterior parcial (parcial dos).
Se instalan las debidas aplicaciones para que los servicios se activen y podamos obtener las salidas que esperamos
y salidas son:


	![][1]
	![][2]
	![][3]

[1]: imgs/img1.png
[2]: imgs/img2.png
[3]: imgs/img3.png
