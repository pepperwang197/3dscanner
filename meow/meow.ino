/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>

Servo motor1; // upper motor
Servo motor2; // lower motor
// twelve Servo objects can be created on most boards

int distanceSensor = A0;

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  motor1.attach(9);  // attaches the servo on pin 9 to the Servo object
  motor2.attach(10);
}

int averageSensorValues(){
  int samples = 2;
  int sum = 0;
  for(int i=0; i<samples; i++){
    delay(50);
    sum += analogRead(distanceSensor);
  }
  return sum/samples;
}

void loop() {

  motor1.write(60);
  motor2.write(0);
  delay(5000);

  bool dir = 0; // true for going up, false for going down
  int angle1 = 60;
  int angle2 = 0;

  int angleInterval = 1;
  int delayPerMotorRotation = 4; // in milliseconds

  for (; angle1<=135; angle1+=angleInterval){
    // Serial.println(phi);
    motor1.write(angle1);
    delay(delayPerMotorRotation);
    if(dir){
      for (; angle2<60; angle2+=angleInterval){
        motor2.write(angle2);
        delay(delayPerMotorRotation);
        Serial.println(angle1);
        // Serial.print(" ");
        Serial.println(angle2);
        // Serial.print(" ");
        Serial.println(averageSensorValues());
        Serial.println("next");
      }
    } else {
      for (; angle2>0; angle2-=angleInterval){
        motor2.write(angle2);
        delay(delayPerMotorRotation);
        Serial.println(angle1);
        // Serial.print(" ");
        Serial.println(angle2);
        // Serial.print(" ");
        Serial.println(averageSensorValues());
        Serial.println("next");
      }
    }
    dir = !dir;
  }

  Serial.println("hello world");

  while(1){ delay(1000); }
}
