# GameManager

## GameManager là một StateMachine

Game Manager là nơi quản lý State của Game, các States của Game được định nghĩa trong Game Design Document.

<img width="303" alt="image" src="https://user-images.githubusercontent.com/1218572/203506015-55132246-bdcb-4c00-bb89-ad51ce12ff36.png">


GameManager triển khai Finite State Machine Pattern:

- Số state là giới hạn - finite. FSM rất phổ biến trong Game Development vì lí do này. Các State phổ biến: Playing, Pausing, Init
- Quá trình chuyển từ State này qua State kia được gọi là Transition. Một Transition được xảy ra khi Fire một Trigger
- Có thể define các SubStates cho một State. Transition di chuyển đến SubState sẽ phải chạy qua ParentState nếu khác level.
- Khi Enter một State, có thể định nghĩa được OnEntry, OnExit, OnActivate, OnDeActivate. Số lượng Handler Function là không giới hạn.
- Nên suy nghĩ theo hướng Declarative khi triển khi FSM:
   - Khi Click Shop Button -> Trigger GoShopping -> StateMachine
   - Với State = Shopping - Subscribe - ShowShopUI

## GameManager là một Dependencies Container

- Chỉ nên có duy nhất GameManager là Singleton trong Game,
- Các Instance khác nếu cần dùng toàn App sẽ được khởi tạo qua GameManager và truy cập qua GameManager

# Triển khai Game Manager trong SDK

Trong SDK đã implement [AbstractGameManager ](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Game/AbstractGameManager.cs)
- Thư viện: https://github.com/dotnet-state-machine/stateless

https://plantuml.com/state-diagram

```
@startuml
state Lobby {
  [*] --> LobbyHome
  LobbyHome --> Shopping
  LobbyHome --> Map
}



Init --> Lobby: InitToLobby

Lobby --> Playing : Play
Playing --> Lobby : End
@enduml
```
