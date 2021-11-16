
# Hahow專案

此為應試者曾思源,應徵軟體測試工程師之專案考題Readme檔案.

專案大致分為兩部分：

•針對專案需求設計一個 API 自動化程式.

•針對專案需求設計一個 UI 自動化程式.


## 版本紀錄

- v 1.0.0 - 
    
    建置API自動化程式之介紹文件.
    


## 目錄

- 需安裝之工具
- 文件
- 專案需求＆執行步驟
  
  - API自動化程式
      
      Q1 有多少不同種族的人出現在第六部？

      Demo

      Q2 請依據電影集數去排序電影名字？

      Demo-2

      Q3 請幫我挑出電影裡所有的車輛，馬力超過１０００的

      Demo-3
  - UI自動化程式 （尚未建置）
- API Reference
## 需安裝之工具

本專案是利用Postman和VS(Visual Studio)code-python來執行,因此須先安裝.

```bash
  Postman_9.1.3
  VS(Visual Studio)code_1.62.2
  Python_3.9.4
```
    
## 文件

[API Info](https://swapi.dev/)


## 專案需求＆執行步驟

此部分(共3題)為API自動化程式之建置和使用介紹(詳細API資訊可參考'文件'當中的API資訊or API Reference) ：

### Q1.有多少不同種族的人出現在第六部？
  
  (1)利用Postman request 第六部曲的film API(#get character/species from film),
  並用程式做擷取：
  
    (a)從'show postman console'中獲取該集的人物(characters).
    (b)從'show postman console'中獲取該集的種族(species)).
  
  (2)利用Postman,將該集所有人物的API建立並存進指定collection(#species)中, 並執行'Run collection',
     一次從'show postman console'中獲取人物種族(species).
  
  (3)將species輸入至VS code的程式(#species.py)中.
  
  (4)利用set去重,並可從結果中得知各種族的個數,和總共有幾個種族.




### Demo-1

https://www.loom.com/share/1cd5c26888da4d89bf09a36c6da86b67

### Q2.請依據電影集數去排序電影名字？
  
  (1)利用postman request film(#get episode from film),並用程式做擷取,從'show postman console'中獲取出集數(episode)和對應的電影名稱(title).
  
  (2)將集數(episode)和對應的電影名稱(title)輸入至VS code的程式(#order of episode.py)中.
    
  (3)利用sorted指定集數作為排序依據,並列出結果.
### Demo-2

https://www.loom.com/share/966d0b0cb0374c08bd7224e5484bb88d



### Q3.請幫我挑出電影裡所有的車輛，馬力超過１０００的。

  (1)利用postman request vehicles(#get info of vehicles),並用程式做擷取,從'show postman console'中獲取出機具(name))和對應的馬力(max_atmosphering_speed).
  
  (2)將機具(name)和對應的馬力(max_atmosphering_speed)輸入至VS code的程式(#Vehicles)中.
    
  (3)利用資料分析函示-pandas列出車輛列表,並列出馬力大於1000的車輛.
### Demo-3

https://www.loom.com/share/4ecfca5abbe3480da1671f553fb656b7
## API Reference

僅列出此專案用到之API和相關參數,詳細資料可參考'文件'中的API Info.

#### Get film info

```http
  GET https://swapi.dev/api/films
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `episode_id` | `integer` | The episode number of this film |
| `title` | `string` | The title of this film |
| `species` | `array` | An array of species resource URLs that are in this film. |
| `characters` | `array` | An array of people resource URLs that are in this film.. |
| `vehicles` | `array` | An array of vehicle resource URLs that are in this film. |

#### Get characters info
```http
  GET https://swapi.dev/api/people
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `species` | `array` | An array of species resource URLs that are in this film. |

#### Get Vehicles info
```http
  GET https://swapi.dev/api/vehicles
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | The name of this vehicle. The common name, such as "Sand Crawler" or "Speeder bike". |
| `max_atmosphering_speed` | `string` | The maximum speed of this vehicle in the atmosphere.|






