int kitchen = D6;
int hall = D3;
void setup() {
pinMode(kitchen,OUTPUT); 
pinMode(hall,OUTPUT);
Particle.function("led",ledToggle);
digitalWrite(kitchen,LOW);
digitalWrite(hall,LOW);
}

void loop() {
}

int ledToggle(String command) {

    if (command=="kitchen_on") {
        digitalWrite(kitchen,HIGH);
        
    }
    else if (command=="kitchen_off") {
        digitalWrite(kitchen,LOW);
    
    }
    else if (command=="hall_on") {
        digitalWrite(hall,HIGH);
    
    }
    else if (command=="hall_off") {
        digitalWrite(hall,LOW);
    
    }
    else {
        return -1;
    }

}
 
