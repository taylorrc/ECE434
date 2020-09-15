# ReadMe for Homework 2
## Measuring a gpio pin on an Oscilloscope
### Using ./togglegpio.sh
1. Min Voltage: -42mV
   Max Voltage: 3.26V

2. Period: 246ms

3. Not very close to 100ms at all--there is a 146ms difference between the two values.

4. 

5. 22.1% of CPU was used

6. 
| Period (s) | CPU Usage | Measured Period (s) |
|---|---|---|
| 0.1 | 22.1% | 0.246 |
| 0.01 | 72.8% | 0.066 |
|0.05| 33.6%| 0.146|
|0.075| 26.8%| 0.194|
|0.005 |84.1% |0.0848|

7. As I decrease the period, the measured toggle time becomes less and less stable

8. Not stable at all. My CPU usage shot up to around 93%

9. After cleaning up togglegpio.sh, there was little to no impact on the period

10. The period is slightly shorter--moving down to 233ms 

11. I was able to run at 5ms period

### Using python 

1. Min Voltage: -41.8mV
   Max Voltage: 3.24V

2. Period: 101.2ms

3. Pretty close to 100ms

4. 

5. 4% of CPU

6. 
| Period (s) | CPU Usage | Measured Period (s) |
|---|---|---|
|0.1| 4% |0.101|
|0.01| 18.1%| 0.011|
|0.05 |4.8% |0.0514|
|0.075 |4.7% |0.0766|
|0.005| 28.7%| 0.0632|

7. As I decrease the period, the measured toggle time becomes less and less stable

8. Very stable. Very little CPU Usage spike when i open vim

11. I was able to run at 5ms period with somewhat significant distortion