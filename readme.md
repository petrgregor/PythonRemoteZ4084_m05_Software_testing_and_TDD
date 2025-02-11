# Testování softwaru a TDD

## Lekce 1 (6. 2. 2025)
Prošli jsme prezentaci slajdy 1-33:
- Motivace - proč testovat
- TDD (Test-Driven Development)
- Druhy testů
  - Unit testy
  - Integrační testy
  - End-to-end testy
  - Akceptační testy
- PyTest
  - [Dokumentace](https://docs.pytest.org/en/latest/contents.html)
  - Instalace:
    ```bash
    pip install pytest
    ``` 
  - Testování
    - assert
    - testování vyvolané výjimky

### Domácí úkol
Definujte třídu `ComplexNumber` reprezentující [komplexní číslo](https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo)
a definujte následující metody:
- [ ] `__init__` (konstruktor)
- [ ] `__eq__` (rovnost)
- [ ] `__lt__` (<)
- [ ] `__gt__` (>)
- [ ] `__repr__`
- [ ] `__str__`
- [ ] `properties` (gettery a settery)
- [ ] `add` (sčítání)
- [ ] `subtract` (odečítání)
- [ ] `multiply` (násobení)
- [ ] `divide` (dělení)
- [ ] `conjugate` (číslo komplexně sdružené)
- [ ] `absolute_value` (absolutní hodnota)

**A vše řádně otestujte.**

## Lekce 2 (7. 2. 2025)
Prošli jsme prezentaci slajdy 34-:
- testování pomocí třídy
- fixtures
- mockování

### Domácí úkol
K třídě ComplexNumber definujete testy pomocí třídy.

## Lekce 3 (10. 2. 2025)
Příklady:
- faktoriál
- is_prime
- parametrické testy
- Cvičení 2, 3, 4

## Lekce 4 (11. 2. 2025)
- fixtury
  - add
  - save_primes (práce se souborem)
  - Cvičení 5


### Domácí úkoly
#### Počítání slov
Implementujte funkci `word_count(s)`, která vrátí počet slov v daném řetězci. A otestujte ji.

#### Fibonacciho posloupnost
Implementujte funkci `fibonacci(n)`, která vrátí n-tý prvek Fibonacciho posloupnosti. A otestujte ji.

#### Správa knihovny (OOP)
Vytvořte třídu `Book` s atributy `title` (název knihy), `author` (autor knihy) a `year` (rok vydání).
Vytvořte třídu `Library`, která umožňuje přidávat knihy a vyhledávat knihy podle autora. Vše řádně otestujte.

#### Matice a transpozice
Implementujte třídu `Matrix`, která umožňuje vytvořit matici z dvourozměrného seznamu a poskytuje metodu `transpose()`,
která vrátí transponovanou matici. Otestujte.

#### Správa úkolů (OOP)
Vytvořte třídu `Task` s atributy `description` (popis úkolu) a `completed` (boolean určující, zda je úkol dokončen).
Vytvořte třídu `TaskManager`, která umožňuje přidávat úkoly, označovat úkoly jako dokončené
a vracet seznam dokončených a nedokončených úkolů. Vše otestujte.

#### Správa uživatelských účtů a volání externího API
Vytvořte třídu `User`, která má atributy `username` (uživatelské jméno) a `email`.
Vytvořte třídu `UserManager`, která umožňuje přidávat uživatele a odesílat ověřovací e-mail prostřednictvím externí služby.
Metoda `send_verification_email(user)` ve třídě `UserManager` by měla volat metodu `send_email(to, subject, body)`, 
která simuluje volání externího API pro odesílání e-mailu.
Použijte **mock** objekty, abyste otestovali, zda metoda `send_verification_email` volá `send_email` s odpovídajícími parametry.

#### Validace rodného čísla
Napište funkci validující rodné číslo. 
Funkce `is_valid()` bere jako parameter string s rodným číslem, 
a vráti `True` nebo `False` v závislosti na výsledku validace.

- K funkci přidejte pozitivní i negativní testy.
- Zkuste použít programování s cyklem. 
- Zkuste parametrizování testu. 
- Zkuste testování výjimek.

[Odkaz na paragraf 2 zákona stanovující validní rodné číslo](https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1995/301/)
