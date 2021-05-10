
#                      FINAL IMPORTANTE---------------------------------TESTER da interface

import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
import re



while (1):
    print('\n')
    cor=input("Inserir cor a aplicar: \n")
    img = cv2.imread("lego-rotXX-8a.jpg")
    img = cv2.resize(img, (900,600))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(cor)


    if cor=='amarelo':
        with open(r'C:\Users\Samuel\Desktop\Interface\YellowMask.txt') as f:
            contentsYellow = f.read()
            f.close()

        xYellow = contentsYellow.split()
        str(xYellow)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        print('Low Yellow Range => [' + xYellow[0] + ', ' + xYellow[1] + ', ' + xYellow[2] + ']')
        print('High Yellow Range => [' + xYellow[3] + ', ' + xYellow[4] + ', ' + xYellow[5] + ']')
        LowerRegionYellow = np.array([xYellow[0], xYellow[1], xYellow[2]], np.uint8)
        upperRegionYellow = np.array([xYellow[3], xYellow[4], xYellow[5]], np.uint8)
        ObjectYellow = cv2.inRange(hsv, LowerRegionYellow, upperRegionYellow)
        ObjectYellow = cv2.resize(ObjectYellow, (900, 600))
        cv2.imshow("Masking", ObjectYellow)  # em vez de object, res_red
        edgesYellow = cv2.Canny(ObjectYellow, 100, 200)
        cv2.imshow("Edges", edgesYellow)
        contoursYellow, hierarchyYellow = cv2.findContours(edgesYellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of yellow pieces= " + str(len(contoursYellow)))

        # cv2.putText(hsv, "Yellow ", (-1, 3), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
        #x, y, w, h = cv2.boundingRect(contoursYellow)
        for pic, contour in enumerate(contoursYellow):
          area = cv2.contourArea(contour)
          if(area>2):
            x,y,w,h=cv2.boundingRect(contour)
            cv2.drawContours(img, contoursYellow, -1, (0, 255, 0), 5)
            img = cv2.putText(img, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

            cv2.imshow('Contours', img)

        #imagem = cv2.putText(cont, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 5.0, (0, 0, 255), 4, cv2.LINE_AA)
        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\yellowMaskNumber.txt', "w")
        f.writelines("Number of Yellow Pieces = " + str(len(contoursYellow)))
        f.close()

    #RED
    elif cor=='vermelho':
        with open(r'C:\Users\Samuel\Desktop\Interface\RedMask.txt') as f:
            contentsRed = f.read()
            f.close()

        xRed = contentsRed.split()
        str(xRed)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        print('Low Red Range => [' + xRed[0] + ', ' + xRed[1] + ', ' + xRed[2] + ']')
        print('High Red Range => [' + xRed[3] + ', ' + xRed[4] + ', ' + xRed[5] + ']')
        LowerRegionRed = np.array([xRed[0], xRed[1], xRed[2]], np.uint8)
        upperRegionRed = np.array([xRed[3], xRed[4], xRed[5]], np.uint8)
        ObjectRed = cv2.inRange(hsv, LowerRegionRed, upperRegionRed)
        ObjectRed = cv2.resize(ObjectRed, (900, 600))
        cv2.imshow("Masking", ObjectRed)  # em vez de object, res_red
        edgesRed = cv2.Canny(ObjectRed, 100, 200)
        cv2.imshow("Edges", edgesRed)

        contoursRed, hierarchyRed = cv2.findContours(edgesRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of red pieces= " + str(len(contoursRed)))

        for pic, contour in enumerate(contoursRed):
          area = cv2.contourArea(contour)
          if(area>10):
            x,y,w,h=cv2.boundingRect(contour)
            cv2.drawContours(img, contoursRed, -1, (0, 255, 0), 5)
            img = cv2.putText(img, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

            cv2.imshow('Contours', img)


        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\RedMaskNumber.txt', "w")
        f.writelines("Number of Red Pieces = " + str(len(contoursRed)))
        f.close()

    # GREEN
    elif cor=='verde':
        with open(r'C:\Users\Samuel\Desktop\Interface\GreenMask.txt') as f:
            contentsGreen = f.read()
            f.close()

        xGreen = contentsGreen.split()
        str(xGreen)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        LowerRegionGreen = np.array([xGreen[0], xGreen[1], xGreen[2]], np.uint8)
        upperRegionGreen = np.array([xGreen[3], xGreen[4], xGreen[5]], np.uint8)
        ObjectGreen = cv2.inRange(hsv, LowerRegionGreen, upperRegionGreen)
        ObjectGreen = cv2.resize(ObjectGreen, (900, 600))
        cv2.imshow("Masking", ObjectGreen)  # em vez de object, res_red
        edgesGreen = cv2.Canny(ObjectGreen, 100, 200)
        cv2.imshow("Edges", edgesGreen)
        contoursGreen, hierarchyGreen = cv2.findContours(edgesGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of green pieces= " + str(len(contoursGreen)))

        contoursGreen, hierarchyGreen = cv2.findContours(edgesGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of green pieces= " + str(len(contoursGreen)))

        for pic, contour in enumerate(contoursGreen):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursGreen, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)


        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\GreenMaskNumber.txt', "w")
        f.writelines("Number of Green Pieces = " + str(len(contoursGreen)))
        f.close()

    #DARK BLUE
    elif cor=='azul escuro':
        with open(r'C:\Users\Samuel\Desktop\Interface\DarkBlueMask.txt') as f:
            contentsDarkBlue = f.read()
            f.close()

        xDarkBlue = contentsDarkBlue.split()
        str(xDarkBlue)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        print('Low Dark Blue Range => [' + xDarkBlue[0] + ', ' + xDarkBlue[1] + ', ' + xDarkBlue[2] + ']')
        print('High Dark Blue Range => [' + xDarkBlue[3] + ', ' + xDarkBlue[4] + ', ' + xDarkBlue[5] + ']')
        LowerRegionDarkBlue = np.array([xDarkBlue[0], xDarkBlue[1], xDarkBlue[2]], np.uint8)
        upperRegionDarkBlue = np.array([xDarkBlue[3], xDarkBlue[4], xDarkBlue[5]], np.uint8)
        ObjectDarkBlue = cv2.inRange(hsv, LowerRegionDarkBlue, upperRegionDarkBlue)
        ObjectDarkBlue = cv2.resize(ObjectDarkBlue, (900, 600))
        cv2.imshow("Masking", ObjectDarkBlue)  # em vez de object, res_red
        edgesDarkBlue = cv2.Canny(ObjectDarkBlue, 100, 200)
        cv2.imshow("Edges", edgesDarkBlue)
        contoursDarkBlue, hierarchyDarkBlue = cv2.findContours(edgesDarkBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of dark blue pieces= " + str(len(contoursDarkBlue)))

        contoursDarkBlue, hierarchyDarkBlue = cv2.findContours(edgesDarkBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of dark blue pieces= " + str(len(contoursDarkBlue)))

        for pic, contour in enumerate(contoursDarkBlue):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursDarkBlue, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Dark Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\DarkBlueMaskNumber.txt', "w")
        f.writelines("Number of Dark Blue Pieces = " + str(len(contoursDarkBlue)))
        f.close()

    #Orange
    elif cor=='laranja':
        with open(r'C:\Users\Samuel\Desktop\Interface\OrangeMask.txt') as f:
            contentsOrange = f.read()
            f.close()

        xOrange = contentsOrange.split()
        str(xOrange)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        LowerRegionOrange = np.array([xOrange[0], xOrange[1], xOrange[2]], np.uint8)
        upperRegionOrange = np.array([xOrange[3], xOrange[4], xOrange[5]], np.uint8)
        ObjectOrange = cv2.inRange(hsv, LowerRegionOrange, upperRegionOrange)
        ObjectOrange = cv2.resize(ObjectOrange, (900, 600))
        cv2.imshow("Masking", ObjectOrange)  # em vez de object, res_red
        edgesOrange = cv2.Canny(ObjectOrange, 100, 200)
        cv2.imshow("Edges", edgesOrange)
        contoursOrange, hierarchyOrange = cv2.findContours(edgesOrange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of orange pieces= " + str(len(contoursOrange)))

        for pic, contour in enumerate(contoursOrange):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursOrange, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Orange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\OrangeMaskNumber.txt', "w")
        f.writelines("Number of Orange Pieces = " + str(len(contoursOrange)))
        f.close()

        # PINK
    elif cor == 'rosa':
        with open(r'C:\Users\Samuel\Desktop\Interface\PinkMask.txt') as f:
            contentsPink = f.read()
            f.close()

        xPink = contentsPink.split()
        str(xPink)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        LowerRegionPink = np.array([xPink[0], xPink[1], xPink[2]], np.uint8)
        upperRegionPink = np.array([xPink[3], xPink[4], xPink[5]], np.uint8)
        ObjectPink = cv2.inRange(hsv, LowerRegionPink, upperRegionPink)
        ObjectPink = cv2.resize(ObjectPink, (900, 600))
        cv2.imshow("Masking", ObjectPink)  # em vez de object, res_red
        edgesPink = cv2.Canny(ObjectPink, 100, 200)
        cv2.imshow("Edges", edgesPink)
        contoursPink, hierarchyPink = cv2.findContours(edgesPink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of Pink pieces= " + str(len(contoursPink)))

        for pic, contour in enumerate(contoursPink):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursPink, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Pink", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\PinkMaskNumber.txt', "w")
        f.writelines("Number of Pink Pieces = " + str(len(contoursPink)))
        f.close()

    #ROXO
    elif cor == 'roxo':
        with open(r'C:\Users\Samuel\Desktop\Interface\PurpleMask.txt') as f:
            contentsPurple = f.read()
            f.close()

        xPurple = contentsPurple.split()
        str(xPurple)
        print('Cor disponível')
        print('Máscara definida pelo user indicada abaixo')
        LowerRegionPurple = np.array([xPurple[0], xPurple[1], xPurple[2]], np.uint8)
        upperRegionPurple = np.array([xPurple[3], xPurple[4], xPurple[5]], np.uint8)
        ObjectPurple = cv2.inRange(hsv, LowerRegionPurple, upperRegionPurple)
        ObjectPurple = cv2.resize(ObjectPurple, (900, 600))
        cv2.imshow("Masking", ObjectPurple)  # em vez de object, res_red
        edgesPurple = cv2.Canny(ObjectPurple, 100, 200)
        cv2.imshow("Edges", edgesPurple)
        contoursPurple, hierarchyPurple = cv2.findContours(edgesPurple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of Purple pieces= " + str(len(contoursPurple)))

        for pic, contour in enumerate(contoursPurple):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursPurple, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Purple", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\PurpleMaskNumber.txt', "w")
        f.writelines("Number of Purple Pieces = " + str(len(contoursPurple)))
        f.close()

    #TODOS
    elif cor == 'todas':
        #ROSA
        with open(r'C:\Users\Samuel\Desktop\Interface\PinkMask.txt') as f:
            contentsPink = f.read()
            f.close()

        xPink = contentsPink.split()
        LowerRegionPink = np.array([xPink[0], xPink[1], xPink[2]], np.uint8)
        upperRegionPink = np.array([xPink[3], xPink[4], xPink[5]], np.uint8)
        ObjectPink = cv2.inRange(hsv, LowerRegionPink, upperRegionPink)
        ObjectPink = cv2.resize(ObjectPink, (900, 600))
        cv2.imshow("Masking", ObjectPink)  # em vez de object, res_red
        edgesPink = cv2.Canny(ObjectPink, 100, 200)
        cv2.imshow("Edges", edgesPink)
        contoursPink, hierarchyPink = cv2.findContours(edgesPink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of Pink pieces= " + str(len(contoursPink)))

        for pic, contour in enumerate(contoursPink):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursPink, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Pink", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\PinkMaskNumber.txt', "w")
        f.writelines("Number of Pink Pieces = " + str(len(contoursPink)))
        f.close()

        #Yellow
        with open(r'C:\Users\Samuel\Desktop\Interface\YellowMask.txt') as f:
            contentsYellow = f.read()
            f.close()

        xYellow = contentsYellow.split()
        LowerRegionYellow = np.array([xYellow[0], xYellow[1], xYellow[2]], np.uint8)
        upperRegionYellow = np.array([xYellow[3], xYellow[4], xYellow[5]], np.uint8)
        ObjectYellow = cv2.inRange(hsv, LowerRegionYellow, upperRegionYellow)
        ObjectYellow = cv2.resize(ObjectYellow, (900, 600))
        cv2.imshow("Masking", ObjectYellow)  # em vez de object, res_red
        edgesYellow = cv2.Canny(ObjectYellow, 100, 200)
        cv2.imshow("Edges", edgesYellow)
        contoursYellow, hierarchyYellow = cv2.findContours(edgesYellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of yellow pieces= " + str(len(contoursYellow)))

        for pic, contour in enumerate(contoursYellow):
          area = cv2.contourArea(contour)
          if(area>2):
            x,y,w,h=cv2.boundingRect(contour)
            cv2.drawContours(img, contoursYellow, -1, (0, 255, 0), 5)
            img = cv2.putText(img, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

            cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\yellowMaskNumber.txt', "w")
        f.writelines("Number of Yellow Pieces = " + str(len(contoursYellow)))
        f.close()

        #ORANGE
        with open(r'C:\Users\Samuel\Desktop\Interface\OrangeMask.txt') as f:
            contentsOrange = f.read()
            f.close()


        xOrange = contentsOrange.split()
        LowerRegionOrange = np.array([xOrange[0], xOrange[1], xOrange[2]], np.uint8)
        upperRegionOrange = np.array([xOrange[3], xOrange[4], xOrange[5]], np.uint8)
        ObjectOrange = cv2.inRange(hsv, LowerRegionOrange, upperRegionOrange)
        ObjectOrange = cv2.resize(ObjectOrange, (900, 600))
        cv2.imshow("Masking", ObjectOrange)  # em vez de object, res_red
        edgesOrange = cv2.Canny(ObjectOrange, 100, 200)
        cv2.imshow("Edges", edgesOrange)
        contoursOrange, hierarchyOrange = cv2.findContours(edgesOrange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of orange pieces= " + str(len(contoursOrange)))

        for pic, contour in enumerate(contoursOrange):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursOrange, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Orange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\OrangeMaskNumber.txt', "w")
        f.writelines("Number of Orange Pieces = " + str(len(contoursOrange)))
        f.close()

        #green
        with open(r'C:\Users\Samuel\Desktop\Interface\GreenMask.txt') as f:
            contentsGreen = f.read()
            f.close()

        xGreen = contentsGreen.split()
        LowerRegionGreen = np.array([xGreen[0], xGreen[1], xGreen[2]], np.uint8)
        upperRegionGreen = np.array([xGreen[3], xGreen[4], xGreen[5]], np.uint8)
        ObjectGreen = cv2.inRange(hsv, LowerRegionGreen, upperRegionGreen)
        ObjectGreen = cv2.resize(ObjectGreen, (900, 600))
        cv2.imshow("Masking", ObjectGreen)  # em vez de object, res_red
        edgesGreen = cv2.Canny(ObjectGreen, 100, 200)
        cv2.imshow("Edges", edgesGreen)

        contoursGreen, hierarchyGreen = cv2.findContours(edgesGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of green pieces= " + str(len(contoursGreen)))

        for pic, contour in enumerate(contoursGreen):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursGreen, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)


        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\GreenMaskNumber.txt', "w")
        f.writelines("Number of Green Pieces = " + str(len(contoursGreen)))
        f.close()

        #RED
        with open(r'C:\Users\Samuel\Desktop\Interface\RedMask.txt') as f:
            contentsRed = f.read()
            f.close()

        xRed = contentsRed.split()
        LowerRegionRed = np.array([xRed[0], xRed[1], xRed[2]], np.uint8)
        upperRegionRed = np.array([xRed[3], xRed[4], xRed[5]], np.uint8)
        ObjectRed = cv2.inRange(hsv, LowerRegionRed, upperRegionRed)
        ObjectRed = cv2.resize(ObjectRed, (900, 600))
        cv2.imshow("Masking", ObjectRed)  # em vez de object, res_red
        edgesRed = cv2.Canny(ObjectRed, 100, 200)
        cv2.imshow("Edges", edgesRed)

        contoursRed, hierarchyRed = cv2.findContours(edgesRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of red pieces= " + str(len(contoursRed)))

        for pic, contour in enumerate(contoursRed):
          area = cv2.contourArea(contour)
          if(area>10):
            x,y,w,h=cv2.boundingRect(contour)
            cv2.drawContours(img, contoursRed, -1, (0, 255, 0), 5)
            img = cv2.putText(img, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

            cv2.imshow('Contours', img)


        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\RedMaskNumber.txt', "w")
        f.writelines("Number of Red Pieces = " + str(len(contoursRed)))
        f.close()

        # ROXO
        with open(r'C:\Users\Samuel\Desktop\Interface\PurpleMask.txt') as f:
            contentsPurple = f.read()
            f.close()

        xPurple = contentsPurple.split()
        str(xPurple)
        LowerRegionPurple = np.array([xPurple[0], xPurple[1], xPurple[2]], np.uint8)
        upperRegionPurple = np.array([xPurple[3], xPurple[4], xPurple[5]], np.uint8)
        ObjectPurple = cv2.inRange(hsv, LowerRegionPurple, upperRegionPurple)
        ObjectPurple = cv2.resize(ObjectPurple, (900, 600))
        cv2.imshow("Masking", ObjectPurple)  # em vez de object, res_red
        edgesPurple = cv2.Canny(ObjectPurple, 100, 200)
        cv2.imshow("Edges", edgesPurple)
        contoursPurple, hierarchyPurple = cv2.findContours(edgesPurple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of Purple pieces= " + str(len(contoursPurple)))

        for pic, contour in enumerate(contoursPurple):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursPurple, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Purple", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\PurpleMaskNumber.txt', "w")
        f.writelines("Number of Purple Pieces = " + str(len(contoursPurple)))
        f.close()


        # DARK BLUE
        with open(r'C:\Users\Samuel\Desktop\Interface\DarkBlueMask.txt') as f:
            contentsDarkBlue = f.read()
            f.close()

        xDarkBlue = contentsDarkBlue.split()
        LowerRegionDarkBlue = np.array([xDarkBlue[0], xDarkBlue[1], xDarkBlue[2]], np.uint8)
        upperRegionDarkBlue = np.array([xDarkBlue[3], xDarkBlue[4], xDarkBlue[5]], np.uint8)
        ObjectDarkBlue = cv2.inRange(hsv, LowerRegionDarkBlue, upperRegionDarkBlue)
        ObjectDarkBlue = cv2.resize(ObjectDarkBlue, (900, 600))
        cv2.imshow("Masking", ObjectDarkBlue)  # em vez de object, res_red
        edgesDarkBlue = cv2.Canny(ObjectDarkBlue, 100, 200)
        cv2.imshow("Edges", edgesDarkBlue)
        contoursDarkBlue, hierarchyDarkBlue = cv2.findContours(edgesDarkBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("Number of dark blue pieces= " + str(len(contoursDarkBlue)))

        for pic, contour in enumerate(contoursDarkBlue):
            area = cv2.contourArea(contour)
            if (area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.drawContours(img, contoursDarkBlue, -1, (0, 255, 0), 5)
                img = cv2.putText(img, "Dark Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4, cv2.LINE_AA)

                cv2.imshow('Contours', img)

        f = open(r'C:\Users\Samuel\Desktop\pythonProject1\DarkBlueMaskNumber.txt', "w")
        f.writelines("Number of Dark Blue Pieces = " + str(len(contoursDarkBlue)))
        f.close()

    else:
        print("Cor indisponível, adicionar com as track bars")

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
