# __all__ = ['x', 'hello']
__all__ = ['YOU_SHOULD_NEVER_USE_IMPORT_*!']

print('Hello from mymod!')

x = 100

y = [10, 20, 30]


def hello(name):
    return f'Hello, {name}, from mymod!'


_secret = 'shhh!'

if __name__ == '__main__':
    print('Goodbye from mymod!')
