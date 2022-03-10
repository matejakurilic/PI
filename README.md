# Projekt iz kolegija Programsko inženjerstvo

Program ne obavlja potpunu funkcionalnost. Omogućeno je prepoznavanje Python i Java datoteka, prikupljanje svih iz poddirektorija te čitanje pojedine datoteke. 

S obzirom da je Java sintaksno puno kompliciranija implementiran je samo dio metoda prepoznavanja, a za Python program trenutno kreira dictionary unutar kojeg zapisuje klase i funkcije koje su definirane unutar klase.

Program se u terminalu pokreće naredbom python3 ./main.py <lang> <path_to_dir> gdje korisnik može navesti nekoliko putanja do direktorija nakon čega program obrađuje jedan po jedan direktorij.
  
Nažalost, dio koda koji je trebao povezati pojedine datoteke nije funkcionirao zbog većeg broja rekurzivnih poziva.
