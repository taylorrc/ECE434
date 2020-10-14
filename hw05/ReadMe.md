# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Project - *LED wreath sounds interesting*
|  2 | Makefile
|  4 | Kernel Source
|  2 | Cross-Compiling
|  6 | Kernel Modules: hello, ebbchar, gpio_test, led *led not done*
|  0 | Extras
| 16 | **Total**

*My comments are in italics. --may*

# ReadMe for hw05
## Ryan Taylor

### Make
My makefile is fully included in the hw05 folder. 

### Installing of the Kernel Source
I installed to version 5.8, which was the most recent stable version I could see available. The output of my terminal showing this can be seen in my hw05Pictures folder. 

### Cross Compiling
The output of my terminal can be seen in the hw05Pictures folder. 

### Kernel Modules
This was definitely the most difficult portion of the homework. In the end, I was able to modify gpio_test.c to take two button inputs and interact with two LED outputs. The pins used can be updated at the beginning of the .c file. 