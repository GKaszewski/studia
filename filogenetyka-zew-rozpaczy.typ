#set page(header: [
  _Filogenetyka molekularna - zew rozpaczy_
  #h(1fr)
  Gabriel Kaszewski
])
#set page(numbering: "— 1 —")

#align(center, text(17pt)[*Filogenetyka molekularna - zew rozpaczy*])
= Abstract
W tym dokumencie spróbuję zawrzeć najważniejsze informacje z zakresu filogenetyki molekularnej, które mogą się przydać na egzaminie. Nie potrafię zagwarantować, że posiadając wiedzę z tego dokumentu uda się zdać egzamin, aczkolwiek lepsze to niż nic.
Do trzech razy _(w moim przypadku)_ sztuka.

#set quote(block: true)
#quote(attribution: "Albert Camus")[
    _In the depth of winter, I finally learned that within me there lay an invincible summer._
]

= Wyjaśnij pojęcie mikroewolucji
Ewolucja ponizej poziomu gatunków, np. dryf, selekcja.

= Wyjaśnij pojęcie makroewolucji
Ewolucja na poziomie gatunków bądź powyzej.

= Kod genetyczny
+ Jest trójkowy - na jeden kodon przypadają trzy nukleotydy.
+ Jest zdegenerowany - aminokwas moze byc kodowany przez rozne kodony / trojki nukleotydow.
+ Jest bezprzecinkowy - nie ma przerw miedzy kodonami.
+ Jest niezachodzacy - jeden nukleotyd moze byc czescia tylko jednego kodonu.
+ Jest uniwersalny - kodony koduja te same aminokwasy u wszystkich organizmow.

= Kodony STOP
Kodony STOP to *UAA* *UAG* *UGA* - koncza ekspresje bialka.

= IUAPC
#table(
    columns: 2,
    inset: 5pt,
    table.header(
        [*IUAPC*], [*Nukleotyd*]
    ),
    [A], [Adenina],
    [C], [Cytozyna],
    [G], [Guanina],
    [T badz U], [Tymina / Uracyl],
    [R], [A / G],
    [Y], [C / T],
    [S], [C / G],
    [W], [A / T],
    [K], [G / T],
    [M], [A / C],
    [B], [C / G / T],
    [D], [A / G / T],
    [H], [A / C / T],
    [V], [A / C / G],
    [N], [cokolwiek],
    [. lub -], [przerwa]
    
)

= Modele ewolucji
#table(
    columns: (auto, auto, auto),
    table.header(
        [*Model*], [*Tempo subtytucji*], [*Frekwencja nukleotydow*]
    ),
    [K2P], [rózne], [równa],
    [GTR], [rózne], [różna],
    [HKY], [różne], [różna],
    [JC], [równe], [równa],
)

= Metody filogenetyczne
- oparte na dystansie
  + Neighbor Joining
  + UPGMA
  + ME 
- oparte na podobieństwie
  + Maximum Parsimony
  + Maximum Likelihood
  + Bayesian Inference (bayesowska)

= Markery molekularne
#figure(
    image("figures/marker.png"),
    caption: [
        Ze względu na obecność krótkich tandemowych powtórzeń (STR), ten marker to mikrosatelita.
    ]
)
Zapis schematyczny tej mikrosatelity:

5' - TTGTCAAAGAGTTCAGCCGAATACAATTTATTAAGTG ... [AG]n ... TAAAGATATAGGAGACTAGCTAGAGCCAAGCACTAAGATACAACACGC - 3'

- [AG]n oznacza powtarzającą się sekwencję AG, gdzie n to liczba powtórzeń (w tym przypadku jest ich sporo, można policzyć dokładnie, ale schematycznie wystarczy oznaczyć jako n).
- Sekwencje flankujące przed i po powtórzeniach są istotne dla projektowania primerów do amplifikacji PCR.

=== Cechy widoczne w sekwencji:

    - Region powtarzalny:
        W środku sekwencji znajduje się wiele powtórzeń AG i AGAG, które są charakterystyczne dla markerów typu mikrosatelitów (krótkie tandemowe powtórzenia, *STR* - _short tandem repeats_).

    - Sekwencje flankujące:
        Powtórzenia AG są otoczone przez unikalne sekwencje DNA na początku i na końcu.

=== Markery dziedziczone dwurodzicielsko
- Dziedziczone od obojga rodziców.
- Wykorzystywane do badania rekombinacji genetycznej, różnorodności genetycznej i filogenii na poziomie populacji.
Przykłady:
- Alloenzymy:
    - Polimorfizmy w białkach kodowanych przez geny jądrowe.
    - Używane w analizach enzymatycznych, np. elektroforezie.
    - Zastosowania: badania różnorodności genetycznej, porównania populacji.
- nDNA (jądrowy DNA):
    - Zawiera zarówno geny kodujące białka, jak i niekodujące sekwencje.
    - Zastosowania:
        + Analiza filogenetyczna (np. geny kodujące rRNA).
        + Badania różnorodności genetycznej.
        + Analizy związane z rekombinacją genetyczną.

=== Markery dziedziczone jednorodzicielsko
- Dziedziczone wyłącznie od jednego z rodziców.
- Pozwalają na śledzenie linii matczynej lub ojcowskiej.
- Stabilność w dziedziczeniu (brak rekombinacji lub jej ograniczenie).
Przykłady:
- mtDNA (mitochondrialny DNA):
    - Dziedziczenie matczyne (w większości organizmów).
    - Zastosowania:
        + Analizy linii matczynej.
        + Badania różnorodności populacyjnej.
        + Rekonstrukcja filogenezy.
    - Cechy charakterystyczne:
        + Wysoka mutowalność w niektórych regionach (np. D-loop).
        + Brak rekombinacji.
- cpDNA (chloroplastowy DNA):
    - Dziedziczenie głównie matczyne (u większości roślin, choć u niektórych gatunków ojcowskie).
    - Zastosowania:
        + Analiza filogenetyczna roślin.
        + Śledzenie migracji roślin.
    - Cechy charakterystyczne:
        + Relatywnie konserwatywne sekwencje.
        + Stabilne dziedziczenie.
- Chromosomy haploidalne:
    
    Np. chromosom Y u organizmów o determinacji płciowej XY (dziedziczenie ojcowskie).
    - Zastosowania:
        + Analizy linii ojcowskiej.
        + Rekonstrukcja historii populacji ludzkich i zwierzęcych.

Dwurodzicielskie markery dostarczają informacji o zmienności genetycznej i rekombinacji w obrębie populacji.

Jednorodzicielskie markery pozwalają na śledzenie linii genealogicznych i migracji.

#figure(
    image("figures/markery_w_badaniach.png"),
    caption: [
        Markery molekularne w badaniach Gyrodactylus
    ]
)

= Teroria Darwina
#figure(
    image("figures/darwin.png"),
)

= Teoria Lamarcka
#figure(
    image("figures/lamark.png"),
)

= Analiza BI z opcja zegara molekularnego
5 kroków analizy:
+ Matrycę .nxs importujemy do programu BEAUTi -> tworzymy plik .xml.
+ Plik .xml importujemy do programu BEAST -> uzyskujemy plik .log., .trees.
+ Plik .log. importujemy do programu Tracer -> weryfikujemy parametry.
+ Plik .trees. importujemy do programu TreeAnnotator -> uzyskujemy plik z drzewem o największej wiarygodności.
+ Plik z drzewem importujemy do programu FigTree -> wizualizujemy drzewo i formatujemy.

= Tranzycje i transwersje
- Tranzycje: zmiana puryny na purynę lub pirymidynę na pirymidynę.
- Transwersje: zmiana puryny na pirymidynę lub odwrotnie.

#figure(
    image("figures/tranzycje.png"),
    caption: [
        Na niebiesko zaznaczone są transwersje (pionowo i na skoks), na czerwono tranzycje (poziomo).
    ]
)

= Miara zmienności genetycznej
#figure(
    image("figures/zmiennosc_genetyczna.png"),
)

#pagebreak()

- h#sub[i] - heterozygotyczność osobnika (kolumna)
- h#sub[j] - heterozygotyczność locus / populacji (wiersz)
- H - heterozygotyczność populacji. Liczy się jako średnia h#sub[i] dla wszystkich osobników w populacji. Bądź jako średnia h#sub[j] dla wszystkich locusów w populacji. Obie średnie są sobie równe. Albo jako $ sum_(k=1)^n k = (k#sub[1] + k#sub[2] + ... + k#sub[n]) / n$ gdzie _n_ to ilość osobników w populacji (czyli i #sym.dot j w naszej tabeli to wynosi _40_), a _k_ to suma heterozygotycznych alleli w całej tabeli w naszym przypadku _11_. Co daje nam $ 11 / 40 = 0.275$
- _a, b, c, d, e_ - allele
- _A, B, C, D, E_ - locii

Jak liczymy h#sub[j]? Patrzymy ile jest różnych alleli w danym locusie (kolumna) i dzielimy przez liczbę wierszy.
 
Przykład:
- h#sub[j] dla osobnika _B_ = $ (1 + 1) / 5 = 2 / 5 = 0.4$
- h#sub[j] dla locus _A_ = $ 0 / 5 = 0$

Teraz policzmy h#sub[i], czyli heterozygotyczność locus / populacji (wiersz).

- h#sub[i] dla populacji _1_ = $ 1 / 8 = 0.125 $
- h#sub[i] dla populacji _3_ = $ (1 + 1 + 1 + 1 + 1 + 1) / 8 = 6 / 8 = 0.75 $
- h#sub[i] dla populacji _5_ = $ 0 / 8 = 0 $

Teraz zrobimy na innym przykładzie.
#figure(
    image("figures/zmiennosc_genetyczna_2.png"),
)

=== h#sub[i]
- h#sub[i] dla _locus 1_ - $ (1 + 1 + 1) / 9 = 3 / 9 = 1 / 3$
- h#sub[i] dla _locus 2_ - $ (1 + 1 + 1 + 1 + 1 + 1) / 9 = 6 / 9 = 2 / 3$
- h#sub[i] dla _locus 3_ - $ (1 + 1 + 1 + 1 + 1) / 9 = 5 / 9$

=== h#sub[j]
- h#sub[j] dla _osobnika 1_ - $ 0 / 3 = 0$
- h#sub[j] dla _osobnika 2_ - $ (1 + 1) / 3 = 2/3$
- h#sub[j] dla _osobnika 3_ - $ 1/3$
- h#sub[j] dla _osobnika 4_ - $ 2/3$
- h#sub[j] dla _osobnika 5_ - $ 1/3$
- h#sub[j] dla _osobnika 6_ - $ 1/3$
- h#sub[j] dla _osobnika 7_ - $ 2/3$
- h#sub[j] dla _osobnika 8_ - $ 1/3$
- h#sub[j] dla _osobnika 9_ - $ 3/3 = 1$

=== H
- H = $ (1 / 3 + 2 / 3 + 5 / 9) / 3 = (3 + 6 + 5) / 27 = 14 / 27$ - sposób pierwszy
- H = $ (0 + 2/3 + 1/3 + 2/3 + 1/3 + 1/3 + 2/3 + 1/3 + 3/3) / 9 = 13 / 27$ - sposób drugi, *UWAGA* tu jest błąd, który wynika z błędu w slajdzie, powinno być $ 14/27$ ale profesor się pomylił.

= Koalescencja
Dla genów dziedziczonych jednorodzicielsko np. _mtDNA_ czy _chromosom Y_.
Wszystkie kopie genu zbiegają się do jednej kopii – koalescencja.

= Odległość genetyczna *D* i d
- *D* - odległość między sekwencjami jako odsetek różnych nukleotydów w dopasowaniu.
- *d* - średnia liczba podstawień na pojedynczą pozycję w dopasowaniu.

#figure(
    image("figures/odleglosc_d_wykres.png"),
    caption: [
        Wykres odległości genetycznej *D* i *d*.
    ]
)

Różnice między *D*, a *d*:
- Główna różnica wynika z faktu, że *D* to miara obserwowalna, natomiast *d* to miara oszacowana, która uwzględnia model ewolucji.
- *D* zawsze jest mniejsze niż *d*, ponieważ *d* uwzględnia _„niewidoczne”_ zmiany genetyczne, które nie są bezpośrednio widoczne w sekwencjach porównawczych.
- Na wykresie:
    - Krzywa _D(t)_ rośnie wolniej, ponieważ reprezentuje obserwowalną różnicę.
    - Krzywa _d(t)_ rośnie szybciej, pokazując bardziej dokładny obraz liczby mutacji.

Odległość *d* w kontekście modelu Jukes-Cantora (JC):
Założenia:
- Tempo mutacji jest jednakowe dla wszystkich nukleotydów (oznaczymy je jako _μ_) i częstość nukleotydów jest jednakowa.

Wzór na odległość *d* w modelu Jukes-Cantora (JC): $ d = 2t * 3μ = 6t μ$, gdzie:
- _t_ to czas ewolucji.
- _μ_ to tempo mutacji.
inny wzór: $ d = -3/4 * ln((1 - 4) / (3D))$, gdzie _D_ to odległość genetyczna.

Odległość *D* w kontekście modelu Kimury 2-parametrowego (K2P):
Założenia:
- Tempo podstawień jest różne dla transwersji i tranzycji (oznaczymy je jako _α_ i _β_). Częstość nukleotydów jest jednakowa.

Wzór na odległość *D*: $ D = _ + V$, gdzie:
- _S_ - liczba pozycji, w których występuje tranzycja, podzielona przez całkowitą liczbę porównanych pozycji.
- _V_ - liczba pozycji, w których występuje transwersja, podzielona przez całkowitą liczbę porównanych pozycji.
_S_ i _V_ liczymy poprzez porównanie sekwencji.

Wzór na odległość *d*: $ d = -1/2 ln(1 - 2S - V) - 1/4ln(1 - 2V)$

*d* z *D* w miarę się pokrywa do wartości 0.25, dla *D* > 0.5 *d* zaczyna rosnąć szybciej.


= Metoda sekwencjonowania Sangera
Wersja krótka:
- Izolacja DNA.
- Przygotowanie reakcji sekwencjonowania.
- Synteza DNA.
- Rozdział fragmentów DNA.
- Odczyt fluorescencji.
- Analiza danych.

Wersja długa:
- *Izolacja DNA*: Na początku izoluje się fragment DNA, który ma być sekwencjonowany. Najczęściej używa się PCR (reakcji łańcuchowej polimerazy) do powielenia tego fragmentu.
- *Przygotowanie reakcji sekwencjonowania*: 
    - Do probówki dodaje się:
        - Matrycowy DNA (fragment, który ma być sekwencjonowany).
        - Starter (krótki odcinek DNA komplementarny do sekwencji początkowej matrycy).
        - Polimerazę DNA.
        - Nukleotydy (dNTPs) oraz zmodyfikowane nukleotydy (ddNTPs) oznaczone barwnikami fluorescencyjnymi.
- *Synteza DNA*: Polimeraza DNA zaczyna tworzyć nową nić, korzystając z matrycy i startera. Gdy wbudowany zostanie zmodyfikowany nukleotyd (ddNTP), synteza zostaje zakończona, ponieważ ddNTP nie posiada grupy hydroksylowej (3’-OH), która jest niezbędna do przyłączenia kolejnego nukleotydu.
- *Rozdział fragmentów DNA*: Powstałe fragmenty DNA różnej długości są rozdzielane za pomocą elektroforezy kapilarnej, gdzie krótsze fragmenty migrują szybciej niż dłuższe.
- *Odczyt fluorescencji*: Oznakowane ddNTPs emitują światło o różnych długościach fal w zależności od barwnika, co pozwala na określenie ostatniego nukleotydu w każdym fragmencie.
- *Analiza danych*: Na podstawie sygnałów fluorescencyjnych komputer odczytuje sekwencję DNA.

= Organizacja genomu u eukariontów
== Uszeregowanie homologiczne (paralogi)
#table(
    stroke: none,
    columns: 2,
    inset: 2pt,
    column-gutter: 12pt,
    [Osobnik 1], [LdhA],
    [Osobnik 1], [LdhB],
    [Osobnik 1], [LdhC],
    [Osobnik 2], [LdhA],
    [Osobnik 2], [LdhB],
    [Osobnik 2], [LdhC],
    [Osobnik 3], [LdhA],
    [Osobnik 3], [LdhB],
    [Osobnik 3], [LdhC],
)

== Uszeregowanie ortologiczne (ortologi)
#table(
    stroke: none,
    columns: 2,
    inset: 2pt,
    column-gutter: 12pt,
    [Osobnik 1], [LdhA, LdhB, LdhC],
    [Osobnik 2], [LdhA, LdhB, LdhC],
    [Osobnik 3], [LdhA, LdhB, LdhC],
)

- Paralogi: Duplikacja → Różnicowanie w obrębie gatunku.
- Ortologi: Specjacja → Zachowanie funkcji w różnych gatunkach.

= Związki filogenetyczne drzewa
- Takson monofiletyczny: takson posiadający wspólnego przodka i grupujący wszystkich potomków taksonu ancestralnego.
#figure(
    image("figures/monofiletyczny.png"),
    caption: [
        Drzewo filogenetyczne z taksonem monofiletycznym.
    ]
)
- Takson parafiletyczny: takson posiadający wspólnego przodka ale nie grupujący wszystkich potomków taksonu ancestralnego
#figure(
    image("figures/parafiletyczny.png"),
    caption: [
        Drzewo filogenetyczne z taksonem parafiletycznym.
    ]
)
- Takson polifiletyczny: takson nie posiadający wspólnego przodka i grupujący potomków kilku taksonów ancestralnych
#figure(
    image("figures/polifiletyczny.png"),
    caption: [
        Drzewo filogenetyczne z taksonem polifiletycznym.
    ]
)

= Zegar molekularny
== Etapy analizy
+ Szacowanie stopnia zróżnicowania sekwencji: obliczanie dystansu genetycznego
+ Kalibracja zegara:
    -  przybliżona data rozejścia się dwóch linii genetycznych, powinna być uzyskana z innych danych niż badania molekularne np.:
        + znane wydarzenie geologiczne
        + zapisów kopalnych organizmów
+ Określenie tempa substytucji RS:
    - dystans genetyczny podzielony przez czas np.: 2% na mln lat – „uniwersalny” zegar dla mtDNA obliczny z badań nad naczelnymi

== R#sub[S] vs R#sub[D]
Tempo dywergencji RD między dwoma dowolnie wybranymi taksonami jest równe podwojonemu tempu substytucji RS: $ R#sub[D] = 2 * R#sub[S] $

== strict vs relaxed
- opcja strict (rygorystyczna) - zakłada równe tempo substytucji wzdłuż gałęzi drzewa filogenetycznego (mało realna, ale lepsza dla nierówno próbkowanych matryc)
- opcja relaxed (rozluźniona) - zakłada różne tempo substytucji wzdłuż gałęzi drzewa filogenetycznego (realna, ale wymaga równomiernie próbkowanych matryc)

= Ewaluacja topologii drzewa
- Bootstrap: metoda resamplingu, polega na wielokrotnym losowaniu z powtórzeniami sekwencji z macierzy i ponownym budowaniu drzewa filogenetycznego.
- Posterior probability: prawdopodobieństwo a posteriori, wyznaczane na podstawie analizy bayesowskiej, określa jak bardzo dana gałąź drzewa jest wspierana przez dane.

#figure(
    image("figures/ewaluacja_topologii.png"),
    caption: [
        Ewaluacja topologii drzewa filogenetycznego.
    ]
)

