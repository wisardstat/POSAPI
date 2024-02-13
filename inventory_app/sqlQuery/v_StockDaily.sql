
Create view [v_stockDaily] as 
SELECT TOP (1000) 
      -- cast( a.[stock_date] as datetime)  as stock_date
	  a.[stock_date]
      ,a.[wh_id]
	  ,w.[wh_name]
      ,a.[bar_code]
	  ,b.group_id
	  ,b.group_name
	  ,b.brand_id
	  ,b.brand_name
	  ,b.model_id
	  ,b.model_name
	  ,b.pd_id
	  --,replace( b.pd_name,'  ','') as pd_name
	  ,pd_name
	  ,b.color
      ,a.[qty]
      ,a.[cost]
      ,a.[cc_id]
      ,a.[seq]
	  , case when qty=0 then 1 else 0 end as qty_zero 
  FROM [TbStockDaily] a
  left join v_ProductAll b on a.bar_code=b.bar_code
  left join tbwarehouse w on a.wh_id=w.wh_id
  where 1=1 
  and b.bar_code is not null
  --and [stock_date]='2021-09-21'
GO
