
def hello_world(obj):
    print("Hello World from %s!" % obj)

class BaseClass(object):
    def __init__(self, instance_name):
        self.instance_name = instance_name

    def __repr__(self):
        return self.instance_name

my_class = type("MyClass", (BaseClass,), {"hello_world": hello_world})
my_class_instance = my_class("My Instance")

print(my_class.__name__)
print(my_class_instance.instance_name)
my_class_instance.hello_world()
