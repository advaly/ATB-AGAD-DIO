# ATB-AGAD-DIO Sample code

Armadillo拡張ボードのATB-AGAD-DIOをPythonから制御するときのサンプルコードです。

Armadilloは株式会社アットマークテクノの製品、ATB-AGAD-DIOはアドバリーシステム株式会社の製品です。

## 使用方法

### 値の取得
Armadilloのシェルから下記のように実行します。
```
$ python dio-addon.py
```

結果例（SW1, SW2ともにDI側の場合）

```
root@armadillo:~# python dio-addon.py

- List of current port status -
DI0 = 1
DI1 = 1
DI2 = 1
DI3 = 1
DI4 = 1
DI5 = 1
DI6 = 1
DI7 = 0
DO0 = (failed to read)
DO1 = (failed to read)
```

### 値の設定
Armadilloのシェルから下記のように実行します。

```
$ python dio-addon.py do0=1 do1=1
```

引数は、DO0または/およびDO1の出力値を指定できます。
どちらか1つを指定でも構いません。

```
$ python dio-addon.py do0=0
```

結果例（SW1, SW2ともにDO側の場合）

```
root@armadillo:~# python dio-addon.py do0=1 do1=1
Set DO0 = 1
Set DO1 = 1

- List of current port status -
DI0 = 1
DI1 = 1
DI2 = 1
DI3 = 1
DI4 = (failed to read)
DI5 = (failed to read)
DI6 = (failed to read)
DI7 = (failed to read)
DO0 = 1
DO1 = 1
```

## SWの組み合わせと有効なポート

### SW1=DI側、SW2=DI側

DI0|DI1|DI2|DI3|DI4|DI5|DI6|DI7|DO0|DO1
-- |-- |-- |-- |-- |-- |-- |-- |-- |--
IN |IN |IN |IN |IN |IN |IN |IN |-  |-

### SW1=DI側、SW2=DO側

DI0|DI1|DI2|DI3|DI4|DI5|DI6|DI7|DO0|DO1
-- |-- |-- |-- |-- |-- |-- |-- |-- |--
IN |IN |IN |IN |IN |IN |-  |-  |-  |OUT

### SW1=DO側、SW2=DI側

DI0|DI1|DI2|DI3|DI4|DI5|DI6|DI7|DO0|DO1
-- |-- |-- |-- |-- |-- |-- |-- |-- |--
IN |IN |IN |IN |-  |-  |IN |IN |OUT|-

### SW1=DO側、SW2=DO側

DI0|DI1|DI2|DI3|DI4|DI5|DI6|DI7|DO0|DO1
-- |-- |-- |-- |-- |-- |-- |-- |-- |--
IN |IN |IN |IN |-  |-  |-  |-  |OUT|OUT
