import cv2
from Refill import Refill
from capture import capture_handler
from action import dragAndDrop, doubleClick, click
from pathConfig import (
    single_coin_path,
    double_coin_path,
    quadra_coin_path,
    go_path,
    screenshot_path,
    comparing_current_path,
    comparing_compare_path,
)
import numpy as np

auto_refill = Refill()


coinImage = cv2.imread(single_coin_path, cv2.IMREAD_GRAYSCALE)
coinImage2 = cv2.imread(double_coin_path, cv2.IMREAD_GRAYSCALE)
coinImage4 = cv2.imread(quadra_coin_path, cv2.IMREAD_GRAYSCALE)

goImage = cv2.imread(go_path, cv2.IMREAD_GRAYSCALE)


def checkGoButtonAvaialble():
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)
    goResult = cv2.matchTemplate(goImage, screenshot, cv2.TM_CCOEFF_NORMED)
    min_val, max_val_go, min_loc, max_loc = cv2.minMaxLoc(goResult)
    thresh_hold = 0.7
    if max_val_go >= thresh_hold:
        loc = np.where(goResult >= thresh_hold)
        for pt in zip(*loc[::-1]):
            goButton = (
                pt[0],
                pt[1],
            )
            click(goButton)


def checkCoin(currentImage, box):
    coinResult = cv2.matchTemplate(currentImage, coinImage, cv2.TM_CCOEFF_NORMED)
    coin2Result = cv2.matchTemplate(currentImage, coinImage2, cv2.TM_CCOEFF_NORMED)
    coin4Result = cv2.matchTemplate(currentImage, coinImage4, cv2.TM_CCOEFF_NORMED)

    coin4Result = cv2.matchTemplate(currentImage, coinImage4, cv2.TM_CCOEFF_NORMED)

    min_val, max_val_coin, min_loc, max_loc = cv2.minMaxLoc(coinResult)
    min_val, max_val_coin_2, min_loc, max_loc = cv2.minMaxLoc(coin2Result)
    min_val, max_val_coin_4, min_loc, max_loc = cv2.minMaxLoc(coin4Result)

    thresh_hold = 0.5
    element_thresh_hold = 0.8
    if (
        max_val_coin >= thresh_hold
        or max_val_coin_2 >= thresh_hold
        or max_val_coin_4 >= thresh_hold
    ):
        top, left, right, bottom = box
        currentImageCenterWidth = (left + right) // 2
        currentImageCenterHeight = (top + bottom) // 2
        doubleClick((currentImageCenterWidth, currentImageCenterHeight))
        return True

    return False


def swap(rows, cols):
    check_go = 1
    for row in rows:
        left, right = row
        for col in cols:
            top, bottom = col
            if (
                left in [450, 540, 640]
                and right in [525, 615, 715]
                and top == 1175
                and bottom == 1241
            ):
                continue

            save = check_go == 10
            im = capture_handler(save)
            currentImage = im.crop((left, top, right, bottom))
            currentImage.save(comparing_current_path)
            image1 = cv2.imread(comparing_current_path, cv2.IMREAD_GRAYSCALE)

            for row in rows:
                leftCompare, rightCompare = row
                break_outer = False
                for col in cols:
                    topCompare, bottomCompare = col

                    if check_go >= 20:
                        check_go = 0
                        try:
                            checkGoButtonAvaialble()
                        except:
                            print("")

                    check_go = check_go + 1

                    if (
                        leftCompare == left
                        and rightCompare == right
                        and topCompare == top
                        and bottomCompare == bottom
                    ):
                        continue

                    if checkCoin(image1, box=(top, left, right, bottom)):
                        break_outer = True
                        continue

                    compareImage = im.crop(
                        (leftCompare, topCompare, rightCompare, bottomCompare)
                    )

                    compareImage.save(comparing_compare_path)
                    image2 = cv2.imread(comparing_compare_path, cv2.IMREAD_GRAYSCALE)

                    result = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)

                    # Get the best match location
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    match_percent = str(round(max_val * 100)) + "%"

                    # print("Image match rate = " + match_percent)

                    # Check if the best match is above a certain threshold
                    thresh_hold = 0.35
                    if max_val >= thresh_hold:
                        currentImageCenterWidth = (left + right) // 2
                        currentImageCenterHeight = (top + bottom) // 2

                        compareImageCenterWidth = (leftCompare + rightCompare) // 2
                        compareImageCenterHeight = (topCompare + bottomCompare) // 2
                        try:
                            dragAndDrop(
                                (currentImageCenterWidth, currentImageCenterHeight),
                                (compareImageCenterWidth, compareImageCenterHeight),
                            )

                            auto_refill.execute()
                            break_outer = True
                            break
                        except:
                            continue

                if break_outer == True:
                    break
