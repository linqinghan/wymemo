二 使用ConfigAdmin为项目51备忘录扩展功能（50分）
 
 MemoAdmin类；
 1. 添加注册和登陆功能，用户名密码使用dict保存为：users.pkl 。
 2. 添加配置文件，为备忘录数据指定路径,类型和文件名。
    比如zhangsan，则数据文件可以为zhangsan.pkl或zhangsan.db。
 3. 注册时，相应数据文件根据用户名在配置文件保存为新的section。
    比如zhangsan，则有新的section叫 [zhangsan]。
 4. 启动程序先提示登陆，每次登陆时候，先根据配置文件读取用户信息，找不到则提示注册。
5.导出文件功能，将历史数据导出为pdf文件。
6.对每一个函数操作添加日志功能，并在需要时候随时关闭。


MemoAdmin
add, delete, modify, show


users.pkl
[{"user":"u1", "pwd":"p1"}, {"user":"u2", "pwd":"p2"}]

UserAdmin
load()
save()
check_is_register()
check_password()
login
register


ConfAdmin

[zhangsan]
name=zhangsan.pkl
type=pkl



