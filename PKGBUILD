# Maintainer: samtf <samtf1@proton.me>
pkgname=pyfetch
pkgver=1.0
pkgrel=1
pkgdesc="Bare-bones alternative to Neofetch written in Python."
arch=('any')
url="https://github.com/samtf1/pyfetch"
license=('GPL3')
depends=()
source=("https://github.com/samtf1/pyfetch")
md5sums=("SKIP")


package() {
        cd ${srcdir}
        mkdir -p ${pkgdir}/usr/bin
        cp "${srcdir}/pyfetch.py" "${pkgdir}/usr/bin/pyfetch"
        chmod +x "${pkgdir}/usr/bin/pyfetch"

}
