# Makefile

CXX = g++
CFLAGS = -g 

LIB = -lode -ldrawstuff -lGL -lGLU -lX11 -lrt -lm -lpthread -lstdc++
LIBDIR = -L/usr/lib/x86_64-linux-gnu -L/home/libode/ode-0.16.3/drawstuff/src/.libs  -L/home/libode/ode-0.16.3/ode/src/.libs -L/usr/lib 
INCDIR = -I/home/libode/ode-0.16.3/include -I/home/libode/ode-0.16.3/ode/src -I/usr/include

# 以下のtemplateを好きなファイル名に変更する。
OUT  = template
OBJS = $(OUT).o

all: $(OUT)


$(OUT): $(OBJS)
	$(CXX) $(CFLAGS) -o $@ $(OBJS) $(INCDIR) $(LIBDIR) $(LIB) 


$(OUT).o: $(OUT).cpp template.h
	$(CXX) $(CFLAGS) -c $< $(INCDIR) $(LIBDIR) $(LIB) 


clean: 
	rm -f $(OUT)   
	rm -r $(OBJS)  


.PHONY: all clean
