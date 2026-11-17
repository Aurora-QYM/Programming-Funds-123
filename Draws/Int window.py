import tkinter as tk
from tkinter import ttk

class BuildingRoomCanvas:
    def __init__(self, parent, building_name, room_list, cell_w=80, cell_h=60, dot_radius=6):
        """
        :param parent: 父窗口
        :param building_name: 楼宇名称
        :param room_list: [(room_no, has_person), ...]
                          has_person=True 有人(红点)，False 无人(绿点)
        :param cell_w: 房间格子宽度
        :param cell_h: 房间格子高度
        :param dot_radius: 状态圆点半径
        """
        self.parent = parent
        self.building_name = building_name
        self.room_list = room_list
        self.cell_w = cell_w
        self.cell_h = cell_h
        self.dot_r = dot_radius

        self.win = tk.Toplevel(parent)
        self.win.title(f"楼宇详情：{building_name}")

        # 画布
        self.canvas = tk.Canvas(self.win, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 提示标签（悬浮显示房间信息）
        self.tip_label = ttk.Label(self.win, text="", foreground="#222")
        self.tip_label.pack(pady=4)

        # 绑定鼠标移动
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Leave>", lambda e: self.tip_label.config(text=""))

        self.room_rect_map = {}  # key:房间号，value:(rect_id, dot_id, bbox)
        self.draw_rooms()

    def draw_rooms(self):
        cols = 4  # 一行放4个房间，可以自己改
        margin_x = 20
        margin_y = 20
        for idx, (room_no, has_person) in enumerate(self.room_list):
            row = idx // cols
            col = idx % cols

            x1 = margin_x + col * self.cell_w
            y1 = margin_y + row * self.cell_h
            x2 = x1 + self.cell_w - 10
            y2 = y1 + self.cell_h - 10

            # 画房间方格
            rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline="#333", width=2)
            # 房间文字（方格中间）
            self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=room_no, font=("SimSun",10))

            # 状态圆点：方格顶端中间
            dot_x = (x1 + x2) / 2
            dot_y = y1
            if has_person:
                color = "#ff3333"
            else:
                color = "#33bb33"
            dot_id = self.canvas.create_oval(
                dot_x - self.dot_r, dot_y - self.dot_r,
                dot_x + self.dot_r, dot_y + self.dot_r,
                fill=color, outline=color
            )
            self.room_rect_map[room_no] = (rect_id, dot_id, (x1,y1,x2,y2))

    def on_mouse_move(self, event):
        mx, my = event.x, event.y
        for room_no, (_, _, (x1,y1,x2,y2)) in self.room_rect_map.items():
            if x1 <= mx <= x2 and y1 <= my <= y2:
                self.tip_label.config(text=f"房间：{room_no}")
                return
        self.tip_label.config(text="")


# ========== 测试入口 ==========
if __name__ == "__main__":
    root = tk.Tk()
    root.title("楼宇管理主程序")
    root.geometry("400x200")

    def open_building():
        # 模拟楼宇房间数据：(房间号, 是否有人)
        rooms_data = [
            ("101", True),
            ("102", False),
            ("103", True),
            ("104", False),
            ("201", False),
            ("202", True),
            ("203", False),
            ("204", True),
        ]
        BuildingRoomCanvas(root, "一号教学楼", rooms_data)

    ttk.Button(root, text="打开楼宇平面图", command=open_building).pack(expand=True)

    root.mainloop()
