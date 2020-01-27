def add_to_txt_database(txt_file: str, data: list, without_new_line=False):
    while None in data:
        data.remove(None)
    with open(f'readfromfiles\\{txt_file}.txt', 'a+') as f:
        f.read()
        if not without_new_line:
            f.write('\n')
        for info in range(len(data)):
            f.write(f'{data[info]},')