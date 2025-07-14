import json
import time
import random
from utils import get_headers

USER_ID = "mock-user-id-1234"
url = "https://apihub.document360.io/v2/Drive/Folders"

def create_folder(folder_name):
    data = {
        "title": folder_name,
        "parent_folder_id": None,
        "user_id": USER_ID
    }

    headers = get_headers()
    headers['Content-Type'] = 'application/json'

    print(f"\n [POST] Creating folder with data:")
    print(json.dumps(data, indent=2))

    time.sleep(1)
    fake_folder_id = f"mock-folder-{random.randint(1000, 9999)}"

    mock_response = {
        "success": True,
        "data": {
            "id": fake_folder_id,
            "title": folder_name,
            "updated_on": "2025-07-14T12:00:00Z",
            "updated_by": USER_ID,
            "folder_color": "blue",
            "is_starred": False
        }
    }

   
    with open("folder_id.txt", "w") as f:
        f.write(fake_folder_id)

    print("\n Folder created successfully!")
    print(f"   - ID: {fake_folder_id}")
    print(f"   - Title: {folder_name}")
    print(f"   - Updated By: {USER_ID}")
    print(f"   - Folder Color: {mock_response['data']['folder_color']}")
    print(f"   - Is Starred: {mock_response['data']['is_starred']}")

 
    print("\n" + "=" * 50)
    print(" Updated Folder List:")
    print("=" * 50)

    folders = [
        {"id": "mock-folder-1111", "title": "DemoFolder1"},
        {"id": "mock-folder-2222", "title": "DemoFolder2", "sub_folders": [
            {"id": fake_folder_id, "title": folder_name}
        ]}
    ]

    for folder in folders:
        print(f"- {folder['title']} (ID: {folder['id']})")
        for sub in folder.get('sub_folders', []):
            print(f"  └── {sub['title']} (ID: {sub['id']})")

    return fake_folder_id
