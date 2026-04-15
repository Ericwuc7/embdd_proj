const int PIR_PIN = 8;

void setup() {
  pinMode(PIR_PIN, INPUT);
  Serial.begin(9600);
  Serial.println("SYSTEM_READY");
}

void loop() {
  int motion = digitalRead(PIR_PIN);
  if (motion == HIGH) {
    Serial.println("MOTION_DETECTED");
    delay(1000);
  } else {
    Serial.println("NO_MOTION");
    delay(500);
  }
}
