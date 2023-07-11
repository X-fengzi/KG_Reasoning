import os



def list_data_storage(data:list, file_path:str, file_name:str):

    # This function stores the secondary list data as a file, where each list is a row

    if not file_path.endswith('/'):
         file_path = file_path + '/'
    if os.path.exists(file_path):
        pass
    else:
        os.makedirs(file_path)
    file = file_path+file_name
    with open(file,'a+') as f:
        for item in data:
                f.writelines(str.replace(str(item)[1:-1],',',' ')+'\n')
    f.close()
