## 笔记·第一节课

### 一个完整的交易系统
* 市场——买卖什么
* 逻辑——买卖思路
* 头寸规模——买卖多少
* 入市——何时买进
* 止损——何时退出亏损的头寸
* 离市——何时退出赢利的头寸

### 一个典型的双均线策略 初始化
> ```
> 双均线策略，当五日均线位于十日均线上方则买入，反之卖出。
> ```
>
>
> ## 初始化函数，设定要操作的股票，基准等等
> ``` def initialize(context):
>     # 定义一个全局变量，保存要操作的股票
>     # 000002（股票：万科A）
>     g.security = '000002.XSHE'
>     # 设定沪深300作为基准
>     set_benchmark('000300.XSHG')
>     # True为开启动态复权模式，使用真实价格交易
>     set_option('use_real_price', True)
>     # 设定成交量比例
>     set_option('order_volume_ratio', 1)
>     # 股票类交易手续费是： 买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税，每笔交易佣金最低扣5块钱
>     set_order_cost(OrderCost(open_tax=0, close_tax=0.001, \
>				open_commission=0.0003, close_commission=0.0003.\
>			close_today_commission=0, min_commission=5), type='stock')
>     # 运行函数
>     run_daily(trade, 'every_bar')
> def trade(context):
> 	security = g.security
> 	# 设定均线窗口长度
> 	n1 = 5 
> 	n2 = 10
> 	# 获取股票的收盘价
> 	close_data = attribute_history(security, n2+2, '1d', ['close'],df=False)
>	ma_n1 = close_data['close'][-n1:].mean()
>	ma_n2 = close(data['close'][-n2:].mean()
> 	# 取得当前的现金
> 	cash = context.portfolio.cash ```
