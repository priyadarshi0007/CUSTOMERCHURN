import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_customer_churn_data(dataset, output_folder):
    """
    Downloads a Kaggle dataset and saves it to the specified folder.
    """
    try:
        # Initialize the Kaggle API
        api = KaggleApi()
        api.authenticate()

        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Download the dataset
        print(f"Downloading dataset '{dataset}' to folder '{output_folder}'...")
        api.dataset_download_files(dataset, path=output_folder, unzip=True)
        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Define the Kaggle dataset and output folder
kaggle_dataset = "blastchar/telco-customer-churn"  
output_directory = "/Users/priyadarshisoumyakumar/Downloads/CustomerChurn/data" 

# Run the function
if __name__ == "__main__":
    download_customer_churn_data(kaggle_dataset, output_directory)