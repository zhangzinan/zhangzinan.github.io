---
layout:     post
title:      "Odoo：对many2many或one2many的操作"
subtitle:   "oe中调用create函数或者write函数时，对many2many或one2many的操作"
tags:		python odoo many2many one2many
date:       2014-01-23 12:00:00
author:     "Nan"
header-img: "img/14-09/post-bg1.jpg"
---

<h2>Odoo：对many2many或one2many的操作</h2>
<blockquote>oe中调用create函数或者write函数时，对many2many或one2many的操作</blockquote>

one2many

    (0, 0,{vals})       根据vals里面的信息新建一条记录，并链接到当前记录
    (1,ID,{vals})       更新id=ID的记录
    (2,ID)              删除id=ID的记录

many2many

    (0,0,{vals})        根据vals里面的信息新建一条记录
    (1,ID,{vals})       更新id=ID的记录
    (2,ID)              删除id=ID的记录
    (3,ID)              删除主从数据的链接关系，但是不删除记录
    (4,ID)              为id=ID的数据添加链接关系
    (5)                 删除所有的从数据的链接关系，就是向所有的从数据调用(3,ID)
    (6,0,[IDs])         用IDs里面的记录替换原来的记录
