import os

def search_file(id):
    print(f'[log] search for following ID: {id}')

    folder_path = 'archive/'
    file_name = f'{id}.pdf'
    
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)
