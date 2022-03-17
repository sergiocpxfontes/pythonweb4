from azure.storage.blob import BlobServiceClient,BlobClient
class AzureUtils:
    @staticmethod
    def BlobUpload(filename, data,id):
        bsc = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=ac2020storage;AccountKey=5fAS2v1hAZnoxilyas06ZvZwd7ehsftjBQkGlhsnW8+qtGiqboSO3UhsMS4+y59mx+DKJhmulzSx4NG2UF78SQ==;EndpointSuffix=core.windows.net")
        containername = "python-sergio"
        bc = bsc.get_blob_client(containername,filename)
        bc.upload_blob(data,overwrite=True)
        bc.set_blob_metadata(metadata={'codigo':id})
        return