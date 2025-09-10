# # pickling 

# import pickle

# riddhi = {'key' : 'riddhi', 'name' : 'riddhi gorasiya', 'age' : 21, 'pay' : 50000}
# heni = {'key' : 'heni', 'name' : 'heni nakrani', 'age' : 22, 'pay' : 40000}
# db = {}
# db['riddhi'] = riddhi
# db['heni'] = heni
# b = pickle.dumps(db)
# myEntry = pickle.loads(b)
# print(myEntry)

# # Pickling with a File

# import pickle

# riddhi = {'key' : 'riddhi', 'name' : 'riddhi gorasiya', 'age' : 21, 'pay' : 50000}
# heni = {'key' : 'heni', 'name' : 'heni nakrani', 'age' : 22, 'pay' : 40000}
# file = "exPickle.pickle"
# fileObj = open(file, 'wb')
# pickle.dump((riddhi, heni), fileObj)
# fileObj.close() 

# file = "exPickle.pickle"
# fileObj = open(file, 'rb')
# riddhi, heni = pickle.load(fileObj)
# print(riddhi)
# print(heni)

# # pickle.dump

# # pickle.dump(obj, file, protocol = None, *, fix_imports = True) 

# import pickle 
# import io
# class SimpleObject(object): 

#     def __init__(self, name): 
#         self.name = name 
#         l = list(name) 
#         l.reverse() 
#         self.name_backwards = ''.join(l) 
#         return

# data = [] 
# data.append(SimpleObject('pickle')) 
# data.append(SimpleObject('cPickle')) 
# data.append(SimpleObject('last')) 
# out_s = io.BytesIO() 
# for o in data: 
#     print ('WRITING: %s (%s)' % (o.name, o.name_backwards)) 
#     pickle.dump(o, out_s) 
    
# out_s.flush()

# # pickle.dumps(obj, protocol = None, *, fix_imports = True)

# import pickle

# data = [{'a': 1, 'b': 2,'c': 3.0}]
# data_string = pickle.dumps(data)
# print('PICKLE:', data_string)

# # pickle.load

# # pickle.load(file, *, fix_imports = True, encoding = "ASCII", errors = "strict") 

# import pickle
# import io

# class SimpleObject(object):

#     def __init__(self, name):
#         self.name = name
#         l = list(name)
#         l.reverse()
#         self.name_backwards = ''.join(l)
#         return
    
# data = []
# data.append(SimpleObject('pickle'))
# data.append(SimpleObject('cPickle'))
# data.append(SimpleObject('last'))
# out_s = io.BytesIO()
# for o in data:
#     print('WRITING: %s (%s)' % (o.name, o.name_backwards))
#     pickle.dump(o, out_s)
# out_s.flush()
# in_s = io.BytesIO(out_s.getvalue())
# while True:
#     try:
#         o = pickle.load(in_s)
#     except EOFError:
#         break
#     print('READ: %s (%s)' % (o.name, o.name_backwards))

# pickle.loads(bytes_object, *, fix_imports = True, encoding = "ASCII", errors = "strict") 

import pickle
import pprint

data1 = [{'a': 1, 'b': 2, 'c': 3.0}]
print('BEFORE:',)
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print('AFTER:',)
pprint.pprint(data2)

print('SAME:', data1 is data2)
print('EQUAL:', data1 == data2)