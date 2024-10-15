def get_cats_info(path):
    cats = []
    try:
        with open (path, 'r', encoding = 'utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({'id':cat_id,'name': name, 'age': int(age)})
                except ValueError:
                    print(f"Invalid cat info: {line.strip()}")
            return cats
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
print(get_cats_info('task_02/cats.txt'))