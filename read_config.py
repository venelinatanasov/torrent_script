import json
""" 
#def write_config():
    data={
        "server":"192.168.100.100",
        "user": 'pi',
        "pas": "",
        "src": '',
        "dest" :''
    }
    with open('config.json','w') as outfile:
        json.dump(data,outfile)
     """
def read_config():
    with open('config.json') as data_file:
        data=json.load(data_file)
    data_file.close()
    return data
    #print(data['server'])
    




#write_config()
if __name__ == "__main__":
    
    a=read_config()
    print(a)