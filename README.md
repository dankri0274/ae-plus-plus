# Æ++ | Programmeringsspråk på norsk

## Progress

- [x] Reworked runtime and execution
- [x] Rework strings and memory
- [x] Add memory read and write
- [x] Add string manipulation
- [x] Pointer manipulation
- [x] Add type casting
- [x] Add rest of stack operators
- [x] Add constants
- [x] Add Else-if
- [x] Add functions
- [x] Make printing better
- [ ] Drop memory
- [x] Scoping
- [ ] Implement pointer struct for memory safety
- [ ] Structure
- [ ] Var
- [ ] Local mem
- [ ] Add import
- [ ] Make better error system
- [ ] Make better docs

## Installering

### Windows

---

Du trenger følgende installert:  

- [python](https://www.python.org/)
- [git](https://git-scm.com/)
- [rust](https://www.rust-lang.org/tools/install)

```ps1
git clone https://github.com/kegma1/ae-plus-plus.git
cd .\ae-plus-plus
python.exe .\install.py {-addpath} # legger til .\aepp.exe i windows path
.\aepp.exe {-Flagg} [./Sti]
```

For å legge Æ++ til i PATH bruk følgende kommando i PowerShell:  

```ps1
cp .\aepp.exe "C:\Users\$env:USERNAME"; $env:Path += ";C:\Users\env:USERNAME\aepp.exe";
```

Nå kan du bruke aepp.exe fra hvor du måtte ønske på PC-en din  

## Flagg

Flagg er frivillig.
| Flagg | Beskrivelse                                                 |
| :---- | :---------------------------------------------------------- |
| `-d`  | Debug flagg, vil skrive ut stabelen når programmet kræsjer. |

## Referanse

### Stack

Æ++ er et stable basert programmeringsspråk. Det vil si at programmert fungerer veldig annerledes enn i konvensjonell språk.  
I Æ++ vil nesten alt av operasjoner fungere på toppelementene på stabelen.  
Under er et simpelt program som plusser to Int sammen, og hvordan hver operasjon endrer stabelen

``` txt
35 34 +
-------------------------------------------------------
35
----------------
|35|  |  |  |      <- Dytter 35 til stabelen
----------------

34
----------------
|35|34|  |  |      <- Dytter 34 til stabelen
----------------

+
----------------
|  |  |  |  |      -> Fjerner de to øverste tallene på stabelen
----------------

+
----------------
|69|  |  |  |      <- Dytter summen til stabelen
----------------
```

## Operasjoner

### Matteoperasjoner

| Operasjon |   Æ++   |             C             |
| :-------: | :-----: | :-----------------------: |
|     +     | `a b +` |          `a + b`          |
|     -     | `a b -` |          `a - b`          |
|     *     | `a b*`  |          `a * b`          |
|     /     | `a b /` | `a % b` **eller** `a / b` |

### Logiske operasjoner

| Operasjon |     Æ++     |     C      |
| :-------: | :---------: | :--------: |
|   ikke    |  `a ikke`   |    `!a`    |
|    og     |  `a b og`   |  `a && b`  |
|   eller   | `a b eller` | `a \|\| b` |

### Likhetsoperasjoner

| Operasjon |   Æ++    |    C     |
| :-------: | :------: | :------: |
|     =     | `a b =`  | `a == b` |
|     <     | `a b <`  | `a < b`  |
|     >     | `a b >`  | `a > b`  |
|    <=     | `a b <=` | `a <= b` |
|    >=     | `a b >=` | `a >= b` |

### Stabeloperasjoner

| Operasjon |   Før   |  Etter  |
| :-------: | :-----: | :-----: |
|    dup    |   `a`   |  `a a`  |
|    rot    | `a b c` | `b c a` |
|   slipp   |  `a b`  |   `a`   |
|    snu    |  `a b`  |  `b a`  |
|   over    |  `a b`  | `a b a` |

## Typer

| Navn  | Beskrivelse |
| :---: | :---------: |
| Helt  |    `i32`    |
| Flyt  |    `f32`    |
| Bool  |   `bool`    |
|  Str  |  `string`   |
|  Pek  |    `Ptr`    |
| Bokst |   `Char`    |

## Nøkkelord

## omgjør

```txt
 "69"   Int omgjør
# ^verdi ^type
skriv  # vil skrive ut 69 som et Int
```

## konst

```txt
konst x 35 34 + slutt

x skriv  # dette vil skrive ut 69
```

## minne

Når man definerer et minne trenger man (*i rekkefølge*) et navn, en type og en lengde på hvor stor buffer vi skal dekke.  
Når du skriver minnenavnet vil den dytte en peker til det første elementet i bufferen, du kan lagre data med "`.`"-operatoren og lese data med "`.`".  
Du kan velge andre elementer i bufferen med "`+`" eller "`-`".  
For eksempel hvis x har en lengde på 10 og peker til adresse 20 vil denne koden **`x 5 +`** skape en peker som peker til adresse 25.

```txt
minne x Helt 3 slutt
1 x ->
2 x 1 + ->
3 x 2 + ->
x 1 + @ skrivnl # skriver ut 2

```

Minnet vil se ut som: `| 1 | 2 | 3 | | | | |...`

## Hvis og ellers

```txt
"Skriv et tall: " spør Int omgjør
hvis 10 > gjør
    "større enn 10"
ellers
    "mindre enn 10"
slutt
skrivnl
```

## Ellvis

```txt
"Skriv et tall: " spør Int omgjør
hvis dup 10 > gjør
    "større enn 10"
ellvis dup 5 = gjør
    "tallet er 5"
ellers
    "mindre enn 10"
slutt
skrivnl
```

## Når løkker

```txt
0 når dup 15 <= gjør
    dup skrivnl
    1 +
slutt
# Skriver ut alle tallene fra 0 til 15
```

## Let bindinger

```txt
1 2 3

let x y z inni
    x z +
    y -
slutt

skrivnl # Skriver ut 2
```

## Funksjoner

Før du kaller en funksjon må du passe på at du har alle argumentene i rett rekkefølge.  
Når funksjonen blir utført vil du bare ha tilgang til de verdiene som ble gitt når den ble kalt.  
Når funksjonen er kommet til slutten vil den dytte retur-verdien til toppen av forrige stabel.

``` txt
# funk <navn> <argument type> -- <retur-type> inni
funk sum Helt Helt -- Helt inni
    x
slutt
2 2 sum skrivnl # skriver-ut 4
```

## Strengmanipulasjon

En streng er i bunn og grunn en peker til en bokstavbuffer.  
Dette vil si at hvis man ønsker å endre på en streng kan man omgjøre streng-pekeren til en standard peker ved hjelp av slik.

```txt
"hallo\n" Pek omgjør
dup "m" snu -> 1 + feilsøk
dup "o" snu -> 1 +
dup "r" snu -> 1 +
dup "d" snu -> 1 +
dup "i" snu -> 1 +
5 - Str omgjør 
skrivnl # skriver ut "mordi"
```
