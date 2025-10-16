"""
Methods are functions that belong to objects.
They are called using dot notation (object.method()).
Methods are defined inside a class and can only be used on objects of that class

There are methods which are not available globally (they are not tied to any built-in
functions).
They come with Python objects (like strings, lists, dicts, sets, etc.), but are
not built-ins.
These are called methods and belong to classes (str, list, dict, set, tuple, int, float, etc.).

🔹 1. String (str) Methods
    'hello'.upper(),            'hello'.lower(),            'hello'.capitalize(),
    'hello'.title(),            'hello'.swapcase(),         'hello'.strip(),
    'hello'.lstrip(),           'hello'.rstrip(),           'hello'.replace('h','H'),
    'hello'.split(),            ' '.join(['hi','bye']),     'hello'.find('e'),
    'hello'.index('e'),         'hello'.count('l'),         'hello'.startswith('he'),
    'hello'.endswith('lo'),     'hello'.isalpha(),          '123'.isdigit(),
    'abc123'.isalnum(),         ' '.isspace(),              'Hello'.istitle(),
    'Hello'.encode(),           'hello'.format(),           'hello'.format_map({}),
    'hello'.partition('l'),     'hello'.rpartition('l'),    'hello'.splitlines(),
    'hello'.rfind('l'),         'hello'.rindex('l'),        'hello'.zfill(10),
    'hello'.center(20,'*'),     'hello'.ljust(20,'*'),      'hello'.rjust(20,'*'),
    'hello'.casefold(),         'hello'.removeprefix('he'), 'hello'.removesuffix('lo'),


🔹 2. List (list) Methods
    lst = [1,2,3]
    lst.append(4),              lst.extend([5,6]),          lst.insert(1,10),
    lst.remove(2),              lst.pop(),                  lst.clear(),
    lst.index(3),               lst.count(1),               lst.sort(),
    lst.reverse(),              lst.copy()


🔹 3. Dictionary (dict) Methods
    d = {'a':1,'b':2}
    d.keys(),                   d.values(),                 d.items(),
    d.get('a'),                 d.update({'c':3}),          d.pop('a'),
    d.popitem(),                d.clear(),                  d.copy(),
    d.setdefault('x',100),      d.fromkeys(['a','b'],0)


🔹 4. Set (set) Methods
    s = {1,2,3}
    s.add(4),                   s.remove(2),                s.discard(5),
    s.pop(),                    s.clear(),                  s.copy(),
    s.union({4,5}),             s.intersection({2,3}),      s.difference({1}),
    s.symmetric_difference({3}),                            s.issubset({1,2,3,4}),
    s.issuperset({1,2}),        s.isdisjoint({10,11})


🔹 5. Tuple (tuple) Methods
    t = (1,2,3)
    t.count(2),                 t.index(3)


🔹 6. Other useful methods
    File objects (open() returns a file object)
    f.read(),                   f.readline(),               f.readlines(),
    f.write('text'),            f.writelines(['a','b']),    f.seek(0),
    f.tell(),                   f.close()


"""

message = "Hello World"

words = message.split()
print(words)
print(", ".join(word.capitalize() for word in words))
