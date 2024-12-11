import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name,mode="r") as input:
        
        text=csv.reader(input)
        names_hash=dict()
        hash_pass=dict()
        names_pass=dict()
        
        
        for n in range (1000,10000):
            hash=hashlib.sha256()
            hash.update(str(n).encode())
            hash_pass[hash.hexdigest()]=str(n)
        
        for row in text:
            names_hash[row[0]]=row[1]
        
        names=list(names_hash.keys())
       
        for i in range (0,len(names)):
            names_pass[names[i]]=hash_pass[names_hash[names[i]]]
    
    with open(output_file_name,mode="w") as output:
        for i in range (0,len(names)):
            output.write(names[i]+","+names_pass[names[i]]+"\n")

    


