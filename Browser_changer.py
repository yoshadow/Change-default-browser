#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Output:
# Al ejecutar:
# 1. Se revisará qué navegador está por defecto.
# 2. Se colocará el navegador siguiente al que estaba por defecto.
# 3. Se notificará qué navegador se puso por defecto.

import os

# Variables
firefox = "firefox.desktop"
opera = "opera_opera.desktop"

def navegador_por_defecto():
    stream = os.popen("xdg-settings get default-web-browser")
    output = stream.read().strip()
    return output

def run():
    navegador_actual = navegador_por_defecto()
    #print(output)
    if firefox in navegador_actual:
        os.system("xdg-settings set default-web-browser "+opera)
    else:
        os.system("xdg-settings set default-web-browser "+firefox)

    nuevo_navegador = navegador_por_defecto()
    if firefox in nuevo_navegador:
        nuevo_navegador = "Firefox"
    elif opera in nuevo_navegador:
        nuevo_navegador = "Opera"

    notificacion = "Navegador "+nuevo_navegador+" puesto por defecto."
    print(notificacion)
    os.system("notify-send '"+notificacion+"'")


if __name__ == "__main__":
    run()
