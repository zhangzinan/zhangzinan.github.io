---
layout:     post
title:      "python进阶：将table转化为excel"
subtitle:   "去掉list中元素为字典的且字典key相同的list元素"
date:       2014-12-02 12:00:00
author:     "张子楠"
header-img: "img/14-09/post-bg1.jpg"
---

<h2>python进阶：将table转化为excel</h2>
<blockquote>使用xlsxwriter库，将table转为excel</blockquote>

函数使用库引入

    from lxml import etree
    import xlsxwriter
    import StringIO

函数实现如下

    def get_xlsx(wkb_name, html, *args, **kwargs):
        """
            生成xlsx数据
        """
        page = etree.HTML(html.lower().decode('utf-8'))
        table = page.xpath('//table/tr')
        fp = StringIO.StringIO()
        workbook = xlsxwriter.Workbook(fp, {'in_memory': True})
        worksheet = workbook.add_worksheet(wkb_name)

        # excel矩阵表
        excel_map = {}

        # 生成数据
        row = 0
        for tr in table:
            col = 0
            for td in tr.xpath('td'):
                cell_rs = row
                cell_re = row
                cell_cs = col
                cell_ce = col

                # merge table
                colspan, rowspan = 0, 0
                attrib = td.attrib
                if 'colspan' in attrib.keys():
                    colspan = int(attrib['colspan'])
                    cell_ce += colspan - 1
                if 'rowspan' in attrib.keys():
                    rowspan = int(attrib['rowspan'])
                    cell_re += rowspan - 1

                # 更新excel矩阵表
                if row not in excel_map.keys():
                    excel_map[row] = []
                for x in xrange(cell_rs, cell_re+1):
                    if x not in excel_map.keys():
                        excel_map[x] = []
                    if x != row:
                        excel_map[x].extend([x for x in xrange(cell_cs, cell_ce+1)])

                # 判断是否在矩阵表中，若是，则往后顺延
                while cell_cs in excel_map[row]:
                    cell_cs += 1
                    cell_ce += 1
                    continue

                # 写入数据
                style = {
                    'align': 'center',
                    'valign': 'vcenter',
                }
                if cell_rs == cell_re and cell_cs == cell_ce:
                    worksheet.write(cell_rs, cell_cs, td.text, workbook.add_format(style))
                else:
                    worksheet.merge_range(cell_rs, cell_cs, cell_re, cell_ce, td.text, workbook.add_format(style))

                col = cell_ce + 1
            row += 1
        # 关闭
        workbook.close()
        # 返回数据
        return fp

函数接收参数：
<blockquote>html:接收的table字符串</blockquote>
<blockquote>wkb_name:生成的excel文件名(可选)</blockquote>

函数返回值 `fp` 是文件流对象

待拓展功能：可以将table中的部分样式应用到生成的excel中

<p>原文来自 <a href="http://blog.csdn.net/ngforever/">张子楠</a> 的CSDN.</p>
