# Deníček změn

## 26.10.2026
**Co bylo změněno?**
- Přidána nová entita `AnnotationType` pro evidenci typů anotací, včetně českého a anglického názvu.
- Entita byla zapojena napříč databázovou, service a GraphQL vrstvou; GraphQL nabízí načtení podle ID, stránkový dotaz a operace vložení, úpravy a smazání.
- Anotace nyní může odkazovat na svůj typ přes volitelný cizí klíč `annotation_type_id`. Doplněny jsou vztahy z anotace na typ i z typu na související anotace.
- Do `systemdata.json` byla přidána ukázková data typů a anotací a doplněny testy vztahu i dostupnosti operací ve schématu.

**Co jsme objevili?**
- Pro rozlišování anotací bylo potřeba oddělit jejich typ od samotného textu anotace do samostatné entity.
- Vztah musí být volitelný, aby bylo možné zachovat i anotace bez přiřazeného typu.

**Problém**
- Model anotace dosud neměl samostatný číselník typů ani vazbu, přes kterou by šlo typ anotace ukládat a zobrazovat.

**Řešení**
- Vytvořili jsme `AnnotationTypeModel`, jeho GraphQL typ a službu a zaregistrovali potřebný dataloader.
- Do `AnnotationModel` jsme přidali nepovinnou vazbu na typ. GraphQL zpřístupňuje vztah v obou směrech a nabízí CRUD i dotazy pro typy anotací.
- Připravili jsme ukázková data a ověřovací testy pro databázový vztah a GraphQL schéma.

## 22.10.2026
**Co bylo změněno?**
- Tvorba souboru `.env`, která povoluje demodata a naplňuje tabulku příslušnými daty.

**Co jsme objevili?**
- Nesprávná funkčnost a tvorba tabulky z důvodu `isDemoData = false`, tabulka se nesprávně tvořila.

**Problém**
- Po dokončení seedování a následném spuštění tabulky se demodata nenačetla do tabulka a ta se vytvořila prázdná.

**Řešení**
- Vytvořili jsme soubor `.env`, kde jsme demodata odblokovali.

## 19.10.2026
**Co bylo změněno?**
- Úprava `main.py` a `seed.py` v `DBDefinitions`.
- Doplnění `systemdata.json` o cvičná demo data.

**Co jsme objevili?**
- V hlavním spouštěcím souboru nebylo implifikováno seedování dat našeho modelu.
- V `seed.py` chyběly požadavky našeho modelu.
- Chyběly naše cvičná data pro názornou ukázku funkčnosti.

**Problém**
- Nemohli jsme nijak spustit náš model, protože nenačítal žádná data a nebyl vůbec napojen na hlavní spouštěcí soubor.

**Řešení**
- Upravili jsme příslušné soubory a vytvořili počáteční demo data.

## 15.10.2026
**Co bylo změněno?**
- V `DBDefinitions` příslušná úprava souborů našeho modelu.
- V `Dataloaders` byl připojen náš model do souboru `__init__.py`.
- Do složky `ServiceDefinitions` byla vytvořena podsložka `Domain_Annotation` se soubory `AnnotationService` a `__init__.py`.
- Úprava `ServiceContext.py`.

**Co jsme objevili?**
- Chyběly základní složky a soubory našeho modelu napříč různými vrstvami `DBDefinitions`.
- Model nebyl správně připojen do spouštěcího souboru `main.py`.

**Problém**
- Model nešel spustit, nebyly řádně připojeny příslušné knihovny a v `ServiceDefinitions` vůbec neexistoval náš model.

**Řešení**
- Vytvořili jsme nezbytně důležité soubory s patřičnými knihovnami pro náš model.
- Do již vzniklých a funkčních souborů jsme napojili náš modelu.

## 12.10.2026
**Co bylo změněno?**
- V `DBDefinitions` vznikla složka `Domain_Annotation` se soubory `AnnotationModel.py` a `__init__.py`.
- V `GraphTypeDefinitions` vznikla opět složka `Domain_Annotation` se soubory `AnnotationGQLModel.py` a `__init__.py`.
- Byly upraveny soubory `mutation.py` a `query.py` podle našich potřeb.

**Co jsme objevili?**
- Původní projekt gql evolution obsahoval pouze model Event a EventType a nikoliv náš modul Annotation.

**Problém**
- Našemu modelu úplně chyběly kořenové soubory a jejich napojení.

**Řešení**
- Vytvořili jsme základní soubory našeho modelu a napojili je na již vytvořený projekt.

## Časová osa commitů
| Datum | Hlavní změna | Stručný popis |
|---|---|---|
| 26.10.2026 | Nová entita AnnotationType | Přidání typů anotací, jejich CRUD v GraphQL, vazby na anotace a ukázkových dat. |
| 22.10.2026 | Odblokování demodat | Tvorba souboru `.env`, který demodata povoluje a naplňuje tabulku daty. |
| 19.10.2026 | Přidání testovací anotace | Úprava `main.py` a `seed.py` a tvorba nových demodat. |
| 15.10.2026 | Spuštění main – iniciace | Tvorba a úprava souborů, zakomponování našeho modelu do `main.py`. |
| 12.10.2026 | Úvodní tvorba modelu | Tvorba kořenových a základních souborů modelu `Annotation` a jeho napojení. |

## Jak spustit konkrétní app

```bash
python -m src.DBDefinitions.main Annotation seed '{}' --no-makeup
```
## Jak sestavit konkrétní app

```bash
python -m src.DBDefinitions.main Annotation List '{}' --no-makeup
```