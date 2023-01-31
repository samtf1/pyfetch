# Maintainer: samtf <samtf1@proton.me>
pkgname=pyfetch
pkgver=1.0
pkgrel=1
pkgdesc="Bare-bones alternative to Neofetch written in Python."
arch=('any')
url="https://github.com/samtf1/pyfetch"
license=('GPL3')
depends=("python" "python-psutil" "python-py-cpuinfo")
source=("https://github.com/samtf1/pyfetch")
md5sums=("SKIP")


package() {
        mkdir -p ${pkgdir}/usr/bin
        cp "${srcdir}/pyfetch" "${pkgdir}/usr/bin/pyfetch"
        chmod a+x "${pkgdir}/usr/bin/pyfetch"

}
