# C declarations (still not sure on implementation language yet)
C       	:= gcc
CFLAGs  	:= -g -O2

# source directory declarations

# build directory declarations
B_TOP	 	:= Build
B_RPC		:= Common/RPC
B_PROCESSING	:= Processing
B_DISPLAY	:= Display

# full build and clean declarations
.PHONY: clean
.PHONY: build

# temporary phony decl since not implemented yet
.PHONY: rpc
.PHONY: processing
.PHONY: display
.PHONY: fpga

build: rpc processing display

clean:
	rm -rf $(BUILDTOP)/*

rpc:
	echo "rpc build not implemented yet"
	# build message components and protofiles

processing:
	echo "processing build not implemented yet"
	# build GPS processing components and GPS interface

display:
	echo "display build not implemented yet"
	# build display components and display interface

fpga:
	echo "fpga build not implemented yet"
	# build fpga components and GPS module binaries
