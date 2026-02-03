from google.cloud import storage
import argparse

PROJECT_ID = "gcp-data-engineer-curso-486318"


def main():
    parser = argparse.ArgumentParser(
        description="Crea un nuevo bucket en Google Cloud Storage."
    )
    parser.add_argument("bucket_name", type=str)
    args = parser.parse_args()

    bucket_name = args.bucket_name
    print(f"Bucket name received: {bucket_name}")

    storage_client = storage.Client(project=PROJECT_ID)

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"

    new_bucket = storage_client.create_bucket(bucket, location="us-central1")

    print(
        f"✅ Bucket {new_bucket.name} creado en {new_bucket.location} "
        f"en el proyecto {PROJECT_ID}"
    )


if __name__ == "__main__":
    main()
