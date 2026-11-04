# CallFootprint

Bir modüldeki çağrı ifadelerini kullanıldıkları satırlarla eşler.

## Girdi

Python kaynak metni.

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python callfootprint.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
{
  "send": [
    1,
    2
  ]
}
```

Python dosyasını doğrudan incelemek için: `python callfootprint.py --source module.py`.
