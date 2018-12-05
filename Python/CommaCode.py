def func(item):
	return item
spam = ['apples', 'bananas', 'tofu', 'cats']
val=''
for i in spam:
	val+=func(i)+','
print(val[0:-1])
