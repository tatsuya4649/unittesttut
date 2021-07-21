def hoge(arg):
	if not isinstance(arg,int):
		raise TypeError("hoge argument must be integer")
	return arg * 10
