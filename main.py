import import_test.foo as foo

print foo.bar  # Prints out "Bar"

import import_test.foo.bar

print foo.bar  # Prints out <module 'import_test.foo.bar'>
