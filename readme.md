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

### Domácí úkol
K třídě ComplexNumber definujete testy pomocí třídy.
