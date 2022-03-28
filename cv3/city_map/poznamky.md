Co potřebujeme za role a jaká data z nich?
    display - název
    area - rozloha
    population - počet obyvatel
    location - souřadnice

Máme datový set, abychom mohli zobrazovat/předávat informace, potřebujeme ty horní čtyři role.

Qt.UserRole
    chceme si vyrábět vlastní role, tahle má první číslo a ty další vždycky větší

roleNames
    qml předáme info, že máme role, které nejsou původní
    vrátí slovník všech rolí
    defaultně nic - vyrobíme vlastní - vezmeme původní a rozšíříme je
    QByteArray - jméno role v qml
        není normální string, není kódováno v utf-8, nebere všechny znaky, anglická abeceda _ apod. v pohodě

role nadefinované uvnitře citylistmodel

-> doplnit role do programu z minula a vypsat je

příště zadá první úkol

kliknu na město, vypíše rozlohu a poč. obyv, vycentruje mapu

někde v tom qml rozhraní si udělám property, která si pamatuje aktuální položku -> property var currentModelItem;
    var - je to obecný typ
    currentModelItem - jak se jmenuje

ze citylist model nezvládneme dostat info o aktuální položce
-> delegateModel

activeMapType: supportedMapTypes[supportedMapTypes.length - 1] // chceme, aby použil naši mapu
    seznam dostupných map, ta naše je poslední
    supportedMapTypes.length - 1 =>vem tu poslední

aby byl v mapě u názvu v závorce poč. obyv
místo jména obdélník/kolečko jehož velikost bude odpovídat počtu obyvatel
vedle obdélníku i název obce

udělat klikací obce - bude to provázané i obráceně