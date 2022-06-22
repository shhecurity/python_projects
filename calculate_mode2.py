class Mode:
    

    def calculate_mode(self, items):
        item_count_dict = {}
        max_count = 0
    
        for item in items:
            count = item_count_dict[item] + 1 if item in item_count_dict else 1
            item_count_dict[item] = count
            if (count > max_count):
                max_count = count
            
        node_list = []
        for item in item_count_dict:
            if (item_count_dict[item] == max_count):
                node_list.append(item)
    
        return node_list
    
    
mode = Mode()
mode.calculate_mode([1.5, -1, 1, 1.5])