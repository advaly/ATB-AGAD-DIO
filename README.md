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

※ 起動時に一度SW1、SW2の値を読んで処理を分岐しており、ランタイムでのSWの切り替えには対応しておりません。

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

## DI/DOポートへのアクセスについて

### クラスファイル名

以下のファイルによって制御することができます。
`DIx`, `DOx` の `x` は、DO/DIの各インデックスを意味します。

DI/DO | Direction | Path
--|--|--
DI | IN | `/sys/devices/soc0/addon/DIx_INTF1/value`
DO | OUT | `/sys/devices/soc0/addon/DOx_INTF1/value`


### 例

DI2の状態を取得する。
```
[armadillo ~]# cat /sys/devices/soc0/addon/DI2_INTF1/value
1
```

DO0の状態を取得する。
```
[armadillo ~]# echo 1 > /sys/devices/soc0/addon/DO0_INTF1/value
```
