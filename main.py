from google.cloud import storage
from google.cloud import aiplatform
from config import BUCKET_NAME, PROJECT, LOCATION, MODEL

def list_gcs_files(bucket_name):
    client = storage.Client()
    blobs = client.list_blobs(bucket_name)
    return [blob.name for blob in blobs]

def summarize_with_gemini(file_list, project, location, model_id):
    aiplatform.init(project=project, location=location)
    model = aiplatform.TextGenerationModel.from_pretrained(model_id)
    
    prompt = (
        "Here is a list of files:\n"
        + "\n".join(file_list)
        + "\n\nPlease summarize the main themes of these file names."
    )
    response = model.predict(prompt)
    return response.text

if __name__ == "__main__":
    # 1. List files from bucket
    files = list_gcs_files(BUCKET_NAME)
    print("Files found:", files)

    if files:
        # 2. Use Gemini to generate summary
        summary = summarize_with_gemini(files, PROJECT, LOCATION, MODEL)
        print("\nGemini Summary:\n", summary)
    else:
        print("No files found in the bucket")
