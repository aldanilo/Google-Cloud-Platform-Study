from setuptools import setup
setup(name='newfilesinbucket',
      version='0.0.1',
      description='return a list of new files in bucket',
      author='Danilo Souza',
      author_email='danilo.souza@casadosventos.com.br',
      packages=['bucket_new_files'],
      install_requires=['google-cloud-pubsub'])
