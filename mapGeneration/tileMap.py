def array_from_file(file_path):
    dummy_map_file = open(file_path, mode="rb")
    content = dummy_map_file.readline()
    content_lines = content.split(b'\x02')

    area_map = []
    for line in content_lines:
        area_map.append(list(map(int, line)))

    return area_map
