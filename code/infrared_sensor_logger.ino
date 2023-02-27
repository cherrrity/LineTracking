#define LEET_SENSORPIN 2
#define CENTER_SENSORPIN 4
#define RIGHT_SENSORPIN 3

void setup() {
	Serial.begin(9600);
	pinMode(LEET_SENSORPIN, INPUT);
	pinMode(CENTER_SENSORPIN, INPUT);
	pinMode(RIGHT_SENSORPIN, INPUT);
}

void loop() {
	byte leftSensor = digitalRead(LEET_SENSORPIN);
	byte centerSensor = digitalRead(CENTER_SENSORPIN);
	byte rightSensor = digitalRead(RIGHT_SENSORPIN);

	Serial.print("Left : ");
	Serial.print(leftSensor);
	Serial.print("Center : ");
	Serial.print(centerSensor);
	Serial.print("Right : ");
	Serial.print(rightSensor);
	Serial.print("\n");
	
	delay(1000);
}