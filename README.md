DrCOM客户端于Openwrt
=======

*如果你愿意捐助作者这个穷屌, 支付宝: latyas@live.com*

本补丁默认您掌握了以下技能

* 基本 Linux 命令
* Openwrt opkg软件源操作
* 会上传文件到路由器中

内容
-------------

1. 纯粹的的登录脚本在 */client* 里, 您可以直接将这个目录里的文件覆盖到 */* 目录下,并给予执行权限 <br>
`chmod +x /usr/bin/dog_drcom`

2. 有个基于 Python 的 GUI 在 */gui* 里, 使用时请直接覆盖, 并基于执行权限, 注意本 GUI 不能独立运行<br>

```shell
chmod +x /www/cgi-bin/*
```

访问 http://路由器地址/drcom/ , 默认密码是 123456, 可以登录后修改.

该 GUI 做的比较简略,主要是方便修改.

# 许可证

GPLv2

特别指出禁止任何个人或者公司将 [drcoms](http://github.com/drcoms/) 的代码投入商业使用，由此造成的后果和法律责任均与本人无关。 
