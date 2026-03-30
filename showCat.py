"""512x512 가상 고양이 이미지 생성 및 표시"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_cat(ax, color='#FF8C00', eye_color='#2E8B57', name='Cat'):
    """가상의 고양이를 도형으로 그린다."""
    ax.set_xlim(0, 512)
    ax.set_ylim(0, 512)
    ax.set_aspect('equal')
    ax.set_facecolor('#2b2b2b')
    ax.axis('off')

    # 외곽선 색상 (메인 색상 어둡게)
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    ec = f'#{max(r-50,0):02X}{max(g-50,0):02X}{max(b-50,0):02X}'

    # 몸통
    body = patches.Ellipse((256, 160), 200, 160, fc=color, ec=ec, lw=2)
    ax.add_patch(body)

    # 머리
    head = patches.Circle((256, 320), 100, fc=color, ec=ec, lw=2)
    ax.add_patch(head)

    # 왼쪽 귀
    ear_l = patches.Polygon([[190, 390], [160, 460], [230, 410]], closed=True,
                            fc=color, ec=ec, lw=2)
    ax.add_patch(ear_l)
    ear_l_in = patches.Polygon([[195, 395], [175, 445], [225, 408]], closed=True,
                               fc='#FFB6C1')
    ax.add_patch(ear_l_in)

    # 오른쪽 귀
    ear_r = patches.Polygon([[322, 390], [352, 460], [282, 410]], closed=True,
                            fc=color, ec=ec, lw=2)
    ax.add_patch(ear_r)
    ear_r_in = patches.Polygon([[317, 395], [337, 445], [287, 408]], closed=True,
                               fc='#FFB6C1')
    ax.add_patch(ear_r_in)

    # 눈 (왼쪽)
    eye_l_w = patches.Ellipse((220, 330), 35, 30, fc='white', ec='#333', lw=1.5)
    ax.add_patch(eye_l_w)
    eye_l_iris = patches.Circle((222, 332), 10, fc=eye_color)
    ax.add_patch(eye_l_iris)
    eye_l_pupil = patches.Ellipse((223, 333), 6, 12, fc='black')
    ax.add_patch(eye_l_pupil)
    eye_l_hl = patches.Circle((218, 336), 3, fc='white')
    ax.add_patch(eye_l_hl)

    # 눈 (오른쪽)
    eye_r_w = patches.Ellipse((292, 330), 35, 30, fc='white', ec='#333', lw=1.5)
    ax.add_patch(eye_r_w)
    eye_r_iris = patches.Circle((290, 332), 10, fc=eye_color)
    ax.add_patch(eye_r_iris)
    eye_r_pupil = patches.Ellipse((289, 333), 6, 12, fc='black')
    ax.add_patch(eye_r_pupil)
    eye_r_hl = patches.Circle((286, 336), 3, fc='white')
    ax.add_patch(eye_r_hl)

    # 코
    nose = patches.Polygon([[256, 300], [248, 290], [264, 290]], closed=True,
                           fc='#FF69B4', ec='#CC5490', lw=1)
    ax.add_patch(nose)

    # 입
    ax.plot([256, 240, 235], [290, 275, 270], color='#333', lw=1.5)
    ax.plot([256, 272, 277], [290, 275, 270], color='#333', lw=1.5)

    # 수염
    for dy in [-5, 0, 5]:
        ax.plot([155, 215], [295 + dy, 300 + dy], color='#333', lw=1)
        ax.plot([297, 357], [300 + dy, 295 + dy], color='#333', lw=1)

    # 앞발
    paw_l = patches.Ellipse((200, 100), 50, 35, fc=color, ec=ec, lw=2)
    ax.add_patch(paw_l)
    paw_r = patches.Ellipse((312, 100), 50, 35, fc=color, ec=ec, lw=2)
    ax.add_patch(paw_r)

    # 발바닥 패드
    for cx in [200, 312]:
        pad = patches.Circle((cx, 97), 8, fc='#FFB6C1')
        ax.add_patch(pad)
        for dx in [-10, 0, 10]:
            toe = patches.Circle((cx + dx, 110), 4, fc='#FFB6C1')
            ax.add_patch(toe)

    # 꼬리
    theta = np.linspace(0, np.pi * 0.8, 50)
    tail_x = 356 + 60 * np.sin(theta)
    tail_y = 120 + 80 * (theta / theta.max())
    ax.plot(tail_x, tail_y, color=color, lw=8, solid_capstyle='round')
    ax.plot(tail_x, tail_y, color=ec, lw=2, solid_capstyle='round')

    # 줄무늬
    for y_off in [0, 25, 50]:
        stripe = patches.Arc((256, 340 + y_off), 60, 15, angle=0,
                             theta1=0, theta2=180, ec=ec, lw=2)
        ax.add_patch(stripe)

    ax.set_title(name, fontsize=11, color='white', pad=5)


def main():
    cats = [
        {'color': '#FF8C00', 'eye_color': '#2E8B57', 'name': 'Orange'},
        {'color': '#808080', 'eye_color': '#FFD700', 'name': 'Gray'},
        {'color': '#F5F5DC', 'eye_color': '#4169E1', 'name': 'White'},
        {'color': '#8B4513', 'eye_color': '#90EE90', 'name': 'Brown'},
        {'color': '#2F2F2F', 'eye_color': '#FF6347', 'name': 'Black'},
    ]

    # 전체 512x512 픽셀, 고양이 5마리 배치
    dpi = 100
    fig_size = 512 / dpi
    fig, axes = plt.subplots(1, 5, figsize=(fig_size, fig_size), dpi=dpi)
    fig.patch.set_facecolor('#2b2b2b')

    for ax, cat in zip(axes, cats):
        draw_cat(ax, **cat)

    plt.subplots_adjust(left=0.01, right=0.99, top=0.92, bottom=0.01, wspace=0.05)
    plt.show()


if __name__ == '__main__':
    main()
