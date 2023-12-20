

## MaxLotto

MaxLotto to prosty skrypt przewidywania dowolnej loterii Lotto za pomocą sieci neuronowej. Tak wiemy, loterii nie da się przewidzieć, ale czasami warto spróbować ;-) 

## Instalacja

Aby zainstalować MaxLotto, musisz mieć zainstalowany program Python 3.x i następujące biblioteki:
- numpy
- tensorflow
- keras

Możesz zainstalować te biblioteki za pomocą pip.
Uruchom następujące polecenie:

pip install numpy tensorflow keras

## Dane

Aby skorzystać z programu, będziesz potrzebować pliku danych zawierającego wyniki poprzednich losowań danej loterii. Plik ten powinien być w odpowiednim formacie oddzielonym przecinkami, przy czym każdy wiersz reprezentuje pojedyncze losowanie, a liczby są w porządku rosnącym, a wiersze są w nowym wierszu bez przecinków. Nie używaj białych spacji. Numer ostatniego wiersza nie może zawierać niczego po ostatnim numerze!.

Po utworzeniu pliku z danymi, możesz uruchomić skrypt "neuro.py" w celu wytrenowania modelu i wygenerowania prognozy. Skrypt wydrukuje na konsoli przewidywane liczby.

Powodzenia! ;-)


## Licencja
MIT License

Copyright (c) 2023 CorvusCodex

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
