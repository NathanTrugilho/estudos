import socket
MEU_IP = '192.168.0.10'  
 # Endereco IP do Servidor, '' = significa que ouvira em todas as interfaces

MINHA_PORTA = 8000  
# Porta que o Servidor vai ouvir 

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)sockets, #socket.SOCK_STREAM=usaremos TCP

#x = 1
testa_mensagem = ''
MEU_SERVIDOR = (MEU_IP, MINHA_PORTA) 
tcp.bind(MEU_SERVIDOR)
 # faz o bind do ip e a porta para que possa comecar a ouvir

tcp.listen(1) 
#comeca a ouvir

conexao, docliente =tcp.accept()
print ("o cliente = ", docliente, " se conectou")
#pega o ip do cliente que conectou

while 1:
 Mensagem_Recebida = conexao.recv(1024)
 #Mensagem recebida do cliente 
 if testa_mensagem != Mensagem_Recebida:  
 #aqui verifica se exite mensagem nova  
  print ("Recebi = ",Mensagem_Recebida," , Do cliente", docliente)

conexao.close()
#fim do socket