def main():
    file_type = input("File name: ").lower().strip()

    if ".gif" in file_type:
        print("image/gif")
    elif ".jpg" in file_type:
        print("image/jpg")
    elif ".png" in file_type:
        print("image/png")
    elif ".pdf" in file_type:
        print("document/pdf")
    elif ".txt" in file_type:
        print("document/txt")
    elif ".zip" in file_type:
        print("folder/zip")
    else:
        print("application/octet-stream")

main()
