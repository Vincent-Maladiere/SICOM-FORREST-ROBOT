#include <Servo.h> // Servo librairies // 


// Creating all the servos object; we need 10 (2 by legs), we take the convention that servo_i_1 is the one for height movement and i_2 is the one for horizental movement

Servo servo_1_1;
Servo servo_1_2;
Servo servo_2_1;
Servo servo_2_2;
Servo servo_3_1;
Servo servo_3_2;
Servo servo_4_1;
Servo servo_4_2;
Servo servo_5_1;
Servo servo_5_2;

int speed_of_execution; // Time between two movements == speed of execution  

int UP1 = 130;
int UP2 = 60;
int UP3 = 30;
int UP4 = 5;
int UP5 = 50;

int DOWN1 = 30;
int DOWN2 = 150;
int DOWN3 = 130;
int DOWN4 = 80;
int DOWN5 = 150;

int FOR1 = 120;
int FOR2 = 20;
int FOR3 = 150;
int FOR4 = 50;

int BACK1 = 60;
int BACK2 = 100;
int BACK3 = 70;
int BACK4 = 130;

long previousMillis = 0;
long interval = 5000; 
long bonus = 0;
#define BUFFER_SIZE_MAX 1024

void setup() {    // Set up of the Robot 

// Matching all the servo object with a PWM pin 

   servo_1_1.attach(2);
   servo_1_2.attach(3);
   servo_2_1.attach(4);
   servo_2_2.attach(5);
   servo_3_1.attach(6);
   servo_3_2.attach(7);
   servo_4_1.attach(8);
   servo_4_2.attach(9);
   servo_5_1.attach(10); 
   servo_5_2.attach(11);
  
   Serial.begin(9600);     
   pinMode(LED_BUILTIN, OUTPUT);
}



void loop() {

//INIT MATRICE
// Reception de l'ensemble de l'information, traitement ensuite.  
    int taille; 
    int j;  
    int matrice[256][2]; 
    char inData[BUFFER_SIZE_MAX];
    unsigned long currentMillis = millis();
    unsigned long diff = 0;
    uint8_t inIndex = 0;
    while(!Serial.available());
    while((diff < (interval + bonus)) && (inIndex < (sizeof(inData)/sizeof(inData[0])))) {
          Serial.print("current: ");
          Serial.println(currentMillis);
          Serial.print("previous: ");
          Serial.println(previousMillis);
          
          if (Serial.available() > 0) {
              Serial.println("reading");
              // read the incoming byte:
              inData[inIndex] = Serial.read();
              //Serial.write(inData[inIndex++]);
              Serial.println(inData[inIndex]++);
              previousMillis = currentMillis;
          }
          
          currentMillis = millis();
          diff = currentMillis - previousMillis;
      }

      delay(500);
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(500);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(500);
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(500);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(500); 
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(500);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(500); 
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(500);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(500);
      digitalWrite(LED_BUILTIN, HIGH);
      
      //Serial.println("HelloD");

   
      //Construction 
      
      if(inData[0] == 0xAA){
          taille = inData[1]<<8 + inData[2]; //0xS1<<8 + 0xS2 , 0xS1 shifté à gauche sur 8 bits
          if(BUFFER_SIZE_MAX < taille){
            //pb
          }
          char mode = inData[3];
          int i;
          for(i=0; i<taille-2; i++){
               matrice[i][0] = inData[i];   //numéro du Pin
               matrice[i][1] = inData[i+1]; //rotation associée  /!\ segmentation 
          }
          if(inData[taille] == 0xFF){ //Fin
               Serial.println("OK");   //Confirmation de création
          }
          
      }
      else{
          Serial.println("Erreur");
          previousMillis = 0;
          currentMillis = bonus;
      }
 
      delay(1000);

    
      if(Serial.read() == 0){    //Reception de l'instruction 
          while(1){
              int newData[256];  //chgmnt char -> int
              unsigned long newtimeout = millis() + interval;
              char newIndex = 0;
              while ( ((int32_t)(millis() - newtimeout) < 0) && (newIndex < (sizeof(newData)/sizeof(newData[0])))) {
                  if (Serial.available() > 0) {
                  // read the incoming byte:
                      newData[newIndex] = Serial.read();
                  Serial.write(newData[newIndex++]);
                  }
              }
              
              //La commande est placée dans newData, il s'agit d'une suite d'indexes de la matrice
              //Execution de l'instruction
      
              uint8_t i;
              for(i=0; i<= newIndex; i++){
                  bouge(matrice[newData[i]][0], matrice[newData[i]][1]); //synchro ? 
                  Serial.print("Mouvement :");
                  Serial.println(i);
              }
          }  
     }
}
        

  
  //init_servo();
  //delay(1000);


void init_servo(){    // /!\ utiliser commandes simultanées cf AdaFruit
  servo_1_2.write(80); //Pattes horizontale passées en milieu
  servo_2_2.write(60);
  servo_3_2.write(110);
  servo_4_2.write(90);
  servo_5_2.write(110);

  delay(1000);

  servo_1_1.write(UP1);
  servo_2_1.write(UP2);
  servo_3_1.write(UP3);
  servo_4_1.write(UP4);
  servo_5_1.write(UP5);

  delay(1000);

  servo_1_1.write(DOWN1);
  servo_2_1.write(DOWN2);
  servo_3_1.write(DOWN3);
  servo_4_1.write(DOWN4);
  servo_5_1.write(DOWN5);

  delay(1000);
  
  servo_1_1.write(UP1);
  servo_2_1.write(UP2);
  servo_3_1.write(UP3);
  servo_4_1.write(UP4);
  servo_5_1.write(UP5);

  delay(2000);

}

void bouge(int servo, int angle){
   switch(servo){
       case 1:
          servo_1_1.write(angle);
          break;
       case 2:
          servo_1_2.write(angle);
          break;
       case 3:
          servo_2_1.write(angle);
          break;
       case 4:
          servo_2_2.write(angle);
          break;
       case 5:
          servo_3_1.write(angle);
          break;
       case 6:
          servo_3_2.write(angle);
          break;
       case 7:
          servo_4_1.write(angle);
          break;
       case 8:
          servo_4_2.write(angle);
          break;
       case 9:
          servo_5_1.write(angle);
          break;
       case 10:
          servo_5_2.write(angle);
          break;
    }
}
