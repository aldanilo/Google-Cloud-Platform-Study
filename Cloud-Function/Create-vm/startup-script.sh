#Colocar dos os pacotes necessários para a aplicação
apt-get install update

#Acessando os metadados da VM setados no deploy
#Aqui pode colocar os nomes das imagens, bucket de acesso e bucket de destino. 
#Qualquer variável pode ser passada por aqui.
BUCKET=$(curl http://metadata/computeMetadata/v1/instance/attributes/bucket -H "Metadata-Flavor: Google")

#Comandos de copiar a aplicação do GS para a VM
#gsutil cp gs://$BUCKET/app.py /app/


#Comandos para executar a aplicação
#python /app/app.py

#Após a execução fazer uma chamada http para deletar a VM

            
