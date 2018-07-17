def init(context):
    context.stock = "000001.SZ"
    context.buy = True
    logger.info("init universe for %s" % context.stock)
    # 加入池
    set_universe([context.stock])
    context.set_benchmark = '000001.SZ'
 
# 日或分钟或实时数据更新，将会调用这个方法
def handle_data(context, data_dict):
    price30 = get_history(30, '1d', 'close')[context.stock]
    price5 = get_history(5, '1d', 'close')[context.stock]
    ma5 = price.mean()
    ma30 = price30.mean()
    if ma5 < ma30:
        order_target_percent(context.stock, 0)
    else:
        order_target_percent(context.stock, 1)
