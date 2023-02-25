#include <mega16.h>
#include <stdio.h>
#include <delay.h>
#asm
   .equ __lcd_port=0x18 ;PORTB
#endasm
#include <lcd.h>  
#define  Up        PIND.0
#define  Down      PIND.1
#define  Enter     PIND.2  
#define  high_LED  PORTA.1
unsigned char compare=0,set=0xff;
float   temp;  
//__________________________________________
void display(){   
char   lcd_buf[32];
sprintf(lcd_buf,"Temp=%3.1f\xdfC\nHigh Temp=%i",temp,compare);
lcd_clear(); 
lcd_gotoxy(0,0); 
lcd_puts(lcd_buf);
lcd_gotoxy(13,1); 
if(high_LED==1) lcd_putsf("on ");
if(high_LED==0) lcd_putsf("off");
}  
//_________________________________________                         
interrupt [ADC_INT] void adc_isr(void){
unsigned int adc_data;
adc_data=ADCW;
temp=adc_data*256/1024; 
if(temp>=set) high_LED=1;
else high_LED=0;
} 
//_________________________________________up
void inc_set_temp(){
if(compare<99) compare++; 
}
//__________________________________________Down
void dec_set_temp(){
if(compare!=0) compare--; 
}              
//__________________________________________
void main(){ 
PORTD=0XFF;
DDRD=0X00;
PORTA.1=0;
DDRA.1=1;  
ACSR=0XC0;
SFIOR=0X00;
ADMUX=0XC0;
ADCSRA=0X8F;
lcd_init(16);
#asm("sei")
ADCSRA=0XCF;
while(1){
   display();
   delay_ms(250);
   ADCSRA=0XCF; 
   if(Up==0)    inc_set_temp();
   if(Down==0)  dec_set_temp();
   if(Enter==0) set=compare; 
 };
} 