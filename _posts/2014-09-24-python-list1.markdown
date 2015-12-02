---
layout:     post
title:      "python进阶：list如何去重"
subtitle:   "去掉list中元素为字典的且字典key相同的list元素"
date:       2014-09-24 12:00:00
author:     "张子楠"
header-img: "img/14-09/post-bg1.jpg"
---

<h2>python进阶：list如何去重</h2>
<blockquote>去掉list中元素为字典的且字典key相同的list元素</blockquote>

<p>python内置set函数可以实现list的简单去重，它接收一个类型为list的可选参数，返回一个包含list去重后的结果集的set对象，这个对象拥有与传统list相同的内部方法，使它能够实现和list几乎相同的使用效果</p>

	s = set()

对它的部分操作

	len(s)
	x in s
	s.add(x)
	s.pop()

例如

	list1 = [1, 2, 3, 1]
	s = set(list1)
	print s

结果是

	set([1, 2, 3])

python内置的set函数只能满足我们一些简单的需求，对于一维list来说
但是对于多维list，或者list元素特殊的结构的去重，就需要我们去写函数来实现

例如

	dict_list ＝ [{'new': 1, 'old': 'hello'}, {'new': 2, 'old': 'world'}, {'new': 2, 'old': 'zzn'}]

我们要去掉list中每个元素 `dict` 部分 `key` 相同的元素`dict`

代码如下

	def _remove_duplicate(dict_list, keys):
	    seen = set()
	    new_dict_list = []
	    for dic in dict_list:
	        t_dict = {k: dic[k] for k in keys}
	        t_tup = tuple(t_dict.items())
	        if t_tup not in seen:
	            seen.add(t_tup)
	            new_dict_list.append(dict)

	    return new_dict_list

函数接收两个参数: `dict_list` `keys`

`dict_list` 是一个字典列表，即以字典作为元素的list，
`keys` 是字典中的key列表，作为去重字典的依据。

我们调用这个函数，看一下它的结果

	keys = ['new']
	print _remove_duplicate(dict_list, keys)

结果

	[{'new': 1, 'old': 'hello'}, {'new': 2, 'old': 'world'}]

上面的去重规则是按照list顺序保留遇到的第一个元素，拓展思维一下，
我们可以保留最后一个或者顺序出现的第n个


<center>
<a href="#">
    <img src="{{ site.baseurl }}/img/14-09/code1.png" alt="Post Sample Image">
</a>
<span class="caption text-muted">每一行代码的诞生，都是成就</span>
</center>

<p>原文来自 <a href="http://blog.csdn.net/ngforever/">张子楠</a> 的CSDN.</p>
