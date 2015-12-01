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

<p>例如</p>
	[{'new': 1, 'old': 'hello '}, {'new': 3,'old': 'orld'}, {'new': 2, 'old': 'w'}]
<p>我们要去掉list中每个元素（dict）key－new相同的元素（dict）</p>

<p>代码如下</p>

	def _remove_duplicate(self, dict_list):  
	    seen = set()  
	    new_dict_list = []  
	    for dict in dict_list:  
	        t_dict = {'res_model': dict['res_model'], 'res_id': dict['res_id']}  
	        t_tup = tuple(t_dict.items())  
	        if t_tup not in seen:  
	            seen.add(t_tup)  
	            new_dict_list.append(dict)  
	    return new_dict_list

<p>上面的去重规则是保留第一个元素，拓展思维一下，我们可以保留最后一个或者顺序出现的第n个</p>

<p>还可以保留元素（dict）中某个其他key的值特殊的那个</p>

<center>
<a href="#">
    <img src="{{ site.baseurl }}/img/14-09/code1.png" alt="Post Sample Image">
</a>
<span class="caption text-muted">每一行代码的诞生，都是成就</span>
</center>

<p>原文来自 <a href="http://blog.csdn.net/ngforever/">张子楠</a> 的CSDN.</p>