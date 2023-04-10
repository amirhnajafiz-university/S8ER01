<h1 align="center">
    Kernels
</h1>

<br />

Building kernels with bare metal Rustlang.

## Install

### ```nasm```

First you need to have ```nasm``` installed on your machine.
nasm is a free cross-platform x86 assembler which supports
all the common x86 operating systems – Linux, MacOS X and Windows.

When you installed ```nasm``` you can create executable files
from ```.asm``` files, which are assembly files.

### ```hexdump``` and ```ndisasm```

Now with these two commands, you can view and disassemble your
```.asm``` codes in order to see the CPU opcodes.

To boot our executable later through GRUB, it should be an ELF (Executable and Linkable Format) executable.
Creating ELF object files by passing the ```‑f elf64``` argument to it.

