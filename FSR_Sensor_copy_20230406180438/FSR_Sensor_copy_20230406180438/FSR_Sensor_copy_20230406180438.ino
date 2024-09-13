
#include "WiFiNINA.h"


// Define FSR pin:
#define fsrpin A0

//Define variable to store sensor readings:
int fsrreading; //Variable to store FSR value


char ssid[] = "DSLab";
char pass[] = "1234567890";
int status = WL_IDLE_STATUS;

WiFiClient client;
void setup() {
  Serial.begin(9600); // initialize serial communication
  while (!Serial) {} // wait for the serial monitor to open

  // attempt to connect to WiFi network
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(5000); // wait for 5 seconds
  }
  Serial.println("Connected to WiFi network");

  // // connect to the server
  // if (client.connect("192.168.0.228", 65432)) { // replace with your server IP address and port number
  //   Serial.println("Connected to server");
  //   client.print("asdsa"); // send a message to the server
  // } else {
  //   Serial.println("Connection failed");
  // }
}



void loop() {
  // Read the FSR pin and store the output as fsrreading:
  fsrreading = analogRead(fsrpin);

  // Print the fsrreading in the serial monitor:
  // Print the string "Analog reading = ".
  Serial.print("Analog reading = ");
  // Print the fsrreading:
  Serial.print(fsrreading);

  // We can set some threshholds to display how much pressure is roughly applied:
  if (fsrreading < 10) {
    Serial.println(" - Off");
  } else {
    Serial.println(" - On");
  }

  delay(1000); //Delay 500 ms.


  // connect to the server
  if (client.connect("192.168.0.228", 65432)) { // replace with your server IP address and port number
    // Serial.println("Connected to server");
    client.print(fsrreading); // send a message to the server
  } else {
    Serial.println("Connection failed");
  }

}


