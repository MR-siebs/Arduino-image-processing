int incomingByte = 0; 

    void setup() {
      Serial.begin(1000000);
    }

    void loop() {
      // reply only when you receive data:
      if (Serial.available() > 0) {
        incomingByte = Serial.read();

        Serial.print(incomingByte);
        }

    }
