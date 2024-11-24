# gmpy2 is a C-coded Python extension module that supports
# multiple-precision arithmetic.
# pip install gmpy2
from gmpy2 import isqrt
from math import lcm

def factorize(n):
    # since even nos. are always divisible by 2, one of the factors will
    # always be 2
    if (n & 1) == 0:
        return (n/2, 2)

    # isqrt returns the integer square root of n
    a = isqrt(n)

    # if n is a perfect square the factors will be ( sqrt(n), sqrt(n) )
    if a * a == n:
        return a, a

    while True:
        a = a + 1 #4
        bsq = a * a - n #1
        b = isqrt(bsq) #1
        if b * b == bsq:
            break

    return a + b, a - b, (a + b - a + b)

print(factorize(960343778775549488806716229688022562692463185460664314559819511657255292180827209174624059690060629715513180527734160798185034958883650709727032190772084959116259664047922715427522089353727952666824433207585440395813418471678775572995422248008108462980790558476993362919639516120538362516927622315187274971734081435230079153205750751020642956757117030852053008146976560531583447003355135460359928857010196241497604249151374353653491684214813678136396641706949128453526566651123162138806898116027920918258136713427376775618725136451984896300788465604914741872970173868541940675400325006679662030787570986695243903017923121105483935334289783830664260722704673471688470355268898058414366742781725580377180144541978809005281731232604162936015554289274471523038666760994260315829982230640668811250447030003462317740603204577123985618718687833015332554488836087898084147236609893032121172292368637672349405254772581742883431648376052937332995630141793928654990078967475194724151821689117026010445305375748604757116271353498403318409547515058838447618537811182917198454172161072247021099572638700461507432831248944781465511414308770376182766366160748136532693805002316728842876519091399408672222673058844554058431161474308624683491225222383))
