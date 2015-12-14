---
layout:     post
title:      "Postgres：批量插入数据"
subtitle:   "使用存储过程批量插入数据"
tags:		postgres sql
date:       2014-02-20 12:00:00
author:     "Nan"
header-img: "img/14-09/post-bg1.jpg"
---

<h2>Postgres：批量插入数据</h2>
<blockquote>使用存储过程批量插入数据</blockquote>

具体实现如下

    create or replace function creatData2() returns   
    boolean AS  
    $BODY$  
    declare ii integer;  
        begin  
        II:=1;  
        FOR ii IN 1..10000000 LOOP  
        INSERT INTO table_name (res_id) VALUES (ii);  
        end loop;  
        return true;  
        end;  
    $BODY$  
    LANGUAGE plpgsql;  
    select * from creatData2() as tab;

其中 `table_name` 是要插入的表名

插入1千万条数据耗时610s左右，当然字段不多的情况下。