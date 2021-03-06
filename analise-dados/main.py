#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def gera_csv(filename):

    fid = open(filename, "r")
    lines = fid.readlines()
    fid.close()

    epoca = None
    dt = None
    train_acc = None
    test_acc = None

    csv_lines = list()

    for line in lines:
        if line.startswith("Epoch"):
            fields = line.split(" ")
            fields = fields[1].split("/")
            epoca = fields[0]
        elif line.startswith("20000/20000"):
            fields = line.rstrip("\n").split(" - ")

            # Delta t
            dt = fields[1].strip().split(" ")[0][0:-1]

            # Acc de treinamento
            train_acc = fields[3].strip().split(" ")[-1]

            # Acc de teste
            test_acc = fields[5].strip().split(" ")[-1]

            csv_line = "{};{};{};{}\n".format(epoca, dt, train_acc, test_acc)

            csv_lines.append(csv_line)

    csv_filename = filename.split(".")[0] + ".csv"
    csv_file = open(csv_filename, "w")
    csv_file.writelines(csv_lines)
    csv_file.close()

def extrai_campo(filename, campo_idx):
    fid = open(filename, "r")
    lines = fid.readlines()
    fid.close()

    x = list()
    y = list()

    for line in lines:
        fields = line.rstrip("\n").split(";")
        x.append(int(fields[0]))
        y.append(float(fields[campo_idx]))

    return (x, y)

def plota_dt(filename_01,
    filename_02,
    label_01,
    label_02,
    title,
    output_filename):

    (x1, y1) = extrai_campo(filename_01, 1)
    (x2, y2) = extrai_campo(filename_02, 1)

    plt.xlabel(u"Épocas")
    plt.ylabel(u"Tempo (s)")
    plt.title(title)

    plt.plot(x1, y1, linestyle="-", linewidth=1, c='blue', label=label_01)

    plt.plot(x2, y2, linestyle=":", linewidth=1, c='blue', label=label_02)
    #plt.xlim(5, 15)
    #plt.ylim(-5, 105)

    plt.legend(loc=7)

    # plt.show()
    plt.savefig(output_filename, dpi=1000)


def plota_acc(filename_01,
    filename_02,
    filename_03,
    filename_04,
    label_01,
    label_02,
    label_03,
    label_04,
    title,
    output_filename):

    (x1, y1) = extrai_campo(filename_01, 3)
    (x2, y2) = extrai_campo(filename_02, 3)
    (x3, y3) = extrai_campo(filename_03, 3)
    (x4, y4) = extrai_campo(filename_04, 3)

    plt.xlabel(u"Épocas")
    plt.ylabel(u"Acc (%)")
    plt.title(title)

    plt.plot(x1, y1, linestyle="-", linewidth=1, c='blue', label=label_01)
    plt.plot(x2, y2, linestyle=":", linewidth=1, c='blue', label=label_02)
    plt.plot(x3, y3, linestyle="--", linewidth=1, c='blue', label=label_03)
    plt.plot(x4, y4, linestyle="-.", linewidth=1, c='blue', label=label_04)
    #plt.xlim(5, 15)
    #plt.ylim(-5, 105)

    plt.legend(loc=0)

    # plt.show()
    plt.savefig(output_filename, dpi=1000)


def get_maior_acc(filename):

    (_, train_acc_list) = extrai_campo(filename, 2)
    (_, test_acc_list) = extrai_campo(filename, 3)

    maior_train_acc = 0
    maior_test_acc = 0

    for i in range(len(test_acc_list)):
        if test_acc_list[i] > maior_test_acc:
            maior_test_acc = test_acc_list[i]
            maior_train_acc = train_acc_list[i]

    print ("Maior train acc: {} | Maior test acc: {}".format(maior_train_acc, maior_test_acc))


if __name__ == "__main__":

    # gera_csv("arquivos/mnist-lenet-desktop-gpu.txt")

    # plota_dt("arquivos/mnist-lenet-colab-cpu.csv",
    #     "arquivos/mnist-lenet-colab-gpu.csv",
    #     "CPU",
    #     "GPU",
    #     "Dataset: MNIST - Rede: LENET - Colaboratory",
    #     "img/mnist-lenet-colab.png")

    # plota_acc("arquivos/mnist-lenet-desktop-cpu.csv",
    #     "arquivos/mnist-lenet-desktop-gpu.csv",
    #     "arquivos/mnist-lenet-colab-cpu.csv",
    #     "arquivos/mnist-lenet-colab-gpu.csv",
    #     "CPU - Desktop",
    #     "GPU - Desktop",
    #     "CPU - Colaboratory",
    #     "GPU - Colaboratory",
    #     "Dataset: MNIST - Rede: LENET",
    #     "img/acc-mnist-lenet.png")

    get_maior_acc("arquivos/cifar10-cifar10-desktop-cpu.csv")

    print ("Feito.")
