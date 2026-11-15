# 🔐 Caesarova šifra – Python

Jednoduchá konzolová aplikace pro šifrování a dešifrování textu pomocí Caesarovy šifry.

Projekt slouží k procvičení základů programování v jazyce Python.

## 📋 Zadání projektu

Vytvoř program, který umožní uživateli zašifrovat nebo dešifrovat text pomocí číselného posunu znaků.

### Požadavky

- Výběr režimu `Encrypt` (šifrování) nebo `Decrypt` (dešifrování).
- Zadání číselného posunu.
- Zadání textové zprávy.
- Šifrování a dešifrování pomocí posunu znaků ve znakové sadě.
- Podpora malých a velkých písmen, číslic a vybraných speciálních znaků.
- Ošetření neplatných uživatelských vstupů.
- Zobrazení výsledné zprávy.

## 🛠️ Použité technologie

- Python 3.10+
- Knihovny `string` a `os`
- Funkce a podmínky
- Cykly `while` a `for`
- Ošetření výjimek `try / except`
- Operátor modulo `%`

## ▶️ Spuštění

Program spusť v terminálu:

```bash
python main.py
```

## ⚠️ Bezpečnostní upozornění

**Caesarova šifra není bezpečná kryptografická metoda.**

Jedná se o jednoduchý způsob nahrazování znaků, který lze snadno prolomit i bez znalosti použitého posunu.

Program je určen výhradně pro vzdělávací účely a demonstraci základních principů šifrování.

**Nepoužívej jej k ochraně hesel, osobních údajů ani jiných citlivých informací.**

## 🎯 Cíl projektu

Procvičit práci s řetězci, cykly, podmínkami, funkcemi a operátorem modulo v Pythonu.

Pochopit princip Caesarovy šifry a rozdíl mezi jednoduchým šifrovacím algoritmem a skutečně bezpečnou kryptografií.