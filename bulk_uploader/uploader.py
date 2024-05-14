import pandas as pd
import requests
from .common_utils import setup_api_session  # Assuming common_utils contains necessary utilities

class TemuBulkUploader:
    def __init__(self, api_url, spreadsheet_path):
        self.api_url = api_url
        self.spreadsheet_path = spreadsheet_path
        self.session = setup_api_session()  # Setup API session

    def read_spreadsheet(self):
        """Reads the product data from a spreadsheet."""
        try:
            df = pd.read_excel(self.spreadsheet_path, sheet_name='Products')
            print("Spreadsheet read successfully.")
            return df
        except Exception as e:
            print(f"Failed to read the spreadsheet: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def validate_data(self, data):
        """Validates the data before uploading."""
        if data.empty:
            print("No data to upload.")
            return False
        if not all(col in data.columns for col in ['Product ID', 'Product Name', 'Category', 'Price', 'Stock', 'Description', 'Image URLs']):
            print("Spreadsheet missing required columns.")
            return False
        return True

    def upload_products(self, data):
        """Uploads validated product data to the Temu store."""
        if not self.validate_data(data):
            return
        successful_uploads = 0
        for _, row in data.iterrows():
            product_data = {
                "product_id": row['Product ID'],
                "name": row['Product Name'],
                "category": row['Category'],
                "price": row['Price'],
                "stock": row['Stock'],
                "description": row['Description'],
                "images": row['Image URLs'].split(',')
            }
            response = self.session.post(self.api_url, json=product_data)
            if response.status_code == 200:
                successful_uploads += 1
                print(f"Product {row['Product ID']} uploaded successfully.")
            else:
                print(f"Failed to upload product {row['Product ID']}: {response.text}")
        print(f"Total successful uploads: {successful_uploads}")

# Example usage
api_url = 'your_temu_store_api_endpoint'  # Replace with the actual API endpoint
spreadsheet_path = 'path_to_spreadsheet.xlsx'  # Replace with your actual spreadsheet path
uploader = TemuBulkUploader(api_url, spreadsheet_path)
product_data = uploader.read_spreadsheet()
uploader.upload_products(product_data)
