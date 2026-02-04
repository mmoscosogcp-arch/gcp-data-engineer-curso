import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    options = PipelineOptions(
        runner='DataflowRunner',  # DirectRunner entorno local, el DataflowRunner entorno nube
        project='axial-canto-486418-n8',
        region='us-central1',
        temp_location='gs://gcs-bucket-curso-04_nube/temp',
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Leer Archivo' >> beam.io.ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')
            | 'Separar Palabras' >> beam.FlatMap(lambda line: line.split())
            | 'Contar Palabras' >> beam.combiners.Count.PerElement()
            | 'Guardar resultados' >> beam.io.WriteToText('gs://gcs-bucket-curso-04_nube/output/wordcount')

        )


print("Pipeline ejecutada correctamente.")


if __name__ == '__main__':
    run()
