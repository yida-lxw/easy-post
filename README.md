# easy-post
微信公众号文章发布工具(后续再考虑CSDN/开源中国/简书等平台)

### 环境要求

Python 3.8+

### 安装项目依赖

+ pip
  > pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
+ conda
  > conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free <br/>
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ <br/>
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ <br/>
  conda config --set show_channel_urls yes <br/>
  (注意:上面4行命令只需执行一次即可)<br/>
  conda install --yes --file requirements.txt <br/>

### 模块说明

+ core  工具类
+ config  系统配置
+ image_extract 图片链接提取
+ image_upload 图片上传
+ image_amend 图片链接修正
+ html_generate HTML生成
+ blog_post 博客发送
+ blog_index 博客索引创建
+ blog_search 博客内容搜索
+ test 单元测试

### 开发成员

+ yida-lxw
+ lijobs
