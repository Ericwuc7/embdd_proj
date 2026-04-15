const int PIR_PIN = 8;
const int BUZZER_PIN = 9;
const int LED_PIN = 10;

void setup() {
  pinMode(PIR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("SYSTEM_READY");
}

void triggerAlarm(bool on) {
  digitalWrite(LED_PIN, on ? HIGH : LOW);
  if (on) {
    tone(BUZZER_PIN, 1000);
  } else {
    noTone(BUZZER_PIN);
  }
}

void loop() {
  int motion = digitalRead(PIR_PIN);
  if (motion == HIGH) {
    triggerAlarm(true);
    Serial.println("MOTION_DETECTED");
    delay(1000);
  } else {
    triggerAlarm(false);
    Serial.println("NO_MOTION");
    delay(300);
  }
}
