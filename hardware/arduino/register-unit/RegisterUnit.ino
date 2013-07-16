
String mainSerialNumber = String(0);

String registerStatus = "CLOSED";

String type = "MRU";
String mySerialNumber = "10002";
String data = String(0);

void readMessageXBee()
{
  String readString = String(0);
  char c = Serial.read();
  
  if (c == '<')
  {
    readString += c;
    while (c != ')') 
    {
      if (Serial.available() > 0) 
      {
        c = Serial.read();
        readString += c;
      }
    }
  }
  processXBeeCommand(readString);
}

void processXBeeCommand(String readString)
{
  String serialNumber = "";
  serialNumber = readString.substring(readString.indexOf("<") + 1, readString.indexOf(">"));
  data = readString.substring(readString.indexOf("(") + 1, readString.indexOf(")"));
  
  if (serialNumber == mySerialNumber && data == "OPEN")
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    delay(600);
  }
  else if (serialNumber == mySerialNumber && data == "CLOSE")
  {
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    delay(600);
  }
}

void setup()
{
  Serial.begin(9600);  
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0)
  {
    readMessageXBee();
  }
  
}
