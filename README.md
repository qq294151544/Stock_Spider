# 股票信息的抓取 #

### 简单分析 ###


----------
链接：
[http://stockapp.finance.qq.com/mstats/#mod=list&id=sha&module=SS&type=rankash&sort=32&page=1&max=40](http://stockapp.finance.qq.com/mstats/#mod=list&id=sha&module=SS&type=rankash&sort=32&page=1&max=40)
		
	
	腾讯财经里的一个股票信息链接，经过页面分析之后，我们要抓取的信
	
	息都是动态生成的，对抓取造成一定的困扰，所以我们选取selenium
	
	这个插件对浏览器进行页面渲染之后的抓取。

#  #本代码为页面抓取测试代码
