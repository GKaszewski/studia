

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

= Co to jest iloczyn skalarny?

= Co to jest przestrzeń Hilberta?
Przestrzeń Hilberta to kompletny, unormowany układ wektorowy nad liczbami zespolonymi, wyposażony w iloczyn skalarny.
Innymi słowy, przestrzeń Hilberta to przestrzeń liniowa nad ciałem liczb rzeczywistych lub zespolonych, która
- ma zdefiniowany iloczyn skalarny
- traktowana jako przestrzeń metryczna z metryka indukowaną przez iloczyn skalarny (poprzez normę) jest zupełna, tzn. każdy ciąg Cauchy'ego ma granicę.


Kompletność - oznacza, że każda zbieżna w sensie normy ciągła sekwencja wektorów ma granicę w tej przestrzeni.
= Co to jest wektor stanu? Jaka jest jego fizyczna interpretacja?

= Porównaj przestrzeń stanów w mechanice klasycznej z przestrzenią stanów w mechanice kwantowej.

= Ile wymiarów i dlaczego ma przestrzeń stanów pojedynczego elektronu, gdy przez stan elektronu rozumiemy jego położenie w przestrzeni?

= Ile wymiarów i dlaczego ma przestrzeń stanów pojedynczego elektronu, gdy przez stan elektronu rozumiemy jego spin?

= Czy stany obiektów kwantowych są obserwowane?

= Co to jest obserwabla (opisać słowami)?

= Co to jest operator liniowy na przestrzeni wektorowej?

= Jaki element w matematycznej strukturze mechaniki kwantowej odpowiada obserwabli?

= Napisz równanie na wartość własną operatora A! Wskaż w tym równaniu symbol, odpowiadający wektorowi własnemu operatora A i symbol, odpowiadający wartości własnej operatora A!

= Jakiego operatora wartości włanse reprezentują możliwe wyniki pomiarów danej obserwabli?

= Jaki matematyczny fakt odpowiada skwantowaniu dopuszczalnych wyników pomiarów?