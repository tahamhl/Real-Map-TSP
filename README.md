# Real Map TSP

Bu proje, gerçek dünya verileriyle **Traveling Salesperson Problem (TSP)** problemini çözmeyi amaçlayan bir Python uygulamasıdır. İstanbul'un Kadıköy ilçesindeki sokak ağını kullanarak, rastgele seçilen 5 kavşak arasında en kısa rotayı bulur ve bu rotayı görsel olarak harita üzerinde gösterir.

## Kullanılan Kütüphaneler

- `osmnx`: Gerçek dünya harita verilerini indirir.
- `networkx`: Graf yapıları ve en kısa yol hesaplamaları için kullanılır.
- `folium`: Harita görselleştirme için kullanılır.

## Kurulum ve Çalıştırma

Bu projeyi çalıştırmak için öncelikle Python ve gerekli kütüphanelerin kurulu olması gerekmektedir.

### Gerekli Kütüphaneler:

Proje için gereken Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install osmnx networkx folium
