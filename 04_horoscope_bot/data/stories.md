## happy path
* greet
  - action_greet
* todays_horoscope{"horoscope":"leo"}
   - slot{"horoscope":"leo"}
   - action_todays_horoscope
   - slot{"horoscope":"leo"}
* goodbye
  - action_goodbye

## happy
* greet
  - action_greet
* todays_horoscope{"horoscope":"caprion"}
   - slot{"horoscope":"aries"}
   - action_todays_horoscope
   - slot{"horoscope":"leo"}
* todays_horoscope{"horoscope":"leo"}
   - slot{"horoscope":"leo"}
   - action_todays_horoscope
   - slot{"horoscope":"leo"}
* goodbye
  - action_goodbye

## hap
* greet
  - action_greet
* todays_horoscope{"horoscope":"caprion"}
   - slot{"horoscope":"aries"}
   - action_todays_horoscope
   - slot{"horoscope":"leo"}

## happy path 1
* greet
  - action_greet
* todays_horoscope{"horoscope":"leo"}
   - slot{"horoscope":"leo"}
   - action_todays_horoscope
* goodbye
  - action_goodbye