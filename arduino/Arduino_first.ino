void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  int time=500;
  for(int i=0;i<5;i++)
  {
    for(int j=8;j<=12;j++)
    {
      digitalWrite(j, HIGH);
    }
    delay(time);

    for(int j=12;j>=8;j--)
    {
      digitalWrite(j, LOW);
    }
      delay(time);
  }//1
  
  for(int i=0;i<3;i++)
  {

   for(int j=12;j>=8;j--)
    {
      digitalWrite(j, HIGH);
      delay(time);
    }
    
    for(int j=8;j<=12;j++)
    {
      digitalWrite(j,LOW);
       delay(time);
    }


      
  }//2
  
  for(int i=0;i<3;i++)
  {
    for(int j=12;j>=8;j--)
    {
      digitalWrite(j+1, LOW);  
      digitalWrite(j, HIGH); 
      delay(time);
    }

    for(int j=8;j<=12;j++)
    {
      digitalWrite(j, HIGH);  
      digitalWrite(j-1, LOW); 
      delay(time);
    }

  }//3

   for(int i=0;i<5;i++)
  {
    for(int j=8;j<=12;j++)
    {
      if(j % 2 == 0 )
        digitalWrite(j, HIGH);  
       else if(j % 2 == 1 )  
        digitalWrite(j, LOW);  
    }
    delay(time);

     for(int j=8;j<=12;j++)
    {
      if(j % 2 == 0 )
        digitalWrite(j, LOW);  
       else if(j % 2 == 1 )  
        digitalWrite(j, HIGH );  
    }
    delay(time);


  }//4
}
