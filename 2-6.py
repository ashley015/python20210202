import turtle                   # 匯入小烏龜模組

screen = turtle.Screen()        # 產生一個螢幕         # 設定螢幕寬高
screen.bgcolor('black')    # 設定螢幕背景

Turtle = turtle.Turtle()      # 產生一個小烏龜物件
Turtle.color('white')          # 設定小烏龜顏色
Turtle.shape('turtle')        # 設定小烏龜形狀

Turtle.penup()                # 提筆
for step in range(0, 100, 5):    # 迴圈：從 5 開始，每次跳 2 步，直到 60
    Turtle.stamp()            # 蓋章
    Turtle.forward(step)      # 向前 step 步
    Turtle.right(24)          # 右轉 24 度

screen.exitonclick()        
