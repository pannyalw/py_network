import paramiko
import time

ip = '192.168.80.253'
username = 'ruijie'
password = 'ruijie@123'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ip, username=username, password=password, look_for_keys=False)
command = ssh_client.invoke_shell()

print("已成功登录交换机" + ip)

command.send('conf t\n')
command.send('interface loop 0\n')
command.send('ip add 1.1.1.1 255.255.255.255\n')
command.send('end\n')
command.send('wr mem\n')
time.sleep(5)

output = command.recv(65535).decode('ascii')
print(output)
ssh_client.close()
