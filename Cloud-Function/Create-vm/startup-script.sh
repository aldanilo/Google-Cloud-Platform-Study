#Colocar dos os pacotes necessários para a aplicação
apt-get install update

#Acessando os metadados da VM setados no deploy
#Aqui pode colocar os nomes das imagens, bucket de acesso e bucket de destino. 
#Qualquer variável pode ser passada por aqui.
export BUCKET=$(curl http://metadata/computeMetadata/v1/instance/attributes/bucket -H "Metadata-Flavor: Google")
export ZONE=$(curl http://metadata/computeMetadata/v1/instance/attributes/zone -H "Metadata-Flavor: Google")
export INSTANCE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/instance_name -H "Metadata-Flavor: Google")
export FILE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/file_name -H "Metadata-Flavor: Google")
export PROJECT_ID=$(gcloud config list --format 'value(core.project)')

echo $BUCKET $ZONE $INSTANCE_NAME $FILE_NAME $PROJECT_ID> randomtext.txt

#Comandos de copiar a aplicação do GS para a VM
#gsutil cp gs://$BUCKET/app.py /app/


#Comandos para executar a aplicação
#python /app/app.py

#Após a execução fazer uma chamada http para deletar a VM

            
