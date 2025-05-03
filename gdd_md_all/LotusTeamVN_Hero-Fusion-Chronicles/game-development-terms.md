# Các thuật ngữ thường sử dụng trong Game Development

<details>
<summary>Mục lục</summary>

[[_TOC_]]
</details>

## Các thuật ngữ nói chung

### Agent

Một nhân vật hoặc đối tượng trong game sử dụng AI để tương tác với các đối tượng khác trong môi trường của game.

### AI

Trí tuệ nhân tạo; một thực thể trong game có chức năng phụ thuộc vào mã máy tính thay vì đầu vào của con người.  
[NPC](#npc) là các thực thể AI phổ biến.

### Alpha

Một phiên bản game có chứa tất cả các tính năng chính và hầu hết các assets.  
Phiên bản game này thường được lưu hành nội bộ để kiểm tra chất lượng và lỗi.

### Artist

Hoạ sĩ thực hiện tạo asset(background, icon, [texture](#texture), animation, concept, model, ...) cho game qua các phần mềm của bên thứ ba khác.

### Asset

Viết tắt cho bất kỳ thứ gì có trong game - nhân vật, đồ vật, hiệu ứng âm thanh, bản đồ, môi trường, v.v.

### Baking

Phương pháp tiền xử lý được thực hiện trên [asset](#asset) và dữ liệu game để đảm bảo chúng tải và hoạt động tốt trong thời gian thực và không làm chậm quá trình chơi game do yêu cầu nhiều bộ xử lý hoặc dung lượng GPU. 

### Balance

Tạo ra trải nghiệm chơi game ổn định và có thể dự đoán được.  
_Ví dụ, bằng cách đảm bảo vũ khí gây sát thương phù hợp và áo giáp sẽ hấp thụ sát thương đầy đủ, trái ngược với việc cung cấp một vũ khí mạnh hơn đáng kể so với các vũ khí khác, hoặc bằng cách tạo ra các cấp độ quá khó để hoàn thành một cách thích thú._  
Tuy nhiên, game mất cân bằng đôi khi được thực hiện có chủ đích. 

### Beta

Một phiên bản trò chơi có chứa tất cả các tính năng và asset chính.  
Phiên bản trò chơi này không có lỗi lớn và đang trên lộ trình phát hành.  
Bản phát hành Beta đôi khi được cung cấp một bản phát hành early-access cho người chơi để kiểm thử, báo cáo lỗi và phản hồi quan trọng.

### Bug

Bất kỳ vấn đề phát triển nào làm cho người chơi game không thể thưởng thức trải ngiệm game, không ổn định hoặc không thể phát hành trong trạng thái hiện tại.

### Build

Tiếng lóng trong phát triển game cho 1 "phiên bản" của game.

### Cert

Chứng nhận.  
Quá trình theo đó các nhà sản xuất console, quản lý store kiểm tra một game để tương thích với các nền tảng phân phối và phần cứng của họ.  
Điều này không bao gồm [**playtesting**](#playtesting) hoặc [**đảm bảo chất lượng**](#quality-assurance).

### Cinematics/cutscenes

Phân đoạn game không do người chơi điều khiển.  
Chúng thường được sử dụng để thu hút sự chú ý của người chơi đến các điểm quan trọng trong câu chuyện chính.

### Clipping

Quá trình xác định trước các khu vực nhất định trong game trong đó việc hiển thị được thực hiện, giúp tối ưu hóa hiệu suất game trong các khu vực được chọn đó.

### Clipping region

Một khu vực của trò chơi được tối ưu hóa để hiển thị GameObjects và địa hình.

### Code

Ngôn ngữ máy tính được sử dụng để tạo và xác định chức năng trong phần mềm.  
Unity sử dụng C # (C Sharp) cho các đoạn mã trong game.  
Unreal, Cocos sử dụng C++ cho các đoạn mã trong game.  
Flash sử dụng FlashScript, ActionScript cho các đoạn mã trong game.  

### Code release

Phiên bản của một game đã sẵn sàng để được gửi đến các nhà sản xuất console, quản lý store để chứng nhận.  

### Collision

Hành động của hai vật thể tiến vào nhau và chạm/va đập vào nhau trong game.  
_Hành động đơn giản của nhân vật khi đứng trên sàn trong nhà đòi hỏi các thông số va chạm ở cả hai chân của nhân vật và sàn nhà, nếu không, nhân vật đó sẽ chỉ rơi qua sàn._

### Collision detection

Một quá trình xác định thời điểm và nơi một đối tượng sẽ va chạm với một đối tượng khác trong game.  
Điều này thường được thực hiện bằng cách sử dụng một đối tượng được gọi là **[hitbox](#hitbox)**/**collider** để ngăn va chạm hoặc quyết định khu vực nào cần tiếp cận để tạo ra va chạm.

### Content

Mọi thứ tạo nên trò chơi của bạn, chẳng hạn như asset, components, GameObjects và scripts.

### Core-loop

Là một chuỗi hoặc chuỗi hành động được lặp đi lặp lại nhiều lần như là luồng chính mà người chơi của bạn trải nghiệm game.

### Cross-platform

Một game có thể hoạt động hoặc được sử dụng trên các nền tảng khác nhau (iOS, Android, PC, ...).

### Culling

Việc phát hiện, cô lập và từ chối mọi dữ liệu không cần thiết trong thiết kế, hiển thị các thành phần của game.

### Debug

Tìm và loại bỏ [lỗi](#bug) trong một trò chơi.  

### Demo

Phiên bản thể hiện concept của một game, thường được phát hành ra công chúng cho mục đích quảng cáo hoặc nhận phản hồi.

### Dev

Tiếng lóng trong phát triển game cho người phát triển và việc phát triển.

### Edge

Cạnh.  
Kết nối giữa hai [đỉnh](#vertex) của một góc.

### Event

Một hành động trò chơi được hoàn thành thông qua tương tác của người dùng.  
_Khi người chơi nhấn một nút trên UI của game và nhân vật trên màn hình nhảy lên, đây được coi là một sự kiện._

### Feature

Bất kỳ khía cạnh nào của trò chơi tạo ra giá trị và mục đích của nó.  
[Mechanics](#mechanics), cốt truyện và [level design](#level-design) đều được coi là các tính năng.

### Game Design Document

Thường được viết tắt là GDD.  
Là một tài liệu chuyên nghiệp được tạo bởi các nhà phát triển trò chơi để xác định đầy đủ và biện minh cho trò chơi mà họ đã tạo hoặc dự định tạo, thường là một phần của việc thuyết trình ý tưởng của họ cho nhà xuất bản.  
Thường được cập nhật liên tục song song với quá trình phát triển.  
Câu chuyện, gameplay, nhân vật, [level design](#level-design) và các phần không thể thiếu khác của trò chơi được trình bày và mô tả trong tài liệu thiết kế trò chơi.

### Game designer

Một người thiết kế thẩm mỹ và cấu trúc, [Mechanics](#mechanics), [level design](#level-design) của một trò chơi.  
#### LƯU Ý
Các thuật ngữ `Game Designer` và `Graphic Designer` thường được sử dụng thay thế cho nhau, mặc dù hai vai trò kỹ thuật khác nhau.

### Game developer

Một người biến thiết kế game thành một game có thể chơi được thông qua scripts và tạo asset trong engine. 

### Game development

Hành động tạo ra một trò chơi; đôi khi được gọi là gamedev.  
Quá trình phát triển trò chơi thường yêu cầu đầu vào từ một hoặc nhiều [game designer](#game-designer), [artist](#artist), lập trình viên, nhà làm phim hoạt hình, người thử nghiệm, người quản lý dự án, v.v., mặc dù một số trò chơi đã được tạo bởi chỉ một hoặc hai nhà phát triển trò chơi.

### Game engine

Phần mềm cung cấp một bộ công cụ và tính năng cho các nhà phát triển game nhằm xây dựng game của họ một cách chuyên nghiệp và hiệu quả.

### Gameflow

Các game thường được hình thành dưới dạng một loạt các lựa chọn sử dụng phần thưởng để thúc đẩy [player engagement](#player-engagement).  
Quá trình này là `Gameflow`

### Gamefeel

Cảm giác trò chơi là cảm giác vô hình, xúc giác có kinh nghiệm khi tương tác với các trò chơi video.  
Thuật ngữ này đã được phổ biến bởi cuốn sách [Game Feel: Hướng dẫn của nhà thiết kế trò chơi về cảm giác ảo được viết bởi Steve Swink](https://g.co/kgs/VQuXuU).  
Thuật ngữ này không có định nghĩa chính thức, nhưng có nhiều cách được xác định để cải thiện cảm giác trò chơi.

### Gameplay

Gameplay là cách cụ thể mà người chơi tương tác với một trò chơi,  đặc biệt với các trò chơi video.  
Gameplay là mô hình được xác định thông qua các quy tắc trò chơi, kết nối giữa người chơi và trò chơi, thử thách và vượt qua chúng,  cốt truyện và kết nối của người chơi với nó.  

### Gold master

Một phiên bản game đã đáp ứng tất cả các yêu cầu của nhà phát hành và nền tảng, bao gồm tất cả các asset và tính năng và được coi là sẵn sàng để ra mắt.

### Hitbox

Một đối tượng vô hình được tạo xung quanh một GameObject khác xác định khu vực xảy ra va chạm với các đối tượng khác.

### Keyframing

Trong phát triển game, hành động đưa một asset vào một khung hình độc lập và ghi lại thông số đó, được tiếp nối bởi những keyframe khác, cho đến khi có một loạt các khung này để truyền tải hiệu quả animation của asset.

### Level-Design

`[TBD]`
Thiết kế màn chơi cho game, đảm bảo màn chơi bổ trợ cho lối chơi.

### Lightmap

Một hệ thống chiếu sáng được [bake](#baking) sẵn để lưu trữ và sử dụng liên tục trong game mà không phải tính toán ở thời gian thực.

### Localization

Bản địa hóa.  
Dịch và hiển thị một game sang nhiều ngôn ngữ.

### Mechanics

Các chức năng, quy tắc và kết quả thiết yếu tạo ra lối chơi.  
Mechanic là những gì làm cho một trò chơi bổ ích, có tính giải trí và tương tác.
Tất cả các trò chơi đều có mechanic; tuy nhiên, có những lý thuyết khác nhau về tầm quan trọng cuối cùng của chúng đối với game.

### Mesh

Một tập hợp các [đỉnh](#vertex), [cạnh](#edge) và [mặt](#face) đóng vai trò là nền tảng của một mô hình trong game.

### Model

Một 3D asset hoàn chỉnh trong game được tạo bằng cách thêm [texture](#texture) và các tính năng khác vào [mesh](#mesh).

### Parallax

Một kỹ thuật được sử dụng trong phát triển game 2D trong đó hình ảnh nền di chuyển ở tốc độ khác so với các đối tượng ở tiền cảnh trong quá trình di chuyển của người chơi/cảnh, tạo độ sâu và tỷ lệ.  
Hiện nay kỹ thuật này còn được sử dụng để làm giả nội thất bên trong cửa sổ.

### Physics

Sử dụng các định luật vật lý trong đời thực được đơn giản hoá trong các game để làm cho các chuyển động và hành vi môi trường trở nên thực tế hơn.

### Playtesting

Chơi qua từng bản [build](#build) mới của game để tìm [bug](#bug), đảm bảo luồng game và tìm kiếm những ý tưởng, sáng kiến để cải thiện, tăng chất lượng game.

### Player Engagement

Đề cập đến cam kết của người chơi đối với các hoạt động chơi trò chơi.  
Người chơi tham gia sâu sắc hoàn toàn tập trung vào các hoạt động chơi game và không nhận thức được những điều đang diễn ra xung quanh.  
[Gameflow](#gameflow) là khái niệm trung tâm trong nhiều nghiên cứu liên quan đến player engagement với game.

### Plugin

Trình cắm.  
Các phần mềm hoặc thư viện được phát triển sẵn để mở rộng hoặc sử dụng trực tiếp bằng cách thêm vào code base của dự án.

### Polygon

Đa giác.  
Một chuỗi các [đỉnh](#vertex), [cạnh](#edge) tạo thành một đối tượng ba chiều (3D).

### Project

dự án, chỉ quá trình phát triển 1 game từ lên ý tưởng đến khi ngừng thực hiện update.

### Prop

Đạo cụ.  
Các đối tượng tĩnh để tương tác trong một trò chơi.

### Prototype

Bản build tạm thời trong 1 giai đoạn nhất định trong quá trình phát triển nhằm kiểm tra hay giới thiệu một hay nhiều tính năng cho game.

### Prototyping

Tạo các phiên bản [prototype](#prototype) khác nhau của game để khám phá các [mechanics](#mechanics) và tính năng khác nhau để quyết định phiên bản nào sẽ tốt nhất cho [Gold master](#gold-master).

### Quality-Assurance

Thường gọi tắt là QA.  
Thử nghiệm một game về chất lượng tổng thể của nó, thường bao gồm việc tìm và định nghĩa các [bug](#bug).

### Ray tracing

Một kỹ thuật tính toán ánh sáng mô phỏng sự tương tác của ánh sáng với các vật thể trong trò chơi theo cách cực kỳ chân thực.

### Render

Hành động liên tục tạo và hiển thị hình ảnh 2D hoặc 3D thông qua xử lý máy tính để hiển lên màn hình.  
Game thông thường render 60 hình trong 1 giây.

### Scripting

Một cách gọi khác cho việc viết script hoặc lập trình hành vi cho đối tượng, hệ thống trong game.

### Shader

Các chương trình nhỏ chạy trên GPU trong quy trình phát triển game, thường được sử dụng để kiểm soát hiệu ứng ánh sáng và bóng tối trong [render](#render).

### Skeletal animation

Một loại chuyển động được tính toán dựa vào một tập hợp các bộ xương trong một [mesh](#mesh), cho phép [mesh](#mesh) tĩnh được tính toán dựa theo khớp nối và tạo ra cho khung hình trong chuyển động.

### Sprite

Hình ảnh Bitmap, thường được sử dụng làm GameObject 2D. Trong 3D, sprite thường là [texture](#texture).

### Terrain

Bất cứ cái gì tạo ra môi trường trong một game.

### Texture

Một hình ảnh được bao xung quanh GameObjects, _thường là 3D_, chẳng hạn như da trên một nhân vật. 

### Texture mapping

Quá trình xác định và bao [texture](#texture) cho GameObjects.

### Tile

Một hình ảnh được sử dụng để tạo các hình ảnh khác lớn hơn (như đất nền) bằng cách xếp cạnh nhau trong 1 lưới trong trò chơi 2D.

### Tilemap

Một hệ thống lưu trữ và xử lý các [tile](#tile) asset để tạo các level 2D.

### T-Pose

Tư thế mặc định nhân vật đứng với hai tay vươn ra theo chiều ngang, thường được dùng làm dáng default (không animation) của nhân vật.

### UI/GUI

Giao diện người dùng/giao diện người dùng đồ họa.  
Menu, inventory và các hệ thống tương tác không phải game khác trên màn hình.

### UX

Trải nghiệm người dùng.  
Đảm bảo rằng thiết kế và tương tác với game là dễ chịu và thân thiện với người dùng.

### Vector graphic

Một loại hình ảnh đồ họa sử dụng các điểm hai chiều để kết nối các đường và đường cong, cho phép nó được thu nhỏ, phóng to và tùy chỉnh.

### Vertex

Một điểm trong không gian 2D hoặc 3D. Nối hai điểm lại với nhau tạo thành một [cạnh](#edge).

### Vertical slice

Một bản [build](#build) với tiến trình được xác định sẵn để thể hiện lối chơi và tính năng của game, thường được trao cho các nhà đầu tư hoặc nhà xuất bản để có cơ hội nhận được tài trợ và quan hệ đối tác.

### Visual scripting

Phương pháp tổ chức và tạo script trực quan, nơi các nhà phát triển có thể tạo và kết nối các nút đồ họa để tổ chức các GameObject, event, program khác nhau, v.v. mà không cần phải động vào phần mềm lập trình.

## Các thuật ngữ riêng cho Unity

### Component

Một thành phần được gắn vào GameObject để thay đổi chức năng của nó.

### Editor

Cửa sổ điều khiển chứa tất cả các chức năng của Unity được cung cấp cho người dùng.

### Entity

Thực thể.  
Một GameObject nhận các thành phần cho chức năng.

### GameObject

Nhân vật, [đạo cụ](#prop) và cảnh vật trong Unity.

### Hierarchy window

Cửa sổ phân cấp.  
Một cửa sổ trong Unity Editor hiển thị tất cả các GameObject hiện đang được sử dụng trong Scene.

### Inspector window

Cửa sổ thanh tra.  
Cửa sổ trong đó bạn có thể xem và chỉnh sửa các thuộc tính và cấu hình của hầu hết mọi thứ xuất hiện trong Unity Editor, bao gồm asset, GameObjects và chính Unity Editor.

### Instance

Một phiên bản của GameObject được tạo từ prefab và được sửa đổi để mang các đặc điểm và hành vi cụ thể giúp phân biệt với prefab ban đầu. 

### Instantiation

Khởi tạo.  
Việc tạo ra một [Instance](#instance).

### Materials

Vật liệu.  
Các đối tượng soạn thảo lưu trữ các thuộc tính của các bề mặt trong Unity, chẳng hạn như [texture](#texture), đổ bóng và color.

### Orthographic camera

Chế độ xem camera làm cho các vật thể xuất hiện cố định kích thước trên màn hình, bất kể khoảng cách thực tế của chúng với nhau hoặc vị trí tương đối của chúng. Điều này thường được sử dụng cho các trò chơi 2D theo phong cách retro, vì nó có thể làm cho GameObject trông phẳng hoặc các trò chơi 2.5D (trò chơi 2D sử dụng các yếu tố 3D), đặc biệt vì chúng cho phép sử dụng độ sâu và định nghĩa 3D trong khi vẫn duy trì hình dạng 2D.

### Package

Một gói bất kỳ asset, Shader, [Texture](#texture), trình cắm, biểu tượng và tập lệnh nâng cao cho các phần khác nhau trong dự án.

### Package Manager

Một tính năng trong Unity Editor cho phép bạn tải xuống và cài đặt các [Package](#package) cho Unity Editor.

### Perspective camera

Chế độ xem camera chiếu các đối tượng theo vị trí và khoảng cách thực tế của chúng trên màn hình, mang đến cho người xem cảm giác về vị trí và độ sâu trong thế giới thực của họ. Điều này thường được sử dụng cho các game hoàn toàn 3D. 

### Prefab

Một phiên bản GameObject được lưu lại, tùy chỉnh sẵn.  
Thường được sử dụng lặp đi lặp lại.

### ProBuilder

Một tính năng Unity cho phép các nhà thiết kế xây dựng, chỉnh sửa và tùy chỉnh kết cấu hình học 3D cho [level-design](#level-design).

### Project window

Cửa sổ dự án.  
Trình quản lý & tìm file hiệu quả trong Unity.  
Đây là nơi bạn sẽ có thể đi sâu vào các thư mục Scene, Assets, Prefab và các thư mục khác.

### Rigidbody

Một thành phần trong Unity cho GameObject khả năng phản ứng với môi trường của nó thông qua [vật lý](#physics), ví dụ, cho GameObject có trọng lượng.

### Runtime

Đầu ra được [render](#render), dành riêng cho nền tảng _(ví dụ: cho iOS, Android, Oculus hoặc PlayStation 4)_ từ một dự án Unity. 

### Scene

Khung cảnh.  
Toàn bộ khu vực có thể chỉnh sửa trong đó một game có thể được xây dựng. Môi trường, [đạo cụ](#prop), chướng ngại vật, NPC, chức năng menu và nhiều thứ khác có thể là một phần của mỗi Scene trong Unity. 

### Shader Graph

Một công cụ chỉnh sửa Shader trực quan trong Unity cho phép các nhà phát triển tạo Shader mà không phải viết code.

### Timeline

Một tính năng trong Unity để tạo nội dung điện ảnh, đoạn cắt cảnh, chuỗi âm thanh và hiệu ứng particles phức tạp.

### UIElements

Một công cụ chỉnh sửa UI thống nhất trong Unity. Kể từ Unity 2020.1, đây được gọi là Bộ công cụ UI.

### Visual Effect Graph

Trình chỉnh sửa hiệu ứng hình ảnh trực quan cho phép nhà phát triển thiết kế hiệu ứng hình ảnh mà Unity chạy trực tiếp trên GPU.
