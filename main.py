import numpy as np
from matplotlib import pyplot as plt

camasir_sertligi = [["sert", [0, 20, 40], [1, 1, 0]], ["h.sert", [20, 40, 60], [0, 1, 0]],
                    ["h.yumuşak", [40, 60, 80], [0, 1, 0]], ["yumuşak", [60, 80, 100], [0, 1, 1]]]
camasir_miktari = [["az", [0, 1, 3], [1, 1, 0]], ["normal", [1, 3, 5], [0, 1, 0]], ["çok", [3, 5, 6], [0, 1, 1]]]
devir = [["hassas", [0, 400, 600], [1, 1, 0]], ["hafif", [400, 600, 800], [0, 1, 0]],
         ["normal", [600, 800, 1000], [0, 1, 0]], ["güçlü", [800, 1000, 1200], [0, 1, 1]]]
# Kullanıcıdan alınacak değerler burası. Farklı varyasyonlar için bu iki satırı tek değiştirmemiz yeterli olacaktır.
aranan_sertlik = 65  # 65
aranan_miktar = 4  # 4


# Grafik Çizim Fonksiyonu. Tüm grafikler bu fonksiyon yardımı ile çizilmektedir.
def graph_generator(data, tag_label, show=True, title=""):
    for label, x, y1 in data:
        plt.plot(x, y1, label=label)
    plt.xlabel(tag_label)
    plt.ylabel('Değer')
    if len(title) == 0:
        plt.title(tag_label + " Grafiği")
    else:
        plt.title(title)
    plt.legend()
    plt.grid(True)
    if show:
        plt.show()


# Verilerimize Göre Üyelik Fonksiyonlarını Grafik Çizdiren Fonksiyonu
graph_generator(camasir_sertligi, "Çamaşır Sertliği")
graph_generator(camasir_miktari, "Çamaşır Miktarı")
graph_generator(devir, "Devir")


def laundry_hardness_member(laundry_hardness, search_hardness):
    members = list()
    # Sert
    if laundry_hardness[0][1][0] <= search_hardness < laundry_hardness[0][1][2]:
        if laundry_hardness[0][1][0] <= search_hardness <= laundry_hardness[0][1][1]:
            members.append([laundry_hardness[0][0], 1])
        else:
            members.append([laundry_hardness[0][0], (1 - 0) * ((laundry_hardness[0][1][2] - search_hardness) / (
                    laundry_hardness[0][1][2] - laundry_hardness[0][1][1]))])
    # Hafif Sert
    if laundry_hardness[1][1][0] <= search_hardness < laundry_hardness[1][1][2]:
        if laundry_hardness[1][1][0] <= search_hardness <= laundry_hardness[1][1][1]:
            members.append([laundry_hardness[1][0], 2 - (1 - 0) * ((laundry_hardness[1][1][2] - search_hardness) / (
                    laundry_hardness[1][1][2] - laundry_hardness[1][1][1]))])
        else:
            members.append([laundry_hardness[1][0], 0.5 - (1 - 0) * ((laundry_hardness[1][1][2] - search_hardness) / (
                    laundry_hardness[1][1][2] - laundry_hardness[1][1][1]))])
    # Hafif Yumuşak
    if laundry_hardness[2][1][0] <= search_hardness < laundry_hardness[2][1][2]:
        if laundry_hardness[2][1][0] <= search_hardness <= laundry_hardness[2][1][1]:
            members.append([laundry_hardness[2][0], 2 + (-1 + 0) * ((laundry_hardness[2][1][2] - search_hardness) / (
                    laundry_hardness[2][1][2] - laundry_hardness[2][1][1]))])
        else:
            members.append([laundry_hardness[2][0], (1 - 0) * ((laundry_hardness[2][1][2] - search_hardness) / (
                    laundry_hardness[2][1][2] - laundry_hardness[2][1][1]))])
    # Yumuşak
    if laundry_hardness[3][1][0] <= search_hardness <= laundry_hardness[3][1][2]:
        if laundry_hardness[3][1][0] <= search_hardness <= laundry_hardness[3][1][1]:
            members.append([laundry_hardness[3][0], 2 - (1 - 0) * ((laundry_hardness[3][1][2] - search_hardness) / (
                    laundry_hardness[3][1][2] - laundry_hardness[3][1][1]))])
        else:
            members.append([laundry_hardness[3][0], 1])
    return members


def laundry_amount_members(laundry_amount, search_amount):
    members = list()
    if laundry_amount[0][1][0] <= search_amount < laundry_amount[0][1][2]:
        if laundry_amount[0][1][0] <= search_amount <= laundry_amount[0][1][1]:
            members.append([laundry_amount[0][0], 1])
        else:
            members.append([laundry_amount[0][0], (laundry_amount[0][1][2] - search_amount) / (
                    laundry_amount[0][1][2] - laundry_amount[0][1][1])])
    if search_amount >= laundry_amount[1][1][0] <= search_amount < laundry_amount[1][1][2]:
        if laundry_amount[1][1][0] and search_amount <= laundry_amount[1][1][1]:
            members.append([laundry_amount[1][0], ((search_amount - laundry_amount[1][1][0]) * (
                    laundry_amount[1][2][1] - laundry_amount[1][2][0])) / (
                                    laundry_amount[1][1][1] - laundry_amount[1][1][0])])
        else:
            members.append([laundry_amount[1][0], (laundry_amount[1][1][2] - search_amount) / (
                    laundry_amount[1][1][2] - laundry_amount[1][1][1])])
    if laundry_amount[2][1][0] <= search_amount < laundry_amount[2][1][2]:
        if laundry_amount[2][1][0] <= search_amount <= laundry_amount[2][1][1]:
            members.append([laundry_amount[2][0], ((search_amount - laundry_amount[2][1][0]) * (
                    laundry_amount[2][2][1] - laundry_amount[2][2][0])) / (
                                    laundry_amount[2][1][1] - laundry_amount[2][1][0])])
        else:
            members.append([laundry_amount[2][0], 1])
    return members


result = np.array([[x, y] for x in laundry_hardness_member(camasir_sertligi, aranan_sertlik) for y in
                   laundry_amount_members(camasir_miktari, aranan_miktar)])
rows_to_delete = np.where(result[:, :, 1] == '0.0')[0]
if len(rows_to_delete) > 0:
    result = np.delete(result, rows_to_delete, axis=0)
print(result)  # Verilerimizi numpy array içinde kullanmak üzere result değişkenine aktarıyoruz.


def kural_tabani(data):
    if data[0][0] == "sert":
        if data[1][0] == "az":
            return "normal"
        elif data[1][0] == "normal":
            return "güçlü"
        elif data[1][0] == "çok":
            return "güçlü"
    elif data[0][0] == "h.sert":
        if data[1][0] == "az":
            return "normal"
        elif data[1][0] == "normal":
            return "normal"
        elif data[1][0] == "çok":
            return "güçlü"
    elif data[0][0] == "h.yumuşak":
        if data[1][0] == "az":
            return "hafif"
        elif data[1][0] == "normal":
            return "hafif"
        elif data[1][0] == "çok":
            return "normal"
    elif data[0][0] == "yumuşak":
        if data[1][0] == "az":
            return "hassas"
        elif data[1][0] == "normal":
            return "hassas"
        elif data[1][0] == "çok":
            return "hafif"


# En düşük üye değerini bulalım.
def find_min_value(data):
    return min(data[0][1], data[1][1])


ruleBase = list()
for i in result:
    ruleBase.append([find_min_value(i), kural_tabani(i)])
arr = list()
for y in result:
    arr.append(find_min_value(y))
arr = list(set(arr))


def create_intersection_points(array_value):
    intersection_points = list()
    for value in array_value:
        for level in devir:
            if value[1] == level[0]:
                if float(level[2][0]) <= float(value[0]) <= float(level[2][1]):
                    Xbas = float(level[1][0])
                    Xbit = float(level[1][1])
                    Ybas = float(level[2][0])
                    Ybit = float(level[2][1])
                    Aranan = float(value[0])
                    X = ((Xbit - Xbas) / (Ybit - Ybas)) * (Aranan - Ybit) + Xbit
                    intersection_points.append([X, Aranan])
                if float(level[2][1]) >= float(value[0]) >= float(level[2][2]):
                    Xbas = float(level[1][1])
                    Xbit = float(level[1][2])
                    Ybas = float(level[2][1])
                    Ybit = float(level[2][2])
                    Aranan = float(value[0])
                    X = ((Xbit - Xbas) / (Ybit - Ybas)) * (Aranan - Ybit) + Xbit
                    intersection_points.append([X, Aranan])
    return intersection_points


points = create_intersection_points(ruleBase)


def algorithmMOMandLOM(points_array):
    y = 0.0
    xList = list()
    for point in points_array:
        if point[1] > y:
            xList.append(point[0])

    MOM = max(xList)
    LOM = min(xList)

    print("MOM Algoritmasına Göre :", MOM)
    print("LOM Algoritmasına Göre :", LOM)


algorithmMOMandLOM(points)


def finally_graph_generator(cycle, point_values, y_values):
    size = 120
    color = 'red'
    plt.figure(figsize=(12, 8))
    for x, y in point_values:
        plt.scatter(x, y, c=color, s=size)
    graph_generator(cycle, "Devir", False, title='Çamaşır Makinesi Devir ve Üye Değerleriyle Kesişim Grafiği')
    for y in y_values:
        plt.axhline(y=float(y), color='black', linestyle='--', label=f'y={y}')
        plt.text(x=float(0), y=float(y), s=f'{y}', color='black', fontsize=12)
    if aranan_sertlik == 65 and aranan_miktar == 4 :
        plt.fill_between([400,450,900,1000],[0,0.5,0.5,0],color='skyblue', alpha=0.4)
        plt.fill_between([400,450,750,800],[0,0.25,0.25,0],color='skyblue', alpha=0.4)
    plt.legend()
    plt.show()


finally_graph_generator(devir, points, arr)
