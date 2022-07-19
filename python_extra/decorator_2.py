import functools

user = {
    "username": "ashkan",
    "access_level": "admin",
    "active": True
}
def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(*args):
            if user.get("access_level") == access_level:
                return func(*args) # or func(args[index])
            else:
                return "user has no permission to access"
        return secure_func
    return user_has_permission

def user_activation(func):
    @functools.wraps(func)
    def activation_check(*args):
        if user.get('active'):
            return func(*args)
        else:
            return 'user is inactive'
    return activation_check

@user_activation
@third_level('admin')
def my_functions(*args):
    """
    Allows us to retrieve the password for the admin panel
    """
    return f"Password for {args[1]}\'s panel is 1234."

print(my_functions('<anything>',2))