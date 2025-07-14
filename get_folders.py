import time
from utils import get_headers

def get_folders():
    url = "https://apihub.document360.io/v2/Drive/Folders"
    headers = get_headers()

    print(f"[GET] {url}")
    print("Using headers:", headers)
    print("\nFetching folder list…")
    time.sleep(1)

    # Mocked response
    mock_response = {
        "success": True,
        "data": [
            {"id": "mock-folder-1111", "title": "DemoFolder1"},
            {"id": "mock-folder-2222", "title": "DemoFolder2", "sub_folders": [
                {"id": "mock-folder-3333", "title": "SubFolder_A"}
            ]}
        ]
    }

    if mock_response["success"]:
        print("\n Folder list:")
        for folder in mock_response["data"]:
            print(f"- {folder['title']} (ID: {folder['id']})")
            for sub in folder.get("sub_folders", []):
                print(f"  └── {sub['title']} (ID: {sub['id']})")
    else:
        print(" Request failed (mock).")
