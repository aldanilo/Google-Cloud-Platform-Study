import sys
def carregar_tabela_BQ(Nome_dataset,Nome_Arquivo,Ano):
    from google.cloud import bigquery
    client = bigquery.Client()
    dataset_id = Ano
    dataset_ref = client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.schema = [
    bigquery.SchemaField('Col1', 'STRING'),
    bigquery.SchemaField('Col2', 'STRING'),
    bigquery.SchemaField('Col3', 'STRING'),
    bigquery.SchemaField('Col4', 'FLOAT64'),
    bigquery.SchemaField('Col5', 'STRING'),
    bigquery.SchemaField('Col6', 'FLOAT64'),
    bigquery.SchemaField('Col7', 'FLOAT64'),
    bigquery.SchemaField('Col8', 'STRING'),
    bigquery.SchemaField('Col9', 'STRING'),
    bigquery.SchemaField('Col10', 'STRING'),
    bigquery.SchemaField('Col11', 'STRING'),
    bigquery.SchemaField('Col12', 'STRING'),
    bigquery.SchemaField('Col13', 'STRING'),
    bigquery.SchemaField('Col14', 'STRING'),
    bigquery.SchemaField('Col15', 'STRING'),
    bigquery.SchemaField('Col16', 'STRING')]
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV
    uri = 'gs://cvc-files/'+Ano+'/'+Nome_Arquivo+'.csv'
    load_job = client.load_table_from_uri(
											uri,
											dataset_ref.table(Nome_dataset),
											job_config=job_config)
		
    print('Starting job {}'.format(load_job.job_id))
    load_job.result()
    print('Job finished.')
    destination_table = client.get_table(dataset_ref.table(Nome_dataset))
    print('Loaded {} rows.'.format(destination_table.num_rows))


Ano = str(sys.argv[1])
mes = ['01','02','03','04','05','06','07','08','09','10','11','12']
for elem in mes:
    Nome_dataset = 'dataset'+Ano+elem
    Nome_Arquivo = 'utf8_'+Ano+elem
    carregar_tabela_BQ(Nome_dataset,Nome_Arquivo,Ano)
