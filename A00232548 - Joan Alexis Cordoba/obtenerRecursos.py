#Retorna el porcentaje de memoria usada
def uso_mem():
	result1 = commands.getoutput('free|grep Mem:|tr -s "'" "'" |cut -d "'" "'" -f 2')
	result2 = commands.getoutput('free|grep Mem:|tr -s "'" "'" |cut -d "'" "'" -f 3')
	result3=int(result2)*100/int(result1)
	return result3

#Retorna uso de la CPU
def uso_cpu():
	grep_process = Popen(["mpstat", "", ""], stdout=PIPE, stderr=PIPE)
	return filter(None, grep_process)
	grep_process = Popen(["sar", "1", "1"], stdout=PIPE, stderr=PIPE)
	lista = Popen(["awk", '{print $5}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None, lista)

#Retorna espacio en HD
def uso_hdd():
	rep_process = Popen(["df", "/dev/mapper/cl-root", "-h"], stdout=PIPE, stderr=PIPE)
 	lista= Popen(["awk",'{print $4}' ],stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n') 
	return filter(None, lista)

#Retornasi el servicio esta corriendo
def status_service():
	grep_process = Popen(["service", "httpd", "status"], stdout=PIPE, stderr=PIPE)
	lista = Popen(["awk", '-F', 'Active:', '{print $2}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None, lista)


