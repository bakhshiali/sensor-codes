smt160 & lm35
============
1) lm35</br>
The LM35 series are precision integrated-circuit temperature sensors, whose output voltage is linearly proportional to the Celsius (Centigrade) temperature. The LM35 thus has an advantage over linear temperature sensors calibrated in ° Kelvin, as the user is not required to subtract a large constant voltage from its output to obtain convenient Centigrade scaling. The LM35 does not require any external calibration or trimming to provide typical accuracies of ±1⁄4°C at room temperature and ±3⁄4°C over a full −55 to +150°C temperature range.
Low cost is assured by trimming and calibration at the wafer level. The LM35’s low output impedance, linear output, and precise inherent calibration make interfacing to readout or control circuitry especially easy. It can be used with single power supplies, or with plus and minus supplies. As it draws only 60 μA from its supply, it has very low self-heating, less than 0.1°C in still air. The LM35 is rated to operate over a −55° to +150°C temperature range, while the LM35C is rated for a −40° to +110°C range (−10° with improved accuracy).</br>
2) smt160</br>
The SMT160-30 is a three terminal integrated temperature sensor, with a duty-cycle output. Two terminals are used for the power supply of 5 Volts and the third terminal carries the output signal. A duty cycle modulated output is used because this output is interpretable by a micro-processor without A-D converter, while the analogue information is still available.
An easy way of measuring a duty cycle is to use a microcontroller. It is only necessary to connect the sensors output to one of the micro-controllers inputs. With help of a small program it is possible to sense that input whether it is high or low. The speed of this sampling is limited due to the instruction time of the controller. So to achieve the wished accuracy it is necessary to sample over more than one sensor period. This way of working has also the advantage to filter noise. From the theory of signal processing it can be derived that there is a fixed ratio between the sensors signal frequency, the sampling rate and the sampling noise.
with SMT160 we could measure temperature from -45 °C to +130 °C . Output Pulse of sensor is similar to below timing chart, in this special case T0 is constant so we will measure TH and TL by duty cycles:
duty cycle = TH/T0;</br>
temp = (duty cycle -0.32)/0.0047<br>
In practice to measure the temperature we will use ATmega16 microcontroller, 74LS245 buffer, 4514 decoder, BC337 transistors and 8*16 LED matrix so the code is similar to "smt160.txt" in Code-Vision-AVR.

If you are interested in this kind of works, contact me (please don’t hesitate).
