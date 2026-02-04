from google.cloud import bigquery

client = bigquery.Client(project="smart-bridge-486423-i4")


def query_public_datasets():
    client = bigquery.Client()

    query = """
        SELECT 
            ORDER_ITEMS.id, 
            order_id, 
            product_id, 
            PRODUCTS.name 
        FROM `bigquery-public-data.thelook_ecommerce.order_items` AS ORDER_ITEMS
        JOIN `bigquery-public-data.thelook_ecommerce.products` AS PRODUCTS
        ON ORDER_ITEMS.product_id = PRODUCTS.id
        LIMIT 10
    """

    results = client.query(query).to_dataframe()[:20]

    print("La query funciono perfecto")
    print(results)


if __name__ == "__main__":
    query_public_datasets()
