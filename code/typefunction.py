# Python3 code to explain
# the type() function

# Class of type dict
class DictType:
    DictNumber = {1:'John', 2:'Wick',
                  3:'Barry', 4:'Allen'}

    # Will print the object type
    # of existing class
    print(type(DictNumber))

# Class of type list
class ListType:
    ListNumber = [1, 2, 3, 4, 5]

    # Will print the object type
    # of existing class
    print(type(ListNumber))

# Class of type tuple
class TupleType:
    TupleNumber = ('I', 'don't', 'know')

    # Will print the object type
    # of existing class
    print(type(TupleNumber))

# Creating object of each class
d = DictType()
l = ListType()
t = TupleType()
