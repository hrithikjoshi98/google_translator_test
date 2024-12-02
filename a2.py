import requests
from parsel import Selector

cookies = {
    'SID': 'g.a000qgiE86cf_U8KuoN--kRfyGgj5e43jRGX8cJiAmoXnaEBL_ECSyzexV433Yv6MecacKkfsQACgYKAZMSARASFQHGX2Mi9x0D4EiJ3Xbqpi6XD83CEBoVAUF8yKq023dV85gPXppFIFdapnmM0076',
    '__Secure-1PSID': 'g.a000qgiE86cf_U8KuoN--kRfyGgj5e43jRGX8cJiAmoXnaEBL_ECyg2R0C5kppdjciJAJ9-gFQACgYKAfISARASFQHGX2MiP6rDWyzw7aqaZpyOTPdbPRoVAUF8yKomuo7DrXKXgzqJgh4coOM70076',
    '__Secure-3PSID': 'g.a000qgiE86cf_U8KuoN--kRfyGgj5e43jRGX8cJiAmoXnaEBL_ECqMEY5u4-tLn84Lv61_N74QACgYKAZgSARASFQHGX2MiwPQb0wjs9MC4c5KqJO00_BoVAUF8yKo-iURgwIzymWu4S7BjQNAA0076',
    'HSID': 'Akfbc5PYN9P2V3c7d',
    'SSID': 'A6dj94qEYtFLyaoyQ',
    'APISID': 'BKPFhwlGmmdwwwK-/AuiXcEDG4M2gDHbYy',
    'SAPISID': 'ElfTRU8GxnrF7Apo/AvufrDzlNgmcUylHr',
    '__Secure-1PAPISID': 'ElfTRU8GxnrF7Apo/AvufrDzlNgmcUylHr',
    '__Secure-3PAPISID': 'ElfTRU8GxnrF7Apo/AvufrDzlNgmcUylHr',
    'SEARCH_SAMESITE': 'CgQI15wB',
    '__Secure-ENID': '24.SE=ZrjRl9yj4BoEFKOnsUM_myXdXzcaZ1H_EIGA7AA9CH6DXOi_TKBEVXkjqx5lzurZGUZyNS8wLBAxPIDut3WT3-fffSjH2MT7lAz8gw1ZSMmnmjtNrzMLkJaLlUTHV8c6c4IGtmpGLcS3Ge2c3bvQdvLYBzye4Vao4ZfpxheYYH5qXYR2TKKa3j8ajkM-zRSNgrpCw3Gde55qrSWDDpk4qOntcdKKIMXfd6EQhPjOsXYh_W_GPpfdOiJxYiWYEKbeGJqtFMxGzhqKpSfivbcQYB1w3_tlWD5nsAmesOf61xUqUSJC7QwjpXb3K4i5R1W1-kEuPDieDIaZE4Nsjtwj7VDlQEuvsDjAYEJpKT-ZuILwTHw4S4nt5fg',
    'AEC': 'AZ6Zc-VVtOfvqbh_n35kiuMHJ2jbhCb3hhr1eHm_KQFRe2yX7CwULMMYIfc',
    'OTZ': '7847333_34_34__34_',
    'NID': '519=F6D3riUC5AN7VNFCEQTmwMGP4QZk36steLkSDW2_cdmPl8BGhPbzORegOgNJHiQJCZCkS4ycmeXO-4cUzR-bmJiAWMamrcTdKmpTQ_d55gL8kFaTSax769gyRC8NUFzl5bmiHvVdAXm7lGPk-wJqDWvKlS2x8ZA-7sHZU0VmNIoyYyZqVAuISo-fgfui6ZpQnmk6CRSSjHUXQlUzvEXOuaM_JVGo7vVGefOkg8jmYLMfy4GKcbHtDGANBnzjB6iZy523X4cGzzC1RxDAOCvigXmPDB4mnCwCqNGhbW9ekMKeTvEVdrK9LcvCCUgfAALQ2ZGwqt0sWo_XuMWb_mNN3JBQDJMNs5S1vKhhsY1R1Bw6BL2EOc9sTu6Pc6k05bEUMHzjK2O8iO1yjgk31M2ZtVCcL1MXWxrenBxwQryLS0VVVXyqtUiqO6_WZgFqXoIGrxeUV_-ToxktZb1zHgILePrLRbRsE72lBXoX9e-BydMpm91J3vIo2Gqp00ase02H1YNago9GGC7C5mcsh2p5kkb1N-HdORVkOZBqkDBcfjj3ONsdGWg9fxh1P1HZy26CR7qyDOa9shkartMfJ7L0ICriObzOh_ln4mIOyQ2KXWhGmH5Uv77OmS12ienDPSLys6E_BRGF2dW3iWcIOKksIhZ8jckya6eiIiZHa-TFsAhQni2d_rWEvY1jfyX70d0yfmtILIq2tskvecXoQVbM9dMML65zgcOsbV3fxrhiDSfLSYkaW9W04TkXHbDH-f0HKoB-Ci1OGZca52Txrpj2qdHvVQ',
    '__Secure-1PSIDTS': 'sidts-CjEBQT4rX-pEUHgJw6U2xuPjj5PlYYtX-sndvcgJGHw3_sc9fvm7QXSPjOxJipd_zZquEAA',
    '__Secure-3PSIDTS': 'sidts-CjEBQT4rX-pEUHgJw6U2xuPjj5PlYYtX-sndvcgJGHw3_sc9fvm7QXSPjOxJipd_zZquEAA',
    'SIDCC': 'AKEyXzWW8y-5uWrM0VcCN0e6nGNgdhaC1LXfUXIQK1ilUNDhJeywBBjETJwRBrdAQM0K8vz15A',
    '__Secure-1PSIDCC': 'AKEyXzXeRPU_m1The1I2UlWm0gkWWhdpYH_3Fx5YdyD9J1jnI8KS0rmzeKj6UanYAMixx6ri1Q',
    '__Secure-3PSIDCC': 'AKEyXzUU6eRR-YjSHPSRS0hYbydpATGLurkudC4_7xzcJumljV2SEjTI23EyHhhHJum_WUfH6RU',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'SID=g.a000qgiE86cf_U8KuoN--kRfyGgj5e43jRGX8cJiAmoXnaEBL_ECSyzexV433Yv6MecacKkfsQACgYKAZMSARASFQHGX2Mi9x0D4EiJ3Xbqpi6XD83CEBoVAUF8yKq023dV85gPXppFIFdapnmM0076; __Secure-1PSID=g.a000qgiE86cf_U8KuoN--kRfyGgj5e43jRGX8cJiAmoXnaEBL_ECyg2R0C5kppdjciJAJ9-gFQACgYKAfISARASFQHGX2MiP6rDWyzw7aqaZpyOTPdbPRoVAUF8yKomuo7DrXKXgzqJgh4coOM70076; __Secure-3PSID=g.a000qgiE86cf_U8KuoN--kRfyGgj5e43jRGX8cJiAmoXnaEBL_ECqMEY5u4-tLn84Lv61_N74QACgYKAZgSARASFQHGX2MiwPQb0wjs9MC4c5KqJO00_BoVAUF8yKo-iURgwIzymWu4S7BjQNAA0076; HSID=Akfbc5PYN9P2V3c7d; SSID=A6dj94qEYtFLyaoyQ; APISID=BKPFhwlGmmdwwwK-/AuiXcEDG4M2gDHbYy; SAPISID=ElfTRU8GxnrF7Apo/AvufrDzlNgmcUylHr; __Secure-1PAPISID=ElfTRU8GxnrF7Apo/AvufrDzlNgmcUylHr; __Secure-3PAPISID=ElfTRU8GxnrF7Apo/AvufrDzlNgmcUylHr; SEARCH_SAMESITE=CgQI15wB; __Secure-ENID=24.SE=ZrjRl9yj4BoEFKOnsUM_myXdXzcaZ1H_EIGA7AA9CH6DXOi_TKBEVXkjqx5lzurZGUZyNS8wLBAxPIDut3WT3-fffSjH2MT7lAz8gw1ZSMmnmjtNrzMLkJaLlUTHV8c6c4IGtmpGLcS3Ge2c3bvQdvLYBzye4Vao4ZfpxheYYH5qXYR2TKKa3j8ajkM-zRSNgrpCw3Gde55qrSWDDpk4qOntcdKKIMXfd6EQhPjOsXYh_W_GPpfdOiJxYiWYEKbeGJqtFMxGzhqKpSfivbcQYB1w3_tlWD5nsAmesOf61xUqUSJC7QwjpXb3K4i5R1W1-kEuPDieDIaZE4Nsjtwj7VDlQEuvsDjAYEJpKT-ZuILwTHw4S4nt5fg; AEC=AZ6Zc-VVtOfvqbh_n35kiuMHJ2jbhCb3hhr1eHm_KQFRe2yX7CwULMMYIfc; OTZ=7847333_34_34__34_; NID=519=F6D3riUC5AN7VNFCEQTmwMGP4QZk36steLkSDW2_cdmPl8BGhPbzORegOgNJHiQJCZCkS4ycmeXO-4cUzR-bmJiAWMamrcTdKmpTQ_d55gL8kFaTSax769gyRC8NUFzl5bmiHvVdAXm7lGPk-wJqDWvKlS2x8ZA-7sHZU0VmNIoyYyZqVAuISo-fgfui6ZpQnmk6CRSSjHUXQlUzvEXOuaM_JVGo7vVGefOkg8jmYLMfy4GKcbHtDGANBnzjB6iZy523X4cGzzC1RxDAOCvigXmPDB4mnCwCqNGhbW9ekMKeTvEVdrK9LcvCCUgfAALQ2ZGwqt0sWo_XuMWb_mNN3JBQDJMNs5S1vKhhsY1R1Bw6BL2EOc9sTu6Pc6k05bEUMHzjK2O8iO1yjgk31M2ZtVCcL1MXWxrenBxwQryLS0VVVXyqtUiqO6_WZgFqXoIGrxeUV_-ToxktZb1zHgILePrLRbRsE72lBXoX9e-BydMpm91J3vIo2Gqp00ase02H1YNago9GGC7C5mcsh2p5kkb1N-HdORVkOZBqkDBcfjj3ONsdGWg9fxh1P1HZy26CR7qyDOa9shkartMfJ7L0ICriObzOh_ln4mIOyQ2KXWhGmH5Uv77OmS12ienDPSLys6E_BRGF2dW3iWcIOKksIhZ8jckya6eiIiZHa-TFsAhQni2d_rWEvY1jfyX70d0yfmtILIq2tskvecXoQVbM9dMML65zgcOsbV3fxrhiDSfLSYkaW9W04TkXHbDH-f0HKoB-Ci1OGZca52Txrpj2qdHvVQ; __Secure-1PSIDTS=sidts-CjEBQT4rX-pEUHgJw6U2xuPjj5PlYYtX-sndvcgJGHw3_sc9fvm7QXSPjOxJipd_zZquEAA; __Secure-3PSIDTS=sidts-CjEBQT4rX-pEUHgJw6U2xuPjj5PlYYtX-sndvcgJGHw3_sc9fvm7QXSPjOxJipd_zZquEAA; SIDCC=AKEyXzWW8y-5uWrM0VcCN0e6nGNgdhaC1LXfUXIQK1ilUNDhJeywBBjETJwRBrdAQM0K8vz15A; __Secure-1PSIDCC=AKEyXzXeRPU_m1The1I2UlWm0gkWWhdpYH_3Fx5YdyD9J1jnI8KS0rmzeKj6UanYAMixx6ri1Q; __Secure-3PSIDCC=AKEyXzUU6eRR-YjSHPSRS0hYbydpATGLurkudC4_7xzcJumljV2SEjTI23EyHhhHJum_WUfH6RU',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://translate.google.com/m',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'sec-ch-ua-full-version': '"131.0.6778.86"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.86", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-browser-channel': 'stable',
    'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
    'x-browser-validation': 'Nbt54E7jcg8lQ4EExJrU2ugNG6o=',
    'x-browser-year': '2024',
    'x-client-data': 'CIq2yQEIo7bJAQiKksoBCKmdygEIn5XLAQiUocsBCPaYzQEIhaDNAQj9pc4BCNWszgEI6rzOAQj9yc4BCMbPzgEIrtDOAQji0M4BCJzSzgEIi9POAQiy084B',
}

para = """
भारत एक अत्यंत प्राचीन और समृद्ध सांस्कृतिक धरोहर से समृद्ध देश है। भारतीय सभ्यता का इतिहास हजारों वर्षों पुराना है और इस दौरान इसने अनेक सामाजिक, सांस्कृतिक और राजनीतिक परिवर्तन देखे हैं। प्राचीन काल में भारत का संबंध विज्ञान, गणित, चिकित्सा और दर्शनशास्त्र से था। भारतीय ऋषि-मुनियों ने वेद, उपनिषद, भगवद गीता और अन्य धार्मिक ग्रंथों के माध्यम से जीवन के हर पहलू पर गहरी सोच दी। यह ग्रंथ न केवल धार्मिक शिक्षा देते हैं, बल्कि यह जीवन के उद्देश्य, सत्य, धर्म, और मोक्ष पर भी विचार करते हैं। भारतीय संस्कृति में आस्था, विश्वास, और नैतिकता का अत्यधिक महत्व है। यहां परंपराएँ, त्यौहार और रीति-रिवाज पीढ़ी दर पीढ़ी चलते आ रहे हैं, जो समाज को जोड़ने का काम करते हैं।
भारतीय समाज में विविधता का अनूठा मिश्रण है। यहाँ विभिन्न जातियाँ, धर्म, बोलियाँ और संस्कृति एक साथ मिलती हैं। हिन्दू, मुस्लिम, सिख, ईसाई, बौद्ध, जैन जैसे धर्मों का यहाँ समावेश है और इन सभी धर्मों के अनुयायी अपने-अपने धर्म की पूजा करते हुए भी एक दूसरे के प्रति सम्मान का भाव रखते हैं। भारतीय समाज का यह सामंजस्य और भाईचारा एक विशेष प्रकार की सामूहिकता का प्रतीक है। यह विविधता न केवल सामाजिक और धार्मिक जीवन में, बल्कि भारतीय भोजन, संगीत, कला और नृत्य में भी प्रकट होती है। भारत के विभिन्न क्षेत्रों में अलग-अलग पारंपरिक भोजन, संगीत शैली, नृत्य रूप और कला रूप देखने को मिलते हैं।
इतिहास में भी भारत ने कई महान साम्राज्यों का उदय और पतन देखा है। मौर्य साम्राज्य, गुप्त साम्राज्य, दिल्ली सल्तनत और मुग़ल साम्राज्य भारतीय इतिहास के महत्वपूर्ण अध्याय हैं। इन साम्राज्यों ने न केवल भारत की राजनीतिक स्थिति को आकार दिया, बल्कि यहाँ की संस्कृति, कला और विज्ञान में भी योगदान दिया। उदाहरण के तौर पर, मौर्य साम्राज्य के समय अशोक ने बौद्ध धर्म को अपनाया और भारत में शांति और अहिंसा का संदेश फैलाया। गुप्त साम्राज्य के समय में भारतीय विज्ञान और गणित में महत्वपूर्ण विकास हुआ। गुप्त काल को भारतीय स्वर्ण युग माना जाता है, क्योंकि इस समय कई महान गणितज्ञ और खगोलज्ञी हुए जिन्होंने भारतीय विज्ञान को नई दिशा दी।
"""

params = {
    'sl': 'auto',
    'tl': 'en',
    'hl': 'en',
    'q': para,
}

response = requests.get('https://translate.google.com/m',
                        params=params,
                        # cookies=cookies,
                        headers=headers
                        )
print(response.status_code)
# print(response.text)
selector = Selector(response.text)

data = selector.xpath('//div[@class="result-container"]//text()').get()
print(data)



