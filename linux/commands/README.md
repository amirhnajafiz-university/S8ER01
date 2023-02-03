<h1 align="center">
    Commands
</h1>

<br />

In this lecture I collect linux commands that I learned in courses or I used myself.

## Guide

Get manual of each command:

```shell
man [command | ls]
```

## Kernel

Find linux kernel version:

```shell
uname -r
```

For full information:

```shell
cat /proc/version
```

## Host

Find host information:

```shell
hostnamectl
```

## File & Directory

Print working directory:

```shell
pwd
```

List files:

```shell
ls [path | /home] [flags | -la]
```

Move between directories:

```shell
cd [path | /Desktop]
```

Create a new file:

```shell
touch [name | me.txt]
```

Create directories:

```shell
mkdir [name | user]
```

Remove file:

```shell
rm [name]
```

Remove directory:

```shell
rmdir [name]
rm -r [name]
```

Move file:

```shell
mv [src] [dst]
```

Copy file:

```shell
cp [src] [dst]
```
