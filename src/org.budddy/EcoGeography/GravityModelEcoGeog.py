def gravityModelTrade(p2, d):
    k = 15
    tGDPofUS = 20936.6
    p1 = tGDPofUS

    return k * ((p1 * p2) / d)


print("Ecuador Spatial Interaction is: " + str(gravityModelTrade(98.80801, 2696.915833759588)))
print("Egypt Spatial Interaction is: " + str(gravityModelTrade(363.06925, 5806.53048371437)))
