---
title: Design guide
slug: user-interface/design-guide
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:21:50 GMT+0000 (Coordinated Universal Time)
---

# Flipper One screen colors
<img width="941" height="616" alt="image" src="https://github.com/user-attachments/assets/c741ddab-59a2-4682-9898-1d8594b14662" />

Despite the fact taht, Flipper one uses monocrome 6-bit screen with 62 shades of gray. We are going to use only 5 of them. To keep UI element contrast and distiguishable.

| ![](https://placehold.co/24x24/000000/000000.png) | ![](https://placehold.co/24x24/696969/696969.png) | ![](https://placehold.co/24x24/AAAAAA/AAAAAA.png) | ![](https://placehold.co/24x24/CCCCCC/CCCCCC.png) | ![](https://placehold.co/24x24/FFFFFF/FFFFFF.png) |
|---|---|---|---|---|
| `#000000` | `#696969` | `#AAAAAA` | `#CCCCCC` | `#FFFFFF` |

<img width="1660" height="432" alt="image" src="https://github.com/user-attachments/assets/d5f0eae0-119b-4dc9-a090-a0378b0b941c" />


# UI screen for preview

For demo purposes we are using the `#FF8200` in `Multiply` blend mode to imitate Flipper One screen

<img width="1024" height="422" alt="image" src="https://github.com/user-attachments/assets/30f77c24-9653-4fa1-b64a-6d62098be08c" />

# Core components and design constants

## Responcive frame

One of the base components, wich is the foundation of other more complicated UI assets

### Transform Properties:
**Anchor:** Origin point of the componet.
Could be anchored for two axis independantly.
Options for X: `Left, Center, Right`.
Options for Y: `Top, Center, Bottom`

**Position:** Relative coordingates to the parrent componend (e.g. Screen, another responcive frame)
X, Y in pixels. 

**Width and Height:** Component dinmmentions in px. 

Keep in mind that position and dimmentions of the frame could not be decinimal. Only round numbers. Decimal number like 110.5 will result sub pixels.

Fill:

<img width="1528" height="544" alt="image" src="https://github.com/user-attachments/assets/66ce86c7-5ed9-4106-a50b-c61cf208d574" />



# Round corners
<img width="1660" height="538" alt="image" src="https://github.com/user-attachments/assets/129733b1-71d1-410a-8295-aab8039cb5b7" />




