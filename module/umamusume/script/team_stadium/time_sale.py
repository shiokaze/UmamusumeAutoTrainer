from module.umamusume.context import UmamusumeContext
from module.umamusume.asset.point import *


def script_time_sale_main(ctx: UmamusumeContext):
    if not ctx.task.detail.time_sale_bought:
        ctx.task.detail.time_sale_bought.append([])
    buy = ctx.task.detail.time_sale
    bought = ctx.task.detail.time_sale_bought[-1]
    item = {"泥地跑鞋": 9, "长距离跑鞋": 8, "中距离跑鞋": 7, "英里跑鞋": 6, "短距离跑鞋": 5}
    point = {0: TIME_SALE_ITEM_1,
             1: TIME_SALE_ITEM_2,
             2: TIME_SALE_ITEM_3,
             3: TIME_SALE_ITEM_4}
    for i in range(4):
        if i in buy and i not in bought:
            ctx.ctrl.click_by_point(point[i])
            bought.append(i)
            return
    if any(i for i in buy if i not in bought):
        ctx.ctrl.swipe(x1=360, y1=950, x2=360, y2=200, duration=600, name="翻页")
    if 4 in buy and 4 not in bought:
        ctx.ctrl.click_by_point(TIME_SALE_ITEM_6)
        bought.append(4)
        return
    if any(i for i in buy if i not in bought):
        import cv2
        from bot.recog.ocr import ocr_line, find_similar_text
        img = cv2.cvtColor(ctx.ctrl.get_screen(), cv2.COLOR_RGB2GRAY)
        sub_img = img[760:793, 146:257]
        text = ocr_line(sub_img)
        result = find_similar_text(text, item, 0.7)
        if not result: print(text)
        if result:
            if item[result] in buy:
                ctx.ctrl.click_by_point(TIME_SALE_ITEM_5)
                bought.append(item[result])
    ctx.ctrl.click_by_point(TIME_SALE_CLOSE)


def script_shop_main(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TIME_SALE_RETURN)


def script_time_sale_buy_confirm(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TIME_SALE_BUY_CONFIRM)


def script_time_sale_buy_success(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TIME_SALE_BUY_SUCCESS)


def script_time_sale_close_confirm(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TIME_SALE_CLOSE_CONFIRM)
