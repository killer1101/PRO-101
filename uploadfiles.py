import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'dRpRgf3RuJkAAAAAAAAAAQo5UtSV3APj5NyokSgXkn4wEGcVREHx98TGAUSRz7YW'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ") 
 
    # API 
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

if __name__ == '__main__':
    main()