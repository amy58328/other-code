int buttonPin[4] = {2,4,6,8};


const int ledPin =  13;      
int speakerOut = 9;
int fre[4] = {2093,2349,2637,2794};



int buttonState = 0;       
void setup()
{
  pinMode(ledPin, OUTPUT);

  for(int i=0 ; i<4 ; i++)
  {
    pinMode(buttonPin[i], INPUT);
  }
  

  pinMode(speakerOut, OUTPUT);
}

void loop() 
{

  for(int i=0 ; i<4 ; i++)
  {
    buttonState = digitalRead(buttonPin[i]);

    if (buttonState == HIGH) 
    {

      digitalWrite(speakerOut,HIGH);
      delayMicroseconds(fre[i] / 2);
      digitalWrite(speakerOut, LOW);
      delayMicroseconds(fre[i] / 2);

    }
  }

 
}
