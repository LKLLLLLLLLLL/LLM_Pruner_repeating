
# 此仓库使用的一些注意事项
1. 此仓库由git管理，所有更改请一定要`git commit`。  

2. 每次进行修改时，请先`fork`分支，当确定修改完成且确保成功运行后，再`merge`回主线。  

3. 如果对于git不熟悉，可以参见我在群里发布的笔记。  

4. 尽量不要过多的提交`git commit`，确保一次`commit`对应一个功能，这样可以确保文件树的清晰。  

5. 每次提交请详细写`message`，说明代码修改内容。

6. 每次下线时，请执行`git push`，确保代码同步到github仓库。

7. 如果有其他约定的事项，请更新此`README.md`。

# auto-dl使用技巧
1. 官方教程非常全面，大部分的问题里面都有解答，包括但不限于：SSH连接、资源加速、vscode配置等。[auto-dl官方文档](https://www.autodl.com/docs)  

2. 资源加速：auto-dl官方提供了内置服务。 
加速主要涵盖了：
+ github.com
+ githubusercontent.com
+ githubassets.com
+ huggingface.co
```shell
source /etc/network_turbo # 开启加速服务
unset http_proxy && unset https_proxy # 取消加速服务
```
注：如果不需要访问上述网站，请关闭加速，否则会影响正常的网络使用。    
*详见[学术资源加速](https://www.autodl.com/docs/network_turbo/)*

3. auto-dl主机一共提供两种硬盘，分别位于`/`和`/root/autodl-tmp`。前者为系统盘，速度较慢；后者为数据盘，且官方确保使SSD，速度较快。因此，请将所有的工程文件（包括从此github仓库克隆的文件）放在`/root/autodl-tmp`下。