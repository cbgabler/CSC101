def groups_of_3(group_list):
    chunk_size = 3
    chunked_list = [group_list[i:i + chunk_size] for i in range(0, len(group_list), chunk_size)]
    print(chunked_list)
    return chunked_list
