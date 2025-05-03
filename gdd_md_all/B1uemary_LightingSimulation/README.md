# BladeSlayer

#### BladeSlayer Documents

通过链接，你可以查看，并且修改文档（求不瞎改）

---
- TDD(Tech Design Document)技术设计文档

https://docs.qq.com/doc/DWXFJWVR2a3NWTVl3

如果您对于Entity和系统架构并不熟悉，请先阅读这份文档。

---

- GDD(Game Design Document)游戏设计文档:

https://docs.qq.com/doc/DWW9FdEZDd1ViQXRV


---
- ADD(Art Design Document)艺术设计文档:

https://docs.qq.com/doc/DWWdLc0Vya3hWZnZI

---

- Concept Design概念设计:

https://docs.qq.com/doc/DWXlKeVRRUkNEWUxh

---



#### Project Introduction
A cyberpunk-style action-playing game with unique rendering effects.


#### Introduction to play


#### Collaborative Instructions

1. ** clone remote repository** `git clone https://github.com/kwh3884858/BladeSlayer`
2. **Enter the warehouse** `cd BladeSlayer` Switch to the repository
3. **View branch** `git branch` If you are sure that you are on the master, there is no problem.
4. **Update the repository** `git pull`
5. **Branch description**, `master` is the **main branch**, `dev` is the **development branch**.
6. **Switch to development branch** `git checkout dev`
7. **Modify bugs, ** **Add new features**
   - `git add <filename>` filename can also use * to indicate all
   - `git commit -m "message"` message format below
   - `git push origin dev` push your own changes
   - `git pull` fetches new commits from the repository (if the push fails, the update first resolves the conflict)
8. **Daily development** `git pull` and then connect 6, continue to iterative development

> The master branch is merged by the administrator to prevent bugs from crashing in later projects. There is no need to roll back directly, and the master is a stable version. Every time dev updates new features and there are no bugs, the administrator merges once.

#### format requirement 

**commit** information inside: <type> : <body> <footer>

Type must have, body and footer optional.

Type:

- feat: new features
- fix: fix bug
- docs: documentation
- style: format (code function logic is unchanged)
- refactor: refactoring
- test: test file
- chore: changes to the aids

The common information is as follows:

`git commit -m "fix: modify a certain bug" `

`git commit -m "feat: add new features"

The footer can be omitted later, if the description is clear enough.

If you mistyped the information yourself

`git commit --amend`

Enter the modified commit message to save

`git push <remote> <branch> -f `
   
---
#### 项目介绍

建筑学和室内装修专业的学生，都要学习如何根据建筑物的室内用途，来设计如何自然采光和灯光补光。在传统的教学过程中，学生只能做一些图纸相关的实验，无法直观有效的体验到实际的光照效果。课题组拟采用Unity3D引擎，实现一套基于Web的用于室内展览馆采光设计实验的虚拟仿真系统。该系统可以允许用户通过浏览器访问，在虚拟实验中选择窗户类型，调整窗户尺寸，布置展台补光灯源位置，选择灯源参数。用户可以实时体验到室内灯光在多种因素影响下的实际效果，同时系统自动计算室内不同采样点的光照强度等物理参数值。系统所需要的静态美工模型已经具备。
本课题的任务是开发一套基于Unity3D的展览馆采光设计虚拟仿真实验系统，让用户可以在调整采光多项参数的同时，体会到光照效果。主要的研究内容：（1）漫游展览馆各个区域；（2）窗户设计，包括窗户的类型选择、窗户的位置选择、窗户尺寸的设定；（3）灯光设计，包括灯的类型选择、位置选择、入射角度选择、光线的色调选择、光线的强度选择；（4）不同参数情况下的室内各区域光照效果实时变化；（5）计算并显示室内各主要区域的光照强度值；（6）自动生成实验报告，内容包括窗户设计截图、关键位置灯光设计截图、展台实际灯光效果截图、光照强度值表格等内容。


#### 格式要求 

**commit** 里面的信息 ：<type> : <body> <footer>

type必须有，body跟footer选填。

type：

- feat：新功能
- fix：修复bug
- docs：文档
- style：格式（代码功能逻辑不变）
- refactor：重构
- test：测试文件
- chore：辅助工具的变动

常见的信息如下：

`git commit -m "fix: 修改某某bug" `

`git commit -m "feat: 增加新功能"` 

后面footer可以省略，描述清楚就行了。

如果自己输错了信息

`git commit --amend` 

输入修改后的commit message 保存

`git push <remote> <branch> -f ` 

