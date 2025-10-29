void setup() {
  // setup code here, to run once:
// set up the pin output
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {
  // main code here, to run repeatedly:
  // LED on
  digitalWrite(2, HIGH);
    // Control DC motor CW
  digitalWrite(3, HIGH);
  digitalWrite(4, LOW);
  analogWrite(9,255);
  // LED on max
  //analogWrite(2, 255);
  delay(5000);
  // stop motor for 2 sec
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  analogWrite(9, 0);
  delay(2000);
  // LED off
   // Control DC motor CCW
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
  analogWrite(9, 100);
  //digitalWrite(3, LOW);
  // LED on Min
  //analogWrite(2, 150);
  delay(5000);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  analogWrite(9, 0);
  delay(2000);
  }
