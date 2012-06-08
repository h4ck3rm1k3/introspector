all : test

#CFLAGS=-DATTRIBUTE_NORETURN="" -DATTRIBUTE_PRINTF_1="" -DATTRIBUTE_PRINTF_2="" -DATTRIBUTE_PRINTF_4="" -DHAVE_TARGET_64_LITTLE

#BINUTILS=/home/mdupont/experiments/introspector/binutils-2.20.1
BINUTILS=/home/mdupont/experiments/introspector/binutils

introspector : introspector.cpp
	g++ $(CFLAGS) -save-temps  -g3 -lelf -std=gnu++0x introspector.cpp -I $(BINUTILS) -I $(BINUTILS)/elfcpp  -o ./introspector
#	g++ $(CFLAGS) -save-temps  -g3 -lelf  -I $(BINUTILS) -I $(BINUTILS)/elfcpp  -o ./introspector introspector.cpp


#FILES=$(BINUTILS)/gold/libgold.a $(BINUTILS)/bfd/libbfd.a $(BINUTILS)/opcodes/libopcodes.a $(BINUTILS)/libiberty/libiberty.a
FILES= -L$(BINUTILS)/gold/ -lgold -L$(BINUTILS)/bfd/ -lbfd  -L$(BINUTILS)/opcodes -lopcodes -L$(BINUTILS)/libiberty -liberty -lz

gold : gold.cpp
	g++ $(CFLAGS) -save-temps  -g3 -lelf -std=gnu++0x gold.cpp -I $(BINUTILS) -I $(BINUTILS)/elfcpp $(FILES) -o ./gold

test : gold
	./gold

test2 : introspector
	./introspector