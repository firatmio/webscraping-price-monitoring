# Web Scraping Price Monitoring

Bu proje, e-ticaret sitelerindeki (şu anda Trendyol odaklı) ürün fiyatlarını takip etmek için geliştirilen Python tabanlı bir araçtır.

## Proje Durumu: Geliştirme Aşamasında (Alpha)

Proje şu anda erken geliştirme aşamasındadır. Temel özellikler ve mevcut durum aşağıdadır:

*   **Veri Kazıma (Web Scraping):** `requests` ve `BeautifulSoup` kütüphaneleri kullanılarak Trendyol ürün sayfalarından ürün adı ve fiyat bilgisi çekilebilmektedir.
*   **Veri Modeli:** Ürün (`Product`) ve Fiyat Takipçisi (`PriceMonitor`) sınıfları oluşturulmuştur.
*   **Kullanıcı Arayüzü (GUI):** `customtkinter` kullanılarak modern bir arayüz tasarlanması planlanmaktadır (kod yapısı mevcuttur ancak şu an aktif değildir).
*   **Bildirimler:** Fiyat değişikliklerinde `win10toast` ile masaüstü bildirimleri gönderilmesi hedeflenmektedir.

## Gereksinimler

Projenin çalışması için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

*   `beautifulsoup4`
*   `requests`
*   `customtkinter`
*   `win10toast`

## Kurulum ve Kullanım

Şu an için proje kaynak kodları üzerinden çalıştırılabilir durumdadır. Geliştirme süreci devam ettikçe kurulum adımları netleşecektir.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.