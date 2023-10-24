import os
import random

class ClassInstance:
    def __init__(self, label, path):
        self.label = label
        self.path = path

def create_class_instances_from_directory(directory):
    class_instances = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            label = os.path.basename(root)
            path = os.path.join(root, filename)
            class_instance = ClassInstance(label, path)
            class_instances.append(class_instance)
    return class_instances

def get_next_instance(class_instances, label, used_instances):
    filtered_instances = [instance for instance in class_instances if instance.label == label]

    unused_instances = [instance for instance in filtered_instances if instance.path not in used_instances]

    if unused_instances:
        next_instance = random.choice(unused_instances)
        used_instances.add(next_instance.path) 
        return next_instance.path
    else:
        return None

if __name__ == "__main__":
    root_directory = "D:\\ucioba\\PD\\lab_2\\dataset"

    instances = create_class_instances_from_directory(root_directory)
    
    used_instances = set()

    next_leopard_instance = get_next_instance(instances, "leopard", used_instances)
    print("Next leopard instance:", next_leopard_instance)
    
    next_tiger_instance = get_next_instance(instances, "tiger", used_instances)
    print("Next tiger instance:", next_tiger_instance)
    
    next_undefined_instance = get_next_instance(instances, "undefined", used_instances)
    print("Next undefined class instance:", next_undefined_instance)

    next_tiger_instance = get_next_instance(instances, "tiger", used_instances)
    print("Next tiger instance:", next_tiger_instance)
