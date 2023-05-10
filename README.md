# Minimal RTOS

This is a minimal ```RTOS``` based on Python. It is a simple implementation of a ```EDF```,
```RM```, ```DM``` scheduler. It is a good starting point for learning how to implement a ```RTOS```.

## Execute

### usage

```sh
usage: main.py [-h] [-m MODE] [-p PREEMPTIVE] [-f FILE] [-d DURATION]
```

### mode

- ```RM```
- ```DM```
- ```EDF```

### example

```sh
python3 main.py --mode RM --file tasks_interrupts.csv --duration 100 --preemptive True
```

## Tasks

You can create your own tasks in csv file with following rows in order:

```csv
priority,name,state,type,act_time,period,wcet,deadline
```
