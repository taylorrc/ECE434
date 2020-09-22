#!/bin/bash
#chmod +x

# Reading tmp101 sensors and putting output in fahrenheit

temp1=`i2cget -y 2 0x48`
temp2=`i2cget -y 2 0x4a`

decimal1=$(printf "%d\n" $temp1)
decimal2=$(printf "%d\n" $temp2)

intermed1=$(($decimal1 *9))
intermed2=$(($decimal2 *9))

int1=$(($intermed1 /5))
int2=$(($intermed2 /5))

output1=$(($int1 +32))
output2=$(($int2 +32))

echo "Temp 1:" $output1
echo "Temp 2:" $output2
