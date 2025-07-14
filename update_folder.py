import time
from utils import get_headers

def update_folder(folder_id, new_name):
    url = f"https://apihub.document360.io/v2/Drive/Folders/{folder_id}"
    headers = get_headers()

    print(f"\n[PUT] {url}")
    print("Payload:", {"title": new_name})
    time.sleep(1)

    # Mocked response
    mock_response = {
        "success": True,
        "data": {
            "id": folder_id,
            "title": new_name,
            "updated_on": "2025-07-14T12:05:00Z"
        }
    }

    if mock_response["success"]:
        folder = mock_response["data"]
        print("\n Folder renamed successfully!")
        print(f"   - ID   : {folder['id']}")
        print(f"   - Title: {folder['title']}")
        print(f"   - Updated On: {folder['updated_on']}")
    else:
        print(" Rename failed (mock).")
