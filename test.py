import re

# 示例文本
text = """
2）、 **Lucence Directory**: 是lucene的框架服务发现以及选主 ZenDiscovery: 用来实现节点自动发现，还有Master节点选取，假如Master出现故障，其它的这个节点会自动选举，产生一个新的Master

它是Lucene存储的一个抽象，由此派生了两个类：FSDirectory和RAMDirectory，用于控制索引文件的存储位置。使用FSDirectory类，就是存储到硬盘；使用RAMDirectory类，则是存储到内存
这里是一些文本内容。
![image-20200527104442279](/Users/yida/Typora_Space/Elasticsearch Java API 很全的整理以及架构剖析/images/image-20200527104442279.png)
这里是一些文本内容。
![](/Users/yida/Typora_Space/Elasticsearch Java API 很全的整理以及架构剖析/images/image-20200527104442279.png)
这里是一些文本内容。
一个Directory对象是一份文件的清单。文件可能只在被创建的时候写一次。一旦文件被创建，它将只被读取或者删除。在读取的时候进行写入操作是允许的

3）、**Discovery**
"""

# 使用正则表达式匹配图像链接
pattern = '(!\\[(.*?)\\]\\((.*?)\\))'

# 查找所有匹配项
matches = re.findall(pattern, text)

# 打印结果
for match in matches:
    print(f"all:{match[0]},Alt Text: {match[1]}, Image URL: {match[2]}")
