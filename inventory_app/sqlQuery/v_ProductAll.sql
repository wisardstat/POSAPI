

Create view [dbo].[v_ProductAll] AS
SELECT     a.pd_id, u.bar_code
,dbo.zDisPlayPdName(b.brand_name, m.model_name,a.color) as pd_name
,g.cat_id, a.group_id, g.group_name, a.brand_id, b.brand_name, a.model_id, m.model_name, a.color
, a.cc_id, a.img_id, a.cost, 
a.point_buy, a.chk_cancel, a.warranty_mn, g.group_emei, u.unit_id, mu.unit_name, u.ratio, u.price1 AS price, u.price1, u.price2, u.price3
, mu.unit_ratio,flag_show_front
,u.last_cost,print_barcode
,a.price1 as price1_default
,a.price2 as price2_default
,a.price3 as price3_default
FROM  dbo.TbProductM AS a 
	  LEFT OUTER JOIN
      dbo.TbGroup_item AS g ON a.group_id = g.group_id  
      LEFT OUTER JOIN
      dbo.TbBrand AS b ON a.brand_id = b.brand_id  
      LEFT OUTER JOIN
      dbo.tbModel AS m ON a.model_id = m.model_id AND a.group_id = m.group_id 
      AND a.brand_id = m.brand_id  
      LEFT OUTER JOIN
      dbo.tbProduct_unit AS u ON a.pd_id = u.pd_id  
      LEFT OUTER JOIN
      dbo.tbms_unit AS mu ON u.unit_id = mu.unit_id
WHERE     (1 = 1)