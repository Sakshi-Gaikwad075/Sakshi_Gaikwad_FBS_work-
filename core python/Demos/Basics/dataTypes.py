### numeric
# 1. int
var = 12
print(type(var))


# 2. float
var = 12.34
print(type(var))

# 3. complex
var = 10 + 5j  #real + imaginary
print(var)


### Text
var = 'firstbit solution'
print(type(var))

# ## sequential 
# 1.list
var = [10,20,30,40]

# 2.tuple
var = (10,20,30,40)
print(type(var))

# 3.range
var = range(1,10)

print(type(var))


# ## set type
# 1.set
var ={10,20,30,40}
print(type(var))

# 2.frozenset
var = frozenset({10,20,30,40})
print(type(var))

# ## Mapping
#1. dict
var = {1:"python", 2:"java",3:"c"}
print(type(var))


# ## other
# 1.bool
var = True

# 2. nontype
var = None
print(type(var))
