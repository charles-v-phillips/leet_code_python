@staticmethod
def decorator_function(original_function):
    def wrapper_function():
        print('we out here wrapping')
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

# decorated_display = decorator_function(display)

display()