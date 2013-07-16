
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

String type = "SNU";
String serialNumber = "10001";
String data = String(0);

void printTemperature()
{
  float tempC = sensors.getTempCByIndex(0);  
  Serial.print("{" + type + "}");
  Serial.print("[" + serialNumber + "]");
  
  Serial.print("(");
  Serial.print(DallasTemperature::toFahrenheit(tempC));
  Serial.println(")");
}

void setup()
{
  Serial.begin(9600);
  sensors.begin();
}

void loop()
{
  sensors.requestTemperatures();  
  printTemperature();
  delay(10000);  
}
