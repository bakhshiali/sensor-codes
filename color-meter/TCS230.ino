/*
TCS230 color sensor
by Ali Bakhshi
Color Sensor      Arduino
-----------      --------
VCC               5V
GND               GND
s0                13
s1                12
s2                11
s3                10
OUT               9
OE                GND
*/
const int s0 = 13;
const int s1 = 12;
const int s2 = 11;
const int s3 = 10;
const int out = 9;
int red = 0;
int green = 0;
int blue = 0;
int cal_min = 5;
int cal_max_r = 50;
int cal_max_g = 50;
int cal_max_b = 50;
void calibrate() {
Serial.println("Clear screen. Then enter c again");
while (Serial.read() != 'c') {
;
color();
cal_max_r = red;
cal_max_g = green;
cal_max_b = blue;
Serial.println("Put white color in front of sensor and enter c again.");
while (Serial.read() != 'c') {
;
}
color();
cal_min = (red + green + blue) / 3;
Serial.println("calibrated.");
delay(300);
}

}
void color()
{
digitalWrite(s2, LOW);
digitalWrite(s3, LOW);
red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
digitalWrite(s3, HIGH);
blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
digitalWrite(s2, HIGH);
green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
}
void setup()
{
Serial.begin(9600);
pinMode(s0, OUTPUT);
pinMode(s1, OUTPUT);
pinMode(s2, OUTPUT);
pinMode(s3, OUTPUT);
pinMode(out, INPUT);
digitalWrite(s0, HIGH);
digitalWrite(s1, HIGH);
}
void loop()
{
color();
if (Serial.read() == 'c') {
calibrate();
}
red = map(red, cal_min, cal_max_r, 255, 0);
green = map(green, cal_min, cal_max_g, 255, 0);
blue = map(blue, cal_min, cal_max_b, 255, 0);

String data= String(red)+" "+String(green)+" "+String(blue);
Serial.println(data);
delay(300);
}
