## Các thông tin cơ bản về quy trình làm game và các công cụ sử dụng trong phát triển game

### Phương pháp trong phát triển dự án game
Chúng ta áp dụng mô hình Agile – quy trình Scrum ở mức linh hoạt theo từng giai đoạn và quy mô nhân sự. Tìm hiểu thêm về [Scrum ở đây](guides/agile/agile-scrum.md)

### Các bước trong sản xuất game

| Bước | Thời gian |
| ---- | --------- |
**Planning**: lập kế hoạch | ~10% timeline
**Pre-production**: chuẩn bị | ~30% timeline 
**Production & Testing**: thực hiện (dev game) | ~(30-45)% timeline
**Pre-lauch**: trước khi phát hành | ~4% timeline
**Launch**: phát hành | ~1% timeline
**Post-Production**: hậu phát triển | ~10% timeline

### Các công cụ phục vụ trong sản xuất game

- Công cụ làm việc nhóm: Discord (đang sử dụng), Skype
- Công cụ viết GDD (game design document): Word, Excel, Markdown
- Công cụ quản lý GDD: Github Wiki, Drive
- Công cụ lập trình game: Unity
- Công cụ quản lý dự án: Github, Sourcetree
- Công cụ thiết kế 3D: Maya, Blender, Substance
- Công cụ thiết kế 2D: Photoshop
- Công cụ test game: ...

### Các thuật ngữ trong sản xuất game (đọc lúc rảnh)

Các thuật ngữ được chấp nhận và sử dụng rộng rãi trong ngành công nghiệp game [đọc chi tiết](guides/game-development-terms.md)

## Các quy định trong dự án

Đối với toàn bộ thành viên làm việc và thao tác trên dự án liên quan đến Git và Unity nói chung

### Các file cấu hình sử dụng chung với mọi dự án

- [Editor Config](configs/.editorconfig): cấu hình IDE để mọi thành viên sử dụng chung một codestyle.
- [Git Ignore Config](configs/.gitignore): cấu hình những file không cần tracking với Git cho một project Unity.
- [Git Attribute](configs/.gitattributes): cấu hình chiến lược merge và tracking bằng Git LFS cho một project Unity.  
_**Lưu ý**: để sử dụng trình merge thông minh của Unity thì cần cấu hình Git theo như hướng dẫn ở [Sử dụng Git cho Unity](guides/git/using-git-for-unity.md)_

### Các quy ước

- [Naming Convention][git-convention]: các **quy tắc đặt tên** cho file, folder tự tạo trong quá trình phát triển sản phẩm.
- [Coding Convention][coding-convention]: các **quy tắc đặt tên và chuẩn hoá code** cho các Programmer trong quá trình code.

### Cài đặt và sử dụng Git

- [Cài đặt Git cho Windows](guides/git/install-git-for-windows.md): các bước cài đặt công cụ Git cho máy tính sử dụng hệ điều hành Windows.
- [Sử dụng Git cho Unity](guides/git/using-git-for-unity.md): cách sử dụng Git với Unity nói chung và cách **IceHouseStudio** (amateur) sử dụng Git trong các dự án.
- [Quy trình sử dụng Git và cách giải quyết khi gặp vấn đề][git-rule]: cách sử dụng các thủ tục Git đơn giản trong quá trình phát triển sản phẩm.

[coding-convention]: guides/code/code-convention.md
[git-convention]: guides/git/git-convention.md
[git-rule]: guides/git/git-rules.md
