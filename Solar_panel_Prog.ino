#include <Servo.h>
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include "RTClib.h"
//use clock module RTC DS1307
//use a voltage sensor
//ethernet shield
Servo servo1;
Servo servo2;
int val1 = 0;
int val2 = 0;
int valpot;
int potpin = A0;
int sensorLT = A1;
int sensorLB = A2;
int sensorRT = A3;
int sensorRB = A4;
int LT;
int LB;
int RT;
int RB;
const int chipSelect = 10;
RTC_DS1307 RTC;
String dataString = "";
String date = "";

void setup() {
  // put your setup code here, to run once:
  servo1.attach(3);
  servo2.attach(5);
  Wire.begin();
  RTC.begin();
}

void loop() {
  valpot = analogRead(potpin);
  valpot = 5*valpot*(5/1023);
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  DateTime now=RTC.now();
  char str[32];
  sprintf(str, sizeof str, "%Y.%m.%d:%H.%M.%S", now);
  dataString = String(str);
  if (dataFile) {

    dataFile.print(dataString);
    dataFile.print(";");
    dataFile.print(valpot);
    dataFile.println("\n");

    dataFile.close();
  }
  LB = analogRead(sensorLB);
  LT = analogRead(sensorLT);
  RT = analogRead(sensorRT);
  RB = analogRead(sensorRB);
  if (LT and LB < (max(RT, RB)/2)) {
    val1 += 5;
    servo1.write(val1);
    
  }
  else if (RT and RB < (max(LT, LB)/2)) {
    val1 -= 5;
    servo1.write(val1);
  }
  else if (RT and LT < (max(LB, RB)/2)) {
    val2 -= 5;
    servo2.write(val2);
  }
  else if (RB and LB < (max(LT, RT)/2)) {
    val2 += 5;
    servo2.write(val2);
  }
  
  
  delay(1000); 
}
