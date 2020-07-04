import paramiko
import os



""" class mySSHClient(paramiko.SSHClient):
    def put_dir(self, source, target):
        self. """




def send_dir(server,user,pas,src,dest):
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))
    ssh.connect(server,username=user,password=pas)
    sftp=ssh.open_sftp()
    sftp.mkdir(dest)
    local=os.path.split(src)
    local_root=local[0]
    remote=os.path.split(dest)
    remote_root=remote[0]
    
    
    print(local_root)
    print(remote_root)

    
    
   
    for(root, dirs, files) in os.walk(src):
        
        if(root.startswith(local_root)):
            path=root[len(local_root):]#seperates the prefix, aka the common dir for local and remote 
        print('PATH:' + path )
        print('Root: ' + root)
        print('Dirs: ' + str(dirs))
        print(files)


        for d in dirs:
            
            sftp.mkdir(remote_root + os.path.join(path,d)) #concatenation of the main dir + the relative path
        for f in files:
            sftp.put(os.path.join(root, f), (remote_root + os.path.join(path,f)))
        
    

        

        

   
    sftp.close()
    ssh.close()
    return 1


def send_file(server,user,pas,src,dest):
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))
    ssh.connect(server,username=user,password=pas)
    sftp=ssh.open_sftp()
    sftp.put(src, dest)
    sftp.close()
    ssh.close()







if __name__ == "__main__":
   # a=send_dir(1,1,1,'/home/venelin/get_pip.py','/home/venelin/get_pip.py')
    #print(a)
    #a=send_dir('192.168.100.100','pi','','/home/venelin/Programming_local/torrent_script','/home/pi/Desktop/torrent_script')

    
    pass