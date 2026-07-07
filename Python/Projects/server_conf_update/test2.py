def update_serverconf(file_path, key, value):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    with open(file_path, 'w') as f:
        for line in lines:
            if key in line:
                line = f"{key} = {value}\n"
                f.write(line)
            else:
                line = line
                f.write(line)

update_serverconf('server_conf.txt', 'MAX_CONNECTIONS', '1000')
            