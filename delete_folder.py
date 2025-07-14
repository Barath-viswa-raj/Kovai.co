import time
from utils import get_headers

def delete_folder(folder_id):
    url = f"https://apihub.document360.io/v2/Drive/Folders/{folder_id}"
    headers = get_headers()

    print(f"\n[DELETE] {url}")
    time.sleep(1)

    # Mocked response
    mock_response = {
        "success": True,
        "deleted_id": folder_id
    }

    if mock_response["success"]:
        print("\nFolder deleted successfully!")
        print(f"   - ID: {mock_response['deleted_id']}")
    else:
        print(" Deletion failed (mock).")
