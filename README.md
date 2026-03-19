# Analýza fyzikálních dat – výkon solárního panelu

## Popis projektu

Cílem projektu bylo analyzovat data z měření výkonu solárních panelů v různých podmínkách. Data byla sbírána během jednoho týdne v interiéru (lampy) i exteriéru (slunce), při různých úhlech a intenzitě světla.

Projekt byl řešen pomocí dvou knihoven:
- pandas
- polars

## Postup řešení

### 1. Načtení dat
Dataset byl načten ze souboru CSV a byla provedena základní kontrola dat (head, info/schema, shape).

### 2. Čištění dat
Data obsahovala několik typů chyb, které bylo nutné opravit:
- převod datových typů (čísla, datum)
- odstranění nesmyslných hodnot (např. záporný výkon, úhel > 90°)
- odstranění chybějících hodnot
- odstranění duplicit
- sjednocení textových hodnot (např. "suny" → "sunny", odstranění mezer)

### 3. Vytvoření nových veličin
Byl vytvořen nový sloupec:
power_calc = voltage × current

Tento sloupec byl porovnán s původním sloupcem power_w.

### 4. Analýza dat
Byly provedeny následující analýzy:
- vliv úhlu na výkon
- vztah mezi intenzitou světla a výkonem
- porovnání výkonu indoor vs outdoor
- nalezení nejlepších podmínek
- detekce anomálií

## Odpovědi na otázky

### Jaké chyby dataset obsahoval?
- chybějící hodnoty (NaN)
- duplicity
- špatné datové typy
- nesmyslné hodnoty (např. záporné hodnoty, úhel větší než 90°)
- nekonzistentní text (např. "suny", mezery)

### Jsou hodnoty power_calc a power_w stejné?
Ne vždy. Hodnoty se mohou lišit kvůli:
- zaokrouhlování
- nepřesnosti měření
- chybám senzorů

### Jak úhel ovlivňuje výkon?
S rostoucím úhlem výkon klesá. Nejvyšší výkon je při malém úhlu (panel je kolmo ke zdroji světla).

Ano, tento výsledek dává fyzikální smysl, protože při větším úhlu dopadá méně světla na panel.

### Jak silná je závislost mezi lux a výkonem?
Závislost je silná a kladná. Čím větší intenzita světla (lux), tím větší výkon panelu.

Závislost je přibližně lineární, ale může být ovlivněna reálnými podmínkami.

### Kde panel funguje lépe?
Panel funguje lépe venku (outdoor), protože sluneční světlo má vyšší intenzitu než umělé osvětlení v interiéru.

### Jaké jsou nejlepší podmínky?
- vysoká intenzita světla (lux)
- malý úhel (blízko 0°)
- venkovní prostředí
- kvalitní panel

### Jsou extrémní hodnoty chyby nebo zajímavý jev?
Extrémní hodnoty mohou být:
- chyba měření
- nebo výjimečné podmínky (např. velmi silné světlo)

Je nutné je posoudit individuálně.

## Vlastní analýza

Byla provedena analýza vlivu úhlu při vysoké intenzitě světla.

Postup:
- filtrování dat podle vysoké hodnoty lux
- seskupení podle úhlu
- výpočet průměrného výkonu

Výsledek:
I při vysoké intenzitě světla výkon klesá s rostoucím úhlem.

## Porovnání pandas vs polars

### pandas
Výhody:
- jednoduchý na pochopení
- velké množství dokumentace
- vhodný pro začátečníky

Nevýhody:
- pomalejší při práci s velkými daty

### polars
Výhody:
- velmi rychlý
- efektivní práce s velkými daty
- moderní výrazový (expression) styl

Nevýhody:
- složitější na pochopení
- méně rozšířený než pandas

## Shrnutí

Obě knihovny umožňují efektivní práci s daty.  
Pandas je vhodnější pro začátečníky, zatímco polars nabízí vyšší výkon a modernější přístup.
