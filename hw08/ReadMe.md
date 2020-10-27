# Homework 8 -- Ryan Taylor

## Blinking an LED
This section took me a little bit of time to understand. I had the correct software in my hello.pru0.c file, but the P9_31 pin was not set to be a GPIO output. Because of this, I couldn't see the LED blinking. 

I can start the program by saying </br>
bone$ **make TARGET=hello.pru0**

And to stop the program from executing, 
bone$ **make TARGET=hello.pru0 stop**

I was able to toggle the pin with delay = 0 and record a frequency of 12.5MHz. The waveform has slight jitter and a little bit of overshoot, but for the most part it is stable. 

## PWM Generator
I was able to move the output pin of the example code to P9_31. After making one of the delays 1, I ran the waveform at 50MHz. The wave was very stable, but was smoothed out to look more sinusoidal than like pulses. There was hardly any jitter. The scopes in C115 are not equipped to record the standard deviation of the wave, but I would say that it would be very small. 

## Controlling the PWM Frequency  
The code in pwm4.pru0.c is driving the output pins P9_28 through P9_31
because of the bits that are being changed in __R30. The fastest frequency I could run on the four channels was 326.8 kHz. There is a little bit of overshoot and undershoot when coming up to the high voltage but overall the waveform was pretty stable. I was able to run the pwm-test.c program and saw the count value always at 20. countOn and countOff always add to 20. 

## Reading an Input at Regular Intervals
I was able to run the input.pru0 code and output to P9_31 from a button press. After using a scope, I could tell that from the initial button pressing to the output changing of the PRU on pin 31, there was ~5us difference. It took longer for the button press to debounce than for the PRU to change states. 

## Analog Wave generator
I followed the directions in the PRU cookbook to display a sinusoidal wave from the PRU. I included a picture in the pictures folder in my repository. The signal very strongly resembled a sinusoidal signal. </br>
Initially, I didn't realize that I needed an RC circuit to smooth the output of the P9_31 pin, but when I implemented the filter, all of the noise in the signal went away. 

## Overall Table of Results:

| Section | Fastest clock speed | 
| --- | --- | 
| Blinking from GPIO | 12.5MHz |
| PWM Generator | 50 MHz |
| pwm4.pru0.c | 326.8kHz |

