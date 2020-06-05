
def hello_world(obj):
    print("Hello World from %s!" % obj)

class Root(object):
    def __init__(self, instance_name):
        self.instance_name = instance_name

    def __repr__(self):
        return self.instance_name

custom_class = type("Person", (Root,), {"hello_world": hello_world})
cc_instance = custom_class("My Instance")

print(custom_class.__name__)
print(cc_instance.instance_name)
cc_instance.hello_world()

y = custom_class("Sue")
vars(y)
