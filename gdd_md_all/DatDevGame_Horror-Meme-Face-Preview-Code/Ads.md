# Implement Ads

Đây là quá trình sau khi bạn đã Import các package từ [CreateProject](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Docs/CreateProject.md)

Đọc phần này để hiểu rõ luồng hoạt động và cách implement các loại Ads vào game.
Tìm hiểu: [Ads Implement ](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Docs/ImplementAds.md)

# Ads and Analytics

**NOTE:** QUY TRÌNH NÀY RẤT QUAN TRỌNG VÌ NÓ LIÊN QUAN ĐẾN TIỀN, PHẢI ĐẢM BẢO CÓ DOUBLE CHECK (2 NGƯỜI KHÁC NHAU) KHI RELEASE.

## Quy trình

### Requirements
Game Design Document sẽ cung cấp các vị trí đặt ads

<img width="300" alt="image" src="https://user-images.githubusercontent.com/1218572/201575588-dadd9542-5096-4e48-a5a5-0e91b79eb4de.png">

### INPUT từ Marketing Team:
- Google Sheet các Config KEYS để gắn Ads. Ví dụ:
 <img width="300" alt="image" src="https://user-images.githubusercontent.com/1218572/192181425-5f07251d-b064-43ca-92c6-48ba57719472.png">
 
- File google-services.json để thiết lập connect tới Firebase, đây là file export từ Firebase Console:
<img width="300" alt="image" src="https://user-images.githubusercontent.com/1218572/194008791-e24bb67b-638f-4c7d-b17d-e61086f5ada4.png">

- Danh sách các Events cần Log:

<img width="300" alt="image" src="https://user-images.githubusercontent.com/1218572/192414300-0cc705d9-31c7-407f-af62-3b0519a80bb7.png">

### Setup CheckList
 * [ ] Đảm bảo thư mục **Ads** và **Analytics** và file _ApplicationStart.cs_ trong SDK và đã init Firebase và AppsFlyer Service
 * [ ] Đảm bảo [AdsManager](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Ads/AdsClient/AdsManager.cs) đã được load trong [GameLoader](https://github.com/rocketsaigon/RocketSgSdk/blob/148412c31ba4f15e111839ea3c14d4f7f95204d2/Assets/_SDK/Game/GameLoader.cs#L19)
 * [ ] Thiết lập Package Name: ví dụ _com.bucket.crash.rsg_
 * [ ] Copy keys vào [Ads Config](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Ads/AdsConfig.cs)
 * [ ] Copy google-services.json và ReImport để đảm bảo file đã được add vào build.
 * [ ] Enable các Ads Networks và Enable MAX Ad Review + AppLoving SDK Key
 * [ ] Tất cả các code đã có trong SDK, chỉ cần viết thêm các đoạn code để gọi Interstitial, đặt Banner
 * [ ] Chỉ thưởng khi người chơi xem hết Rewarded Video
 
```
//EXAMPLE
AdsManager.Instance.AdsClient.ShowRewardedVideo(0, "TestExample", (result =>
		{
			if (result == ShowResult.Finished)  //TODO: Get Reward Items here.
      
		}));
```

* [ ] AppOpenAd sẽ hiển thị khi người chơi mở App và không hiển thị khi người chơi xem quảng cáo RV, Inter xong và quay lại Game


### Tài liệu tham khảo

 * [ ] Đọc các tài liệu tham khảo từ HyperCat [Link 1](https://hypercatstudio.notion.site/Quy-tr-nh-double-check-build-aab-6291703a8a0c4648a05f47650da82428)
 * [ ] Đọc hướng dẫn của MKT về AOA [Link](https://docs.google.com/document/d/1B4tLaKfOcGbT3F0Csfg9rZwYChznco3XKoUoG2oRClY/edit)


![image](https://user-images.githubusercontent.com/1218572/192258992-26a87855-5b79-414b-b017-62d5e9fce28f.png)
 * [ ] Log các [Analytics Event](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Analytics/AnalyticsEvent.cs#L6) tương ứng trong game để log trên Firebase và AppsFlyer

### Release - thử nghiệm khép kín trên Google Play trước
<img src="https://user-images.githubusercontent.com/1218572/194201521-b109cef9-6df2-4373-a77b-bf9832dd2d25.png" alt="drawing" width=200/>
- Sau khi đưa file aab lên đây, có thể check ngay lập tức với Firebase và Ads Intergration

### Test Ads Device
Để loại trừ tình huống Ads Network không trả về Inter nên ads không show -> add device vào test mode theo hướng dẫn này:
https://dash.applovin.com/documentation/mediation/max/get-started-with-max#test-mode


### Google Policy
```
Từ 30/9, toàn bộ interstitals ads xuất hiện trong 1 trong 3 trường hợp sau đây sẽ bị cấm:
1. Xuất hiện đột ngột giữa màn chơi (ví dụ như các dòng Tycoon không chia level và chỉ có capping time hoặc show ở check point)
2. Xuất hiện ở đầu level (ví dụ như FNF show đầu level)
3. Xuất hiện đúng vị trí nhưng không thể tắt sau 15s 
```

## Giải thích Sequence Diagram

https://sequencediagram.org/

```
title Ads and Analytics

participant ApplicationStart
participant Game

participant MaxAdsClient

participant "AppLoving Max(Mediation-Platform)" as AppLoving MAX

participant Firebase

participant AppsFlyer

ApplicationStart -> ApplicationStart:Init Firebase, AppsFlyer Và AdsManager
ApplicationStart -> Firebase:Lấy Frequency CappingTime trong RemoteConfig

ApplicationStart -> MaxAdsClient:Setup Client với AdsConfig
MaxAdsClient -> AppLoving MAX: Init Banner, Inter, RV, AOA => Load AOA
AppLoving MAX -> AppLoving MAX: Load Inter, RV

ApplicationStart -> MaxAdsClient:Show AOA
MaxAdsClient -> AppLoving MAX: Show AOA

Game -> MaxAdsClient: Show Banner ở Bottom khi Game Start

MaxAdsClient -> AppLoving MAX: Show Banner

note over Game:Dựa theo Google Policy, Frequency Capping, Game Rules

Game -> MaxAdsClient:Show Inter khi có thể (check CappingTime)
MaxAdsClient -> AppLoving MAX: Show Inter
MaxAdsClient ->Firebase:Log Show Inter
MaxAdsClient -> AppsFlyer:Log Show Inter

Game -> MaxAdsClient: Show RV khi player muốn reward
MaxAdsClient -> AppLoving MAX: Show RV
MaxAdsClient ->Firebase:Log Show RV
MaxAdsClient -> AppsFlyer:Log Show RV

 AppLoving MAX -> MaxAdsClient: OnRewarded
MaxAdsClient -> Game: OnRewarded

Game->Game: Reward if Result == finish



```




