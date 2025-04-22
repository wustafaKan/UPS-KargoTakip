Languages
-
**Python**
**Node.js**

Installation
-
```
pip install requests
```

Explanation
-
A customer wanted to show the location status of UPS shipments on their shipping site. Customers could see the status of their UPS shipments without leaving the site.  After opening DevTools and finding the right request in the Network section, I created a simple API with the help of https://curlconverter.com/. I had an API, but I needed to create a TOKEN to make a request. This is where I got help from my friend who you can find on githup with the username “AmourHG”. We went through the code and with the help of reverse engineering “<strong>AmourHG</strong>” figured out how to create the token needed for the API. You should run “createToken.js” before running “ups.py”. You should get the token information sent to localhost/3000 and run “ups.py”. After entering the cargo tracking number, you can access the status, datetime and location information of the cargo with the help of the API.

<br />

Açıklama
-
Bir müşterim kendi kargo sitesi üzerinden, UPS kargolarının konum durumlarını göstermek istiyordu. Müşteriler siteden çıkmadan UPS kargolarının durumlarını görebilecekti.  DevTools açıp Network kısmından doğru isteği bulduktan sonra https://curlconverter.com/ yardımıyla basit bir API oluşturdum. Elimde bir API vardı ancak istek atabilmem için TOKEN oluşturmam gerekiyordu. Bu kısımda "<strong>AmourHG</strong>" kullanıcı ismi ile githup'da bulabileceğiniz arkadaşımdan yardım aldım. Kodları inceledik ve tersine mühendislik yardımıyla API için gerekli olan token'ın nasıl oluşturulduğunu "AmourHG" buldu. "ups.py"'yi çalıştırmadan önce "createToken.js"'i çalıştırmalısınız. localhost/3000'e gönderilen token bilgisini alarak "ups.py" kodunu çalıştırmalısınız. Kargo takip numarasını girdikten sonra API yardımıyla kargonun status, datetime ve location bilgilerine ulaşabilirsiniz. 

