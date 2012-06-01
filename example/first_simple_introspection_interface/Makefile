all : test



introspector : introspector.cpp
	g++ -lelf -std=gnu++0x introspector.cpp -o ./introspector

test : introspector
	./introspector