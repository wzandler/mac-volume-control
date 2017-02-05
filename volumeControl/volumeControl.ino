int const potPin = A0;
int potVal;
int vol;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  potVal = analogRead(potPin);
  vol = map(potVal,0,1023,0,8);
  Serial.println(vol);
}
