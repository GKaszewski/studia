

#set page(
  header: [_Mechanika kwantowa - przygotowanie_
  #h(1fr)
  Gabriel Kaszewski]
)
#set page(numbering: "— 1 —")

#align(center, text(17pt)[*Mechanika kwantowa - przygotowanie*])
= Abstract
W tym dokumenecie przedstawione są zagadnienia do zaliczenia przedmiotu Mechanika kwantowa.

#set quote(block: true)
#quote(attribution: "Jack Handey")[
    _Before you criticize someone, you should walk a mile in their shoes. That way when you criticize them, you are a mile away from them and you have their shoes._
]

= Co to jest stan punktu materialnego w mechanice klasycznej?
Stan punktu materialnego w mechanice klasycznej opisuje jego położenie i ruch w danym momencie.
+ Położenie - Jest to określenie miejsca, w którym znajduje się punkt materialny w przestrzeni. W układzie kartezjańskim położenie opisuje wektor $r=(x,y,z)$, gdzie $ x,y,z$ to współrzędne punktu w trzech wymiarach.
+ Pęd - $ p = m * v$  łączy informacje o prędkości $v$ (wektor prędkości w przestrzeni, określający kierunek i szybkość ruchu) oraz masie $m$ punktu materialnego. Prędkość może być również zapisana jako pochodna położenia względem czasu: $ v = (d x)/(d t)$
W układzie współrzędnych stan punktu materialnego można opisać za pomocą wektora stanu, który zawiera położenie i pęd:
$ "Stan punktu materialnego" = (r, p) $

= Czym różnią się stany kwantowe od stanów makroskopowych?
Stany kwantowe różnią się od stanów makroskopowych probabilistycznym charakterem, możliwością superpozycji, zasadą nieoznaczoności i kwantowaniem wielkości fizycznych. Stany makroskopowe są deterministyczne, ciągłe i opisywane w ramach klasycznych praw fizyki.

- *kwantowe*
  - probliastyczny charakter
  - superpozycja
  - zasada nieoznaczoności
  - kwantowanie wielkości fizycznych
- *makroskopowe*
  - deterministyczne
  - ciągłe
  - opisywane w ramach klasycznych praw fizyki

= Jaka rolę w mechanice kwantowej pełni przestrzeń Hilberta?
Przestrzeń Hilberta w mechanice kwantowej:
- jest matematycznym fundamentem do opisu stanów kwantowych.
- umożliwia opis operatorów, prawdopodobieństw i ewolucji czasowej.
- pozwala uogólnić mechanikę klasyczną na świat kwantowy w spójny, abstrakcyjny sposób.

= Co to jest przestrzeń wektorowa (liniowa)?
Przestrzeń wektorowa (liniowa) to matematyczna struktura, w której można dodawać wektory i mnożyć je przez skalary (liczby), spełniając pewne zasady.
== Definicja
Przestrzeń wektorowa to zbiór $V$, którego elementy nazywamy wektorami z dwoma operacjami:
+ Dodawanie wektorów: $ plus: V crossmark V -> V$
+ Mnożenie przez skalar: $ dot: F crossmark V -> V$, gdzie $F$ to ciało skalarów (np. liczby rzeczywiste)
Operacje muszą spełniać następujące aksjomaty:
=== Aksjomaty dodawania
+ Łączność: $ u + (v + w) = (u+v)+w$
+ Przemienność: $ u + v = v + u$
+ Element neutralny: Istnieje wektor $0 in V$, taki że $u + 0 = u$ dla każdego $u in V$
+ Element przeciwny: Dla każdego $u in V$ istnieje $-u in V$, taki że $u + (-u) = 0$
=== Aksjomaty mnożenia przez skalar
+ Łączność: $ a * (b * u) = (a * b) * u$, gdzie $a, b in F$
+ Element neutralny: $1 * u = u$, gdzie $1$ to element neutralny mnożenia w ciele $F$
+ Rozdzielność względem dodawania wektorów: $u * (a + b) = a * u + b * u$
+ Rozdzielność względem dodawania wektorów: $a * (u + v) = a * u + a * v$

= Co to jest przestrzeń unormowana?
Przestrzeń unormowana to rozszerzenie przestrzeni wektorowej, w której można mierzyć długości (normy) wektorów. Wprowadzenie normy pozwala na precyzyjne określenie takich pojęć jak długość, odległość, czy zbieżność wektorów w tej przestrzeni.
== Definicja
Przestrzeń unormowana to para $(V, norm( dot ))$, gdzie:
+ $V$ to przestrzeń wektorowa nad ciałem (np. $R$ lub $C$)
+ $norm( dot ): V -> R$ to funkcja nazywana normą, która spełnia następujące właściwości:
  - Nieujmność i zerowa długość: $ norm(v) gt.eq 0$ oraz $ norm(v) = 0 ⟺ v = 0$
  - Jednorodność: $ norm(alpha dot v) = |alpha| dot norm(v)$ dla wszystkich $alpha in R$ lub $C$, $v in V$
  - Nierówność trójkąta: $ norm(u + v) lt.eq norm(u) + norm(v)$ dla wszystkich $u, v in V$

= Co to jest przestrzeń zupełna?
Przestrzeń zupełna to taka przestrzeń metryczna, w której każda ciągłość Cauchy'ego jest zbieżna.
Przykłady przestrzeni zupełnych:
- Liczby rzeczywiste z metryką standardową $d(x,y) = |x - y| $
- Liczby zespolone z metryką standardową
- Przestrzenie Banacha
= Co to jest iloczyn skalarny?
Iloczyn skalarny to operacja algebraiczna definiowana na dwóch wektorach w przestrzeni wektorowej, która przyporządkowuje parze wektorów liczbę (skalar). 
Dla dwóch wektorów $u,v in R^n$, iloczyn skalarny jest zdefiniowany jako:
$ u dot v = u_1 v_1 + u_2 v_2 + ... + u_n v_n = sum_(i=1)^n u_i v_i $,
gdzie $u=(u_1, u_2, ..., u_n)$ i $v=(v_1, v_2, ..., v_n)$. 
= Co to jest przestrzeń Hilberta?
Przestrzeń Hilberta to kompletny, unormowany układ wektorowy nad liczbami zespolonymi, wyposażony w iloczyn skalarny.
Innymi słowy, przestrzeń Hilberta to przestrzeń liniowa nad ciałem liczb rzeczywistych lub zespolonych, która
- ma zdefiniowany iloczyn skalarny
- traktowana jako przestrzeń metryczna z metryka indukowaną przez iloczyn skalarny (poprzez normę) jest zupełna, tzn. każdy ciąg Cauchy'ego ma granicę.


Kompletność - oznacza, że każda zbieżna w sensie normy ciągła sekwencja wektorów ma granicę w tej przestrzeni.
= Co to jest wektor stanu? Jaka jest jego fizyczna interpretacja?
Wektor stanu to zbiór zmiennych (wielkości fizycznych), które w pełni opisują stan układu w danej chwili czasu.
Może to być wektor w przestrzeni euklidesowej $R^n$, przestrzeni zespolonej $C^n$ lub przestrzeni Hilberta etc.
$ x(t) = [x_1(t), x_2(t)...x_n(t)] $
== Fizyczna interpretacja w mechanice klasycznej
W mechanice klasycznej, wektor stanu opisuje układ w przestrzeni fazowej. Składa się z wektorów położenia $q(t)$ i pędu $p(t)$.
$ x(t) = [q(t), p(t)] $
Znając położenie i pęd, można określić zarówno aktualny stan układu, jak i przewidzieć jego przyszłe zachowanie.
== Fizyczna interpretacja w mechanice kwantowej
W mechanice kwantowej wektor stanu (czasem nazywany funkcją falową) to element przestrzeni Hilberta $H$, który opisuje
stan układu kwantowego. Wektor stanu może być reprezentowany jako $|psi angle.r$.
$ |psi angle.r = sum_(i) C_i |phi.alt_i| $, gdzie $|phi.alt_i|$ to bazowe wektory stanu, a $C_i$ to współczynniki opisujące 
rozkład w tej bazie.

Wektor stanu zawiera pełną informację o układzie kwantowym, a jego moduł kwadratowy $|C_i|^2$ daje prawdopodobieństwo
znalezienia układu w danym stanie $|phi.alt_i angle.r$.
= Porównaj przestrzeń stanów w mechanice klasycznej z przestrzenią stanów w mechanice kwantowej.
== Mechanika klasyczna
- Przestrzen fazowa: stan układu opisany jest przez punkt w przestrzeni fazowej, złożony z położenia i pędu. $x = (q, p)$
- Charakter: Jest to przestrzeń euklidesowa, w której można jednoznacznie określić stan układu (deterministyczność).
- Stan układu: Reprezentowany jako punkt, którego ewolucja jest opisana równaniami Hamiltona lub Newtona.
- Pomiar nie zmienia stanu układu. Możemy dokładnie określić położenie i pęd jednocześnie.
- Nie ma pojęcia superpozycji. Układ nie może być w wielu stanach jednocześnie.
- Położenie i pęd można określić jednoczesnie z dowolną dokładnością.
== Mechanika kwantowa
- Przestrzeń Hilberta: stan układu opisany jest przez wektor stanu w przestrzeni Hilberta. $|psi angle.r$
- Charakter: Wektory stanu mogą być znormalizowane $(angle.l psi|psi angle.r = 1)$ i mogą różnić się fazą (faza globalna nie ma znaczenia fizycznego).
- Stan układu: Reprezentowany jako superpozycja możliwych stanów bazowych $|psi angle.r space = sum_(i) C_i |phi.alt_i|$
- Pomiar zmienia stan układu (kolaps funkcji falowej). Po pomiarze układ przechodzi w stan odpowiadający wynikowi pomiaru.
- Stany mogą być w superpozycji. Przykład: Elektron może jednocześnie znajdować się w dwóch stanach energetycznych opisanych jako:
$|psi angle.r = C_1 |phi.alt_1angle.r + C_2 |phi.alt_2angle.r$
- Zasada nieoznaczoności Heisenberga: nie można jednocześnie znać dokładnych wartości położenia i pędu. Dla operatorów $attach(q, t: hat)$ (położenie) i $attach(p, t: hat)$ (pęd):
$Delta q dot Delta p >= ℏ/2$

#table(columns: (auto, 1fr, 1fr), table.header([*Cecha*], [*Mechanika klasyczna*], [*Mechanika kwantowa*]),
[Przestrzeń stanów], [Przestrzeń fazowa], [Przestrzeń Hilberta],
[Charakter stanu], [Punkt w przestrzeni fazowej], [Wektor w superpozycji stanów],
[Pomiar], [Nie zmienia stanu], [Powoduje kolaps funkcji falowej],
[Superpozycja], [Brak], [Możliwa],
[Zasada nieoznaczoności], [Nie obowiązuje], [Obowiązuje],
)
= Ile wymiarów i dlaczego ma przestrzeń stanów pojedynczego elektronu, gdy przez stan elektronu rozumiemy jego położenie w przestrzeni?
Gdy przez stan elektronu rozumiemy jego położenie w przestrzeni, przestrzeń stanów elektronu jest przestrzenią trójwymiarową $R^3$.
Elektron porusza się w przestrzeni fizycznej, która jest trójwymiarowa, co oznacza, że jego położenie można opisać za pomoca trzech współrzędnych kartezjańskich:
$r = (x,y,z)$. Przestrzeń stanów to zbiór wszystkich możliwych konfiguracji układu. W przypadku elektronu mamy tylko położenie, więc przestrzeń stanów jest trójwymiarowa. Mamy tyko trzy wymiary.

== Krócej
Jeśli ograniczamy się wyłącznie do położenia elektronu w przestrzeni, przestrzeń stanów jest trójwymiarowa, ponieważ wymagane są trzy współrzędne
$(x,y,z)$ do jednoznacznego określenia położenia w przestrzeni fizycznej.

= Ile wymiarów i dlaczego ma przestrzeń stanów pojedynczego elektronu, gdy przez stan elektronu rozumiemy jego spin?
Gdy przez stan elektronu rozumiemy jego spin, przestrzeń stanów ma dokładnie 2 wymiary.
Przestrzeń stanów elektronu, gdy uwzględniamy tylko spin, jest dwuwymiarową przestrzenią Hilberta. Wynika to z faktu, że spin $1/2$ może przyjmować tylko dwa dyskretne stany własne
$(+1/2$ i $-1/2)$, co odpowiada dwóm wymiarom przestrzeni kwantowej.
= Czy stany obiektów kwantowych są obserwowane?
Stany obiektów kwantowych nie są bezpośrednio obserwowane, lecz wnioskujemy o nich na podstawie wyników pomiarów.
Obserwacja w mechanice kwantowej różni się fundamentalnie od klasycznej,
a jej natura jest probabilistyczna i związana z kolapsem funkcji falowej.
= Co to jest obserwabla (opisać słowami)?
Obserwabla to mierzalna wielkość w układzie kwantowym, reprezentowana przez operator hermitowski. 
Dzięki obserwablom możemy wnioskować o stanie układu kwantowego, ale wyniki pomiaru są zawsze probabilistyczne
i zależą od stanu układu przed pomiarem.
= Co to jest operator liniowy na przestrzeni wektorowej?
Operator liniowy na przestrzeni wektorowej to funkcja, która przekształca wektory z danej przestrzeni wektorowej
w inne wektory (z tej samej lub innej przestrzeni), przy czym przekształcenie to jest liniowe,
czyli zachowuje strukturę wektorową.
= Jaki element w matematycznej strukturze mechaniki kwantowej odpowiada obserwabli?
W matematycznej strukturze mechaniki kwantowej obserwabli odpowiadają operatory hermitowskie (lub samosprzężone) działające w przestrzeni Hilberta.
= Napisz równanie na wartość własną operatora A! Wskaż w tym równaniu symbol, odpowiadający wektorowi własnemu operatora A i symbol, odpowiadający wartości własnej operatora A!
$Â |phi.alt angle.r = a|phi.alt angle.r$, gdzie:
+ $Â$ - operator (np. operator hermitowski), który reprezentuje obserwablę w przestrzeni Hilberta.
+ $|phi.alt angle.r$ - wektor własny operatora $Â$, który reprezentuje stan układu.
+ $a$ - wartość własna operatora $Â$, która odpowiada wynikowi pomiaru obserwabli. Jest to liczba rzeczywista.
= Jakiego operatora wartości włanse reprezentują możliwe wyniki pomiarów danej obserwabli?
Wartości własne operatora hermitowskiego odpowiadają możliwym wynikom pomiarów obserwabli reprezentowanej przez ten operator.
Operator hermitowski pełni kluczową rolę, ponieważ gwarantuje, że wyniki pomiarów są liczbami rzeczywistymi, 
a jego stany własne definiują możliwe stany układu po pomiarze.
= Jaki matematyczny fakt odpowiada skwantowaniu dopuszczalnych wyników pomiarów?
Matematycznym faktem, który odpowiada skwantowaniu dopuszczalnych wyników pomiarów w mechanice kwantowej,
jest to, że operator hermitowski (reprezentujący obserwablę) może mieć dyskretny zbiór wartości własnych,
jeśli jego spektrum jest dyskretne.