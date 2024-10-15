def total_salary(path):
    total =0
    count =0
    try:
        with open(path, 'r',encoding="utf-8") as file:
            for line in file:
                try:
                    _,salary = line.strip().split(",")
                    total += int(salary)
                    count +=1
                except ValueError:
                    print(f"Invalid salary value: {salary}")
            if count ==0:
                return None
            else: 
                average = total/count
                return int(total),int(average)
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
print(total_salary('task_01/salary_file.txt'))