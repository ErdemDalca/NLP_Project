# GameManager và FSM Pattern

Game Manager là nơi quản lý State của Game, các States của Game được định nghĩa trong Game Design Document.

<img width="303" alt="image" src="https://user-images.githubusercontent.com/1218572/203506015-55132246-bdcb-4c00-bb89-ad51ce12ff36.png">


GameManager triển khai Finite State Machine Pattern:

- Số state là giới hạn - finite. FSM rất phổ biến trong Game Development vì lí do này.
- Chỉ được phép có 1 state trong ở cùng level một thời điểm. Có thể có các SubState. Khi Game chuyển qua một SubState, ParentState của SubState đó tự động OnEntry.
- Khi Enter một State, có thể định nghĩa được OnEntry, OnExit, OnActivate, OnDeActivate. Số lượng Handler Function là không giới hạn.
- Nên triển khai ở các OnEntry/OnExit Function ở nơi quản lý logic đó, ví dụ định nghĩa show homeScreen và shopScreen LobbyUIScene với stateMachine - _Separation of Concern_
- Nên suy nghĩ theo hướng Declarative khi triển khi FSM:
   - Khi Click Shop Button -> Trigger GoShopping -> StateMachine
   - Với State = Shopping - OnEntry ShowShopUI

- Chỉ nên có duy nhất GameManager là Singleton trong dự án, các Singleton khác nên được khai báo bình thường và khởi tạo qua GameManager để đảm bảo thứ tự declare statemachine trước khi activate - pattern IoC

# Triển khai Game Manager trong SDK

Trong SDK đã implement [AbstractGameManager ](https://github.com/rocketsaigon/RocketSgSdk/blob/master/Assets/_SDK/Game/AbstractGameManager.cs)
- Thư viện: https://github.com/dotnet-state-machine/stateless

- 
http://www.webgraphviz.com/

```
digraph {
compound=true;
node [shape=Mrecord]
rankdir="LR"

subgraph "clusterLobby"
	{
	label = "Lobby"
"LobbyHome" [label="LobbyHome"];
"Shopping" [label="Shopping"];
"SelectingMap" [label="SelectingMap"];
}

subgraph "clusterPausing"
	{
	label = "Pausing"
"InGameSettings" [label="InGameSettings"];
"Equipping" [label="Equipping"];
"Rewarding" [label="Rewarding"];
}

subgraph "clusterEnd"
	{
	label = "End"
"Won" [label="Won"];
"Lost" [label="Lost"];
}
"Init" [label="Init"];
"Playing" [label="Playing"];

"Init" -> "Lobby" [style="solid", label="InitToLobby"];
"LobbyHome" -> "Shopping" [style="solid", label="GoShopping"];
"LobbyHome" -> "SelectingMap" [style="solid", label="SelectMap"];
"Lobby" -> "Playing" [style="solid", label="Play"];
"Shopping" -> "LobbyHome" [style="solid", label="BackToLobbyHome"];
"SelectingMap" -> "LobbyHome" [style="solid", label="BackToLobbyHome"];
"Playing" -> "Lobby" [style="solid", label="BackToLobbyHome"];
"Playing" -> "Pausing" [style="solid", label="Pause"];
"Playing" -> "Won" [style="solid", label="Win"];
"Playing" -> "Lost" [style="solid", label="Lose"];
"Pausing" -> "Playing" [style="solid", label="UnPause"];
 init [label="", shape=point];
 init -> "Init"[style = "solid"]
}

```
