#include <Servo.h> 

Servo myservo;

int motorPin = 9;
int pos = 0;
int incomingData;

void setup() {
  myservo.attach(motorPin);
  
  Serial.begin(9600);

  backAndForth();
}

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.read();

    if (incomingData == 'F') {
      backAndForth();
    }
  }
}

void backAndForth() {
  // Run the motor back and forth
  for (pos = 0; pos <= 180; pos += 1) { 
    myservo.write(pos);
    delay(15);
  }
  
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);
    delay(15);
  }
}
