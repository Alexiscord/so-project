from obtenerRecursos import uso_mem, uso_cpu, uso_hdd, status_service
import json, time, sqlite3

file = open('resultados.txt','a+')
varDate= "Date: " + time.strftime("%c")
varRam = "Ram: " + uso_mem()
varCPU = "CPU Usage: " + uso_cpu()[2]
varHDD = "Hard Disks: " + uso_hdd()[1]
varServ = "Estado SSH: " + status_service()

miQuery = "INSERT INTO tblData (ram, cpu, hd, status) VALUES("+varRam+", "+varCPU+", "+varHDD+", "+varServ+")"

con = sqlite3.connect(":infra:")
cursor = con.cursor()
print "Conexion abierta"

cursor.execute(miQuery)
con.commit()
print "Valores insertados"

con.close()
print "Conexión Cerrada"

file.write(varDate+"\n")
file.write(varRam+"\n")
file.write(varCPU+"\n")
file.write(varHDD+"\n")
file.write(varServ+"\n")
file.write("\n")
file.close()
