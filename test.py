# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		return False;
# 	if x>=0:
# 		return x
# 	else:
# 		return -x

# score = my_abs(-23)
# # print(score)

# if score==False:
# 	print('输入类型错误')
# else:
# 	print(score)


# #可变参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# person('li',2)
# person('li',2, o='a', c='bi')


# #参数组合
# def f1(a, b, c=0, *args, **kw):
# 	print('a=',a, 'b=',b, 'c=',c, 'args=',args, 'kw=',kw)

# def f2(a, b, c=0, *, d, e, **kw):
# 	print('a=',a, 'b=',b, 'c=',c, 'd=',d, 'kw=',kw)

# f1(1,2)
# f1(1,2,3,'a','b',x=33,f=23,e='se')
# f2(1,2,3,d=23,e='sdf',bt=23,sd=2323,gf=23)


#迭代 遍历
# a = {'a':111,'b':222,'c':333}
# for i,k in a.items():
# 	print(i,k)

# from collections.abc import Iterable
# if isinstance(123,Iterable):
# 	print('ok')
# else:
# 	print('错误类型')


# def findMinAndMax(L):
# 	min = None
# 	max = None
# 	for i in L:
# 		if(i < min):
# 			min = i
# 		if(i > max):
# 			max = i
# 	return min,maxxxx


# print(findMinAndMax([1,2,3,4,5]))


# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# s = [k + '=' + v for k, v in d.items()]
# print(s)

L1 = ['HelloP', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)