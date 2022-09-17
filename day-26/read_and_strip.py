

class Read_and_strip():
        
    def read(url):
        with open(url) as file:
            list_file = file.readlines()
            new_list_file_striped = []
            for item in list_file:
                new_item_striped = int(item.strip())
                new_list_file_striped.append(new_item_striped)
        new_list_file_striped.sort()
        return new_list_file_striped