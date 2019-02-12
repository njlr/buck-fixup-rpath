libtest.so: test.h test.cpp
	c++ -shared test.cpp -olibtest.so