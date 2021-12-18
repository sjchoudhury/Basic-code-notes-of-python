dictObj = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4' };    
print (dictObj.keys())
evenArray =  dictObj.keys()[2]
oddArray =  dictObj.keys()[1]

dictObjNew = dict(zip(evenArray, oddArray))
print (dictObjNew)