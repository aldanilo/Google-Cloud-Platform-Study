#Colocar dos os pacotes necessários para a aplicação
apt-get install update

#Acessando os metadados da VM setados no deploy
#Aqui pode colocar os nomes das imagens, bucket de acesso e bucket de destino. 
#Qualquer variável pode ser passada por aqui.
BUCKET=$(curl http://metadata/computeMetadata/v1/instance/attributes/bucket -H "Metadata-Flavor: Google")
ZONE=$(curl http://metadata/computeMetadata/v1/instance/attributes/zone -H "Metadata-Flavor: Google")
INSTANCE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/instance_name -H "Metadata-Flavor: Google")
FILE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/file_name -H "Metadata-Flavor: Google")
PROJECT_ID=$(gcloud config list --format 'value(core.project)')

cat > ~/delete_instance.sh <<EOF
PROJECT_ID=$(gcloud config list --format 'value(core.project)')
ZONE=$(curl http://metadata/computeMetadata/v1/instance/attributes/zone -H "Metadata-Flavor: Google")
INSTANCE_NAME=$(curl http://metadata/computeMetadata/v1/instance/attributes/instance_name -H "Metadata-Flavor: Google")

curl -X POST "[URL-API]" -H "Content-Type:application/json" \
--data '{"project": "'$PROJECT_ID'","zone": "'$ZONE'","name": "'$INSTANCE_NAME'"}'
EOF

chmod +x ~/delete_instance.sh
#Comandos de copiar a aplicação do GS para a VM
#gsutil cp gs://$BUCKET/app.py /app/


#Comandos para executar a aplicação
#python /app/app.py

#Após a execução fazer uma chamada http para deletar a VM

            
