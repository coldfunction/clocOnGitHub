# clocOnGitHub

## Install on MacOS
* % brew install cloc
* % git clone https://github.com/coldfunction/clocOnGitHub.git
* % cd clocOnGitHub

## Execute
* python3 clocgithub.py $the_github_https_address.git

## Example
```
% python3 clocgithub.py https://github.com/qemu/qemu.git
Cloning into '.clocOnGitHubtmp'...
remote: Enumerating objects: 533486, done.
remote: Total 533486 (delta 0), reused 0 (delta 0), pack-reused 533486
Receiving objects: 100% (533486/533486), 303.38 MiB | 1.48 MiB/s, done.
Resolving deltas: 100% (432847/432847), done.
Updating files: 100% (7988/7988), done.
    7580 text files.
    7512 unique files.                                          
    1433 files ignored.

github.com/AlDanial/cloc v 1.88  T=15.10 s (420.3 files/s, 165369.9 lines/s)
---------------------------------------------------------------------------------------
Language                             files          blank        comment           code
---------------------------------------------------------------------------------------
C                                     2998         198841         160243        1227899
C/C++ Header                          1869          35122          76095         183975
Pascal                                  35          33170         245710         102266
Python                                 261           9141          10492          36031
JSON                                   244           1016              0          22925
C++                                     11           4023           7230          18208
Bourne Again Shell                     234           5050           7059          17318
reStructuredText                       125           5850           2487          14305
Assembly                               197           2857           1847          13460
Bourne Shell                            62           1352           2092          12584
Meson                                  186            607            243           6927
Haxe                                     5           1369             13           6697
Perl                                    11           1148           1039           6461
SVG                                      2              2              2           1982
XML                                     37            134            192           1874
YAML                                    13            202            182           1780
Windows Module Definition                5             69              0           1546
Objective-C                              1            224            266           1399
make                                    18            228            153           1009
Windows Resource File                    3            102              0            802
PO File                                  8            153             35            415
WiX source                               1             13              0            176
TNSDL                                    2             24              0            121
Dockerfile                               2              6             10             44
HTML                                     7              0              0             35
INI                                      2              5              0             29
GLSL                                     3              9              0             21
IDL                                      1              1              0             19
Markdown                                 1              2              0              5
Lisp                                     1              0              0              2
---------------------------------------------------------------------------------------
SUM:                                  6345         300720         515390        1680315
---------------------------------------------------------------------------------------


```
